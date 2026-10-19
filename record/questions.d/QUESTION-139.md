---
number: 139
status: Open
formerly:
- QUESTION-tmpg2gry
title: 'Does the one-hidden-layer lower bound of ∏(rᵢ+1) neurons for the monomial x₁^r₁⋯xₙ^rₙ hold for uniform approximation on a box, and not only for Taylor matching at the origin, and what replaces it when hidden units have biases?'
version: 1
tags:
- mathematics
- learning-theory
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The open half of [THEORY-206](../theory.d/THEORY-206.md)'s former promotion condition. On 2026-10-19
  [THEORY-206](../theory.d/THEORY-206.md) was narrowed to the Taylor-matching bound for bias-free
  networks, which Rolnick and Tegmark prove and the record re-derived, and
  promoted. Their uniform lower bound rests on a step that fails, and the
  biased case is untreated. Both are here.
---

# QUESTION-139: Does the one-hidden-layer lower bound of ∏(rᵢ+1) neurons for the monomial x₁^r₁⋯xₙ^rₙ hold for uniform approximation on a box, and not only for Taylor matching at the origin, and what replaces it when hidden units have biases?

## Why it is a question

[THEORY-206](../theory.d/THEORY-206.md) holds Rolnick and Tegmark's bound ([LIT-890](../literature.d/LIT-890.md), Theorem 4.2, read in
[NOTE-693](../notes.d/NOTE-693.md)) in the sense their proof reaches. A bias-free one-hidden-layer
network of smooth units whose degree-d Taylor polynomial at the origin is
the monomial needs exactly ∏(rᵢ+1) neurons. Until 2026-10-19 [THEORY-206](../theory.d/THEORY-206.md)'s
promotion condition also asked for the uniform and biased versions, which
are different theorems. At the owner's direction, from the promotion
audit's batch-006 decision ([ADR-047](../decisions.d/ADR-047.md)), the Taylor-sense result was promoted
alone, and the rest moved here unchanged.

It is open because the source does not settle it. Theorem 4.1 claims the
uniform lower bound, but its proof assumes that uniform closeness on a box
forces the Taylor coefficients close. That fails for networks in general:
ε·tanh(x/ε²) is within ε of 0, with first Taylor coefficient 1/ε ([NOTE-693](../notes.d/NOTE-693.md),
claim C3, "weak as proved"). With biases, each unit is expanded about a
different point, and the rank argument does not apply as stated.

## What would answer it

[THEORY-206](../theory.d/THEORY-206.md)'s former condition, unchanged. A proof, read and checked, that
the lower bound ∏(rᵢ+1) for one hidden layer holds for uniform
approximation on a box, and either that it survives hidden-layer biases or
a statement of what replaces it with them. Against it: a family of
one-hidden-layer networks with fewer neurons converging uniformly to a
monomial, or a bias-free construction beating the bound. More
trained-network experiments on products cannot settle it, since they
measure what training finds, not what exists.
