---
number: 154
status: Open
formerly:
- LEAD-tmprscqw
title: 'Measure, for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references'
version: 1
stage: specified
priority: high
method:
- empirical
tags:
- cognition
- embodied-cognition
- learning-theory
date: '2026-11-19'
line:
- distributed-agency
- nucleating-argument
advances:
- QUESTION-095
operationalized_in:
- CASE-234
summary: >-
  The one measured crossover proposed for the record's most-cited question
  on stored work. Named in [QUESTION-095](../questions.d/QUESTION-095.md) and [CASE-234](../cases.d/CASE-234.md). Filed by the backlog
  audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-234 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-154: Measure, for each generation of image model, the number of generations of one character at which training a character LoRA becomes cheaper than conditioning on references

## What it would do

Run [CASE-234](../cases.d/CASE-234.md) across several generations of image model, costing training
and inference for a LoRA against reference conditioning as the number of
generations of one character grows.

Where the record names it:

- [QUESTION-095](../questions.d/QUESTION-095.md): "with A's proposal to measure the crossover as [CASE-234](../cases.d/CASE-234.md)"
- [CASE-234](../cases.d/CASE-234.md): "measures that crossover rather than assuming its direction"

## What would count

A crossover that moves with model generation prices one regime of
[QUESTION-095](../questions.d/QUESTION-095.md)'s trade in measured terms; no crossover in range says the
stored-work strategy does not pay for this task.
