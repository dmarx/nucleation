---
number: 2093
status: Proposed
formerly:
- THEORY-tmpw5877
title: 'Random-label pretraining can speed learning'
statement: >-
  Maennel and colleagues find that convolutional networks pretrained on
  images with random labels, rescaled and given a fresh head, usually learn
  a new labelling of fresh images faster than from scratch, a gain
  reproduced by first-layer filters sampled from the learned weight
  covariance, which aligns with the data covariance, while in other settings
  the same pretraining slows later learning as later-layer units go inactive
version: 1
source:
- LIT-2878
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with several seeds finds in one image dataset
  that random-label pretraining with per-layer norm rescaling and a fresh
  head raises downstream training speed over training from scratch at
  matched hyperparameters, that first-layer filters sampled from the
  pretrained weight covariance reproduce that gain, and that at least one
  stated setting reverses the effect together with a measured drop in
  later-layer activation at the switch.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-2878](../literature.d/LIT-2878.md) in [NOTE-2173](../notes.d/NOTE-2173.md). The memorization
  arm's baseline: input statistics alone carry a later saving, which can
  reverse. Proposed until its promote_when is met.
---

# THEORY-2093: Random-label pretraining can speed learning

## The account

VGG16, ResNet18 and small CNNs on CIFAR10 and ImageNet: after random-label pretraining with norm rescaling, downstream training is usually faster; covariance-sampled first-layer filters reproduce the gain; a data-built initialization gives much of it early in training; some settings of scale, upstream classes and width slow downstream training, with later-layer activations collapsing at the switch.

## Evidence

12 runs in the key figures, fewer elsewhere; cost as area under curves; first-stage accuracy unreported.
