import numpy as np
import pytest

import model as M


def rand_params(rng, **kw):
    sigma = rng.uniform(0.05, 0.6)
    phi = rng.uniform(0, 1 - sigma - 0.05)
    P = M.default_params(rho=rng.uniform(0.05, 0.9), sigma=sigma, phi=phi,
                         eps=rng.uniform(0, 1), g=rng.uniform(0, 40),
                         delta=rng.uniform(0, 0.99), eta=rng.uniform(0, 5))
    P.update(kw)
    return P


@pytest.mark.parametrize("conferral", ["ema", "replicator"])
@pytest.mark.parametrize("regime", ["A", "B"])
def test_closed_form_equals_mean_field(conferral, regime):
    rng = np.random.default_rng(1)
    for _ in range(200):
        P = rand_params(rng, conferral=conferral, regime=regime,
                        r=tuple(rng.uniform(0.3, 0.9, 2)))
        m, a = rng.uniform(-0.95, 0.95, 2)
        if regime == "B" and conferral == "replicator":
            continue
        assert np.allclose(M.mean_field(m, a, P), M.mean_field_closed(m, a, P), atol=1e-12)


def test_hard_score_difference():
    P = M.default_params(scoring="hard")
    for m in (-0.3, 0.2):
        m1, a1 = M.mean_field(m, 0.0, P)
        exp = (1 - P["delta"]) * np.tanh(P["g"] * P["sigma"] * np.sign(m) / 2)
        assert np.isclose(a1, exp)


@pytest.mark.parametrize("conferral", ["ema", "replicator"])
def test_jacobian(conferral):
    rng = np.random.default_rng(2)
    for _ in range(200):
        P = rand_params(rng, conferral=conferral)
        assert np.allclose(M.jacobian_analytic(P), M.jacobian_numeric(M.mean_field, P), atol=1e-6)


def test_threshold_closed_form_and_spectral_radius():
    rng = np.random.default_rng(3)
    for _ in range(2000):
        P = rand_params(rng)
        J = M.jacobian_analytic(P)
        lam = max(abs(np.linalg.eigvals(J)))
        closed = P["g"] * P["sigma"] ** 2 / 2 > 1 - P["phi"] * (1 - P["eps"])
        assert M.threshold_holds(P) == closed
        assert (lam > 1) == closed or abs(lam - 1) < 1e-9


def test_containment_exact_agreement_kernel():
    rng = np.random.default_rng(4)
    for _ in range(100):
        P = rand_params(rng)
        b = rng.uniform(-1, 1) * (1 - P["sigma"] - P["phi"])
        P["b"] = b
        Q = M.to_bc_params(P)
        m, a = rng.uniform(-0.9, 0.9, 2)
        for _ in range(50):
            m1, a1 = M.mean_field(m, a, P)
            m2, a2 = M.adaptive_bc_step(m, a, Q, "agreement")
            assert abs(m1 - m2) < 1e-12 and abs(a1 - a2) < 1e-12
            m, a = m1, a1


def test_containment_gaussian_kernel_balanced():
    rng = np.random.default_rng(5)
    for _ in range(100):
        P = rand_params(rng, b=0.0)
        Q = M.to_bc_params(P)
        m, a = rng.uniform(-0.9, 0.9, 2)
        for _ in range(50):
            m1, a1 = M.mean_field(m, a, P)
            m2, a2 = M.adaptive_bc_step(m, a, Q, "gaussian")
            assert abs(m1 - m2) < 1e-12 and abs(a1 - a2) < 1e-12
            m, a = m1, a1


def test_gaussian_differs_when_imbalanced():
    P = M.default_params(b=0.2)
    Q = M.to_bc_params(P)
    assert abs(M.mean_field(0.1, 0.0, P)[1] - M.adaptive_bc_step(0.1, 0.0, Q, "gaussian")[1]) > 1e-3


def test_predecessor_power_maps_symmetric():
    C = M.network_from_case(M.default_params(), 0.0)
    x = np.array([0.2, 0.5, 0.5])
    for step in (M.degroot_friedkin_step, M.friedkin2011_step):
        y = x.copy()
        for _ in range(50):
            y = step(y, C)
            assert abs(y[1] - y[2]) < 1e-10


def test_stochastic_one_step_mean_is_mean_field():
    """The frame is drawn once per round, so trajectories stay noisy in phi;
    the expected one-step map is the mean field (exact for p, and for w up to
    O(1/k) in the soft score)."""
    P = M.default_params(k=5000, g=4.0)
    rng = np.random.default_rng(0)
    for p0, w0 in ((0.6, 0.45), (0.3, 0.7)):
        draws = np.array([M.step_stochastic(p0, w0, P, rng) for _ in range(4000)])
        m1, a1 = M.mean_field(2 * p0 - 1, 2 * w0 - 1, P)
        assert abs(2 * draws[:, 0].mean() - 1 - m1) < 0.01
        assert abs(2 * draws[:, 1].mean() - 1 - a1) < 0.002
