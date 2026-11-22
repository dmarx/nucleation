---
number: 40
status: Open
formerly:
- LEAD-tmp49pn2
title: 'Train small recurrent networks with a Z2 symmetry on a boundary-dependent task, compute the four candidate partitions of the hidden field, and move walls by intervention'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- representation-learning
- complex-systems
date: '2026-11-19'
line:
- learned-structure
- distributed-agency
advances:
- QUESTION-491
summary: >-
  Named in [QUESTION-491](../questions.d/QUESTION-491.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-040: Train small recurrent networks with a Z2 symmetry on a boundary-dependent task, compute the four candidate partitions of the hidden field, and move walls by intervention

## What it would do

Run A15's Experiment B as refined by the readings of 2026-11-19.

Where the record names it:

- [QUESTION-491](../questions.d/QUESTION-491.md): "A family of small recurrent networks with a Z2 symmetry,
  trained on a task whose answer depends on boundaries in the input"

## What would count

Partitions that agree, and walls whose movement changes the answer, answer
[QUESTION-491](../questions.d/QUESTION-491.md).

## Note of 2026-11-22: carried out in part
<!-- inactive-ok-file: CASE-tmp2e2a5 CLAIM-tmpwx1cm — new; filed by this lead on 2026-11-22 -->

Done by a delegated worker on branch claude/lead-040-z2-rnns; code, results and a rerun README are in scratch/studies/lead-040/. Six trained networks and four frozen controls; the four partitions compared on four time slices; walls moved by interchange; a closed pair compared with a boundary-forced wall. Filed as [CASE-tmp2e2a5](../cases.d/CASE-tmp2e2a5.md) and [CLAIM-tmpwx1cm](../claims.d/CLAIM-tmpwx1cm.md). What remains: two-dimensional lattices, where a closed wall can shrink by itself; boundary conditions as hard constraints; a sweep of the partition thresholds; more seeds (one of six networks learned an oscillating phase); and A15's Experiment E. Whether this suffices to mark the lead Done is the owner's call.
