---
number: 2
status: Done
formerly:
- LEAD-tmp5lpoy
title: 'Read the data-scheduling and curriculum literature for experiments that order acquisitions, so that the cost of a later acquisition can be measured with and without an earlier one'
version: 2
history:
- version: 2
  date: '2026-11-19'
  note: >-
    Done: a search and six readings (curation entry of 2026-11-19, 211445).
    The candidates the assistant recalled were read; one was misdescribed
    here: Chen and colleagues mix prerequisite data in, they do not order
    it. The specific result the owner recalls was not found; a narrower
    search, for Reddit or forum data, is LEAD-008.
stage: underway
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
  the shape [CLAIM-756](../claims.d/CLAIM-756.md) needs, an earlier acquisition and the measured cost
  of a later one, with and without it, which neither GPT-3 nor ULMFiT
  isolates.
---

# LEAD-002: Read the data-scheduling and curriculum literature for experiments that order acquisitions, so that the cost of a later acquisition can be measured with and without an earlier one

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

For [CLAIM-756](../claims.d/CLAIM-756.md)'s premise: the data or compute needed to reach a level on a
later domain or skill, lower after an earlier one than without it, with
the earlier one's cost stated. Against the stronger reading the owner's
example suggests: the order not mattering once total data is fixed.

## What came of it

Two works measure an earlier acquisition lowering a later one's cost with
the earlier cost counted: Hu and colleagues (a formal-language first
phase, a third fewer total tokens at 1B) and Chen and colleagues (mixing
prerequisites in, a third fewer steps at fixed budget). Bengio and
colleagues give the pattern in final-error terms. Gururangan and
colleagues, Liu and colleagues, and Feng and colleagues measure final
performance; the second finds specialized data early better than late,
against the direction of the owner's example, and the third finds that
developmental order within child conversation barely matters.
