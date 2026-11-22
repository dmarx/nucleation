---
number: 16
status: Open
formerly:
- LEAD-tmp0fbe3
title: 'Run emergent specialization in a population of identical adaptive operators, holding the final diversity fixed while changing the mechanism that produced it'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: a reduced run of CASE-117 was carried
    out (CASE-tmpnti0m, CLAIM-tmp1u4m3, CLAIM-tmp1jz5w). Status and
    stage are unchanged; marking the lead Done is the owner's call.
stage: specified
priority: high
method:
- empirical
tags:
- complex-systems
- self-governance
- ecology
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-132
- QUESTION-133
- QUESTION-134
- QUESTION-135
- QUESTION-125
- QUESTION-083
operationalized_in:
- CASE-117
- CASE-tmpnti0m
summary: >-
  One study bears on six open questions. Named in [CASE-117](../cases.d/CASE-117.md), [QUESTION-133](../questions.d/QUESTION-133.md)
  and [QUESTION-134](../questions.d/QUESTION-134.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpnti0m CLAIM-tmp1u4m3 CLAIM-tmp1jz5w — Proposed, filed 2026-11-22 by LEAD-016's study and cited in the note of that date -->

# LEAD-016: Run emergent specialization in a population of identical adaptive operators, holding the final diversity fixed while changing the mechanism that produced it

## What it would do

Run [CASE-117](../cases.d/CASE-117.md), and within it the experiment [QUESTION-134](../questions.d/QUESTION-134.md) asks for,
separating loss of influence, loss of competence and loss of access.

Where the record names it:

- [CASE-117](../cases.d/CASE-117.md): "The decisive comparison holds the final diversity of operator
  usage roughly fixed while changing the mechanism that produced it."
- [QUESTION-133](../questions.d/QUESTION-133.md): "[CASE-117](../cases.d/CASE-117.md) is the study that would test it"
- [QUESTION-134](../questions.d/QUESTION-134.md): "An experiment separating three things:"

## What would count

Specialists that recover when rare and refill after removal under one
mechanism and not another answer [QUESTION-132](../questions.d/QUESTION-132.md) and [QUESTION-133](../questions.d/QUESTION-133.md) for the
simulation. [CASE-117](../cases.d/CASE-117.md) warns that a positive result does not show
self-constitution ([CLAIM-288](../claims.d/CLAIM-288.md)).

## Note of 2026-11-22: a reduced run, and what remains

A reduced version of CASE-117 was run on a CPU and filed as
CASE-tmpnti0m. It used four contexts, one of them rare, and linear
operators that differ only by initialization. Four influence rules were
compared: ordinary mixture-of-experts gating (the baseline), gating with a
load-balancing loss, gating with a usage bias, and a multiplicative
contribution rule. Each ran with no spare operator (K = 4) and with two
spare (K = 6), in 6 seeds, with eleven test arms.

**What the lead's criterion finds.** Specialists "recover when rare and
refill after removal under one mechanism and not another", but the
mechanism that decides is not the influence rule alone.

- **Recovery when rare, at matched participation (K = 4).** Every rule
  recovers a rare specialist from 10⁻³. Only the multiplicative rule and
  the usage bias recover it from 10⁻⁵. The multiplicative rule's rate
  does not depend on the starting share. The gating rules' rate falls
  with it, for the reason CLAIM-tmp1u4m3 derives. The usage bias also
  lifts an incompetent copy.
- **Refill after removal.** It depends on spare capacity, not on the
  rule. A spare refilled the niche in 6 of 6 seeds under every rule at
  K = 6, and nothing refilled it at K = 4.
- **QUESTION-134's experiment.** With spare capacity, a suppressed
  specialist is shut out whether or not it kept its competence. Without
  it, the specialist returns even after losing most of its competence
  (CLAIM-tmp1jz5w).

**What remains of the lead:**

- the CASE-117 conditions not run: learned features, historical-grant
  influence, an authority-update rule the organization revises, abrupt
  shifts and recurring dormancy, internally maintained exploration;
- the compatibility-complex measurement for QUESTION-133;
- any parameter sweep for QUESTION-125;
- 12 seeds rather than 6, and longer windows for the slow recoveries;
- a marginalization the population produces itself, rather than a clamp.

The lead's status and stage are left for the owner.
