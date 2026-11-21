---
number: 2152
status: Proposed
formerly:
- THEORY-tmp4zojc
promote_when: >-
  A second reading of §3.1 with the theorems it applies (Theorems 2.8 to
  2.10), or an independent restatement read by the record, confirms that
  for an n × m Gaussian matrix with entries of variance 1/m, n/m → c ∈
  (0, 1], plus a deterministic rank-r perturbation with singular values θ_i,
  the top singular values tend almost surely to
  √((1 + θ_i²)(c + θ_i²)/θ_i²) when θ_i > c^(1/4) and to 1 + √c otherwise,
  and that for r = 1 the left singular vector's squared overlap tends to
  1 − c(1 + θ²)/(θ²(θ² + c)) above the threshold and to zero below.
title: "Benaych-Georges and Nadakuditi show that a large Gaussian rectangular matrix plus a fixed-rank deterministic perturbation has an outlying singular value, and singular vectors correlated with the perturbation's, only for perturbation singular values above the fourth root of the aspect ratio, with closed forms for both above it"
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-2964
corroborates:
- CLAIM-799
summary: >-
  Benaych-Georges and Nadakuditi (2012), [LIT-2964](../literature.d/LIT-2964.md), read in [NOTE-2246](../notes.d/NOTE-2246.md)
  (§3.1 only). The additive, signal-plus-noise form of the spiked
  transition: the model the record's two-class mixture ([CASE-301](../cases.d/CASE-301.md)) and
  mean-shift step ([CLAIM-827](../claims.d/CLAIM-827.md)) actually use, with the same formulas as
  the spiked covariance model ([ARG-135](../arguments.d/ARG-135.md)). Proposed until §3.1 and the
  theorems behind it are confirmed.
---
<!-- inactive-ok-file: NOTE-2246 — Skimmed; the reading this account is filed from -->
<!-- inactive-ok-file: CASE-301 CLAIM-827 ARG-135 — Proposed; the entries that use this reading, and the argument of 2026-11-21 -->

# THEORY-2152: Benaych-Georges and Nadakuditi show that a large Gaussian rectangular matrix plus a fixed-rank deterministic perturbation has an outlying singular value, and singular vectors correlated with the perturbation's, only for perturbation singular values above the fourth root of the aspect ratio, with closed forms for both above it

## Source

Benaych-Georges and Nadakuditi, arXiv 1103.2221 (2011); J. Multivariate
Anal. 111 (2012). [LIT-2964](../literature.d/LIT-2964.md), read in [NOTE-2246](../notes.d/NOTE-2246.md) (§3.1).

## The account

X_n is n × m with independent N(0, 1/m) entries, n/m → c ∈ (0, 1]; P_n is
deterministic with fixed rank r and singular values θ_i. Then
σ_i(X_n + P_n) → √((1 + θ_i²)(c + θ_i²)/θ_i²) almost surely if
θ_i > c^(1/4), and → 1 + √c otherwise (9). For r = 1, P_n = θuv*, the
squared overlap of the top left singular vector with u tends to
1 − c(1 + θ²)/(θ²(θ² + c)) for θ ≥ c^(1/4) and to zero otherwise (10).

In the record's notation (n = D, m = N, c = γ, θ² = β) the threshold is
β > √γ, the top eigenvalue of the uncentred second moment is
(1 + β)(1 + γ/β), and the overlap is (1 − γ/β²)/(1 + γ/β): the spiked
formulas, for a signal added to the data matrix.

## What this does not say

- Not the spiked covariance model itself; that is BBP's, Baik and
  Silverstein's and Paul's. The two models agree in these limits, which is
  why the record's entries could state BBP's formulas for additive models.
- Not the fluctuations, nor non-Gaussian noise, as read here (§3.1 only).
- Not a perturbation of growing rank.
