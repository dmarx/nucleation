---
number: 201
status: Skimmed
formerly:
- NOTE-tmp6l5l9
paper: LIT-231
title: 'Assran et al. 2022 — hidden uniform cluster prior in SSL'
version: 1
date: '2026-09-26'
summary: >-
  Joint-embedding SSL methods that rely on mini-batch volume maximization (SimCLR, VICReg, SwAV, MSN) implicitly impose a prior toward features that cluster the data into equal-sized groups, which hurts on class-imbalanced data; replacing it with a power-law prior (PMSN) improves representations on long-tailed data.
---
<!-- inactive-ok-file: LIT-231 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-201: Assran et al. 2022 — hidden uniform cluster prior in SSL

## Contribution

Many successful self-supervised pretraining methods use tasks built on mini-batch statistics. The authors argue that all of these formulations carry an overlooked prior toward learning features that split the data into uniformly sized clusters. That prior suits class-balanced data like ImageNet but hampers learning on class-imbalanced data. They extend Masked Siamese Networks to accept arbitrary feature priors and show that a power-law prior improves representation quality on real-world long-tailed datasets.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Fig. 1 (pp. 1–2): volume-maximization regularizers (negatives, decorrelation, high-entropy clustering) are presented as a single principle whose side effect is a uniform-cluster prior, illustrated with K-means on imbalanced data.
- §3, Props. 1–4 (pp. 3–5): VICReg with γ≫α recovers the K-means loss, MSN recovers a GMM loss, SwAV a constrained K-means, and SimCLR is covered under limited assumptions via its equivalence to VICReg (Garrido et al.); proofs in App. C.
- §4, Table 1 (pp. 5–6): pretraining with class-imbalanced mini-batches (same marginal sampling probability, only K=2 or 8 classes per batch) degrades SimCLR, MSN and VICReg on semantic transfer tasks, while MAE and data2vec, which lack volume maximization, are relatively unaffected.
- Fig. 2 (p. 7): with imbalanced batches, MSN prototypes encode low-level attributes (shape, pose, texture) instead of class-level concepts.
- §5, Eq. 9 & §5.1 toy (p. 7): PMSN swaps the entropy term for a KL divergence to a power-law distribution; on CIFAR10 with power-law-distributed MNIST overlays, the uniform prior discards the digit feature while the matched power-law prior keeps it.

## Open questions

- Gives a cluster/probabilistic reading of SSL regularizers that complements the spectral reading of k17; together they say what the "collapse-prevention" term actually commits the representation to.
- Practice implication: SSL on long-tailed or uncurated data may want a non-uniform prior; check §5.2 gains on iNat18 and how the power-law exponent is chosen without labels.
- Check how strong the "limited assumptions" for SimCLR are.
