---
status: Active
title: 'On a finite augmentation space, over unconstrained functions of the two views, the spectral contrastive and NT-Logistic losses are both minimized at the positive-pair density ratio'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-001 and filed Active at the owner's direction, from
    the second pass of the owner's promotion audit of 2026-10-19.
    THEORY-001's promote_when recorded this half as done (NOTE-751: the
    derivations of Johnson et al. App. B.2–B.3 confirmed with their
    finite-space and unconstrained-function conditions) and held the whole
    entry Proposed for the InfoNCE/NT-Xent minimizer alone. This THEORY
    holds the confirmed half; THEORY-001 keeps the three-way statement and
    extends this one. Both derivations checked again for the split.
tags:
- representation-learning
- information-theory
- mathematics
date: '2026-10-19'
source:
- LIT-258
summary: >-
  Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), App. B.2–B.3, read in
  [NOTE-751](../notes.d/NOTE-751.md): on a finite augmentation space, with every function of the two
  views allowed, the spectral contrastive loss is minimized by
  K⁺ = p⁺/(p⊗p) exactly, and the NT-Logistic loss with equal positive and
  negative classes by the log-odds log K⁺, so its exponentiated score is
  K⁺. Population optima over unconstrained functions only; not what an
  encoder reaches, and not InfoNCE, which is [THEORY-001](THEORY-001.md)'s open part.
extended_by:
- THEORY-001
---
<!-- inactive-ok-file: THEORY-001 — Proposed; the three-way account this half was split from and that extends it, cited as open -->

# THEORY-tmpsuto2: On a finite augmentation space, over unconstrained functions of the two views, the spectral contrastive and NT-Logistic losses are both minimized at the positive-pair density ratio

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), App. B.2–B.3, read in
[NOTE-751](../notes.d/NOTE-751.md) (its claim C1, "strong", "exact").

## What was actually shown

Let A be finite, p⁺ the positive-pair distribution on A × A with marginal
p, and K⁺ = p⁺/(p⊗p).

- **Spectral contrastive loss.** Over all kernels K̂ on A × A, the loss
  −2 E_{p⁺}[K̂] + E_{p⊗p}[K̂²] equals
  Σ_{a,b} (p⁺(a,b)/√(p(a)p(b)) − √(p(a)p(b)) K̂(a,b))² − C, with C not
  depending on K̂ (B.3). Each term is minimized separately, at K̂ = K⁺.
- **NT-Logistic.** With one negative per positive drawn from p⊗p and equal
  priors on the two classes, the logistic loss is a binary cross-entropy
  between p⁺ and p⊗p. Pointwise its minimizer is the log-odds
  log(p⁺/(p⊗p)) = log K⁺ (B.2), so the exponentiated score is K⁺.

Both derivations are pointwise and exact. They could have failed: a loss
whose optimum depended on how the negatives are drawn, in a way that did
not cancel, would have another target. Here the negatives are drawn from
the product of the marginals, and the target is the ratio.

## What this does not say

- **That a network reaches K⁺.** The minimum is over unconstrained
  functions. A finite-capacity encoder, or a low-rank inner-product
  parametrization, reaches at best a constrained optimum, and for the
  spectral loss that is the rank-k one, which is HaoChen et al.'s
  ([LIT-249](../literature.d/LIT-249.md)).
- **Anything about InfoNCE/NT-Xent.** Its minimizer is taken from van den
  Oord et al., not derived, and is fixed only up to a factor constant on
  communicating classes ([THEORY-001](THEORY-001.md)).
- **Anything for continuous views.** The derivation is on a finite space;
  in the continuous case the ratio needs P⁺ ≪ P⊗P, and the spectral loss
  needs K⁺ ∈ L²(p⊗p), which is finite χ² ([CLAIM-tmpu2dsm](../claims.d/CLAIM-tmpu2dsm.md)).
- **That the two losses give the same d-dimensional features.** The
  spectral loss fits K⁺ and the logistic loss fits log K⁺, and truncation to
  rank d does not commute with the logarithm.
