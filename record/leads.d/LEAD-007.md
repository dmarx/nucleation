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
<!-- inactive-ok-file: THEORY-2305 THEORY-2290 CLAIM-1043 CLAIM-1013 CLAIM-1089 ARG-223 CASE-407 CLAIM-754 CLAIM-1011 THEORY-2077 — Proposed or new; filed or cited by the lead run of 2026-11-23 -->

Lippl and Lindsey registered ([LIT-3172](../literature.d/LIT-3172.md)) and read from the arXiv HTML
of v4 ([NOTE-2415](../notes.d/NOTE-2415.md), Read), with two accounts: [THEORY-2305](../theory.d/THEORY-2305.md), the
shallow-network theory that Anguita and colleagues ([THEORY-2077](../theory.d/THEORY-2077.md)) extend,
and [THEORY-2290](../theory.d/THEORY-2290.md), the deep-network results.

The check. The paper never compares networks with the same function, but
its rescaling after pretraining, with the auxiliary readout compensated,
gives one: same pretrained function and same readout-only reach, different
full fine-tuning, and the better rescaling reverses with the main task
([CLAIM-1043](../claims.d/CLAIM-1043.md), demonstrated; run over 40 seeds in [CASE-407](../cases.d/CASE-407.md)). It acts
on any converged network, not on a chosen initialization. Whether this is
two learners with equal present capability and different later learning
([CLAIM-1013](../claims.d/CLAIM-1013.md), the assistant's lean, supporting [CLAIM-754](../claims.d/CLAIM-754.md) through
[ARG-223](../arguments.d/ARG-223.md)) or one learner under two procedures, because the rescaling
is a change of step sizes ([CLAIM-1011](../claims.d/CLAIM-1011.md)), is filed as the objection
[CLAIM-1089](../claims.d/CLAIM-1089.md). That choice is the owner's. Nothing here bears on the
frontiers moving in opposite directions over training. Status and stage
left for the owner.
