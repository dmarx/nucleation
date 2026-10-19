---
number: 850
status: Read
formerly:
- NOTE-tmpyexl4
paper: LIT-231
title: 'Assran et al. — The Hidden Uniform Cluster Prior in Self-Supervised Learning'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2210.07277v1, 13 October 2022, the
    only version, 25 pages), text extracted with pdftotext in
    reading-order and layout modes: §§1–6, figure captions 1–5, and
    appendices A–I, including the proofs of Propositions 1–4 (C.1–C.4),
    the pretraining and evaluation details (D–E), the sampling
    alternative (F), the marginal-probability derivation (G) and the
    full results tables (I, Tables 5–11). Equations were read from the
    layout extraction. The prototype visualisations (Figs. 2, 4) and the
    nearest-neighbour panel (Fig. 3) are images, read from their
    captions and the text. Table 1 was checked cell by cell against
    Tables 5–11. Replaces the seeded skim NOTE-201.
date: '2026-10-14'
summary: >-
  MSN's entropy term is a KL penalty pulling cluster sizes toward
  uniform, and SwAV's Sinkhorn step enforces equal sizes outright; for
  VICReg the same prior is reached only through an informal reduction to
  K-means, and for SimCLR only by a cited equivalence. With mini-batches
  of two to eight ImageNet classes, SimCLR, VICReg and MSN lose 11–18
  points of ImageNet linear accuracy while MAE and data2vec do not. A
  power-law prior in MSN gains about 1–3 points on long-tailed iNat18 and
  loses heavily on ImageNet.
---
<!-- inactive-ok-file: NOTE-201 — Superseded; the skim this reading replaces -->
<!-- inactive-ok-file: THEORY-306 THEORY-305 THEORY-228 — Proposed; the account filed from this reading and its neighbours, open -->

# NOTE-850: Assran et al. — The Hidden Uniform Cluster Prior in Self-Supervised Learning

## Contribution

The paper argues that joint-embedding self-supervised methods whose
collapse-prevention term maximizes the volume the representations
occupy (SimCLR, VICReg, SwAV, MSN) all prefer features that split the
data into equal-sized clusters. It connects each loss to a K-means
variant, shows that training with class-imbalanced mini-batches hurts
exactly these methods, and extends MSN to an arbitrary target
distribution over cluster sizes (PMSN). With a power-law target it gains
modestly on the long-tailed iNaturalist-18.

## Key insight

The term that keeps a joint embedding from collapsing is not neutral. In
MSN it is the entropy of the mean cluster assignment, which is a KL
divergence to the uniform distribution plus a constant (footnote 2). So
the objective scores a feature partly by how evenly it splits the batch.
A feature that splits the data unevenly, even a semantic one, is
penalized.

## Assumptions

- **VICReg (Proposition 2).** The simplified loss of Eq. 3, with the
  variance and covariance terms merged into α‖Cov(Z) − I‖²_F, and
  γ ≫ α. The proof (C.2) assumes Z is centred and works through bounds
  on eigenvalues; its conclusion that "the only possible solution" is to
  minimize ‖(1/N)ZᵀGZ − I‖ is argued, not derived step by step. The
  number of centroids is min(dim z, rank(G + I)), so the "clusters" are
  the groups of positive views of each image.
- **SimCLR.** Covered only through Garrido et al.'s equivalence of VICReg
  and SimCLR "under mild conditions"; nothing is proved for SimCLR here.
- **MSN (Proposition 3).** The zero-temperature limit σ → 0, with target
  sharpening σ⁺ ≪ σ, and (for simplicity, removable) no empty cluster.
- **SwAV (Proposition 4).** A one-paragraph proof that refers the link
  between Sinkhorn–Knopp and the constrained, relaxed K-means problem to
  Wang et al. (2010).
- **The uniform prior of K-means itself** is not proved. It is cited
  (Wu et al. 2009; Liang et al. 2012): K-means works best with
  "roughly the same number of samples" per cluster and isotropic
  covariance σI.
- **"Class-imbalanced" in §4 means the mini-batch, not the dataset.**
  The pretraining data is ImageNet-1K in every case. Imbalanced sampling
  draws K classes per batch (8 for SimCLR at batch 4096; 2 for VICReg
  and MSN at batch 1024) and keeps each image's marginal sampling
  probability unchanged (Appendix G).
- **Architectures differ across methods**: ResNet-50 for SimCLR and
  VICReg, ViT-B/16 for MSN and data2vec, ViT-L/16 for MAE. The
  comparison is between balanced and imbalanced runs of each method, not
  between methods at a fixed architecture.

## Key results

- **Proposition 1 (C.1).** Explicit K-means (learn centroids) and implicit
  K-means (learn memberships, Eq. 2:
  Σ_k Σ_{x∈X_k} ‖x − μ_k‖² = Σ_k (1/2|X_k|) Σ_{x,x′∈X_k} ‖x − x′‖²)
  have the same global optimum. Standard; already in Zha et al. (2001).
- **Proposition 2 (C.2).** VICReg with γ ≫ α "recovers the K-means loss
  … with an additional regularizer enforcing orthogonality of the
  centroids": (γ/N) Σ_k Σ_{x∈X_k} ‖x − μ_k‖² + α‖MᵀM − I‖²_F. *Holds
  when:* the simplified Eq. 3 and γ ≫ α. The authors note that
  γ ≫ α is the usual practice.
- **Proposition 3 (C.3).** In the limit σ → 0, σ·L_MSN becomes
  Σ_k Σ_{x∈X_k} ‖x − μ_k‖² + λ Σ_k (N_k/N) log((N_k/N)/(p_prior)_k),
  K-means plus a KL penalty on the empirical cluster sizes N_k/N against
  the prior, uniform in MSN. *Holds when:* zero temperature, with
  sharpening. Here the cluster-size prior is explicit in the loss.
- **Proposition 4 (C.4).** SwAV's equipartition constraint,
  P1_N = (N/K)1_K, enforced by Sinkhorn–Knopp, is K-means with every
  |X_k| = N/K: "strict enforcement of the uniform cluster prior".
- **Imbalanced batches hurt volume-maximizing methods (Table 1;
  Tables 5–11).** Imbalanced minus balanced, linear evaluation:
  - ImageNet-1K: SimCLR −11.1, MSN −17.7, VICReg −17.7; data2vec −0.8,
    MAE −0.1 (Table 10).
  - ImageNet 1% low-shot: MSN −38.2, VICReg −30.5; data2vec +4.0,
    MAE −0.3 (Table 11; SimCLR not reported).
  - Places205: −5.2, −4.6, −6.0 for SimCLR, MSN, VICReg; Clevr/Count:
    −4.3, −6.4, −3.0.
  - Depth (Clevr/Dist, KITTI): within about ±2 for all methods, which the
    authors read as the imbalanced models keeping lower-level features.
- **Prototypes (Fig. 2).** In MSN trained on imbalanced batches, the
  RCDM-decoded prototypes hold low-level attributes ("shape, pose, or
  texture") rather than ImageNet classes. Qualitative.
- **PMSN (Eq. 9).** (1/N) Σ H(p⁺ᵢ, pᵢ) + λ D_KL(p̄ ‖ p_PL(τ)), with
  [p_PL(τ)]_k ∝ 1/k^τ.
- **Toy (§5.1, Fig. 3).** Grayscale CIFAR-10 with an MNIST digit overlaid
  in a corner, digits power-law distributed (exponent 0.5). A matched
  power-law prior keeps the digit in the embedding (nearest neighbours
  share it); the uniform prior discards it. Entropy coefficient 100, ten
  prototypes (E.1.1). Qualitative.
- **iNat18 (Tables 2–3).** ViT-S/16, one run each, no error bars.
  - True class prior instead of uniform: iNat18 29.1 → 32.1 (+3.0),
    CIFAR-100 +0.9, Places205 +1.4, Clevr/Count +2.1, Clevr/Dist +2.3,
    KITTI +2.7. The true class distribution is not available in
    self-supervised pretraining, as the authors say.
  - Power law with τ = 0.25: iNat18 +1.0, CIFAR-100 +0.7, Places205 +0.8,
    Clevr/Count +1.7, Clevr/Dist +2.1, KITTI 0.0.
  - The same power law on ImageNet (ViT-B/16): −19.9 on iNat18, −17.8 on
    CIFAR-100, −15.7 on Places205, −6.7 on KITTI, +8.0 on Clevr/Dist.
- **Sampling is not the fix (Appendix F, Table 4).** Inverse square-root
  class-frequency sampling on iNat18 does worse than uniform (23.4 vs
  29.1 on iNat18).
- **InfoMax (Appendix B).** Maximizing I(Z; X) = H[Z] − H[Z|X] pushes
  toward high marginal entropy, "uniformly distributed feature
  embeddings", so the same prior is in the InfoMax principle. Stated as
  an argument, not a result.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | MSN's regularizer is an explicit KL penalty pulling cluster sizes toward uniform | strong | Eq. 6, footnote 2, Proposition 3 (exact in the zero-temperature limit) |
| C2 | SwAV enforces equal cluster sizes | strong | its equipartition constraint, Eq. 8 |
| C3 | VICReg is K-means on the embeddings plus a centroid-orthogonality term | weak | Proposition 2, for a simplified loss and γ ≫ α, with an informal final step |
| C4 | SimCLR carries the same prior | weak | a cited equivalence to VICReg, nothing proved here |
| C5 | Volume-maximizing methods lose semantic transfer when each mini-batch holds few classes; MAE and data2vec do not | moderate | Tables 1, 5–11, one run per cell, two to eight classes per batch |
| C6 | Matching the prior to the class distribution improves long-tailed pretraining | moderate | Table 2 with the true class prior; Table 3 with a guessed power law, about +1 on iNat18 |
| C7 | The uniform prior explains the degradation reported on real long-tailed data | weak | inferred from C5, whose batches hold 2–8 classes, far more extreme than natural imbalance |

## Method

PMSN: MSN (a masked view and an unmasked view of an image, soft
assignments to K learned prototypes, cross-entropy between them with a
sharpened target) with the mean-entropy regularizer replaced by a KL
divergence from the batch-mean assignment p̄ to a chosen distribution
over prototypes, uniform or power-law. Prototypes are visualised by
training an RCDM diffusion decoder on the projector's 256-dimensional
embedding and conditioning it on a prototype vector (Appendix H).

## Concepts

- **Volume maximization principle.** A regularizer that maximizes "the
  volume of space occupied by the representations": negatives,
  decorrelation, or high-entropy clustering.
- **Uniform cluster (feature) prior.** "A bias to learn features that
  enable grouping the data into clusters of roughly equal size".
- **Explicit and implicit K-means.** Learning centroids, or learning a
  membership matrix and using pairwise distances within clusters.
- **Class-balanced and class-imbalanced sampling (§4).** 960 classes per
  batch, or the fewest classes that fill the batch, with equal marginal
  sampling probability per image.
- **Instance-based methods.** Here MAE and data2vec, which do not compute
  mini-batch statistics in their loss.

## Connections

It cites, and does not reproduce, Wang and Isola (2020) on alignment and
uniformity on the hypersphere, Garrido et al. (2022) on the
SimCLR–VICReg equivalence, and Balestriero and LeCun (2022, [LIT-228](../literature.d/LIT-228.md)) on
contrastive and non-contrastive methods as spectral embeddings. Its
K-means reading sits beside the spectral-clustering reading of SimCLR in
Tan et al. ([LIT-227](../literature.d/LIT-227.md)), filed today as [THEORY-305](../theory.d/THEORY-305.md): the K-means
objective and its spectral relaxation are linked by the Zha et al. (2001)
result that Proposition 1 cites. It answers Tian et al. (2021) on the
drop of joint-embedding methods on long-tailed data, offering a cause.

## Bearing on the record

- **No THEORY held it before.** A search of theory.d for the cluster-size
  prior, volume maximization and the authors found nothing. The account
  is filed as [THEORY-306](../theory.d/THEORY-306.md), at the strength each method's link is
  established, which differs a great deal by method.
- **Beside the spectral readings.** The seeded entry asked how this
  complements "the spectral reading of k17". [LIT-228](../literature.d/LIT-228.md) (Balestriero and
  LeCun) is cited here only for VICReg's degenerate whitening when
  α ≫ γ. [THEORY-007](../theory.d/THEORY-007.md), [THEORY-009](../theory.d/THEORY-009.md) and [THEORY-228](../theory.d/THEORY-228.md) hold the spectral account
  of the positive-pair graph; this paper's account is about the
  regularizer's preference over partitions, and the two do not conflict.
  [THEORY-305](../theory.d/THEORY-305.md) reads SimCLR as spectral clustering "only in a sense
  that admits any regularizer"; this paper says what one regularizer,
  MSN's, prefers.
- **For practice, which belongs in the anthology.** The paper's practical
  advice, to match the prior to the class distribution when pretraining
  on long-tailed data, is an instruction for machine-learning practice.
  It is noted here and not filed. The entry's `anthology-candidate` flag
  stands. The anthology was not checked for this paper in this reading.
- **The skim's checks.**
  - "How strong the limited assumptions for SimCLR are": nothing is
    proved for SimCLR; it rests on Garrido et al.'s equivalence.
  - "How the power-law exponent is chosen without labels": it is not.
    τ = 0.25 is set by hand, and τ = 0.5 in the toy is matched to the
    known digit distribution.
  - "§5.2 gains on iNat18": +1.0 with the guessed power law, +3.0 with
    the true class prior, single runs.

## Limitations

- **The §4 imbalance is extreme and artificial**: two classes in a
  1024-image batch, from a balanced dataset. It shows sensitivity to
  batch composition, not the size of the effect under natural long
  tails.
- **One run per cell, no error bars.** Differences of 1–3 points in
  Tables 2–3 have no stated variance.
- **Table 1 does not quite match the appendix.** Its "CIFAR100" column
  (−10.2, −13.2, −12.0, −1.6, +2.5) is the CIFAR-100 1% column of
  Tables 5–9; full CIFAR-100 gives −6.4, −12.9, −8.9, −1.7, +0.4. Its
  data2vec Clevr/Dist entry is −1.5 where Table 8 gives +1.5, and several
  MAE cells differ from Table 9 by up to 0.7. Its caption says
  "balanced minus imbalanced", but the signs are imbalanced minus
  balanced.
- **Propositions 2 and 4 are sketches.** Proposition 2 concerns a
  simplified VICReg, and its last step is argued in words. Proposition 4
  is a pointer to Wang et al.
- **MAE and data2vec differ from the others in architecture and
  objective**, so their stability under imbalanced batches is not cleanly
  attributed to the absence of a volume term. The authors note that
  data2vec avoids collapse by "architectural heuristics".
- **The authors' own scope:** "we do not claim to have completely solved
  the issue of class-imbalanced pretraining."

## Open questions

- How large is the effect at natural degrees of imbalance, with batches
  sampled uniformly from a long-tailed dataset and a controlled
  architecture?
- Can the target distribution be estimated without labels, for instance
  from the learned assignments themselves?
- Does the VICReg reduction hold for the actual loss with its hinge
  variance term, not only the simplified one?
