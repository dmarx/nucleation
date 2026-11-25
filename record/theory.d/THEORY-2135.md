---
number: 2135
status: Proposed
formerly:
- THEORY-tmpecd1x
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
- LIT-2941
summary: >-
  The scale account of lazy training, read for [CLAIM-775](../claims.d/CLAIM-775.md): a
  separation of rates between a fast output and a slow parameter vector,
  readout included. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2170 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: THEORY-212 THEORY-813 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-775 THEORY-2133 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2135: Chizat, Oyallon and Bach show that lazy training, in which a non-linear model trained by gradient methods stays close to its linearization at initialization, is produced by a choice of scale: multiplying the output by α makes the relative change of the model's differential per step small against that of the loss, so that as α grows the parameters move by order 1/α and the model and its linearization differ by order 1/α, and their experiments find networks in this regime generalize worse

## Source

Chizat, Oyallon and Bach, [LIT-2941](../literature.d/LIT-2941.md), read in [NOTE-2227](../notes.d/NOTE-2227.md) from arXiv 1812.07956v5 (7 Jan 2020, the NeurIPS 2019 camera-ready with supplement).

## What was actually shown

§1.2, §2.1, Theorems 2.2–2.5, Appendix A and §3.2 as quoted in the NOTE.

## What this does not say

Nothing per layer; nothing about μP; it does not show hidden modules slower than the readout.

## Connections

[THEORY-2133](THEORY-2133.md) (Yang and Hu: the per-layer, width-indexed form); [THEORY-212](THEORY-212.md) (per-layer finite-size form); [LIT-1232](../literature.d/LIT-1232.md) (mean-field); [THEORY-813](THEORY-813.md).

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-2258](../notes.d/NOTE-2258.md), [THEORY-2170](THEORY-2170.md)): **a
contrast.** Their point is leaving the lazy, random-features regime: "It is
precisely the presence of such correlated components that enables the
trained model to surpass the Random Features performance". No relation.
