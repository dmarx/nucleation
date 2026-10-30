---
status: Proposed
promote_when: >-
  Data, not more simulation: in a sequential avoidance task with known
  transition structure, people's choices are fit better by a model with a
  pessimistic weight on their own future actions than by an optimal agent
  with inflated threat values or altered transition beliefs, and that
  weight relates to anxiety; or the model's own prediction confirmed, a
  free-choice premium reduced or reversed in anxious people. It is refuted
  if anxious avoidance in such tasks is explained as well by altered threat
  values with an optimal policy, or if the bias appears where no future
  avoidance is at stake. A qualitative match of new simulations to further
  published effects cannot settle it.
title: 'In a Markov decision process, an agent that evaluates actions as if it will fail to avoid danger at later steps, while in fact choosing optimally at each step, spreads threat value to states far from the danger and avoids early and widely, which reproduces qualitatively exaggerated threat appraisal, fear generalization and several laboratory findings associated with anxiety'
version: 1
tags:
- psychopathology-and-treatment
- learning-and-conditioning
date: '2026-10-30'
source:
- LIT-1496
extends:
- THEORY-915
bears_on:
- QUESTION-325
summary: >-
  The wide form [THEORY-915](THEORY-915.md) held before the thirteenth status review
  narrowed it, kept as a Proposed reading by the [ADR-047](../decisions.d/ADR-047.md) kind-1 sweep of
  2026-10-30: the source asserts it, and [THEORY-915](THEORY-915.md), Active, is its
  evidence. Zorowitz, Momennejad and Daw (2020), [LIT-1496](../literature.d/LIT-1496.md), state it of
  Markov decision processes in general and show it in the environments
  they simulate. The inherited promote_when asks for data in people, which
  the paper leaves to future work.
---

# THEORY-tmpv4uka: In a Markov decision process, an agent that evaluates actions as if it will fail to avoid danger at later steps, while in fact choosing optimally at each step, spreads threat value to states far from the danger and avoids early and widely, which reproduces qualitatively exaggerated threat appraisal, fear generalization and several laboratory findings associated with anxiety

## Source

Zorowitz, Momennejad and Daw (2020), *Computational Psychiatry* 4: 1–17,
[LIT-1496](../literature.d/LIT-1496.md), read in full in [NOTE-1136](../notes.d/NOTE-1136.md). What its simulations showed is
[THEORY-915](THEORY-915.md), which this entry extends.

## The claim

The paper argues from the Bellman equation itself. Under the optimal
equation, opportunities for reward propagate back to earlier states and
avoidable dangers do not, "because the return-maximizing action is to
avoid": "If danger can be avoided later, it poses less threat now".
Replace the max over next actions with a mixture of best and worst, so
that the agent expects to fail later while still choosing optimally now,
and the asymmetry goes: threat value spreads backward across the state
space, and the agent avoids early and widely. The paper presents this as a
property of any such agent, and as an account of exaggerated threat
appraisal, fear generalization and several laboratory findings in
anxious people, in which the misbelief concerns one's own future control
and the danger is represented correctly.

[THEORY-915](THEORY-915.md) holds what the simulations showed, in a gridworld, the balloon
analogue risk task, a sleeping-predator task and a two-branch task. The
general statement, and the match to anxiety, are the paper's.

## What would settle it

The promote_when, carried over unchanged, which is also the [THEORY-915](THEORY-915.md)
part of [QUESTION-325](../questions.d/QUESTION-325.md)'s "What would answer it": people's choices in a
sequential avoidance task fit better by a pessimistic weight on their own
future actions than by inflated threat values or altered transition
beliefs, with the weight related to anxiety, or a free-choice premium
reduced or reversed in anxious people. More simulations matched to
published effects cannot settle it.
