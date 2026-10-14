---
number: 248
status: Proposed
formerly:
- THEORY-tmp7xiz6
promote_when: >-
  A bound of this form, R_E(ε) or the rate-distortion function of the
  output's law, is evaluated for an algorithm whose I(S;W) is infinite,
  such as deterministic training of a network with continuous weights,
  and gives a non-trivial value, with distortion measured in the units
  the Lipschitz condition uses. The theorem itself is proved, by
  Xu–Raginsky's bound applied to a surrogate, so a counterexample to it
  would refute the account outright. What cannot settle it: correlations
  between estimated compressibility and test error across training
  settings, since they do not show that the bound holds or is tight.
title: "The expected generalisation error of a learning algorithm is at most √(2σ²R/n) + ε, where R is the least information about the sample carried by any surrogate output whose expected generalisation error is within ε; I(S;W) is the lossless case, and the lossy bound stays finite where I(S;W) is infinite"
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-14'
source:
- LIT-236
summary: >-
  Sefidgaran, Gohari, Richard & Şimşekli (COLT 2022), [LIT-236](../literature.d/LIT-236.md), read in
  [NOTE-780](../notes.d/NOTE-780.md). Theorem 4: |E gen| ≤ √(2σ²·R_E(ε)/n) + ε, where R_E(ε)
  is the least I(S;Ŵ) over surrogates within ε in expected generalisation
  error. For a Lipschitz loss R_E is bounded by the rate-distortion
  function of P_W (Corollary 6). Theorem 10 is a tail version over a KL
  ball. The block-coding meaning is proved for finite alphabets only. No
  bound is evaluated for a learned model, and every bound depends on the
  unknown data distribution.
---
<!-- inactive-ok-file: THEORY-238 THEORY-263 — Proposed; the account of a related block-coding bound for representations, and the data-dependent successor filed today, cited for context -->

# THEORY-248: The expected generalisation error of a learning algorithm is at most √(2σ²R/n) + ε, where R is the least information about the sample carried by any surrogate output whose expected generalisation error is within ε; I(S;W) is the lossless case, and the lossy bound stays finite where I(S;W) is infinite

## Source

Sefidgaran, Gohari, Richard & Şimşekli (2022), [LIT-236](../literature.d/LIT-236.md), read in full in
[NOTE-780](../notes.d/NOTE-780.md): Definitions 1 and 8, Theorems 2–4, 9 and 10, Corollaries
5–7, 11 and 26, Appendix D.2, and proofs E.1–E.6.

## What was actually shown

**The bound.** For a σ-subgaussian loss and any algorithm P_{W|S},

|E gen(S, W)| ≤ √(2σ²·R_E(ε)/n) + ε,  R_E(ε) = inf I(S; Ŵ) subject to
|E[gen(S, W) − gen(S, Ŵ)]| ≤ ε,

with the infimum over Markov kernels P_{Ŵ|S} (Theorem 4, eq. 9). For
general spaces the proof (App. E.3) applies Xu and Raginsky's Theorem 1
([LIT-347](../literature.d/LIT-347.md)) to the surrogate Ŵ and adds ε by the triangle inequality. At
ε = 0 with Ŵ = W it is Xu and Raginsky's bound (Corollary 5).

**Why it is called compression.** For finite S and W, Theorems 2 and 3
show that R_E(ε) is an achievable rate for a block code. Take m
independent experiments (S_i, W_i). A book of e^{mR} candidate output
blocks can, with probability tending to 1, hold one whose average
generalisation error is within ε of the true block's. A union bound over
the book then gives √(2σ²R/n) + ε. On this reading I(S;W) is the
lossless compression rate of the algorithm, not only "dataset
dependency" (§1).

**Lossy and Lipschitz.** If |ℓ(z, w) − ℓ(z, ŵ)| ≤ L·ρ(w, ŵ), then |E gen| ≤
√(2σ²·RD(ε/(2L); P_W, ρ)/n) + ε, with RD the rate-distortion function of
the output's marginal law (Corollary 6). The step is to impose
Ŵ – W – S, so that I(S; Ŵ) ≤ I(W; Ŵ). This is finite for continuous W
with I(S;W) = ∞. As ε → 0 it becomes √(4σ²·dim_R(P_W)·log(nL²)/n),
under a uniform-convergence assumption (Corollary 7).

**Tail.** With probability ≥ 1 − δ, gen(S, W) ≤ √(2σ²(R_p(δ, ε) +
log(1/δ))/n) + ε, where R_p is the supremum of the rate-distortion
quantity over all laws within KL log(1/δ) of P_{S,W} (Theorem 10).

What could have failed: the bound needs the surrogate to match only the
expected generalisation error of W, not W itself. A bound that needed Ŵ
close to W in parameters would have tied the rate to the parameter
dimension. Here that enters only through the Lipschitz corollaries.

## What this does not say

- **Not that it is computable.** R_E(ε) and RD(ε; P_W) depend on the
  unknown data distribution, through P_{S,W} or P_W. [LIT-233](../literature.d/LIT-233.md) calls these
  bounds data-independent for that reason.
- **Not that it is non-vacuous for networks.** No bound is evaluated for
  a learned model. The one analytic example, a Gaussian mean, plugs the
  squared-error rate-distortion function into a Lipschitz condition on
  the unsquared norm. Its d/n rate is therefore unsupported. With
  consistent units it is of order √(d/n), up to a logarithm.
- **Not a compression of a model.** The rate is of a code for the
  algorithm's outputs over many independent training sets. It is not the
  description length of the one network trained, and not a Kolmogorov
  complexity.
- **Not a new information inequality in general spaces.** Outside finite
  alphabets the bound is Xu–Raginsky applied to a surrogate. The
  source-coding reading is proved only for finite S and W.
- **Not that the tail bound improves on Hoeffding.** For S and W
  independent, Theorem 10 can be worse, because I_Q(S;W) need not vanish
  on the KL ball (App. D.2).
- **Not that the rate-distortion dimension controls generalisation in
  general.** Corollary 7 assumes a uniform convergence over n that is
  not examined, while P_W changes with n.

## Connections

- **[THEORY-028](THEORY-028.md).** This is a strict generalisation of that bound's
  Xu–Raginsky half. It adds a third remedy for infinite I(S;W), beside
  quantisation and injected noise: a surrogate that keeps the expected
  generalisation error. It also adds a tail form with log(1/δ)
  dependence.
- **[LIT-233](../literature.d/LIT-233.md)** (read today, [THEORY-263](THEORY-263.md)) makes the rate vary with the
  realised sample, turning these bounds into data-dependent ones.
- **[THEORY-238](THEORY-238.md)** ([LIT-245](../literature.d/LIT-245.md)) applies a block-coding bound of the same family
  to an encoder's latents instead of the whole output.
