---
status: Proposed
promote_when: >-
  An independent derivation or replication of the O(1/α) parameter
  displacement and the O(1/α) gap between lazy and linearized outputs
  under the stated assumptions, and an independent experiment finding a
  drop in test accuracy as α grows from 1 for a standard CNN with centred
  output.
title: 'Chizat, Oyallon and Bach show that lazy training, in which a non-linear model trained by gradient methods stays close to its linearization at initialization, is produced by a choice of scale: multiplying the output by α makes the relative change of the model''s differential per step small against that of the loss, so that as α grows the parameters move by order 1/α and the model and its linearization differ by order 1/α, and their experiments find networks in this regime generalize worse'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmp67epj
summary: >-
  The scale account of lazy training, read for [CLAIM-tmpqwoxz](../claims.d/CLAIM-tmpqwoxz.md): a
  separation of rates between a fast output and a slow parameter vector,
  readout included. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-212 THEORY-813 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpqwoxz THEORY-tmp7n7a9 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmpecd1x: Chizat, Oyallon and Bach show that lazy training, in which a non-linear model trained by gradient methods stays close to its linearization at initialization, is produced by a choice of scale: multiplying the output by α makes the relative change of the model's differential per step small against that of the loss, so that as α grows the parameters move by order 1/α and the model and its linearization differ by order 1/α, and their experiments find networks in this regime generalize worse

## Source

Chizat, Oyallon and Bach, [LIT-tmp67epj](../literature.d/LIT-tmp67epj.md), read in [NOTE-tmpo2iav](../notes.d/NOTE-tmpo2iav.md) from arXiv 1812.07956v5 (7 Jan 2020, the NeurIPS 2019 camera-ready with supplement).

## What was actually shown

§1.2, §2.1, Theorems 2.2–2.5, Appendix A and §3.2 as quoted in the NOTE.

## What this does not say

Nothing per layer; nothing about μP; it does not show hidden modules slower than the readout.

## Connections

[THEORY-tmp7n7a9](THEORY-tmp7n7a9.md) (Yang and Hu: the per-layer, width-indexed form); [THEORY-212](THEORY-212.md) (per-layer finite-size form); [LIT-1232](../literature.d/LIT-1232.md) (mean-field); [THEORY-813](THEORY-813.md).
