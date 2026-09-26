---
number: 2
status: Proposed
formerly:
- THEORY-tmp4sf4k
promote_when: >-
  A proved stability result linking a distributional distance to a kernel
  distance (Bures or CKA) for a model family that includes contrastive or
  language-model objectives, or a measurement showing whether model pairs with
  high mutual-nearest-neighbour alignment also have high Bures alignment of
  their centred kernels.
title: 'Convergence of representations, in the Platonic hypothesis''s sense, is convergence of kernels, which fixes representations only up to the symmetry group of what is observed; closeness in distribution does not imply closeness of representation'
version: 1
tags:
- representation-learning
- philosophy-of-science
date: '2026-09-26'
source:
- LIT-253
- LIT-250
summary: >-
  An inference joining Huh et al.'s Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)) to
  Nielsen et al. ([LIT-253](../literature.d/LIT-253.md)) and Harvey, Larsen & Williams ([LIT-250](../literature.d/LIT-250.md)).
  It does not refute the hypothesis; it says what the hypothesis can and
  cannot mean.
extends:
- THEORY-004
---
<!-- inactive-ok-file: LIT-253 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-250 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-002: Convergence of representations, in the Platonic hypothesis's sense, is convergence of kernels, which fixes representations only up to the symmetry group of what is observed; closeness in distribution does not imply closeness of representation

## Source

Nielsen et al. (2025), [LIT-253](../literature.d/LIT-253.md), Thm 2.2, Thm 3.1, Cor. 3.2; Harvey, Larsen & Williams (2023), [LIT-250](../literature.d/LIT-250.md). The hypothesis itself is Huh et al. (2024), [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md), §4.2 and App. A.

## What was actually shown

Huh et al. ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md), §4.2) prove that, under bijective observations and an NCE objective, representations converge to the PMI kernel up to an offset — the log of the density ratio K⁺ that the contrastive losses target (see the first claim in this group). Their measurements, though, use mutual nearest neighbours (App. A), which is much weaker than kernel equality. Nielsen et al. show that for softmax models the output distribution fixes the embeddings only up to an invertible linear map, not an orthogonal one (Thm 2.2, cited from earlier work), and that ε-closeness in KL does not bound representational dissimilarity (Thm 3.1, Cor. 3.2). Harvey, Larsen & Williams supply the kernel-side metric under which kernel closeness is rotation-aligned closeness.

Read together: the defensible formal content of "representations converge" is that kernels converge, and the representation is then fixed only up to the symmetry group of the observed quantity — orthogonal if the kernel is observed, general linear if only the distribution is.

## What this does not say

- That the Platonic hypothesis is false.
- That trained models do, or do not, converge in kernel.
- That any one metric (Bures, CKA, mutual nearest neighbours) is the right one.
