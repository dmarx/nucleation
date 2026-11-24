---
number: 1013
status: Proposed
formerly:
- CLAIM-tmp2tjpt
title: 'For a network trained by gradient descent, how its parameters are scaled belongs to the organization it has acquired: two networks computing the same function, and alike in what a linear readout can reach from them, can differ in what fine-tuning makes them learn, so the function a learner computes now does not fix what it can come to learn'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as the verdict on the check that
    lead asks for, and the reading of it the assistant leans to.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the scale of a trained network's parameters is not part
  of what the network retains, for instance that every acquisition
  procedure a declared interface admits for such networks is invariant to
  the rescaling symmetries of the network, so that function-equivalent
  networks always learn alike; or that the networks of CLAIM-1043 do
  not compute the same function or do not learn differently.
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
rests_on:
- CLAIM-1043
corroborates:
- CLAIM-754
bears_on:
- QUESTION-495
summary: >-
  The verdict on the check the lead run of 2026-11-23 was asked to make:
  whether Lippl and Lindsey's regimes already show the same present
  capability with different later learning, outside the initialization
  Anguita and colleagues generalize. Read this way, yes. A pretrained
  network and its compensated rescaling are two learners with one
  function and different developmental frontiers under the same
  procedure, gradient descent in the network's own parameters, and which
  is better placed depends on the declared later task ([CLAIM-1043](CLAIM-1043.md)).
  The rival reading, that they are one learner under two procedures, is
  [CLAIM-1089](CLAIM-1089.md); the assistant leans to this one. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1043 CLAIM-1089 CLAIM-754 CLAIM-1011 THEORY-2077 THEORY-2305 — Proposed; the claims filed by the lead run of 2026-11-23, the claim the verdict bears on, and the readings it is set against -->

# CLAIM-1013: For a network trained by gradient descent, how its parameters are scaled belongs to the organization it has acquired: two networks computing the same function, and alike in what a linear readout can reach from them, can differ in what fine-tuning makes them learn, so the function a learner computes now does not fix what it can come to learn

## The claim

[CLAIM-754](CLAIM-754.md) counts three frontiers fixed by a learner's acquired
organization M, and says the operational one (what it can do now) does
not fix the developmental one (what it can come to do within an
acquisition budget, given an admissible procedure). [CLAIM-1043](CLAIM-1043.md) gives
two diagonal linear networks, pretrained alike, that compute the same
function and reach the same functions when only their readout is
trained, and that full fine-tuning, the same procedure in each one's own
parameters, sends to different solutions; on one declared later task the
first generalizes better, on another the second.

Taking M to be what a trained network retains, its weights, these are
two learners with one operational frontier and two developmental
frontiers. The difference the function cannot register is the balance
of scale between the layers, which Lippl and Lindsey ([THEORY-2305](../theory.d/THEORY-2305.md))
reach by rescaling after pretraining and Anguita and colleagues
([THEORY-2077](../theory.d/THEORY-2077.md)) by the relative scale at initialization. So the case is
not tied to Anguita and colleagues' initialization: any converged network
of this kind has a whole orbit of function-equivalent rescalings, with
different later learning.

It also shows the indexing by procedure that [CLAIM-754](CLAIM-754.md)'s last section
names. Under readout-only training the two learners' developmental
frontiers coincide; under full fine-tuning they part.

## Why it is read this way

Gradient descent is applied to a network's parameters, in the
coordinates the network has. The learner that arrives at fine-tuning is
its weight vector; nothing else is carried forward. That a change of
coordinates would turn the rescaling into a change of step sizes
([CLAIM-1011](CLAIM-1011.md)) is true. But that identity holds for any two weight
vectors joined by a symmetry, and it does not make the learner's own
state a property of the optimizer.

## The stronger reading it invites and does not support

That present function never fixes later learning for any learner. A
learner whose acquisition procedure is invariant to its reparameterizations
(natural-gradient methods aim at this) would not show the effect, and
[CLAIM-1089](CLAIM-1089.md) presses that point.
