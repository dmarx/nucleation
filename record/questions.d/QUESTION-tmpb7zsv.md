---
status: Open
title: 'If a kind''s admissible transformations are given as a distribution over pairs of its realizations, is its stable, decision-sufficient signature the top eigenspace of the pair operator, and what takes that role when the transformations are directed?'
version: 1
tags:
- representation-learning
- information-theory
- mathematics
date: '2026-10-12'
line: 'pragmatic-transport'
refines:
- QUESTION-027
answered_by:
- THEORY-001
- THEORY-003
- THEORY-005
- THEORY-006
- THEORY-007
- THEORY-009
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [QUESTION-027](QUESTION-027.md), [CLAIM-098](../claims.d/CLAIM-098.md), CLAIM-
  tmppqir6, [CLAIM-164](../claims.d/CLAIM-164.md) and [CLAIM-043](../claims.d/CLAIM-043.md). [THEORY-001](../theory.d/THEORY-001.md), [THEORY-003](../theory.d/THEORY-003.md), [THEORY-005](../theory.d/THEORY-005.md),
  [THEORY-006](../theory.d/THEORY-006.md), [THEORY-007](../theory.d/THEORY-007.md) and [THEORY-009](../theory.d/THEORY-009.md) answer it in part; the body gives
  each one's limit.
---

# QUESTION-tmpb7zsv: If a kind's admissible transformations are given as a distribution over pairs of its realizations, is its stable, decision-sufficient signature the top eigenspace of the pair operator, and what takes that role when the transformations are directed?

## The question

Treat "these two realizations are of the same kind" as a joint distribution over pairs. That distribution defines a conditional-expectation operator on functions of realizations. The question is whether its top eigenspace is the signature [QUESTION-027](QUESTION-027.md) asks for: stable under the transformations, sufficient for a stated family of decisions, and discriminating between kinds. It also asks what replaces the eigenspace when the pairing is not symmetric.

## Why the record needs it

[QUESTION-027](QUESTION-027.md) asks for a signature with three properties and names no construction. This is one candidate. The mechanism transfers because the operator is defined for any symmetric pair distribution on any space. Nothing in it is specific to networks. [CLAIM-098](../claims.d/CLAIM-098.md) holds that translation is directed and need not be invertible, and directedness is exactly where the construction breaks. [CLAIM-164](../claims.d/CLAIM-164.md) says the definite object is the eigenspace, not a single vector. [CLAIM-tmppqir6](../claims.d/CLAIM-tmppqir6.md) says linear probes see only the kernel, and here the kernel is the density ratio.

## What the record holds

- [THEORY-007](../theory.d/THEORY-007.md): the top eigenfunctions are "the most view-invariant directions", and their span is minimax-optimal for linear prediction of approximately invariant targets. Limit: finite spaces, population level, linear decisions only.
- [THEORY-005](../theory.d/THEORY-005.md): the operator is compact when "the positive-pair χ²-divergence is finite". Limit: the condition fails when realizations determine each other almost exactly.
- [THEORY-009](../theory.d/THEORY-009.md): self-adjointness comes "from the symmetry of the positive-pair distribution". For directed pairs "no such account was found".
- [THEORY-001](../theory.d/THEORY-001.md): three losses "share one population optimum", so the candidate signature does not depend on the objective used. Limit: low-rank truncations differ.
- [THEORY-003](../theory.d/THEORY-003.md): HSIC maximizes the "average squared MMD" between kinds, which gives discrimination. Limit: it is injective only for a characteristic kernel.
- [THEORY-006](../theory.d/THEORY-006.md): the information bound "can never exceed the log of the batch size" and does not track quality, so the signature is not an amount of information (compare [CLAIM-043](../claims.d/CLAIM-043.md)).

## What would answer it

A singular-function result for a non-symmetric pair operator, with its own sufficiency guarantee. Or a showing that directed transports admit no such signature.
