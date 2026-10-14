---
number: 239
status: Proposed
formerly:
- THEORY-tmp1iy33
promote_when: >-
  A second, independent derivation or a published check of Zhai's
  Theorem 3.4 and Lemma 1.4 for a general joint law of input and context
  (the dissertation is not peer-reviewed as a whole), together with one
  worked case on a single space with a non-reversible kernel, A = X and
  P⁺(a|x)P_X(x) ≠ P⁺(x|a)P_X(a), showing which of the left or right
  singular spaces carries the guarantee there. It is refuted by a joint law
  meeting the Hilbert–Schmidt assumption and 1 − ε ≤ s₁ for which some
  d-dimensional encoder not spanning the top-d left singular functions
  attains a lower worst-case approximation error on the compatible class.
  What cannot settle it: alignment scores of trained networks, or further
  symmetric examples, since the claim is about the population optimum and
  its novelty is the asymmetric case.
title: "For any joint law of an input and a context, symmetric or not, the top-d left singular functions of the conditional-expectation operator are the unique d-dimensional span minimizing worst-case linear-probe approximation error over tasks of compatibility at least 1 − ε, with error (s₁² − (1 − ε)²)/(s₁² − s²_{d+1})"
version: 1
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-10-14'
source:
- LIT-975
summary: >-
  Zhai (2025), [LIT-975](../literature.d/LIT-975.md), read in [NOTE-770](../notes.d/NOTE-770.md): Lemma 1.4, Theorem 3.2 and
  Theorem 3.4 with App. B. The operator g ↦ E[g(A)|X] runs from L²(P_A) to
  L²(P_X) and is never assumed self-adjoint; its singular value
  decomposition comes from composing it with its adjoint. The guarantee is
  for linear probes and approximation error at the population level only.
  It does not cover a non-reversible kernel on one space, which the thesis
  never works through, nor what a trained network reaches.
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-005 THEORY-009 THEORY-228 CLAIM-098 — Proposed; accounts and a claim this one bears on, open -->

# THEORY-239: For any joint law of an input and a context, symmetric or not, the top-d left singular functions of the conditional-expectation operator are the unique d-dimensional span minimizing worst-case linear-probe approximation error over tasks of compatibility at least 1 − ε, with error (s₁² − (1 − ε)²)/(s₁² − s²_{d+1})

## Source

Zhai, *Contextures: The Mechanism of Representation Learning* (CMU PhD
dissertation, 2025), [LIT-975](../literature.d/LIT-975.md), read in [NOTE-770](../notes.d/NOTE-770.md): Definition 1.1,
Lemmas 1.4–1.5, Definitions 1.7 and 3.1, Theorems 3.2 and 3.4 (proofs in
App. B.1–B.2), Theorems 2.9 and 2.11 (App. A.5–A.6).

## What was actually shown

**The operator.** For a joint law P⁺(x,a) of an input X and a context A on
possibly different spaces, (T_P⁺g)(x) = E[g(A)|x] maps L²(P_A) to L²(P_X).
Its adjoint is written out by Bayes' rule: (T_P⁺*f)(a) = E[f(X)|a]. Assuming
T_P⁺T_P⁺* and T_P⁺*T_P⁺ Hilbert–Schmidt, both are self-adjoint by
construction, share eigenvalues s_i² ∈ [0,1], and their eigenfunctions
μ_i, ν_i are linked by μ_i = s_i⁻¹T_P⁺ν_i (Lemma 1.4). The density ratio has
the expansion P⁺(x,a)/(P_X(x)P_A(a)) = Σ s_i μ_i(x)ν_i(a) (Lemma 1.5).

**The task class.** A target f is (1 − ε)-compatible when
(Σ s_i²u_i² / Σ u_i²)^(1/2) ≥ 1 − ε for f̃ = Σ u_iμ_i. Such an f is
E[g(A)|x] for a g that varies little across two context draws for the
same x: E[(g(A) − g(A′))²] ≤ 4ε‖g‖² (Theorem 3.2).

**The guarantee.** If 1 − ε ≤ s₁, then among all d-dimensional encoders in
L²(P_X), Φ minimizes the worst-case linear-probe approximation error over
the compatible class if and only if its span is that of top-d left
singular functions μ₁…μ_d, and the minimum is
(s₁² − (1 − ε)²)/(s₁² − s²_{d+1}). Every other encoder has a compatible
task with at least that error (Theorem 3.4). The proof (App. B.2) builds,
for any d-dimensional span, a unit target β₁μ₁ + β₂f₀ with f₀ in
span{μ₂, …, μ_{d+1}} that is compatible and reaches the bound, and shows
equality only when the span is that of μ₁…μ_d.

**How the span is reached.** At their population optima, the spectral
contrastive loss and the covariance-constrained non-contrastive loss give
an encoder on A spanning the top right singular functions, whose average
T_P⁺Ψ spans the left ones (Theorem 2.9); a two-encoder objective,
min E‖Φ(X) − Ψ(A)‖² with Cov[Φ] = I imposed on Φ only, reaches the left
span directly (Theorem 2.11).

What could have failed: the optimal encoder could have depended on the
context's right space, or on how the pair is symmetrized, and it does not.
Only the left singular space and the singular values enter.

## What this does not say

- **Not the directed transport of a single space.** X and A may differ,
  and the operator is not self-adjoint, but the thesis never works a case
  where A = X with a non-reversible kernel. Its only graph example
  (Example 1.13, Theorem 2.8) assumes w(u,v) = w(v,u). Whether the left
  space is still the signature for a directed chain on one space is
  inferred from the general statement, not exhibited.
- **Not about what training reaches.** All results are at the population
  optimum of squared-error objectives; the thesis sets aside optimization
  and architecture, and does not cover cross-entropy or InfoNCE.
- **Not about BYOL or SimSiam.** The two-encoder objective is asymmetric
  only in where the constraint sits. The thesis names predictor and
  stop-gradient methods but does not analyse them.
- **Not estimation error.** Theorem 3.4 bounds approximation by a linear
  probe on an exact span; finite-sample bounds (Chapter 5) depend on a
  context complexity that grows exponentially in input dimension for
  masking contexts.
- **Not a measure of a context's quality.** The thesis's claim that a
  moderate association is best is argued and tested with a heuristic
  metric that fails on some datasets; it is not part of this account.

## Connections

- **[QUESTION-052](../questions.d/QUESTION-052.md).** An answer in part, to the half that asks what replaces
  the eigenspace when the pairing is not symmetric. It is the left
  singular space of the conditional-expectation operator, and it comes with
  a sufficiency guarantee for linear decisions on compatible tasks. The
  half about directed transports on one space stays open.
- **[THEORY-009](THEORY-009.md).** It complicates that account. Self-adjointness here comes
  from composing T_P⁺ with its adjoint (X → A → X′), not from any symmetry
  of the original pair. In the multi-view case the two views are
  exchangeable because both are drawn given the same x, which is the
  symmetry [THEORY-009](THEORY-009.md) names. The adjoint is closed-form, with no Riesz. It
  is a nearer miss for [THEORY-009](THEORY-009.md)'s promote_when than [LIT-228](../literature.d/LIT-228.md), but not a
  BYOL-type objective.
- **[THEORY-007](THEORY-007.md).** The symmetric sibling: the same top span, with a
  minimax guarantee over view-invariant targets instead of compatible ones.
- **[THEORY-228](THEORY-228.md).** A different guarantee on the same object in the
  symmetric, finite case: cluster leakage over conductance rather than a
  worst case over a compatibility class.
- **[THEORY-005](THEORY-005.md).** The Hilbert–Schmidt condition is assumed here; the
  thesis's context complexity is the same χ² quantity taken pointwise.
- **[CLAIM-098](../claims.d/CLAIM-098.md).** Translation is directed; this account shows a signature
  survives an asymmetric pairing between two spaces, which is weaker than
  surviving a non-invertible transport on one.
- The training objectives themselves are ML practice and are held in the
  Anthology ([ANTH-LIT-459](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-459.md)), not here.
