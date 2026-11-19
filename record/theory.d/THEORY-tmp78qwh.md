---
status: Proposed
title: 'Bardes, Ponce and LeCun show that in a joint-embedding objective the invariance term alone collapses all inputs to one vector, a covariance (decorrelation) term cannot prevent this, and a hinge keeping each embedding variable''s batch standard deviation above a threshold does; with all three terms the method matches contemporary self-supervised methods on ImageNet without negatives, normalization, predictors or shared weights'
version: 1
source:
- LIT-tmpf5qpo
tags:
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-141
promote_when: >-
  Table 7's ablation (invariance alone and invariance plus covariance
  collapse; invariance plus variance 57.5%; all three 68.6% at 100 epochs)
  is confirmed from the published ICLR version or an independent
  reimplementation.
summary: >-
  From the reading of [LIT-tmpf5qpo](../literature.d/LIT-tmpf5qpo.md) in [NOTE-tmpprl89](../notes.d/NOTE-tmpprl89.md). Bardes, Ponce, LeCun
  (2021), ICLR 2022, arXiv 2105.04906. The loss has three terms on the
  embeddings: invariance (mean squared distance between two views), a
  hinge holding each variable's batch standard deviation above 1, and a
  penalty on off-diagonal covariances, the last two applied to each branch
  separately. In the ablation the invariance term alone collapses
  everything to one vector, covariance cannot stop it, and the variance
  term does (57.5%, and 68.6% with all three, at 100 epochs; 73.2% at
  1000). The hinge must be on the standard deviation: on the variance, its
  gradient vanishes and the embeddings collapse. That bears on [LIT-228](../literature.d/LIT-228.md)'s
  Laplacian-eigenmaps reading, which assumes a squared variance term. Here
  because A27 used it as a non-collapse mechanism ([CLAIM-481](../claims.d/CLAIM-481.md)'s note of
  2026-11-19). Read in its NOTE.
---

# THEORY-tmp78qwh: Bardes, Ponce and LeCun show that in a joint-embedding objective the invariance term alone collapses all inputs to one vector, a covariance (decorrelation) term cannot prevent this, and a hinge keeping each embedding variable's batch standard deviation above a threshold does; with all three terms the method matches contemporary self-supervised methods on ImageNet without negatives, normalization, predictors or shared weights

## The account

VICReg's loss is λ s(Z, Z′) + µ[v(Z) + v(Z′)] + ν[c(Z) + c(Z′)]: s the mean squared distance between paired embeddings, v the mean over variables of max(0, γ − S(z_j)) with S the regularized batch standard deviation, c the summed squared off-diagonal covariances scaled by 1/d. In the ablation the invariance term alone collapses, adding covariance does not help, adding variance gives 57.5% and all three 68.6% ImageNet linear accuracy at 100 epochs. A hinge on the variance instead of the standard deviation collapses because its gradient vanishes near the mean. With 1000 epochs VICReg reaches 73.2%, and it degrades less than Barlow Twins when the branches do not share weights or architecture.

## What it does not show

No theorem: the paper does not characterize VICReg's optimum (the spectral reading is [LIT-228](../literature.d/LIT-228.md)'s, for a modified loss) or its training dynamics, does not measure dimensional collapse, and does not study which classes beyond the augmentation the representation separates.
