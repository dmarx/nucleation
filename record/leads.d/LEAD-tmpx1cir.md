---
status: Open
title: 'Calibrate the Pythia study: pilot two task families on four checkpoints of one model and confirm that each family is learnable and that adaptation cost is measurable before any arm is added'
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
operationalized_in:
- CASE-294
summary: >-
  The first step of [CASE-294](../cases.d/CASE-294.md), as ChatGPT's review set it: four checkpoints
  of Pythia-70M-deduped, two synthetic task families, three seeds, the
  primary estimand the minimum adaptation budget to a reliability
  threshold.
---
<!-- inactive-ok-file: CASE-294 CLAIM-758 — Proposed or newly filed; cited in this filing of 2026-11-19 -->

# LEAD-tmpx1cir: Calibrate the Pythia study: pilot two task families on four checkpoints of one model and confirm that each family is learnable and that adaptation cost is measurable before any arm is added

## What would be done

[CASE-294](../cases.d/CASE-294.md)'s pilot: checkpoints 16k, 64k, 128k and 143k of
Pythia-70M-deduped; two task families (associative mappings, relational
composition) with rules randomized by episode; three fine-tuning seeds;
fresh optimizer state, calibrated learning rates, runs that never reach
threshold reported as censored. The reading of Anguita and colleagues
adds: fix and report the head's initialization scale.

## What would count

The pilot succeeds as calibration if every checkpoint can learn both
families within budget and the estimand separates from seed noise. It
says nothing yet for or against [CLAIM-758](../claims.d/CLAIM-758.md); a flat or noisy result calls
for redesigning the tasks, not adding arms.

## Cost

Twenty-four fine-tuning runs of a 70M model, plus calibration: small.
