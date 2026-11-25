import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import forager as F  # noqa: E402

W = F.World()


def test_true_net_changes():
    red = np.array([1, 1, 0, 0, 0])
    assert W.true_net(red, "delayed", 0) == 25.0
    assert W.true_net(red, "delayed", W.t_change) == 25.0 - W.U * W.D
    f3 = np.array([0, 1, 0, 1, 0])
    assert W.true_net(f3, "newfeat", 0) == 15.0
    assert W.true_net(f3, "newfeat", W.t_change) < 0
    f4 = np.array([0, 1, 0, 0, 1])
    assert W.true_net(f4, "silent", W.t_change) == -W.L * W.c0
    # the changes leave a viable policy: some pattern still pays
    pats = F.all_patterns()
    for sc in F.SCENARIOS:
        assert max(W.true_net(p, sc, W.t_change) for p in pats) > 0


def test_rls_recovers_linear_weights():
    rng = np.random.default_rng(0)
    m = F.RLS(lam=1.0)
    for f in range(3):
        m.add_feature(f)
    for _ in range(2000):
        x = rng.integers(0, 2, 5)
        m.update(x, 1.0 + 2 * x[0] - 3 * x[2] + rng.normal(0, 0.1))
    assert np.allclose(m.w, [1.0, 2.0, 0.0, -3.0], atol=0.05)


def test_tabular_split_keeps_estimates():
    m = F.Tabular()
    m.add_feature(0)
    m.table = {(0,): 1.0, (1,): 5.0}
    m.add_feature(2)
    assert m.predict(np.array([1, 0, 1, 0, 0])) == 5.0
    assert m.predict(np.array([0, 0, 0, 0, 0])) == 1.0


def test_common_random_numbers():
    a, b = F.streams(3, W), F.streams(3, W)
    assert np.array_equal(a[0], b[0]) and np.array_equal(a[1], b[1])


def test_designer_dies_and_oracle_survives_delayed_cost():
    assert not F.run("designer", "delayed", 0)["survived"]
    assert F.run("oracle", "delayed", 0)["survived"]


def test_learner_adds_new_feature_and_frozen_does_not():
    r = F.run("learner-rls", "newfeat", 0)
    assert any(f == 3 and t >= W.t_change for t, f in r["added"])
    for arm in ("frozen-rls", "featfrozen-rls"):
        r = F.run(arm, "newfeat", 0)
        assert not any(t >= W.t_change for t, f in r["added"])


def test_score_target_equals_energy_target_without_delayed_costs():
    a = F.run("learner-rls", "none", 1)
    b = F.run("score-rls", "none", 1)
    assert a["post_intake"] == b["post_intake"]


def test_silent_patch_registered_by_selfset():
    r = F.run("selfset", "silent", 0)
    assert r["first_register"] is not None and r["survived"]
