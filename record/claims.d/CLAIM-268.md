---
number: 268
status: Active
formerly:
- CLAIM-tmpkyg0l
title: 'Model stitching certifies an order of information only in its reconstruction
  form: a map fitted to reproduce the target layers shows the source representation
  is at least as informative for every decision on the label, task-loss stitching
  compares one decision problem through a fixed head, and a failure to stitch
  is no evidence against sufficiency'
version: 2
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-126 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-126 rests on; CLAIM-126
    now rests on this claim.
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/CLAIM-268.yaml,
    batch 003, ADR-047). The reconstruction step is now written out as a
    composition argument and no longer grounded on THEORY-176, which is
    Proposed only for the measured size of the effect. The claim's "not
    invariant under invertible reparametrisation" reads "not in general
    invariant", with a construction. The defeat condition's second disjunct
    was empirical: agreement on the pairs tested cannot refute a statement
    about what the penalty guarantees. It is restated as a proof of
    monotonicity. The claim is otherwise unchanged.
role: thesis
warrant: demonstrated
defeated_if: A representation that a map of the stitching class reproduces
  on the input distribution (s ∘ r equal to the target layers) while some
  decision problem on the label is solved worse from r than from the target
  layers. Or a proof that, for the map class in use, the task-loss stitching
  penalty is monotone in Blackwell's order on every pair of representations,
  invertible reparametrisations included.
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-13'
line:
- formal-apparatus
grounds:
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
<!-- inactive-ok-file: CLAIM-050 CLAIM-126 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-268: Model stitching certifies an order of information only in its reconstruction form: a map fitted to reproduce the target layers shows the source representation is at least as informative for every decision on the label, task-loss stitching compares one decision problem through a fixed head, and a failure to stitch is no evidence against sufficiency

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
  penalty orders neither, and it is not in general invariant under
  invertible reparametrisation.

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

## Note of 2026-10-19: the three steps, written out

**Reconstruction form: a composition argument.** Let Y be the label, r the
source representation and t the target layers, and let s ∘ r = t almost
surely on the input distribution. Then P(t | Y) = s#P(r | Y), so t is a
deterministic garbling of r about Y. Any decision rule δ that reads t gives
the rule δ ∘ s on r, with the same action under every input and so the same
risk under every label. So r is at least as informative as t for every
decision problem on Y. Nothing here needs a finite outcome space, and none
of it needs [THEORY-176](../theory.d/THEORY-176.md), which holds the measured size of the effect.

**Task-loss form: a difference of upper bounds.** The stitched network's
loss is the risk of one rule on r, the fixed head composed with s, so it
bounds from above the best risk attainable from r. The target network's
loss bounds the best risk from t in the same way. The penalty is a
difference of two upper bounds, so it orders neither minimum.

**Not in general invariant: a construction.** Use the 1×1 convolutional
stitcher of [LIT-850](../literature.d/LIT-850.md), which applies one channel map at each spatial position
and mixes no positions. Take inputs whose layer-ℓ activations at position
(0, 0) are independent of those at every other position, a label that is a
function of the activations at (0, 0), and a top network that reads only
position (0, 0). Let φ be a spatial permutation that moves (0, 0) to
another position. Then r and φ(r) are each a function of the other, so they
are equivalent in Blackwell's order. Stitched into the top network, r with
the identity map recovers the label exactly. From φ(r), every 1×1 stitcher
gives position (0, 0) a channel map of the activations from φ⁻¹(0, 0), which
are independent of the label, so no map in the class does better than
chance. Equivalent representations get different penalties.
