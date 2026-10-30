---
status: Proposed
title: 'The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is exact for frequency-adjusted Q-learning, not for Q-learning, whose expected update carries an extra factor of each action''s selection probability and whose trajectories in 2×2 games depart from the model depending on initialization'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-30'
source:
- LIT-1511
extends:
- THEORY-932
promote_when: >-
  The 2003 derivation (LIT-1501) read and found to assume, as Kaisers and
  Tuyls say, that every Q-value changes at rate α; and a quantitative
  comparison, not only plots, of Q-learning and frequency-adjusted
  Q-learning against the model's predicted trajectories in 2×2 games over
  a range of temperatures, showing the frequency-adjusted learner within
  noise of the model and Q-learning off it in an initialization-dependent
  way. It is refuted if plain Q-learning with small steps matches the
  model as closely as the frequency-adjusted learner across
  initializations. Results in multi-state tasks are wider than this and
  neither promote nor refute it.
summary: >-
  The wide form of Kaisers & Tuyls (AAMAS 2010), [LIT-1511](../literature.d/LIT-1511.md), kept here when
  the twenty-fourth status review narrowed [THEORY-932](THEORY-932.md) to what the
  derivation proves and what their three games showed, and promoted it
  ([ADR-047](../decisions.d/ADR-047.md), kind 1). The paper asserts that the model is exact for
  frequency-adjusted Q-learning and that Q-learning departs from it
  depending on initialization. Its plots are three games, one
  temperature, compared by eye.
---
<!-- inactive-ok-file: LIT-1501 — Unavailable; the model Kaisers and Tuyls correct, known here only through them -->

# THEORY-tmpdpn31: The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is exact for frequency-adjusted Q-learning, not for Q-learning, whose expected update carries an extra factor of each action's selection probability and whose trajectories in 2×2 games depart from the model depending on initialization

## Source

Kaisers and Tuyls (2010), [LIT-1511](../literature.d/LIT-1511.md), read in full in [NOTE-1140](../notes.d/NOTE-1140.md). The model
they correct is Tuyls, Verbeeck and Lenaerts (2003), [LIT-1501](../literature.d/LIT-1501.md), which is
Unavailable and is known here only as Kaisers and Tuyls restate it.

## What is shown and what is not

[THEORY-932](THEORY-932.md) holds what is proved. The model is the expected dynamics of an
all-update learner, and so of frequency-adjusted Q-learning wherever every
probability is at least β. Q-learning's expected update carries a factor
x_i. This entry asserts more. It says "exact" without the small-step and
x_i ≥ β conditions, and it says the departure holds in 2×2 games generally.
The paper's evidence for that is Fig. 4, three games at τ = 0.1 with no
measure of fit. A check of the expected dynamics at the status review of
2026-10-30, three games with payoffs of its own at τ = 0.1 and 1, found
departures of 0.02 to 0.31 and dependence on initialization from 0.00 to
0.31. That is not the quantitative comparison of sampled learners that the
condition asks for.
