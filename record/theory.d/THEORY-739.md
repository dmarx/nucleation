---
number: 739
status: Active
formerly:
- THEORY-tmpppb1u
title: 'For the quartic proxy of word2vec with tied weights, symmetric reweighting and constant weights, the rank-d minimisers are the top d eigenvectors of the relative deviation-from-independence matrix M*, scaled by the square roots of their eigenvalues, up to rotation; and from an initialisation aligned with those eigenvectors, gradient flow acquires each one in an independent logistic rise, in order of eigenvalue'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-182 and filed Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-182 (batch 024,
    ADR-047). THEORY-182 joined this proved result to a derivation from
    random initialisation that drops couplings, and to an empirical match
    with word2vec. This THEORY holds the proved part, LIT-855's Theorem 1
    and Proposition 2, which NOTE-660 followed step by step. It was
    re-derived for the split, written out below (ADR-047 v2). THEORY-182
    keeps the rest and extends this one.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-19'
source:
- LIT-855
summary: >-
  Karkada, Simon, Bahri and DeWeese (2025), [LIT-855](../literature.d/LIT-855.md), Theorem 1 and
  Proposition 2, read in [NOTE-660](../notes.d/NOTE-660.md) and re-derived here. The quartic proxy
  is a function of WWᵀ alone, so von Neumann's trace inequality gives its
  rank-d minimisers. Gradient flow from an aligned start keeps the
  eigenbasis and reduces each mode to a logistic equation. It does not say
  that word2vec, or the proxy from random initialisation, behaves this
  way; that is [THEORY-182](THEORY-182.md)'s.
extended_by:
- THEORY-182
---
<!-- inactive-ok-file: THEORY-182 — Proposed; the account this core was split from and that extends it, cited as open -->

# THEORY-739: For the quartic proxy of word2vec with tied weights, symmetric reweighting and constant weights, the rank-d minimisers are the top d eigenvectors of the relative deviation-from-independence matrix M*, scaled by the square roots of their eigenvalues, up to rotation; and from an initialisation aligned with those eigenvectors, gradient flow acquires each one in an independent logistic rise, in order of eigenvalue

## Source

Karkada, Simon, Bahri and DeWeese (2025), [LIT-855](../literature.d/LIT-855.md), Theorem 1 and
Proposition 2, with Lemma 3.1, as read in [NOTE-660](../notes.d/NOTE-660.md), whose reader followed
the proofs step by step. Re-derived here as a check.

## What was actually shown

The quartic expansion of the skip-gram negative-sampling loss, with the two
embedding matrices tied, symmetric reweightings and constant weights
G_ij = c, is L(W) = (c/4)‖WWᵀ − M*‖²_F + const, where
M*_ij = (Ψ⁺P_ij − Ψ⁻P_iP_j) / (½(Ψ⁺P_ij + Ψ⁻P_iP_j)).

- **The minimisers.** L depends on W only through X = WWᵀ, which is
  positive semi-definite of rank at most d. Write M* = Σ λ_i v_i v_iᵀ with
  λ₁ ≥ λ₂ ≥ …, and let X have eigenvalues μ₁ ≥ … ≥ μ_d ≥ 0. Then
  ‖X − M*‖² = Σ μ_i² − 2 tr(XM*) + ‖M*‖². Von Neumann's trace inequality
  gives tr(XM*) ≤ Σ_{i≤d} μ_i λ_i, with equality when X shares M*'s top
  eigenvectors. So ‖X − M*‖² ≥ ‖M*‖² + Σ_{i≤d} (μ_i² − 2μ_iλ_i), and each
  term is least, over μ_i ≥ 0, at μ_i = max(λ_i, 0). The minimum is
  X = Σ_{i≤d} max(λ_i, 0) v_i v_iᵀ, unique when λ_d > λ_{d+1}. When the top
  d eigenvalues are positive, W = V_d Λ_d^{1/2} R for any orthogonal R.
- **The aligned dynamics.** Gradient flow is Ẇ = −c(WWᵀ − M*)W. If
  W(0) = V_d S(0) with S(0) diagonal, then W(t) = V_d S(t) solves it, with
  ṡ_k = c(λ_k − s_k²)s_k. For u_k = s_k² this is u̇_k = 2c u_k(λ_k − u_k), so
  u_k(t) = λ_k / (1 + (λ_k/u_k(0) − 1) e^{−2cλ_k t}). Mode k reaches half
  its final strength at t_k = (1/(2cλ_k)) ln(λ_k/u_k(0) − 1) and rises over
  a time of order 1/(cλ_k). As the initial scale shrinks, the modes arrive
  one at a time, in order of eigenvalue.

What could have failed: a loss that sees the two embedding matrices
separately, or weights G_ij that vary, would not reduce to a function of
WWᵀ alone, and the trace argument would not apply.

## What this does not say

- **Not from random initialisation.** That a vanishing random start first
  aligns with the eigenbasis and then follows these steps is [LIT-855](../literature.d/LIT-855.md)'s
  Result 3, derived with couplings dropped and not proved. It stays with
  [THEORY-182](THEORY-182.md).
- **Not that word2vec factorises M\*.** Word2vec unties the matrices and
  uses an asymmetric negative sampling. That it behaves like the proxy is
  an empirical match, also [THEORY-182](THEORY-182.md)'s.
- **Not unique embedding directions.** The loss sees only WWᵀ, so any
  rotation R is equally optimal.
