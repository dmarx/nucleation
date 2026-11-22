import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import pytest

import model as M


def rand_problem(rng, k=3):
    G = rng.normal(size=(k, 2))
    eps = rng.normal(0, 0.5, k)
    r = rng.uniform(0.05, 1.0)
    return eps, G, r


def test_exact_oracle_matches_slsqp_and_duality():
    rng = np.random.default_rng(0)
    for _ in range(300):
        eps, G, r = rand_problem(rng)
        phi_x, d_x = M.oracle_exact2d(eps, G, r)
        phi_p, d_p, lam, gap = M.oracle(eps, G, r)
        phi_d, _ = M.oracle_dual(eps, G, r)
        assert np.linalg.norm(d_x) <= r + 1e-12
        assert phi_x == pytest.approx(M.worst_residual(eps, G, d_x), abs=1e-12)
        # weak duality: dual <= exact; SLSQP primal >= exact
        assert phi_d <= phi_x + 1e-7
        assert phi_p >= phi_x - 1e-7
        assert phi_x == pytest.approx(phi_d, abs=1e-5)


def test_exact_oracle_beats_random_admissible_updates():
    rng = np.random.default_rng(1)
    for _ in range(100):
        eps, G, r = rand_problem(rng)
        phi, _ = M.oracle_exact2d(eps, G, r)
        a = rng.uniform(0, 2 * np.pi, 2000)
        rho = r * np.sqrt(rng.uniform(0, 1, 2000))
        D = np.stack([rho * np.cos(a), rho * np.sin(a)], 1)
        assert np.min(np.max(eps + D @ G.T, axis=1)) >= phi - 1e-12


def test_claim365_worked_case():
    # CASE-115 / K07: g1 = -2, g2 = 2 (embedded in 2-D), Phi_r = eps for every r
    G = np.array([[-2.0, 0.0], [2.0, 0.0]])
    eps = np.array([0.3, 0.3])
    for r in [0.0, 0.1, 1.0, 5.0]:
        phi, _ = M.oracle_exact2d(eps, G, r)
        assert phi == pytest.approx(0.3)


def test_claim357_counterexample_regret_positive_but_met():
    # one demand eps = 1, g = 1 (embedded); U = ball of radius 2: Phi = -1;
    # d = -1 meets the requirement (m = 0) with regret 1
    G = np.array([[1.0, 0.0]])
    eps = np.array([1.0])
    phi, _ = M.oracle_exact2d(eps, G, 2.0)
    assert phi == pytest.approx(-1.0)
    m = M.worst_residual(eps, G, np.array([-1.0, 0.0]))
    assert m == pytest.approx(0.0) and m - phi == pytest.approx(1.0)


def test_alloc_oracle_bounds():
    rng = np.random.default_rng(2)
    for _ in range(100):
        eps, G, r = rand_problem(rng)
        phi, _ = M.oracle_exact2d(eps, G, r)
        pa, w = M.alloc_oracle(eps, G, r)
        assert pa >= phi - 1e-12          # allocations reach only part of U_r
        assert w.sum() == pytest.approx(1.0) and (w >= 0).all()
        assert pa == pytest.approx(M.worst_residual(eps, G, M.update_of(w, G, r)))


def test_update_map_admissible_and_vectorized():
    rng = np.random.default_rng(3)
    G = rng.normal(size=(3, 2))
    W = M.simplex_grid(3, 10)
    D = M.updates_of(W, G, 0.3)
    for w, d in zip(W, D):
        assert np.allclose(d, M.update_of(w, G, 0.3))
        assert np.linalg.norm(d) <= 0.3 + 1e-12


def test_demands_requirement():
    dem = M.Demands([[0.0, 0.0]], [0.5], eta=0.05)
    assert dem.requirement(np.array([3.0, 0.0]))[0] == pytest.approx(0.05)
    assert dem.requirement(np.array([0.5, 0.0]))[0] == pytest.approx(0.125 - 0.5)
    assert np.allclose(dem.grads(np.array([1.0, 2.0])), [[1.0, 2.0]])


def test_regime_A_score_is_agreement_and_B_is_residual():
    G = np.array([[1.0, 0.0], [0.0, 1.0]])
    d = np.array([-0.1, 0.0])
    sA = M.scores("A", G, d, np.zeros(2), 0.05)
    assert sA == pytest.approx([1.0, 0.0])
    eps = np.array([0.05, 0.05])
    sB = M.scores("B", G, d, eps, 0.05)
    assert sB == pytest.approx([(0.05 - 0.1) / 0.05, 1.0])


def test_fixed_rule_keeps_weights_and_oracle_rule_never_worse_on_a_step():
    rng = np.random.default_rng(4)
    dem = M.random_instance(rng)
    rec, s = M.run(dem, [0.0, 2.2], [0.5, 0.3, 0.2], "fixed", T=30)
    assert np.allclose(rec["wmax"], 0.5)
    rec, s = M.run(dem, [0.0, 2.2], [1 / 3] * 3, "oracle", T=30)
    assert np.allclose(rec["m"], rec["phi_alloc"])


def test_random_instance_overlap():
    rng = np.random.default_rng(5)
    for _ in range(20):
        assert M.common_region_nonempty(M.random_instance(rng, overlap=True))
