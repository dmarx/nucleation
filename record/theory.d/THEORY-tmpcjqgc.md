---
status: Active
title: "In few-shot classification and multiple choice by language models up to 175B parameters, whether each demonstration's label is correct contributes little to the gain over zero-shot, while the distribution of the inputs, the label space and the paired format carry most of it"
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-10-16'
source:
- LIT-814
summary: >-
  Min et al. (2022), [LIT-814](../literature.d/LIT-814.md), read in [NOTE-607](../notes.d/NOTE-607.md). With k = 16 demonstrations,
  labels drawn at random from the correct label set cost 0–5 points
  against gold labels (2.6 on classification, 1.7 on multiple choice on
  average) across twelve model–inference combinations and 26 datasets.
  Out-of-distribution inputs, random English words as labels, or breaking
  the input–label pairing each cost far more. The random labels always
  come from the right label set, gaps reach about 14 points on single
  datasets, and the authors' reading that the models learn no new
  correspondence at test time is untested on tasks pretraining cannot
  have taught.
---
<!-- inactive-ok-file: CLAIM-029 — Proposed; the claim that reads this result as support, named, not leaned on -->

# THEORY-tmpcjqgc: In few-shot classification and multiple choice by language models up to 175B parameters, whether each demonstration's label is correct contributes little to the gain over zero-shot, while the distribution of the inputs, the label space and the paired format carry most of it

## Source

Min, Lyu, Holtzman, Artetxe, Lewis, Hajishirzi & Zettlemoyer (2022),
[LIT-814](../literature.d/LIT-814.md) (EMNLP 2022), read in full in [NOTE-607](../notes.d/NOTE-607.md).

## What was actually shown

**The decomposition.** A demonstration carries four things: the
input–label mapping, the distribution of the inputs, the label space and
the format (inputs paired with labels). Each is ablated alone, on
classification and multiple-choice tasks with small answer sets: 26
datasets, six language models from 774M to 175B parameters, each with
direct (P(y|x)) and channel (P(x|y)) inference.

**Labels (§4.1–4.2).** With k = 16, replacing gold labels by labels drawn
uniformly from the label set lowers accuracy by 0–5 points absolute: 2.6
on classification and 1.7 on multiple choice on average, and 0.1–0.9 for
the meta-trained MetaICL. All-incorrect labels keep 92%, 100% and 97% of
the gain in three of four settings. The gold–random gap stays at 0.8–1.6
points for k from 4 to 32.

**The rest (§5, four model–method pairs, nine datasets).**
Out-of-distribution sentences in place of the inputs cost 3–16 points for
most models. Random English words in place of the labels cost 5–16 points
for direct models and 0–2 for channel models. Removing the pairing,
inputs only or labels only, is about as bad as no demonstrations; keeping
the format with only one side real retains up to 95% (direct MetaICL) and
75–87% (channel) of the gain.

**What could have come out otherwise.** Random labels could have cost as
much as removing the demonstrations. They cost a few points.

## What this does not say

- **That labels do not matter.** The random labels always come from the
  correct label set, so the label space is always given. What matters
  little is which label goes with which input.
- **That the models learn nothing at test time.** That is the authors'
  interpretation (§6), drawn from the result and not tested on tasks whose
  correspondence cannot have been learned in pretraining. The authors
  predict the gap would open there.
- **That it holds for every dataset.** Macro-averages hide gaps up to
  about 14 points (financial_phrasebank with GPT-J), and Kim et al. (2022)
  find negated labels hurt substantially.
- **That it holds for generation.** Only classification and multiple
  choice were tested.
- **That one context does one thing.** Which parts act depends on the
  read-out: the label space matters for direct inference and hardly for
  channel inference, on the same model.

## Connections

- **Lu et al. ([LIT-833](../literature.d/LIT-833.md), [THEORY-tmpyh9bm](THEORY-tmpyh9bm.md))** vary a different axis: the
  order of a fixed set of demonstrations, which moves accuracy far more.
  Both say that what a context does to a fixed model is carried by its
  form more than by the correctness of its examples.
- **Xie et al. ([LIT-797](../literature.d/LIT-797.md))** give the latent-concept account the authors
  cite. On it, inputs, label space and format are evidence about the task,
  and the mapping is evidence the model can do without.
- **Akyürek et al. ([LIT-796](../literature.d/LIT-796.md), [THEORY-tmp4sei8](THEORY-tmp4sei8.md))** cite this paper for in-context
  learning not resembling standard learning, and show that updating the
  weights on the same demonstrations does more than conditioning on them.
- **[CLAIM-029](../claims.d/CLAIM-029.md)** reads this result as support for treating a context as a
  frame.
