---
number: 159
status: 'Open'
formerly:
- QUESTION-tmpw593l
title: "Does an exact train-then-predict identity, of the kind proved for unnormalized linear attention and for softmax attention, hold for further sequence-layer classes such as delta-rule or mini-batch inner updates, and is there a standard attention layer whose dependence on its context admits no description as any learner's train-then-predict step?"
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The scope test formerly in [THEORY-169](../theory.d/THEORY-169.md)'s promote_when, moved here
  unchanged when [THEORY-169](../theory.d/THEORY-169.md) was narrowed and promoted on 2026-10-19. The
  identities are proved for unnormalized causal linear attention (one batch
  gradient step of a linear model from zero) and for softmax attention
  (kernel regression that stores the context). Whether the pattern reaches
  other layer classes, or is bounded by one, is open.
---

# QUESTION-159: Does an exact train-then-predict identity, of the kind proved for unnormalized linear attention and for softmax attention, hold for further sequence-layer classes such as delta-rule or mini-batch inner updates, and is there a standard attention layer whose dependence on its context admits no description as any learner's train-then-predict step?

## Why it is a question

[THEORY-169](../theory.d/THEORY-169.md), narrowed on 2026-10-19, holds that for unnormalized causal
linear attention and for softmax attention the layer's output equals a
learner's train-then-predict step on its context, and that one linear
self-attention layer with constructed weights carries one gradient step of
in-context linear regression. Until that date its promote_when also asked
for a test of scope. At the owner's direction, from the promotion audit's
batch 024 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was narrowed and promoted on the proved
identities, which were re-derived, and that part of the condition moved
here unchanged.

It is open because the identities are for particular layers. Normalized
linear attention, TTT-Linear as built (mini-batch updates, a learned W₀,
LayerNorm) and delta-rule layers are not covered, and nothing the record
holds shows that some standard layer has no such description.

## What would answer it

The scope test formerly on [THEORY-169](../theory.d/THEORY-169.md), unchanged. An exact identity of
this kind for a further layer class, for instance a delta-rule or
mini-batch inner update, would confirm the pattern. A proof that some
standard attention layer's dependence on its context admits no description
as any learner's train-then-predict step would bound it. Restating the two
known constructions, or measuring trained models' similarity to gradient
descent, does not count.
