---
number: 105
status: Open
formerly:
- LEAD-tmpi9mte
title: 'Run the crossed intervention on a conventionally trained network: change the optimizer with the network fixed, and disrupt a learned state with the optimizer fixed'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- agency
- learning-theory
date: '2026-11-19'
line:
- learned-structure
- distributed-agency
advances:
- CLAIM-367
operationalized_in:
- CASE-tmphp4pt
summary: >-
  Named in [CLAIM-367](../claims.d/CLAIM-367.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-367 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-105: Run the crossed intervention on a conventionally trained network: change the optimizer with the network fixed, and disrupt a learned state with the optimizer fixed

## What it would do

Run both interventions on one trained network.

Where the record names it:

- [CLAIM-367](../claims.d/CLAIM-367.md): "crossed intervention coming out the other way on a
  conventionally trained network"

## What would count

The outcome is [CLAIM-367](../claims.d/CLAIM-367.md)'s defeat condition.

## Note of 2026-11-23: carried out on one small network

<!-- inactive-ok-file: CASE-tmphp4pt CLAIM-tmp60fme CLAIM-tmpmgb7l CLAIM-tmpyf8s0 CLAIM-tmp2k67n — new; filed by the lead run of 2026-11-23 -->

Done on 2026-11-23 (scratch/studies/lead-105/, eight tests): both
interventions, crossed, on a width-32 two-layer ReLU network trained
conventionally on two tasks with a task-identity input, by heavy ball or by
Adam, twelve seeds each, against a conflicting demand (task B's target
turned against task A's). Study: CASE-tmphp4pt.

The optimizer arm was not null. With the parameters fixed and each
optimizer at matched pace, the probe optimizer changed how much of A was
lost by −39% to +147%, and so did Adam's carried state. The learned-state
arm was not null either: re-initializing and healing the most
task-selective units raised the loss, and random units of equal number did
so less (CLAIM-tmp60fme). So CLAIM-367's defeat condition is not met.
Two readings of what the run does to CLAIM-367 are filed as alternatives:
CLAIM-tmpmgb7l, that it corroborates the claim (the assistant's lean),
and CLAIM-tmpyf8s0, that the shares, set by the training optimizer,
count against its "most". A function-preserving rescaling, run as a
disruption, turned out to be an optimizer change in other coordinates
(CLAIM-tmp2k67n).

What remains: a larger network, stochastic batches, and a conflict that
persists; a disruption aimed at a representation the network uses to
regulate updates, which needs CASE-113's System B or C built; and a
disruption control matched on activity as well as on number.
