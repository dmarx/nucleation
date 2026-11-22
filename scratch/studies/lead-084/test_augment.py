"""pytest checks for augment.py. Run: python3 -I -m pytest -q test_augment.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pytest
from augment import *

RNG = np.random.default_rng(12345)
MODELS = []
for _ in range(25):
    n = int(RNG.integers(2, 7)); m = int(RNG.integers(1, n))
    MODELS.append(random_model(n, m, RNG, radius=0.9, corr=bool(RNG.integers(0, 2))))

# a 3-dimensional model whose eliminated dynamics are nilpotent
NIL_A = np.array([[0.1, 0.3, -1.0], [0.6, 0.0, -0.7], [0.1, 0.0, 0.0]])
NIL_L = np.array([[1.0, 0.0, 0.0]])
NIL_S = np.eye(3)


def test_lyap():
    A, L, S = MODELS[0]
    P = lyap(A, S)
    assert np.allclose(P, A @ P @ A.T + S, atol=1e-12)


@pytest.mark.parametrize("i", range(len(MODELS)))
def test_steady_dare_matches_iteration(i):
    A, L, S = MODELS[i]
    assert np.allclose(steady(A, L, S), steady_iter(A, L, S), atol=1e-10)


@pytest.mark.parametrize("i", range(len(MODELS)))
@pytest.mark.parametrize("p", [1, 3, 7])
def test_riccati_equals_finite_lag_regression(i, p):
    A, L, S = MODELS[i]
    Ps = riccati_seq(A, L, S, p)
    assert np.allclose(L @ Ps[p] @ L.T, regression_error(A, L, S, p), atol=1e-11)


@pytest.mark.parametrize("i", range(len(MODELS)))
@pytest.mark.parametrize("p", [1, 2, 5, 10])
def test_bound_sandwich(i, p):
    A, L, S = MODELS[i]
    exc, bnd, _ = excess_and_bound(A, L, S, p)
    assert np.linalg.eigvalsh(exc).min() > -1e-10
    assert np.linalg.eigvalsh(bnd - exc).min() > -1e-10


@pytest.mark.parametrize("i", range(len(MODELS)))
def test_closed_loop_has_m_zero_eigenvalues_and_matches_reduced(i):
    A, L, S = MODELS[i]
    m = L.shape[0]
    Acl = A - gain(A, L, steady(A, L, S)) @ L
    ev = np.sort(np.abs(np.linalg.eigvals(Acl)))
    assert np.all(ev[:m] < 1e-6)
    red = np.sort(np.abs(np.linalg.eigvals(reduced_filter(A, L, S)["Acl_r"])))
    assert np.allclose(ev[m:], red, atol=1e-6)


@pytest.mark.parametrize("i", range(len(MODELS)))
def test_kmin_at_most_n_minus_m_and_augmentation_markov(i):
    A, L, S = MODELS[i]
    W, k = predictive_coords(A, L, S)
    assert k <= A.shape[0] - L.shape[0]
    F, Q, M = joint_state(A, L, S, W)
    assert markov_defect(F, Q, M) < 1e-5
    c1 = cond_cov_lags(F, Q, M, 1)
    m = L.shape[0]
    assert np.allclose(c1[:m, :m], L @ steady(A, L, S) @ L.T, atol=1e-8)


@pytest.mark.parametrize("i", range(len(MODELS)))
def test_transfer_entropy_unchanged_by_augmentation(i):
    A, L, S = MODELS[i]
    W, k = predictive_coords(A, L, S)
    F, Q, M = joint_state(A, L, S, W)
    c1 = cond_cov_lags(F, Q, M, 1)
    cx = cond_cov_lags(F, Q, M, 1, extra=True)
    assert abs(logdet_range(c1, cx) - transfer_entropy_Y(A, L, S)) < 1e-6


@pytest.mark.parametrize("i", range(len(MODELS)))
def test_contraction_factor_bounds_rate(i):
    A, L, S = MODELS[i]
    c, normed, rf = contraction_factor(A, L, S)
    assert normed <= c + 1e-9
    assert rho(rf["Acl_r"]) <= c + 1e-9


def test_scalar_eliminated_rate_below_atilde():
    rng = np.random.default_rng(1)
    for _ in range(200):
        n = int(rng.integers(2, 6))
        A, L, S = random_model(n, n - 1, rng, radius=0.95)
        rf = reduced_filter(A, L, S)
        assert rho(rf["Acl_r"]) <= abs(rf["Atil"][0, 0]) + 1e-12


def test_atilde_invariant_to_complement():
    """Atilde is the same for any complement R' = R + H Y (and similar under
    R -> G R): check against the natural frame R = (x2..xn) for L = e1."""
    A, _, S = MODELS[3]
    n = A.shape[0]
    L = np.zeros((1, n)); L[0, 0] = 1
    nat = A[1:, 1:] - np.outer(S[1:, 0], A[0, 1:]) / S[0, 0]
    mori = reduced_filter(A, L, S)["Atil"]
    assert np.allclose(np.sort_complex(np.linalg.eigvals(nat)),
                       np.sort_complex(np.linalg.eigvals(mori)), atol=1e-8)


def test_nilpotent_eliminated_dynamics_counterexample():
    rf = reduced_filter(NIL_A, NIL_L, NIL_S)
    # natural frame: Atilde = A22 = [[0, -0.7], [0, 0]], nilpotent
    assert np.allclose(NIL_A[1:, 1:] @ NIL_A[1:, 1:], 0)
    assert rho(rf["Atil"]) < 1e-6
    r = rho(rf["Acl_r"])
    assert r > 0.09
    # the memory kernel in the natural frame vanishes after two lags
    K3 = NIL_A[:1, 1:] @ np.linalg.matrix_power(NIL_A[1:, 1:], 2) @ NIL_A[1:, :1]
    assert np.allclose(K3, 0)
    # yet the finite-lag excess error never reaches zero
    exc, _, _ = excess_and_bound(NIL_A, NIL_L, NIL_S, 6)
    assert exc[0, 0] > 1e-12


def test_ma_zeros_equal_closed_loop_scalar():
    rng = np.random.default_rng(2)
    for _ in range(10):
        n = int(rng.integers(2, 5))
        A, L, S = random_model(n, 1, rng, radius=0.9)
        ev = np.linalg.eigvals(A - gain(A, L, steady(A, L, S)) @ L)
        ev = np.sort(np.abs(ev[np.abs(ev) > 1e-8]))
        z = np.sort(np.abs(ma_zeros_scalar(A, L, S)))
        assert len(z) == len(ev) and np.allclose(z, ev, atol=1e-8)


def test_claim389_counterexample_needs_no_augmentation():
    A = np.array([[0.5, 0.4], [0.0, 0.3]]); S = np.eye(2) - A @ A.T
    L = np.array([[1.0, 0.0]])
    assert k_min(A, L, S) == 0
    assert abs(transfer_entropy_Y(A, L, S) - 0.5 * np.log((1 - 0.25) / (1 - 0.25 - 0.16))) < 1e-10


def test_closed_variable_zero_everything():
    A = np.array([[0.6, 0.0, 0.0], [0.3, 0.5, 0.0], [0.0, 0.4, 0.2]])
    L = np.array([[1.0, 0, 0]]); S = np.eye(3)
    assert k_min(A, L, S) == 0
    assert abs(transfer_entropy_Y(A, L, S)) < 1e-12
    exc, _, _ = excess_and_bound(A, L, S, 1)
    assert abs(exc[0, 0]) < 1e-12


def test_exact_discretization():
    Ac = np.array([[-1.0, 1.0], [0.2, -0.3]])
    Ah, Sh = exact_discretization(Ac, 0.1)
    # Sigma_h solves the discrete Lyapunov relation of the continuous one:
    # stationary covariances agree
    from scipy.linalg import solve_continuous_lyapunov
    Pc = solve_continuous_lyapunov(Ac, -np.eye(2))
    assert np.allclose(lyap(Ah, Sh), Pc, atol=1e-10)
