---
number: 2018
status: Proposed
formerly:
- THEORY-tmpanqm0
title: 'Zbontar and colleagues show that a joint-embedding objective which standardizes each embedding unit over the batch and drives the cross-correlation matrix between two views'' embeddings toward the identity learns ImageNet representations on par with contemporary self-supervised methods without negatives, predictors, stop-gradients or large batches, and that both the invariance (diagonal) and redundancy-reduction (off-diagonal) terms are needed'
version: 1
source:
- LIT-2795
tags:
- representation-learning
date: '2026-11-19'
promote_when: >-
  Table 5's loss ablation (only-invariance 57.3%, only-redundancy 0.1%,
  full 71.4% linear top-1 at 300 epochs) is confirmed from the published
  version or a reimplementation, and the 73.2% 1000-epoch linear result is
  confirmed from Table 1.
summary: >-
  From the reading of [LIT-2795](../literature.d/LIT-2795.md) in [NOTE-2129](../notes.d/NOTE-2129.md). Zbontar, Jing, Misra,
  LeCun, Deny (2021), ICML 2021 (PMLR 139), arXiv 2103.03230. The loss
  standardizes each embedding unit over the batch and drives the cross-
  correlation matrix between two distorted views' embeddings toward the
  identity. The diagonal makes the embedding invariant to the distortions
  and the off-diagonal decorrelates its units. It avoids collapse without
  negatives, predictors, stop-gradients or large batches, keeps improving
  with very wide embeddings, and both terms are needed: in the ablation,
  the off-diagonal term alone gives 0.1% linear accuracy, the diagonal
  alone 57.3%, the full loss 71.4%. The information-bottleneck reading
  rests on a Gaussian assumption and stated approximations, and there is
  no theorem. Here because A27 used it as a non-collapse mechanism
  ([CLAIM-481](../claims.d/CLAIM-481.md)'s note of 2026-11-19); [LIT-228](../literature.d/LIT-228.md) holds its CCA reading. Read in
  its NOTE.
---

# THEORY-2018: Zbontar and colleagues show that a joint-embedding objective which standardizes each embedding unit over the batch and drives the cross-correlation matrix between two views' embeddings toward the identity learns ImageNet representations on par with contemporary self-supervised methods without negatives, predictors, stop-gradients or large batches, and that both the invariance (diagonal) and redundancy-reduction (off-diagonal) terms are needed

## The account

The loss is Σ_i (1 − C_ii)² + λ Σ_i Σ_{j≠i} C_ij², where C is the cross-correlation between batch-standardized embeddings of two distortions of the same images. The diagonal term makes the embedding invariant to the distortions; the off-diagonal term decorrelates the units. With a ResNet-50 and an 8192-wide projector, it reaches 73.2% ImageNet linear top-1 (Table 1, per the text), is robust to batch sizes down to 256, and improves with embedding dimension where SimCLR and BYOL saturate. Removing either term gives worse or collapsed solutions. The authors read the loss as an information bottleneck under a Gaussian assumption, through stated approximations.

## What it does not show

There is no theorem. The paper does not prove that the surrogate has the information-maximizing optimum, does not characterize the optimal representation (the CCA reading is [LIT-228](../literature.d/LIT-228.md)'s, on a modified loss), and does not analyse training dynamics. Batch standardization does part of the anti-collapse work, and the paper does not separate its contribution from the redundancy term's.
