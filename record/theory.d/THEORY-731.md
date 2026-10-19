---
number: 731
status: Active
formerly:
- THEORY-tmpuga9q
title: 'For softmax cross-entropy with balanced classes, the Gauss–Newton matrix splits exactly into four positive semidefinite second-moment terms, the class-centre term has rank at most C with eigenvectors in the span of the class centres and the spectrum of a C × C Gram matrix, and so the k-th eigenvalue of the whole is never below the k-th eigenvalue of the class-centre term'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-078 and filed Active, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/THEORY-078.yaml,
    batch 017, ADR-047). THEORY-078's title joins this exact algebra to an
    attribution measured by eye, and its promote_when concerns only the
    attribution. NOTE-479 read the derivation of Eqs. 12–28 in full. The
    derivation is written out below and checked, including both eigenvalue
    inequalities, which the paper shows only on scree plots. Under ADR-047
    v2, a step-by-step re-derivation in the decision file meets the
    condition. THEORY-078 keeps the attribution and extends this entry.
tags:
- information-geometry
- mathematics
date: '2026-10-19'
source:
- LIT-619
summary: >-
  Papyan (2019), [LIT-619](../literature.d/LIT-619.md), read in [NOTE-479](../notes.d/NOTE-479.md). Exact algebra, re-derived here.
  For softmax cross-entropy, the Gauss–Newton matrix is G = (1/n)ΔΔᵀ, an
  uncentred second moment of logit derivatives indexed by class and logit.
  Grouping them gives G = G₀ + G₁ + G₂ + G₃, with every term positive
  semidefinite. G₁, the class-centre term, has rank at most C, and its
  spectrum is read from a C × C Gram matrix. So λ_k(G) ≥ λ_k(G₁ + G₂) ≥
  λ_k(G₁) for every k, in any network, trained or not. That G₁ carries the
  outliers of trained networks is measured, not derived, and stays
  Proposed in [THEORY-078](THEORY-078.md).
extended_by:
- THEORY-078
---
<!-- inactive-ok-file: THEORY-078 — Proposed; the measured attribution this was split from and that extends it, cited as open -->

# THEORY-731: For softmax cross-entropy with balanced classes, the Gauss–Newton matrix splits exactly into four positive semidefinite second-moment terms, the class-centre term has rank at most C with eigenvectors in the span of the class centres and the spectrum of a C × C Gram matrix, and so the k-th eigenvalue of the whole is never below the k-th eigenvalue of the class-centre term

## Source

Papyan (2019, ICML), "Measurements of three-level hierarchical structure in
the outliers in the spectrum of deepnet Hessians", [LIT-619](../literature.d/LIT-619.md), read in full in
[NOTE-479](../notes.d/NOTE-479.md), including the proof of Lemma 2.1 and the derivation of Eqs.
12–28 (claims C1 and C2, "strong (algebra)"). The eigenvalue inequalities
appear in the paper as a reading of its scree plots (Figure 7). Here they
are derived.

## What was actually shown

**Setting.** C classes, N training examples per class (balanced), n = NC.
The softmax Hessian in the logits is
diag(p) − ppᵀ = (I − 1pᵀ)ᵀ diag(p) (I − 1pᵀ) (Lemma 2.1). So the
Gauss–Newton matrix is G = (1/n)ΔΔᵀ, whose columns δ_{i,c,c′} are column c′
of diag(√p)(I − 1pᵀ)∂f/∂θ at example i of class c (Eqs. 13–16), and

G = Ave_{i,c} Σ_{c′} δ_{i,c,c′} δ_{i,c,c′}ᵀ = (1/C) Σ_{c,c′} Ave_i δ_{i,c,c′} δ_{i,c,c′}ᵀ.

Write δ_{c,c′} = Ave_i δ_{i,c,c′} for the C² group means, and Σ_{c,c′} for
the within-group covariances.

**The decomposition.** A second moment is the outer product of the mean
plus the covariance, so Ave_i δ_{i,c,c′}δ_{i,c,c′}ᵀ = δ_{c,c′}δ_{c,c′}ᵀ + Σ_{c,c′}.
Hence G = (1/C) Σ_{c,c′} δ_{c,c′}δ_{c,c′}ᵀ + G₃, with
G₃ = (1/C) Σ_{c,c′} Σ_{c,c′} (Eq. 23). Take the terms with c′ = c apart:
G₀ = Ave_c δ_{c,c}δ_{c,c}ᵀ. For fixed c, the C − 1 group means δ_{c,c′},
c′ ≠ c, have centre δ_c = (1/(C − 1)) Σ_{c′≠c} δ_{c,c′} and covariance Σ_c
about it. So Σ_{c′≠c} δ_{c,c′}δ_{c,c′}ᵀ = (C − 1)(δ_cδ_cᵀ + Σ_c). Averaging
over c gives

G = G₀ + G₁ + G₂ + G₃,  G₁ = (C − 1) Ave_c δ_cδ_cᵀ,  G₂ = (C − 1) Ave_c Σ_c,

which is Eq. 28. Each term is a non-negative combination of outer products
or of covariance matrices, so each is positive semidefinite.

**The class-centre term.** Put D = [δ_1 … δ_C]. Then
G₁ = ((C − 1)/C) DDᵀ, which has rank at most C. Its non-zero eigenvalues
are those of the C × C Gram matrix ((C − 1)/C) DᵀD. If DᵀDu = μu with
μ > 0, then Du/√μ is a unit eigenvector of DDᵀ, and it lies in the span of
the class centres.

**The inequalities.** If B is positive semidefinite, then
λ_k(A + B) ≥ λ_k(A) for every k, by Courant–Fischer. Since
G − (G₁ + G₂) = G₀ + G₃ and (G₁ + G₂) − G₁ = G₂ are positive semidefinite,

λ_k(G) ≥ λ_k(G₁ + G₂) ≥ λ_k(G₁) for every k.

**What could have failed.** The cross terms in a mean-plus-covariance
split vanish only because each covariance is taken about its own group's
mean, and the c′ = c columns sit apart from the cluster centres only
because the paper groups them separately. Both were checked above. The
inequalities need nothing about training, the data or the architecture.

## What this does not say

- **That the top C eigenvalues of a trained network's G are those of G₁.**
  The inequalities bound them from below. That they are close is measured
  in [LIT-619](../literature.d/LIT-619.md), Figures 6–7, by plot comparison, and that attribution is
  [THEORY-078](THEORY-078.md)'s.
- **Anything for unbalanced classes.** There the averages become weighted
  sums, and the terms must be re-weighted ([NOTE-479](../notes.d/NOTE-479.md), assumptions).
- **Anything about the Hessian.** The Hessian adds a residual term that is
  not positive semidefinite, so these inequalities do not carry over to it.
- **That the C directions are discriminative.** The span of the class
  centres includes their common mean.
- **Anything about the empirical Fisher.** G is the model's Fisher, with
  labels drawn from the model's predictive distribution.

## Connections

- **[THEORY-078](THEORY-078.md)** extends this. It claims that in trained classifiers G₁
  carries the top C eigenvalues, so a cut at the bulk edge keeps the span
  of the class centres. That claim is measured and stays Proposed.
- **[CLAIM-377](../claims.d/CLAIM-377.md)**, the Fisher–NTK spectral identity, is the other exact
  spectral fact the record holds about a model's Fisher. It concerns a
  Gaussian likelihood, not softmax cross-entropy.
