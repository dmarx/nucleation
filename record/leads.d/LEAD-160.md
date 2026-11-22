---
number: 160
status: Open
formerly:
- LEAD-tmpt6mca
title: 'Run the world-model achievements study under matched competence'
version: 1
stage: specified
priority: medium
method:
- empirical
tags:
- agency
- cognition
- philosophy-of-science
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-362
- CLAIM-513
- CLAIM-514
- CLAIM-519
operationalized_in:
- CASE-187
summary: >-
  Named in [CASE-187](../cases.d/CASE-187.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmp6hkf9 CLAIM-tmpq92r4 CLAIM-tmpo59pd CLAIM-519 — new or Proposed; the LEAD-160 study and claims cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-514 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-160: Run the world-model achievements study under matched competence

## What it would do

Run [CASE-187](../cases.d/CASE-187.md): agents matched on task competence, tested for the
world-model achievements the claims separate.

Where the record names it:

- [CASE-187](../cases.d/CASE-187.md): "as the experiment that would sharpen the world-model
  distinction."

## What would count

Achievements that come apart under matched competence support the
distinctions of [CLAIM-513](../claims.d/CLAIM-513.md) and [CLAIM-514](../claims.d/CLAIM-514.md); achievements that always come
together count against them.

## Note of 2026-11-22: run at toy scale

A delegated worker ran [CASE-187](../cases.d/CASE-187.md) as [CASE-tmp6hkf9](../cases.d/CASE-tmp6hkf9.md): twenty 8x8 gridworld
mazes; a planner on a learned transition table, a goal-conditioned value
learner and a bank of occupancy-predicting demons; goal success matched
exactly by one shared stream of experience. All four of [CASE-187](../cases.d/CASE-187.md)'s tests
were run. Code, tests and results are in `scratch/studies/lead-160/`.

The achievements came apart in three places:
- read-out query competence went with goal competence, but query
  competence within each agent's own budget did not ([CLAIM-tmpq92r4](../claims.d/CLAIM-tmpq92r4.md));
- a unit-level intervention separated agents that act identically, but a
  content-level one made the distributed predictor respond as the planner
  does without a table ([CLAIM-tmpo59pd](../claims.d/CLAIM-tmpo59pd.md));
- recovery and damage localization went with the explicit table.

So [CLAIM-514](../claims.d/CLAIM-514.md)'s and [CLAIM-519](../claims.d/CLAIM-519.md)'s defeated_if clauses are not met in this
class, and [CLAIM-513](../claims.d/CLAIM-513.md) is untouched. What remains:
- scale: function approximation, partial observation, stochastic
  dynamics;
- the replay variant;
- other budgets;
- the composite goals of Richens et al.

The stage and status are the owner's to change.
