---
status: Active
title: "For a network linearised at its initial parameters, with an isotropic Gaussian prior of precision α on the parameter displacement and Gaussian noise of precision β, the log-determinant part of the evidence is −½ Σ log(1 + βλ/α) over the non-zero eigenvalues λ of the empirical neural tangent kernel's Gram matrix on the training inputs, so at most n directions are priced however many parameters the network has"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed from THEORY-080 under ADR-032 (promotion audit, batches 036 and
    046). THEORY-080's summary calls its derivation "the filer's synthesis,
    stated by no source": MacKay's evidence for linear-in-parameters models
    has no tangent kernel, and the kernel papers say nothing of evidence.
    A result the record itself proves belongs in a CLAIM, as THEORY-005's
    became CLAIM-370. The proof below is self-contained given MacKay's
    Eq. 20, so the claim is filed Active, demonstrated. THEORY-080 keeps the
    spherical, per-harmonic account, which rests on a Gram-spectrum
    approximation the record holds no source for, and stays Proposed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: a network linearised at θ0, with prior
  θ − θ0 ~ N(0, α⁻¹I) and Gaussian noise of precision β, whose log evidence
  has a log-determinant part other than −½ Σ log(1 + βλ/α) over the
  non-zero eigenvalues of J Jᵀ, or in which a direction with zero
  eigenvalue is priced.
tags:
- model-comparison
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-19'
line:
- formal-apparatus
grounds:
- LIT-623
---
<!-- inactive-ok-file: THEORY-080 THEORY-087 THEORY-005 — Proposed; the account this was filed from, which keeps the spherical half, the singular-model account named in what this does not say, and the precedent named in the history; none is leaned on -->

# CLAIM-tmprruzz: For a network linearised at its initial parameters, with an isotropic Gaussian prior of precision α on the parameter displacement and Gaussian noise of precision β, the log-determinant part of the evidence is −½ Σ log(1 + βλ/α) over the non-zero eigenvalues λ of the empirical neural tangent kernel's Gram matrix on the training inputs, so at most n directions are priced however many parameters the network has

## The claim

Linearise a network with k parameters at θ0:
f(x; θ) = f(x; θ0) + J(x)(θ − θ0), with J(x) the row of parameter
gradients at x. Put a Gaussian prior θ − θ0 ~ N(0, α⁻¹I_k) on the
displacement, and let the n training targets carry independent Gaussian
noise of precision β. Write J for the n × k matrix whose rows are J(x_i),
so that J Jᵀ is the empirical neural tangent kernel's Gram matrix on the
training inputs. Then:

1. **The log-determinant part of the log evidence** is
   −½ log det(I_k + (β/α) JᵀJ) = −½ Σ_a log(1 + βλ_a/α), the sum over the
   non-zero eigenvalues λ_a of J Jᵀ.
2. **At most n directions are priced.** Directions in the null space of J
   contribute log 1 = 0, whatever k is. The number of well-determined
   parameters, γ = Σ_a βλ_a/(βλ_a + α), is likewise a function of the
   Gram spectrum alone and is at most n.

## Proof

The linearised model is MacKay's linear-in-parameters model with basis
functions the components of J(x), quadratic regulariser
E_W = ½|θ − θ0|² and quadratic misfit E_D = ½ Σ_i (y_i − f(x_i; θ))²
(MacKay, [LIT-623](../literature.d/LIT-623.md), Eqs. 7–11, read in [NOTE-471](../notes.d/NOTE-471.md)). For such a model the
posterior is Gaussian and the evidence is exact. MacKay's log evidence
(Eq. 20) is

log P(D | α, β) = −αE_W^MP − βE_D^MP − ½ log det A − log Z_W(α)
− log Z_D(β) + (k/2) log 2π,

with A = αI_k + βJᵀJ, the Hessian of αE_W + βE_D.

(1) With Z_W(α) = (2π/α)^(k/2), the three terms −½ log det A − log Z_W(α)
+ (k/2) log 2π sum to −½ log det A + (k/2) log α = −½ log det(A/α)
= −½ log det(I_k + (β/α)JᵀJ). JᵀJ is symmetric positive semidefinite, so
the determinant is the product of 1 + (β/α)µ over its eigenvalues µ.

(2) JᵀJ (k × k) and J Jᵀ (n × n) have the same non-zero eigenvalues with
the same multiplicities, by the singular value decomposition of J. The
remaining eigenvalues of JᵀJ are zero and contribute log 1 = 0. So the sum
runs over the at most n non-zero eigenvalues of J Jᵀ. γ (MacKay, Eq. 23)
is a sum of βλ_a/(βλ_a + α) over the same eigenvalues, each term in [0, 1),
so γ < n.

## What it does not say

- **Anything about the network itself.** The network may be singular, and
  its evidence governed by a learning coefficient ([THEORY-087](../theory.d/THEORY-087.md));
  linearisation removes that question.
- **What the Gram spectrum is.** That the eigenvalues on uniform spherical
  data are close to nµ_k with multiplicity N(d, k), and so the per-harmonic
  schedule, is [THEORY-080](../theory.d/THEORY-080.md)'s account, which stays Proposed.
- **That the evidence picks good networks.** MacKay's own §6 lists reasons
  evidence and test error can disagree.
- **That a source states it.** MacKay has no tangent kernel; the kernel
  papers have no evidence.
