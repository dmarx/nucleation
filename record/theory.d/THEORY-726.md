---
number: 726
status: Active
formerly:
- THEORY-tmpkmw55
title: 'Weight decay on factors is a nuclear-norm penalty on their product: with tied weights λ‖W‖²_F = λ‖WWᵀ‖_*, and for untied factors the least (‖U‖²_F + ‖V‖²_F)/2 over UVᵀ = M is ‖M‖_*, so for any loss that sees the weights only through the product, square-penalized training is nuclear-norm-penalized training of a product of bounded rank'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-180 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-180.yaml, batch 010, ADR-047).
    THEORY-180 already separated a proved identity (LIT-857, Appendix A)
    from a spectral law derived non-rigorously, and its promote_when tests
    only the law. This THEORY holds the identity. It was re-derived for the
    split, and the derivation is written out below (ADR-047 v2, the owner's
    rule of 2026-10-19). THEORY-180 keeps the spectral law and extends this
    one.
tags:
- learning-theory
- mathematics
date: '2026-10-19'
source:
- LIT-857
summary: >-
  Boncoraglio et al. (2025), [LIT-857](../literature.d/LIT-857.md), Appendix A, read in [NOTE-661](../notes.d/NOTE-661.md), and
  re-derived here. ‖W‖²_F = Tr(WWᵀ) = ‖WWᵀ‖_*, since a PSD matrix's
  singular values are its eigenvalues. For untied factors, Hölder's
  inequality for Schatten norms and AM–GM bound ‖M‖_* by
  (‖U‖²_F + ‖V‖²_F)/2 over every factorization UVᵀ = M, and the balanced SVD
  factorization attains it. The product's rank is bounded by the factors'
  inner dimension. It says nothing about what the trained product looks
  like, which is [THEORY-180](THEORY-180.md)'s spectral law.
extended_by:
- THEORY-180
---
<!-- inactive-ok-file: THEORY-180 — Proposed; the spectral law this identity was split from and that extends it, cited as open -->

# THEORY-726: Weight decay on factors is a nuclear-norm penalty on their product: with tied weights λ‖W‖²_F = λ‖WWᵀ‖_*, and for untied factors the least (‖U‖²_F + ‖V‖²_F)/2 over UVᵀ = M is ‖M‖_*, so for any loss that sees the weights only through the product, square-penalized training is nuclear-norm-penalized training of a product of bounded rank

## Source

Boncoraglio, Erba, Troiani, Xu, Krzakala & Zdeborová (2025), [LIT-857](../literature.d/LIT-857.md),
Appendix A, read in [NOTE-661](../notes.d/NOTE-661.md). The paper proves the identity. It is
re-derived here as a check.

## What was actually shown

- **Tied weights.** For W ∈ ℝ^(d×p), ‖W‖²_F = Tr(WWᵀ). WWᵀ is symmetric
  positive semi-definite, so its singular values are its eigenvalues and
  ‖WWᵀ‖_* = Tr(WWᵀ). So λ‖W‖²_F = λ‖WWᵀ‖_* exactly.
- **Untied factors, the bound.** For any U, V with UVᵀ = M, Hölder's
  inequality for Schatten norms gives ‖M‖_* = ‖UVᵀ‖_* ≤ ‖U‖_F ‖V‖_F, and
  AM–GM gives ‖U‖_F ‖V‖_F ≤ (‖U‖²_F + ‖V‖²_F)/2.
- **Untied factors, attained.** Let M = PΣQᵀ be a singular value
  decomposition and take U = PΣ^(1/2), V = QΣ^(1/2). Then UVᵀ = M and
  ‖U‖²_F = ‖V‖²_F = Tr Σ = ‖M‖_*. So min over UVᵀ = M of
  (‖U‖²_F + ‖V‖²_F)/2 is ‖M‖_*.
- **The consequence for training.** If the loss depends on the weights only
  through the product, minimizing loss + λ(‖U‖²_F + ‖V‖²_F)/2 over (U, V)
  is minimizing loss + λ‖M‖_* over M. With tied weights the same holds for
  the PSD map S = WWᵀ. In both cases the product's rank is at most the
  inner dimension p, so the nuclear-norm problem is over matrices of rank
  at most p.

What could have failed: a loss that depends on the factors other than
through their product, such as a nonlinearity between them. Then the
reduction does not apply.

## What this does not say

- **What the trained product looks like.** The law
  η·ReLU(S0 + δZ − εI) for the learned map is [THEORY-180](THEORY-180.md)'s. It is derived
  by replica and AMP arguments under a replicon condition checked only
  numerically, and it stays Proposed.
- **Anything for losses that see the factors separately.** Then weight
  decay is not a nuclear-norm penalty on anything.
- **That gradient methods reach the minimizer.** The identity concerns the
  objective, not the dynamics.
