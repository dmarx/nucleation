"""Tests for the LEAD-137 study. Run: python3 -I -m pytest -q test_study.py"""
import numpy as np
import study as S


def test_stationary_cov_solves_lyapunov():
    rng = np.random.default_rng(0)
    M = rng.standard_normal((6, 6))
    A = S.scale_to_radius(M, 0.8)
    Sigma = S.stationary_cov(A)
    resid = A @ Sigma @ A.T + np.eye(6) - Sigma
    assert np.max(np.abs(resid)) < 1e-9
    # stationary covariance is symmetric PSD
    assert np.allclose(Sigma, Sigma.T, atol=1e-8)
    assert np.min(np.linalg.eigvalsh(0.5 * (Sigma + Sigma.T))) > 0


def test_scale_to_radius():
    rng = np.random.default_rng(1)
    M = rng.standard_normal((8, 8))
    A = S.scale_to_radius(M, 0.9)
    assert abs(np.max(np.abs(np.linalg.eigvals(A))) - 0.9) < 1e-9


def test_overlap_self_and_orthogonal():
    u = np.array([1.0, 2.0, 2.0]); u = u / np.linalg.norm(u)
    v = np.array([2.0, -1.0, 0.0]); v = v / np.linalg.norm(v)  # u.v = 0
    assert abs(S.overlap(u, u) - 1.0) < 1e-12
    assert S.overlap(u, v) < 1e-12


def test_block_direction_recovers_slow_mode():
    # Symmetric 3-node block: uniform mode is the leading (slowest) eigenvector.
    A_RR = np.array([[0.6, 0.3, 0.3],
                     [0.3, 0.6, 0.3],
                     [0.3, 0.3, 0.6]])
    N = 4
    A = np.zeros((N, N)); A[:3, :3] = A_RR
    u, gap, _ = S.block_direction(A, np.array([0, 1, 2]))
    uniform = np.ones(3) / np.sqrt(3)
    assert S.overlap(u, uniform) > 0.999
    assert gap > 0


def test_info_direction_canon_corr_in_range():
    rng = np.random.default_rng(2)
    M = rng.standard_normal((12, 12))
    A = S.scale_to_radius(M, 0.85)
    Sigma = S.stationary_cov(A)
    idx_R = np.arange(4); idx_E = np.arange(8, 12)
    u, cc2, _ = S.info_direction(Sigma, idx_R, idx_E)
    assert 0.0 <= cc2 <= 1.0 + 1e-9
    assert abs(np.linalg.norm(u) - 1.0) < 1e-9


def test_coarse_corr_bounds():
    rng = np.random.default_rng(3)
    X = rng.standard_normal((5, 5)); S_RR = X @ X.T + np.eye(5)
    u = rng.standard_normal(5); u /= np.linalg.norm(u)
    v = rng.standard_normal(5); v /= np.linalg.norm(v)
    c = S.coarse_corr(S_RR, u, v)
    assert 0.0 <= c <= 1.0 + 1e-9
    assert abs(S.coarse_corr(S_RR, u, u) - 1.0) < 1e-9


def test_homogeneous_border_matches_better_than_generic():
    # The lattice-like homogeneous-border system should align the informative
    # direction and the slow block mode better than a generic sparse border.
    base = dict(K=4, n=8, p_in=0.5, w_in=1.0, w_cross=0.3, mode='symmetric',
                rho=0.9, buffer_width=1)
    hom = [S.run_item({**base, 'seed': s, 'homogeneous_border': True})['overlap']
           for s in range(10)]
    gen = [S.run_item({**base, 'seed': s, 'homogeneous_border': False})['overlap']
           for s in range(10)]
    assert np.mean(hom) > np.mean(gen)


def test_run_item_keys():
    out = S.run_item(dict(K=4, n=8, p_in=0.5, w_in=1.0, w_cross=0.3,
                          mode='symmetric', rho=0.9, buffer_width=1, seed=0))
    for key in ('overlap', 'coarse_corr', 'subspace2', 'top_sq_canon_corr',
                'block_gap', 'near_decomp_ratio', 'N'):
        assert key in out
    assert 0.0 <= out['overlap'] <= 1.0 + 1e-9
