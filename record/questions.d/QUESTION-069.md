---
number: 69
status: Open
formerly:
- QUESTION-tmpzj6fs
title: 'Is the connectedness of trained solutions a property of the solutions, or of the path family searched, the shared history that produced them and the regime they were trained in?'
version: 1
tags:
- loss-landscapes
- anthology-candidate
- learning-theory
date: '2026-10-12'
line: 'learned-structure'
answered_by:
- THEORY-105
- THEORY-107
- THEORY-108
- THEORY-109
- THEORY-110
- THEORY-114
- THEORY-209
- THEORY-210
- THEORY-211
- THEORY-tmpe5k4b
- THEORY-tmpjgtxb
- THEORY-tmpltw3b
- THEORY-tmpxxllh
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-187](../claims.d/CLAIM-187.md) and [CLAIM-142](../claims.d/CLAIM-142.md).
  [THEORY-105](../theory.d/THEORY-105.md), [THEORY-107](../theory.d/THEORY-107.md), [THEORY-108](../theory.d/THEORY-108.md), [THEORY-109](../theory.d/THEORY-109.md), [THEORY-110](../theory.d/THEORY-110.md) and
  [THEORY-114](../theory.d/THEORY-114.md) answer it in part; the body gives each one's limit.
---
<!-- inactive-ok-file: THEORY-209 — Proposed; a reading that bears on the regime alternative, open -->

# QUESTION-069: Is the connectedness of trained solutions a property of the solutions, or of the path family searched, the shared history that produced them and the regime they were trained in?

## The question

Several results say that the solutions training reaches are joined at low loss. Each was measured with a particular instrument (a curve family, a straight line, a centre, an alignment), on runs with a particular history (shared start, shared stem, none), and in a particular regime. The question is which of these the connectedness belongs to. Equivalently: what does a residual barrier between two trained networks tell us about the networks themselves?

## Why the record needs it

[CLAIM-187](../claims.d/CLAIM-187.md) reads a barrier that survives alignment as a different mechanism. It would carry that protocol to communicative kinds. Its defeater asks whether systems that share a mechanism can stay separated after alignment. If the barrier depends on the instrument or the history, then the protocol measures those and not the mechanism. [CLAIM-142](../claims.d/CLAIM-142.md) makes the same point about probes.

## What the record holds

- [THEORY-109](../theory.d/THEORY-109.md): curves join solutions where the straight segment fails, and this is "a property of the solutions training finds, not of every minimum". Limit: "one set" is extrapolated from pairs.
- [THEORY-114](../theory.d/THEORY-114.md): linear connectivity "emerges during training, not at initialization". It comes early for copies that share a stem and gradually for aligned strangers.
- [THEORY-110](../theory.d/THEORY-110.md): a centre is linearly connected to held-out solutions when pairs are not, so the relation is "a star domain even where it is not convex". Limit: the barriers to the centre are not zero.
- [THEORY-105](../theory.d/THEORY-105.md): from one start, the low-loss region "contains the convex hull" of same-task models, and it is graded by dataset and task family.
- [THEORY-107](../theory.d/THEORY-107.md): sign conflicts are as frequent within one task as across tasks, yet cost far less within one. So disagreement in coordinates is not the residue.
- [THEORY-108](../theory.d/THEORY-108.md): in phase III, flat solutions are "poorly connected" on one curve family without alignment. It is open whether this is a real barrier.
- [THEORY-209](../theory.d/THEORY-209.md) (Kunin et al., filed 2026-10-13): a converged run trained with SGD is a nonequilibrium stationary distribution, not a point, whose spread and correlations are set by learning rate, momentum and batch size. It bears on the "regime" alternative. It measures no connectivity, and is silent on flat directions.

## What would answer it

Phase III runs aligned by permutation, with the barrier measured on several path families. Alongside that, a pair of networks known to share a mechanism, tested for whether alignment always removes their barrier.
