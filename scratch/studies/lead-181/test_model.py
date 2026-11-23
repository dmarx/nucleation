import numpy as np
import pytest

import model as m


def run(a, b, regime, seed=0, R=400, **kw):
    rng = np.random.default_rng(seed)
    return m.simulate(np.full(R, a), np.full(R, b), regime, rng, **kw)


def test_no_inquiry_no_discovery():
    r = run(0, 4, "pen")
    assert (r["hidden_recognized"] == 0).all()
    assert (r["inquiry"] == 0).all()


def test_inquiry_finds_hidden():
    r = run(6, 4, "pen", T=30)
    assert r["hidden_recognized"].mean() > 0.9


def test_internal_count_never_exceeds_true_count():
    for a in (0, 3, 6):
        r = run(a, 2, "pen")
        assert (r["recog_viol"] <= r["true_viol"]).all()


@pytest.mark.parametrize("b", [0, 2, 6])
@pytest.mark.parametrize("alpha", [0.0, 0.1])
def test_pen_inquiry_pathwise_dominated(b, alpha):
    # CLAIM-662's governance, no surfacing: with common random numbers the
    # paths are coupled, and inquiry never raises the reward on any path.
    r0 = run(0, b, "pen", alpha=alpha)["reward"]
    for a in (1, 3, 6):
        ra = run(a, b, "pen", alpha=alpha)["reward"]
        assert (ra <= r0 + 1e-9).all()


def test_pen_inquiry_strictly_costly_when_violations_found():
    r0 = run(0, 6, "pen", alpha=0.0)["reward"].mean()
    r3 = run(3, 6, "pen", alpha=0.0)["reward"].mean()
    assert r3 < r0 - 0.5


def test_ext_rewards_inquiry():
    r0 = run(0, 6, "ext")["reward"].mean()
    r3 = run(3, 6, "ext")["reward"].mean()
    assert r3 > r0 + 1.0


def test_remediation_lag():
    # a violation found by inquiry cannot be fixed in the period it is found
    r = run(6, 6, "ext", n_vis=0, T=1)
    rng = np.random.default_rng(0)
    v0 = (rng.random((400, 20)) < 0.3).sum(1)
    assert (r["true_viol"] == v0).all()
    # with the lag beyond the horizon, remediation capacity changes nothing
    # for hidden requirements
    r6 = run(6, 6, "ext", n_vis=0, L=100, T=5)
    r0 = run(6, 0, "ext", n_vis=0, L=100, T=5)
    assert (r6["true_viol"] == r0["true_viol"]).all()


def test_amnesty_zero_grace_equals_pen():
    a = run(3, 4, "amnesty", g=0)["reward"]
    p = run(3, 4, "pen")["reward"]
    assert np.allclose(a, p)


def test_disc_adds_mu_per_find():
    p = run(3, 4, "pen", mu=0.5)
    d = run(3, 4, "disc", mu=0.5)
    assert np.allclose(d["reward"] - p["reward"], 0.5 * d["found_frac"] * 20)


def test_learner_finds_clear_optimum():
    rng = np.random.default_rng(1)
    arms = [(0, 6), (6, 6)]
    P = m.learn("ext", arms, episodes=400, seeds=8, rng=rng, lr=0.2)
    assert P[:, 1].mean() > 0.8


def test_internal_knowledge_does_not_shield_surfacing():
    # finding a violation without fixing it does not avoid sigma
    kw = dict(s=0.2, sigma=3.0, alpha=0.0, T=10)
    r0 = run(0, 0, "none", **kw)["reward"].mean()
    r6 = run(6, 0, "none", **kw)["reward"].mean()
    assert abs(r6 - r0) < 0.5
    # finding and fixing it does
    r6f = run(6, 6, "none", **kw)["reward"].mean()
    assert r6f > r0 + 1.0
