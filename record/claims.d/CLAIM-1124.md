---
number: 1124
status: Proposed
formerly:
- CLAIM-tmpk8zw2
title: 'In a percept–action loop whose context matters only to what the action does and whose sticky nuisance matters only to prediction, the cheapest memory that does the task keeps exactly the interventional partition taken relative to the task''s outcome, which is disjoint from the predictive partition, by nostalgia, heat per step and overwrite entropy alike'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation such that, corrected, some memory that does
  the task in the toy loop costs less than the one keeping only the context
  by one of the three measures, or the computed partitions differ from
  those stated. A different loop in which a predictive memory is cheapest
  does not defeat it, since the claim is about this loop; nor does the
  objection that the interventional partition should be taken relative to
  the whole percept, which is the alternative reading.
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
- THEORY-1125
bears_on:
- QUESTION-494
summary: >-
  One of two readings of [CASE-391](../cases.d/CASE-391.md)'s comparison, filed as alternatives;
  the other is [CLAIM-1116](CLAIM-1116.md). This one takes the interventional partition
  as [THEORY-1125](../theory.d/THEORY-1125.md) does, relative to a target, here the outcome of the
  action: percepts grouped by p(y' | x, do(a)) for each a. That partition
  is the context u; the predictive partition, grouped by p(x' | x) under
  random actions or under the agent's own loop, is the nuisance v. The
  memory keeping only u does the task (success 0.95, against 0.5 for v or
  nothing) and is the cheapest that does, by the Still nostalgia, the heat
  per step and the entropy lost on overwriting, in four parameter settings.
  In this loop [QUESTION-494](../questions.d/QUESTION-494.md)'s answer is the interventional partition. The
  assistant leans to this reading. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-391 CLAIM-1116 — filed by the lead run of 2026-11-23 -->

# CLAIM-1124: In a percept–action loop whose context matters only to what the action does and whose sticky nuisance matters only to prediction, the cheapest memory that does the task keeps exactly the interventional partition taken relative to the task's outcome, which is disjoint from the predictive partition, by nostalgia, heat per step and overwrite entropy alike

## The claim

[QUESTION-494](../questions.d/QUESTION-494.md) asks whether the memory that minimizes dissipation in a loop
with feedback keeps the interventional partition, the predictive one, or
neither. Taken literally, the memory that keeps nothing dissipates least,
so the comparison is among memories that do the task.

In [CASE-391](../cases.d/CASE-391.md)'s loop, with the interventional partition relative to the
outcome y:

| memory | partition | success | nostalgia | heat per step | H[S_t \| S_{t+1}] |
|---|---|---|---|---|---|
| none | — | 0.500 | 0 | 0 | 0 |
| v | predictive | 0.500 | 0.312 | 0.597 | 0.334 |
| u | interventional | 0.948 | 0.676 | 2.985 | 0.693 |
| u and v | both | 0.946 | 0.975 | 3.268 | 1.035 |
| u, v and y | everything | 0.941 | 1.158 | 3.508 | 1.293 |

(ε = 0.1, δ = 0.05, gap 6; three other settings give the same order.)

## Why the interventional reading

[THEORY-1125](../theory.d/THEORY-1125.md) defines the causal information bottleneck relative to a
target Y, and [QUESTION-494](../questions.d/QUESTION-494.md) names that bottleneck as the interventional
partition. The task's outcome is the natural target. Read so, the loop
gives the question's first answer: keep the interventional partition and
nothing else. The predictive partition is cheaper and useless.

## Limits

- **Much follows from the construction.** The task is defined by
  intervention, and u is the only thing the action's effect depends on.
  What the run adds is that all three costs agree with that choice and
  that the partition the no-feedback result favours does nothing here.
- **Revision is not counted.** The loop does not change, so the cost of
  revising a memory, one of [QUESTION-494](../questions.d/QUESTION-494.md)'s four, is absent.
- **One loop.** Under confounding the partitions can differ in other ways
  ([THEORY-1146](../theory.d/THEORY-1146.md)); this loop has no hidden common cause.
