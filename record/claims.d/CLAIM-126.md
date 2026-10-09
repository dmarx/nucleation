---
number: 126
status: Proposed
formerly:
- CLAIM-tmpkx2sz
title: 'Model stitching tests whether a transport preserves decision-relevant information only in its reconstruction form: a map fitted to reproduce the target representation certifies one direction of Blackwell sufficiency, while task-loss stitching compares one decision problem through a fixed head, and a failure to stitch is no evidence against sufficiency'
version: 1
role: thesis
defeated_if: >-
  A representation is exhibited that a map of the stitching class
  reproduces on the input distribution (s ∘ r = target layers) while some
  decision problem on the label is solved worse from r than from the
  target layers; or task-loss stitching penalties are shown, for the map
  class in use, to agree with Blackwell's order on every pair of
  representations tested, invertible reparametrisations included.
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-09'
line: pragmatic-transport
rests_on:
- CLAIM-050
complements:
- CLAIM-125
grounds:
- THEORY-176
- THEORY-156
- LIT-363
- LIT-850
- THEORY-175
summary: >-
  Proposed by the record on 2026-10-09 as an operational handle on the
  decision-relevant half of [CLAIM-125](CLAIM-125.md), and qualified by the reading of
  Bansal, Nakkiran & Barak before it was filed: only reconstruction-fitted
  stitching certifies sufficiency, and only within the map class.
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-125 THEORY-176 THEORY-156 THEORY-175 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-126: Model stitching tests whether a transport preserves decision-relevant information only in its reconstruction form: a map fitted to reproduce the target representation certifies one direction of Blackwell sufficiency, while task-loss stitching compares one decision problem through a fixed head, and a failure to stitch is no evidence against sufficiency

## The claim

[CLAIM-125](CLAIM-125.md) leaves open when a transport between scenarios preserves
decision-relevant information, and [CLAIM-050](CLAIM-050.md) takes Blackwell's order
([THEORY-156](../theory.d/THEORY-156.md)) as the measure of that. Model stitching is the machine-learning
practice closest to a test of it. A learned map s carries one network's
representation r into another network at layer ℓ, and the result is judged
by what the second network can then do.

Stitching comes in two forms, and only one of them is a test of Blackwell's
order:

- **Reconstruction form.** Here s is fitted so that s ∘ r reproduces the
  target layers, φ′ ≈ E φ in Lenc and Vedaldi ([LIT-363](../literature.d/LIT-363.md)). If it succeeds on
  the input distribution, then given each label the target representation
  is a function of r. The target is then a garbling of r, and r is at least
  as informative for every decision problem on the label ([THEORY-176](../theory.d/THEORY-176.md),
  relation 4). Success certifies one direction of sufficiency.
- **Task-loss form.** Here s is fitted to minimise the second network's
  task loss, the protocol of Bansal, Nakkiran and Barak ([LIT-850](../literature.d/LIT-850.md)).
  The stitching penalty then compares one decision problem, through a
  fixed head and a restricted map class. Both of its losses are upper
  bounds on the best attainable risk, so the penalty orders neither, and
  it is not invariant under invertible reparametrisation
  ([THEORY-176](../theory.d/THEORY-176.md), relations 1–3). A negative penalty, the paper's
  evidence that "more is better", shows that the fitted map did not
  reproduce the layers it replaced.

In both forms the test runs in one direction. A failure to stitch says only
that no map in the class works. The information may still be there in a
form the class cannot reach: Lenc and Vedaldi's identity stitch fails
between networks that a learned linear map makes interchangeable.

Relative representations ([THEORY-175](../theory.d/THEORY-175.md)) are a third route. The map is
replaced by a fixed construction, cosine similarity to matched anchor
points, and that construction is blind exactly to the cosine-preserving
maps. It moves the correspondence problem into the choice of anchors. What
it transports is judged by task performance alone, so it is the task-loss
form's evidence, not the reconstruction form's.

## What it does not say

It does not say stitching answers [CLAIM-125](CLAIM-125.md). Even in reconstruction form the
certificate covers one pair of representations on one input distribution,
for decisions about the label used to define the experiment. It gives no
characterisation of which transports preserve information, and no measure
of how much a non-sufficient transport loses; that is Le Cam's deficiency
([THEORY-156](../theory.d/THEORY-156.md)). It does not say task-loss stitching is useless. It is the
right test when the decision problem really is fixed in advance, which is
[CLAIM-050](CLAIM-050.md)'s point that fidelity is relative to the receiver's decisions. It
says that the penalty is not, by itself, an order of information.
