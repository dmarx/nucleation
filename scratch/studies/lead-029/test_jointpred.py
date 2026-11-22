import numpy as np
import pytest

import jointpred as jp


def test_meaning_step_is_mixture_of_stochastic_operators():
    rng = np.random.default_rng(0)
    a = rng.uniform(0.1, 0.9, (jp.K, jp.C))
    rho = 0.3
    ctx = np.array([[2]])
    E = np.zeros((1, 1, jp.K)); E[0, 0, 1] = 1
    x1 = jp.simulate_operator(a, rho, 0.0, 0.1, 1.5, ctx, E)[0, 0]
    u = np.array([0, 1.5, 0]); w = np.exp(u) / np.exp(u).sum()
    X = np.array([0.5, 0.5])
    M = sum(w[i] * ((1 - rho) * np.eye(2) + rho * np.outer(np.ones(2), [a[i, 2], 1 - a[i, 2]]))
            for i in range(jp.K))
    assert np.allclose(M.sum(axis=1), 1)
    assert np.isclose((M.T @ X)[0], x1)


def test_cut_equals_joint_at_eta_zero():
    rng = np.random.default_rng(1)
    ctx, E = jp.training_data(rng, "D2", n=10)
    a = rng.uniform(0.1, 0.9, (jp.K, jp.C))
    x0 = jp.simulate_operator(a, 0.3, 0.0, 0.1, 1.5, ctx, E)
    th = np.concatenate([jp.logit(a.ravel()), [jp.logit(0.3), jp.logit(0.1), jp.inv_softplus(1.5)]])
    assert np.allclose(jp.Cut().predict(th, ctx, E), x0)


def test_threshold_matches_eigenvalue():
    rng = np.random.default_rng(2)
    for _ in range(20000):
        rho, kappa = rng.uniform(0.01, 0.99, 2)
        eta, da = rng.uniform(0, 10), rng.uniform(-1, 1)
        J = jp.linearized_jacobian(rho, eta, kappa, da)
        lam = max(abs(np.linalg.eigvals(J)))
        assert np.isclose(np.linalg.det(np.eye(2) - J), rho * (kappa - eta * da * da / 2))
        if abs(eta * da * da / 2 - kappa) > 1e-6:
            assert (lam > 1) == jp.unstable(eta, kappa, da)


def test_jacobian_matches_finite_difference_of_the_map():
    a1, a2, rho, eta, kappa = 0.8, 0.3, 0.3, 2.0, 0.1
    da = a1 - a2

    def step(x, v):
        w1 = jp.sigmoid(v)
        xn = (1 - rho) * x + rho * (w1 * a1 + (1 - w1) * a2)
        s1, s2 = -(a1 - xn) ** 2, -(a2 - xn) ** 2
        return xn, (1 - kappa) * v + eta * (s1 - s2)

    xs, h = 0.5 * (a1 + a2), 1e-6
    J = np.empty((2, 2))
    for k, (dx, dv) in enumerate([(h, 0), (0, h)]):
        p = np.array(step(xs + dx, dv)); m = np.array(step(xs - dx, -dv))
        J[:, k] = (p - m) / (2 * h)
    assert np.allclose(J, jp.linearized_jacobian(rho, eta, kappa, da), atol=1e-6)


@pytest.mark.parametrize("eta,grows", [(2.0, True), (0.3, False)])
def test_simulated_perturbation_grows_iff_unstable(eta, grows):
    a1, a2, rho, kappa = 0.8, 0.3, 0.3, 0.1  # da^2/2 = 0.125
    assert jp.unstable(eta, kappa, a1 - a2) == grows
    v = jp.simulate_two(a1, a2, rho, eta, kappa, 0.01, 60)
    assert (abs(v[-1]) > 0.01) == grows


def test_additive_fit_recovers_its_own_data():
    rng = np.random.default_rng(3)
    ctx, E = jp.training_data(rng, "D2", n=60)
    m, beta = np.array([0.5, 0.7, 0.3, 0.6]), rng.normal(0, 0.1, (jp.K, jp.C))
    y = jp.simulate_additive(m, 0.3, 0.8, beta, ctx, E)
    th, sse, _ = jp.fit(jp.Additive(), ctx, E, y, rng, restarts=2)
    assert sse / y.size < 1e-5


def test_test_episodes_pair_treated_and_untreated():
    ctx, E, labels = jp.test_episodes()
    assert len(labels) * 2 == ctx.shape[0]
    assert np.all(ctx[0::2] == ctx[1::2])
    assert np.all(E[1::2] == 0) and np.all(np.abs(E[0::2]).sum(axis=(1, 2)) == 1)


def test_heldout_pairs_absent_from_d2_training():
    rng = np.random.default_rng(4)
    ctx, E = jp.training_data(rng, "D2")
    n, t, j = np.nonzero(E)
    assert not any((jj, ctx[nn, tt]) in jp.HELDOUT for nn, tt, jj in zip(n, t, j))
