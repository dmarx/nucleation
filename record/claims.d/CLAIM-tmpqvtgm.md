---
status: Proposed
title: 'Whether several objectives share a strict first-order descent direction is constant on the orbits of any function-preserving symmetry that acts on the parameters as a diffeomorphism, so permutation, positive rescaling across a ReLU and orthogonal maps of a residual stream all leave the verdict unchanged; a frustration residual budgeted in a fixed Euclidean norm is constant on an orbit only where the symmetry''s derivative is orthogonal, so it holds across permutations and orthogonal maps and changes along rescalings'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a function-preserving symmetry σ that is a
  diffeomorphism of the parameter space, with every demand's loss
  invariant under it, at whose orbit points θ and σθ the objectives share
  a strict descent direction at one and not the other; or a symmetry whose
  derivative is orthogonal at which CLAIM-365's residual, in the Euclidean
  norm, differs between θ and σθ. Not defeated by a symmetry that is not a
  diffeomorphism, such as a blow-up (CLAIM-305), which the claim does not
  cover, or by a residual whose metric is carried along by the symmetry,
  which CLAIM-366 already holds invariant.
tags:
- loss-landscapes
- mathematics
- information-geometry
date: '2026-11-07'
line:
- learned-structure
- formal-apparatus
rests_on:
- CLAIM-366
- CLAIM-365
answers:
- QUESTION-127
summary: >-
  A by-product of the second synthesis review of 2026-11-07, where the
  reader of the learned-structure cluster found the cluster did not
  integrate and that one inference from it was new. QUESTION-127 leaves
  open "Whether a frustration verdict is constant on symmetry orbits".
  CLAIM-366 holds the common-descent test invariant under a change of
  chart, the same point described two ways. This claim is about two
  different points of one chart related by a symmetry of the losses, and
  says the unbudgeted verdict is constant on such orbits while a residual
  budgeted in a fixed Euclidean norm is not. The derivation is the
  reader's, checked by the filer and in scratch/formal/orbit_descent_check.py.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-263 CLAIM-555 CLAIM-305 — Proposed; the symmetry group and the neighbouring claims, cited with their standing -->

# CLAIM-tmpqvtgm: Whether several objectives share a strict first-order descent direction is constant on the orbits of any function-preserving symmetry that acts on the parameters as a diffeomorphism, so permutation, positive rescaling across a ReLU and orthogonal maps of a residual stream all leave the verdict unchanged; a frustration residual budgeted in a fixed Euclidean norm is constant on an orbit only where the symmetry's derivative is orthogonal, so it holds across permutations and orthogonal maps and changes along rescalings

## The claim

Let σ be a diffeomorphism of the parameter space Θ with L_i∘σ = L_i for every
demand i: a function-preserving symmetry. The three QUESTION-127 names,
permuting units, rescaling the weights into and out of a ReLU by a > 0 and
1/a, and an orthogonal map on the residual stream, are each a linear
isomorphism of Θ, so each is such a σ.

1. **Common descent is constant on orbits.** Differentiating L_i∘σ = L_i
   gives g_i(θ) = Dσ(θ)ᵀ g_i(σθ), with Dσ(θ) invertible. An invertible
   linear map sends conv{g_i(σθ)} onto conv{g_i(θ)} and 0 to 0, so
   0 ∈ conv{g_i(θ)} exactly when 0 ∈ conv{g_i(σθ)}. By CLAIM-366's criterion,
   the objectives share a strict descent direction at θ exactly when they do
   at σθ.
2. **A budgeted residual in a fixed norm is not.** CLAIM-365's residual
   Φ_r = max over the simplex of Σλᵢεᵢ − r‖Σλᵢgᵢ‖ depends on the gradients'
   norms. Since ‖Dσᵀ g‖ = ‖g‖ for every g only when Dσ is orthogonal, Φ_r in
   the Euclidean norm is constant along permutation and orthogonal orbits and
   changes along rescalings. With f = v·relu(ux), one demand at x = 1, y = 1,
   and a = ½, the squared gradient norm is 612 at (u, v) = (4, 1) and 288 at
   its image (2, 2).
3. **So quotienting before diagnosing matters only for the budgeted test.**
   Dividing by CLAIM-263's symmetry group before testing for common descent
   changes nothing. Before computing a Euclidean Φ_r it changes the value,
   unless the metric is carried along, which is CLAIM-366's "only with the
   metric pulled back".

## Check

scratch/formal/orbit_descent_check.py takes a two-unit ReLU network with
three demands and 300 random parameter points. The chain rule holds at
every point. Common descent, decided by linear programming, agrees across
every rescaling and every swap of the hidden units. The Euclidean Φ_r
differs on 192 of the 300 rescalings and on none of the swaps.

## Relation to the record

- **CLAIM-366** is the premise for item 1. It compares one point in two
  charts. This claim compares two points in one chart, so it does not
  follow from CLAIM-366's statement, only from its criterion with the chain
  rule.
- **CLAIM-555** already says the compatibility complex is unchanged by
  quotienting function-preserving symmetries. Item 1 is the first-order
  counterpart.
- **CLAIM-366's disclaimer** of "Anything about function-preserving
  symmetries" is broader than needed. Its stated reason, that "the map need
  not be a diffeomorphism of the whole space", holds for blow-ups
  (CLAIM-305) and not for the three symmetries QUESTION-127 names.

## What it does not say

- **Anything about symmetries that are not diffeomorphisms**, such as the
  blow-ups of CLAIM-305, or about points where the symmetry's derivative is
  singular.
- **Which test is the right one.** CLAIM-366's own caution stands: the
  unbudgeted first-order test ignores budgets and finite steps.
- **What a practitioner should do.** Like CLAIM-366, this is about the
  learning problem, not an instruction for practice, which belongs to the
  anthology.
