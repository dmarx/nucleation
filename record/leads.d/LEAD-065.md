---
number: 65
status: Open
formerly:
- LEAD-tmpaxs5j
title: 'Remove core units from Ito and Kaneko''s core-periphery system and see whether the periphery refills the core'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: the removal study was run (CASE-tmpvn7wm,
    CLAIM-tmpf11gs). Status and stage are unchanged; marking the lead
    Done is the owner's call.
stage: idea
priority: high
method:
- empirical
tags:
- complex-systems
- ecology
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-132
operationalized_in:
- CASE-tmpvn7wm
summary: >-
  The record calls it the cheap decision of whether a held case shows
  recovery when rare. Named in [QUESTION-132](../questions.d/QUESTION-132.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpvn7wm CLAIM-tmpf11gs — Proposed, filed 2026-11-22 by LEAD-065's study and cited in the note of that date -->

# LEAD-065: Remove core units from Ito and Kaneko's core-periphery system and see whether the periphery refills the core

## What it would do

Reimplement Ito and Kaneko's coupled-map system, remove core units, and
measure whether peripheral units move into the core.

Where the record names it:

- [QUESTION-132](../questions.d/QUESTION-132.md): "Removing core units and seeing whether the periphery
  refills the core would decide it cheaply."

## What would count

Refilling classes the system as one whose differentiation recovers when
rare, a case for [QUESTION-132](../questions.d/QUESTION-132.md); no refilling classes it as a frozen
arrangement.

## Note of 2026-11-22: run

The model was reimplemented from NOTE-1414's equations, checked against
arXiv's v1. The removal study was run on 12 seeds at the paper's
parameter point, with code, tests and results under
`scratch/studies/lead-065/`. It is filed as CASE-tmpvn7wm, with the claim
CLAIM-tmpf11gs.

The periphery refills the core in every seed. With the core deleted, a
new core of 17.2 ± 0.8 units forms from former periphery units within
10⁶ steps. A same-sized network that lost periphery instead has one of
17.0 ± 1.1, and the new core has the original's one-way structure.
Half a core removed is made up from the periphery. A core cut to 10⁻³ of
its influence is regained by its own members, who make up 92% of the
core 10⁶ steps later.

By this lead's criterion, the system is one whose differentiation
recovers when rare, not a frozen arrangement. The claim files two
readings of what that means for QUESTION-132, for the owner to choose
between: the first outcome at the level of roles, or a fourth outcome,
role regeneration by interchangeable holders.

**What remains:**

- other parameter points in the desynchronized phase, other N and δ;
- recovery of a periphery unit made rare.

The lead's status and stage are left for the owner.
