---
number: 1030
status: Proposed
formerly:
- CLAIM-tmp60fme
title: 'In a small two-layer ReLU network trained conventionally on two tasks, both crossed interventions move its response to a conflicting learning demand: changing the optimizer with the network fixed changes how much of one task is lost while the other is relearned, and so does disrupting the units that carry its learned task separation with the optimizer fixed, by shares that depend on which optimizer trained it'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, from the lead run of that date.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of the same design (scratch/studies/lead-105/), with more seeds
  or other matched-pace step sizes at which every optimizer relearns the
  changed task, in which changing the probe optimizer with the trained
  parameters fixed leaves task A's peak forgetting unchanged within its
  95% interval for every optimizer in both trained populations; or in
  which re-initializing and healing the most task-selective units leaves
  it unchanged under every probe optimizer. Not defeated by a larger or
  different network that behaves otherwise, which bounds the claim's scope
  without contradicting it.
tags:
- learning-theory
- agency
date: '2026-11-23'
line:
- learned-structure
- distributed-agency
bears_on:
- QUESTION-122
grounds:
- CASE-404
summary: >-
  The crossed design of [CASE-113](../cases.d/CASE-113.md), run once in a small setting
  ([CASE-404](../cases.d/CASE-404.md)): two tasks with a task-identity input, a width-32
  ReLU network trained by heavy ball or by Adam, twelve seeds each, and a
  conflicting demand (task B's target turned against task A's). At matched
  pace, changing only the probe optimizer changed A's peak forgetting by
  −0.018 (−39%) for heavy-ball-trained networks and by up to +0.045
  (+147%) for Adam-trained ones, and carrying Adam's state from training
  instead of resetting it added +0.038. Re-initializing the eight most
  task-selective hidden units and healing raised it by +0.028 (+61%)
  under the training optimizer for heavy-ball-trained networks, where
  eight random units did not; for Adam-trained networks the same
  disruption showed under SGD, heavy ball and sign descent but not under
  Adam. Across the crossed cells the state accounts for 0.58 of the
  variation and the optimizer for 0.39 in heavy-ball-trained networks,
  0.15 and 0.81 in Adam-trained ones. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-404 — new; the study filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-367 — Proposed; the claim whose defeat condition the run tests -->

# CLAIM-1030: In a small two-layer ReLU network trained conventionally on two tasks, both crossed interventions move its response to a conflicting learning demand: changing the optimizer with the network fixed changes how much of one task is lost while the other is relearned, and so does disrupting the units that carry its learned task separation with the optimizer fixed, by shares that depend on which optimizer trained it

## The claim

[CASE-404](../cases.d/CASE-404.md) holds the design and every number. Three findings.

1. **The optimizer arm is not null.** With the trained parameters fixed
   and every optimizer calibrated to relearn the changed task at the same
   pace, the probe optimizer changed task A's peak forgetting in both
   populations: in heavy-ball-trained networks SGD and sign descent lost
   less of A than heavy ball; in Adam-trained networks heavy ball and SGD
   lost more than Adam. The optimizer's state counts as well as its rule:
   Adam's moments carried from training more than doubled the forgetting.
2. **The learned-state arm is not null.** Re-initializing the hidden
   units most selective for one task and healing them on the original
   tasks raised the forgetting under the training optimizer for
   heavy-ball-trained networks, and under three of the four optimizers for
   Adam-trained ones. Re-initializing as many random units did so less,
   and not at all under the training optimizer; permuting the units, a
   null control, did nothing.
3. **The split is not fixed.** The share of the variation that follows
   the optimizer rather than the state was 0.39 for one training optimizer
   and 0.81 for the other, and a disruption's effect depended on the
   optimizer that met it. What the response depends on is a fact about the
   network, the optimizer that trained it and the optimizer that meets the
   demand, together.

The first finding is the first limb of [CLAIM-367](CLAIM-367.md)'s defeat condition
failing in this setting; the second is the second limb holding in part.

## What it does not say

- That the network holds a regulatory representation. The disrupted units
  carry learned task separation that shapes how a conflict spreads; nothing
  in the network monitors or selects among updates.
- Anything beyond one small network, full batch, a conflict that resolves
  in tens of steps, and losses of a few percent of A's level.
- How the effect sizes compare with those in a large network or under
  stochastic batches.
