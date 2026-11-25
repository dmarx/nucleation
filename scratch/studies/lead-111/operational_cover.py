"""LEAD-111: the operational cover as the determinacy sub-cover of a scenario.

A measurement scenario in the Abramsky-Brandenburger sense (THEORY-012, LIT-016,
and TERM-042's communicative object) is a triple (X, M, O):

  X  a finite set of measurements,
  M  a cover: a family of maximal *contexts*, subsets of X of jointly
     performable measurements, with union X,
  O  an outcome set per measurement (here binary {0,1}).

The event presheaf is E(U) = prod_{x in U} O_x for U subset of X, with the
restriction map res^U_V : E(U) -> E(V) for V subset of U given by dropping the
coordinates outside V. An empirical model e assigns each context C in M a
distribution e_C over E(C); it is no-signalling when the e_C agree on the
marginals of shared measurements.

CLAIM-201 defines, operationally, a context as "a question whose answers
readers give determinately": agreement among readers above a threshold theta
fixed in advance. This module makes that precise and tests whether the
resulting "operational cover" is a cover with restriction maps.

Determinacy functional (per singleton measurement x):
    det_theta(e, x)  =  [ max_o  margin(e, x)(o)  >=  theta ].
Operational cover:
    K_theta(e) = { x in X : det_theta(e, x) }           (the determinable base)
    induced sub-scenario on D = K_theta(e):
        contexts  M|_D = { C & D : C in M }  (nonempty),
        restriction maps inherited from the event presheaf.

The functions below build these objects and expose the facts the two readings
of LEAD-111 rest on. See README.md for how to run.

Run with:  OMP_NUM_THREADS=1 python3 -I operational_cover.py
"""
from __future__ import annotations

from itertools import product

import numpy as np

# ---------------------------------------------------------------------------
# Event presheaf and restriction maps
# ---------------------------------------------------------------------------


def assignments(U):
    """All local assignments E(U) = {0,1}^U, as tuples ordered by sorted(U)."""
    xs = tuple(sorted(U))
    return [dict(zip(xs, vals)) for vals in product((0, 1), repeat=len(xs))]


def restrict_assignment(s, V):
    """res^U_V on an assignment s (a dict over U): drop coords outside V."""
    return {x: s[x] for x in V}


def restriction_matrix(U, V):
    """Matrix R (|E(V)| x |E(U)|) pushing a distribution on E(U) to E(V).

    (R @ p)[t] = sum of p[s] over s in E(U) with res^U_V(s) = t.  This is the
    marginalization that realizes the presheaf action on distributions.
    """
    assert set(V) <= set(U)
    EU, EV = assignments(U), assignments(V)
    idxV = {tuple(sorted(t.items())): i for i, t in enumerate(EV)}
    R = np.zeros((len(EV), len(EU)))
    for j, s in enumerate(EU):
        t = restrict_assignment(s, V)
        R[idxV[tuple(sorted(t.items()))], j] = 1.0
    return R


def marginal(dist, U, x):
    """Marginal distribution of measurement x from a distribution over E(U)."""
    R = restriction_matrix(U, {x})
    m = R @ dist
    # E({x}) is ordered [{x:0}, {x:1}]
    return m


# ---------------------------------------------------------------------------
# Empirical model, determinacy, operational cover
# ---------------------------------------------------------------------------


def is_no_signalling(model, tol=1e-9):
    """model: dict C(tuple) -> distribution over E(C). Agree on shared margins."""
    contexts = list(model)
    for i in range(len(contexts)):
        for j in range(i + 1, len(contexts)):
            Ci, Cj = contexts[i], contexts[j]
            shared = set(Ci) & set(Cj)
            for x in shared:
                mi = marginal(model[Ci], Ci, x)
                mj = marginal(model[Cj], Cj, x)
                if not np.allclose(mi, mj, atol=tol):
                    return False
    return True


def det_theta(model, x, theta):
    """Is measurement x determinately answerable at threshold theta?

    Uses any context containing x (well-defined under no-signalling).
    """
    for C in model:
        if x in C:
            m = marginal(model[C], C, x)
            return float(np.max(m)) >= theta
    raise KeyError(f"no context contains {x}")


def operational_cover(model, X, theta):
    """K_theta(e): the set of determinable measurements (the operational base)."""
    return frozenset(x for x in X if det_theta(model, x, theta))


def induced_cover(M, D):
    """M|_D = { C & D : C in M, nonempty }, the induced cover on D.

    Returns the maximal faces (drop any C&D contained in another).
    """
    faces = {frozenset(C) & frozenset(D) for C in M}
    faces.discard(frozenset())
    maximal = {f for f in faces if not any(f < g for g in faces)}
    return maximal


def is_down_closed_subpresheaf(M, D):
    """The induced sub-scenario is closed under restriction within subsets of D.

    For every context face F in M|_D and every subset V of F, V is a subset of
    some face of M|_D (trivially F itself), and E(V) with res^F_V is defined.
    The point to verify is that D together with M|_D forms a genuine
    sub-simplicial-complex: every face sits inside D, and restriction never
    leaves D.  This is immediate but we check it rather than assert it.
    """
    cover = induced_cover(M, D)
    Dset = frozenset(D)
    for F in cover:
        if not (F <= Dset):
            return False
        # every subset V of F stays in D and has a well-defined restriction
        for r in range(len(F) + 1):
            from itertools import combinations

            for V in combinations(sorted(F), r):
                if not (frozenset(V) <= Dset):
                    return False
    # union of faces must cover D
    union = frozenset().union(*cover) if cover else frozenset()
    return union == Dset
