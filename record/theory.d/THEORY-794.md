---
number: 794
status: Proposed
formerly:
- THEORY-tmpu18sx
promote_when: >-
  For the empirical half: the volume-against-diversity comparison repeated
  with model selection on a validation split disjoint from the unseen
  combinations, so that a model never chosen by its score on the test pairs
  still fails to generalize under more data of the same combinations and
  succeeds as coverage rises. A second architecture trained from scratch, or
  more than two concepts, would widen it. For the theoretical half: a
  line-by-line check of Proposition B.7's proof, or a second derivation such
  as Trager et al.'s. The account is refuted if, at fixed combinatorial
  coverage, enough added data of the seen combinations closes the gap on
  unseen ones, or if networks reach high accuracy on unseen pairs at low
  coverage without linearly factored features. Further runs with oracle
  selection on the test pairs cannot settle it, since they measure the best
  case by construction.
title: In vision models, compositional generalization to unseen combinations of concepts is driven by the diversity of the combinations seen in training rather than by data volume, and arrives with representations that are linearly factored by concept, as Uselis, Dittadi and Oh propose
version: 1
tags:
- representation-learning
- compositionality
- learning-theory
- anthology-candidate
date: '2026-10-20'
source:
- LIT-667
extends:
- THEORY-117
answers:
- QUESTION-207
summary: >-
  Uselis, Dittadi & Oh (2025), [LIT-667](../literature.d/LIT-667.md), read in [NOTE-525](../notes.d/NOTE-525.md). Their title and
  abstract present diversity of combinations, not data volume, as what
  drives compositional generalization in vision models. Their evidence is
  ResNet-50s trained from scratch on two-concept grids, with checkpoints
  chosen on the unseen pairs, and that measured part, with the factorization
  theorem, is the Active [THEORY-117](THEORY-117.md). This THEORY holds the general causal
  claim.
---

# THEORY-794: In vision models, compositional generalization to unseen combinations of concepts is driven by the diversity of the combinations seen in training rather than by data volume, and arrives with representations that are linearly factored by concept, as Uselis, Dittadi and Oh propose

## Source

[LIT-667](../literature.d/LIT-667.md). Filed by the promotion audit's narrowing-loss sweep
(batch 066, [ADR-047](../decisions.d/ADR-047.md) v4) on 2026-10-20, to carry the wider claim that the
narrowing of [THEORY-117](THEORY-117.md) dropped. [THEORY-117](THEORY-117.md) is Active and is this
THEORY's evidence; this one stays Proposed.

## What was actually shown

In an n × n grid of two concepts with k combinations seen per value,
ResNet-50s trained from scratch fit the seen pairs and fail on unseen
ones; four times the data of the same combinations leaves 60–80% drops,
while seeing a larger share of the combinations closes the gap, and the
features pass from spurious to decodable to linearly factored as coverage
grows. Pretrained DINO, DINOv2 and CLIP features are partly factored.
[THEORY-117](THEORY-117.md) states the measured result, with its oracle checkpoint
selection, and the re-derived theorem that exactly factored embeddings
of every unseen pair are fixed by seen pairs connecting every value. The
authors draw the general conclusion, about vision models and about
what drives compositional generalization, from this one design.

## What would settle it

The promote_when is inherited from [THEORY-117](THEORY-117.md)'s before it was
narrowed, and [QUESTION-207](../questions.d/QUESTION-207.md) asks the same question.

## What this does not say

It is not a claim about how much data a practitioner needs, and it
says nothing about generative models. The measurements chose
checkpoints on the test pairs, so they bound what is possible rather
than what honest selection reaches; this THEORY's general form needs
that gap closed.
