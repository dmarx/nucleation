---
number: 81
status: Open
formerly:
- LEAD-tmpdqp3c
title: 'Run the discriminating experiment on governance-induced frustration: intervene on the allocation of influence while search and information stay fixed, with declared demands and a feasible-update oracle'
version: 1
stage: specified
priority: high
method:
- empirical
- formal
tags:
- self-governance
- agency
date: '2026-11-19'
line:
- distributed-agency
- will-organization
advances:
- CLAIM-500
- CLAIM-357
operationalized_in:
- CASE-099
summary: >-
  The only named test of the governance-induced kind of frustration; A39
  called it the best candidate for an early discriminating experiment.
  Named in [CLAIM-500](../claims.d/CLAIM-500.md) and [CLAIM-357](../claims.d/CLAIM-357.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpgustv, CLAIM-tmpifr7i — Proposed or new; cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-500 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-081: Run the discriminating experiment on governance-induced frustration: intervene on the allocation of influence while search and information stay fixed, with declared demands and a feasible-update oracle

## What it would do

Build [CASE-099](../cases.d/CASE-099.md) with declared demands and an oracle for feasible updates,
then vary only how influence is allocated among the components.

Where the record names it:

- [CLAIM-500](../claims.d/CLAIM-500.md): "The discriminating experiment of the note of 2026-10-30 is
  still unrun: [CASE-099](../cases.d/CASE-099.md) with declared demands and a feasible-update oracle,
  intervening on the allocation of influence with search and information
  held fixed."
- [CLAIM-357](../claims.d/CLAIM-357.md): "A39's case study 2, [CASE-099](../cases.d/CASE-099.md) with demands and a
  feasible-update oracle, would test it"

## What would count

Frustration that changes with the allocation of influence while search and
information are fixed supports [CLAIM-500](../claims.d/CLAIM-500.md) and [CLAIM-357](../claims.d/CLAIM-357.md). Frustration that
tracks search or information alone defeats the governance-induced reading.

## Note of 2026-11-22: what was done, and what remains

Done: CASE-099 was built with declared demands, a feasible-update oracle (exact Φ_r, checked against CLAIM-365's dual) and an allocation oracle. Only the conferral rule was varied, with the update map (search) and the gradients (information) the same under every rule. The study ran on 200 paired satisfiable instances and 100 structural ones, with optimizer and information controls, a sweep of the conferral parameters, and the best fixed weighting in hindsight. It is filed as CASE-tmpgustv with CLAIM-tmpifr7i. The code is under scratch/studies/lead-081/.

Result against "what would count": frustration changed with the allocation while search and information were fixed, 0.95 under Regime A against 0.05 under Regime B. It did not track step size, noise or conditioning alone. Noise raised it under every rule, but the gap between the rules survived. That is the shape that supports CLAIM-500 and CLAIM-357. However, a fixed weighting chosen in hindsight did as well as Regime B, and CLAIM-500's defeater counts a fixed weighting rule as an optimizer mechanism. Whether the result supports CLAIM-500 is filed as two readings in CLAIM-tmpifr7i for the owner.

Remains:
- Another update map (search).
- More demands and dimensions.
- QUESTION-124's persistence condition stated in the parameters, and a non-Euclidean (modular) geometry.
- A non-local oracle, since the one-step oracle misclassified the structural instances under capture.

Status and stage are the owner's.
