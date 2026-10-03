---
number: 541
status: Read
formerly:
- NOTE-tmpvuq1m
paper: 'LIT-678'
title: 'Intermediate Layer Classifiers for OOD generalization'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v1 (30 pages, text layer, ICLR 2025 camera-ready
    header). Sections 1–6 read in full. Appendices read for the setup (A.1–
    A.3), comparisons with other methods (A.5.2, A.6), neural collapse
    (C.1), non-linear probes (C.2), PCA dimensionality control (C.3) and
    layer transfer (C.4); A.4, A.7–A.9 and B.1–B.2 skimmed. The equations
    for the ILC and the sensitivity score did not survive text extraction
    and are described from the prose. Numbers are those the text states;
    plotted values not stated in the text are not reported.
date: '2026-10-03'
summary: >-
  ILC_l(x) = W_l r_l(x) + b_l on frozen layer-l features, l ≤ L − 2, layer
  chosen on OOD validation data. Few-shot, best ILC minus last-layer
  retraining: +16.8, +6.3, +1.6, +6.3 points (ResNets on CMNIST, CIFAR-10,
  CIFAR-100C, MultiCelebA); +27.0 on MultiCelebA at π ≤ 0.03. Zero-shot
  worst-group accuracy: Waterbirds 79.4 → 87.1, CelebA 56.0 → 82.0,
  MultiCelebA 20.8 → 46.0. Layer 7 beats 8 everywhere in Figure 8.
  Intermediate features are less displaced by shift for minority groups.
---

<!-- inactive-ok-file: THEORY-083 — Proposed; named as the record's statement of neural collapse, with no relation claimed -->

# NOTE-541: Intermediate Layer Classifiers for OOD generalization

## Contribution

A broad measurement that last-layer retraining, the standard cheap fix for
distribution shift (Kirichenko et al.'s deep feature reweighting and its
relatives), uses the wrong layer more often than not. Linear probes on an
intermediate layer are better with a little OOD data. With none at all
(probes trained in-distribution, only the layer chosen on OOD validation),
they still beat retraining the last layer, sometimes by more than twenty
points of worst-group accuracy.

## Key insight

Training specializes the last layers to the training distribution. In
particular, they map rare groups, which the training set barely covers, far
away from where the classifier was fit. Earlier layers have not yet done
that, so they keep the information that identifies the class under the new
distribution in a place a linear probe can reach. The question to ask of a
pretrained classifier under shift is not "is the penultimate layer good
enough" but "which layer is".

## Assumptions

- **Frozen, publicly released task-specific models**: ResNet-18/50 and
  ViTs trained on each dataset; no backbone fine-tuning.
- **Layer granularity**: a ResNet has L = 8 layers (blocks) excluding the
  head; a ViT layer is an encoder block. ILCs at l ≤ L − 2 are compared
  with retraining at L − 1.
- **Probes**: linear on flattened raw features (no pooling); non-linear
  MLP probes only in C.2.
- **Model selection uses OOD data.** Layer and hyperparameters are chosen
  on an OOD validation split in both settings, "a standard practice" in the
  OOD literature that the authors adopt for comparability (Section 3.1).
  "Zero-shot" therefore means zero OOD training data, not zero OOD data.
- **Shift types** (Table 2): conditional shift (CMNIST), subpopulation
  shift (Waterbirds, CelebA, MultiCelebA), input noise (CIFAR-10C,
  CIFAR-100C), and style or natural shift (ImageNet-A, ImageNet-R,
  cue-conflict, silhouette).

## Key results

- **Information content (Section 4.2.1, Figure 3).** With the whole OOD
  validation set as probe data, ResNet gains of +16.8 (CMNIST), +6.3
  (CIFAR-10), +1.6 (CIFAR-100C) and +6.3 (MultiCelebA, worst-group). ViT
  gains of +1.1, +1.3 and −0.2. Non-linear probes (C.2) and PCA to 512
  dimensions per layer (C.3, Table 7: layer 6 best before and after) give
  the same picture.
- **Data efficiency (4.2.2, Figure 4).** At π ≤ 0.03 of the OOD data, +5.7,
  +3.4, +27.0 (Waterbirds, CelebA, MultiCelebA). At π = 0.25, +12, +3.6,
  +1.0 (CMNIST, CIFAR-10C, CIFAR-100C). ViTs follow the pattern less
  strongly.
- **Zero-shot, subpopulation (4.3.1, Figure 5).** Worst-group accuracy
  Base < Last layer < Best layer on all three datasets, with Last → Best
  79.4 → 87.1, 56.0 → 82.0, 20.8 → 46.0. Retraining the last layer on the
  same training set already beats the original head, which the authors
  flag as unexplained.
- **Zero-shot, input noise (4.3.2, Figure 6).** +2 to +5 points of mean
  accuracy on CIFAR-10C across models, with a ViT reaching 71%; +3 (ResNet-
  18) and +1 (ViT) on CIFAR-100C.
- **Zero-shot, ImageNet variants (4.3.3, Figure 7).** About +2 on
  cue-conflict and silhouette, +0.91 on ImageNet-A, +0.34 on ImageNet-R.
- **Comparisons (A.5.2, A.6).** Few-shot ILCs beat last-layer retraining
  and multi-objective optimization (Kim et al.) on all datasets in Table 3.
  Zero-shot ILCs beat JTT and DFR and lose to Correct-N-Contrast, which
  trains a specialized model (Table 4).
- **Depth (5.1, Figure 8).** Layer 7 beats layer 8 in both settings on
  every subpopulation dataset; for example Waterbirds worst-group 94.0%
  against 93.9% few-shot and 86.7% against 79.4% zero-shot. The best layer
  varies by dataset and, in C.4, between CIFAR-10C and CIFAR-100C for the
  same corruption.
- **Sensitivity (5.2, Figures 9–10).** Minority groups have higher
  sensitivity scores than majority groups at deeper layers. For minority
  groups, intermediate layers score lower, "often collapsing to a single low
  value", while the penultimate layer stays high. PCA projections show the
  largest train–test separation at layer 8 for minority groups.
- **Neural collapse (C.1, Figures 22–23).** The class-distance normalized
  variance is lowest (most collapsed) at the penultimate layer on CIFAR-10C
  and CIFAR-100C, under shift as in distribution.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Intermediate layers often hold more linearly accessible OOD information than the penultimate layer | moderate to strong for ResNets on these datasets; weak for ViTs | Figure 3, C.2, C.3 |
| C2 | The advantage grows as OOD probe data shrink | moderate | Figure 4 |
| C3 | ID-trained intermediate probes beat last-layer retraining OOD, given OOD model selection | moderate: large gains under subpopulation shift, small on ImageNet variants | Figures 5–7, Table 4 |
| C4 | The pen-penultimate layer beats the penultimate layer | moderate: consistent across the datasets shown, small in some (94.0 against 93.9) | Figure 8, C.4 |
| C5 | Intermediate layers are less sensitive to distribution shift, and this explains the gains | weak to moderate: the sensitivity score supports the first half; the explanation is stated as "may be due to" | Section 5.2 |

## Method

For each layer l ≤ L − 2 of a frozen network, flatten the layer's output
and fit a linear classifier on the probe set (OOD samples for few-shot, the
training set for zero-shot). Choose the layer and hyperparameters on OOD
validation data, then truncate the network at that layer for inference
(Algorithm 1).

## Concepts

- **ILC**: an affine map from a frozen intermediate representation to
  logits, trained for OOD classification.
- **few-shot / zero-shot OOD**: probe trained on a few OOD samples / on ID
  samples only.
- **worst-group accuracy (WGA)**: minimum accuracy over subpopulations.
- **sensitivity score**: within a group, the mean train-to-test pairwise
  distance at layer l normalized by the mean pairwise distance among probe
  points; 0 means test points sit as close to training points as those do
  to each other.

## Connections

- **Kirichenko et al. (2023), Izmailov et al. (2022), Rosenfeld et al.
  (2022), Kang et al. (2020)**: the last-layer retraining line this
  challenges. None is held in the record.
- **Neural collapse ([LIT-618](../literature.d/LIT-618.md))**: cited in the main text as a reason the last
  layer transfers poorly, and measured layer-wise in C.1.
- **Masarczyk et al.'s tunnel effect**: later layers compress the linearly
  separable representation built earlier, which degrades OOD transfer; named
  as complementary.
- **Ansuini et al.**: intrinsic dimension rising then falling with depth.

## Bearing on the record

- **[THEORY-083](../theory.d/THEORY-083.md) (neural collapse).** The record's statement is about the
  last layer in the terminal phase. This paper adds that, for OOD use, the
  penultimate layer is also where class-irrelevant but shift-relevant
  variation is most suppressed. It does not show causation: the collapse
  proxy and the OOD deficit peak at the same layer.
- **Generalization Ridge ([LIT-657](../literature.d/LIT-657.md))** takes this paper's finding as a
  premise, in transformers for generation.
- **THEORY candidate (not filed):** "In a trained classifier, the layer
  whose features best support a linear classifier under distribution shift
  is usually before the penultimate one, because the last layers map
  under-represented groups away from the training points while earlier
  layers keep them close." Source this paper and [LIT-657](../literature.d/LIT-657.md); promote when
  the sensitivity explanation is tested by intervention (for example,
  regularizing penultimate collapse and measuring OOD probe accuracy).
- **Anthology.** It carries a direct practice instruction, so it is an
  anthology candidate. The anthology's [ANTH-THEORY-020](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-020.md) (middle layers are
  robust to deletion) is a different measurement of the same non-uniformity
  of depth.

## Limitations

- **OOD data choose the layer in every setting**, so "zero-shot" is not
  free of OOD information.
- **ViT gains are small or negative** in the information-content
  experiment.
- **Layers are coarse**: eight ResNet blocks. Within-block layers are not
  probed.
- **Raw flattened features** give early CNN layers very high dimension
  (8,192 at layer 5 of ResNet-18 on CIFAR). C.3 controls for this on one
  dataset and model.
- **The explanation is correlational.** Sensitivity and neural collapse are
  measured, not manipulated.

## Open questions

- Why does retraining the last layer on the same training data improve OOD
  worst-group accuracy over the original head?
- Can the layer be chosen without OOD validation data?
- Does the effect hold for large pretrained (not task-specific) models,
  where Li et al. found the most collapsed layer to vary with the task?

## Corrections

- none (there was no seed)
