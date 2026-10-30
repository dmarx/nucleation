---
number: 957
status: Active
formerly:
- THEORY-tmpjv5er
title: 'When the signal law depends on the decision, Kwon and Perchet''s approachability algorithm learns what each decision would reveal only from the stages on which it is played: it keeps every decision''s probability at least γ/|I| and estimates the flag by importance weighting, an estimate that is conditionally unbiased with second moment Σ_i 1/P[i_t = i] ≤ |I|²/γ, with the tuned floor γ shrinking as T^-1/3; when the signal law does not depend on the decision, the raw signal is already unbiased for every component and no floor is used'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-1159. The estimate and its properties are
    Kwon and Perchet's §4.1 and Lemma A.4, and the floor's tuning is
    Theorem 4.1's γ. Lemma A.4 is re-derived below step by step and was
    checked by simulation on the approach–avoid signals, which meets the
    condition for Active under ADR-047 v2. The reading of the floor as
    protected access is the record's.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-1526
summary: >-
  Kwon and Perchet (2017), [LIT-1526](../literature.d/LIT-1526.md), read in [NOTE-1159](../notes.d/NOTE-1159.md). Under
  decision-dependent partial monitoring, information about a decision's
  signal comes only from playing it, and its unbiased estimate costs
  variance inversely proportional to the probability of playing it. A
  floor is how the algorithm keeps that finite. That the floor is
  necessary in general is supported by the matching lower bound, not shown
  here. Nothing here says what floor a non-learning system should keep.
---
<!-- inactive-ok-file: CLAIM-446 THEORY-932 — Proposed; entries this account is compared with, nothing here rests on their being settled -->
# THEORY-957: When the signal law depends on the decision, Kwon and Perchet's approachability algorithm learns what each decision would reveal only from the stages on which it is played: it keeps every decision's probability at least γ/|I| and estimates the flag by importance weighting, an estimate that is conditionally unbiased with second moment Σ_i 1/P[i_t = i] ≤ |I|²/γ, with the tuned floor γ shrinking as T^-1/3; when the signal law does not depend on the decision, the raw signal is already unbiased for every component and no floor is used

## Source

Kwon and Perchet (2017), [LIT-1526](../literature.d/LIT-1526.md), §4.1 (the algorithm), Lemma A.4 of the
supplement (the estimate), Theorem 4.1 (γ) and §4.3 (outcome-dependent
signals). Read in [NOTE-1159](../notes.d/NOTE-1159.md). The derivation below follows Lemma A.4.

## What was actually shown

At stage t the decision maker draws i_t with P[i_t = i | G_t] = (1 − γ)a_t^i
+ γ/|I| ≥ γ/|I|, then sees s_t ~ s(i_t, j_t). The flag is
f_t = (s(i, y_t))_{i∈I}, the signal law each decision would have under
Nature's current mixed action. The estimate is

f̂_t^i = 1{i_t = i} δ_{s_t} / P[i_t = i | G_t], for each i ∈ I.

**Unbiased.** Conditional on G_t, f̂_t^i is nonzero only on {i_t = i},
which has probability P[i_t = i | G_t]. So
E[f̂_t^i | G_t] = E[δ_{s_t} | G_t, i_t = i] = E[s(i, y_t) | G_t] = E[f_t^i | G_t].

**Second moment.** At most one component is nonzero, and ‖δ_s‖² = 1, so
E[‖f̂_t‖² | G_t] = Σ_i P[i_t = i] · 1/P[i_t = i]² = Σ_i 1/P[i_t = i]
≤ |I| · |I|/γ = |I|²/γ. Almost surely ‖f̂_t‖² ≤ (|I|/γ)².

**The floor's size.** Theorem 4.1 sets γ = min{(11L_r|I||K||A|/(4‖g‖))^{2/3}
T^{−1/3}, 1}. As a heuristic reading, which is the record's and not the
proof's: exploration costs O(γ) in distance, and the estimate's variance
costs about √(|I|²/(γT)) by the second moment above. Balancing the two
gives γ ∝ T^{−1/3}, and the distance then also scales as T^{−1/3}.

**No floor when signals do not depend on the decision.** If s(i, j) does
not depend on i, then the one signal s_t has law s(i, y_t) for every i at
once. So f̂_t = (δ_{s_t})_i is unbiased for every component, with
‖f̂_t‖² = |I|, without any decision being forced (§4.3).

**Checked by simulation** on the approach–avoid signals: avoid shows one
symbol whatever the outcome, approach reveals it, the danger probability is
0.3, and the policy always avoids except for the floor. Over 2 × 10⁵
stages the estimate recovered both flags, approach's (0.3, 0.7) to within
0.012. The empirical second moment matched Σ 1/P exactly (5.32 against
5.33 at γ = 0.5, 21.2 against 21.1 at γ = 0.1, and 99 against 101 at
γ = 0.02), within the bound |I|²/γ.

What could have failed: the decision maker might have been able to infer
an unplayed decision's flag component from the others. In general it
cannot, since Nature's mixed actions that agree on the played components
can differ on the rest. [THEORY-962](THEORY-962.md)'s kernel construction is the
finite case.

## What this does not say

- **Not that a floor is the only device.** Bartók et al.'s CBP, against
  stochastic opponents, samples informative actions as confidence widths
  demand and has no fixed floor ([NOTE-1164](../notes.d/NOTE-1164.md)). The floor is this
  algorithm's device for adversarial Nature.
- **Not that the floor must be uniform.** It is uniform for simplicity. The
  variance depends on Σ_i 1/P[i_t = i], so only the decisions whose signals
  matter need protecting.
- **Not a prescription for organizations or people.** That defensive
  authority removing approach is a zero floor is [CLAIM-446](../claims.d/CLAIM-446.md)'s reading.
- **Not that the T^{−1/3} rate is caused by the floor alone.** The rate is
  proved for this algorithm and matches a lower bound. Lemma A.4 is one of
  its parts.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** Its evidence-access correction is a positive floor on
  approach. The approach–avoid signals are decision-dependent, so the
  general case applies.
- **[THEORY-932](THEORY-932.md), [THEORY-925](THEORY-925.md).** The same frequency factor. [THEORY-932](THEORY-932.md)'s
  expected update scales with how often an option is chosen, and COMA keeps
  a probability floor for this reason. Here the cost is explicit, as the
  variance Σ 1/P.
- **[QUESTION-271](../questions.d/QUESTION-271.md).** When feedback is bandit-like, information about an
  untried process costs exploration. When it is outcome-dependent, it does
  not.
- **[THEORY-947](THEORY-947.md).** The rates this estimate serves.
