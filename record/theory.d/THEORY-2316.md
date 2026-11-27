---
number: 2316
status: Proposed
formerly:
- THEORY-tmpjgsul
promote_when: >-
  An independent replication, on other models or with the released benchmark, finds the same per-factor accuracy drops with target and answer held fixed, and a prompt-time activation classifier that separates high- from low-load variants of held-out problems at comparable AUC by factor and shifts little, relative to that separation, under changes of intrinsic difficulty that lower accuracy; the classifier part fails if the separation vanishes once prompts are matched in length. The cognitive-load reading is the authors' and is not what this asks to confirm.
title: 'Presentation alone costs language models accuracy, and activations tell which presentation it was'
statement: >-
  Gupta, Liu and Zou find that in five open instruction-tuned models of 4-14B parameters, on synthetic contextual, arithmetic and analogy problems whose target and answer are held fixed, changing only presentation (more or more similar distractors, a secondary task, shuffled statements, or an implicit reference) usually lowers accuracy, by up to about 37 points averaged over models, and that a per-model classifier on 30 prompt-time activation statistics tells high- from low-load variants of unseen problems apart (ROC AUC 0.71-1.00 by factor) while moving little under two manipulations of intrinsic difficulty; they read this as extraneous cognitive load arising from competing content or from a harder reasoning path
version: 1
tags:
- cognition
- representation-learning
date: '2026-11-27'
source:
- LIT-3312
corroborates:
- CLAIM-1269
- CLAIM-1086
- CLAIM-1100
- CLAIM-1403
summary: >-
  Gupta, Liu and Zou (2026), [LIT-3312](../literature.d/LIT-3312.md), read in [NOTE-2425](../notes.d/NOTE-2425.md). Proposed: one benchmark, synthetic tasks, open models up to 14B, and a classifier that does not generalize across load factors.
---

# THEORY-2316: Presentation alone costs language models accuracy, and activations tell which presentation it was

Gupta, Liu and Zou (2026), [LIT-3312](../literature.d/LIT-3312.md), read in [NOTE-2425](../notes.d/NOTE-2425.md).

## The account

With what makes the answer true held fixed, the way a problem is laid out still changes whether a model solves it. The largest costs come from order and implicit reference, the smallest from an interfering task. The model's activations register the layout, but differently for each kind.

## Evidence

Controlled synthetic benchmarks, five open models, one real-document test with four models including two frontier ones. No human comparison, and intrinsic and extraneous load are not crossed.
