import numpy as np
import pytest

import dd as D


def rand_stable(n, rng, rho=0.9):
    A = rng.standard_normal((n, n))
    return A * rho / max(abs(np.linalg.eigvals(A)))


@pytest.mark.parametrize("seed", range(12))
def test_filter_matches_lag_regression(seed):
    rng = np.random.default_rng(seed)
    n, m = 5, 1 + seed % 2
    A = rand_stable(n, rng, 0.8)
    S = D.random_spd(n, rng)
    L = rng.standard_normal((m, n))
    t = D.dd(A, L, S)
    t_lag = D.dd_lags(A, L, S, 60)
    assert abs(t - t_lag) < 1e-8 * max(1.0, t)


@pytest.mark.parametrize("seed", range(40))
def test_sandwich(seed):
    rng = np.random.default_rng(100 + seed)
    n, m = 6, 1 + seed % 3
    A = rand_stable(n, rng, rng.uniform(0.3, 0.97))
    S = D.random_spd(n, rng)
    L = rng.standard_normal((m, n))
    lo, up = D.bounds(A, L, S)
    t = D.dd(A, L, S)
    assert -1e-12 <= lo <= t + 1e-10
    assert t <= up + 1e-10


def test_closed_aggregate_is_zero():
    rng = np.random.default_rng(7)
    B1 = D.equal_colsum_block(3, 0.9, rng)
    B2 = D.equal_colsum_block(4, 0.8, rng)
    A = D.block_diag(B1, B2)
    S = D.random_spd(7, rng)
    L = D.block_sum([3, 4], 0)
    assert abs(D.dd(A, L, S)) < 1e-12
    lo, up = D.bounds(A, L, S)
    assert abs(lo) < 1e-12 and abs(up) < 1e-12


def test_unclosed_aggregate_floor_positive():
    rng = np.random.default_rng(8)
    B1 = D.unequal_colsum_block(3, 0.9, rng)
    B2 = D.equal_colsum_block(4, 0.8, rng)
    A = D.block_diag(B1, B2)
    S = D.random_spd(7, rng)
    L = D.block_sum([3, 4], 0)
    lo, up = D.bounds(A, L, S)
    assert lo > 1e-4
    assert D.dd(A, L, S) >= lo


def test_block_full_state_upper_is_claim390():
    """With L the projection onto a block, the upper bound is
    CLAIM-390's 1/2 log det(I + S_YY^-1 A_YR C A_YR^T), C = Cov(R|Y)."""
    rng = np.random.default_rng(9)
    n, k = 5, 2
    A = rand_stable(n, rng, 0.85)
    S = D.random_spd(n, rng)
    L = np.eye(n)[:k]
    Pi = D.lyap(A, S)
    C = Pi[k:, k:] - Pi[k:, :k] @ np.linalg.solve(Pi[:k, :k], Pi[:k, k:])
    AYR = A[:k, k:]
    ref = 0.5 * np.linalg.slogdet(
        np.eye(k) + np.linalg.solve(S[:k, :k], AYR @ C @ AYR.T))[1]
    assert abs(D.bounds(A, L, S)[1] - ref) < 1e-12


def test_block_constructors():
    rng = np.random.default_rng(3)
    B = D.equal_colsum_block(4, 0.7, rng)
    assert np.allclose(B.sum(axis=0), 0.7)
    assert abs(max(abs(np.linalg.eigvals(B))) - 0.7) < 1e-12
    U = D.unequal_colsum_block(4, 0.7, rng)
    assert np.ptp(U.sum(axis=0)) > 1e-3
    assert abs(max(abs(np.linalg.eigvals(U))) - 0.7) < 1e-12


def test_lyap():
    rng = np.random.default_rng(4)
    A = rand_stable(4, rng)
    S = D.random_spd(4, rng)
    P = D.lyap(A, S)
    assert np.allclose(P, A @ P @ A.T + S)
