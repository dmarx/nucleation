---
number: 1013
status: Proposed
formerly:
- THEORY-tmpx97zh
promote_when: >-
  A systematic count, not chosen examples: for whole layers of trained
  networks, a stated criterion of what makes a unit or direction an
  understood feature (for instance, the seven arguments Zoom In applies to
  curve detectors), the fraction of units that meet it, and for the
  connections between understood features, weight-level predictions of
  what editing them changes, tested by editing them. Confirmed if most of a
  layer's capacity is accounted for by such features and their circuits
  predict edits; refuted if the understood features are a small and
  unrepresentative minority, or if circuit-level predictions fail under
  edits. More well-chosen examples cannot settle it.
title: 'In trained vision networks, units or other directions in a layer''s activation space are typically meaningful features, and the weights between understood features implement algorithms that can be read off them, so that features and their circuits are the units in which such a network can be understood, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-1182, the reading of Zoom In in full. The
    essay offers it as the first two of three "deliberately speculative"
    claims, with qualitative examples from one model.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Curve Detectors, the first of the articles
    Zoom In defers its evidence to, was registered and read on
    2026-10-27. It supplies four of the seven arguments for one family
    and no fraction of a layer, so the promote_when is not met and the
    account stays Proposed.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-1543
summary: >-
  Olah et al. (2020), [LIT-1543](../literature.d/LIT-1543.md), read in [NOTE-1182](../notes.d/NOTE-1182.md): Claims 1 and 2
  of the essay. The evidence is a set of examples in InceptionV1 (curve,
  high-low frequency and dog head detectors; the curve, oriented dog head
  and car circuits), argued with feature visualization, dataset examples,
  synthetic stimuli, tuning curves and the weights. The essay names
  polysemantic neurons as the main obstacle. It gives no count of how much
  of a layer is understood.
---
<!-- inactive-ok-file: THEORY-986 THEORY-802 — Proposed; the companion claim from the same essay and the basis-relative account it is set beside, cited as open -->
<!-- inactive-ok-file: THEORY-1022 — Proposed; the Curve Detectors authors' full claim, cited as open -->

# THEORY-1013: In trained vision networks, units or other directions in a layer's activation space are typically meaningful features, and the weights between understood features implement algorithms that can be read off them, so that features and their circuits are the units in which such a network can be understood, as Olah, Cammarata, Schubert, Goh, Petrov and Carter propose

## Source

Olah, Cammarata, Schubert, Goh, Petrov and Carter (2020), *Zoom In: An
Introduction to Circuits*, Distill, [LIT-1543](../literature.d/LIT-1543.md), read in full in
[NOTE-1182](../notes.d/NOTE-1182.md): Claims 1 and 2, the glossary, and Interpretability as a
Natural Science.

## What is asserted

That a trained network "consist[s] of meaningful, understandable
features", directions in activation space, usually neurons, and that the
weights between features in adjacent layers are "meaningful algorithms
corresponding to facts about the world" that can be read off. The essay
offers these as empirical claims and as norms for how to study networks.

## What the record holds toward it

- **Curve detectors in InceptionV1's mixed3b**, argued seven ways,
  including a hand-set reimplementation that mimics the originals.
- **Three circuits**: curve detectors built from earlier curve detectors
  along the tangent, with weights that rotate with orientation; a
  four-layer oriented dog head circuit; and a car feature spread over dog
  neurons.
- **Its own counter-case**: polysemantic neurons such as 4e:55 (cat faces,
  car fronts, cat legs), "a major challenge for the circuits agenda".

## Why it stays Proposed

The essay calls its claims speculative and defers the evidence. The
examples were chosen, from one model, with no denominator, and the
counter-case is acknowledged and unresolved. The transformer work that
follows ([LIT-1534](../literature.d/LIT-1534.md)) reports it "had a lot more success" with attention
heads than with neurons, and that MLP neurons have been "much harder to
develop hypotheses for".

## What this does not say

- Not that every neuron is a feature: polysemantic neurons are granted.
- Not that features are unique directions: a direction is a linear
  combination of neurons, and the essay does not ask whether another basis
  would serve as well (the question of [THEORY-802](THEORY-802.md)).
- Not anything about how features or circuits form in training.

## What would confirm or reject it

The promote_when above.

## Note of 2026-10-27: Curve Detectors, read

Cammarata et al.'s *Curve Detectors* ([LIT-1575](../literature.d/LIT-1575.md), [NOTE-1198](../notes.d/NOTE-1198.md)), the
first of the articles Zoom In defers its evidence to, was registered and
read on 2026-10-27 at the owner's request. Of Zoom In's seven arguments
for a curve detector, it supplies four for the mixed3b family (feature
visualization, dataset examples, synthetic curves and joint tuning under
rotation, with attribution and blind labelling added), measured as
[THEORY-1028](THEORY-1028.md). The other three (the implementing circuit, the
downstream use and the hand-written reimplementation) are deferred again,
to *Curve Circuits*, which the record does not hold. The authors' full
claim of causality, generality and purity is [THEORY-1022](THEORY-1022.md), Proposed.

The article gives no count over a layer: the family is ten of mixed3b's
480 units, about 2%. The promote_when's "fraction of units that meet" a
stated criterion is therefore not supplied, and the account stays Proposed
for the reason it already gives: chosen examples, no denominator. The
likeliest source of such a count is the thread's *An Overview of Early
Vision in InceptionV1*, which sorts the early layers' units into families;
it is not registered.
