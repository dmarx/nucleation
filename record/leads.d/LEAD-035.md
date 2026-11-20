---
number: 35
status: Open
formerly:
- LEAD-tmp3ol4v
title: 'Check the SNR singular values against the predicted quarter-power law for neural collapse'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-051
summary: >-
  Named in [NOTE-783](../notes.d/NOTE-783.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: NOTE-772 — Skimmed; cited in the backlog audit of 2026-11-19 -->

# LEAD-035: Check the SNR singular values against the predicted quarter-power law for neural collapse

## What it would do

Measure on trained networks, and register the work [NOTE-772](../notes.d/NOTE-772.md) names.

Where the record names it:

- [NOTE-783](../notes.d/NOTE-783.md): "A measurement of the SNR singular values in a trained
  network, against (4t/N)^(1/4), would settle whether the closed form
  describes training."

## What would count

Agreement says the closed form describes training by ordinary gradient
descent, which bears on [QUESTION-051](../questions.d/QUESTION-051.md); disagreement confines it to the
renormalized flow.
