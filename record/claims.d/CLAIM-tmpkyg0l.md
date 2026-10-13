---
status: Proposed
title: 'Model stitching certifies an order of information only in its reconstruction
  form: a map fitted to reproduce the target layers shows the source representation
  is at least as informative for every decision on the label, task-loss stitching
  compares one decision problem through a fixed head, and a failure to stitch
  is no evidence against sufficiency'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-126 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-126 rests on; CLAIM-126
    now rests on this claim.
role: thesis
defeated_if: A representation that a map of the stitching class reproduces
  on the input distribution (s ∘ r equal to the target layers) while some
  decision problem on the label is solved worse from r than from the target
  layers. Or task-loss stitching penalties shown, for the map class in use,
  to agree with Blackwell's order on every pair of representations tested,
  invertible reparametrisations included.
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- THEORY-176
- LIT-363
- LIT-850
summary: The general content of [CLAIM-126](CLAIM-126.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the result about stitching does not rest on [CLAIM-050](CLAIM-050.md)'s account of fidelity.
  Reconstruction-fitted stitching makes the target a garbling of the source
  given the label, which certifies one direction of Blackwell sufficiency
  ([THEORY-176](../theory.d/THEORY-176.md)). Task-loss stitching ([LIT-850](../literature.d/LIT-850.md)) compares one decision problem
  through a fixed head, orders neither representation, and is not invariant
  under reparametrisation. In both forms a failure says only that no map in
  the class works.
supports:
- CLAIM-126
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-126 THEORY-176 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-tmpkyg0l: Model stitching certifies an order of information only in its reconstruction form: a map fitted to reproduce the target layers shows the source representation is at least as informative for every decision on the label, task-loss stitching compares one decision problem through a fixed head, and a failure to stitch is no evidence against sufficiency

## The claim

Model stitching carries one network's representation r into another
network at layer ℓ through a learned map s, and judges the result by what
the second network can then do. It comes in two forms, and only one of
them tests an order of information:

- **Reconstruction form.** s is fitted so that s ∘ r reproduces the target
  layers, as in Lenc and Vedaldi ([LIT-363](../literature.d/LIT-363.md)). If it succeeds on the input
  distribution, then given each label the target representation is a
  function of r. The target is then a garbling of r, and r is at least as
  informative for every decision problem on the label ([THEORY-176](../theory.d/THEORY-176.md)). Success
  certifies one direction of sufficiency.
- **Task-loss form.** s is fitted to minimise the second network's task
  loss, the protocol of Bansal, Nakkiran and Barak ([LIT-850](../literature.d/LIT-850.md)). The penalty
  compares one decision problem through a fixed head and a restricted map
  class. Both losses are upper bounds on the best attainable risk, so the
  penalty orders neither, and it is not invariant under invertible
  reparametrisation.

In both forms the test runs one way. A failure to stitch says only that no
map in the class works.

## Where the record applies it

[CLAIM-126](CLAIM-126.md) applies the result to the question of when a transport between
scenarios preserves decision-relevant information, resting on [CLAIM-050](CLAIM-050.md)'s
account of fidelity. It now also rests on this claim for the result about
stitching.

## What it does not say

- It does not characterise which transports preserve information, or
  measure how much a non-sufficient one loses. That is Le Cam's deficiency.
- It does not say task-loss stitching is useless. It is the right test
  when the decision problem really is fixed in advance.
