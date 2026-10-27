---
number: 193
status: Open
formerly:
- QUESTION-tmpihczu
title: 'Does sign descent provably delay each weaker skill until the stronger one is learned when a loss''s eigendirections are misaligned with the coordinates, and does changing only the optimizer turn a trained network''s simultaneous skill onsets into a sequence?'
version: 2
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: a theory of invariant learning dynamics in
    transformers, read on 2026-10-26, gives a trained-network setting in
    which the second limb could be run, with the coordinates on which
    onsets would be measured. The question is unchanged.
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

## Note of 2026-10-26: a testbed for the second limb

Musat, Pimentel, Zucchet and Hofmann's theory of invariant learning
dynamics ([NOTE-tmpcuw4h](../notes.d/NOTE-tmpcuw4h.md)), read on 2026-10-26 for the exchange
"Experimental Infrastructure Review" ([QUESTION-tmpivbso](QUESTION-tmpivbso.md)), gives a ready
setting for this question's trained-network test. For attention-only
transformers on block-list inductive tasks, the weights the data's
symmetries fix form a subspace that population gradient descent never
leaves, spanned by a few elementary actions composed through the heads
([THEORY-tmpdxhxm](../theory.d/THEORY-tmpdxhxm.md)). The record's check found that sign descent keeps the
subspace only when those actions are aligned with the parameter
coordinates.

So the test could be: train the same block-list task with gradient
descent and with sign descent, with embeddings rotated off the
coordinates, and compare the onset order of the circuit coordinates (the
in-weights coordinate against the induction circuit's three). The theory
supplies the coordinates on which onsets are measured, which the
Geometry model's skills supply by construction.

Two limits. The circuits there are not independent skills: they solve
overlapping parts of the data, and that alone delays the induction
circuit under gradient descent ([THEORY-tmpvqsx2](../theory.d/THEORY-tmpvqsx2.md)), so a sequence under
both optimizers would not answer the question either way. And the paper's
own §5 trained with AdamW, outside its theorem, with no gradient-descent
run for contrast. Neither the induction-heads paper nor the other works
read with it varies the optimizer. The question is unchanged.
