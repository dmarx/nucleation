---
status: Active
title: 'Equivalence under feasible tests can be much coarser than statistical equivalence:
  if pseudorandom generators exist, there are pairs of distributions almost disjoint
  in total variation that no efficient test tells apart'
version: 1
role: thesis
defeated_if: >-
  An error in the counting bound, or a proof that secure pseudorandom generators
  do not exist, which would remove the witness without touching the definitional
  half.
tags:
- mathematics
- information-theory
- epistemology
date: '2026-10-15'
line:
- formal-apparatus
grounds:
- CASE-tmp51hxx
- LIT-tmpfy61e
complements:
- CLAIM-264
summary: >-
  A15's witness for "Complexity changes what we mean by an observable", which the
  owner asked to have developed at U15. [CLAIM-264](CLAIM-264.md) says agreement on a restricted
  probe family is coarser than identity. Computational indistinguishability gives
  a restriction that is not chosen but forced, by feasibility. The separation is
  conditional on secure pseudorandom generators, which is an assumption of cryptography
  and not a theorem.
supports:
- CLAIM-tmpzk2fj
---
<!-- inactive-ok-file: LIT-tmpfy61e — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-264 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-tmpvdl53: Equivalence under feasible tests can be much coarser than statistical equivalence: if pseudorandom generators exist, there are pairs of distributions almost disjoint in total variation that no efficient test tells apart

## The claim

A15 §1: for observation channels K_x, K_x′ and a test family F_r, let
d_r(x, x′) = sup over f in F_r of |E[f | x] − E[f | x′]|. Over all tests
this is total variation. Restricting the family cannot increase it, and
nested families give a distance that grows with r. "The conclusion is not
that the states became different. It's that a new distinction became
operationally observable."

The witness ([CASE-tmp51hxx](../cases.d/CASE-tmp51hxx.md), A15 §2). Let G: {0,1}ⁿ → {0,1}²ⁿ, P = G(Uₙ),
Q = U₂ₙ. G has at most 2ⁿ outputs, so the test "is y in the image of G"
gives TV(P, Q) ≥ 1 − 2ⁿ/2²ⁿ = 1 − 2⁻ⁿ. If G is a secure pseudorandom
generator, every probabilistic polynomial-time test has negligible
advantage, by definition. So the two distributions are almost perfectly
distinguishable and practically indistinguishable.

A15 added the invariance that keeps this from being arbitrary: an
efficient transformation applied to both preserves computational
indistinguishability, since a distinguisher for the outputs composed with
the transformation would distinguish the inputs. "Efficient
postprocessing cannot reveal a computational distinction that no
efficient algorithm could previously detect."

## Why it is Active

The counting is checked here, and the rest is the definition of a secure
generator (Goldreich, [LIT-tmpfy61e](../literature.d/LIT-tmpfy61e.md), registered unread). The claim is the
conditional, and it says so in its title.

## What it does not say

- Not that a distinction no efficient test sees is unreal. A15: "The
  distributions are not identical."
- Not that it depends on the objects alone. It is relative to the
  computational model, the encoding and any auxiliary information; an
  expensively computed label makes the same pair trivially
  distinguishable (A15 §3).
- Not quantum contextuality, ontological identity or pragmatic
  equivalence. A14: "Each stronger interpretation requires its own
  arguments and tests."
