---
status: Proposed
promote_when: >-
  Two kinds of result, one for each half. For the prior: a derivation of
  the cluster-size preference for the losses as used (VICReg with its
  hinge variance term, SimCLR at finite temperature), or a measurement of
  the cluster-size distribution that trained VICReg and SimCLR models
  induce on data with known unequal classes. For the effect: the
  imbalance experiment repeated with batches sampled uniformly from a
  naturally long-tailed dataset, at one architecture across methods, with
  seeds. The account is refuted for a method if its learned partitions
  track unequal class sizes as well as an instance-based method's do.
  What cannot settle it: more results with two-class batches, or gains
  from a prior matched with labels.
title: 'Volume-maximizing joint-embedding objectives carry a prior toward equal-sized clusters, explicit in MSN and SwAV and derived for VICReg only through a reduction to K-means, and with mini-batches of two to eight classes they lose semantic transfer while MAE and data2vec do not'
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-231
summary: >-
  Assran et al. (2022), [LIT-231](../literature.d/LIT-231.md), §§3–5 and Appendix C, read in
  [NOTE-tmpyexl4](../notes.d/NOTE-tmpyexl4.md). The prior is explicit in MSN's loss (a KL to uniform
  over mean cluster assignments) and in SwAV's equipartition constraint.
  For VICReg it rests on an informal reduction of a simplified loss to
  K-means and on K-means's cited tendency to equal clusters, and for
  SimCLR on a cited equivalence. The effect is shown with batches of
  two to eight ImageNet classes, one run per cell, not with natural long
  tails.
---
<!-- inactive-ok-file: THEORY-tmp7rs2e THEORY-228 THEORY-009 — Proposed; neighbouring accounts of what self-supervised objectives commit a representation to, open -->

# THEORY-tmp8v921: Volume-maximizing joint-embedding objectives carry a prior toward equal-sized clusters, explicit in MSN and SwAV and derived for VICReg only through a reduction to K-means, and with mini-batches of two to eight classes they lose semantic transfer while MAE and data2vec do not

## Source

Assran, Balestriero, Duval, Bordes, Misra, Bojanowski, Vincent, Rabbat
and Ballas (2022; ICLR 2023), [LIT-231](../literature.d/LIT-231.md), read in full in [NOTE-tmpyexl4](../notes.d/NOTE-tmpyexl4.md):
§3 with Propositions 1–4 and their proofs (Appendix C), §4 with Tables 1
and 5–11, §5 with Tables 2–4.

## What was actually shown

**The prior, method by method, at different strengths.**

- *MSN.* The regularizer is the entropy of the batch-mean assignment
  p̄, and −H(p̄) is D_KL(p̄ ‖ uniform) up to a constant (footnote 2). In
  the zero-temperature limit with sharpening, σ·L_MSN becomes K-means
  plus λ Σ_k (N_k/N) log((N_k/N)/(1/K)), a penalty on unequal cluster
  sizes (Proposition 3). The prior is in the loss.
- *SwAV.* The Sinkhorn–Knopp projection enforces P1_N = (N/K)1_K, equal
  cluster sizes, as a constraint (Eq. 8; Proposition 4, a one-paragraph
  pointer to Wang et al. 2010).
- *VICReg.* For a simplified loss, α‖Cov(Z) − I‖²_F plus the invariance
  term, and γ ≫ α, the loss becomes K-means on the embeddings plus an
  orthogonality penalty on the centroids (Proposition 2). The last step
  of the proof is argued in words. The uniform prior then follows only
  from K-means's tendency toward "roughly the same number of samples"
  per cluster, which is cited, not shown.
- *SimCLR.* Nothing is proved. The paper relies on Garrido et al.'s
  equivalence with VICReg "under mild conditions".

**The effect.** Each method was pretrained on ImageNet-1K twice: with
960 classes per batch, and with the fewest classes that fill a batch
(8 for SimCLR, 2 for VICReg and MSN), keeping each image's marginal
sampling probability unchanged. Linear ImageNet accuracy fell by 11.1
(SimCLR), 17.7 (MSN) and 17.7 (VICReg) points, and by 0.8 (data2vec) and
0.1 (MAE). Places205 and Clevr/Count fell for the first three, while
depth tasks moved by about two points or less for all. This could have
come out otherwise: the instance-based methods, which compute no batch
statistics, were run under the same sampling and did not degrade.

**Changing the prior.** Replacing MSN's uniform target with the true
class distribution of iNaturalist-18 raised iNat18 linear accuracy from
29.1 to 32.1, and a hand-set power law (τ = 0.25) to 30.1. The same
power law on ImageNet cost 15–20 points on the semantic tasks. So the
target over cluster sizes affects what is learned, in the direction the
account predicts.

## What this does not say

- **It does not say the prior is equally established for every method.**
  It is exact for MSN and SwAV. For VICReg it rests on a reduction of a
  simplified loss plus a cited property of K-means, and for SimCLR on a
  cited equivalence.
- **It does not say that natural class imbalance causes the drops
  reported on long-tailed data.** The experiment uses two to eight
  classes per batch from a balanced dataset. Its size at natural
  imbalance is not measured.
- **It does not isolate the volume term.** The methods compared differ in
  architecture (ResNet-50, ViT-B, ViT-L) and in objective, and data2vec
  avoids collapse by other means. The contrast is within each method,
  balanced against imbalanced.
- **It is not an instruction.** That a matched prior helps on long-tailed
  data is advice for practice, and belongs in the anthology. The gains
  are single runs of 1–3 points, and the best one uses labels.
- **It does not say what the representation is.** The account is about
  the regularizer's preference over partitions of a batch. What the
  learned eigenfunctions or spectral embedding are is the subject of the
  accounts below.

## Connections

- **[THEORY-tmp7rs2e](THEORY-tmp7rs2e.md).** Reads SimCLR's loss as a graph-Laplacian form,
  spectral clustering only in a sense that admits any regularizer. This
  account says what a particular regularizer prefers. K-means and its
  spectral relaxation are linked by the result Proposition 1 cites (Zha
  et al. 2001).
- **[THEORY-007](THEORY-007.md), [THEORY-009](THEORY-009.md) and [THEORY-228](THEORY-228.md).** The spectral account of the
  positive-pair graph, its eigenfunctions and its probe guarantees. Those
  concern which subspace the invariance term selects. This one concerns a
  bias of the anti-collapse term over partitions, and is compatible with
  them.
