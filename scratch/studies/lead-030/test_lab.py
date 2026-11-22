import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lab  # noqa: E402


def test_ari_identity_and_permutation():
    a = np.array([0, 0, 1, 1, 2, 2])
    assert abs(lab.ari(a, a) - 1) < 1e-12
    assert abs(lab.ari(a, (a + 1) % 3) - 1) < 1e-12
    rng = np.random.default_rng(0)
    x, y = rng.integers(0, 4, 4000), rng.integers(0, 4, 4000)
    assert abs(lab.ari(x, y)) < 0.01


def test_gumbel_topk_without_replacement_and_weighted():
    rng = np.random.default_rng(1)
    w = np.ones((2000, 10))
    w[:, 0] = 50.0
    X = lab.sample_exposure(w, 3, rng)
    assert all(len(set(r)) == 3 for r in X)
    assert (X == 0).any(1).mean() > 0.95
    assert ((X == 1).any(1).mean() - 0.24) ** 2 < 0.01


def test_size_matched_partition():
    lab_ = lab.size_matched_partition(np.array([5.0, 1.0, 3.0, 4.0, 2.0]), [2, 3])
    assert list(lab_) == [0, 1, 1, 0, 1]


def test_spectral_coclusters_recovers_planted_blocks():
    rng = np.random.default_rng(2)
    U, I, K = 300, 200, 3
    lu0, li0 = rng.integers(0, K, U), rng.integers(0, K, I)
    P = np.where(lu0[:, None] == li0[None, :], 0.3, 0.03)
    C = (rng.random((U, I)) < P).astype(float)
    lu, li = lab.spectral_coclusters(C, K, rng)
    assert lab.ari(lu, lu0) > 0.95 and lab.ari(li, li0) > 0.95


def test_block_rates_degree_corrected():
    C = np.array([[2.0, 0.0], [0.0, 4.0]])
    om = lab.block_rates(C, np.array([0, 1]), np.array([0, 1]), 2)
    assert np.allclose(np.outer(C.sum(1), C.sum(0)) * om[[0, 1]][:, [0, 1]], C)


def test_logistic_models_nest_in_sample():
    rng = np.random.default_rng(3)
    U, I, n = 7, 5, 60
    u, i = rng.integers(0, U, n), rng.integers(0, I, n)
    y = rng.random(n) < 0.3
    cu, ci = rng.integers(0, 2, U), rng.integers(0, 2, I)
    # recover the objective through a one-iteration fit is awkward; instead
    # check that the fitted class model beats the degree model in-sample and
    # that predictions have the right shape
    m0 = lab.fit_logistic(u, i, y, U, I)
    m1 = lab.fit_logistic(u, i, y, U, I, cu=cu, ci=ci, K=2)
    m2 = lab.fit_logistic(u, i, y, U, I, rank=2, lam=0.1)
    ll = [lab.mean_loglik(lab.predict_logistic(m, u, i), y) for m in (m0, m1, m2)]
    assert ll[1] >= ll[0] - 1e-6 and ll[2] >= ll[0] - 1e-6


def test_logistic_recovers_planted_class_effect():
    rng = np.random.default_rng(4)
    U, I, n = 200, 100, 40000
    cu, ci = rng.integers(0, 2, U), rng.integers(0, 2, I)
    u, i = rng.integers(0, U, n), rng.integers(0, I, n)
    z = -1.0 + 1.5 * (cu[u] == ci[i])
    y = rng.random(n) < lab.sigmoid(z)
    m = lab.fit_logistic(u, i, y, U, I, cu=cu, ci=ci, K=2)
    g = m["ga"].reshape(2, 2)
    contrast = (g[0, 0] + g[1, 1] - g[0, 1] - g[1, 0]) / 2
    assert abs(contrast - 1.5) < 0.15


def test_closure_score():
    assert lab.closure_score(-1.0, -0.5, -0.5) == 1.0
    assert lab.closure_score(-1.0, -1.0, -0.5) == 0.0
    assert np.isnan(lab.closure_score(-1.0, -1.0, -1.0))


def test_separation_r2():
    v = np.array([[0.0], [0.0], [2.0], [2.0]])
    assert abs(lab.separation_r2(v, np.array([0, 0, 1, 1])) - 1) < 1e-12
    assert abs(lab.separation_r2(v, np.array([0, 1, 0, 1]))) < 1e-12


def test_adapt_moves_users_toward_engaged_items():
    rng = np.random.default_rng(5)
    p = dict(lab.DEFAULTS, U=20, I=30, turnover=0.0)
    st = lab.make_world("taste", rng, p)
    X = np.tile(np.arange(5), (20, 1))
    Y = np.zeros_like(X, bool)
    Y[:, 0] = True
    before = np.linalg.norm(st["u"] - st["v"][0], axis=1)
    cls = dict(user=np.zeros(20, int), item=np.zeros(30, int), target=np.zeros(6, int))
    lab.adapt(st, p, X, Y, rng, cls)
    after = np.linalg.norm(st["u"] - st["v"][0], axis=1)
    assert np.allclose(after, (1 - p["eta"]) * before)
