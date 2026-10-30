---
status: Proposed
title: 'In a simulated active inference agent, a habit learned by counting the agent''s own state transitions and policy choices emerges from goal-directed behaviour, and once acquired it persists, and reinforces itself, after the reward is devalued, while an agent devalued before acquisition switches at once'
version: 1
tags:
- learning-and-conditioning
- probabilistic-modeling
- neuroscience
date: '2026-10-30'
source:
- LIT-1476
extends:
- THEORY-923
promote_when: >-
  An empirical test, not another simulation: animals or people whose
  choices are fitted by this scheme, with the habit's prior and transitions
  estimated from their own history, showing that the amount of prior
  practice the fitted counts imply predicts insensitivity to devaluation,
  and that the same fits predict immediate switching when devaluation comes
  before that point. The account of habit is refuted if devaluation
  sensitivity is lost under training regimes where the fitted policy counts
  stay low, or kept where they are high. A simulation in another task
  cannot settle it.
bears_on:
- QUESTION-313
summary: >-
  The wide form THEORY-923 held before the tenth status review narrowed it,
  kept as a Proposed reading by the ADR-047 kind-1 sweep of 2026-10-30: the
  source asserts it, and THEORY-923, Active, is its evidence.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-tmpvfbtz: In a simulated active inference agent, a habit learned by counting the agent's own state transitions and policy choices emerges from goal-directed behaviour, and once acquired it persists, and reinforces itself, after the reward is devalued, while an agent devalued before acquisition switches at once

## Source

Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo (2016),
LIT-1476, read in full in NOTE-1138. What its one simulated T-maze task,
with hand-set parameters and run once per condition, showed is THEORY-923,
which this entry extends.

## The claim

The paper states its result as a property of the scheme, not of the one
task. In active inference a habit is one more policy, a state-to-state
mapping whose transitions and prior grow by counting what the agent does.
The paper asserts that such a habit forms from the agent's observation of
its own goal-directed behaviour, and that once acquired it persists after
devaluation, while before acquisition behaviour switches at once (NOTE-1138,
C1–C2). It goes further and says that, to the extent one accepts the
variational formulation, model-free learning cannot be learned apart from
model-based behaviour (C7). The authors also concede that at the level of
behavioural predictions the scheme probably offers nothing new (p. 876).

## What would settle it

The promote_when, which is QUESTION-313: choices of animals or people
fitted by this scheme, with the counts estimated from their own history,
predicting when behaviour becomes insensitive to devaluation and when it
still switches at once. A simulation in another task cannot settle it.
