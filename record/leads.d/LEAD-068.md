---
number: 68
status: Open
formerly:
- LEAD-tmpb8gee
title: 'Compare two arrangements whose overseer has the same authority and resources and that differ only in how fast the acting institution can act'
version: 1
stage: specified
priority: high
method:
- empirical
- historical
tags:
- society-and-governance
- philosophy-of-technology
date: '2026-11-19'
line:
- distributed-agency
advances:
- CLAIM-464
- CLAIM-731
- CLAIM-706
- CLAIM-710
- CLAIM-730
- CLAIM-462
- QUESTION-278
operationalized_in:
- CASE-285
summary: >-
  The cleanest test of the owner's U11 ([CLAIM-710](../claims.d/CLAIM-710.md)); several claims depend
  on it. Named in [CLAIM-464](../claims.d/CLAIM-464.md) and [CASE-285](../cases.d/CASE-285.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-285 CLAIM-710 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-068: Compare two arrangements whose overseer has the same authority and resources and that differ only in how fast the acting institution can act

## What it would do

Run [CASE-285](../cases.d/CASE-285.md), by simulation or by matched historical pairs: the same
oversight, the acting institution's speed varied.

Where the record names it:

- [CLAIM-464](../claims.d/CLAIM-464.md): "A study that varies only an acting institution's speed is
  proposed as [CASE-285](../cases.d/CASE-285.md)"
- [CASE-285](../cases.d/CASE-285.md): "the cleanest test of the owner's U11"

## What would count

Oversight that loses effect as speed rises, with authority and resources
fixed, supports [CLAIM-710](../claims.d/CLAIM-710.md) and [CLAIM-464](../claims.d/CLAIM-464.md); no effect of speed defeats them.

## Note of 2026-11-22: the simulation arm run
<!-- inactive-ok-file: CASE-316 CLAIM-879 — new; the executed study and claim of LEAD-068, filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-730 — Proposed; cited in the note of 2026-11-22 on LEAD-068's simulation -->

The simulation arm is built and run: [CASE-316](../cases.d/CASE-316.md), with code, tests and results under scratch/studies/lead-068/. A queueing model holds the overseer's authority (an objection suspends), information (detection delay) and resources (four reviewers) fixed, and varies only how soon the acting institution's actions become irreversible; precommitted limits, automatic suspension and pauses are added in turn in the fast arm. 20 seeds per configuration.

- **What would count, met in the model.** Oversight lost effect as speed rose with authority and resources fixed: the share of objectionable actions stopped in time fell from 0.994 to 0.396 at ten times the speed, and to 0.043 when speed also multiplied the volume of actions. That is the lead's support for [CLAIM-710](../claims.d/CLAIM-710.md) and [CLAIM-464](../claims.d/CLAIM-464.md), in stipulated form: the model builds in A23 §3's timing condition, so the runs add the loss's shape and the remedies' comparison, not evidence about institutions.
- **The remedies.** Limits won back their coverage of the gap, suspension at most the share detected in time, pauses only by giving up the speed, and nothing under the volume reading. [CLAIM-879](../claims.d/CLAIM-879.md) states it.
- **A choice the design left open, run both ways.** Whether "speed" shortens only the time to irreversibility or also raises the volume of actions; both readings are reported, neither chosen.

What remains:

- the historical arm, matched pairs of real arrangements, not attempted;
- an affected party and revisable limits, which [CLAIM-730](../claims.d/CLAIM-730.md)'s first clause needs and the model lacks.

The lead stays Open.
