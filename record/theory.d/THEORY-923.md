---
number: 923
status: Active
formerly:
- THEORY-tmpydeuq
title: 'In one simulated T-maze task with hand-set parameters, run once per condition, an active inference agent''s habit, learned by counting its own state transitions and policy choices, emerged from goal-directed behaviour, and once acquired it persisted, and reinforced itself, after the reward was devalued, while an agent devalued before acquisition switched at once'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the tenth status review (ADR-057;
    ADR-047's evidence ruling, read in full in NOTE-1138, the
    figures from their captions). The title now claims only what the
    one task, run once per condition, showed. The old title: In a
    simulated active inference agent, a habit learned by counting
    the agent's own state transitions and policy choices emerges
    from goal-directed behaviour, and once acquired it persists, and
    reinforces itself, after the reward is devalued, while an agent
    devalued before acquisition switches at once. The promote_when
    asked for an empirical test the title never claimed, and moves
    unchanged to QUESTION-313, as THEORY-285's did to
    QUESTION-303. CLAIM-443 now lists this reading under
    corroborated_by, not grounds (ADR-058).
tags:
- learning-and-conditioning
- probabilistic-modeling
- neuroscience
date: '2026-10-24'
source:
- LIT-1476
summary: >-
  Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo (2016),
  [LIT-1476](../literature.d/LIT-1476.md), read in full from the CC BY version of record in
  [NOTE-1138](../notes.d/NOTE-1138.md). One simulated T-maze task. The habit is one more policy
  scored by posterior probability; its prior and transitions grow by
  count, not by reward. It shows persistence under devaluation, a cached
  mapping failing when what is appropriate changes; it does not show
  amortization, and its reaction times are simulation run times.
bears_on:
- QUESTION-313
---
<!-- inactive-ok-file: CLAIM-443 THEORY-062 — Proposed; the claim and account this bears on, named, nothing here rests on them -->

# THEORY-923: In one simulated T-maze task with hand-set parameters, run once per condition, an active inference agent's habit, learned by counting its own state transitions and policy choices, emerged from goal-directed behaviour, and once acquired it persisted, and reinforced itself, after the reward was devalued, while an agent devalued before acquisition switched at once

## Source

Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo,
[LIT-1476](../literature.d/LIT-1476.md), read in full in [NOTE-1138](../notes.d/NOTE-1138.md) from the version of record
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

- **[CLAIM-443](../claims.d/CLAIM-443.md).** Supports it in two places and corrects one
  citation. The formula π = σ(Ê − F − γ·G) is the claim's P(g | z, H) at
  the level of action policies. The devaluation result is its point that a
  prior over actions fails when what is appropriate changes, shown for the
  cached arm. But the paper's learned prior is frequency-driven, not the
  reward-modulated Hebbian bias the claim proposes, and it shows
  persistence, which the claim already says is not amortization.
- **[THEORY-062](THEORY-062.md).** That account arbitrates model-based and model-free
  control by relative reliability. This one arbitrates by posterior
  probability with ambiguity added, and denies that model-free learning
  arises apart from model-based behaviour.
