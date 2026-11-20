---
number: 157
status: Open
formerly:
- LEAD-tmpsn7tp
title: 'Measure the permutation-aligned barrier over several path families, and test whether alignment always removes the barrier between networks known to share a mechanism'
version: 1
stage: idea
method:
- empirical
tags:
- loss-landscapes
- representation-learning
date: '2026-11-19'
line:
- learned-structure
- pragmatic-transport
advances:
- QUESTION-069
- CLAIM-263
- CLAIM-187
summary: >-
  Named in [QUESTION-069](../questions.d/QUESTION-069.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-263 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-157: Measure the permutation-aligned barrier over several path families, and test whether alignment always removes the barrier between networks known to share a mechanism

## What it would do

Align networks by permutation, measure the loss barrier along several path
families, and repeat for a pair built to share a mechanism.

Where the record names it:

- [QUESTION-069](../questions.d/QUESTION-069.md): "Phase III runs aligned by permutation, with the barrier
  measured on several path families. Alongside that, a pair of networks
  known to share a mechanism, tested for whether alignment always removes
  their barrier."

## What would count

A barrier that survives alignment between networks sharing a mechanism
defeats the reading that a surviving barrier marks a different mechanism
([CLAIM-263](../claims.d/CLAIM-263.md)); its removal supports it.
