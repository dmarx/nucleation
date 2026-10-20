---
number: 202
status: Open
formerly:
- QUESTION-tmpybmwx
title: 'Does neural collapse hold outside its first protocol, under augmentation, label noise, class imbalance and several seeds per setting, and does gradient descent on cross-entropy provably reach it?'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-20'
line: learned-structure
refines:
- QUESTION-051
summary: >-
  The promotion condition formerly on [THEORY-083](../theory.d/THEORY-083.md), moved here when [THEORY-083](../theory.d/THEORY-083.md)
  was narrowed to the runs Papyan, Han and Donoho plotted and promoted on
  2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3). Those runs had balanced classes, no
  augmentation, dropout removed and one plotted run per learning rate.
  Whether collapse holds outside that protocol, and why training reaches
  it, is open.
answered_by:
- THEORY-788
---

# QUESTION-202: Does neural collapse hold outside its first protocol, under augmentation, label noise, class imbalance and several seeds per setting, and does gradient descent on cross-entropy provably reach it?

## Why it is a question

Papyan, Han & Donoho ([LIT-618](../literature.d/LIT-618.md), read in [NOTE-476](../notes.d/NOTE-476.md), whose figures were read
from the plots on 2026-10-20) measured the four collapses through the
terminal phase of training for VGG, ResNet and DenseNet on seven balanced
datasets, with no augmentation, dropout removed and one plotted run per
dataset and network. Every measure moved toward collapse, close to
completion on the easier datasets and partially on ImageNet ([THEORY-083](../theory.d/THEORY-083.md)).
Until 2026-10-20 the rest was [THEORY-083](../theory.d/THEORY-083.md)'s promote_when; it moved here when
the title was narrowed to those runs.

## What would answer it

- Measurements of NC1 and NC2 through the terminal phase under data
  augmentation, label noise and several seeds per setting, and of NC1
  under class imbalance. Under imbalance the geometry to test is that of
  [THEORY-286](../theory.d/THEORY-286.md), not equiangularity: NC2 is predicted for balanced classes
  only.
- A held paper that derives collapse as the limit of gradient descent on
  cross-entropy. [LIT-974](../literature.d/LIT-974.md) derives it for MSE under a re-whitened flow
  ([THEORY-278](../theory.d/THEORY-278.md)), and [LIT-994](../literature.d/LIT-994.md) gives an endpoint, not a gradient-descent
  derivation ([THEORY-286](../theory.d/THEORY-286.md)).

It would be answered in the negative if standard training run well past
zero error leaves within-class variability of last-layer features flat, or,
with balanced classes, leaves the centred class means far from
equiangular. Further runs under the original protocol cannot settle it, nor
can the theorems, which assume the collapsed end state.
