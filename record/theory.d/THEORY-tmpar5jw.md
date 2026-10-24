---
status: Proposed
promote_when: >-
  The 2003 derivation (LIT-tmp0imkw) read and found to assume, as Kaisers
  and Tuyls say, that every Q-value changes at rate α; and a quantitative
  comparison, not only plots, of Q-learning and frequency-adjusted
  Q-learning against the model's predicted trajectories in 2×2 games over
  a range of temperatures, showing the frequency-adjusted learner within
  noise of the model and Q-learning off it in an initialization-dependent
  way. It is refuted if plain Q-learning with small steps matches the model
  as closely as the frequency-adjusted learner across initializations.
  Results in multi-state tasks are wider than this and neither promote nor
  refute it.
title: 'The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is exact for frequency-adjusted Q-learning, not for Q-learning, whose expected update carries an extra factor of each action''s selection probability and whose trajectories in 2×2 games depart from the model depending on initialization'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-tmpgfdwc
- LIT-tmp0imkw
summary: >-
  Kaisers & Tuyls (AAMAS 2010), LIT-tmpgfdwc, read in full in NOTE-tmp43vkx,
  correcting the model of Tuyls, Verbeeck & Lenaerts (2003), LIT-tmp0imkw,
  which is not read. The derivation of the discrepancy is short and was
  checked in the reading; the experiments are three games, one
  temperature, compared by eye.
---
<!-- inactive-ok-file: LIT-tmp0imkw NOTE-tmp43vkx THEORY-tmp3wkwk CLAIM-tmp8z857 — Proposed, Unavailable or new; the sources and the accounts this bears on, named -->

# THEORY-tmpar5jw: The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is exact for frequency-adjusted Q-learning, not for Q-learning, whose expected update carries an extra factor of each action's selection probability and whose trajectories in 2×2 games depart from the model depending on initialization

## Source

Michael Kaisers and Karl Tuyls, "Frequency adjusted multi-agent
Q-learning", AAMAS 2010, pp. 309–315, LIT-tmpgfdwc, read in full in
NOTE-tmp43vkx (sections 2.4–4). The model it corrects is Tuyls, Verbeeck
and Lenaerts (AAMAS 2003), LIT-tmp0imkw, which could not be reached and is
known here only as Kaisers and Tuyls restate it.

## What was actually shown

- **The model.** ẋ_i = x_i α(τ⁻¹[(Ay)_i − x·Ay] − log x_i +
  Σ_k x_k log x_k): replicator selection plus a mutation term (Eq. 2).
- **The assumption behind it.** Q̇_i = α(E[r_i] + γ max_j Q_j − Q_i) for
  every action. In Q-learning only the chosen action is updated, so
  E[ΔQ_i] = x_i α(…) (p. 312). Under the assumption the γ term cancels and
  the dynamics live in policy space; with the factor x_i neither holds, and
  the dynamics depend on the Q-values (checked in the reading).
- **Frequency adjustment.** Scaling each update by min(β/x_i, 1) restores
  the model wherever x_i ≥ β.
- **Experiments.** In the prisoners' dilemma, battle of the sexes and
  matching pennies at τ = 0.1, Q-learning's trajectories depend on whether
  Q-values start at the minimum, mean or maximum of the reward range and
  depart from the model, most in the prisoners' dilemma, while the
  frequency-adjusted learner's follow it (Fig. 4).

## What this does not say

- That the mutation term is wrong. It is right for learners whose every
  option is updated, the case Sato and Crutchfield treat (THEORY-tmp3wkwk).
- That Q-learning's departure is large in general. No measure is given.
- That the term removes absorbing states. The paper does not discuss it;
  that the boundary is repelling under the term is a reading of Eq. 2.

## Connections

- **CLAIM-tmp8z857.** The factor x_i is the claim's trap in a learner:
  evidence about an option arrives only when the option is chosen, so an
  estimate of a rarely chosen option is rarely corrected. Inverse-frequency
  weighting is the correction that removes it.
