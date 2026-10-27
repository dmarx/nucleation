---
status: Active
title: 'In the Indian buffet process the feature probabilities in decreasing order are products of independent Beta(α, 1) draws, so the k-th has mean (α/(α + 1))^k, and keeping only the first K of them gives an expected number of occupied features among N objects that approaches αH_N from below: 8.97 at K = 16, N = 12 and α = 3, against 9.31 in the limit and 6.83 for the finite model with sixteen independent prevalences'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmptxvho. The construction is the paper's,
    §3.1 of Teh, Görür and Ghahramani (2007), re-derived from the cdf of a
    maximum. The truncation's count is the record's, from the
    construction: E[μ_(k)^j] = (α/(α + j))^k gives the exact sum, 8.974 at
    K = 16, which 200,000 simulated draws reproduce (8.969 ± 0.006); the
    finite model's 6.83 is THEORY-999's (record script, 2026-10-27). It
    confirms CASE-165's simulated 8.97.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-27'
source:
- LIT-tmpfhqac
summary: >-
  Teh, Görür and Ghahramani (2007), LIT-tmpfhqac, read in NOTE-tmptxvho.
  μ_(k) = ∏_{l≤k} ν_l with ν_l ~ Beta(α, 1). Truncated at K, the expected
  number of occupied features is Σ_{k≤K} Σ_{j=1}^{N} (−1)^{j+1} C(N, j)
  (α/(α + j))^k, which sums to αH_N as K → ∞. At N = 12, α = 3: 6.80,
  8.97, 9.27 and 9.31 at K = 8, 16, 24 and 32. It concerns the prior's
  expected count, not a posterior, and the paper itself computes no
  truncation error.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-tmphvhg6: In the Indian buffet process the feature probabilities in decreasing order are products of independent Beta(α, 1) draws, so the k-th has mean (α/(α + 1))^k, and keeping only the first K of them gives an expected number of occupied features among N objects that approaches αH_N from below: 8.97 at K = 16, N = 12 and α = 3, against 9.31 in the limit and 6.83 for the finite model with sixteen independent prevalences

## Source

Teh, Görür and Ghahramani (2007), *Stick-breaking construction for the
Indian buffet process*, LIT-tmpfhqac, read in full in NOTE-tmptxvho:
§3.1 (the construction, (5)–(15)) and §3.2 (truncation, (19)–(20)).

## What was actually shown

**The construction (the paper's).** For the finite model's K independent
Beta(α/K, 1) prevalences, the largest has cdf μ^α, so it is Beta(α, 1);
given the k largest, the next has cdf (μ/μ_(k))^{α(K − k)/K} → (μ/μ_(k))^α.
So ν_(k) = μ_(k)/μ_(k−1) are i.i.d. Beta(α, 1) and μ_(k) = ∏_{l≤k} ν_(l).
E[μ_(k)] = (α/(α + 1))^k.

**The truncation's count (the record's).** An object holds feature k with
probability μ_(k), independently given the sticks, so feature k is
occupied among N objects with probability 1 − E[(1 − μ_(k))^N] =
Σ_{j=1}^{N} (−1)^{j+1} C(N, j) E[μ_(k)^j], and E[μ_(k)^j] = (α/(α + j))^k.
Summing over all k gives Σ_j (−1)^{j+1} C(N, j) α/j = αH_N, the IBP's
count (THEORY-tmpo1cju); summing to K gives the truncation's. At N = 12,
α = 3:

| K | 8 | 16 | 24 | 32 | 50 | limit |
|---|---|---|---|---|---|---|
| truncated construction | 6.799 | 8.974 | 9.274 | 9.306 | 9.310 | 9.310 |
| finite model, K independent Beta(α/K, 1) (THEORY-999) | | 6.83 | | | 8.38 | 9.310 |

Simulation of the truncated construction at K = 16 (200,000 draws) gives
8.969 ± 0.006. Each object holds Σ_{k≤16} (3/4)^k = 2.97 features on
average there, against α = 3. The deficit at K = 16, 0.34, is the expected
number of occupied features beyond the 16th stick; at least one such
feature is occupied in 24% of draws, although P(K+ > 16) under
Poisson(9.31) is only 0.015.

## What this does not say

- **Not a bound on the error of the matrix.** It gives the expected count
  only; the paper points to the Dirichlet process's truncation bound and
  computes nothing.
- **Not about the posterior.** A truncation's effect on inference
  depends on the data.
- **Not that the two approximations are interchangeable.** At the same K
  the finite model and the truncated construction are different priors;
  CASE-165's model (T23) is the finite one.

## Connections

- **CASE-165, item 1.** Confirms the case's "8.97, simulated" and its
  "close to it", and qualifies its reason: what the truncation loses is
  features beyond the 16th stick, occupied in 24% of draws, not the
  1.5% of draws in which more than 16 features are occupied.
- **THEORY-999.** The finite model at the same K = 16 expects 6.83.
  Both approach αH_N from below, the construction much faster.
- **THEORY-1034.** The Markov IBP's stick-breaking construction is this
  one with an independent persistence attached to each stick.
