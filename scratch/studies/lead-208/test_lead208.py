"""Tests for the LEAD-208 study code. Run: python3 -I -m pytest -q (from this directory)."""
import itertools
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from clusters import box_counts, largest_cluster_masks  # noqa: E402
from fisher import compatible_mean, cross_cov, level_estimates  # noqa: E402
from ising import (K_C, NPARAM, OFFSETS, checkerboard, energy_mag,  # noqa: E402
                   heat_bath, label_clusters, metropolis, observables,
                   observed_mask, random_spins, rb_given_black, shift,
                   swendsen_wang)
from strip import (column_block_entropy, column_mi, markov_chain,  # noqa: E402
                   row_block_entropies, transfer_matrix)

L4 = 4


@pytest.fixture(scope="module")
def all_4x4():
    """Every configuration of the 4 x 4 torus, shape (65536, 4, 4)."""
    n = L4 * L4
    c = np.arange(2 ** n)[:, None]
    s = np.where((c >> np.arange(n)) & 1, 1, -1).astype(np.int8)
    return s.reshape(-1, L4, L4)


def exact_moments(all_s, K):
    e, m = energy_mag(all_s)
    w = np.exp(-K * (e - e.min()))
    w /= w.sum()
    return w, e, m


def test_energy_magnetisation_exact_vs_sw_and_metropolis(all_4x4):
    """<E>/N and <M^2>/N^2 from SW and Metropolis match exact enumeration."""
    for K in (K_C, K_C / 1.1, K_C / 0.9):
        w, e, m = exact_moments(all_4x4, K)
        N = L4 * L4
        eE, eM2 = (w * e).sum() / N, (w * m.astype(float) ** 2).sum() / N ** 2
        for update in ("sw", "met"):
            rng = np.random.default_rng(1)
            s = random_spins(rng, 256, L4)
            es, ms = [], []
            for t in range(400):
                if update == "sw":
                    swendsen_wang(s, K, rng)
                else:
                    metropolis(s, K, rng)
                if t >= 50:
                    ee, mm = energy_mag(s)
                    es.append(ee.mean() / N)
                    ms.append((mm.astype(float) ** 2).mean() / N ** 2)
            es, ms = np.array(es), np.array(ms)
            # replicas are independent; error ~ spread / sqrt(256 * effective samples)
            assert abs(es.mean() - eE) < 0.01, (update, K, es.mean(), eE)
            assert abs(ms.mean() - eM2) < 0.01, (update, K, ms.mean(), eM2)


def test_transfer_matrix_partition_function(all_4x4):
    """trace(T^4) on width 4 equals the 4 x 4 torus partition function."""
    K = 0.37
    e, _ = energy_mag(all_4x4)
    Z = np.exp(-K * e).sum()
    Tm, lam, psi, shiftc = transfer_matrix(4, K)
    Ztm = np.trace(np.linalg.matrix_power(Tm, 4)) * np.exp(4 * shiftc)
    assert np.isclose(Z, Ztm, rtol=1e-10)


def test_column_process_is_markov():
    """Column-block predictive information does not depend on block length."""
    for K in (K_C, 0.3):
        I1 = column_mi(3, K)
        for T in (1, 2):
            H = column_block_entropy(3, K, T)
            H2 = column_block_entropy(3, K, 2 * T)
            assert np.isclose(2 * H - H2, I1, atol=1e-10)


def test_row_block_entropy_by_enumeration():
    """Forward recursion equals summing the column chain over hidden columns."""
    W, K, tmax = 3, K_C, 4
    pi, P = markov_chain(W, K)
    H = row_block_entropies(W, K, tmax)
    for t in range(1, tmax + 1):
        probs = {}
        for cols in itertools.product(range(2 ** W), repeat=t):
            p = pi[cols[0]]
            for a, b in zip(cols[:-1], cols[1:]):
                p *= P[a, b]
            key = tuple(c & 1 for c in cols)
            probs[key] = probs.get(key, 0.0) + p
        p = np.array(list(probs.values()))
        assert np.isclose(-(p * np.log2(p)).sum(), H[t - 1], atol=1e-10)


def test_rb_given_black_exact(all_4x4):
    """E[Phi | black] from the formula equals brute-force conditioning."""
    K = K_C
    black = checkerboard(L4)
    rng = np.random.default_rng(3)
    s0 = random_spins(rng, 1, L4)[0]
    match = (all_4x4[:, black] == s0[black]).all(axis=1)
    sub = all_4x4[match]
    w, e, _ = exact_moments(sub, K)
    brute = (w[:, None] * observables(sub)).sum(axis=0)
    formula = rb_given_black(s0[None], K)[0]
    assert np.allclose(brute, formula, atol=1e-10)


def test_frozen_sampler_samples_conditional(all_4x4):
    """SW + heat-bath with frozen sites reproduces E[Phi | observed] (level 2)."""
    K = K_C
    obs = observed_mask(L4, 2)
    rng = np.random.default_rng(5)
    s0 = random_spins(rng, 1, L4)[0]
    match = (all_4x4[:, obs] == s0[obs]).all(axis=1)
    w, e, _ = exact_moments(all_4x4[match], K)
    exact = (w[:, None] * observables(all_4x4[match])).sum(axis=0)
    s = np.repeat(s0[None], 2000, axis=0)
    est = compatible_mean(s, K, obs, rng, burn=5, nmeas=10)
    assert (s == s0).all()  # the start configuration is not modified
    assert np.allclose(est.mean(axis=0), exact, atol=0.15)


def test_frozen_sites_never_change():
    rng = np.random.default_rng(7)
    s = random_spins(rng, 8, 16)
    fz = observed_mask(16, 3)
    before = s[:, fz].copy()
    for _ in range(5):
        swendsen_wang(s, K_C, rng, frozen=fz)
        heat_bath(s, K_C, rng, frozen=fz)
    assert (s[:, fz] == before).all()


def bfs_labels(br, bd):
    L = br.shape[0]
    lab = -np.ones((L, L), dtype=int)
    for i0 in range(L):
        for j0 in range(L):
            if lab[i0, j0] >= 0:
                continue
            root = i0 * L + j0
            stack = [(i0, j0)]
            lab[i0, j0] = root
            while stack:
                i, j = stack.pop()
                nb = []
                if br[i, j]:
                    nb.append((i, (j + 1) % L))
                if br[i, (j - 1) % L]:
                    nb.append((i, (j - 1) % L))
                if bd[i, j]:
                    nb.append(((i + 1) % L, j))
                if bd[(i - 1) % L, j]:
                    nb.append(((i - 1) % L, j))
                for a in nb:
                    if lab[a] < 0:
                        lab[a] = root
                        stack.append(a)
    return lab


def test_label_clusters_matches_bfs():
    rng = np.random.default_rng(11)
    for p in (0.3, 0.5, 0.7):
        br = rng.random((3, 12, 12)) < p
        bd = rng.random((3, 12, 12)) < p
        lab = label_clusters(br, bd)
        for b in range(3):
            ref = bfs_labels(br[b], bd[b])
            # same partition: a bijection between label sets
            pairs = set(zip(lab[b].ravel(), ref.ravel()))
            assert len(pairs) == len(set(ref.ravel())) == len(set(lab[b].ravel()))


def test_observed_mask_sizes():
    for L in (16, 32):
        for k in range(7):
            if 2 ** ((k + 1) // 2) <= L:
                assert observed_mask(L, k).sum() == L * L // 2 ** k
    # nested
    for k in range(5):
        assert (observed_mask(32, k + 1) <= observed_mask(32, k)).all()


def test_box_counts():
    L = 32
    full = np.ones((1, L, L), bool)
    line = np.zeros((1, L, L), bool)
    line[0, 3, :] = True
    eps = [1, 2, 4, 8]
    assert (box_counts(full, eps)[0] == [(L // e) ** 2 for e in eps]).all()
    assert (box_counts(line, eps)[0] == [L // e for e in eps]).all()


def test_largest_cluster_uniform():
    s = np.ones((2, 8, 8), np.int8)
    s[1, :, :4] = -1
    m = largest_cluster_masks(s)
    assert m[0].all() and m[1].sum() == 32


def test_cross_cov_equals_cov_when_identical():
    rng = np.random.default_rng(2)
    A = rng.normal(size=(500, 4))
    assert np.allclose(cross_cov(A, A), np.cov(A.T))


def test_fisher_level0_exact_small(all_4x4):
    """Level-0 Fisher (Cov Phi) from SW agrees with exact enumeration on 4 x 4."""
    K = K_C
    w, e, m = exact_moments(all_4x4, K)
    Phi = observables(all_4x4)
    mu = (w[:, None] * Phi).sum(axis=0)
    G = (w[:, None, None] * (Phi - mu)[:, :, None] * (Phi - mu)[:, None, :]).sum(axis=0)
    rng = np.random.default_rng(4)
    s = random_spins(rng, 512, L4)
    rows = []
    for t in range(120):
        swendsen_wang(s, K, rng)
        if t >= 20:
            rows.append(level_estimates(s, K, [0], rng)[0][0])
    rows = np.concatenate(rows)
    Gmc = cross_cov(rows, rows)
    assert np.allclose(np.diag(Gmc), np.diag(G), rtol=0.05)
