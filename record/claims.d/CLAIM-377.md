---
number: 377
status: Active
formerly:
- CLAIM-tmp2qr6a
title: 'For any differentiable model under squared loss with Gaussian noise of precision β, the model''s Fisher on n inputs is the Gauss–Newton matrix βJᵀJ, and its non-zero eigenvalues are exactly β times those of the empirical NTK Gram matrix JJᵀ, with the same multiplicities, its eigenvectors being Jᵀ applied to the Gram matrix''s, normalized'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-084 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-084.yaml, batch 010, ADR-047).
    Step 1 of THEORY-084 is linear algebra, the record's own, as its summary
    and NOTE-475 say, and a result the record proves is a CLAIM (ADR-032).
    The proof is written out below. THEORY-084 keeps the block inheritance
    and the threshold claim, Proposed, and cites this claim for Step 1.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a matrix J whose JᵀJ and JJᵀ differ in a
  non-zero eigenvalue or its multiplicity, or a model under a Gaussian
  likelihood of precision β whose Fisher on n inputs is not βJᵀJ.
tags:
- information-geometry
- learning-theory
- mathematics
date: '2026-10-19'
line: formal-apparatus
summary: >-
  [THEORY-084](../theory.d/THEORY-084.md)'s Step 1, stated as the record's own and proved. Through the
  SVD J = UΣVᵀ, JᵀJ and JJᵀ share the non-zero eigenvalues σ_i² with equal
  multiplicities, and Jᵀu/σ is the eigenvector of JᵀJ for a unit
  eigenvector u of JJᵀ. Under y | x ~ N(f(x; θ), β⁻¹), the expected outer
  product of the score is β∇f∇fᵀ, which summed over inputs is βJᵀJ, the
  Gauss–Newton matrix. "Fisher" means the model's Fisher, not the
  empirical Fisher of observed residuals. It holds at every width, in
  every regime and on any data. It says nothing about what the spectrum
  looks like, which is [THEORY-084](../theory.d/THEORY-084.md)'s.
---
<!-- inactive-ok-file: THEORY-084 — Proposed; the account this step was split from and that cites it, cited as open -->

# CLAIM-377: For any differentiable model under squared loss with Gaussian noise of precision β, the model's Fisher on n inputs is the Gauss–Newton matrix βJᵀJ, and its non-zero eigenvalues are exactly β times those of the empirical NTK Gram matrix JJᵀ, with the same multiplicities, its eigenvectors being Jᵀ applied to the Gram matrix's, normalized

## The claim

Let f(x; θ) be differentiable in θ ∈ ℝ^p, and let J be the n × p matrix
whose rows are ∇_θ f(x_i; θ) at the n inputs. JJᵀ is the empirical NTK Gram
matrix, (JJᵀ)_ij = ∇f(x_i) · ∇f(x_j). Model the outputs as
y | x ~ N(f(x; θ), β⁻¹).

1. **The Fisher is βJᵀJ.** The model's Fisher on the n inputs is βJᵀJ,
   which is the Gauss–Newton matrix of the squared loss weighted by β, up
   to the 1/n convention.
2. **Shared spectrum.** JᵀJ and JJᵀ have the same non-zero eigenvalues with
   the same multiplicities.
3. **Eigenvectors.** If u is a unit eigenvector of JJᵀ with eigenvalue
   σ² > 0, then Jᵀu/σ is a unit eigenvector of JᵀJ with the same
   eigenvalue.

So the non-zero Fisher spectrum is β times the empirical NTK spectrum.

## Proof

(1) The log-likelihood of one observation is
−(β/2)(y − f(x; θ))² + const, so the score is β(y − f)∇f. Its expected outer
product under the model is β²E[(y − f)²]∇f∇fᵀ = β∇f∇fᵀ, since
E[(y − f)²] = β⁻¹. Summed over the n inputs this is βJᵀJ. The Gauss–Newton
matrix of the loss (β/2)Σ_i (y_i − f(x_i))² is also βJᵀJ. With k outputs, J
stacks nk rows and the argument is unchanged.

(2) Let J = UΣVᵀ be a singular value decomposition, with rank r. Then
JᵀJ = VΣᵀΣVᵀ and JJᵀ = UΣΣᵀUᵀ, whose non-zero eigenvalues are both
σ₁², …, σ_r², with equal multiplicities.

(3) JᵀJ(Jᵀu) = Jᵀ(JJᵀu) = σ²Jᵀu, and ‖Jᵀu‖² = uᵀJJᵀu = σ², so Jᵀu/σ has
unit norm.

## What it does not say

- **That "Fisher" is the empirical Fisher.** It is the model's Fisher under
  the Gaussian likelihood. The empirical Fisher, built from observed
  residuals, differs from it away from the optimum.
- **What the spectrum looks like.** That the lazy-regime spectrum of a ReLU
  network on spherical data inherits the NTK's harmonic-degree blocks, and
  where a threshold on it is well posed, is [THEORY-084](../theory.d/THEORY-084.md)'s, Proposed.
- **Anything for cross-entropy.** There the Gauss–Newton matrix is JᵀΛJ,
  and the identity holds for Λ^(1/2)J instead.
