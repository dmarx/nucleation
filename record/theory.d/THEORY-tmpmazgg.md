---
status: Active
title: 'In InceptionV1 trained on ImageNet, the ten curve units of layer mixed3b each respond most to curves of one orientation, with responses invariant to fill and colour and jointly spanning all orientations under rotation of real images; for one of them, 3b:379, which fires on about 11% of dataset positions, activation level separated one author''s blind four-class labels of over 800 activation-binned images, and curves and imperfect curves made up 55% of its contribution to expected value'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmptb2tz, the reading of Cammarata et al.
    (2020) in full. One study, read in full; the title claims no more than
    the article measured and states, and nothing in the record contradicts
    it (ADR-047 v3). The authors' fuller claim, that the units detect
    curves causally, generally and purely, is THEORY-tmpb0s0r, Proposed.
tags:
- representation-learning
date: '2026-10-27'
source:
- LIT-tmp73ge1
summary: >-
  Cammarata et al. (2020), LIT-tmp73ge1, read in NOTE-tmptb2tz: the
  behaviour of the mixed3b curve family as measured by feature
  visualization, rotated dataset examples, synthetic curves and, for one
  unit, activation statistics and blind hand labels. It holds for the
  neuron basis of one model. It does not say how the units are computed,
  what their weak firings encode, or what fraction of the layer is
  understood.
extended_by:
- THEORY-tmpb0s0r
---
<!-- inactive-ok-file: THEORY-tmpb0s0r THEORY-1013 — Proposed; the authors' full claim and the Zoom In account this example serves, cited as open -->
# THEORY-tmpmazgg: In InceptionV1 trained on ImageNet, the ten curve units of layer mixed3b each respond most to curves of one orientation, with responses invariant to fill and colour and jointly spanning all orientations under rotation of real images; for one of them, 3b:379, which fires on about 11% of dataset positions, activation level separated one author's blind four-class labels of over 800 activation-binned images, and curves and imperfect curves made up 55% of its contribution to expected value

## Source

Cammarata, Goh, Carter, Schubert, Petrov and Olah (2020), *Curve
Detectors*, Distill, LIT-tmp73ge1, read in full in NOTE-tmptb2tz: Feature
Visualization, Dataset Analysis, Visualizing Attribution, Human
Comparison, Joint Tuning Curves, Synthetic Curves and Synthetic Angles. The
figures were not rendered; the numbers are those the text states.

## What was actually shown

**The units.** The ten units of mixed3b whose feature visualizations are
curves. Every optimization for maximal firing, with or without a
diversity term, gives a curve.

**Orientation and the family.** Each unit's top dataset examples, rotated
in 1° steps, drive that unit in a bump around one orientation, and as one
unit stops firing the next starts, so that the ten together cover 360°.
The article notes gaps, partly filled by double-curve units.

**Synthetic stimuli.** Rendered curves varied in orientation and curvature
drive 3b:379 up to 24 standard deviations above its mean dataset
activation, most for curves like its visualization. The response is wider
in orientation at higher curvature, and unchanged by filling or colouring
the shape. Angles drive it where an arm is tangent to its preferred curve.

**One unit on the data.** 3b:379 fires (pre-ReLU above zero) on 11% of
receptive-field crops. One author labelled over 800 images drawn at random
in activation bins, seeing pixels only: curve, imperfect curve, unrelated,
opposing curve. The labels sort by activation level. Weighting each level
by x·p(x), curves and imperfect curves account for 55% of the unit's
contribution to expected value.

**What could have come out otherwise.** Visualizations could have been
textures or varied by seed. Rotated examples could have left the unit
unmoved, or the family could have left orientations uncovered. Fill or
colour could have mattered. Blind labels could have been spread evenly
across activation levels. Strongly firing images could have been clocks
for reasons attribution would show were not curves.

## What this does not say

- **Not that the units are pure.** Most of 3b:379's firings are weak, most
  images labelled curves fall where it fires weakly or not at all, and the
  other 45% of its contribution to expected value is not accounted for.
  The authors' claim of purity is THEORY-tmpb0s0r.
- **Not how the units are computed.** The circuit and the hand-written
  reimplementation are in a later article, not read.
- **Not about other models or bases.** One network, its neuron basis.
- **Not a count.** Ten of mixed3b's 480 units; nothing here says how much
  of the layer is understood, which THEORY-1013's promote_when requires.
- **The units are not robust.** Small changes in orientation or curvature
  swing activations by several standard deviations.

## Connections

- **THEORY-1013.** The worked example that account cites, measured. It
  supplies four of Zoom In's seven arguments for one family, and none of
  the count the account's promote_when asks for.
- **THEORY-991.** In a one-layer transformer the neurons were the
  uninterpretable basis and dictionary features the interpretable one.
  This family is a case where the neuron basis itself is clean; the
  article does not ask how typical that is.
