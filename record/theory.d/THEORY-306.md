---
number: 306
status: Active
formerly:
- THEORY-tmp8v921
title: "MSN's objective penalizes unequal cluster sizes explicitly and SwAV's enforces equal sizes, and in one study with mini-batches of two to eight ImageNet classes, SimCLR, MSN and VICReg lost 11 to 18 points of ImageNet linear accuracy while MAE and data2vec lost under one"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision file for THEORY-306 (batch 033, ADR-047
    v3). The title keeps what is exact and what one study, read in full,
    measured. MSN's and SwAV's prior holds by their definitions, and a
    dated note below gives the identity. The imbalance result is stated
    for the methods and batches tested. The class-wide claim is dropped,
    because VICReg's prior rests on a reduction of a simplified loss and
    SimCLR's on a cited equivalence. The promote_when moves unchanged to
    QUESTION-171.
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-14'
source:
- LIT-231
summary: >-
  Assran et al. (2022), [LIT-231](../literature.d/LIT-231.md), §§3–5 and Appendix C, read in
  [NOTE-850](../notes.d/NOTE-850.md). The prior is explicit in MSN's loss (a KL to uniform
  over mean cluster assignments) and in SwAV's equipartition constraint.
  For VICReg it rests on an informal reduction of a simplified loss to
  K-means and on K-means's cited tendency to equal clusters, and for
  SimCLR on a cited equivalence, so the title claims the prior for MSN
  and SwAV only. The effect is shown with batches of two to eight
  ImageNet classes, one run per cell, not with natural long tails; the
  open half is QUESTION-171.
---
<!-- inactive-ok-file: THEORY-305 THEORY-228 — Proposed; neighbouring accounts of what self-supervised objectives commit a representation to, open -->

# THEORY-306: MSN's objective penalizes unequal cluster sizes explicitly and SwAV's enforces equal sizes, and in one study with mini-batches of two to eight ImageNet classes, SimCLR, MSN and VICReg lost 11 to 18 points of ImageNet linear accuracy while MAE and data2vec lost under one

## Source

Assran, Balestriero, Duval, Bordes, Misra, Bojanowski, Vincent, Rabbat
and Ballas (2022; ICLR 2023), [LIT-231](../literature.d/LIT-231.md), read in full in [NOTE-850](../notes.d/NOTE-850.md):
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

- **It does not say every volume-maximizing objective carries the prior.**
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

- **[THEORY-305](THEORY-305.md).** Reads SimCLR's loss as a graph-Laplacian form,
  spectral clustering only in a sense that admits any regularizer. This
  account says what a particular regularizer prefers. K-means and its
  spectral relaxation are linked by the result Proposition 1 cites (Zha
  et al. 2001).
- **[THEORY-007](THEORY-007.md), [THEORY-009](THEORY-009.md) and [THEORY-228](THEORY-228.md).** The spectral account of the
  positive-pair graph, its eigenfunctions and its probe guarantees. Those
  concern which subspace the invariance term selects. This one concerns a
  bias of the anti-collapse term over partitions, and is compatible with
  them.

## Note of 2026-10-19: the prior in MSN and SwAV, checked

MSN's regularizer is the entropy of the batch-mean assignment p̄ over K
prototypes. Then

D_KL(p̄ ‖ U_K) = Σ_k p̄_k log(p̄_k K) = log K − H(p̄),

so −H(p̄) = D_KL(p̄ ‖ U_K) − log K. Maximizing H(p̄) is minimizing the KL
from the soft cluster sizes p̄ to uniform, which is [LIT-231](../literature.d/LIT-231.md)'s footnote 2.
Proposition 3 sharpens this to hard cluster sizes at zero temperature, and
the title needs only the identity. SwAV's Sinkhorn–Knopp step projects the
assignment matrix onto matrices whose prototype sums are all N/K (Eq. 8),
so equal soft cluster sizes are a constraint of the method. Neither half
needs Propositions 2 or 4, which are the sketches [NOTE-850](../notes.d/NOTE-850.md) flags.
