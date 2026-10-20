---
status: Proposed
promote_when: >-
  An analysis of sign descent, or of Adam at small β, on a sum of
  frequency-weighted quadratic losses whose eigendirections are not
  aligned with the coordinates. It would need to derive the delayed onset
  of each weaker skill, and the ratio t₂/t₁ → 2, that the paper shows only
  in simulation. Or a trained network on independent skills of unequal
  frequency whose onsets go from simultaneous to sequential when only the
  optimizer is changed from SGD to sign descent. It is refuted by a case
  in which orthogonal skills under plain gradient descent start one after
  another without small-initialization plateaus, or by sign descent on a
  rotated quadratic that learns all directions together. Further fits of
  the Resource ODE cannot settle it, since that model was fitted to the
  behaviour it would be confirming.
title: 'In neural-network training, sign-descent-like optimizers such as Adam make independent skills of unequal frequency compete for coordinate signs, so that they are learned one after another where gradient descent would learn them together; this is one source of sequential skill onset, beside dependence between skills, as Liu, Liu, Michaud, Gore and Tegmark propose'
version: 1
tags:
- learning-theory
date: '2026-10-20'
source:
- LIT-951
summary: >-
  Liu, Liu, Michaud, Gore and Tegmark (2025), [LIT-951](../literature.d/LIT-951.md), read in [NOTE-794](../notes.d/NOTE-794.md).
  The paper explains the Domino effect, skills starting as others finish,
  by a coordinate-wise optimizer's competition for update signs.
  [THEORY-253](THEORY-253.md) holds the simulation in their Geometry model and the rotated
  quadratic. The paper also shows dependent skills starting after their
  prerequisites (C5), so the optimizer is one source of sequential onset,
  not the only one. The test in a trained network is [QUESTION-193](../questions.d/QUESTION-193.md).
extends:
- THEORY-253
answers:
- QUESTION-193
---

# THEORY-tmpnt3o1: In neural-network training, sign-descent-like optimizers such as Adam make independent skills of unequal frequency compete for coordinate signs, so that they are learned one after another where gradient descent would learn them together; this is one source of sequential skill onset, beside dependence between skills, as Liu, Liu, Michaud, Gore and Tegmark propose

## Source

Liu, Liu, Michaud, Gore and Tegmark (2025), [LIT-951](../literature.d/LIT-951.md), read in [NOTE-794](../notes.d/NOTE-794.md):
§§2.2–2.6 and the paper's framing of the Domino effect in skill learning.

## What is asserted

That when skills share parameters, an optimizer that acts on each
coordinate's sign, as sign descent does and Adam partly does, gives the
dominant skill nearly all the update directions until its gradient
vanishes, and only then lets the next one move. Under plain gradient
descent orthogonal skills do not interact, and each proceeds at a rate
set by its frequency. So the order of skill onsets in real training is in
part an effect of the optimizer.

## What the Active account establishes toward it

[THEORY-253](THEORY-253.md) holds the Geometry model's simulations, reproduced by the
record: skills progress together under gradient descent and in sequence
under sign descent, with the ratio of onset times approaching 2, and on a
rotated quadratic only when the eigendirections are misaligned with the
coordinates. That is a toy model and simulation, with no derivation and
no trained network.

## Why "one source" and not "the cause"

The title [THEORY-253](THEORY-253.md) carried before it was narrowed said sequential onset
"comes from the optimizer". The paper's own §5.1 shows dependent skills in
a two-layer network starting after their prerequisites, beyond what
frequency predicts ([NOTE-794](../notes.d/NOTE-794.md), C5). So the paper does not assert the
optimizer as the only cause, and this entry does not.

## What would confirm or reject it

The promote_when above, [QUESTION-193](../questions.d/QUESTION-193.md)'s test.

## Provenance

Filed on 2026-10-20 by the narrowing-loss sweep ([ADR-047](../decisions.d/ADR-047.md) v4, batch 068),
from the wider title [THEORY-253](THEORY-253.md) carried before it was narrowed on
2026-10-19.
