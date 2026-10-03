---
number: 104
status: Proposed
formerly:
- THEORY-tmp13uaq
promote_when: >-
  Two kinds of result, one for each source's weak point. For language
  models: the early-exit or linear-readout comparison of Chang et al.'s
  Table 1 on a natural task with a real shift, not only the synthetic
  arithmetic task, showing out-of-distribution accuracy peaking below the
  last layer while in-distribution accuracy keeps rising. For the layer
  choice: a study in which the layer is chosen on one out-of-distribution
  split and scored on a disjoint one, in a large pretrained model and not
  only a task-specific one, and the intermediate layer still beats the
  penultimate. The account is refuted if, once selection and scoring are
  separated, the penultimate layer is as good out of distribution as the
  best earlier one, or if the effect is confined to small task-specific
  models and disappears in pretrained ones. More layer-wise curves of the
  matrix-based information estimate cannot settle it, since what that
  estimate measures is in question.
title: 'Under distribution shift the best layer for a linear readout lies below the top: across the last layers of a trained network, in-distribution accuracy rises while out-of-distribution accuracy falls'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-03'
source:
- LIT-678
- LIT-657
summary: >-
  Uselis & Oh (2025), [LIT-678](../literature.d/LIT-678.md): linear probes on frozen intermediate
  layers of image classifiers beat last-layer retraining under shift, with
  zero-shot worst-group accuracy 79.4 → 87.1 (Waterbirds) and 56.0 → 82.0
  (CelebA), layer 7 of 8 beating layer 8 on every subpopulation dataset,
  while in-distribution accuracy is best at the last layer. Chang, Deng &
  Chen (2025), [LIT-657](../literature.d/LIT-657.md): in GPT-2 Small on a synthetic task, early-exit
  out-of-distribution accuracy peaks at layer 10 (56.90%) and falls to
  50.00% at layer 12 while in-distribution accuracy climbs to 93.17%. The
  layer is chosen on out-of-distribution data throughout; ViT gains are
  small; the language-model evidence is one synthetic task; and Chang et
  al.'s information estimate is questioned in its NOTE.
---
<!-- inactive-ok-file: THEORY-083 — Proposed; named in Connections as the record's statement of neural collapse, nothing here rests on it -->

# THEORY-104: Under distribution shift the best layer for a linear readout lies below the top: across the last layers of a trained network, in-distribution accuracy rises while out-of-distribution accuracy falls

## Source

- Uselis & Oh (2025), [LIT-678](../literature.d/LIT-678.md), read in [NOTE-541](../notes.d/NOTE-541.md): Sections 4–5
  (Figures 3–9), Appendices A.2, A.4, B.1.1 (Figure 18), C.1–C.3.
- Chang, Deng & Chen (2025), [LIT-657](../literature.d/LIT-657.md), read in [NOTE-536](../notes.d/NOTE-536.md): Section
  4.1 (Table 1, Figure 2), Section 4.2 (Figures 3–4), Appendix E.

## The claim

**In image classifiers.** Uselis and Oh ([LIT-678](../literature.d/LIT-678.md)) fit linear
classifiers on the frozen features of each layer of publicly released,
task-specific ResNets and ViTs, and compare them with retraining the last
layer, on conditional, subpopulation, corruption and natural shifts. With
plenty of out-of-distribution data for the probe, the best intermediate
ResNet layer beats last-layer retraining by +16.8, +6.3, +1.6 and +6.3
points on CMNIST, CIFAR-10C, CIFAR-100C and MultiCelebA (Figure 3). With
probes trained on in-distribution data only, worst-group accuracy goes
from last layer to best layer as 79.4% → 87.1% on Waterbirds, 56.0% →
82.0% on CelebA and 20.8% → 46.0% on MultiCelebA (Figure 5). The step down
from the top is visible one layer below it: layer 7 of 8 beats layer 8 in
both settings on every subpopulation dataset, for example 86.7% against
79.4% zero-shot on Waterbirds (Figure 8). The in-distribution side runs
the other way: "while ID performance generally increases with deeper
layers ... OOD performance does not exhibit the same trend" (Appendix
B.1.1, Figure 18), and "in-distribution data is best classified at the
last layer" (A.4). Non-linear probes and PCA to equal dimension give the
same picture (C.2, C.3).

**In a language model.** Chang, Deng and Chen ([LIT-657](../literature.d/LIT-657.md)) fine-tune
GPT-2 Small on a synthetic arithmetic-progression task, with the modulus
held at 13 in distribution and drawn from 5 to 25 out of it, and exit
early after each layer (Table 1). Out-of-distribution accuracy reaches
56.90% at layer 10, then falls to 52.67% and 50.00% at layers 11 and 12.
Over the same two layers in-distribution accuracy rises from 53.40% to
79.17% and 93.17%. That is the trade in one table: the last two blocks buy
about forty points in distribution and give up about seven out of it. The
paper's residual-scaling probe agrees in direction: per-block scales
fitted with all weights frozen put relatively less weight on the last
blocks when fitted on out-of-distribution data than on in-distribution
data (Figure 4).

The two together are the claim: the last layers specialize to the
training distribution, so the layer whose features best support a linear
readout under shift is below the top, and the cost of the specialization
is paid out of distribution.

## What Chang et al.'s information profile does and does not add

Chang et al.'s headline is a layer-wise profile of a matrix-based Rényi
estimate of I(Zℓ; Y) between the last-token state and the target token's
input embedding, which rises, peaks in the upper-middle layers and falls,
the "generalization ridge". Its NOTE questions what that estimate
measures, and this account does not rest on it. In Table 1 the estimate
is 0.0188 at layer 12, about its layer-6 value of 0.0185, yet layer 12's
early exit decodes the target with 93.17% in-distribution accuracy and
layer 6's with 0%. Shannon information about the target cannot be near
zero where the target is decoded that well. What falls in the last layers
is the alignment between the Gaussian-kernel geometry of the hidden states
at bandwidth 1 and that of the target embeddings ([NOTE-536](../notes.d/NOTE-536.md); the point
is the reading's, not the paper's). The ridge's coincidence with the best
out-of-distribution exit is a real observation. The early-exit accuracies
are the evidence here, not the estimate.

## What this does not say

- **It does not say the layer can be chosen without out-of-distribution
  data.** Uselis and Oh choose the layer on out-of-distribution validation
  data in every setting, a standard practice they adopt for comparability,
  and in the information-content experiment the validation set is the test
  set (oracle selection, A.2.1). "Zero-shot" there means no
  out-of-distribution training data, not none at all. A best-of-eight
  choice made on the scoring data overstates the gain.
- **It is weak for vision transformers.** ViT gains in the
  information-content experiment are +1.1, +1.3 and −0.2 points.
- **The language-model evidence is one synthetic task.** The early-exit
  table is GPT-2 Small on arithmetic progressions. On CLUTRR, ECQA and
  CNN/DailyMail the ridge is shown only in the questioned estimate, not in
  out-of-distribution accuracy.
- **It does not establish why.** Uselis and Oh's sensitivity score finds
  penultimate features displaced further by the shift than intermediate
  ones, most for minority groups (Figure 9), and their penultimate layer is
  also the most collapsed (C.1). Both are correlations at the same layer.
  Chang et al.'s "memorization" in the final layers is inferred from
  accuracies, not measured.
- **It does not locate the best layer.** It varies by dataset, and between
  CIFAR-10C and CIFAR-100C for the same corruption (C.4).
- **It is about small, task-specific models.** No large pretrained vision
  model is probed layer-wise for this comparison, and in Li et al.'s
  pretrained-model study, as Uselis and Oh report it, the most collapsed
  layer depends on the downstream task.

## Connections

- **Neural collapse** ([LIT-618](../literature.d/LIT-618.md), stated in the record as [THEORY-083](THEORY-083.md)) is
  Uselis and Oh's named candidate for why the last layer transfers badly:
  classes collapsed to their means keep little else. Their C.1 shows
  collapse strongest at the layer where out-of-distribution probes do
  worst, which is consistent with it and does not test it.
- **Anthology.** The nearest holdings are the measurement that middle
  transformer layers tolerate deletion and reordering while the first and
  last do not ([ANTH-THEORY-020](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-020.md)), and the logit lens for reading
  intermediate predictions ([ANTH-LIT-570](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-570.md)); neither source cites them. The
  anthology's practice of reporting zero-shot and in-distribution
  performance separately, because one hyperparameter can move them in
  opposite directions ([ANTH-SOTA-196](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-196.md)), is the same trade seen across a
  training knob rather than across depth.
