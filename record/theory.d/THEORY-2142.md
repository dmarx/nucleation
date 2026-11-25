---
number: 2142
status: Proposed
formerly:
- THEORY-tmpq3h4k
promote_when: >-
  A reading of the full text confirming Theorems 16 and 18, Lemma 28 and
  Theorems 29–30 as stated, and that the paper places no constraint on the
  kernel component beyond the invariance or conservation property.
title: 'Ergodicity coefficients are induced seminorms'
statement: >-
  De Pasquale, Smith, Bullo and Valcher show that ergodicity coefficients
  are induced matrix seminorms and that projection and distance seminorms
  are dual, so one coefficient bounds both averaging and the flow of
  distributions, and that in systems leaving a seminorm's kernel or its
  complement invariant only the part off the kernel contracts, while
  differences along it may persist or grow
version: 1
tags:
- control-theory
- mathematics
- probabilistic-modeling
date: '2026-11-21'
source:
- LIT-2953
summary: >-
  The discrete-time, Markov-side sibling of [THEORY-2143](THEORY-2143.md). It joins
  averaging and distribution flows in one seminorm framework, and confirms
  that semicontraction is a statement about forgetting off a kernel, not
  about what is kept on it. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2044 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2143 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2142: Ergodicity coefficients are induced seminorms

## Source

De Pasquale, Smith, Bullo and Valcher, [LIT-2953](../literature.d/LIT-2953.md), read in [NOTE-2231](../notes.d/NOTE-2231.md) from arXiv 2201.03103v3 (20 Dec 2022), which extends the submitted IEEE TAC version.

## What was actually shown

Theorems 16 and 18: τq(K, A) is an induced matrix seminorm, and projection and distance seminorms are dual, so τ₁ is the contraction factor for x ↦ Ax in the ℓ∞ distance seminorm and for π ↦ Aᵀπ in total variation. Lemma 28 and Theorems 29–34: under invariance or conservation of the kernel, only the perpendicular part contracts.

## What this does not say

It does not say what a semicontracting chain's limit keeps of its start, has no stochastic or information-theoretic content, and does not treat approximate invariance.

## Connections

[THEORY-2143](THEORY-2143.md) (the continuous-time sibling, its ref [17]); [THEORY-960](THEORY-960.md); [THEORY-2044](THEORY-2044.md) (partial contraction, contrasted in the text); [CLAIM-635](../claims.d/CLAIM-635.md) and [CLAIM-270](../claims.d/CLAIM-270.md) (what the record holds on retention, which this does not address); [CLAIM-260](../claims.d/CLAIM-260.md) (nonexpansive later kernels, which τ₁ ≤ 1 gives for stochastic matrices).
