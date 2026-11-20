---
number: 117
status: Open
formerly:
- LEAD-tmpjvq8n
title: 'Compare an RL-trained model with no verifier against its base under best-of-N with the training verifier, at matched total compute and across k, after searching for work that already does so'
version: 1
stage: idea
method:
- reading
- empirical
tags:
- learning-theory
- operations-research
date: '2026-11-19'
line:
- realizability
- learned-structure
advances:
- CLAIM-699
- CLAIM-695
- QUESTION-392
summary: >-
  Named in [CLAIM-699](../claims.d/CLAIM-699.md) and [QUESTION-392](../questions.d/QUESTION-392.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CLAIM-699 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-117: Compare an RL-trained model with no verifier against its base under best-of-N with the training verifier, at matched total compute and across k, after searching for work that already does so

## What it would do

Search for published comparisons at matched compute; failing one, run the
comparison on a small open model, amortizing training cost across the test
set.

Where the record names it:

- [CLAIM-699](../claims.d/CLAIM-699.md): "Compare an RL model at one or few samples with no verifier
  against its base under best-of-N with the training verifier, at matched
  total compute"
- [QUESTION-392](../questions.d/QUESTION-392.md): "It turns this question's "how can the two be told apart"
  into one comparison, valid only where recognition is cheap. Not run."

## What would count

The base under best-of-N matching the RL model at equal compute supports
[CLAIM-699](../claims.d/CLAIM-699.md)'s reading that RL moves capability into the policy without
adding to it; the RL model winning defeats it.
