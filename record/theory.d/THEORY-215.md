---
number: 215
status: Active
formerly:
- THEORY-tmp4cyrt
title: 'A Hawkes process with a Lipschitz rate function and signed kernels has a unique stationary regime, which suitably started versions approach, when the Lipschitz-weighted absolute kernel mass is below one (a spectral radius below one, for a network) or when the rate is bounded'
version: 1
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-13'
source:
- LIT-1035
summary: >-
  Brémaud and Massoulié (1996), [LIT-1035](../literature.d/LIT-1035.md), read in [NOTE-728](../notes.d/NOTE-728.md):
  Theorems 1, 2, 7 and 8, proved. Inhibition is allowed because the
  conditions use |h|. The conditions are sufficient, not necessary; the
  kernels are fixed in time; uniqueness is among solutions with finite
  mean intensity. In the linear excitatory case the condition is the
  branching ratio below one, but in the nonlinear signed case the
  spectral-radius quantity is a bound, not a branching ratio, and a
  bounded rate needs no bound on the kernels at all. Nothing is proved
  about cascade sizes or about what happens past the threshold.
answers:
- QUESTION-091
---
<!-- inactive-ok-file: LIT-1036 LIT-1028 — Unavailable, no lawful full text found; the linear results generalized here, as the source describes them -->
<!-- inactive-ok-file: QUESTION-091 CLAIM-163 CLAIM-286 — Proposed or open; the codes this result bears on, not settled by it -->

# THEORY-215: A Hawkes process with a Lipschitz rate function and signed kernels has a unique stationary regime, which suitably started versions approach, when the Lipschitz-weighted absolute kernel mass is below one (a spectral radius below one, for a network) or when the rate is bounded

## Source

Brémaud and Massoulié (1996), [LIT-1035](../literature.d/LIT-1035.md), read in [NOTE-728](../notes.d/NOTE-728.md):
Theorems 1 and 2 (one process), 7 and 8 (networks), with Remarks 6 and 7.
Active because these are proved theorems.

## What was actually shown

The process has intensity λ_i(t) = φ_i(Σ_j ∫_(−∞,t) h_ji(t−s) N_j(ds)), with
φ_i ≥ 0 and kernels h_ji of either sign, fixed in time.

**What each theorem assumes, and gives.**

| result | rate function φ | kernels h | size condition | gives |
|---|---|---|---|---|
| Theorem 1 | α-Lipschitz, unbounded allowed | signed | α∫\|h\| < 1 | unique stationary law (finite mean intensity); stable in distribution; in variation if also ∫t\|h\| < ∞ |
| Theorem 7 | α_i-Lipschitz | signed, K × K | spectral radius of A, a_ij = α_i∫\|h_ji\|, below 1 | the same, for networks |
| Theorem 2 | α-Lipschitz and bounded | signed, integrable, ∫t\|h\| < ∞ | none | unique stationary law; stable in variation |
| Theorem 8 | α_i-Lipschitz and bounded | signed, integrable, ∫t\|h_ij\| < ∞ | none | the same, for networks |

Stability is convergence of a process started from a given past to the
stationary one. It holds from any past whose direct influence on the future
vanishes, in a stated sense, not only from an empty past. The proofs use
Poisson embedding, a Picard-style iteration that contracts under the size
condition, and coupling.

**The linear excitatory case.** With φ(x) = ν + x, ν > 0, and h ≥ 0,
Theorem 1's condition is ∫h < 1, the branching ratio below one. This is the
Hawkes–Oakes setting, and the paper calls Theorem 1 "a strict
generalization" of their result. Remark 6 adds that with no immigrant rate
(ν = 0) and ∫h < 1, the only stationary solution is the empty one.

**Weaker results nearby.** Under monotone dynamics without a Lipschitz
condition (Theorem 4, excitatory only), and for sign-structured networks
with bounded nondecreasing rates (Theorem 6, two components), a stationary
law exists, and its uniqueness is left open (Remark 7).

## What this does not say

- **It is not a threshold.** Every condition is sufficient. Nothing is
  proved at or past spectral radius one, and nothing says the process
  explodes or changes regime there. When excitation and inhibition offset,
  the |h| bound can be far from sharp.
- **The spectral radius here is not a branching ratio** outside the linear
  excitatory case. The paper says the branching argument is "not
  available in the generality we have placed the problem", and inhibition
  enters the bound through |h|, adding to it. Reading the quantity as how
  far cascades travel imports the linear picture into a model it was not
  proved for.
- **A bounded rate has no critical point.** Theorems 2 and 8 hold for any
  kernel size. A model whose processes saturate is stable whatever the
  allocation of influence, as far as these theorems go.
- **It says nothing about cascade sizes**, the spectrum (Hawkes 1971,
  [LIT-1036](../literature.d/LIT-1036.md), unread), or estimation.
- **Fixed kernels only.** Kernels that change with time or with the
  process's own state are not covered.

## Bearing on the record

- **[QUESTION-091](../questions.d/QUESTION-091.md) (answers, in part).** The question's formal premise
  is that a branching ratio measures how far cascades propagate. This
  result says where that premise holds and where it stops. For linear
  excitatory processes the branching ratio is the stability margin. For
  the exchange's signed, nonlinear model, a spectral radius below one is
  enough for a single stable regime, but its distance from one measures
  nothing proved, and with saturating rates there is no criticality to be
  near. The empirical half, whether influence allocation moves cascade
  sizes, is untouched; and the influence-dependent kernels the question
  is about are outside the theorem.
- **[CLAIM-163](../claims.d/CLAIM-163.md) (no relation).** A multivariate Hawkes model has an explicit
  coupling, the kernels. The spectral radius is a control parameter built
  from them, not an order parameter, which is a collective variable of
  the state. The paper proves nothing about transitions. So it supplies one
  of [CLAIM-163](../claims.d/CLAIM-163.md)'s three parts outright, a candidate control parameter for a
  second, and nothing for the third, and it does so for cascades of
  events, not for an agent's valuations. It neither supports nor weakens
  the objection, which is about valuations.
- **[CLAIM-286](../claims.d/CLAIM-286.md) (no relation).** Theorems 6 and 7 show some signed,
  many-process models are well posed. That is a precondition for the
  thesis's model, not evidence for it. Where these theorems give
  uniqueness, one parameter setting has one stationary regime, so regimes
  in that thesis's sense would need parameter change or the non-unique
  cases Remark 7 leaves open.
