---
status: Proposed
promote_when: >-
  A comparative study of the kind Zoom In itself specifies: features
  characterized rigorously in several independently trained models (of
  different architectures or seeds), shown to be the same features rather
  than merely correlated ones, and shown to be connected by the same weight
  structure in each, over several layers rather than only the first ones.
  Refuted, for a class of models, if such a study finds that beyond the
  lowest layers the features or their connections differ between models
  trained on the same task. Further sightings of one low-level feature
  family in another architecture cannot settle it: that is the anecdote it
  rests on now.
title: 'Analogous features and circuits form across neural networks trained on different architectures, data and tasks, so that a feature or circuit found in one model can be expected in others, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose under the name universality'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmplg2yz, the reading of Zoom In in full, as
    its third "speculative claim". The authors call their evidence
    anecdotal.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-tmplq91w
summary: >-
  Olah et al. (2020), LIT-tmplq91w, read in NOTE-tmplg2yz: Claim 3, the
  universality hypothesis. Curve detectors and high-low frequency detectors
  are reported in AlexNet, InceptionV1, VGG19 and ResNetV2-50, with
  InceptionV3, a Places365 model and conv nets trained from scratch named
  in the text. The authors: "the only evidence we can offer today is
  anecdotal".
---
<!-- inactive-ok-file: CLAIM-263 THEORY-tmpx97zh — Proposed; the claims this bears on, cited as open -->

# THEORY-tmpgz1nk: Analogous features and circuits form across neural networks trained on different architectures, data and tasks, so that a feature or circuit found in one model can be expected in others, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose under the name universality

## Source

Olah et al. (2020), *Zoom In*, LIT-tmplq91w, read in full in
NOTE-tmplg2yz: Claim 3.

## What is asserted

"Analogous features and circuits form across models and tasks." In its
strongest form, a "periodic table of visual features" observed and
catalogued across models; in its weakest, only some lessons transfer.

## What the record holds toward it

- **Two low-level feature families** (curve and high-low frequency
  detectors) seen in four vision architectures, a Places365 model and conv
  nets trained from scratch. Seen, not characterized as the same features.
- **Prior correlational work** the essay cites (convergent learning,
  SVCCA, CKA), which it judges "highly suggestive" but not definitive,
  since correlated features can differ.
- **Nothing about circuits across models.** No circuit is compared between
  two models.

## Why it stays Proposed

The authors' own words: "the only evidence we can offer today is
anecdotal: we simply have not yet invested enough in the comparative study
of features and circuits to give confident answers". They also state the
test, which the promote_when takes over.

## Connections

- **CLAIM-263** proposes a test of whether two trained networks compute
  the same way. Universality is the hypothesis that, for analogous models,
  that test would mostly find shared structure.
- **THEORY-tmpx97zh** is the companion claim that features and circuits
  are the units in the first place; universality presupposes it.
- The essay notes that universality is not needed for circuits research,
  but would decide which kind makes sense.
