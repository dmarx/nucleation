---
number: 2012
status: Proposed
formerly:
- THEORY-tmp78qwh
title: 'Bardes, Ponce and LeCun show that in a joint-embedding objective the invariance term alone collapses all inputs to one vector, a covariance (decorrelation) term cannot prevent this, and a hinge keeping each embedding variable''s batch standard deviation above a threshold does; with all three terms the method matches contemporary self-supervised methods on ImageNet without negatives, normalization, predictors or shared weights'
version: 1
source:
- LIT-2813
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
  From the reading of [LIT-2813](../literature.d/LIT-2813.md) in [NOTE-2122](../notes.d/NOTE-2122.md). Bardes, Ponce, LeCun
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
<!-- inactive-ok-file: THEORY-tmpvwv5n — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# THEORY-2012: Bardes, Ponce and LeCun show that in a joint-embedding objective the invariance term alone collapses all inputs to one vector, a covariance (decorrelation) term cannot prevent this, and a hinge keeping each embedding variable's batch standard deviation above a threshold does; with all three terms the method matches contemporary self-supervised methods on ImageNet without negatives, normalization, predictors or shared weights

## The account

VICReg's loss is λ s(Z, Z′) + µ[v(Z) + v(Z′)] + ν[c(Z) + c(Z′)]: s the mean squared distance between paired embeddings, v the mean over variables of max(0, γ − S(z_j)) with S the regularized batch standard deviation, c the summed squared off-diagonal covariances scaled by 1/d. In the ablation the invariance term alone collapses, adding covariance does not help, adding variance gives 57.5% and all three 68.6% ImageNet linear accuracy at 100 epochs. A hinge on the variance instead of the standard deviation collapses because its gradient vanishes near the mean. With 1000 epochs VICReg reaches 73.2%, and it degrades less than Barlow Twins when the branches do not share weights or architecture.

## What it does not show

No theorem: the paper does not characterize VICReg's optimum (the spectral reading is [LIT-228](../literature.d/LIT-228.md)'s, for a modified loss) or its training dynamics, does not measure dimensional collapse, and does not study which classes beyond the augmentation the representation separates.

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi (LIT-2975, NOTE-tmpll97d, THEORY-tmpvwv5n): **a contrast.**
Here a collapse preventer, the variance hinge, is added to the objective
by hand; there the entropy term implicit in InfoNCE's denominator plays
that role. A note, no relation.
