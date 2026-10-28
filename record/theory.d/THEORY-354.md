---
number: 354
status: Active
formerly:
- THEORY-tmpsavjk
title: "An observer's power to refute a predictor depends on its access to the predictor as well as on its budget: against tests that see only the sampled prediction a predictor of size O(s/ε²) always passes, but if fine-grained clique counting is hard, or BPP ≠ PSPACE, some cheap tests that may query the predictor adaptively pass only predictors about as costly as nature's own"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-1068
extends:
- THEORY-349
summary: >-
  Dwork, Kim, Reingold, Rothblum and Yona (2021), [LIT-1068](../literature.d/LIT-1068.md), read in [NOTE-885](../notes.d/NOTE-885.md).
  Against sample-access distinguishers of size s an outcome-indistinguishable
  predictor of size O(s/ε²) always exists. Against oracle-access distinguishers,
  under fine-grained hardness of clique counting or BPP ≠ PSPACE, there are natures
  and polynomially many cheap distinguishers such that no predictor much cheaper
  than nature is indistinguishable. Non-adaptive queries add little; the power
  comes from adaptive queries. The results are conditional and asymptotic, with
  upper and lower bounds in different parameterisations; they say nothing about
  human observers or about which access a real auditor has.
bears_on:
- QUESTION-104
---

# THEORY-354: An observer's power to refute a predictor depends on its access to the predictor as well as on its budget: against tests that see only the sampled prediction a predictor of size O(s/ε²) always passes, but if fine-grained clique counting is hard, or BPP ≠ PSPACE, some cheap tests that may query the predictor adaptively pass only predictors about as costly as nature's own

## Source

Dwork, Kim, Reingold, Rothblum and Yona (2021), [LIT-1068](../literature.d/LIT-1068.md) (arXiv 2011.13426v1),
read in [NOTE-885](../notes.d/NOTE-885.md): Definitions 2.3 and 2.4, Proposition 2.5, Theorems 5.2 and 5.4,
§6 (Definition 6.2, Theorem 6.4 with Claims 6.5–6.6, Theorem 6.7, Corollaries
6.9 and 6.11). The proofs of Claims 6.5–6.6 were followed line by line; that of
Proposition 6.3 for structure only; Theorems 6.8 and 6.10 are imported from
Goldreich–Rothblum 2018 and Trevisan–Vadhan 2007 and were taken as cited.

## What was actually shown

**Two access levels.** A sample-access distinguisher sees an individual, an
outcome and the prediction for that individual. An oracle-access distinguisher
sees the individual and outcome and may query the predictor on any individual,
adaptively. Oracle access simulates sample access with one query.

**The upper side.** Against size-s sample-access distinguishers an
outcome-indistinguishable (OI) predictor of size O(s/ε²) exists, whatever
nature is (Theorem 5.2; [THEORY-349](THEORY-349.md)). Against (s, q)-oracle circuits the
construction gives s · q^{O(1/ε²)} (Theorem 5.4).

**The lower side (§6).** Theorem 6.4 takes an ensemble of Boolean functions
with "scalable hardness": each harder than the last, a downward
self-reduction, and a worst-to-average-case random self-reduction. Nature puts
these on disjoint blocks. Distinguisher A_i checks an outcome on block i by
running the downward self-reduction and answering its queries from the
predictor on block i−1. By induction, OI against A_1, …, A_i forces the rounded
predictor to agree with f_i on at least 94% of block i, so any predictor much
faster than the hardest function fails. Instantiated:

- **Clique counting (Corollary 6.9).** If k-clique counting has no
  o(ℓ_cc(k, n))-time randomized algorithm, there are m distinguishers running
  in Õ(n³) such that no predictor running in time ℓ_cc(m, n)·log^{−ω(1)}(n) is
  (A, 1/(100m))-oracle-access-OI.
- **BPP ≠ PSPACE (Corollary 6.11).** Nature is computable only in exp(poly(n))
  time, the distinguishers are poly(n) in number and time, ε is polynomially
  small, and no poly(n)-time predictor is OI.

**Adaptivity is what matters.** Proposition 2.5: oracle use that is non-adaptive
preprocessing, summarised in t advice bits, is simulated by 2^t·|A|
sample-access distinguishers of the same size. In the paper's words, "the power
of oracle-access distinguishers over sample-access distinguishers derives from
the ability to query p̃ adaptively, based on the sample in question."

**What could have come out otherwise.** A predictor polynomial in the
distinguishers' size and 1/ε could have existed at every level, as it does at
the lower two. Under the stated assumptions it does not at the oracle level, and
so not at the code level either, which can simulate oracle access.

## What this does not say

- **That the separation is unconditional.** It rests on fine-grained hardness of
  clique counting or on BPP ≠ PSPACE. Without them the lower bounds fall.
- **That the gap is a single clean bound.** The upper and lower bounds are in
  different parameterisations; the paper reconciles them only informally, ruling
  out OI predictors "of (uniform) size significantly smaller than" d^{Ω(1/ε)}.
  The introduction's statement of the clique result differs in form from
  Corollary 6.9, and its proof sketch cites Theorem 6.4 where Theorem 6.7 is
  meant (a slip in v1).
- **That bounded observers in general force expensive models.** The witnesses are
  constructed natures and constructed distinguishers built from self-reducible
  hard problems. Nothing shows that observers of any natural system have this
  power.
- **That an auditor should have query access.** The paper draws that
  recommendation; the theorem is about what such access can force, not about
  what audits ought to be.
- **Anything about multi-sample tests.** The results are for single-sample
  distinguishers; multi-sample OI is left mostly to future work.
- **Anything about human observers or signal detection.** Neither appears.

## Connections

- [QUESTION-104](../questions.d/QUESTION-104.md) presumes a bounded observer can settle for a cheap coarse model.
  This holds at the sample level ([THEORY-349](THEORY-349.md)) and fails, under the assumptions,
  at the oracle level, so an answer must state the observer's access as well as
  its budget.
- [QUESTION-103](../questions.d/QUESTION-103.md): a bounded-observer account with one budget parameter leaves out
  access; two observers of the same size differ in power by it.
- [CLAIM-302](../claims.d/CLAIM-302.md) coarsens what feasible tests can tell apart; this result shows that
  the coarsening an observer enjoys can vanish once it can query the model.
