---
status: Proposed
title: 'If restating an entry adds an error and then enforces its predicates, each a projection onto the closed convex set of versions passing its test, then every version reached lies in the intersection of those sets, the step''s fixed points are exactly that intersection, drift from a start inside it is bounded by its diameter, and each added predicate can only shrink it; a predicate enforced softly, by a penalty of strength λ on distance from its set, leaves versions outside by an amount that falls with λ and has the hard predicate as its limit; and a predicate enforced on every entry keeps nothing of where an entry started, while one whose outcome the step copies keeps it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the monotonicity of an intersection under
  an added set; in the fixed-point set of a composition of projections onto
  closed convex sets with a common point being their intersection; in the
  drift bound for a map into a bounded set; in the proximal map of
  (λ/2)·dist² to a closed convex set being (y + λP(y))/(1 + λ); or in the
  step from a constant indicator to zero information about the start, or
  from a preserved, non-constant indicator to CLAIM-635's retention.
tags:
- mathematics
- design-rationale
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
- record-as-apparatus
rests_on:
- CLAIM-635
- CLAIM-773
uses:
- TERM-tmp7m4at
- TERM-132
summary: >-
  The formal half of the owner's reframe of 2026-11-21, that adding
  predicates to an entry is adding constraints: with each predicate read as
  a test and enforced as a projection, the predicates set the fixed points
  of restating, an added predicate shrinks them, soft and hard enforcement
  are one penalty at different strengths, and enforcing a predicate differs
  from preserving it as contraction differs from conservation ([CLAIM-772](CLAIM-772.md)).
  Proved from standard convex analysis and checked numerically. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-772 CLAIM-773 TERM-tmp7m4at — Proposed; the contraction claims this formalizes for predicates, and the entries filed with it on 2026-11-21 -->

# CLAIM-tmp8v75o: If restating an entry adds an error and then enforces its predicates, each a projection onto the closed convex set of versions passing its test, then every version reached lies in the intersection of those sets, the step's fixed points are exactly that intersection, drift from a start inside it is bounded by its diameter, and each added predicate can only shrink it; a predicate enforced softly, by a penalty of strength λ on distance from its set, leaves versions outside by an amount that falls with λ and has the hard predicate as its limit; and a predicate enforced on every entry keeps nothing of where an entry started, while one whose outcome the step copies keeps it

## The claim

Let a version of an entry be a point x of a finite-dimensional space, and
let each of its predicates p define, as a test ([TERM-tmp7m4at](../terms.d/TERM-tmp7m4at.md)), a closed
convex set A_p of versions that pass. Let A = ∩ A_p be non-empty, and let
P_p be the nearest-point projection onto A_p. A restatement is
x' = T(x + ξ): an error ξ, then enforcement T, the limit of cyclic sweeps
of the P_p, which maps every point into A.

1. **Shrinking.** Adding a predicate q replaces A by A ∩ A_q ⊆ A, so the
   allowed versions, and their diameter, can only shrink.
2. **Fixed points.** Without error, the versions the step leaves where they
   are are exactly A. Each P_p fixes A_p pointwise, so every point of A is
   fixed by every sweep; conversely, projections onto closed convex sets
   are firmly nonexpansive, and for such maps with a common fixed point the
   fixed points of their composition are the intersection of theirs, so a
   point outside A is moved. Cyclic projections converge to a point of A
   (in finite dimension). The predicates set the fixed points of restating;
   inside A, nothing holds a version, and A is what is left free.
3. **Drift.** With error, every version reached after the first step lies
   in A, so from a start x₀ in A, |xₙ − x₀| ≤ diam A for every n: drift
   saturates, the first of [CLAIM-773](CLAIM-773.md)'s kinds, with the ceiling set by the
   predicates. Along a direction no predicate bounds, A is unbounded and the
   feature drifts as a random walk, √n ([CLAIM-779](CLAIM-779.md)). A predicate that fixes a
   feature's value leaves it no drift at all.
4. **Soft enforcement.** Replace the hard projection onto A_p by a penalty
   (λ/2)·dist(x, A_p)². For closed convex A_p its proximal map is
   x ↦ (y + λP_p(y))/(1 + λ), which moves a point a fraction λ/(1 + λ) of the
   way to the set. As λ → ∞ this is P_p. A prose convention and a lint rule
   are the same predicate at different λ.
5. **Enforcing and preserving.** If the step enforces p on every entry,
   f_p(xₙ) = 1 for every n ≥ 1 whatever x₀ was, so the test's outcome
   carries no information about the start: the feature is in the
   contracting part, at the predicate's value. If instead the step copies
   the outcome (K f_p = f_p) and f_p is not constant on the starting law,
   [CLAIM-635](CLAIM-635.md) gives information about the start bounded below at every
   generation: the feature is in the conserved part. Enforcing p onto a
   value taken from the entry's source, rather than from the schema, holds
   every version to the source: the anchoring case of [CLAIM-772](CLAIM-772.md)'s one
   contraction.

Parts 1, 3 and 5 need only that T maps into A, not convexity. Parts 2 and 4
need it.

## Checks

Run under `python3 -I` on 2026-11-21 with numpy (script in the curation entry
of 2026-11-21, 031543). In six dimensions, 2,000 versions started at the
origin, error σ = 0.05 per step for 400 steps, enforcement by five cyclic
sweeps over a ball of radius 2 and k random half-spaces through which the
origin is feasible:

- **Shrinking.** Mean drift 1.72, 1.62, 1.56, 1.21 and 1.03, and mean spread
  0.71, 0.66, 0.62, 0.47 and 0.41, for k = 0, 4, 8, 16 and 24. Maximum drift
  stayed at the ball's radius, 2.0, the bound for a start at its centre.
  Largest violation of any set after five sweeps: at most 4 × 10⁻³.
- **A fixed value.** With one coordinate held at 0.7 (the start's value) or
  at 0 (a convention), it read 0.700 or 0.000 at the end, while a free
  coordinate drifted with spread 1.02 and 1.03 against σ√n = 1.00.
- **Soft enforcement,** k = 24. Mean distance outside A at the end: 0.084,
  0.011, 0.0012, 0.0001 and 0.0000 for λ = 0.1, 1, 10, 100 and 10⁴, falling
  roughly as 1/λ.

## What it does not say

- Not that restating an entry is this map. It is a model: what a session
  does when it revises an entry is not a projection, and the record's
  enforcement is partial.
- Not that the record's predicates have convex sets. Categorical fields and
  tags do not. Shrinking, the drift bound and the enforce-or-preserve
  distinction hold for any enforcement that maps into A; the fixed-point
  identity and the soft-to-hard limit were shown for convex sets only.
- Not what happens when the predicates conflict. If A is empty there is no
  version to converge to; on the record that is an objection, not a model
  result.
- Not the rate at which soft enforcement approaches the hard one; 1/λ is
  what the run showed, not a derived rate.
