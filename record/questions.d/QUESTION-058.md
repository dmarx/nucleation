---
number: 58
status: Open
formerly:
- QUESTION-tmpli6go
title: 'When a trained network''s representation carries a group''s structure, how much of it comes from the task, the architecture, the training set''s relations and the symmetry of the update, and how much can be read off the network without supplying the group?'
version: 1
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-022
- THEORY-181
- THEORY-021
- THEORY-184
- THEORY-210
- THEORY-213
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [QUESTION-036](QUESTION-036.md), [CLAIM-137](../claims.d/CLAIM-137.md),
  [CLAIM-132](../claims.d/CLAIM-132.md), [CLAIM-148](../claims.d/CLAIM-148.md), [CLAIM-135](../claims.d/CLAIM-135.md) and [CLAIM-193](../claims.d/CLAIM-193.md). [THEORY-022](../theory.d/THEORY-022.md),
  [THEORY-181](../theory.d/THEORY-181.md), [THEORY-021](../theory.d/THEORY-021.md) and [THEORY-184](../theory.d/THEORY-184.md) answer it in part; the body gives
  each one's limit.
---

# QUESTION-058: When a trained network's representation carries a group's structure, how much of it comes from the task, the architecture, the training set's relations and the symmetry of the update, and how much can be read off the network without supplying the group?

## The question

Trained networks are found with characters of ℤ/p, with circles for months, and with polytopes in superposition. The question is where that structure comes from, and what an analyst can recover from the weights alone. One possible source is the data's symmetry. Others are an operation built into the architecture, the number of relations in the training set, and the equivariance of the update rule.

## Why the record needs it

[QUESTION-036](QUESTION-036.md) asks whether a kind's symmetries can be reconstructed from its realizations. [CLAIM-137](../claims.d/CLAIM-137.md) identifies kinds by character-like invariants, and [CLAIM-132](../claims.d/CLAIM-132.md) limits what characters fix. Trained networks are the record's only measured cases of group structure in a representation. They show what the group's source is, and whether reconstruction worked or the group was supplied. [CLAIM-135](../claims.d/CLAIM-135.md) and [CLAIM-148](../claims.d/CLAIM-148.md) frame recovery as identification up to stated ambiguities.

## What the record holds

- [THEORY-022](../theory.d/THEORY-022.md): the network multiplies characters, but "the group comes from the task, not the network". A spectral test sees the irreducibles "only as pairs". Limit: one weight-decay model; dropout models are not Fourier-sparse.
- [THEORY-181](../theory.d/THEORY-181.md): the training set's same-answer pairs fix the representation once they "leave only translation and scale free", with a critical training fraction. Limit: the sum is built into the architecture.
- [THEORY-021](../theory.d/THEORY-021.md): the dimensionality-weighted projectors of the packed geometries sum to the identity. But the POVM "needs an inner product", and the feature basis is stipulated. Limit: toy geometry only.
- [THEORY-184](../theory.d/THEORY-184.md): under a permutation-equivariant update "coincident neurons stay coincident", and below step size 1/K distinct ones cannot merge. The update preserves the symmetry it starts with. Limit: it says nothing about the function computed.

## What would answer it

A non-abelian task learned without a matrix representation imposed, analysed without the group being supplied in advance. Its irreducibles would be either recovered from the weights or shown to be unrecoverable.
