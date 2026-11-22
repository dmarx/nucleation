---
number: 175
status: Open
formerly:
- LEAD-tmpvdouu
title: 'Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain''s critical sample sizes'
version: 1
stage: idea
priority: medium
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
<!-- inactive-ok-file: CASE-tmpgqbyq CLAIM-tmpg8m7a CLAIM-tmp9zqvq CLAIM-tmpraadt — new, filed 2026-11-22 by LEAD-175's study -->

# LEAD-175: Re-run the toy-model-of-superposition check: SGD at n = 1,000 and on both sides of n = 600, and posterior sampling across n for the chain's critical sample sizes

## What it would do

Run the existing script across learning rates, batch sizes and
initializations, and sample the posterior across n.

Where the record names it:

- [QUESTION-363](../questions.d/QUESTION-363.md): "and SGD at n = 1,000 and on both sides of n"

## What would count

Whether the 6-gon is reached decides "inaccessible" against "not reached"
for [QUESTION-363](../questions.d/QUESTION-363.md).

## Note of 2026-11-22: carried out

Done by a delegated worker on branch claude/lead-175-superposition-sweep
(scratch/studies/lead-175/). The SGD sweep and posterior sampling across
n are filed as CASE-tmpgqbyq. The claims filed from it:

- CLAIM-tmpg8m7a: the 5-gon's dropped feature gets no gradient under
  SGD;
- CLAIM-tmp9zqvq: the 6-gon is not reached at any setting tried;
  "inaccessible", for this model;
- CLAIM-tmpraadt: the posterior's critical sizes differ from the
  formula's, and there is a factor-½ difference of scale in Chen et al.

**What remains:**

- the finite-dataset posterior (NUTS-like, per n, as Fig. 2);
- other trainers: weight decay, Langevin noise, Adam;
- whether the live 5⁺ route opens at some setting not tried.

The lead's stage and status are the owner's.
