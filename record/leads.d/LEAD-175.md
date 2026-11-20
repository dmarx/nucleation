---
number: 175
status: Open
formerly:
- LEAD-tmpvdouu
title: 'Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain''s critical sample sizes'
version: 1
stage: idea
method:
- empirical
tags:
- learning-theory
- loss-landscapes
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-363
summary: >-
  Named in [QUESTION-363](../questions.d/QUESTION-363.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-175: Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain's critical sample sizes

## What it would do

Run the existing script across learning rates, batch sizes and
initializations, and sample the posterior across n.

Where the record names it:

- [QUESTION-363](../questions.d/QUESTION-363.md): "and SGD at n = 1,000 and on both sides of n"

## What would count

Whether the 6-gon is reached decides "inaccessible" against "not reached"
for [QUESTION-363](../questions.d/QUESTION-363.md).
