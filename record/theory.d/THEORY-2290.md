---
number: 2290
status: Proposed
formerly:
- THEORY-tmpfysqg
title: 'Lippl and Lindsey find that rescaling a pretrained ResNet''s weights by a factor below one before fine-tuning improves fine-tuning on small image classification tasks and gives the representation the signature of nested feature selection, lower dimension after fine-tuning with nearly all of it shared with the pretrained representation, while Vision Transformers show that signature unrescaled and are harmed by rescaling either way'
version: 1
source:
- LIT-3172
tags:
- representation-learning
- learning-theory
date: '2026-11-23'
promote_when: >-
  An independent replication with error bars shows that rescaling a
  pretrained ResNet's weights by a factor below one before fine-tuning
  raises fine-tuning accuracy on held-out classification tasks, and that
  the gain goes with a fall in participation ratio over fine-tuning and
  an effective number of shared dimensions close to the fine-tuned
  participation ratio.
summary: >-
  From the reading of [LIT-3172](../literature.d/LIT-3172.md) in [NOTE-2415](../notes.d/NOTE-2415.md), carrying out the lead
  that asked for it: the deep-network half of the paper, kept apart from
  the shallow theory ([THEORY-2305](THEORY-2305.md)) because it rests on experiment
  alone. That the best rescaling differs between architectures is a
  parallel to [CLAIM-754](../claims.d/CLAIM-754.md)'s point that no ranking holds without a declared
  context. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2305 CLAIM-754 — Proposed; the companion reading filed by the lead run of 2026-11-23, and the claim it parallels -->

# THEORY-2290: Lippl and Lindsey find that rescaling a pretrained ResNet's weights by a factor below one before fine-tuning improves fine-tuning on small image classification tasks and gives the representation the signature of nested feature selection, lower dimension after fine-tuning with nearly all of it shared with the pretrained representation, while Vision Transformers show that signature unrescaled and are harmed by rescaling either way

## The account

ResNet-18 pretrained on 98 CIFAR-100 classes and fine-tuned on the other
two generalizes better when its weights are shrunk before fine-tuning,
and only then does its representation lose dimensions over fine-tuning
while keeping nearly all the dimensions it retains from pretraining, the
signature nested feature selection has in shallow networks. Networks
pretrained on ImageNet gain from a factor of 0.5 on CIFAR-100 and STL-10
tasks. A Vision Transformer already shows the signature without
rescaling and loses accuracy when rescaled up or down: which rescaling is
best depends on the architecture.

## Evidence

Experiments only; the ImageNet factor was not swept; the prose gives no
error bars, and it does not say which weights were rescaled or whether
the pretrained function was kept.
