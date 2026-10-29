---
status: Open
title: 'Does layerwise linear feature connectivity hold outside image classification, in transformers and language models connected by spawning, shared pretraining or alignment, and does it carry from pairs to the many-model averages practice uses, model soups and SWA?'
version: 1
tags:
- loss-landscapes
- representation-learning
date: '2026-10-29'
line: learned-structure
summary: >-
  The promotion condition formerly on THEORY-111, moved here when the
  eleventh status review narrowed it to the pairs of image classifiers its
  source measured and promoted it, as THEORY-114's moved to QUESTION-312.
---

# QUESTION-tmpxygjx: Does layerwise linear feature connectivity hold outside image classification, in transformers and language models connected by spawning, shared pretraining or alignment, and does it carry from pairs to the many-model averages practice uses, model soups and SWA?

## Why it is a question

THEORY-111 holds that, between two linearly connected image classifiers,
nearly every layer's features at three points on the line were
proportional to the interpolation of the endpoints' features. Every
measurement is of a pair of endpoints, in image classification. Whether
the same holds in other architectures and tasks, and whether averaging many
models' weights averages their features, is not shown.

## What would answer it

THEORY-111's former promote_when, unchanged:

Two kinds of result, one for each half. For the layerwise claim, the
same measurement outside image classification: transformers and
language models, linearly connected by spawning, by fine-tuning from a
shared pretrained model or by alignment. It is refuted by a pair that
is linearly connected at the output while some intermediate layer's
interpolated features point away from the interpolated features. For
the averaging claim, the measurement on the averages practice actually
uses: soups of many fine-tuned models and SWA iterates, with the
features of the averaged network compared with the average of the
members' features. It is refuted if the claim holds for pairs but
fails for many-model averages. An approximate version of Zhou et al.'s
Theorem 1, bounding the feature error by the size of the
weak-additivity and commutativity residuals, would also move it. More
pairwise image-classifier measurements would not.
