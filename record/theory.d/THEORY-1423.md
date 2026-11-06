---
number: 1423
status: Active
formerly:
- THEORY-tmps6lqg
title: 'Berry, Lee-Trimble and Santangelo find that near the flat state a non-intersecting rigid origami vertex with small positive Gaussian curvature has a configuration space split into two components (popped up and popped down) that no rigid, non-tearing motion joins, while for small negative curvature the two stay joined by a neck, except at a degree-four vertex, which is split for both signs'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the twenty-fifth status review (ADR-057,
    ADR-065), at the status review's ruling (the owner delegated these
    rulings). Old title: "Berry, Lee-Trimble and Santangelo show that near
    the flat state a non-intersecting rigid origami vertex with positive
    Gaussian curvature has a configuration space split into two components
    (popped up and popped down) that no rigid, non-tearing motion joins,
    while a negative-curvature vertex's components stay joined by a neck".
    'Show' becomes 'find', and the curvature is small, as the paper's
    expansion requires. The negative clause is corrected for degree four,
    which §II finds split for both signs (ADR-047 kind 3, a mis-statement:
    noted here only). The old condition, "An independent derivation or
    simulation confirming that, for small positive vertex curvature and
    fold angles held in (−π, π), the popped-up and popped-down nappes of a
    single rigid origami vertex near the flat state are disconnected, and
    that for small negative curvature they are connected.", asks for an
    independent test of a result the source asserts. It moves word for
    word to THEORY-tmpi4xzs, which extends this entry (ADR-047 kind 1).
    Read in full in NOTE-1605 (arXiv v1).
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
source:
- LIT-2024
summary: >-
  Berry, Lee-Trimble and Santangelo (2020), [LIT-2024](../literature.d/LIT-2024.md), read in full in
  [NOTE-1605](../notes.d/NOTE-1605.md) (arXiv v1). Active on its reading (ADR-065); whether the
  result holds is THEORY-tmpi4xzs's. The single-vertex result follows from
  the second-order condition hᵀQh = K, whose proof to quadratic order the
  authors call somewhat involved, and is confirmed numerically on one
  symmetric 5-fold vertex. It does not say anything far from the flat state
  or at large curvature, it does not hold when faces may pass through each
  other, and its multi-vertex extension is conditional.
---

# THEORY-1423: Berry, Lee-Trimble and Santangelo find that near the flat state a non-intersecting rigid origami vertex with small positive Gaussian curvature has a configuration space split into two components (popped up and popped down) that no rigid, non-tearing motion joins, while for small negative curvature the two stay joined by a neck, except at a degree-four vertex, which is split for both signs

## Source

Berry, Lee-Trimble and Santangelo (2020), [LIT-2024](../literature.d/LIT-2024.md); read in [NOTE-1605](../notes.d/NOTE-1605.md).

## What was actually shown

- **The condition** (§I, eq. 4, App. A): to second order, hᵀQ_n h = K_n at
  each internal vertex, Q_n with one negative eigenvalue.
- **Single vertex** (§II, eqs. 9–10): for K > 0 the solution set is a
  two-sheeted hyperboloid and "the two nappes have split into two
  disconnected components"; for K < 0 a one-sheeted hyperboloid, the
  nappes "connected by a neck".
- **Numerics** (§II): a symmetric 5-fold vertex traced with fold angles in
  (−π, π) agrees.
- **Degree 4** (§II): disconnected for both signs of K.
- **Several vertices** (§III): branches told apart by a K > 0 vertex's nappe
  are disconnected, assuming two distinct real solutions for each vertex
  height.

## What this does not say

- Anything far from the flat state or for large curvature.
- That the separation survives when faces may pass through each other; by
  the authors' anecdote it does not.
- That every combination of nappes is realizable in a multi-vertex pattern,
  or that negative-curvature patterns stay connected globally.
- That curvature in fact reduces misfolding; that is proposed for future
  work.
