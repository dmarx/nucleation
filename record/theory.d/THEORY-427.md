---
number: 427
status: Active
formerly:
- THEORY-tmp3fv4l
title: "For gradient matrices of rank at most r, the Kronecker product of the square roots of the accumulated row and column gradient second moments dominates the full-matrix AdaGrad statistic up to the factor r, so preconditioning each side of a weight matrix by a fourth root, as Shampoo does, preconditions at least as strongly as full-matrix AdaGrad and has O(√T) regret for convex Lipschitz losses"
version: 1
tags:
- information-geometry
- mathematics
date: '2026-10-16'
source:
- LIT-621
summary: >-
  Gupta, Koren and Singer (2018), [LIT-621](../literature.d/LIT-621.md), read in [NOTE-480](../notes.d/NOTE-480.md). Lemma 8 is pure
  matrix analysis (operator monotonicity of the geometric mean); Theorems
  7 and 10 give regret √(2r) D Tr(L^{1/4}) Tr(R^{1/4}), O(√T) when the
  spectral norm of the gradients is at most 1. Proved, in online convex
  optimisation, with D uncontrolled because the implementation omits the
  projection. Nothing here is a result about non-convex training; the deep
  network curves are four runs without seeds.
---
<!-- inactive-ok-file: THEORY-085 — Proposed; named to contrast a Fisher-based Kronecker structure, not leaned on -->

# THEORY-427: For gradient matrices of rank at most r, the Kronecker product of the square roots of the accumulated row and column gradient second moments dominates the full-matrix AdaGrad statistic up to the factor r, so preconditioning each side of a weight matrix by a fourth root, as Shampoo does, preconditions at least as strongly as full-matrix AdaGrad and has O(√T) regret for convex Lipschitz losses

## Source

Gupta, Koren and Singer (2018), [LIT-621](../literature.d/LIT-621.md) (ICML 2018), read in [NOTE-480](../notes.d/NOTE-480.md) from
arXiv v2: sections 1–6 and Appendix A, with the proofs of Lemmas 8–9 and
Theorem 7 followed; the tensor proofs in Appendices B and C skimmed.

## What was actually shown

**The update (Algorithm 1).** For a weight matrix W with gradients G_t,
L = εI + Σ G Gᵀ and R = εI + Σ GᵀG, and W ← W − η L^{-1/4} G R^{-1/4}.

**Lemma 9.** For G of rank at most r, with g its vectorisation,
(1/r) g gᵀ ⪯ I_m ⊗ (GᵀG) and (1/r) g gᵀ ⪯ (G Gᵀ) ⊗ I_n.

**Lemma 8.** εI_{mn} + (1/r) Σ g_t g_tᵀ ⪯
(εI_m + Σ G_t G_tᵀ)^{1/2} ⊗ (εI_n + Σ G_tᵀ G_t)^{1/2}, by the operator
monotone geometric mean of commuting PSD matrices (Ando et al.).

**Theorem 7.** Regret ≤ √(2r) D Tr(L_T^{1/4}) Tr(R_T^{1/4}). With
‖G_t‖₂ ≤ 1 and ε = 0 the traces are at most m T^{1/4} and n T^{1/4}, so
regret is O(√T). **Theorem 10** gives the same for order-k tensors, with
power −1/2k per dimension; **Theorem 13** a diagonal variant.

**What could have come out otherwise.** The Kronecker product of the two
small statistics could have failed to dominate the full statistic in some
directions, in which case the factored preconditioner would not inherit
AdaGrad's guarantee. Lemma 8 shows it dominates, up to the rank.

## What this does not say

- **That Shampoo trains deep networks better.** That evidence is four
  curves without repeated seeds; on LM1B Shampoo ran at its default while
  only the baselines were swept (C3, weak to moderate).
- **That the bound is uniform.** D, the largest distance from the optimum,
  is uncontrolled without the projection step the implementation omits.
- **That the Kronecker structure comes from the network.** Lemma 8 is pure
  matrix analysis with no statistical model of the network. Class-indexed
  Kronecker structure in a Fisher matrix ([THEORY-085](THEORY-085.md)) is structure in a
  different, model-defined object.
- **That −1/4 is the right exponent for training.** It comes from the
  analysis.
- **Anything about curvature across layers.** The preconditioner is
  block-diagonal over tensors by construction.

## Connections

- K-FAC ([LIT-622](../literature.d/LIT-622.md)) is the other factored preconditioner, contrasted in §1.2
  and not compared experimentally. The record's account of where its
  class-averaged factors go wrong is [THEORY-085](THEORY-085.md).
- Natural gradient is defined relative to the Fisher metric ([THEORY-082](THEORY-082.md));
  Shampoo's statistics are gradient second moments, not a Fisher, and its
  guarantee is a regret bound, not Fisher efficiency.
- [LIT-621](../literature.d/LIT-621.md) carries an instruction for practice and is flagged
  `anthology-candidate`; this document states only the mathematical result.
