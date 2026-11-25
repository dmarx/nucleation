---
number: 2148
status: Proposed
formerly:
- THEORY-tmp0covn
promote_when: >-
  A second proof, or a published restatement read by the record, confirms
  for complex Gaussian spiked sample covariance with M/N → γ² ≥ 1 the
  threshold 1 + γ⁻¹ for the largest eigenvalue's separation, its limit
  ℓ₁(1 + γ⁻²/(ℓ₁ − 1)) above the threshold, and the change of fluctuation
  order from M^(−2/3) to M^(−1/2). Baik and Silverstein (THEORY-2149)
  already confirm the threshold and the limit almost surely; the
  fluctuation part still rests on this paper alone.
title: 'Spikes above 1+√(N/M) pull out the top eigenvalue'
statement: >-
  Baik, Ben Arous and Péché prove that for complex Gaussian samples whose
  population covariance is the identity but for finitely many eigenvalues,
  with at least as many samples as variables, the largest sample eigenvalue
  leaves the bulk edge if and only if some population eigenvalue exceeds 1 +
  √(N/M), converging then to a stated outlier with fluctuations of order
  M^(-1/2) instead of the edge's Tracy-Widom M^(-2/3)
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-2986
corroborates:
- CLAIM-799
- CLAIM-804
- CLAIM-827
- CLAIM-837
bears_on:
- QUESTION-510
summary: >-
  Baik, Ben Arous and Péché (2005), [LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md):
  the BBP transition. The record's spiked-matrix claims use its threshold
  and outlier, but for real data, eigenvectors, more variables than samples
  and several outliers they rest on Baik and Silverstein, Paul, and
  Benaych-Georges and Nadakuditi, which this paper corroborates
  ([ARG-145](../arguments.d/ARG-145.md)). Proposed until a second reading confirms it.
---
<!-- inactive-ok-file: THEORY-2201 — new; the reading of Takeuchi and Sano, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2149 ARG-145 — Proposed; the neighbouring reading and the argument of 2026-11-21 -->

# THEORY-2148: Spikes above 1+√(N/M) pull out the top eigenvalue

## Source

Baik, Ben Arous and Péché, arXiv math/0403022v2; Ann. Probab. 33(5), 2005.
[LIT-2986](../literature.d/LIT-2986.md), read in [NOTE-2241](../notes.d/NOTE-2241.md) (§1, §2.1, §6; proofs skipped).

## The account

With M complex Gaussian samples of N variables, M/N = γ², and a population
covariance whose eigenvalues are 1 except ℓ_1 ≥ … ≥ ℓ_r, the largest sample
eigenvalue λ_1 tends to the Marchenko–Pastur edge (1 + γ⁻¹)² with
Tracy–Widom fluctuations of order M^(−2/3) while ℓ_1 < 1 + γ⁻¹; at
ℓ_1 = 1 + γ⁻¹ it has new laws F_k on the same scale; above, it tends to
ℓ_1(1 + γ⁻²/(ℓ_1 − 1)) with fluctuations of order M^(−1/2), the law of the
top eigenvalue of a k × k GUE matrix when k spikes are equal (Theorem 1.1,
Corollary 1.1). In the record's notation (γ_rec = D/N = γ⁻², β = ℓ − 1): the
threshold is β > √γ_rec and the outlier (1 + β)(1 + γ_rec/β).

What could have come out otherwise: the threshold could have been other
than the point where the outlier formula meets the edge, or the transition
could have been smooth in law. It is sharp, with a critical window of width
M^(−1/3) in ℓ (Theorem 1.2).

## What this does not say

- Not the real case, which it states as a conjecture; Baik and Silverstein
  give the almost-sure limits for it ([THEORY-2149](THEORY-2149.md)).
- Not anything about eigenvectors.
- Not the case of more variables than samples.
- Not why the threshold is where it is: "we do not have an intuitive
  reason yet".
- Not that the transition is a phase transition of the population or of
  any learner: it is a transition in the law of an estimator's top
  eigenvalue.

## Note of 2026-11-22: Takeuchi and Sano, read

**Background, no edge.** The GUE Tracy-Widom law this theorem gives at
the edge of a sample covariance spectrum, fluctuations of order
M^(−2/3) below the threshold, turns up in a growing interface: Takeuchi
and Sano ([LIT-2982](../literature.d/LIT-2982.md), [NOTE-2284](../notes.d/NOTE-2284.md); [THEORY-2201](THEORY-2201.md)) find the local radius
of a curved turbulent front distributed as GUE TW, skewness about 0.2241
and kurtosis about 0.09345, with GOE for flat fronts (p. 3). The same
distribution, from a different object; nothing here bears on the
threshold or the outlier this theorem proves.
