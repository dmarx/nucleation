"""Tests for the LEAD-192 bound. Run: python3 -I -m pytest scratch/studies/lead-192 -q"""

import numpy as np
import pytest

import lead192 as L

TOL = 1e-9  # relative slack for rounding


def _check_rows(rows, symmetric=True):
    for r in rows:
        # the a posteriori bound (true f_j) and the a priori chain bound
        assert r["s_true"] <= r["s_bound"] * (1 + TOL) + 1e-12, r
        assert r["s_true"] <= r["s_bound_chain"] * (1 + TOL) + 1e-12, r
        # the accumulation recursion bounds the true operator error
        assert r["f_true"] <= r["f_bound"] * (1 + TOL) + 1e-12, r
        # closure at the level's own time step needs no gap
        assert r["closure_Tm"] <= (r["d_col"] + r["f_true"]) * (1 + TOL) + 1e-12, r
        if symmetric:
            assert r["graded_ok"], r
            # the Davis-Kahan form, which vanishes for exact truncation
            assert r["s_true"] <= r["s_bound_dk"] * (1 + 1e-7) + 1e-9, r
            # closure under one step of T is at most twice the subspace error
            assert r["closure_T"] <= 2 * r["s_true"] * (1 + TOL) + 1e-12, r
            # row and column residuals agree for symmetric A_i
            assert abs(r["d_row"] - r["d_col"]) <= 1e-8 + 1e-6 * r["d_col"], r


@pytest.mark.parametrize("n", [64, 128])
def test_circle_pivoted_qr(n):
    rows = L.run_chain(L.circle_operator(n), 1e-4, 9,
                       lambda A: L.truncate_pivoted_qr(A, 1e-4))
    _check_rows(rows)


def test_clouds_pivoted_qr():
    rows = L.run_chain(L.clouds_operator(n_per=40), 1e-4, 12,
                       lambda A: L.truncate_pivoted_qr(A, 1e-4))
    _check_rows(rows)
    # once a wide gap isolates the three clouds, the subspace error is small
    last = rows[-1]
    assert last["k"] == 3 and last["s_true"] < 1e-2


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_gapped_noisy(seed):
    rng = np.random.default_rng(seed)
    lams = np.r_[1.0, 0.999, 0.998, np.linspace(0.6, 0.0, 57)]
    T = L.spectrum_operator(lams, seed=seed)
    rows = L.run_chain(T, 1e-4, 9, lambda A: L.truncate_noisy(A, 1e-4, 1e-6, rng))
    _check_rows(rows)


def test_exact_truncation_is_spectral():
    """With exact (SVD) truncation the computed space is the spectral one
    (THEORY-758's induction), so the subspace error is rounding."""
    T = L.circle_operator(96)
    rows = L.run_chain(T, 1e-4, 8, lambda A: L.truncate_svd(A, 1e-4))
    for r in rows:
        if r["gap_ratio"] < 0.999:  # a definite top-k space exists
            assert r["s_true"] < 1e-6, r


def test_per_level_bound_is_attained():
    """Two-dimensional example: T = diag(a, b), kept direction at angle theta.
    The residual is sqrt(a^2 sin^2 + b^2 cos^2); the bound residual/a tends
    to sin(theta) as b -> 0, so the per-level constant cannot be improved."""
    a, theta = 0.5, 0.01
    for b in [1e-2, 1e-4, 1e-6]:
        T = np.diag([a, b])
        q = np.array([[np.cos(theta)], [np.sin(theta)]])
        P = q @ q.T
        d = np.linalg.norm((np.eye(2) - P) @ T, 2)
        s = np.linalg.norm(P - np.diag([1.0, 0.0]), 2)
        assert s <= d / a + 1e-15
        assert d / a / s < 1 + (b / a) ** 2 / np.sin(theta) ** 2 + 1e-12


def test_directed_needs_row_residual():
    """Non-symmetric T = Pi^1/2 P Pi^-1/2: the bound with sigma_min(R^M)
    holds, and column-pivoted selection leaves the row residual uncontrolled."""
    T = L.directed_operator(n=80, seed=3)
    assert np.linalg.norm(T, 2) <= 1 + 1e-12
    rows = L.run_chain(T, 1e-4, 8, lambda A: L.truncate_pivoted_qr(A, 1e-4))
    _check_rows([r for r in rows if np.isfinite(r["s_true"])], symmetric=False)
    assert max(r["d_row"] / max(r["d_col"], 1e-300) for r in rows) > 10
