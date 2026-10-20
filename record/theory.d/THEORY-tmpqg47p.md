---
status: Proposed
promote_when: >-
  A formal proof of Simon et al.'s Result 4.6 (generic small initialization
  follows the aligned trajectory as the scale goes to zero), which the paper
  derives only informally, or a proof of the same stepwise order for a
  second spectral SSL loss on a linear or fixed-kernel model. Either would
  settle the account in the regime it claims. It is refuted by a linear or
  fixed-kernel case of this loss, from vanishing generic initialization with
  distinct positive eigenvalues, that does not reach the minimum-norm
  solution or learns a lower mode first. What cannot settle it: more ResNet
  runs showing stepwise rank growth, since the theory does not cover a
  moving tangent kernel and the paper's own initial-NTK predictions for
  ResNets are poor.
title: Gradient flow on a symmetrized Barlow Twins loss with a linear or fixed-kernel model, from generic small initialization and not only from initialization aligned with the eigenvectors, learns the top eigenvectors of the pairs' symmetrized cross-correlation one at a time in order of eigenvalue and ends at a top spectral solution, as Simon and coauthors derive informally
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-20'
source:
- LIT-242
extends:
- THEORY-229
answers:
- QUESTION-175
summary: >-
  Simon et al. (2023), [LIT-242](../literature.d/LIT-242.md), read in [NOTE-741](../notes.d/NOTE-741.md). The stepwise dynamics, the
  minimum-norm end point and the kernel-PCA form are proved from aligned
  initialization, and that part is the Active [THEORY-229](THEORY-229.md). Generic small
  initialization rests on the paper's Result 4.6, which its authors style a
  result and derive informally in App. C, with numerical checks at d = 3.
  This THEORY holds that generic case.
---

# THEORY-tmpqg47p: Gradient flow on a symmetrized Barlow Twins loss with a linear or fixed-kernel model, from generic small initialization and not only from initialization aligned with the eigenvectors, learns the top eigenvectors of the pairs' symmetrized cross-correlation one at a time in order of eigenvalue and ends at a top spectral solution, as Simon and coauthors derive informally

## Source

[LIT-242](../literature.d/LIT-242.md). Filed by the promotion audit's narrowing-loss sweep
(batch 066, [ADR-047](../decisions.d/ADR-047.md) v4) on 2026-10-20, to carry the wider claim that the
narrowing of [THEORY-229](THEORY-229.md) dropped. [THEORY-229](THEORY-229.md) is Active and is this
THEORY's evidence; this one stays Proposed.

## What was actually shown

From an initialization of common small scale aligned with the top
eigenvectors of K_Γ, each mode obeys a closed equation, and the modes are
learned in order of eigenvalue at times τ_j ≈ −log(s_j(0)²γ_j)/(8γ_j)
(Prop. 4.1); the top spectral solutions are exactly the minimum-norm
zero-loss ones (Prop. 4.3), and the kernel case is kernel PCA on K_Γ
(Prop. 5.1). [THEORY-229](THEORY-229.md) states these, re-derived in the promotion audit.
Result 4.6 argues that a generic initialization W(0) = αW̃₀ follows the
aligned trajectory as α → 0, because the off-diagonal parts stay small
while each mode escapes its unstable start in turn. [NOTE-741](../notes.d/NOTE-741.md) rates that
claim moderate: an informal derivation and small numerical checks.

## What would settle it

The promote_when is inherited from [THEORY-229](THEORY-229.md)'s before it was
narrowed, and [QUESTION-175](../questions.d/QUESTION-175.md) asks the same question.

## What this does not say

It says nothing about networks whose tangent kernel moves, such as
the ResNets in which the paper also sees stepwise rank growth under
SimCLR and VICReg; the paper's own initial-kernel predictions there are
poor. It makes no claim about downstream generalization, which the
authors leave open.
