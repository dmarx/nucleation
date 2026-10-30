---
number: 932
status: Active
formerly:
- THEORY-tmpar5jw
title: 'The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is, in the small-step limit, the expected dynamics of a learner that updates every action''s value each step, and so of frequency-adjusted Q-learning wherever every action''s probability is at least its adjustment parameter; it is not that of Q-learning, whose expected update carries an extra factor of each action''s selection probability, so that its policy dynamics depend on the Q-values; in Kaisers and Tuyls''s three 2×2 games at one temperature, compared by eye, Q-learning''s trajectories departed from the model depending on initialization and the frequency-adjusted learner''s followed it'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active at the status review's ruling (the
    owner delegated these rulings), under ADR-065 §5 and §3 and ADR-047's
    "Where a narrowing's dropped claims go". A second checker (the
    twenty-fourth status review) re-derived the model from the all-update
    rule, the factor x_i and the frequency adjustment, and checked them by
    script with controls; the steps are in the note of 2026-10-30. The
    title was narrowed in two ways. "Exact" is now limited to small steps
    and to policies with every probability at least β, and the
    experiment is reported with its hedges, three games, one temperature,
    by eye. The wide form, which Kaisers and Tuyls assert, is kept as
    THEORY-tmpdpn31, Proposed, which extends this entry and inherits the
    promote_when (ADR-047, kind 1). The old title: The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is exact for frequency-adjusted Q-learning, not for Q-learning, whose expected update carries an extra factor of each action's selection probability and whose trajectories in 2×2 games depart from the model depending on initialization. The old
    promote_when: The 2003 derivation (LIT-1501) read and found to assume, as Kaisers and Tuyls say, that every Q-value changes at rate α; and a quantitative comparison, not only plots, of Q-learning and frequency-adjusted Q-learning against the model's predicted trajectories in 2×2 games over a range of temperatures, showing the frequency-adjusted learner within noise of the model and Q-learning off it in an initialization-dependent way. It is refuted if plain Q-learning with small steps matches the model as closely as the frequency-adjusted learner across initializations. Results in multi-state tasks are wider than this and neither promote nor refute it.
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1511
- LIT-1501
summary: >-
  Kaisers & Tuyls (AAMAS 2010), [LIT-1511](../literature.d/LIT-1511.md), read in full in [NOTE-1140](../notes.d/NOTE-1140.md),
  correcting the model of Tuyls, Verbeeck & Lenaerts (2003), [LIT-1501](../literature.d/LIT-1501.md),
  which is not read. The derivation of the discrepancy and of the
  frequency adjustment was re-derived and second-checked at the status
  review of 2026-10-30. The experiments are three games, one temperature,
  compared by eye; whether Q-learning departs in general is [THEORY-tmpdpn31](THEORY-tmpdpn31.md).
---
<!-- inactive-ok-file: LIT-1501 NOTE-1140 CLAIM-446 — Proposed, Unavailable or new; the sources and the accounts this bears on, named -->

<!-- inactive-ok-file: THEORY-tmpdpn31 — Proposed; the wide form this entry was narrowed from, which extends it -->

# THEORY-932: The replicator-plus-entropy model of Boltzmann Q-learning in two-player stateless games is, in the small-step limit, the expected dynamics of a learner that updates every action's value each step, and so of frequency-adjusted Q-learning wherever every action's probability is at least its adjustment parameter; it is not that of Q-learning, whose expected update carries an extra factor of each action's selection probability, so that its policy dynamics depend on the Q-values; in Kaisers and Tuyls's three 2×2 games at one temperature, compared by eye, Q-learning's trajectories departed from the model depending on initialization and the frequency-adjusted learner's followed it

## Source

Michael Kaisers and Karl Tuyls, "Frequency adjusted multi-agent
Q-learning", AAMAS 2010, pp. 309–315, [LIT-1511](../literature.d/LIT-1511.md), read in full in
[NOTE-1140](../notes.d/NOTE-1140.md) (sections 2.4–4). The model it corrects is Tuyls, Verbeeck
and Lenaerts (AAMAS 2003), [LIT-1501](../literature.d/LIT-1501.md), which could not be reached and is
known here only as Kaisers and Tuyls restate it.

## What was actually shown

- **The model.** ẋ_i = x_i α(τ⁻¹[(Ay)_i − x·Ay] − log x_i +
  Σ_k x_k log x_k): replicator selection plus a mutation term (Eq. 2).
- **The assumption behind it.** Q̇_i = α(E[r_i] + γ max_j Q_j − Q_i) for
  every action. In Q-learning only the chosen action is updated, so
  E[ΔQ_i] = x_i α(…) (p. 312). Under the assumption the γ term cancels and
  the dynamics live in policy space; with the factor x_i neither holds, and
  the dynamics depend on the Q-values (checked in the reading).
- **Frequency adjustment.** Scaling each update by min(β/x_i, 1) makes
  the expected step αβ times the all-update step wherever x_i ≥ β for
  every action. So in the small-step limit it follows the model, at rate
  αβ. Below β it is ordinary Q-learning.
- **Experiments.** In the prisoners' dilemma, battle of the sexes and
  matching pennies at τ = 0.1, Q-learning's trajectories depend on whether
  Q-values start at the minimum, mean or maximum of the reward range and
  depart from the model, most in the prisoners' dilemma, while the
  frequency-adjusted learner's follow it (Fig. 4).

## What this does not say

- That the mutation term is wrong. It is right for learners whose every
  option is updated, the case Sato and Crutchfield treat ([THEORY-928](THEORY-928.md)).
- That Q-learning's departure is large in general. No measure is given.
- That the term removes absorbing states. The paper does not discuss it;
  that the boundary is repelling under the term is a reading of Eq. 2.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** The factor x_i is the claim's trap in a learner:
  evidence about an option arrives only when the option is chosen, so an
  estimate of a rarely chosen option is rarely corrected. Inverse-frequency
  weighting is the correction that removes it.

## Note of 2026-10-30: the re-derivation, written out

The second check at the status review ([ADR-065](../decisions.d/ADR-065.md) §5) followed each step.

1. **The model from the all-update rule.** With x_i ∝ e^(Q_i/τ),
ẋ_i/x_i = τ⁻¹(Q̇_i − x·Q̇). If Q̇_i = α(r_i + γ max_j Q_j − Q_i) for every
i, the γ term is common to all actions and cancels. Then ẋ_i/x_i =
ατ⁻¹(r_i − x·r) − ατ⁻¹(Q_i − x·Q). Since Q_i/τ = log x_i + log Z, this is
α[τ⁻¹(r_i − x·r) − log x_i + Σ_k x_k log x_k], Eq. 2. It depends on x
only.

2. **Q-learning.** Only the chosen action is updated, and it is chosen
with probability x_i, so E[ΔQ_i] = x_i α(r_i + γ max Q − Q_i). Then
x·Q̇ = α Σ_k x_k²(…). The γ max Q term enters as γ max Q (x_i − Σ_k x_k²),
which does not vanish. The Q_i term enters through Q_i = τ log x_i + τ log
Z with weights that do not cancel log Z. So the policy dynamics depend on
the Q-values, not on x alone.

3. **Frequency adjustment.** The factor min(β/x_i, 1) x_i equals β
whenever x_i ≥ β. Then every action's expected update is αβ(…), which is
step 1 at rate αβ.

A script (numpy, in the session's scratchpad, s932_faq.py) integrated the
expected dynamics in Q-space. It used a prisoners' dilemma, a battle of the
sexes and matching pennies, with payoffs chosen by the checker, not the
paper's, at τ = 0.1 and τ = 1 and γ = 0.9. Each run started from one
policy, with Q-values shifted to the minimum, mean or maximum of the
reward range. The all-update learner matched Eq. 2 to 8 × 10⁻¹⁰ and
differed across initializations by at most 4 × 10⁻¹⁵. That was the null
control, which had to hold, and it did. The expected Q-learning dynamics
departed from the model by 0.17, 0.08 and 0.31 (largest gap in
probability) at τ = 0.1, and differed across initializations by 0.02,
0.03 and 0.31. That was the control that had to fail, and it did. The
frequency-adjusted learner, with β = 0.01 and step α/β, matched the model
to 4 × 10⁻¹² wherever every probability stayed at least β, which held in
four of the six runs. Where some probability fell below β it did not
match (gaps 1 to 2 × 10⁻³), as step 3 says. These are expected dynamics,
not sampled learners. They test the derivation, not the paper's plots.

## Note of 2026-10-30: the clauses the narrowing drops

The title said the model is "exact for frequency-adjusted Q-learning"
without condition, and that Q-learning's trajectories "in 2×2 games"
depart from it depending on initialization. The paper asserts both in
general, from three games at τ = 0.1 compared by eye. The general form is
kept as [THEORY-tmpdpn31](THEORY-tmpdpn31.md), Proposed, which extends this entry and inherits
the old promote_when ([ADR-047](../decisions.d/ADR-047.md)'s kind 1).
