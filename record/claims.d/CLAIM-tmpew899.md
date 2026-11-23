---
status: Proposed
title: 'A function-preserving rescaling before fine-tuning is a change of the fine-tuning procedure and not of the learner, since gradient descent on the rescaled weights is gradient descent on the original weights with changed step sizes; so Lippl and Lindsey''s case shows one learner whose developmental frontier depends on the procedure admitted, not two learners of equal present capability whose developmental frontiers differ'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23, as the objection to the verdict
    that run leans to, and the alternative reading of the same check.
role: counter
warrant: interpretive
defeated_if: >-
  A showing that the scale of a network's weights is retained state that
  fine-tuning procedures in use do not fix by choice of coordinates, for
  instance that two networks reached by different training histories,
  not by a rescaling applied at the start of fine-tuning, compute the same
  function and still learn differently under one fixed procedure.
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
objects_to:
- CLAIM-tmp2tjpt
rests_on:
- CLAIM-tmp2k67n
- CLAIM-tmp7n00e
bears_on:
- QUESTION-495
summary: >-
  The objection, and the alternative reading of the check the lead run of
  2026-11-23 made. By [CLAIM-tmp2k67n](CLAIM-tmp2k67n.md)'s identity, gradient descent on the
  weights rescaled by c is gradient descent on the original weights with
  step sizes divided by c² on the first layer and multiplied by c² on the
  readout. Lippl and Lindsey themselves present the rescaling as a
  technique applied "following pretraining", part of how one fine-tunes.
  Read so, the case shows [CLAIM-754](CLAIM-754.md)'s indexing of the developmental
  frontier by the admissible procedure, which is not in dispute, and not
  that equal operational frontiers leave different developmental ones.
  The assistant does not lean to it, and says why in [CLAIM-tmp2tjpt](CLAIM-tmp2tjpt.md). The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2tjpt CLAIM-tmp7n00e CLAIM-754 CLAIM-tmp2k67n THEORY-tmpfysqg THEORY-2077 — Proposed; the verdict this objects to, the claims it rests on, the claim the dispute concerns, and the readings it cites -->

# CLAIM-tmpew899: A function-preserving rescaling before fine-tuning is a change of the fine-tuning procedure and not of the learner, since gradient descent on the rescaled weights is gradient descent on the original weights with changed step sizes; so Lippl and Lindsey's case shows one learner whose developmental frontier depends on the procedure admitted, not two learners of equal present capability whose developmental frontiers differ

## The objection

[CLAIM-tmp2tjpt](CLAIM-tmp2tjpt.md) reads [CLAIM-tmp7n00e](CLAIM-tmp7n00e.md)'s pair as two learners with one
function. But the second member exists only because the first was
rescaled at the start of fine-tuning, and [CLAIM-tmp2k67n](CLAIM-tmp2k67n.md) shows that this
step and a change of per-coordinate step sizes are one thing written in
two coordinate systems. Nothing the network computes separates them. In
Lippl and Lindsey's paper the rescaling is offered as "a technique –
weight rescaling following pretraining", a way of fine-tuning, and its
deep-network gains are reported as gains of a method ([THEORY-tmpfysqg](../theory.d/THEORY-tmpfysqg.md)).

So the honest bookkeeping keeps the learner fixed, the pretrained network
with its function, and varies the procedure: plain fine-tuning against
fine-tuning preconditioned by c. That is an instance of what [CLAIM-754](CLAIM-754.md)
already says in its last section, that the developmental frontier is a
family indexed by admissible procedures. It is not an instance of its
divergence clause, which needs learners that differ in what they have
retained.

## What would answer it

A pair whose difference in scale was produced by different training
histories, not inserted at fine-tuning time: two pretraining runs that
end at the same function with a different balance between the layers,
which Anguita and colleagues' relative scale at initialization provides
in theory ([THEORY-2077](../theory.d/THEORY-2077.md)). There the scale is the residue of a history,
and the objection's re-description would have to call the history
itself a choice of procedure.
