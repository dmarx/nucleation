---
number: 12
status: Open
formerly:
- LEAD-tmpyaeh1
title: 'Run the Pythia study: measure across checkpoints whether the cost of acquiring held-out task families rises while the pretraining objective improves, with forgetting measured and the secondary arms added only after the primary contrast'
version: 1
stage: specified
method:
- empirical
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-758
- CLAIM-757
- CLAIM-754
operationalized_in:
- CASE-294
presupposes:
- LEAD-010
summary: >-
  [CASE-294](../cases.d/CASE-294.md)'s study proper, once its calibration pilot is done: the
  record's main test of overconsolidation and of the deadline claim's two
  branches.
---
<!-- inactive-ok-file: CASE-294 CLAIM-757 CLAIM-758 — Proposed or newly filed; cited in this filing of 2026-11-19 -->

# LEAD-012: Run the Pythia study: measure across checkpoints whether the cost of acquiring held-out task families rises while the pretraining objective improves, with forgetting measured and the secondary arms added only after the primary contrast

## What would be done

[CASE-294](../cases.d/CASE-294.md)'s primary estimand across checkpoints, with held capabilities
measured so that forgetting counts as cost ([CLAIM-758](../claims.d/CLAIM-758.md), version 2); then,
only if a developmental difference appears, the secondary arms
(in-context learning, test-time training, adapters, resets, renewed
practice) that tell its readings apart.

## What would count

For [CLAIM-758](../claims.d/CLAIM-758.md): acquisition cost under the floor on held capabilities
rising with training time while the pretraining loss falls. Against it:
cost flat or falling. For [CLAIM-757](../claims.d/CLAIM-757.md): practice failing throughout and
resets working throughout fits depletion; practice failing only after a
point fits decay with disuse.

## Cost

Tens to hundreds of fine-tuning runs; moderate. Presupposes the pilot
([LEAD-010](LEAD-010.md)).
