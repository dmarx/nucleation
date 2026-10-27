---
number: 986
status: Proposed
formerly:
- THEORY-tmpgz1nk
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
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1182, the reading of Zoom In in full, as
    its third "speculative claim". The authors call their evidence
    anecdotal.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Curve Detectors, registered and read on
    2026-10-27, gives as its only cross-model evidence the combing
    phenomenon in a few models and one macaque neuron, and defers
    prevalence across models; the account stays Proposed.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-1543
summary: >-
  Olah et al. (2020), [LIT-1543](../literature.d/LIT-1543.md), read in [NOTE-1182](../notes.d/NOTE-1182.md): Claim 3, the
  universality hypothesis. Curve detectors and high-low frequency detectors
  are reported in AlexNet, InceptionV1, VGG19 and ResNetV2-50, with
  InceptionV3, a Places365 model and conv nets trained from scratch named
  in the text. The authors: "the only evidence we can offer today is
  anecdotal".
---
<!-- inactive-ok-file: CLAIM-263 THEORY-1013 — Proposed; the claims this bears on, cited as open -->

# THEORY-986: Analogous features and circuits form across neural networks trained on different architectures, data and tasks, so that a feature or circuit found in one model can be expected in others, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose under the name universality

## Source

Olah et al. (2020), *Zoom In*, [LIT-1543](../literature.d/LIT-1543.md), read in full in
[NOTE-1182](../notes.d/NOTE-1182.md): Claim 3.

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

- **[CLAIM-263](../claims.d/CLAIM-263.md)** proposes a test of whether two trained networks compute
  the same way. Universality is the hypothesis that, for analogous models,
  that test would mostly find shared structure.
- **[THEORY-1013](THEORY-1013.md)** is the companion claim that features and circuits
  are the units in the first place; universality presupposes it.
- The essay notes that universality is not needed for circuits research,
  but would decide which kind makes sense.

## Note of 2026-10-27: Curve Detectors' cross-model evidence

*Curve Detectors* ([LIT-tmp73ge1](../literature.d/LIT-tmp73ge1.md), [NOTE-tmptb2tz](../notes.d/NOTE-tmptb2tz.md)), read on 2026-10-27,
adds one sighting of the kind the promote_when says cannot settle this:
"combing", excitation of curve units by short lines perpendicular to the
curve, is seen in the curve units of AlexNet, InceptionV1, InceptionV3
and a Places365 model, and in the optimized stimulus of one macaque V4
neuron, from feature visualizations only. The article defers "prevalence
across models" to a later part of the thread. Nothing here compares
features or circuits across models rigorously, so the account stays
Proposed.
