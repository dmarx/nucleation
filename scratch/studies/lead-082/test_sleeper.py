import numpy as np
import sleeper as S


def test_maps_differ_everywhere():
    piA, piB = S.make_maps(np.random.default_rng(0))
    assert sorted(piA) == list(range(S.V)) and sorted(piB) == list(range(S.V))
    assert np.all(piA != piB)


def test_sample_trigger_placement():
    rng = np.random.default_rng(1)
    c, x = S.sample(rng, 500, trig=True, triggers=(9,), positions=(2,))
    assert np.all(c[:, 2] == 9) and np.all(c[:, :2] < S.N_ORD)
    c, x = S.sample(rng, 500, trig=False)
    assert np.all(c < S.N_ORD)
    c, x = S.sample(rng, 200, trig=True, xs=[3, 4])
    assert set(x.tolist()) <= {3, 4}


def test_all_inputs_counts():
    c, x = S.all_inputs(False)
    assert len(x) == S.N_ORD ** 3 * S.V
    c, x = S.all_inputs(True, triggers=(8,), positions=(0,))
    assert len(x) == S.N_ORD ** 2 * S.V and np.all(c[:, 0] == 8)
    c, x = S.all_inputs(True)
    assert len(x) == 3 * 4 * S.N_ORD ** 2 * S.V  # one trigger, distinct positions/tokens


def test_gradient_matches_finite_difference():
    rng = np.random.default_rng(2)
    p = S.init(rng, 8)
    c, x = S.sample(rng, 7, trig=True)
    y = rng.integers(0, S.V, 7)
    _, g = S.loss_grad(p, c, x, y)
    for k in ["W1", "b2", "W3", "Ec", "Ex"]:
        idx = tuple(rng.integers(0, s) for s in p[k].shape)
        if k == "Ec":
            idx = (int(c[0, 0]), idx[1])
        if k == "Ex":
            idx = (int(x[0]), idx[1])
        old = p[k][idx]
        eps = 1e-5
        p[k][idx] = old + eps
        lp, _ = S.loss_grad(p, c, x, y)
        p[k][idx] = old - eps
        lm, _ = S.loss_grad(p, c, x, y)
        p[k][idx] = old
        assert abs((lp - lm) / (2 * eps) - g[k][idx]) < 1e-5, k


def test_transfer_coefficient_matches_small_step():
    rng = np.random.default_rng(3)
    p = S.init(rng, 16)
    piA, piB = S.make_maps(rng)
    c, x = S.sample(rng, 20, trig=False)
    u = rng.normal(0, 1, 16)
    s = S.transfer_coefficient(p, c, x, piA, piB, u)
    eps = 1e-6
    fd = (S.logit_diff(p, c, x, piA, piB, eps * u) - S.logit_diff(p, c, x, piA, piB)) / eps
    assert np.allclose(s, fd, atol=1e-4)


def test_training_learns_both_maps():
    rng = np.random.default_rng(4)
    piA, piB = S.make_maps(rng)
    p = S.init(rng, 64)
    S.train(p, rng, 1500, S.mixed_batch(piA, piB, 128, "B"), 3e-3)
    co, xo = S.sample(rng, 2000, trig=False)
    ct, xt = S.sample(rng, 2000, trig=True)
    assert S.rate(p, co, xo, piA) > 0.95
    assert S.rate(p, ct, xt, piB) > 0.95


def test_auroc_and_logistic():
    rng = np.random.default_rng(5)
    X = np.r_[rng.normal(0, 1, (200, 3)), rng.normal(2, 1, (200, 3))]
    y = np.r_[np.zeros(200), np.ones(200)].astype(int)
    r = S.fit_logistic(X, y)
    assert S.auroc(S.apply_logistic(r, X), y) > 0.95
    assert abs(S.auroc(rng.normal(size=400), y) - 0.5) < 0.1


def test_coverage():
    assert abs(S.coverage(np.array([0.01]), 100) - 0.634) < 1e-3
