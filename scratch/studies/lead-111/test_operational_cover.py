"""Tests for LEAD-111's operational-cover construction.

Run:  OMP_NUM_THREADS=1 python3 -I -m pytest -q
"""
from __future__ import annotations

from itertools import product

import numpy as np

import operational_cover as oc

# A scenario: X = {a,b,c}, cover M = {{a,b},{b,c}} (overlap {b}).
X = ("a", "b", "c")
M = [("a", "b"), ("b", "c")]


def dist_from_table(U, table):
    """Build a distribution over E(U) from {assignment-tuple: prob}."""
    EU = oc.assignments(U)
    p = np.array([table[tuple(s[x] for x in sorted(U))] for s in EU], float)
    assert abs(p.sum() - 1.0) < 1e-12
    return p


# ---------------------------------------------------------------------------
# 1. Restriction maps form a presheaf: functoriality and identity.
# ---------------------------------------------------------------------------


def test_restriction_identity():
    for U in [("a",), ("a", "b"), ("a", "b", "c")]:
        R = oc.restriction_matrix(U, U)
        assert np.allclose(R, np.eye(len(oc.assignments(U))))


def test_restriction_functoriality():
    # W >= U >= V  =>  res^U_V @ res^W_U == res^W_V
    W = ("a", "b", "c")
    for U in [("a", "b"), ("b", "c"), ("a", "c"), ("a",), ("b",)]:
        for V in [("a",), ("b",), ("c",), ("a", "b"), ("b", "c")]:
            if set(V) <= set(U) <= set(W):
                lhs = oc.restriction_matrix(U, V) @ oc.restriction_matrix(W, U)
                rhs = oc.restriction_matrix(W, V)
                assert np.allclose(lhs, rhs), (U, V)


def test_restriction_preserves_probability():
    # A restriction map sends a distribution to a distribution (columns sum 1).
    R = oc.restriction_matrix(("a", "b", "c"), ("b",))
    assert np.allclose(R.sum(axis=0), np.ones(R.shape[1]))


# ---------------------------------------------------------------------------
# 2. A concrete no-signalling empirical model, and its operational cover.
# ---------------------------------------------------------------------------


def make_model(pab, pbc):
    return {("a", "b"): dist_from_table(("a", "b"), pab),
            ("b", "c"): dist_from_table(("b", "c"), pbc)}


def test_model_is_no_signalling():
    # b-marginal must match across the two contexts. Here P(b=0)=0.5 in both.
    pab = {(0, 0): 0.25, (0, 1): 0.25, (1, 0): 0.25, (1, 1): 0.25}
    pbc = {(0, 0): 0.4, (0, 1): 0.1, (1, 0): 0.1, (1, 1): 0.4}
    model = make_model(pab, pbc)
    assert oc.is_no_signalling(model)


def test_signalling_model_detected():
    pab = {(0, 0): 0.5, (0, 1): 0.0, (1, 0): 0.0, (1, 1): 0.5}  # P(b=0)=0.5
    pbc = {(0, 0): 0.8, (0, 1): 0.0, (1, 0): 0.0, (1, 1): 0.2}  # P(b=0)=0.8
    model = make_model(pab, pbc)
    assert not oc.is_no_signalling(model)


# ---------------------------------------------------------------------------
# 3. The induced sub-cover is a genuine down-closed cover (horn 1 of the lead).
# ---------------------------------------------------------------------------


def test_induced_cover_is_down_closed_and_covers_D():
    # a and b sharp, c flat -> D = {a,b}.  theta = 0.75.
    pab = {(0, 0): 0.05, (0, 1): 0.80, (1, 0): 0.05, (1, 1): 0.10}  # a=0:0.85 b=1:0.90
    pbc = {(0, 0): 0.05, (0, 1): 0.05, (1, 0): 0.45, (1, 1): 0.45}  # b=1:0.90 c:0.5/0.5
    model = make_model(pab, pbc)
    assert oc.is_no_signalling(model)
    theta = 0.75
    D = oc.operational_cover(model, X, theta)
    assert D == frozenset({"a", "b"})  # c is indeterminate (0.5 < 0.75)
    assert oc.is_down_closed_subpresheaf(M, D)
    cover = oc.induced_cover(M, D)
    # faces: {a,b}&D={a,b}; {b,c}&D={b}; maximal face is {a,b}
    assert frozenset({"a", "b"}) in cover
    # restriction maps on the induced cover are still a presheaf
    R1 = oc.restriction_matrix(("a", "b"), ("b",))
    R2 = oc.restriction_matrix(("a", "b"), ("a",))
    assert R1.shape == (2, 4) and R2.shape == (2, 4)


def test_full_scenario_recovered_when_all_determinate():
    # Everything sharp -> D = X, induced cover = M. Independent margins
    # P(a=0)=P(b=0)=P(c=0)=0.9, consistent on b.
    pab = {(0, 0): 0.81, (0, 1): 0.09, (1, 0): 0.09, (1, 1): 0.01}
    pbc = {(0, 0): 0.81, (0, 1): 0.09, (1, 0): 0.09, (1, 1): 0.01}
    model = make_model(pab, pbc)
    assert oc.is_no_signalling(model)
    D = oc.operational_cover(model, X, 0.75)
    assert D == frozenset(X)
    assert oc.induced_cover(M, D) == {frozenset(c) for c in M}


# ---------------------------------------------------------------------------
# 4. The selection is a thresholded functional of the MODEL on a fixed cover.
#    (horn / reading A: a change of determinacy with M fixed is a model change.)
# ---------------------------------------------------------------------------


def test_operational_cover_changes_with_model_at_fixed_cover():
    # Same scenario (X, M). Two models differing only in distributions give
    # different operational covers -- so the operational cover is a function of
    # the empirical model, not of M.
    sharp = {(0, 0): 0.05, (0, 1): 0.80, (1, 0): 0.05, (1, 1): 0.10}  # b=1:0.9
    flat_b = {(0, 0): 0.25, (0, 1): 0.25, (1, 0): 0.25, (1, 1): 0.25}  # b:0.5/0.5
    pbc_flat = {(0, 0): 0.25, (0, 1): 0.25, (1, 0): 0.25, (1, 1): 0.25}
    pbc_sharp = {(0, 0): 0.05, (0, 1): 0.05, (1, 0): 0.45, (1, 1): 0.45}  # b=1:0.9
    e = make_model(sharp, pbc_sharp)   # b determinate
    e2 = make_model(flat_b, pbc_flat)  # b indeterminate
    assert oc.is_no_signalling(e) and oc.is_no_signalling(e2)
    Ke = oc.operational_cover(e, X, 0.75)
    Ke2 = oc.operational_cover(e2, X, 0.75)
    assert "b" in Ke and "b" not in Ke2
    assert Ke != Ke2  # M is identical; only the model changed


# ---------------------------------------------------------------------------
# 5. theta-dependence (monotone shrink) and non-injectivity: a thresholded
#    readout, not a canonical functor model -> cover.
# ---------------------------------------------------------------------------


def test_operational_cover_monotone_in_theta():
    pab = {(0, 0): 0.05, (0, 1): 0.80, (1, 0): 0.05, (1, 1): 0.10}  # a=0:0.85 b=1:0.90
    pbc = {(0, 0): 0.05, (0, 1): 0.05, (1, 0): 0.45, (1, 1): 0.45}  # b=1:0.90 c=0:0.5 indet
    model = make_model(pab, pbc)
    assert oc.is_no_signalling(model)
    covers = [oc.operational_cover(model, X, t) for t in (0.5, 0.75, 0.86, 0.95)]
    # as theta rises the determinable set can only shrink
    for lo, hi in zip(covers, covers[1:]):
        assert hi <= lo
    assert covers[0] >= covers[-1]


def test_selection_not_injective():
    # Two distinct models with the same operational cover at a fixed theta.
    pab1 = {(0, 0): 0.05, (0, 1): 0.80, (1, 0): 0.05, (1, 1): 0.10}  # a=0:.85 b=1:.9
    pab2 = {(0, 0): 0.02, (0, 1): 0.88, (1, 0): 0.05, (1, 1): 0.05}  # a=0:.90 b=1:.93
    pbc = {(0, 0): 0.05, (0, 1): 0.05, (1, 0): 0.45, (1, 1): 0.45}  # b=1:.9 c flat
    pbc2 = {(0, 0): 0.03, (0, 1): 0.02, (1, 0): 0.45, (1, 1): 0.50}  # b=1:.95 c flat
    e1 = make_model(pab1, pbc)
    e2 = make_model(pab2, pbc2)
    # make both no-signalling by matching b-marginals is not required for the
    # determinacy readout, but check the covers coincide while models differ.
    t = 0.75
    assert oc.operational_cover(e1, X, t) == oc.operational_cover(e2, X, t)
    # the distributions themselves differ
    assert not np.allclose(e1[("a", "b")], e2[("a", "b")])
