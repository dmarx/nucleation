---
status: Active
title: 'A pseudorandom generator''s output against uniform strings: almost disjoint
  in total variation, indistinguishable to every efficient test if the generator
  is secure'
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- information-theory
date: '2026-10-15'
line: formal-apparatus
summary: >-
  A15 §2's witness, which A15 recommended filing "with its cryptographic assumption
  explicitly stated". It grounds [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) and, by the record's own reduction,
  [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md).
supports:
- CLAIM-tmpvdl53
- CLAIM-tmpzk2fj
---

# CASE-tmp51hxx: A pseudorandom generator's output against uniform strings: almost disjoint in total variation, indistinguishable to every efficient test if the generator is secure

## The case

G: {0,1}ⁿ → {0,1}²ⁿ. P = G(Uₙ), Q = U₂ₙ. G's image has at most 2ⁿ
elements out of 2²ⁿ, so the test "y is in the image of G" separates them
with TV(P, Q) ≥ 1 − 2⁻ⁿ. If G is a secure pseudorandom generator, every
probabilistic polynomial-time distinguisher D has |Pr[D(G(Uₙ)) = 1] −
Pr[D(U₂ₙ) = 1]| ≤ negl(n).

## What it can show

That statistical difference does not imply efficient distinguishability,
and so that agreement under feasible tests does not imply identity of
the distributions. A15: "This is conditional on the existence of a
secure generator, not an unconditional theorem that a specific practical
generator is secure."

## What it cannot show

Anything about language or minds. A15: the construction is "a
mathematical construction ... not an empirical demonstration about
language." And the gap depends on the representation: given an
expensively computed label, the same pair is trivially separable.
