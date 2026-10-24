---
status: Proposed
promote_when: >-
  An empirical test, not another simulation: animals or people whose
  choices are fitted by this scheme, with the habit's prior and transitions
  estimated from their own history, showing that the amount of prior
  practice that the fitted counts imply predicts insensitivity to
  devaluation, and that the same fits predict immediate switching when
  devaluation comes before that point. It is refuted, as an account of
  habit, if devaluation sensitivity is lost under training regimes where
  the fitted policy counts stay low, or kept where they are high. A
  simulation in another task cannot settle it; the authors themselves say
  the scheme makes probably no new behavioural predictions.
title: "In a simulated active inference agent, a habit learned by counting the agent's own state transitions and policy choices emerges from goal-directed behaviour, and once acquired it persists, and reinforces itself, after the reward is devalued, while an agent devalued before acquisition switches at once"
version: 1
tags:
- learning-and-conditioning
- probabilistic-modeling
- neuroscience
date: '2026-10-24'
source:
- LIT-tmp35raq
summary: >-
  Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo (2016),
  LIT-tmp35raq, read in full from the CC BY version of record in
  NOTE-tmpxqv1t. One simulated T-maze task. The habit is one more policy
  scored by posterior probability; its prior and transitions grow by
  count, not by reward. It shows persistence under devaluation, a cached
  mapping failing when what is appropriate changes; it does not show
  amortization, and its reaction times are simulation run times.
supports:
- CLAIM-tmp0qupq
---
<!-- inactive-ok-file: CLAIM-tmp0qupq THEORY-062 — Proposed; the claim and account this bears on, named, nothing here rests on them -->

# THEORY-tmpydeuq: In a simulated active inference agent, a habit learned by counting the agent's own state transitions and policy choices emerges from goal-directed behaviour, and once acquired it persists, and reinforces itself, after the reward is devalued, while an agent devalued before acquisition switches at once

## Source

Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo,
LIT-tmp35raq, read in full in NOTE-tmpxqv1t from the version of record
(CC BY): pp. 865–869 (the model and its updates) and 874–876 (Figs 6–7).

## What was actually shown

The agent chooses among sequential policies and one habit, a policy that
maps each state to the next whatever the time. Its choice is a softmax of
a learned log prior over policies minus their precision-weighted expected
free energy. After each trial the habit's transitions and the policy prior
are updated by counting: "if a particular state or policy is encountered
frequently, it will come to dominate posterior expectations" (p. 869).

- **Emergence.** In a constant context the habit's posterior probability
  rises until it is executed routinely (Fig. 6). With the context random,
  an epistemic habit, visiting the cue first, forms in about 16 trials
  (Fig. 7).
- **Devaluation after acquisition.** Switching preferences at trial 48:
  "Despite this switch, the habit persists and, indeed, reinforces itself
  with repeated executions" (p. 874).
- **Devaluation before acquisition.** Switching at trial 16, the agent
  changes behaviour at once and later forms a habit matching the new
  preferences (p. 874).

What could have come out otherwise: the habit is scored against the
sequential policies on every trial, so the expected free energy of the
devalued outcome could have overturned it. It did not, because its prior
and its better explanation of past outcomes outweighed that term.

## What this does not say

- **That habits work this way in brains.** It is a simulation of one task
  with parameters set by hand. The neural assignments (dopamine as
  precision, cerebellum and dorsolateral striatum for habits) are offered,
  not tested, and the authors concede that "At the level of behavioural
  predictions, the answer is probably no" (p. 876).
- **That habit saves computation.** Reaction times fell, but they are
  simulation processing times, and every sequential policy is still
  evaluated each trial. Persistence is shown; amortization is not.
- **That the prior is reward-driven.** The policy prior and the habit's
  transitions grow by frequency. Reward acts only through which policy was
  inferred and through precision.
- **Anything about priors over who governs.** The habit is a prior over
  action sequences, not over which process decides.

## Connections

- **CLAIM-tmp0qupq.** Supports it in two places and corrects one
  citation. The formula π = σ(Ê − F − γ·G) is the claim's P(g | z, H) at
  the level of action policies. The devaluation result is its point that a
  prior over actions fails when what is appropriate changes, shown for the
  cached arm. But the paper's learned prior is frequency-driven, not the
  reward-modulated Hebbian bias the claim proposes, and it shows
  persistence, which the claim already says is not amortization.
- **THEORY-062.** That account arbitrates model-based and model-free
  control by relative reliability. This one arbitrates by posterior
  probability with ambiguity added, and denies that model-free learning
  arises apart from model-based behaviour.
