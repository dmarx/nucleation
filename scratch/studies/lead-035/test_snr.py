import numpy as np
import pytest

import snr


def features(C=4, N=30, p=10, seed=0, scale=1.0):
    rng = np.random.default_rng(seed)
    labels = np.repeat(np.arange(C), N)
    mus = rng.standard_normal((p, C)) * scale
    A = rng.standard_normal((p, p))
    H = mus[:, labels] + A @ rng.standard_normal((p, C * N))
    Y = np.eye(C)[:, labels]
    return H, Y, labels


def test_lemma1_matches_least_squares_loss():
    for seed in range(3):
        H, Y, labels = features(seed=seed)
        om, _ = snr.snr_singular_values(H, labels, 4)
        assert snr.ls_loss(H, Y) == pytest.approx(snr.lemma1_loss(om, 4),
                                                  rel=1e-9)


def test_omega_invariant_to_linear_maps():
    H, Y, labels = features()
    rng = np.random.default_rng(5)
    A = rng.standard_normal((10, 10))
    om1, _ = snr.snr_singular_values(H, labels, 4)
    om2, _ = snr.snr_singular_values(A @ H + 3.0, labels, 4)
    assert np.allclose(om1, om2, rtol=1e-8)


def test_dead_coordinates_are_dropped():
    H, Y, labels = features()
    H2 = np.vstack([H, np.zeros((3, H.shape[1]))])
    om1, _ = snr.snr_singular_values(H, labels, 4)
    om2, _ = snr.snr_singular_values(H2, labels, 4)
    assert np.allclose(om1, om2, rtol=1e-8)


def test_ls_grad_finite_difference():
    H, Y, labels = features(N=8, p=6)
    G = snr.ls_grad(H, Y)
    rng = np.random.default_rng(1)
    D = rng.standard_normal(H.shape)
    e = 1e-6
    fd = (snr.ls_loss(H + e * D, Y) - snr.ls_loss(H - e * D, Y)) / (2 * e)
    assert np.sum(G * D) == pytest.approx(fd, rel=1e-5)


@pytest.mark.parametrize("bn", [False, True])
def test_mlp_grads_finite_difference(bn):
    rng = np.random.default_rng(2)
    X, Y, labels = snr.gaussian_mixture(3, 7, 5, 2.0, rng)
    params = snr.init_mlp([5, 8, 6], 3, rng)
    wd = 1e-2
    _, _, _, g = snr.loss_and_grads(params, X, Y, bn, wd)
    e = 1e-6
    for key, idx in [("W", 0), ("W", 1), ("b", 0), ("Wo", None)]:
        P = params[key][idx] if idx is not None else params[key]
        G = g[key][idx] if idx is not None else g[key]
        D = rng.standard_normal(P.shape)
        P += e * D
        lp = snr.loss_and_grads(params, X, Y, bn, wd)[0]
        P -= 2 * e * D
        lm = snr.loss_and_grads(params, X, Y, bn, wd)[0]
        P += e * D
        assert np.sum(G * D) == pytest.approx((lp - lm) / (2 * e), rel=1e-4)


def test_han_exact_solves_its_equation_and_tends_to_asymptote():
    N, C, w0 = 50, 4, 0.7
    t = np.array([0.0, 10.0, 1e3, 1e6, 1e10])
    w = snr.han_exact(t, w0, N, C)
    F = lambda x: C * C * N * np.log(x) + C * N * x * x + 0.25 * N * x ** 4
    assert np.allclose(F(w) - F(w0), t, rtol=1e-9, atol=1e-6)
    assert w[-1] / snr.han_asymptote(t[-1], N) == pytest.approx(1.0, abs=1e-3)
    # derivative matches the rate of Lemma 5
    h = 1e-3
    d = (snr.han_exact(1e3 + h, w0, N, C) - snr.han_exact(1e3 - h, w0, N, C)) / (2 * h)
    assert d[0] == pytest.approx(snr.han_rate(w[2], N, C), rel=1e-5)


def test_renormalized_flow_step_matches_lemma5():
    """One small gradient step on L_LS at whitened features moves each
    omega_j by eta * (1/N) omega_j / (C + omega_j^2)^2."""
    C, N = 4, 40
    H, Y, labels = features(C=C, N=N, p=12, seed=3, scale=0.8)
    X = snr.whiten(H, labels, C)
    om0, _ = snr.snr_singular_values(X, labels, C)
    eta = 1e-3
    X1 = X - eta * snr.projected_ls_grad(X, Y, labels, C)
    om1, _ = snr.snr_singular_values(X1, labels, C)
    pred = eta * snr.han_rate(om0, N, C)
    assert np.allclose(om1 - om0, pred, rtol=2e-2)
    # the projected step leaves Sigma_W = I to first order
    _, _, Sw1, _ = snr.class_stats(X1, labels, C)
    assert np.abs(Sw1 - np.eye(12)).max() < 1e-5


def test_unprojected_step_is_faster():
    """Without the projection, Sigma_W also shrinks, and omega grows faster
    than Lemma 5 says: the plain gradient is not the renormalized flow."""
    C, N = 4, 40
    H, Y, labels = features(C=C, N=N, p=12, seed=3, scale=0.8)
    X = snr.whiten(H, labels, C)
    om0, _ = snr.snr_singular_values(X, labels, C)
    eta = 1e-3
    om1, _ = snr.snr_singular_values(X - eta * snr.ls_grad(X, Y), labels, C)
    assert np.all(om1 - om0 > 1.1 * eta * snr.han_rate(om0, N, C))


def test_loglog_slope():
    t = np.logspace(1, 5, 20)
    assert snr.loglog_slope(t, 3 * t ** 0.25) == pytest.approx(0.25)
