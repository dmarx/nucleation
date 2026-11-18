---
status: Proposed
promote_when: >-
  The same approximate equality, per layer and in length as well as
  direction, measured by a second group on models fine-tuned from one
  pretrained checkpoint that the paper did not use, both for pairs
  fine-tuned on different tasks and for averages of several fine-tunes of
  one task. It is refuted by such a pair or average whose interpolated or
  averaged network's features at some layer differ in direction or length
  from the interpolated or averaged features by as much as the endpoints'
  features differ from each other.
title: 'Zhou, Chen, Chen, Zhang and Yan: networks fine-tuned on different tasks from one pretrained checkpoint, though not linearly connected in loss, have at the layers measured (MLPs and ResNet-18 on continual-learning splits, CLIP ViT-B/32 and ViT-L/14, T5-base) features at a weight interpolation approximately equal to the interpolation of their features, and averages of 5 or 10 ViT-B/32 fine-tunes have approximately the average of their members'' features'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmptiitv
extends:
- THEORY-111
bears_on:
- QUESTION-318
- QUESTION-069
corroborates:
- CLAIM-498
summary: >-
  Zhou, Chen, Chen, Zhang & Yan (2024), [LIT-tmptiitv](../literature.d/LIT-tmptiitv.md), read in
  [NOTE-tmpjupyx](../notes.d/NOTE-tmpjupyx.md). Cross-task linearity: cosine near 1 and projection-length
  ratio near 1 between the interpolated model's features and the
  interpolated features, against an endpoint baseline, in the blocks
  reported; the same for soups of 5 CIFAR-10 and 10 ImageNet ViT-B/32
  fine-tunes, all blocks for the latter. Extends [THEORY-111](THEORY-111.md) from
  proportionality to approximate equality and from pairs connected in loss
  to pairs that are not. Bears on both halves of [QUESTION-318](../questions.d/QUESTION-318.md) and supports
  [CLAIM-498](../claims.d/CLAIM-498.md)'s averaging step for soups, not SWA. The wording is the
  reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-498 THEORY-tmpkfmi5 THEORY-115 — new tmp codes, or Proposed; source, reading, the claim this corroborates and neighbouring accounts, named and not leaned on -->

# THEORY-tmpjlixb: Zhou, Chen, Chen, Zhang and Yan: networks fine-tuned on different tasks from one pretrained checkpoint, though not linearly connected in loss, have at the layers measured (MLPs and ResNet-18 on continual-learning splits, CLIP ViT-B/32 and ViT-L/14, T5-base) features at a weight interpolation approximately equal to the interpolation of their features, and averages of 5 or 10 ViT-B/32 fine-tunes have approximately the average of their members' features

## Source

Zhou, Chen, Chen, Zhang & Yan (2024), [LIT-tmptiitv](../literature.d/LIT-tmptiitv.md), read in
[NOTE-tmpjupyx](../notes.d/NOTE-tmpjupyx.md): §§1–6, Appendices A and C.

## The result

- **Pairs across tasks** (§4.1, §4.3): at α ∈ {0.25, 0.5, 0.75}, the
  features of f^(ℓ)(αθ_i + (1−α)θ_j) point in nearly the same direction
  as αf^(ℓ)(θ_i) + (1−α)f^(ℓ)(θ_j), well below the dissimilarity of the
  endpoints' own features, and the projection-length ratio sits near 1.
  So the relation is approximate equality, stronger than the
  proportionality of [THEORY-111](THEORY-111.md). It holds though the pairs, fine-tuned on
  different tasks, are not linearly connected in loss.
- **Averages** (§4.2, App. C.4): for 5 CIFAR-10 and 10 ImageNet ViT-B/32
  fine-tunes, the averaged network's features approximate the average of
  the members' features, for all blocks in the ImageNet case.
- **Checks from outside the measurement**: stitching averaged block-9
  features into the pretrained head works on both tasks (§4.3); 3-model
  weight averages track logit ensembles in accuracy over 1,140 triples
  (Fig. 4).
- **What drives it** (§5): more pretraining strengthens it; the similarity
  of the two fine-tuning tasks barely matters.

This could have come out otherwise. A network is not linear in its
weights, and pairs that fail linear connectivity in loss give no reason to
expect linear features.

## What it does not show

- **SWA, or decoder-only language models.** Neither is measured; the
  authors leave large language models to future work.
- **Every layer everywhere.** Most plots are of the last three or seven
  blocks. All blocks are reported for the ImageNet soup and for ViT-B/32
  arithmetic.
- **Why.** Theorem 5.1 bounds a scalar's deviation from linearity by
  sharpness times squared distance. It is not a bound on feature error,
  and it is checked with the loss on same-task pairs. The step to many
  models (Theorem 4.2) rests on an unproved transitivity conjecture.
- **A first-order Taylor model.** The authors distinguish it from the
  linearisation that Ortiz-Jimenez et al. ([THEORY-tmpkfmi5](THEORY-tmpkfmi5.md)) reject:
  approximate linearity along task-vector directions, not a linear model.
- **A barrier test.** That loss connectivity fails across tasks is taken
  from the setting, not measured against task overlap, so it does not test
  [THEORY-115](THEORY-115.md).
