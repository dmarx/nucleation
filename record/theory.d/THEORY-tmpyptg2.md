---
status: Active
title: "In an actor-critic learner that can choose temporally extended options as well as primitive actions, options that fit the task speed learning, while options with ill-placed subgoals slow it, and options that fit an earlier layout keep the agent from finding a newly opened shortcut, so hierarchy helps only with the right subroutines"
version: 1
tags:
- behavioral-integration
- learning-and-conditioning
- cognition
date: '2026-10-16'
source:
- LIT-581
summary: >-
  Botvinick, Niv and Barto (2009), [LIT-581](../literature.d/LIT-581.md), read in [NOTE-451](../notes.d/NOTE-451.md). Toy
  simulations in a rooms domain with pre-trained options. Doorway options
  sped learning; window options slowed it; with a shortcut opened,
  primitive-only agents found the shortest path on 75% of runs while
  doorway-option agents never used it (mean 11.79 against 9.73 steps). It
  is a result about the model. That people or brains work this way is the
  separate, proposed account [THEORY-tmpal7n3](THEORY-tmpal7n3.md).
presupposed_by:
- THEORY-tmpal7n3
---
<!-- inactive-ok-file: THEORY-062 THEORY-tmpal7n3 — Proposed; named in Connections, not leaned on -->

# THEORY-tmpyptg2: In an actor-critic learner that can choose temporally extended options as well as primitive actions, options that fit the task speed learning, while options with ill-placed subgoals slow it, and options that fit an earlier layout keep the agent from finding a newly opened shortcut, so hierarchy helps only with the right subroutines

## Source

Botvinick, Niv and Barto (2009), [LIT-581](../literature.d/LIT-581.md) (*Cognition*), read in full in
[NOTE-451](../notes.d/NOTE-451.md) from the PMC author manuscript. The online appendix with the
update equations was not read, and the figures' plotted values were not
seen; the numbers below come from the text and footnote 10.

## What was actually shown

**The model.** Options in the standard sense: an initiation set, a
termination function and an option-specific policy, shaped by pseudo-reward
at the subgoal. An actor-critic learner updates by temporal-difference
prediction error. Options are pre-trained, "simulating transfer of
knowledge from earlier experience" (fn. 8). The system is model-free.

**Positive transfer (Fig. 4).** In a rooms task, an agent with doorway
options and primitive actions learns to reach the goal faster than one with
primitives alone.

**Negative transfer (Fig. 5).**

- Options with "window" subgoals slow learning.
- With a shortcut opened, primitive-only agents find the shortest path on
  "75% of training runs". Agents with doorway options learn to use only the
  main doorways. Over the last 10 of 500 episodes, mean solution time is
  11.79 steps with doorway options (passageway visited on 0% of episodes)
  against 9.73 with primitives only (79% of episodes) (fn. 10).

**What could have come out otherwise.** Any options could have helped, or
the doorway agents could have found the shortcut in time. Neither happened.

## What this does not say

- **That this holds at scale.** The domain is small and the options are
  pre-trained.
- **That the same happens in people.** The paper argues that option
  discovery is a central problem for human learning too (C5), and links
  negative transfer to it, but tests no human data.
- **That hierarchical learners always satisfice.** The paper says they tend
  to, "except under very slow learning".
- **That 75% and 79% conflict.** They measure different things: runs that
  converge to the shortest path, and episodes that visit the passage
  ([NOTE-451](../notes.d/NOTE-451.md), Corrections).
- **That human behaviour is strictly hierarchical.** The paper itself argues
  it is only quasi-hierarchical (C6).

## Connections

- The paper's proposed neural implementation of the same model is
  [THEORY-tmpal7n3](THEORY-tmpal7n3.md).
- Brooks's layered architecture ([LIT-436](../literature.d/LIT-436.md)) composes routines by design; this
  composes them by learning. Both are accounts of behavioural integration.
- Model-based option models, which make look-ahead "saltatory", are
  described but not implemented; the model-based and model-free division
  it adopts is [THEORY-062](THEORY-062.md).
