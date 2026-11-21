---
number: 2144
status: Proposed
formerly:
- THEORY-tmpthk75
promote_when: >-
  Layer-drop and adjacent-swap interventions in at least one further
  decoder family showing the same profile, and the stage signatures
  replicated by an independent group.
title: 'Lad, Lee, Gurnee and Tegmark find that in GPT-2 and Pythia models deleting or swapping a single middle layer at inference leaves most top-1 predictions unchanged while first-layer interventions are catastrophic, and, from this and from probes, logit-lens and neuron statistics across 16 models in five families, hypothesize four ordered stages of inference: detokenization, feature engineering, prediction ensembling and residual sharpening'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2937
summary: >-
  Ordered stages around a behaviourally robust middle, the second half
  specialized ([CLAIM-771](../claims.d/CLAIM-771.md)). Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-1030 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-771 THEORY-2140 THEORY-2145 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2144: Lad, Lee, Gurnee and Tegmark find that in GPT-2 and Pythia models deleting or swapping a single middle layer at inference leaves most top-1 predictions unchanged while first-layer interventions are catastrophic, and, from this and from probes, logit-lens and neuron statistics across 16 models in five families, hypothesize four ordered stages of inference: detokenization, feature engineering, prediction ensembling and residual sharpening

## Source

Lad, Lee, Gurnee and Tegmark, [LIT-2937](../literature.d/LIT-2937.md), read in [NOTE-2220](../notes.d/NOTE-2220.md) from arXiv 2406.19384v3 (16 Jun 2025).

## What was actually shown

§3.1, §4, A.4 and §6 as quoted in the NOTE.

## What this does not say

Not that stages are levels of knowledge; not robustness beyond GPT-2 and Pythia; the stages are a hypothesis.

## Connections

[THEORY-2145](THEORY-2145.md) (Layers as Painters); [THEORY-1033](THEORY-1033.md), [THEORY-1030](THEORY-1030.md); [THEORY-2140](THEORY-2140.md).
