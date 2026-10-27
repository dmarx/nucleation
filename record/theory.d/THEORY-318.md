---
number: 318
status: Active
formerly:
- THEORY-tmpqnhih
title: "A bound k on the max-information between a dataset and an analyst's chosen statistic multiplies by at most 2^k the probability that the statistic overfits that dataset, and an ε-differentially private mechanism on datasets of n points keeps k at most log₂e·εn, whatever the distribution on datasets"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision for THEORY-318 (batch 044, ADR-047 v2).
    Theorem 2 and Lemma 5 of the Supplementary Material were re-derived,
    in the dated note below. The title drops its third clause, "so a
    holdout can validate many adaptively chosen statistics", which rests
    on Thresholdout's Theorem 11 and on proofs held in companion papers
    the record has not read. That clause and the former promote_when move
    to QUESTION-196.
tags:
- mathematical-statistics
- learning-theory
date: '2026-10-14'
source:
- LIT-964
summary: >-
  Dwork, Feldman, Hardt, Pitassi, Reingold & Roth (2015), [LIT-964](../literature.d/LIT-964.md),
  Supplementary Material only, read in [NOTE-848](../notes.d/NOTE-848.md) (Skimmed: the main
  text was not reached). Theorem 2 and Lemma 5 are proved there and were
  checked: P[overfit] ≤ 2^{I∞}·max P[overfit], and ε-DP gives
  I∞ ≤ log₂e·εn. Thresholdout's guarantee (Theorem 11), n =
  O(ln(m/β)/τ²·min{B, √(B ln(m/β))/τ}), is stated with its proof elsewhere.
  Statistical queries on a discrete universe only, and a procedure that
  prevents inflation, not a correction for a search already run.
bears_on:
- QUESTION-040
---
<!-- inactive-ok-file: NOTE-848 — Skimmed; the reading this rests on, of the Supplementary Material only -->

# THEORY-318: A bound k on the max-information between a dataset and an analyst's chosen statistic multiplies by at most 2^k the probability that the statistic overfits that dataset, and an ε-differentially private mechanism on datasets of n points keeps k at most log₂e·εn, whatever the distribution on datasets

## Source

Dwork, Feldman, Hardt, Pitassi, Reingold & Roth (2015), [LIT-964](../literature.d/LIT-964.md), the
Supplementary Material (§§1–2, 4), as read in [NOTE-848](../notes.d/NOTE-848.md). The Science
main text was not reached, and four of the six formal results are proved
in companion papers that the record does not hold.

## What was actually shown

**Max-information controls overfitting (Theorem 2, proved and
checked).** Let I∞(S; φ) be the least k with P[S = s | φ = f] ≤
2^k P[S = s] for all s, f. For any family of "bad" datasets R(φ),
P[S ∈ R(φ)] ≤ 2^k · max_f P[S ∈ R(f)]. With R the datasets on which φ's
empirical mean exceeds its true mean by τ, Hoeffding gives: if
I∞ ≤ log₂e·τ²n, the probability is at most e^{−τ²n} (Corollary 3).

**Differential privacy bounds max-information (Lemma 5, proved and
checked).** An ε-differentially private algorithm has I∞(S; M(S)) ≤
log₂e·εn for any distribution on datasets. Post-processing keeps the
privacy guarantee (Lemma 9), so whatever the analyst builds from the
private answers inherits it.

**Stronger bounds, stated with proofs elsewhere.** ε ≤ τ suffices
(Corollary 7: P[|P[φ] − E_S[φ]| > τ] ≤ 6e^{−τ²n}); (ε, δ)-privacy with
ε ≤ τ/4 and δ ≤ (β/8)^{4/τ} gives failure probability β when
n ≥ 48 ln(8/β)/τ² (Theorem 8). Thresholdout, which answers from the
holdout only when it disagrees with the training set beyond a noisy
threshold, keeps all m answers within τ with probability 1 − β while
fewer than B overfitting events have been detected, for n =
O(ln(m/β)/τ² · min{B, √(B ln(m/β))/τ}) (Theorem 11). Fresh data per query
would need width ∝ √(m ln(1/β)/n) (§4).

What could have failed: the analyst is arbitrary. A single adaptive
strategy beating the bound would refute it, and the proof of Theorem 2
leaves no room for one once I∞ is bounded.

## What this does not say

- **Not a correction for a search already run.** The guarantee holds
  only if the data were accessed through a private mechanism. It does not
  say how much an unrestricted search has inflated a statistic.
- **Not beyond statistical queries on a discrete universe.** Theorem 2 is
  general, but the bounds on max-information here come only through
  differential privacy, for [0, 1]-valued queries.
- **Not mutual information.** I∞ is a worst-case quantity, larger than
  mutual information. The expected-bias bound of [THEORY-028](THEORY-028.md) is a
  different, average-case result.
- **Not that the simulations confirm the theory.** The simulated
  implementation used Gaussian noise and an idealized budget, so it is
  not the analysed algorithm.
- **Not advice to reuse holdouts.** That instruction is for
  machine-learning practice and belongs in the anthology.

## Connections

- [THEORY-028](THEORY-028.md) bounds expected selection bias by √(2σ²·I) and says
  high-probability versions "are left to the differential-privacy
  literature". This is that version for statistical queries.
- [QUESTION-040](../questions.d/QUESTION-040.md) asks how far search inflates a candidate's d′. This
  answers the half it can: when access to the test data is mediated by a
  private mechanism, the inflation is bounded with high probability,
  logarithmically in the number of queries. It does not price a search
  that was not so mediated.

## Note of 2026-10-19: Theorem 2 and Lemma 5, re-derived

The promotion audit (batch 044) re-derived the two results the title now
states. S is a dataset drawn from any distribution, φ = M(S) the
analyst's output, taking countably many values, and R(f) a set of
"bad" datasets for each output f.

- **Max-information.** I∞(S; φ) is the least k with
  P[S = s | φ = f] ≤ 2^k P[S = s] for all s and f.
- **Theorem 2.** P[S ∈ R(φ)] = Σ_f P[φ = f] Σ_{s∈R(f)} P[S = s | φ = f]
  ≤ Σ_f P[φ = f] · 2^k P[S ∈ R(f)] ≤ 2^k max_f P[S ∈ R(f)]. With R(f) the
  datasets on which f's empirical mean exceeds its true mean by τ,
  Hoeffding bounds the maximum by e^{−2τ²n}.
- **Lemma 5.** If M is ε-differentially private, any two datasets of n
  points differ in at most n places, so P[M(s) = f] ≤ e^{εn} P[M(s′) = f]
  for all s, s′. Then P[S = s | M(S) = f] = P[S = s] P[M(s) = f] /
  Σ_{s′} P[S = s′] P[M(s′) = f] ≤ e^{εn} P[S = s], so k ≤ εn·log₂e.

These are the proofs [NOTE-848](../notes.d/NOTE-848.md) checked in the Supplementary Material. The
stronger transfers (Theorems 6 and 8) and Thresholdout's guarantee
(Theorem 11), stated above, are not re-derived; they are what
[QUESTION-196](../questions.d/QUESTION-196.md) asks about.
