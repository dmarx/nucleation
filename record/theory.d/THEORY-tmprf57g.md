---
status: Proposed
title: 'Along a low-loss linear path between two networks, every layer''s features are the interpolation of the endpoints'' features'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-30'
source:
- LIT-674
- LIT-669
extends:
- THEORY-111
promote_when: >-
  For the layerwise claim, the same measurement outside image
  classification: transformers and language models, linearly connected by
  spawning, by fine-tuning from a shared pretrained model or by alignment.
  It is refuted by a pair that is linearly connected at the output while
  some intermediate layer's interpolated features point away from the
  interpolated features. An approximate version of Zhou et al.'s Theorem 1,
  bounding the feature error by the size of the weak-additivity and
  commutativity residuals, would also move it. More pairwise
  image-classifier measurements would not.
bears_on:
- QUESTION-318
summary: >-
  The wide form THEORY-111 held before the eleventh status review narrowed
  it, kept as a Proposed reading by the ADR-047 kind-1 sweep of
  2026-10-30: the source asserts it, and THEORY-111, Active, is its
  evidence. The old title's averaging clause was the record's own step and
  is a Proposed claim of its own; the promote_when here is the layerwise
  half of the old one.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-tmprf57g: Along a low-loss linear path between two networks, every layer's features are the interpolation of the endpoints' features

## Source

Zhou, Yang, Yang, Yan & Hu (2023), LIT-674, read in NOTE-512; and Lubana,
Bigelow, Dick, Krueger & Tanaka (2022), LIT-669, read in NOTE-538, for
Lemma 2. What the pairs of image classifiers measured showed is THEORY-111,
which this entry extends.

## The claim

Zhou et al. name layerwise linear feature connectivity: the feature maps of
every layer of two trained networks are linearly connected, so the
features of the network on the straight line between them are the
interpolation of the endpoints' features. They state it as a general
regularity, that whenever two networks are linearly mode connected, by
spawning or by permutation, they satisfy it in nearly all layers
(NOTE-512, C1). Their definition allows a scale factor, and their Theorem 1
gives it exactly, with scale 1, under two conditions, weak additivity of
ReLU and a commutativity of weights with features. Lubana et al.'s Lemma 2
derives the first of those for a one-hidden-layer network, where the claim
is then a theorem.

The measurements are pairs of image classifiers at three points on the
line, and the scale fitted in practice is not 1. The claim is that the
same holds for any two networks joined by a low-loss line.

## What would settle it

The promote_when, which is the layerwise half of QUESTION-318: the same
measurement in transformers and language models connected by spawning,
shared pretraining or alignment, or an approximate version of Theorem 1.
More pairwise image-classifier measurements cannot settle it.
