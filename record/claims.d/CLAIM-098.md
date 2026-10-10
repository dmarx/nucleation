---
number: 98
status: Proposed
formerly:
- CLAIM-tmpse4aa
title: 'Translation and cross-modal reconstruction need not be group actions: they form a category or semigroup of directed stochastic transformations, in which invertible symmetries are special cases'
version: 1
role: thesis
defeated_if: >-
  The transformations that matter for communicative fidelity are well
  modelled as invertible maps with exact invariants, so that directed,
  lossy transport adds no predictive power over symmetry alone.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-035
supersedes:
- CLAIM-102
summary: >-
  Manuscript §4. The one trace the relativity analogy left: symmetry and
  equivariance for exact preservation, a semigroup of stochastic maps
  for the rest.
objected_by:
- CLAIM-tmpz7og0
supports:
- CLAIM-tmpt76qw
---
<!-- inactive-ok-file: CLAIM-004 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: CLAIM-102 — Superseded; replaced, and cited as the history this entry answers or replaces -->

# CLAIM-098: Translation and cross-modal reconstruction need not be group actions: they form a category or semigroup of directed stochastic transformations, in which invertible symmetries are special cases

## The claim

Manuscript §4: "translation and cross-modal reconstruction are often
irreversible; their mappings need not be group actions. The more inclusive
notion is a category or semigroup of stochastic transformations, within which
invertible symmetry maps are special cases. We therefore separate (i) exact
preservation, (ii) representation-changing equivariance, (iii) approximate
preservation, and (iv) structural reorganization."

## What it does not say

That no symmetry applies: equivariance is "often more apt than literal
invariance" (§4). Nor does it supply a criterion for telling (ii) from (iv);
[CLAIM-004](CLAIM-004.md) was one.

## A case from structuralist myth analysis

Santucci, Doja and Capocchi ([LIT-807](../literature.d/LIT-807.md)) say their myth variants form a
group, but the operations they implement do not. Replacing one term with
another that is already in the myth merges the two, and nothing can
separate them again. The operations form a monoid, as this claim expects
of transformations in general. This is the reader's observation, not the
paper's.

## Prior statement in Piaget

Piaget's *Structuralism* ([LIT-837](../literature.d/LIT-837.md), skimmed from the publisher's preview,
[NOTE-618](../notes.d/NOTE-618.md)) makes the same distinction on p. 15. Logico-mathematical
structures are fully reversible operations, which are groups. Linguistic and
social transformations are "not entirely reversible".

## Note of 2026-10-10: the replies

[CLAIM-tmpz7og0](CLAIM-tmpz7og0.md) scopes (iii). In total variation, with Markov kernels,
approximate transports compose with ε₁ + ε₂. If TV(K₁#e_A, e_B) ≤ ε₁ and
TV(K₂#e_B, e_C) ≤ ε₂, then

TV(K₂#K₁#e_A, e_C) ≤ TV(K₂#K₁#e_A, K₂#e_B) + TV(K₂#e_B, e_C) ≤ ε₁ + ε₂,

the first step by the triangle inequality and the second because every
Markov kernel is nonexpansive in total variation. So in that setting
approximate transports form a category in which distortions add. For other
distortions, which may lack the triangle inequality or meet expansive
kernels, the category claim waits on [QUESTION-017](../questions.d/QUESTION-017.md). The manuscript's text quoted above is unchanged.
