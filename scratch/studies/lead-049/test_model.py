import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import pytest

import model as M


def rand_state(rng, k=3, m=8):
    nic = M.GaussianNiche(m=m, w=0.15)
    b = rng.uniform(0.5, 1.5, m)
    c = rng.uniform(0.05, 0.3, k)
    n = rng.uniform(0.1, 1.0, k)
    th = rng.uniform(0.05, 0.95, k)
    return nic, b, c, n, th


def test_gradient_matches_finite_difference():
    rng = np.random.default_rng(0)
    nic, b, c, n, th = rand_state(rng)
    gn, gt = M.grad(nic, b, c, n, th)
    h = 1e-6
    for i in range(len(n)):
        e = np.zeros(len(n)); e[i] = h
        fd_n = (M.potential(nic, b, c, n + e, th) - M.potential(nic, b, c, n - e, th)) / (2 * h)
        fd_t = (M.potential(nic, b, c, n, th + e) - M.potential(nic, b, c, n, th - e)) / (2 * h)
        assert abs(fd_n - gn[i]) < 1e-6
        assert abs(fd_t - gt[i]) < 1e-6


def test_tradeoff_derivative():
    nic = M.TradeoffNiche(0.1, -0.7, 2.5)
    t = np.linspace(0.01, 0.99, 7)
    fd = (nic.a(t + 1e-6) - nic.a(t - 1e-6)) / 2e-6
    assert np.allclose(fd, nic.da(t), atol=1e-6)
    assert nic.a(0.0) == 0.0 and abs(nic.a(1.0) - 1.0) < 1e-12


@pytest.mark.parametrize("kappa", ["n", "one"])
def test_vector_field_is_metric_gradient(kappa):
    """dn_i = -n_i dL/dn_i and dtheta_i = -(eps kappa_i/n_i) dL/dtheta_i off the bounds."""
    rng = np.random.default_rng(1)
    nic, b, c, n, th = rand_state(rng)
    eps = 0.3
    f, dth = M.vector_field(nic, b, c, n, th, eps, kappa)
    gn, gt = M.grad(nic, b, c, n, th)
    D = M.metric_diag(n, eps, kappa)
    k = len(n)
    assert np.allclose(n * f, -D[:k] * gn)
    assert np.allclose(dth, -D[k:] * gt)


def test_potential_decreases_along_flow():
    rng = np.random.default_rng(2)
    nic, b, c, n, th = rand_state(rng)
    L0 = M.potential(nic, b, c, n, th)
    n1, th1, trace = M.simulate(nic, b, c, n, th, eps=0.5, T=20, dt=0.01, record_every=50)
    Ls = [M.potential(nic, b, c, nn, tt) for _, nn, tt in trace]
    assert np.all(np.diff(Ls) <= 1e-10)
    assert Ls[-1] < L0


def test_hessian_nn_block_is_gram():
    rng = np.random.default_rng(3)
    nic, b, c, n, th = rand_state(rng)
    H = M.hessian(nic, b, c, n, th)
    U = nic.u(th)
    k = len(n)
    assert np.allclose(H[:k, :k], U.T @ U, atol=1e-6)


def test_lv_equilibrium_is_kkt_and_matches_bruteforce():
    rng = np.random.default_rng(4)
    for _ in range(20):
        k = rng.integers(2, 6)
        U = rng.uniform(0, 1, (6, k))
        A = U.T @ U
        r = U.T @ rng.uniform(0, 1, 6) - rng.uniform(0, 0.5, k)
        n = M.lv_equilibrium(A, r)
        g = A @ n - r
        assert np.all(n >= 0)
        assert np.all(np.abs(g[n > 0]) < 1e-8)
        assert np.all(g[n == 0] >= -1e-8)


def test_theorem_B_equality_and_bound():
    """lambda_i >= n_i*/(A^-1)_ii, with equality when no secondary extinction."""
    rng = np.random.default_rng(5)
    seen_eq = seen_strict = 0
    for _ in range(300):
        k = rng.integers(2, 6)
        U = rng.uniform(0, 1, (7, k))
        A = U.T @ U
        nstar = rng.uniform(0.05, 1.0, k)
        r = A @ nstar  # interior equilibrium n*
        for i in range(k):
            lam, bound, secondary, _ = M.invasion_frozen(A, r, nstar, i)
            assert lam > 0
            assert lam >= bound - 1e-9
            if not secondary:
                assert abs(lam - bound) < 1e-8
                seen_eq += 1
            elif lam > bound + 1e-6:
                seen_strict += 1
    assert seen_eq > 0 and seen_strict > 0


def test_schur_identity():
    """1/(A^-1)_ii is the squared distance of u_i from the span of the others."""
    rng = np.random.default_rng(6)
    U = rng.normal(size=(6, 4))
    A = U.T @ U
    for i in range(4):
        others = np.delete(U, i, axis=1)
        P = others @ np.linalg.pinv(others)
        d2 = np.sum((U[:, i] - P @ U[:, i]) ** 2)
        assert abs(1 / np.linalg.inv(A)[i, i] - d2) < 1e-9


def test_two_component_case_118():
    """CASE-118: A = [[1, rho], [rho, 1]], r = (1, 1): lambda = 1 - rho."""
    for rho in [0.0, 0.3, 0.8]:
        A = np.array([[1, rho], [rho, 1.0]])
        r = np.ones(2)
        nstar = np.linalg.solve(A, r)
        lam, bound, secondary, _ = M.invasion_frozen(A, r, nstar, 0)
        assert abs(lam - (1 - rho)) < 1e-12 and abs(bound - lam) < 1e-12


def test_theorem_A_linearization_at_tradeoff_corner():
    nic = M.TradeoffNiche(0.0, -0.5, 0.0)  # a'(0) = 1 < a'(1) = 1.5
    b, c = np.ones(2), np.full(2, 0.3)
    n, th = np.full(2, 0.7), np.array([1.0, 0.0])
    chk = M.theorem_A_check(nic, b, c, n, th, eps=0.2)
    assert chk["holds"] and chk["n_free_traits"] == 0
    assert abs(chk["margin"] - 0.3 * 0.5) < 1e-9  # c (a'(1) - a'(0))
    assert chk["jac_max_re"] < 0 and abs(chk["jac_max_re"] - chk["pred_max_re"]) < 1e-5


def test_theorem_A_linearization_interior():
    """At an interior equilibrium the Jacobian on free coordinates is -D H."""
    nic = M.GaussianNiche(m=12, w=0.12)
    b, c = np.ones(12), np.full(3, 0.2)
    n, th = M.simulate(nic, b, c, np.full(3, 0.5), np.array([0.2, 0.5, 0.8]), eps=0.1, T=400, dt=0.02)
    chk = M.theorem_A_check(nic, b, c, n, th, eps=0.1)
    assert np.linalg.norm(np.concatenate(M.grad(nic, b, c, n, th))) < 1e-6
    assert chk["n_free_traits"] >= 1
    assert abs(chk["jac_max_re"] - chk["pred_max_re"]) < 1e-5


def test_generalist_invasion_formula():
    """Lone symmetric generalist: specialist's recovery growth is c (1/(2 a(1/2)) - 1)."""
    for ga in (0.0, 1.5, 3.0):
        nic = M.TradeoffNiche(0.0, -0.5, ga)
        B, c = 1.0, 0.3
        b, cc = np.array([B, B]), np.array([c, c])
        g = nic.a(0.5)
        n1 = (2 * g * B - c) / (2 * g * g)
        n, th = np.array([n1, 0.0]), np.array([0.5, 0.0])
        f = M.growth(nic, b, cc, n, th)
        assert abs(f[0]) < 1e-12  # resident at equilibrium
        assert abs(M.selection_gradient(nic, b, n, th)[0]) < 1e-12  # symmetric trait stationary
        assert abs(f[1] - c * (1 / (2 * g) - 1)) < 1e-12


def test_corner_margin_after_removal():
    """After the partner's removal the lone specialist's outward gradient is a'(1) c - a'(0) B."""
    nic = M.TradeoffNiche(0.0, -0.5, 3.0)
    B, c = 1.0, 0.3
    b = np.array([B, B])
    n, th = np.array([B - c, 0.0]), np.array([1.0, 0.0])
    sg = M.selection_gradient(nic, b, n, th)[0]
    assert abs(sg - (nic.da(1.0) * c - nic.da(0.0) * B)) < 1e-12
