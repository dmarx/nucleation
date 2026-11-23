---
status: Active
title: 'Linear tests are not closed under pointwise minimum or maximum, so a lattice whose concepts each have a linear test cannot in general give its meets and joins linear tests; this does not tell against Xiong''s lattice representation hypothesis as stated, whose meet is already an intersection of half-spaces and not a direction'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from A29 §4 of the exchange "Explain
    First Contact RL" (ChatGPT, shared 2026-11-22), with the assistant's
    check of what the hypothesis states (LIT-267, THEORY-698).
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): counterexample checked; premise CLAIM-
    tmpfza2h promoted in the same change, ground THEORY-698 Active.
role: thesis
warrant: demonstrated
defeated_if: >-
  Two linear functionals on ℝ^d whose pointwise maximum or minimum is
  linear without one dominating the other everywhere; or a statement in
  Xiong's paper that meets or joins of concepts are themselves single
  linear directions, which would turn the second half into an objection
  to it.
tags:
- representation-learning
- mathematics
- logic
date: '2026-11-22'
line:
- learned-structure
- formal-apparatus
rests_on:
- CLAIM-tmpfza2h
grounds:
- THEORY-698
summary: >-
  A29 §4 of the exchange "Explain First Contact RL" (2026-11-22): "the
  pointwise maximum of two linear test functions is generally not linear.
  So a simple LRH does not automatically supply linear directions for
  every meet or join", which A29 called "an important possible failure of
  the lattice representation hypothesis if one interprets it as claiming
  that lattice composition is itself implemented by linear operations."
  The first half is demonstrated. The assistant checked the condition:
  Xiong ([LIT-267](../literature.d/LIT-267.md), read in [THEORY-698](../theory.d/THEORY-698.md)) takes the meet as a half-space
  intersection, a polyhedral cone and not one direction, and the join as a
  union of cones "approximated by the conic hull", which [THEORY-698](../theory.d/THEORY-698.md)
  already finds is not a lattice join as written. So the hypothesis as
  stated does not claim linear composition, and the observation is no
  objection to it; it does say why a single-direction join would fail.
  The wording is A's (ChatGPT, in the exchange of 2026-11-22), except the
  check, which is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: LIT-267 — Proposed; the paper this checks, and the lattice claim this rests on, filed 2026-11-22 -->

# CLAIM-tmpgnozg: Linear tests are not closed under pointwise minimum or maximum, so a lattice whose concepts each have a linear test cannot in general give its meets and joins linear tests; this does not tell against Xiong's lattice representation hypothesis as stated, whose meet is already an intersection of half-spaces and not a direction

## The claim

max(w₁ᵀx, w₂ᵀx) is convex and piecewise linear, and linear only when one
functional dominates the other everywhere. On x = (1, 0), (0, 1), (1, 1)
with w₁ = (1, −1), w₂ = (−1, 1) the maximum takes 1, 1, 0, where
linearity would need 2 at (1, 1). The same holds for the minimum. So a
family of linear tests is not a sublattice of the graded predicate
lattice ([CLAIM-tmpfza2h](CLAIM-tmpfza2h.md)), and thresholding does not help: the meet of two
half-space predicates is an intersection of half-spaces, generally not a
half-space.

## Whether it tells against the lattice representation hypothesis

A29 made the objection conditional on reading the hypothesis as "lattice
composition is itself implemented by linear operations". Xiong's paper
does not claim that. Its geometric meet is half-space intersection and
its join is a union of cones approximated by their conic hull ([LIT-267](../literature.d/LIT-267.md);
[THEORY-698](../theory.d/THEORY-698.md), which notes that the join so defined is not a lattice join).
Its soft algebra takes meets and joins as pointwise min and max of
profiles (Eq. 6; [NOTE-240](../notes.d/NOTE-240.md)), which are not linear either. The concepts
have linear directions; their meets do not, and the paper does not say
they do. So the observation is no objection to the paper as
written. It is a reason, beside [THEORY-698](../theory.d/THEORY-698.md)'s, that no single-direction
join can be a lattice join of half-space concepts.

## Bearing

A29 drew the lesson for perspectives: "A lattice of perspectives may be
induced by our tests without being a uniquely existing decomposition of
the underlying organization" (§3), from [THEORY-698](../theory.d/THEORY-698.md)'s point that every
incidence relation has a complete concept lattice. That part is held.

## Check

python3 -I: the maximum on the three points is (1, 1, 0) against the 2
linearity requires at (1, 1).
