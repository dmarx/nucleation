---
number: 372
status: Active
formerly:
- CLAIM-tmp496tl
title: 'Within a fixed measurement scenario, the contextual fraction is a piecewise-linear and Lipschitz-continuous function of the empirical model''s probability table, with a constant that depends only on the scenario'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-165 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-165.yaml, batch 005, ADR-047).
    THEORY-165 called piecewise linearity and the Lipschitz bound "the
    reader's derivation from strong duality, not stated in the paper". A
    result the record proves belongs in a CLAIM (ADR-032). The proof below
    was checked for the review. It shows strong duality from feasibility and
    boundedness, so it does not lean on the paper's supplemental proof.
    THEORY-165 keeps what LIT-265 proves.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: an empirical model on a fixed scenario where
  the dual minimum is not attained at a vertex of {y ≥ 0 : Mᵀy ≥ 1}, or a
  pair of empirical models whose contextual fractions differ by more than
  (max_k ‖y_k‖₁)·‖v_e − v_e′‖_∞.
tags:
- contextuality
- mathematics
date: '2026-10-19'
line: formal-apparatus
grounds:
- LIT-265
summary: >-
  The record's own derivation, from the linear programme of Abramsky,
  Barbosa and Mansfield ([LIT-265](../literature.d/LIT-265.md), Eq. 3), which [THEORY-165](../theory.d/THEORY-165.md) holds. The
  non-contextual fraction is the minimum of the dual objective over
  finitely many vertices, so it is concave and piecewise linear in the
  probability table, and the contextual fraction is Lipschitz in it. The
  constant is the largest ℓ₁ norm of a dual vertex, which depends only on
  the scenario and is not bounded here. Nothing here crosses scenarios or
  applies to signalling data.
---

# CLAIM-372: Within a fixed measurement scenario, the contextual fraction is a piecewise-linear and Lipschitz-continuous function of the empirical model's probability table, with a constant that depends only on the scenario

## The claim

Fix a measurement scenario with incidence matrix M. Its rows are the pairs
(context C, joint outcome of C), and its columns are the global assignments
g. The entry is 1 when g restricted to C gives that outcome. An empirical
model e is the vector v_e ≥ 0 of its context-wise probabilities. As in
[LIT-265](../literature.d/LIT-265.md), Eq. 3,

NCF(e) = max { 1·b : Mb ≤ v_e, b ≥ 0 },  CF(e) = 1 − NCF(e).

Let y₁, …, y_K be the vertices of the dual polyhedron
P = { y ≥ 0 : Mᵀy ≥ 1 }. Then:

1. NCF(e) = min_k y_k·v_e, so NCF is concave and piecewise linear in v_e,
   and CF is convex and piecewise linear.
2. |CF(e) − CF(e′)| ≤ (max_k ‖y_k‖₁)·‖v_e − v_e′‖_∞ for any two empirical
   models on the scenario.

## Proof

**The primal is feasible and bounded.** b = 0 is feasible. Each column of M
has exactly one 1 among the rows of any one context C, because a global
assignment gives one outcome on C. So summing the rows of C in Mb ≤ v_e
gives 1·b ≤ Σ_(rows of C) v_e = 1. A feasible, bounded linear programme has
a dual that attains the same value:
NCF(e) = min { y·v_e : y ∈ P }.

**The dual minimum is at a vertex.** P is nonempty. Take the indicator y of
the rows of one context: each column has exactly one 1 there, so Mᵀy = 1.
P lies in the nonnegative orthant, so it contains no line. It is therefore
the convex hull of its finitely many vertices plus its recession cone, and
the recession cone is nonnegative. Since v_e ≥ 0, moving along a recession
direction does not lower y·v_e. So the minimum is attained at a vertex, and
NCF(e) = min_k y_k·v_e.

**Piecewise linearity and the bound.** A minimum of finitely many linear
functions is concave and piecewise linear, which gives (1). For (2),
|min_k a_k − min_k b_k| ≤ max_k |a_k − b_k|, and
|y_k·(v_e − v_e′)| ≤ ‖y_k‖₁ ‖v_e − v_e′‖_∞.

Convexity under mixing also follows from (1). It agrees with [LIT-265](../literature.d/LIT-265.md)'s
Theorem 2, which [THEORY-165](../theory.d/THEORY-165.md) holds.

## What it does not say

- **How large the constant is.** It is the largest ℓ₁ norm of a dual
  vertex, a property of the scenario that this does not bound. In a
  sample of 300 random mixtures on CHSH, the largest ‖y*‖₁ seen was 8
  ([THEORY-165](../theory.d/THEORY-165.md)'s check), and that is not the constant.
- **Anything about the underlying states or chains.** The bound is in the
  empirical table. A drift result must first bound the change in every
  context's distribution.
- **Anything across scenarios, or for signalling data,** where CF is
  undefined.
- **That the decomposition varies continuously.** Only its weight does.
