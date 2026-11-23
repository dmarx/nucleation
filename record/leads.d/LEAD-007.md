---
number: 7
status: Open
formerly:
- LEAD-tmpio3p6
title: 'Read Lippl and Lindsey on regimes of feature reuse in multi-task learning and fine-tuning, the direct precursor of Anguita and colleagues'
version: 1
stage: idea
method:
- reading
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-754
summary: >-
  Named by the reading of Anguita and colleagues ([NOTE-2159](../notes.d/NOTE-2159.md)) as the
  work their theory extends; not held.
---

# LEAD-007: Read Lippl and Lindsey on regimes of feature reuse in multi-task learning and fine-tuning, the direct precursor of Anguita and colleagues

## What it would do

Register and read Lippl and Lindsey (2024); check whether their regimes
already show the same present capability with different later learning,
outside the special initialization Anguita and colleagues generalize.

## Note of 2026-11-23: carried out by the lead run of that date
<!-- inactive-ok-file: THEORY-tmpw69kb THEORY-tmpfysqg CLAIM-tmp7n00e CLAIM-tmp2tjpt CLAIM-tmpew899 ARG-tmpbvq7y CASE-tmpjn7jc CLAIM-754 CLAIM-tmp2k67n THEORY-2077 — Proposed or new; filed or cited by the lead run of 2026-11-23 -->

Lippl and Lindsey registered (LIT-tmpkuq67) and read from the arXiv HTML
of v4 (NOTE-tmpw2i45, Read), with two accounts: THEORY-tmpw69kb, the
shallow-network theory that Anguita and colleagues (THEORY-2077) extend,
and THEORY-tmpfysqg, the deep-network results.

The check. The paper never compares networks with the same function, but
its rescaling after pretraining, with the auxiliary readout compensated,
gives one: same pretrained function and same readout-only reach, different
full fine-tuning, and the better rescaling reverses with the main task
(CLAIM-tmp7n00e, demonstrated; run over 40 seeds in CASE-tmpjn7jc). It acts
on any converged network, not on a chosen initialization. Whether this is
two learners with equal present capability and different later learning
(CLAIM-tmp2tjpt, the assistant's lean, supporting CLAIM-754 through
ARG-tmpbvq7y) or one learner under two procedures, because the rescaling
is a change of step sizes (CLAIM-tmp2k67n), is filed as the objection
CLAIM-tmpew899. That choice is the owner's. Nothing here bears on the
frontiers moving in opposite directions over training. Status and stage
left for the owner.
