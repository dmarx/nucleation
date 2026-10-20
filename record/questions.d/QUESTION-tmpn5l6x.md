---
status: Open
title: 'Without choosing checkpoints on the unseen pairs, does coverage of combinations still beat volume for compositional generalization, in a second architecture or with more than two concepts?'
version: 1
tags:
- compositionality
- representation-learning
date: '2026-10-20'
line: 'learned-structure'
summary: >-
  The promotion condition formerly on [THEORY-117](../theory.d/THEORY-117.md). [THEORY-117](../theory.d/THEORY-117.md) was narrowed to
  what Uselis, Dittadi and Oh measured and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md)
  v3), with a determination result the record re-derived: from-scratch
  ResNet-50s on two-concept grids, with checkpoints chosen on the unseen
  pairs, reach unseen combinations as coverage grows and not under up to
  four times more data of the same combinations. Whether that survives
  honest model selection, another architecture or more concepts is open.
---

# QUESTION-tmpn5l6x: Without choosing checkpoints on the unseen pairs, does coverage of combinations still beat volume for compositional generalization, in a second architecture or with more than two concepts?

## Why it is a question

Every from-scratch number behind [THEORY-117](../theory.d/THEORY-117.md) is the best checkpoint as
scored on the unseen combinations, by the authors' design. That makes the
failures under more volume strong evidence and the successes an upper
bound. The volume test is one architecture, n = 3, k = 1, up to four
times the data (sixteen on two datasets). The classifier half of the
paper's Proposition 4.1, and how either half degrades when factorization
is only approximate, are also open. Until 2026-10-20 this was
[THEORY-117](../theory.d/THEORY-117.md)'s promote_when.

## What would answer it

The volume-against-diversity comparison repeated with model selection on a
validation split disjoint from the unseen combinations, so that a model
never chosen by its score on the test pairs still fails under more data of
the same combinations and succeeds as coverage rises; a second
architecture trained from scratch, or more than two concepts, would widen
it. The account is refuted if, at fixed coverage, enough added data of the
seen combinations closes the gap on unseen ones, or if networks reach high
accuracy on unseen pairs at low coverage without linearly factored
features. Further runs with oracle selection cannot settle it.
