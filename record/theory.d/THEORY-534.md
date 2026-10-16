---
number: 534
status: Active
formerly:
- THEORY-tmph943x
title: "The optimality of maximum likelihood was never one theorem: each historical proof holds under conditions its author left implicit, and of the classical counterexamples the practically important one is a parameter count growing with the sample, while Hodges-type superefficiency is confined to a set of measure zero"
version: 1
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-044
summary: >-
  Stigler (2007), [LIT-044](../literature.d/LIT-044.md), read in full in [NOTE-074](../notes.d/NOTE-074.md). Fisher's 1922 proof
  rests on sufficiency, his 1925 proof on exact normality, and his
  private 1930 proof on multinomial data and smooth degree-0 estimators.
  Rigorous treatments (Wald 1943, Cramér 1946) came at the cost of
  unwieldy conditions. Neyman–Scott, where the MLE of σ² tends to σ²/2,
  is the failure Stigler weighs as practical; Hodges's superefficiency is
  possible only on a Lebesgue-null set (Le Cam 1953). It is a history:
  the theorem statements are reconstructions, and it says nothing about
  modern overparameterized models beyond one hedged warning.
---

# THEORY-534: The optimality of maximum likelihood was never one theorem: each historical proof holds under conditions its author left implicit, and of the classical counterexamples the practically important one is a parameter count growing with the sample, while Hodges-type superefficiency is confined to a set of measure zero

## Source

Stigler (2007), "The Epic Story of Maximum Likelihood", *Statistical
Science* 22(4), [LIT-044](../literature.d/LIT-044.md), read in full in [NOTE-074](../notes.d/NOTE-074.md), with Appendices 1–3.
The archival letters are Stigler's account; the reading did not consult
them directly.

## What was actually shown

**Three proofs, three sets of conditions.**

- *1922 (§5).* If T is sufficient and (S, T) are exactly bivariate normal
  with common mean θ, then σ_T ≤ σ_S, so "sufficiency implies
  optimality". Fisher's 1921 abstract had claimed that ML statistics "are
  always sufficient statistics"; the claim was dropped from the published
  paper, and it is false.
- *1925 (§7).* Var X = E[Var(X|T)] + Var[E(X|T)] gives the information
  inequality V ≥ 1/I(θ). The reconstruction treats approximate normality
  as exact and needs a likelihood regular enough to differentiate under
  the integral. The reading checked the algebra.
- *1930 (§10, Appendix 2).* Sent privately to Hotelling. For a
  multinomial model and a smooth estimator homogeneous of degree 0,
  minimising the asymptotic variance under consistency by Lagrange
  multipliers gives the ML estimating equation. The reading checked the
  Lagrangian argument by hand. Stigler calls it "elegant, geometric, and
  I believe also correct, or at least completable", and it was published
  only in disguised form (1935, 1938, 1956).

**Rigour came late (§11).** Doob (1934, 1936) and Dugué (1937) erred.
Wald (1943, 1949) and Cramér (1946) gave the first satisfactory
treatments, and Wald's 1943 conditions excluded even estimating a normal
standard deviation.

**The counterexamples, weighed (§12).**

- *Growing parameters.* Wald's 1938 letter to Neyman, published as
  Neyman & Scott (1948): X_ij ~ N(µ_j, σ²), i = 1, 2, whose MLE of σ²
  converges to σ²/2. Stigler calls it "of more practical import", a
  warning for "modern highly parameterized problems, where the
  information in the data may be spread too thinly to achieve asymptotic
  consistency".
- *Superefficiency.* Hodges's T_n has asymptotic variance α² at θ = 0 and
  1 elsewhere. Le Cam (1953) proved such sets have Lebesgue measure zero.
  Stigler calls it "an ingenious but minor technical achievement".
- *Unbounded likelihoods.* The normal mixture, "at least computational"
  in importance.

What could have come out otherwise: the 1930 proof could have failed the
reader's hand check, and the archive could have shown Fisher aware of a
general proof. Neither happened.

## What this does not say

- **That maximum likelihood is unjustified.** Each proof holds under its
  conditions, and later theory (Wald, Cramér, Le Cam) supplies them. The
  account is about where the guarantee comes from, not whether one
  exists.
- **That the conditions are now settled.** Coverage stops at Le Cam 1953.
  Local asymptotic normality and the convolution and minimax theorems are
  not discussed ([NOTE-074](../notes.d/NOTE-074.md), Limitations). For the conditions themselves,
  read Wald, Cramér, Le Cam or van der Vaart, as Stigler says.
- **That cross-entropy training of neural networks inherits or loses
  classical guarantees.** The Neyman–Scott remark is a historian's
  sentence, not a result about any modern model.
- **That Fisher's proofs are all defensible as stated.** Stigler's own
  defence "flirts with tautology" (§14), and the reading rates it weak.
- **That ML's useful scope exceeds any proof.** Stigler hedges this
  ("Perhaps"); it is not a finding.

## Connections

- Barnett & Bossomaier's transfer-entropy χ² result ([LIT-048](../literature.d/LIT-048.md),
  [THEORY-641](THEORY-641.md)) imports Wald (1943), the paper Stigler names as the
  rigorous completion with restrictive conditions, and its finite-state
  parameter count grows as a^k b^k. Both links are the reader's, made in
  [NOTE-074](../notes.d/NOTE-074.md) and [NOTE-053](../notes.d/NOTE-053.md).
- Hotelling's 1929 parameter-space metric (Appendix 3) is the Fisher
  information metric, two decades before Rao. The record's
  information-geometry holdings may want it as history.
