import numpy as np
import pytest

import tree_pmi as t


@pytest.mark.parametrize("b,D,w", [(2, 3, 1), (3, 3, 2), (4, 2, 1), (2, 5, 1)])
def test_closed_form_spectrum(b, D, w):
    rng = np.random.default_rng(b * 10 + D)
    lam = rng.uniform(0.1, 3, D)
    X, depth, _ = t.incidence(b, D, w)
    M = X @ np.diag(lam[depth - 1]) @ X.T
    ev = np.sort(np.linalg.eigvalsh(M))[::-1]
    pred = np.sort(np.concatenate([[mu] * m for mu, m, _ in t.predicted_spectrum(b, D, lam, w)]))[::-1]
    assert np.allclose(ev[: len(pred)], pred)
    assert np.allclose(ev[len(pred):], 0, atol=1e-8)


@pytest.mark.parametrize("b,D", [(2, 4), (3, 3)])
def test_truncation_keeps_shallow_levels(b, D):
    rng = np.random.default_rng(1)
    lam = rng.uniform(0.1, 3, D)
    X, depth, _ = t.incidence(b, D)
    M = X @ np.diag(lam[depth - 1]) @ X.T
    # K = 0 is skipped: with no root strength the constant vector ties with
    # level 0, so a rank-1 truncation is not determined.
    for K in range(1, D + 1):
        F = t.readout(t.spectral_embedding(M, r=b ** K)[0], X, raw=True)
        for l in range(1, D + 1):
            if l <= K:  # kept: exact
                assert np.allclose(F[:, depth == l], X[:, depth == l], atol=1e-8)
            else:  # lost: readout is the depth-K ancestor's indicator / b^(l-K),
                # identical across all descendants of that ancestor (siblings confused)
                anc = X[:, depth == K] if K > 0 else np.ones((X.shape[0], 1))
                cols = np.where(depth == l)[0]
                for j in cols:
                    a = anc[X[:, j] == 1][0]
                    target = (anc @ a) / b ** (l - K)
                    assert np.allclose(F[:, j], target, atol=1e-8)


def test_general_context_exact_readout():
    rng = np.random.default_rng(2)
    for _ in range(5):
        X, _ = t.random_context(200, 30, 50, rng)
        X = X[:, X.sum(0) > 0]
        M = X @ np.diag(rng.uniform(0.1, 2, X.shape[1])) @ X.T
        assert np.array_equal(t.readout(t.spectral_embedding(M)[0], X), X)


def test_random_context_is_closed():
    rng = np.random.default_rng(3)
    X, parents = t.random_context(100, 20, 30, rng)
    for k, ps in parents.items():
        for p in ps:
            assert np.all(X[:, k] <= X[:, p])
