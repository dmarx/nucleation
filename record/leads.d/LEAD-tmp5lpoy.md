---
status: Open
title: 'Read the data-scheduling and curriculum literature for experiments that order acquisitions, so that the cost of a later acquisition can be measured with and without an earlier one'
version: 1
stage: idea
method:
- reading
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
advances:
- CLAIM-756
- CLAIM-754
summary: >-
  The owner's suggestion of 2026-11-19: work on data scheduling may show,
  for example, that generic conversational text early in training makes
  later domain-specific text easier to learn. Ordering experiments have
  the shape CLAIM-756 needs, an earlier acquisition and the measured cost
  of a later one, with and without it, which neither GPT-3 nor ULMFiT
  isolates.
---

# LEAD-tmp5lpoy: Read the data-scheduling and curriculum literature for experiments that order acquisitions, so that the cost of a later acquisition can be measured with and without an earlier one

## What it would do

Search for, register and read work on data ordering and curricula in
training that measures the cost of acquiring one domain or skill with
and without having acquired another first. The owner recalls a result of
this kind for conversational text before domain-specific text; the
assistant did not recognize the specific paper and will search rather
than guess. Candidates the assistant recalls, unverified until checked:
Chen and colleagues, "Skill-it!" (2023), which orders training data by
prerequisite skills and measures data needed for a target skill;
Gururangan and colleagues, "Don't Stop Pretraining" (2020), on
domain-adaptive pretraining after general pretraining; Bengio and
colleagues, "Curriculum learning" (2009).

## What would count

For CLAIM-756's premise: the data or compute needed to reach a level on a
later domain or skill, lower after an earlier one than without it, with
the earlier one's cost stated. Against the stronger reading the owner's
example suggests: the order not mattering once total data is fixed.
