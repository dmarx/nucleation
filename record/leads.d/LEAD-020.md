---
number: 20
status: Open
formerly:
- LEAD-tmp15t0v
title: 'Simulate an interpretation loop that does not lock in with action held fixed, and show which candidate''s removal makes it lock in'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- cognition
- agency
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-121
summary: >-
  Named in [QUESTION-121](../questions.d/QUESTION-121.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-020: Simulate an interpretation loop that does not lock in with action held fixed, and show which candidate's removal makes it lock in

## What it would do

Build the loop and remove the candidates one at a time.

Where the record names it:

- [QUESTION-121](../questions.d/QUESTION-121.md): "A loop that does not lock in, with action held fixed, and
  a demonstration that removing a given candidate makes it lock in."

## What would count

A candidate whose removal produces lock-in answers [QUESTION-121](../questions.d/QUESTION-121.md).

## Note of 2026-11-22: carried out
<!-- inactive-ok-block: CASE-tmp943kt CLAIM-tmp95c61 — new; filed for LEAD-020 -->

Carried out by the assistant on branch claude/lead-020-nonlockin-ablation. The study is [CASE-tmp943kt](../cases.d/CASE-tmp943kt.md) (executed-study), with code, eleven pytest tests, 1368 result cells and a summary in scratch/studies/lead-020/. The finding is [CLAIM-tmp95c61](../claims.d/CLAIM-tmp95c61.md). Dated notes went on [QUESTION-121](../questions.d/QUESTION-121.md), [CLAIM-342](../claims.d/CLAIM-342.md), [CLAIM-340](../claims.d/CLAIM-340.md), [CLAIM-339](../claims.d/CLAIM-339.md) and [CASE-099](../cases.d/CASE-099.md). A loop that does not lock in, with action held fixed, was built. In its minimal forms, removing commitment, processing signals or exogenous capture makes it lock in, which is what the lead's "What would count" names. With all candidates present, no single removal does. What remains:

- whether this answers [QUESTION-121](../questions.d/QUESTION-121.md), which the claim gives as two readings for the owner;
- why commitment worked even where [CLAIM-340](../claims.d/CLAIM-340.md)'s sign condition predicts coupling, which was not diagnosed;
- intention–outcome contingency, which the model lacks.

The lead's status and stage are the owner's.
