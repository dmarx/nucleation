---
status: Active
title: 'In a linear structural equation model whose exogenous micro-causes W₁, …, W_n drive effects Z = AW + F, with interventions that set all of W, all of Z or both, averaging each block is an exact transformation onto Ẑ = (an/m)Ŵ + F̂ if and only if every column of A sums to the same a, the column-equitability of the block of A from W to Z; the transformation is exact only for those whole-block interventions'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp6b7dr. Sufficiency is Rubenstein et al.'s
    Theorem 11, proved in their Appendix C. The coefficient an/m, the
    necessity of the column condition and the identification with
    column-equitability are the record's, re-derived below step by step,
    which meets the condition for Active under ADR-047 v2.
tags:
- causality
- mathematics
date: '2026-10-21'
source:
- LIT-tmptzsyg
- LIT-tmp6hpx6
summary: >-
  Rubenstein et al. (2017), [LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md), read in [NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md), with
  Beckers and Halpern's restatement ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), Example 3.3). Averages of
  linear micro-variables form a causally consistent macro model exactly
  when each micro-cause has the same total effect on the effect block. It
  says nothing about interventions on single micro-variables, which break
  exactness, nor about nonlinear or approximate aggregation.
---

# THEORY-tmpj5zq1: In a linear structural equation model whose exogenous micro-causes W₁, …, W_n drive effects Z = AW + F, with interventions that set all of W, all of Z or both, averaging each block is an exact transformation onto Ẑ = (an/m)Ŵ + F̂ if and only if every column of A sums to the same a, the column-equitability of the block of A from W to Z; the transformation is exact only for those whole-block interventions

## Source

Rubenstein, Weichwald, Bongers, Mooij, Janzing, Grosse-Wentrup and
Schölkopf (2017), [LIT-tmptzsyg](../literature.d/LIT-tmptzsyg.md), read in full in [NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md): Theorem 11
and its proof in Appendix C. Beckers and Halpern ([LIT-tmp6hpx6](../literature.d/LIT-tmp6hpx6.md), [NOTE-tmp1bdcu](../notes.d/NOTE-tmp1bdcu.md))
restate it as their Example 3.3, with the coefficient an/m. Exact
transformation is Rubenstein et al.'s Definition 3.

## What was actually shown

The micro model: Wᵢ = Eᵢ for i ≤ n, Z_k = Σⱼ A_kj Wⱼ + F_k for k ≤ m, with
(E, F) of any joint law, and declared interventions ∅, do(W = w), do(Z = z)
and do(W = w, Z = z) for all w ∈ ℝⁿ, z ∈ ℝᵐ. τ maps (W, Z) to
(Ŵ, Ẑ) = ((1/n)ΣWᵢ, (1/m)ΣZ_k). Write c_j = Σ_k A_kj, the column sums.

**The macro law under each intervention.** Under ∅ or do(W = w),
Ẑ = (1/m)Σ_k Σⱼ A_kj Wⱼ + F̂ = (1/m)Σⱼ c_j Wⱼ + F̂, with F̂ = (1/m)ΣF_k.

**If** c_j = a for every j, then (1/m)Σⱼ c_j Wⱼ = (a/m)ΣⱼWⱼ = (an/m)Ŵ. So the
macro SEM Ŵ = Ê, Ẑ = (an/m)Ŵ + F̂, with Ê = (1/n)ΣEᵢ and F̂ jointly distributed
as the averages are, and ω sending do(W = w) to do(Ŵ = w̄), do(Z = z) to
do(Ẑ = z̄) and the joint intervention to the joint one, reproduces the
push-forward law under every declared intervention. ω is surjective and
order-preserving (an order embedding, as the paper says). Under do(Z = z)
the macro variable Ẑ is the constant z̄ at both levels, and Ŵ keeps its law.
Checked numerically for n = 4, m = 3, a = 0.7 and a random w: the micro sum
and (an/m)w̄ agreed to machine precision, while (a/m)w̄ did not.

**Only if.** Suppose the averaging τ is exact for these interventions, with
Ê and F̂ not almost surely constant. Under do(W = w) the push-forward puts Ŵ
at the point w̄ and gives Ẑ the law of (1/m)c·w + F̂, which is not a point
mass. Under ∅ or do(Ẑ = ·) the macro model gives Ŵ the law of Ê, not a point
mass, and under a joint intervention Ẑ would be a point mass. So
ω(do(W = w)) must be do(Ŵ = w̄), and the macro law of Ẑ under it depends on
w only through w̄. Hence the law of (1/m)c·w + F̂ is the same for any two w
with the same mean. Two translates of one law are equal only if the shifts
are equal, so c·w = c·w′ whenever w̄ = w̄′, that is, c is orthogonal to every
vector whose entries sum to zero. That forces c = a·1: equal column sums.

**Column-equitability.** With Q the 2 × (n + m) matrix of block indicators,
the condition is [THEORY-755](THEORY-755.md)'s for the pair of blocks (Z, W): Σ_{k∈Z} A_kj is
the same for every j in W. The W block receives nothing and Z nothing from
itself, so every other block pair is trivially equitable.

**Why only whole-block interventions.** do(W₁ = w₁) alone leaves Ŵ with the
law of (w₁ + Σ_{j≥2}Eⱼ)/n, which is neither the point mass of a macro
intervention on Ŵ nor, unless E₁ is itself a point mass at w₁, the law of Ê.
No ω can match it, so adding it to the declared set breaks exactness. This
is the paper's general remark: "If we were to allow larger sets of
interventions 𝑋 in the SEM 𝑋, the transformations given would not be
exact."

What could have failed: the averages could have needed a condition on the
noise as well, or on rows of A. They need only the column sums, because the
noise passes through the averaging unchanged.

## What this does not say

- **Not about interventions on single micro-variables,** or on proper
  subsets of a block, which the transformation does not survive.
- **Not that the macro model predicts any one micro-variable,** or any one
  system's response given its micro state: exactness is equality of
  push-forward laws ([NOTE-tmp6b7dr](../notes.d/NOTE-tmp6b7dr.md), Bearing on the record).
- **Not about nonlinear models or approximate aggregation.** Nearly equal
  column sums give no bound here.
- **Not dynamics.** It is a one-shot SEM; [THEORY-755](THEORY-755.md) has the dynamical
  version for block sums, and Theorem 12 of the same paper treats equilibria.

## Connections

- **[THEORY-755](THEORY-755.md).** The same algebra, QA = ĀQ for a partition, as a causal
  rather than dynamical criterion. The join is the record's.
- **[THEORY-733](THEORY-733.md).** The dynamical-independence criterion LA = BL is the
  linear-map generalization of both.
- **[CLAIM-350](../claims.d/CLAIM-350.md).** Its causal bullet's "intervention-consistent
  coarse-graining for a declared family of interventions" is exact
  transformation; this is a worked instance with the declared family
  explicit.
