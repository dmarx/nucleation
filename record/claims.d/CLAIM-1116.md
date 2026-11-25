---
number: 1116
status: Proposed
formerly:
- CLAIM-tmpj5z7a
title: 'Cheapest memory keeps neither partition'
statement: >-
  In the same percept–action loop, if the interventional partition is taken
  relative to the whole next percept, the cheapest memory that does the task
  keeps neither partition: it is a strict coarsening of the interventional
  partition, and the predictive partition contains it only under a fixed
  action and is disjoint from it under random actions or the agent's own
  loop
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation such that, corrected, the interventional
  partition relative to the whole next percept is the context alone, or
  the cheapest memory that does the task keeps the nuisance too. The
  argument that the partition should be taken relative to the outcome does
  not defeat it; that is the alternative reading.
tags:
- thermodynamics
- causality
- information-theory
- learning-theory
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
grounds:
- CASE-391
bears_on:
- QUESTION-494
summary: >-
  The alternative to [CLAIM-1124](CLAIM-1124.md)'s reading of [CASE-391](../cases.d/CASE-391.md). If the
  interventional partition groups percepts by p(x' | x, do(a)) for the
  whole next percept, it keeps the sticky nuisance v as well as the context
  u, since v's future depends on v whatever is done. The predictive
  partition depends on the regime: v under random actions or the agent's
  own loop, u and v under a fixed action. The cheapest memory that does
  the task keeps u only, which is a strict coarsening of the
  interventional partition and is never the predictive one. In this
  reading [QUESTION-494](../questions.d/QUESTION-494.md)'s answer for the loop is neither: the memory keeps
  what is relevant to the task's outcome under intervention, a target the
  question's two partitions do not name. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-391 CLAIM-1124 — filed by the lead run of 2026-11-23 -->

# CLAIM-1116: Cheapest memory keeps neither partition

## The claim

The partitions of the percept (u, v, y) in [CASE-391](../cases.d/CASE-391.md)'s loop, computed:

| partition | grouped by | result |
|---|---|---|
| predictive, random actions | p(x' \| x) | {v} |
| predictive, the agent's own loop (a = u) | p(x' \| x) | {v} |
| predictive, fixed action (a = 0) | p(x' \| x) | {u, v} |
| interventional, outcome | p(y' \| x, do(a)) for each a | {u} |
| interventional, whole percept | p(x' \| x, do(a)) for each a | {u, v} |

The memory that does the task most cheaply keeps {u} ([CLAIM-1124](CLAIM-1124.md)'s
table). Relative to the whole next percept, that is neither the
interventional partition nor any predictive one. It is the interventional
partition relative to the outcome.

## What it changes

[QUESTION-494](../questions.d/QUESTION-494.md) sets the predictive and the interventional partitions as the
candidates. This reading says the toy picks out a third object, relevance
to a chosen target under intervention, so the question needs its target
named before it can be answered. It also shows that "the predictive
partition" is not one thing under feedback: it depends on the regime that
generates the data, and the agent's own policy is one such regime.

## Which reading

The two claims agree on every number and differ on the definition. This
one is filed beside [CLAIM-1124](CLAIM-1124.md) because [QUESTION-494](../questions.d/QUESTION-494.md) does not say which
target its interventional partition is taken relative to. The assistant
leans to [CLAIM-1124](CLAIM-1124.md), since the question names the causal information
bottleneck, which is defined relative to a target. The choice is the
owner's.
