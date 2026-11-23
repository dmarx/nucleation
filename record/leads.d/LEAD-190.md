---
number: 190
status: Open
formerly:
- LEAD-tmpy1k4c
title: 'Simulate the population comparisons the authority-grant claims name: role-indexed against scalar grants, and operators bound by the two grant conditions'
version: 1
stage: specified
priority: medium
method:
- formal
tags:
- self-governance
- social-ontology
date: '2026-11-19'
line:
- distributed-agency
advances:
- CLAIM-281
- CLAIM-285
operationalized_in:
- CASE-092
presupposes:
- LEAD-090
summary: >-
  Two Proposed claims name this comparison as their test. Named in
  [CLAIM-281](../claims.d/CLAIM-281.md) and [CLAIM-285](../claims.d/CLAIM-285.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-363 — Proposed; the built model the run extends, cited as open -->
<!-- inactive-ok-file: CASE-tmpw3vii CLAIM-tmp5wozo CLAIM-tmppm30v CLAIM-tmpdpnid CLAIM-tmpoc6mo — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-281 CLAIM-285 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-190: Simulate the population comparisons the authority-grant claims name: role-indexed against scalar grants, and operators bound by the two grant conditions

## What it would do

In the built model, compare populations with role-indexed grants against
scalar ones, and populations whose operators are bound by the two grant
conditions against unbound ones, recording to whom they delegate beyond
one hop.

Where the record names it:

- [CLAIM-281](../claims.d/CLAIM-281.md): "The population comparison [CASE-092](../cases.d/CASE-092.md) names, role-indexed
  against scalar grants, has still not been run"
- [CLAIM-285](../claims.d/CLAIM-285.md): "Still missing: a population model in which operators bound
  by the two conditions delegate, and delegate to aligned others rather than
  at random."

## What would count

Factions or retained disagreement under role-indexed grants and not under
scalar ones supports [CLAIM-281](../claims.d/CLAIM-281.md); delegation to aligned others beyond chance
supports [CLAIM-285](../claims.d/CLAIM-285.md). Their absence defeats each as stated.

## Note of 2026-11-23: run

Both comparisons were run as [CASE-tmpw3vii](../cases.d/CASE-tmpw3vii.md), in a population of 20 operators built on [CASE-363](../cases.d/CASE-363.md)'s model. That model's code was loaded by path and not modified (scratch/studies/lead-190/).

- **Role-indexed against scalar grants** ([CLAIM-tmp5wozo](../claims.d/CLAIM-tmp5wozo.md)). Role indexing with the critic role scored by observed relevance left no belief factions and no capture. Scalar grants failed one way or the other: scored by agreement they captured the population or split it into factions, and moved by the reward for realized policy they split it into factions that read only their own side. Role indexing whose critic row is scored by agreement was identical to the scalar scheme. The condition is a closed-form threshold on how far the critic score reads agreement. The cost is [CLAIM-tmppm30v](../claims.d/CLAIM-tmppm30v.md): the shared meaning then follows where competence sits.
- **Bound against unbound operators** ([CLAIM-tmpdpnid](../claims.d/CLAIM-tmpdpnid.md)). Bound operators delegated their whole budget, all of it to their own side, against a chance share of 0.47. Under leave-one-out delegation, the 43% of their authority that travelled two hops or more stayed on their side, and none returned to them. Unbound operators aligned at about chance and recycled 0.15 of a unit each. Within their side, bound operators delegated to its extremes, not its nearest members ([CLAIM-tmpoc6mo](../claims.d/CLAIM-tmpoc6mo.md)).

What remains for the owner:

- The readings set out in [CLAIM-tmp5wozo](../claims.d/CLAIM-tmp5wozo.md) (whether [CLAIM-281](../claims.d/CLAIM-281.md)'s role indexing includes a role-specific score) and in [CLAIM-tmpoc6mo](../claims.d/CLAIM-tmpoc6mo.md) (what "aligned" means in [CLAIM-285](../claims.d/CLAIM-285.md)).
- The statuses of the entries filed and of [CLAIM-281](../claims.d/CLAIM-281.md) and [CLAIM-285](../claims.d/CLAIM-285.md).
- Whether this lead is done. Its stage and status are unchanged.

Not run: decision rules other than the weighted mean, unbalanced populations, coalitions, relevance observed with error or correlated with side, and more than two roles.
