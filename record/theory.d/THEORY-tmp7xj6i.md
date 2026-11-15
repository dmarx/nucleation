---
status: Active
title: 'On Belrose and colleagues, no linear predictor under any convex loss can beat a constant at predicting a categorical concept from a representation if and only if every class has the same mean, that is, the representation''s cross-covariance with the concept is zero; an affine edit Px + b achieves this if and only if P annihilates that cross-covariance''s column space; and one closed-form oblique projection, which whitens, removes the whitened cross-covariance directions and unwhitens, makes the smallest such edit in mean squared distance under every inner-product norm at once'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed Active, not Proposed: the title states theorems the paper
    proves (§3, Thms 4.1–4.3, with two independent proofs of 4.2), and
    the filer checked them numerically on sample moments (NOTE-tmpwodpq,
    "A check of the theorems"). Guardedness to 10⁻¹⁵; an idempotent,
    non-symmetric P; and the smallest cost of the erasers compared under
    all 200 random inner-product norms.
tags:
- information-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpme1pw
summary: >-
  Belrose, Schneider-Joseph, Ravfogel, Cotterell, Raff & Biderman (2023),
  LIT-tmpme1pw, read in NOTE-tmpwodpq. Theorems in population moments, and
  exact for the moments fitted. The sharp edges: the guarantee is linear
  only, and the authors conjecture that nonlinear erasure without damage
  is intractable in general; there is no finite-sample bound; and the
  oblique eraser can enlarge norms.
---

# THEORY-tmp7xj6i: On Belrose and colleagues, no linear predictor under any convex loss can beat a constant at predicting a categorical concept from a representation if and only if every class has the same mean, that is, the representation's cross-covariance with the concept is zero; an affine edit Px + b achieves this if and only if P annihilates that cross-covariance's column space; and one closed-form oblique projection, which whitens, removes the whitened cross-covariance directions and unwhitens, makes the smallest such edit in mean squared distance under every inner-product norm at once

## Source

Belrose et al. (2023), LIT-tmpme1pw, read in full in
NOTE-tmpwodpq from arXiv v4.

## What was actually shown

The equivalence of §3, the characterisation of Thm 4.1, and the optimal
eraser of Thms 4.2–4.3, all proved. The eraser is r(x) = x −
W⁺P_{WΣXZ}W(x − E[X]), with W = (Σ_XX^{1/2})⁺. Each could have failed:
the optimum might have depended on the norm, or been orthogonal.
Empirically, scrubbing part of speech from every layer of LLaMA and
Pythia raises bits per byte well above a random erasure of equal rank.

## What this does not say

- **That the concept is gone.** Nonlinear predictors may still recover
  it. The authors conjecture that preventing this without damage is
  intractable in general.
- **That I(Z; r(X)) = 0.** Zero cross-covariance is weaker than
  independence. The information-theoretic cap of THEORY-281 concerns
  the stronger condition.
- **Anything about model editing or weight-space projections.** The
  paper projects representations.
