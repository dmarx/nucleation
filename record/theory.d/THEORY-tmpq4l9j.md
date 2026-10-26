---
status: Proposed
promote_when: >-
  A result that ties the interaction between candidate circuits to which
  coordinates they share, independently of the projected scan that
  suggested it. Either a derivation from the reduced dynamics on the
  seven circuit coordinates that predicts where the boundaries between
  winners fall and why they are sharp between circuits needing the same
  layers and soft between circuits sharing a unit; or an unconstrained
  training run (not projected onto the seven coordinates after every
  step), varying more than two initial strengths, that reproduces the
  same winners and the same sharp and soft boundaries. It is refuted by
  unconstrained training in which the boundaries' sharpness does not
  follow shared coordinates, or by circuits sharing a unit whose
  boundary is as sharp as that of circuits contending for a layer.
  Further scans of the same projected system cannot settle it, since the
  scan is what the reading was drawn from.
title: 'In a transformer whose candidate circuits are sets of shared elementary coordinates, how circuits interact during training is set by what they share: circuits that share a unit cooperate, and circuits that need the same layers for different roles compete, so that which circuit wins is decided by the initialization of units beyond its own, with sharp boundaries between competitors and soft ones between cooperators, as Musat, Pimentel, Zucchet and Hofmann read their three-layer scan'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmpcuw4h. The scan is the paper's §4.3 and
    Appendix E; the cooperative and competitive reading is the authors',
    offered as an interpretation the learning curves "appear to support".
    The phase diagram itself was read from the text and caption, not seen
    as an image.
tags:
- learning-theory
- representation-learning
date: '2026-10-26'
source:
- LIT-tmp01if4
summary: >-
  Musat et al. (2026), LIT-tmp01if4, read in NOTE-tmpcuw4h. In projected
  SGD training of a three-layer single-head attention-only transformer on
  in-context bigrams, three induction circuits are possible, and the
  winner depends on initial strengths outside the winner itself. The
  authors explain the pattern by cooperation through a shared unit and
  competition for layers. The evidence is one scan over two initial
  strengths with every other coordinate zeroed, in projected training.
---

# THEORY-tmpq4l9j: In a transformer whose candidate circuits are sets of shared elementary coordinates, how circuits interact during training is set by what they share: circuits that share a unit cooperate, and circuits that need the same layers for different roles compete, so that which circuit wins is decided by the initialization of units beyond its own, with sharp boundaries between competitors and soft ones between cooperators, as Musat, Pimentel, Zucchet and Hofmann read their three-layer scan

## Source

Musat, Pimentel, Zucchet and Hofmann (2026), arXiv:2607.11875,
LIT-tmp01if4, read in full in NOTE-tmpcuw4h: §4.3, Fig. 4, Appendix E.1
(setup) and E.2 (Fig. 7, twelve seeds).

## What is asserted, and by whom

**The measurement.** A three-layer, one-head-per-layer attention-only
transformer of width 256, trained with vanilla SGD on in-context bigrams
with every token rare (fr = 1), so only an induction circuit solves the
task. Three induction circuits are possible: on layers (1, 2) with units
(α, β, γ), on (1, 3) with (α, β′, γ′), and on (2, 3) with (α′, β″, γ′).
After every step the weights are projected onto the seven coordinates
α, α′, β, β′, β″, γ, γ′. Each seed draws the initial strengths of β and
β″ uniformly from [0, 0.6], zeroes every other coordinate, and is coloured
by the circuit whose ablation-reduced model has the lowest loss after
training. The scan "aggregates several thousand seeds".

**The pattern** (the paper's words). "The simplest initialization-based
predictor … would be that each circuit wins when its own units start
large." It holds for the (2, 3) circuit. "However, the (α, β′, γ′)-circuit
… seems to benefit from a larger β, which is not part of this circuit.
Moreover, the (α, β, γ)-circuit … seems to require not just a large β …
but also a large β″ (not part of the circuit)." The boundaries "are very
sharp between the blue and green solutions and between blue and red, but
not between green and red".

**The reading, the authors'.** "This is because the red and green circuits
are cooperative: both share α, while β and β′ are in different layers.
Meanwhile, blue is competing with both red and green, trying to use the
same layers in different ways. This might also explain why red requires a
large β″: it stimulates the blue circuit, which in turn inhibits the green
circuit."

The general thesis filed here is that reading: interaction between
circuits in training is set by the coordinates and layers they share.

## What the record holds toward it

- THEORY-tmpdxhxm (Active): in this class the circuits are sets of
  coordinates of an invariant subspace, so "sharing a unit" is well
  defined, which it is not for circuits found by head-level attribution.
- THEORY-tmpvqsx2 (Active): two circuits that solve overlapping parts of
  the data interact through the gradient they share even when their
  coordinates are orthogonal. That is the competitive half in another
  form.
- Nothing in the record derives the boundaries, and the scan was run in
  projected training only.

## What would confirm or reject it

The promote_when above.

## Bearing

This is the interaction QUESTION-tmpivbso's construction proposes to
model, coupling a feature allocation to circuit interaction: here the
allocation (which units each circuit uses) is exact and the interaction
follows it. If the thesis holds, the question's coupled description has a
known comparator in this class, the reduced dynamics on the shared
coordinates.
