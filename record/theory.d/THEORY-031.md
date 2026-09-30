---
number: 31
status: Active
formerly:
- THEORY-tmp87j2h
title: 'The likelihood-ratio detector is optimal under the payoff, Neyman–Pearson and posterior criteria, which differ only in its threshold, so performance is an ROC and the criterion a point on it; d′ is criterion-free only for equal-variance normal signal and noise'
version: 1
tags:
- probabilistic-modeling
- cognition
- information-theory
- mathematics
date: '2026-09-30'
source:
- LIT-364
- LIT-368
- LIT-367
summary: >-
  Peterson & Birdsall (1953), [LIT-364](../literature.d/LIT-364.md) — the threshold on ℓ = f_SN/f_N is
  optimal for expected value and at fixed false-alarm rate, and the two
  optimum families coincide (Part I Thms 1–7). The ROC's slope equals the
  threshold (Thm 8). Tanner & Swets (1954), [LIT-368](../literature.d/LIT-368.md), carry this over to
  the human observer as d′ plus a criterion. Stanislaw & Todorov (1999),
  [LIT-367](../literature.d/LIT-367.md), state that d′ varies with the criterion unless the variances
  are equal. The separation of sensitivity from bias is a property of the
  model, not of the data.
---

# THEORY-031: The likelihood-ratio detector is optimal under the payoff, Neyman–Pearson and posterior criteria, which differ only in its threshold, so performance is an ROC and the criterion a point on it; d′ is criterion-free only for equal-variance normal signal and noise

## Source

Peterson & Birdsall (1953), [LIT-364](../literature.d/LIT-364.md), Part I Thms 1–8 and Eqs. 1.4–1.6, 2.10, 2.51–2.53; Part II §4.2 ([NOTE-315](../notes.d/NOTE-315.md), Skimmed for Part II §4.4–4.9 only). Tanner & Swets (1954), [LIT-368](../literature.d/LIT-368.md), pp. 401–409 ([NOTE-316](../notes.d/NOTE-316.md)). Stanislaw & Todorov (1999), [LIT-367](../literature.d/LIT-367.md), pp. 139–148 ([NOTE-314](../notes.d/NOTE-314.md)).

## What was actually shown

Peterson and Birdsall prove the following. The criterion {x : ℓ(x) ≥ β} maximises P_SN − β·P_N, where β carries the priors and the four payoffs (Thm 1, Eq. 1.6). A likelihood-ratio set with false-alarm rate k maximises detection among all criteria with false alarm ≤ k (Thm 5, the Neyman–Pearson form). Every such set is one of the first kind for some β, and every k is attained (Thms 6–7). The posterior P_x(SN) is a monotone function of ℓ, so the a-posteriori approach uses the same receiver (Eq. 2.10). Optimal criteria are unique up to null sets when f_N is analytic (Thms 3–4). The ROC summarises any receiver, and the optimal ROC's slope at each point is its threshold β (Thm 8). For a signal known exactly in white Gaussian noise, ln ℓ is normal with equal variance under both hypotheses, so one index, d = 2E/N₀, fixes the whole curve (Part II Eqs. 4.1–4.8). The receiver is a matched filter.

Tanner and Swets carry this over to the human observer. They introduce d′ = √d as the separation of equal-variance normals, and a cutoff whose optimal position is where the curve's slope equals the prior-and-payoff β (eq. [2]). They predict that yes-no and 4AFC tasks yield one d′. They reject the "false alarms are guesses" model: false-alarm rates correlated with chance-corrected thresholds, and all 12 fitted lines miss (1, 1) (p. 408). They also write that the data suggest equal variance "is not a true assumption" (p. 403).

Stanislaw and Todorov state the condition. Under normality and equal variance d′ is unaffected by bias; otherwise "d′ will vary with response bias" (p. 140). The z-ROC slope estimates σ_N/σ_S. Their worked rating example gives d′ from 0.84 to 1.86 across five criteria (Table 6). c is independent of d′, and β is not.

## What this does not say

- That human observers use the optimal criterion. Tanner and Swets assert that they "tended to" but report no comparison with eq. [2]. Their data come from three observers, and they give no fit statistics.
- That d′ measures sensitivity model-free. Without equal-variance normality there is only the ROC, or A_z, which assumes normality but not equal variance.
- That Peterson and Birdsall originated the likelihood-ratio lemma. Theorem 5 is Neyman–Pearson ([LIT-365](../literature.d/LIT-365.md), Deferred) restated for receivers, and the report credits it only in its bibliography and Appendix C.
- That P(error) = Q(d′/2) appears in any of the three. It is a one-line consequence of each ([NOTE-314](../notes.d/NOTE-314.md), [NOTE-315](../notes.d/NOTE-315.md), [NOTE-316](../notes.d/NOTE-316.md)).

## Connections

- [LIT-048](../literature.d/LIT-048.md) (transfer entropy as a log-likelihood ratio) shares only the likelihood-ratio framing.
- Green & Swets ([LIT-366](../literature.d/LIT-366.md), Deferred) is cited by [LIT-367](../literature.d/LIT-367.md) for ROC area = 2AFC proportion correct.
