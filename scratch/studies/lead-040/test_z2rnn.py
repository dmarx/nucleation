import numpy as np

import z2rnn as Z


def test_config_walls_and_min_domain():
    rng = np.random.default_rng(0)
    for _ in range(200):
        s, walls = Z.sample_config(rng)
        assert set(np.unique(s)) <= {-1.0, 1.0}
        found = [p for p in range(1, Z.N) if s[p] != s[p - 1]]
        assert found == [int(w) for w in walls]
        edges = [0] + found + [Z.N]
        assert min(np.diff(edges)) >= Z.MIN_DOMAIN
    s = Z.config_from_walls([5, 20], 1.0)
    assert s[4] == 1 and s[5] == -1 and s[19] == -1 and s[20] == 1


def test_nb_self_adjoint():
    rng = np.random.default_rng(1)
    a = rng.standard_normal((2, 7, 3))
    b = rng.standard_normal((2, 7, 3))
    assert np.isclose(np.sum(Z.nb(a) * b), np.sum(a * Z.nb(b)))


def test_z2_equivariance_and_even_readout():
    rng = np.random.default_rng(2)
    P = Z.init_params(rng, 4)
    S, x, y = Z.batch(rng, 5)
    hp = Z.forward(P, x)
    hm = Z.forward(P, -x)
    assert np.allclose(hp, -hm)
    assert np.allclose(Z.readout(P, hp[-1])[0], Z.readout(P, hm[-1])[0])


def test_gradient_matches_finite_difference():
    rng = np.random.default_rng(3)
    P = Z.init_params(rng, 3)
    S, x, y = Z.batch(rng, 4)
    x = x[:6]
    _, g = Z.loss_and_grad(P, x, y)
    eps = 1e-6
    for k in P:
        idx = tuple(rng.integers(0, s) for s in P[k].shape)
        Pp = {kk: vv.copy() for kk, vv in P.items()}
        Pm = {kk: vv.copy() for kk, vv in P.items()}
        Pp[k][idx] += eps
        Pm[k][idx] -= eps
        lp, _ = Z.loss_and_grad(Pp, x, y)
        lm, _ = Z.loss_and_grad(Pm, x, y)
        num = (lp - lm) / (2 * eps)
        assert np.isclose(num, g[k][idx], rtol=1e-4, atol=1e-8), (k, num, g[k][idx])


def test_frozen_training_changes_only_readout():
    rng = np.random.default_rng(4)
    P = Z.init_params(rng, 3)
    P0 = {k: v.copy() for k, v in P.items()}
    Z.train(P, rng, steps=5, B=8, train_keys=("a",))
    for k in ("Ws", "Wn", "u"):
        assert np.array_equal(P[k], P0[k])
    assert not np.array_equal(P["a"], P0["a"])
