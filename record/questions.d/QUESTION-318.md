---
number: 318
status: Open
formerly:
- QUESTION-tmpxygjx
title: 'Does layerwise linear feature connectivity hold outside image classification, in transformers and language models connected by spawning, shared pretraining or alignment, and does it carry from pairs to the many-model averages practice uses, model soups and SWA?'
version: 1
tags:
- loss-landscapes
- representation-learning
date: '2026-10-29'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-111](../theory.d/THEORY-111.md), moved here when the
  eleventh status review narrowed it to the pairs of image classifiers its
  source measured and promoted it, as [THEORY-114](../theory.d/THEORY-114.md)'s moved to [QUESTION-312](QUESTION-312.md).
---

# QUESTION-318: Does layerwise linear feature connectivity hold outside image classification, in transformers and language models connected by spawning, shared pretraining or alignment, and does it carry from pairs to the many-model averages practice uses, model soups and SWA?

## Why it is a question

[THEORY-111](../theory.d/THEORY-111.md) holds that, between two linearly connected image classifiers,
nearly every layer's features at three points on the line were
proportional to the interpolation of the endpoints' features. Every
measurement is of a pair of endpoints, in image classification. Whether
the same holds in other architectures and tasks, and whether averaging many
models' weights averages their features, is not shown.

## What would answer it

[THEORY-111](../theory.d/THEORY-111.md)'s former promote_when, unchanged:

Two kinds of result, one for each half. For the layerwise claim, the
same measurement outside image classification: transformers and
language models, linearly connected by spawning, by fine-tuning from a
shared pretrained model or by alignment. It is refuted by a pair that
is linearly connected at the output while some intermediate layer's
interpolated features point away from the interpolated features. For
the averaging claim, the measurement on the averages practice actually
uses: soups of many fine-tuned models and SWA iterates, with the
features of the averaged network compared with the average of the
members' features. It is refuted if the claim holds for pairs but
fails for many-model averages. An approximate version of Zhou et al.'s
Theorem 1, bounding the feature error by the size of the
weak-additivity and commutativity residuals, would also move it. More
pairwise image-classifier measurements would not.

## Note of 2026-11-15: Zhou et al. (2024) and Zhu (2026), read

<!-- inactive-ok-file: THEORY-tmpjlixb THEORY-tmpqakuv THEORY-tmpkfmi5 — Proposed; the readings of 2026-11-15 that bear on this question, cited as partial evidence, none answers it -->

Two readings of 2026-11-15 answer parts of both halves; neither half is settled.

**Layerwise half.**
- Zhou et al. (2024), "On the Emergence of Cross-Task Linearity in the Pretraining-Finetuning Paradigm", [LIT-tmptiitv](../literature.d/LIT-tmptiitv.md) ([THEORY-tmpjlixb](../theory.d/THEORY-tmpjlixb.md)), is the direct measurement this question asks for. They measure layerwise linearity, approximate equality and not only proportionality, in transformers (CLIP ViT-B/32 and L/14) and an encoder-decoder language model (T5-base, pooled features) connected by fine-tuning from a shared pretrained model, with no refuting pair reported. Most plots are of the last few blocks.
- Zhu (2026), [LIT-tmpdc2rl](../literature.d/LIT-tmpdc2rl.md), read in [NOTE-tmpsyjfz](../notes.d/NOTE-tmpsyjfz.md) ([THEORY-tmpqakuv](../theory.d/THEORY-tmpqakuv.md)), replicates cross-task linearity in decoder-only language models. In task-arithmetic merges of two LoRA task vectors into Qwen2.5 and Llama-3.2 models from one base, "layerwise linearity cosines are 0.93–0.98 across every family" (§7). It is partial, for three reasons. The construction is a sum of task vectors added to the base, not an interpolation between two endpoints. Only the final prompt token is read. And the measure is a cosine, not [THEORY-111](../theory.d/THEORY-111.md)'s proportionality of interpolated to interpolated features. The same paper shows the small residual is causally effective on output non-additivity, so "nearly linear" is not "nothing interacting".

**Averaging half.** Zhou et al.'s soups of 5 and 10 ViT-B/32 fine-tunes have averaged networks whose features approximate the members' average (all blocks for the ImageNet soup). Zhu's v3 six-vector merges, skimmed only, are many-model sums whose interaction grows with the number of vectors.

**Not measured or not given.** SWA iterates; pairs connected by spawning or alignment outside image classification; an interpolation between language-model endpoints. Nor is the approximate version of Zhou et al.'s (2023) Theorem 1 given: Zhou et al.'s (2024) Theorem 5.1 bounds a scalar's deviation by sharpness times squared distance, not feature error by the weak-additivity and commutativity residuals. Ortiz-Jimenez et al. ([THEORY-tmpkfmi5](../theory.d/THEORY-tmpkfmi5.md)) give the tangent-space limit, where the output is exactly linear in the weights, but measure no layer features. No status change.
