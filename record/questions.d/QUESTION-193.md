---
number: 193
status: Open
formerly:
- QUESTION-tmpihczu
title: 'Does sign descent provably delay each weaker skill until the stronger one is learned when a loss''s eigendirections are misaligned with the coordinates, and does changing only the optimizer turn a trained network''s simultaneous skill onsets into a sequence?'
version: 1
tags:
- learning-theory
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-039
summary: >-
  The promotion condition formerly on [THEORY-253](../theory.d/THEORY-253.md). [THEORY-253](../theory.d/THEORY-253.md) was narrowed
  to what Liu, Liu, Michaud, Gore and Tegmark measured in their Geometry
  model and promoted on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3): skills progress together
  under gradient descent and in sequence under sign descent, with the
  ratio of onset times saturating at 2, and on a rotated quadratic only
  when the eigendirections are misaligned with the coordinates. That is
  simulation. A derivation, and a test on a trained network, are open.
answered_by:
- THEORY-783
---

# QUESTION-193: Does sign descent provably delay each weaker skill until the stronger one is learned when a loss's eigendirections are misaligned with the coordinates, and does changing only the optimizer turn a trained network's simultaneous skill onsets into a sequence?

## Why it is a question

[THEORY-253](../theory.d/THEORY-253.md) holds the Geometry model's measured result, reproduced by the
record in a small simulation. Under gradient descent orthogonal skills
evolve independently, each at a rate set by its frequency, which follows
from the decoupled dynamics. Under sign descent a weaker skill makes
rapid progress only once a stronger one is done, and t₂/t₁ approaches 2.
On a rotated quadratic the sequence appears only when the eigendirections
are misaligned with the coordinates. The mechanism offered, that
sign(g₁ + g₂) ≈ sign(g₁) when ‖g₁‖ ≫ ‖g₂‖, is not a proof, and the Resource
model that matches the curves was fitted to them. Until 2026-10-19 this
was [THEORY-253](../theory.d/THEORY-253.md)'s promote_when.

## What would answer it

- An analysis of sign descent, or of Adam at small β, on a sum of
  frequency-weighted quadratic losses whose eigendirections are not
  aligned with the coordinates, deriving the delayed onset of each weaker
  skill and the ratio t₂/t₁ → 2.
- A trained network on independent skills of unequal frequency whose
  onsets go from simultaneous to sequential when only the optimizer is
  changed from gradient descent to sign descent.

Against it: orthogonal skills that start one after another under plain
gradient descent without small-initialization plateaus, or sign descent
on a rotated quadratic that learns all directions together.

What would not answer it: further fits of the Resource model, which was
fitted to the behaviour it would be confirming.
