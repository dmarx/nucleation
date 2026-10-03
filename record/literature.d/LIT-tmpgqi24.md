---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmp9flp3](../notes.d/NOTE-tmp9flp3.md)), main text and Appendices A–F, the proof in Appendix G followed to its reduction to Entezari et al.; worth reading as the case that permutation is the wrong symmetry for merging models trained on different tasks. ZipIt! matches features by activation correlation within each model as well as across the two, and can stop merging at a chosen layer, leaving a multi-head model. On disjoint halves of CIFAR-10 it reaches 79.1% joint accuracy where Git Re-Basin reaches 46.2%, and partial zipping comes within a few points of the ensemble. Its theorem tightens Entezari et al.''s barrier bound when a model has redundant units. With full merging on ImageNet-1k it is no better than a permutation baseline (8.6%), so the gains there come from leaving later layers unmerged.'
title: 'ZipIt! Merging Models from Different Tasks without Training'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v3 (13 March 2024). Semantic
    Scholar lists it at ICLR 2024 (DBLP key conf/iclr/StoicaBBRHH24); the
    arXiv record gives no venue. Filed with the owner's batch on mode
    connectivity and model merging (ADR-027). Not held in the Anthology of
    the SOTA: a grep of its record for the arXiv id, "ZipIt" and "Stoica"
    found nothing. The anthology holds the work it is measured against, Git
    Re-Basin (ANTH-LIT-333), and the practice of aligning permutations
    before averaging (ANTH-SOTA-217).
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-03'
published: '2023-05-04'
arxiv: '2305.03053'
first_author: 'Stoica'
keywords:
- 'model merging'
- 'feature matching'
- 'permutation'
- 'partial zipping'
- 'multi-task model'
- 'linear mode connectivity'
- 'redundant features'
extends:
- LIT-tmp2uwzo
compared_against:
- LIT-tmpd6bma
implementations:
- 'https://github.com/gstoica27/ZipIt'
summary: >-
  Stoica, Bolya, Bjorner, Ramesh, Hearn & Hoffman (2023), ICLR 2024.
  Merging differently initialised models trained on disjoint tasks fails
  under permutation, because the permuted model sits in a basin for its own
  task and not the other's. ZipIt! instead merges correlated features
  within and across models through merge and unmerge matrices, and can
  stop merging part-way, giving a shared trunk with task heads. The
  abstract reports a 20–60% improvement over prior work on CIFAR and
  ImageNet splits; it comes near the ensemble with partial zipping, and proves a
  tighter LMC barrier bound than Entezari et al. when units are redundant.
---


# LIT-tmpgqi24: ZipIt! Merging Models from Different Tasks without Training

George Stoica, Daniel Bolya, Jakob Bjorner, Pratik Ramesh, Taylor Hearn and Judy Hoffman (2023), ICLR 2024 — [ARXIV-2305.03053](https://arxiv.org/abs/2305.03053)

## Key takeaways

- **Permutation is the wrong alignment when tasks differ.** A permutation
  maps each feature of one model to exactly one feature of the other, which
  assumes the two models learned the same features. Trained on disjoint label
  sets, they did not: the permuted model lies in a low-loss basin for its
  own task but not for the other, so the average performs worse than either
  parent (§3, Fig. 2).
- **Merge within as well as across, and stop early.** ZipIt! computes
  correlations among all features of both models together, greedily pairs
  the most correlated features whether in one model or across both, and
  averages each pair. Merge and unmerge matrices are fused into each layer
  (Eq. 8); restricting merges to cross-model pairs recovers permute-then-
  average exactly. A "partial zip" merges only the first layers, then hands
  the merged features to each model's remaining layers as task heads (§4).
- **Results.** CIFAR-10 (5+5), ResNet-20×4, joint 10-way accuracy: Git
  Re-Basin 46.2, the paper's permutation baseline 58.4, ZipIt! 79.1 fully
  merged and 83.8 with 13 of 20 layers merged, ensemble 87.4 (Table 1a). On
  ImageNet-1k (200+200) full merging gives 3.1 (Git Re-Basin), 8.6
  (permute) and 8.6 (ZipIt!); merging 10 of 50 layers gives 60.9 against an
  ensemble of 63.3 (Table 2). The benefit of within-model merges grows with
  width (Fig. 7b) and vanishes when the model is too narrow for redundancy.

## Standing in the record

Filed with the owner's batch on mode connectivity and model merging, under
`loss-landscapes` ([ADR-027](../decisions.d/ADR-027.md)). Merging here is argued from the landscape, as
that decision expects: the obstacle is that two models lie in different
task basins, and the remedy changes the transformation used to bring them
together. `representation-learning` is the second topic because the method
works on feature correlations, and its central evidence is that features of
two models decorrelate with depth (App. A, Table 5, after Kornblith et al.).

It extends Entezari et al. ([LIT-tmp2uwzo](LIT-tmp2uwzo.md)). Its Theorem 1 (App. G) takes
their Theorem 3.1, a bound on the barrier between two wide two-layer
networks after permutation, and adds reductions through redundant units
(after Simsek et al.). The bound shrinks by a factor (1 − 2Γ)^{1/(2d+4)},
where Γ is the fraction of redundant features, and is zero when Γ ≥ 0.5. The
proof repeats theirs for everything except the reduction step. The paper
cites the conjecture of Entezari et al. as the reason permutation-based
merging works at all, and argues that the conjecture is about same-task
models.

It is compared against Git Re-Basin ([LIT-tmpd6bma](LIT-tmpd6bma.md); [ANTH-LIT-333](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-333.md)), whose
weight-matching variant it runs as a baseline in Tables 1, 2 and 6, and its
Eq. 8 reduces to Git Re-Basin's permute-then-interpolate when within-model
merges are disallowed. The anthology's practice of aligning permutations
before averaging ([ANTH-SOTA-217](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-217.md)) is the practice this paper narrows: it
holds for same-task models and fails across tasks.

Within the batch, TIES-Merging ([LIT-tmpqhwnd](LIT-tmpqhwnd.md)) and Gueta et al. ([LIT-tmp9gt28](LIT-tmp9gt28.md))
are cited in its related work as merging from a shared initialisation, the
setting it explicitly leaves.
