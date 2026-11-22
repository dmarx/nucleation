---
number: 59
status: Open
formerly:
- LEAD-tmpa2mqc
title: 'File the demonstrated corollary that answers part of the question on reinforcing loops'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- information-geometry
- loss-landscapes
date: '2026-11-19'
line:
- learned-structure
- formal-apparatus
advances:
- QUESTION-127
- CLAIM-366
summary: >-
  Named in the curation entry of 2026-11-07 (082259). Filed by the backlog
  audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-555 — Proposed; named among what remains of QUESTION-127 -->

# LEAD-059: File the demonstrated corollary that answers part of the question on reinforcing loops

## What it would do

Write the corollary as a demonstrated claim.

Where the record names it:

- The curation entry of 2026-11-07 (082259): "answering part of
  [QUESTION-127](../questions.d/QUESTION-127.md)"

## What would count

Filing it answers part of [QUESTION-127](../questions.d/QUESTION-127.md).

## Note of 2026-11-22: already held, by [CLAIM-629](../claims.d/CLAIM-629.md)

A lead worker took this lead up and found that the corollary it names is
already on the record. The curation entry of 2026-11-07 (082259) lists it
among "By-products, not filed": "Common descent is constant on the orbits
of every function-preserving symmetry that is a diffeomorphism of the
parameters. A test with a fixed Euclidean budget is not: with f =
v·relu(ux) and a rescaling by one half, the squared gradient norm is 612
at (4, 1) and 288 at its image (2, 2)". The same review did file it, as
[CLAIM-629](../claims.d/CLAIM-629.md) (dated 2026-11-07, demonstrated, resting on [CLAIM-366](../claims.d/CLAIM-366.md) and
[CLAIM-365](../claims.d/CLAIM-365.md)), and the status review of 2026-11-20 made it Active and split
the part of [QUESTION-127](../questions.d/QUESTION-127.md) it answers off as [QUESTION-499](../questions.d/QUESTION-499.md), now Answered.
The backlog audit of 2026-11-19 read the curation entry's "not filed"
and did not see that.

- **No new claim filed.** Under [ADR-072](../decisions.d/ADR-072.md) an idea gets a code when the
  record does not already hold it; a second code would duplicate
  [CLAIM-629](../claims.d/CLAIM-629.md), whose statement, proof and example are the corollary's.
- **The checks re-run on 2026-11-22, unchanged.** In
  scratch/formal/orbit_descent_check.py the chain rule holds, common
  descent agrees on all 300 rescalings and swaps, and the Euclidean Φ_r
  differs on 192 of the rescalings and none of the swaps. In
  scratch/formal/claim629_orbit_controls.py both verdicts occur (292 and
  108 of 400 points) and both controls fire (16 and 101 mismatches). By
  hand: with x = y = 1 the gradient is (6, 24) at (4, 1) and (12, 12) at
  (2, 2), squared norms 612 and 288, and diag(½, 2)ᵀ(12, 12) = (6, 24), as
  the chain rule requires.
- **The title is mislabelled.** [QUESTION-127](../questions.d/QUESTION-127.md) is about which frustration
  diagnoses survive function-preserving symmetries and trajectories, not
  about reinforcing loops.
- **What remains of [QUESTION-127](../questions.d/QUESTION-127.md)** is not this lead's: symmetries that are
  not diffeomorphisms ([CLAIM-305](../claims.d/CLAIM-305.md)), the compatibility complex ([CLAIM-555](../claims.d/CLAIM-555.md)),
  governance regret, modular localization, and trajectories.

Nothing remains of this lead. Marking it Done, and whether to retitle it,
is the owner's call.
