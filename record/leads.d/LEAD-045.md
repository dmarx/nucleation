---
number: 45
status: Open
formerly:
- LEAD-tmp67v9a
title: 'Separate the mechanisms that set acquisition order and timing by training the same unequal-frequency skills under gradient descent and under sign descent'
version: 1
stage: idea
priority: high
method:
- empirical
- formal
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-039
- QUESTION-193
summary: >-
  A discriminating test for a question with fourteen bearing entries;
  [LEAD-008](LEAD-008.md) covered only the reading on data order. Named in [QUESTION-039](../questions.d/QUESTION-039.md)
  and [QUESTION-193](../questions.d/QUESTION-193.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: LEAD-008 — Done; cited in the backlog audit of 2026-11-19 -->

# LEAD-045: Separate the mechanisms that set acquisition order and timing by training the same unequal-frequency skills under gradient descent and under sign descent

## What it would do

Train one network on independent skills of unequal frequency under
gradient descent and under sign descent (or Adam at small beta), and a
hierarchical task from small and order-one initial scale; derive, for sign
descent, the delayed onset of each weaker skill and the ratio of onset
times.

Where the record names it:

- [QUESTION-039](../questions.d/QUESTION-039.md): "so swapping the optimizer separates the two mechanisms."
- [QUESTION-193](../questions.d/QUESTION-193.md): "A trained network on independent skills of unequal
  frequency whose onsets go from simultaneous to sequential when only the
  optimizer is changed"

## What would count

Onsets that go from simultaneous to sequential when only the optimizer
changes separate the gradient-flow steps from the Domino steps, answering
[QUESTION-193](../questions.d/QUESTION-193.md) and narrowing [QUESTION-039](../questions.d/QUESTION-039.md).
