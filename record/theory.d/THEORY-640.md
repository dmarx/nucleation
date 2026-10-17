---
number: 640
status: Active
formerly:
- THEORY-tmptjbe9
title: "Measured as mutual 10-nearest-neighbour overlap, competent vision models agree more with one another and better language models agree more with vision models, but the cross-modal score reaches only 0.16 of a possible 1, is the maximum over all layer pairs, and was adopted after a global kernel metric showed only a very weak trend"
version: 1
tags:
- representation-learning
- philosophy-of-science
date: '2026-10-16'
source:
- LIT-302
summary: >-
  Huh, Cheung, Wang & Isola (2024), [LIT-302](../literature.d/LIT-302.md), read in [NOTE-286](../notes.d/NOTE-286.md). Across 78
  vision models, those solving more VTAB tasks agree more in mutual
  k-nearest-neighbour structure; language models with lower bits-per-byte
  agree more with vision models on 1,024 image–caption pairs. The
  cross-modal score "only reaches 0.16" of 1, is maximised over layer
  pairs, and the metric was chosen after CKA "revealed a very weak trend".
  It is local neighbourhood agreement that rises with competence, not
  kernel equality and not convergence to a model of reality.
---
<!-- inactive-ok-file: THEORY-002 THEORY-008 — Proposed; the formal reading of the hypothesis and an account of readout agreement, set beside this measurement, not leaned on -->

# THEORY-640: Measured as mutual 10-nearest-neighbour overlap, competent vision models agree more with one another and better language models agree more with vision models, but the cross-modal score reaches only 0.16 of a possible 1, is the maximum over all layer pairs, and was adopted after a global kernel metric showed only a very weak trend

## Source

Huh, Cheung, Wang & Isola (2024), [LIT-302](../literature.d/LIT-302.md) (ICML 2024), read in full in
[NOTE-286](../notes.d/NOTE-286.md), Appendices A–F included.

## What was actually shown

**The metric.** For paired samples, mutual k-NN is the overlap of the k = 10
nearest-neighbour sets of each point in the two models' feature spaces,
averaged (App. A, eq. 11). Features are l2-normalised, activations above
the 95th percentile are truncated, language features are average-pooled
hidden states, and the cross-modal score is the maximum over all layer
pairs, concatenations included (App. C.2). The authors moved to this
metric because CKA "revealed a very weak trend of alignment between
models, even when comparing models within their own modality" (App. A).

**Vision against vision (Fig. 2).** 78 models on 1,000 Places-365 images.
Models that solve more of the 19 VTAB tasks have higher alignment within
their bucket. Across these models, mutual k-NN and linear CKA rank model
pairs with Spearman 0.73 (Fig. 12, printed).

**Language against vision (Fig. 3).** BLOOM, OpenLLaMA and LLaMA models
against DINOv2, MAE, ImageNet-21K and CLIP models, on 1,024 WIT
image–caption pairs. Alignment rises roughly linearly with 1 − bits-per-byte.
It "only reaches a score of 0.16 … The maximum theoretical value for this
metric is 1", and whether that is strong or poor alignment is left open
(§6).

**Denser captions (Fig. 9).** Alignment rises from 5-word to 30-word
captions, which are LLaMA3-8B summaries of dense captions.

**What could have come out otherwise.** Alignment could have been flat in
competence. It was not. It could have been large in absolute terms. It
was not.

## What this does not say

- **That representations converge to one kernel.** The paper's formal
  argument (§4.2, App. F) shows that in an idealised world of discrete
  events seen through bijective observations, the Bayes-optimal NCE critic
  is the PMI kernel plus a constant, so such modalities share one kernel.
  That prediction, equality of dot-product kernels up to a constant, is
  never tested. The measured kernel is cosine, truncated, pooled and
  maximised over layers.
- **That the endpoint is "a statistical model of reality".** The proof
  reaches the PMI of windowed co-occurrence, "certain pairwise statistics
  of P(Z)" in the paper's words, which does not determine P(Z). That trained
  models reach even that optimum "with sufficient data and optimization"
  is asserted in one sentence.
- **That convergence is large.** The authors themselves leave 0.16 open
  as "poor alignment with major differences left to explain".
- **That scale is the variable.** Fig. 3's axis is language-modelling
  score, not parameter count.
- **That alignment predicts downstream skill.** Fig. 4's correlations with
  HellaSwag and GSM8K are scatter plots with no statistic.

## Connections

- **[THEORY-002](THEORY-002.md)** says what the Platonic hypothesis can mean formally:
  convergence of kernels, fixing representations only up to the symmetry
  of what is observed. This account is the measured half beside it, and
  its gap from kernel equality is the gap [THEORY-002](THEORY-002.md)'s promote_when names.
- **[THEORY-004](THEORY-004.md).** The paper defines a representation by its kernel (§2),
  which is orthogonal equivalence; it adopts that account's notion of
  sameness rather than disputing it ([NOTE-286](../notes.d/NOTE-286.md), Corrections).
- **[THEORY-008](THEORY-008.md).** Mutual k-NN is not an average of readout agreement, so
  that account's link between alignment and decodability does not carry
  to these numbers without an argument.
- **The anthology** holds the paper as [ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md) with [ANTH-THEORY-036](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-036.md).
  [NOTE-286](../notes.d/NOTE-286.md) reports that the anthology's reading omits the metric history
  and the 0.16 ceiling.
