---
status: Open
title: 'Do networks trained on factored sequence processes other than Mess3 and Bloch Walk factors, or under an objective other than next-token prediction, also settle near the factored dimension in per-factor subspaces, and what loss gap does the factored representation pay when noise makes it lossy?'
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-060
summary: >-
  The promotion condition formerly on [THEORY-256](../theory.d/THEORY-256.md), moved here unchanged when
  [THEORY-256](../theory.d/THEORY-256.md) was narrowed to the transformers and processes tested and
  promoted on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3). The embedding theorem is settled.
  Whether the training behaviour holds beyond one synthetic family and one
  objective, and what the lossy case costs, has not been measured.
---

# QUESTION-tmpmknot: Do networks trained on factored sequence processes other than Mess3 and Bloch Walk factors, or under an objective other than next-token prediction, also settle near the factored dimension in per-factor subspaces, and what loss gap does the factored representation pay when noise makes it lossy?

## Why it is a question

[THEORY-256](../theory.d/THEORY-256.md), narrowed on 2026-10-19, holds two things. When a generator's
operators factor as a tensor product, its predictive state embeds
losslessly and linearly in per-factor subspaces of total dimension
Σ(d_n − 1). And 4-layer GPT-2-style transformers trained by next-token
prediction on five Mess3 and Bloch Walk factors settle near that
dimension, and reach it first under the token-noise construction tested.
Until that date, [THEORY-256](../theory.d/THEORY-256.md)'s promote_when asked for a replication. At the
owner's direction, from the promotion audit's batch 019 ([ADR-047](../decisions.d/ADR-047.md) v3: one
study read in full can carry a title that claims no more than it
measured), the THEORY was narrowed and promoted, and the condition moved
here unchanged.

It is open because [LIT-986](../literature.d/LIT-986.md) varies the data within one synthetic family
and keeps the objective fixed, and it argues the loss gap in the noisy case
from the construction rather than reporting it ([NOTE-758](../notes.d/NOTE-758.md)). It refines
[QUESTION-060](QUESTION-060.md)'s question of whether the objective or the architecture fixes
what a trained network represents.

## What would answer it

The condition formerly on [THEORY-256](../theory.d/THEORY-256.md), unchanged. A replication on a
different family of factored generators, or under a second objective on
the same data, that measures the dimension and per-factor orthogonality of
the learned representation. In the noise experiment it would also report
the loss gap between the factored and joint representations at each noise
level. The account is refuted by a transformer trained on a lossless
factored process, with room for the joint representation, that settles
near the joint dimension. It is also refuted by a lossy process on which
training reaches the joint representation without first passing near the
factored one. Linear decodability of each factor's belief alone cannot
settle it, since a representation with overlapping factor subspaces also
supports accurate linear readout ([LIT-986](../literature.d/LIT-986.md), App. H.1.2).
