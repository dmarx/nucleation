import numpy as np

import study as s


def test_stationary_cov_matches_simulation():
    rng = np.random.default_rng(0)
    M, Adj = s.make_org(rng)
    for c, g in [(0.4, 0.0), (0.0, 0.5)]:
        X = s.simulate(Adj, M, c, g, 20000, rng)
        S = s.stationary_cov(None, Adj, M, c, g)
        assert abs(np.cov(X.T).trace() / S.trace() - 1) < 0.1


def test_null_is_matched_on_within_group_correlation():
    rng = np.random.default_rng(1)
    M, Adj = s.make_org(rng)
    target = s.mean_within(s.stationary_cov(None, Adj, M, 0.4, 0.0), M)
    for w in ["driver", "mixed"]:
        c, g = s.world_params(w, Adj, M)
        assert abs(s.mean_within(s.stationary_cov(None, Adj, M, c, g), M) - target) < 1e-6


def test_restricted_var_recovers_coupling():
    rng = np.random.default_rng(2)
    M, Adj = s.make_org(rng)
    X = s.simulate(Adj, M, 0.4, 0.0, 20000, rng)
    A = s.fit_var(X, (Adj + np.eye(s.N)) > 0)
    assert np.abs(A - s.coupling_matrix(Adj, 0.4)).max() < 0.05


def test_gibbs_recovers_planted_sparse_features():
    rng = np.random.default_rng(3)
    T, N = 500, 24
    B = np.zeros((N, 3))
    B[:8, 0] = 1
    B[6:14, 1] = 1
    B[16:, 2] = 1
    W = 1.5 * B
    F = rng.standard_normal((T, 3))
    Y = F @ W.T + 0.5 * rng.standard_normal((T, N))
    Bh, L, psi, Fh = s.gibbs_features(Y, rng, iters=300)
    big = [Bh[:, k] for k in range(Bh.shape[1]) if Bh[:, k].sum() >= 4]
    for k in range(3):
        best = max(((B[:, k] > 0) & (c > 0)).sum() / ((B[:, k] > 0) | (c > 0)).sum()
                   for c in big)
        assert best >= 0.75  # splits are free (CASE-165 item 4)
