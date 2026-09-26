---
status: Skimmed
paper: LIT-tmp68gob
title: 'Tan et al. 2023 — contrastive learning is spectral clustering'
version: 1
date: '2026-09-26'
summary: >-
  SimCLR's unmodified InfoNCE loss is equivalent to spectral clustering on the augmentation-defined similarity graph (min tr(Zᵀ L(π) Z) + log R(Z)), CLIP does generalized spectral clustering on the image–text pair graph, and mixtures of exponential kernels (Kernel-InfoNCE) beat the Gaussian kernel.
---
<!-- inactive-ok-file: LIT-tmp68gob — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpctvbf: Tan et al. 2023 — contrastive learning is spectral clustering

## Contribution

The authors aim to explain theoretically why contrastive learning works. They prove that contrastive learning with the standard InfoNCE loss is equivalent to spectral clustering on the similarity graph induced by data augmentation. Building on this, they extend the analysis to CLIP and characterize how similar multimodal objects end up embedded together. Their theory motivates a Kernel-InfoNCE loss using mixtures of kernel functions, which outperforms the standard Gaussian kernel on several vision datasets.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (p. 1): positions itself against HaoChen et al. (2021), whose spectral result required the modified spectral contrastive loss plus an extra linear transform; here the standard InfoNCE is analyzed directly.
- Fig. 1 & §2 (pp. 2–5): method compares two Markov random fields — one from the similarity matrix π, one from the embedding Gram matrix K_Z — via cross-entropy over sampled subgraphs, following Van Assel et al. (2022).
- §3.1, Thm 3.1 (p. 6): SimCLR ≡ min_Z tr(Zᵀ L(π) Z) + log R(Z), i.e. spectral clustering on π; the discussion reads the full-n requirement as an explanation of why SimCLR benefits from large batches.
- §4, Def. 4.1 & Thm 4.2 (pp. 6–7): CLIP's objective as generalized spectral clustering on an asymmetric bipartite pair graph.
- §5.1–5.2 (pp. 7–8): a maximum-entropy argument for exponential kernels motivates Kernel-InfoNCE; §6 Table 1 (p. 9) compares against SimCLR on CIFAR-10/100 and TinyImageNet at 200/400 epochs.

## Open questions

- The cleanest statement for the heading that standard contrastive learning *is* a spectral method; pairs with k17 (which maps SimCLR to MDS/ISOMAP instead) — a deeper read should reconcile the two characterizations.
- Check the finite-object and symmetric-π assumptions and whether the "larger batch helps" reading is argued or only suggested.
- Kernel-InfoNCE gains are on small-scale datasets only; check effect sizes before treating as practice.
