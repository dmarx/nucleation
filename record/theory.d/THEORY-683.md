---
number: 683
status: Active
formerly:
- THEORY-tmpyh9bm
title: "Permuting a fixed set of few-shot examples moves a GPT-family model's classification accuracy between near chance and near the supervised state of the art, at every model size tested; the good orders are specific to the model, the spread survives more examples and calibration, and bad orders mostly fail by predicting one label"
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-10-16'
source:
- LIT-833
summary: >-
  Lu et al. (2021, ACL 2022), [LIT-833](../literature.d/LIT-833.md), read in [NOTE-626](../notes.d/NOTE-626.md). All 24 orders of
  four balanced SST-2 examples give accuracies from about 50% to above
  85%, in GPT-2 and GPT-3 models of eight sizes; Spearman correlations of
  order accuracy between sizes lie between −0.35 and 0.27 (175B against
  2.7B: 0.05). The variance stays high up to 32 examples and after
  calibration. It is a measurement on causal GPT models and text
  classification, with the transfer analysis resting on one example set,
  and the paper finds no property of an order that predicts its effect.
supports:
- CLAIM-248
---
<!-- inactive-ok-file: THEORY-251 — Proposed; a qualification of this measurement, named, not leaned on -->

# THEORY-683: Permuting a fixed set of few-shot examples moves a GPT-family model's classification accuracy between near chance and near the supervised state of the art, at every model size tested; the good orders are specific to the model, the spread survives more examples and calibration, and bad orders mostly fail by predicting one label

## Source

Lu, Bartolo, Moore, Riedel & Stenetorp (2021; ACL 2022), [LIT-833](../literature.d/LIT-833.md), read in
full in [NOTE-626](../notes.d/NOTE-626.md).

## What was actually shown

**The setting.** Eleven text-classification datasets, answered by the most
probable label word after a template. k = 4 examples (fewer for DBPedia
and AGNews), five example sets per task, all 24 orders (two sets and 12
orders for GPT-3 175B), 256 validation items.

**Order alone (Fig. 1).** For a fixed balanced set of four SST-2 examples,
some orders score above 85% and others near 50%, in every one of eight
GPT-2 and GPT-3 sizes. The spread shrinks with size on SST-2, not on Subj.

**Not a small-sample effect (Fig. 3).** From 1 to 32 examples (GPT-2,
at most 24 orders sampled), accuracy rises and the variance stays high.

**Not transferable (Figs. 4–5).** Spearman correlations of order accuracy
between model sizes lie between −0.35 and 0.27 off the diagonal; 175B
against 2.7B is 0.05. For the six label patterns, correlations range from
−0.66 to 0.77, so no pattern is consistently good.

**How bad orders fail (Fig. 6).** Mostly by a highly unbalanced predicted
label distribution. Calibration raises accuracy but leaves the spread.

**What could have come out otherwise.** Order could have mattered little
once the examples were fixed, or the good orders could have been shared
across sizes. Neither happened.

## What this does not say

- **Why an order works.** The paper finds no common denominator. The
  label-collapse observation describes the failure, not its cause.
- **That order sensitivity is a property of in-context learning in
  general.** The authors' conclusion (C6 in [NOTE-626](../notes.d/NOTE-626.md)) is tested only on
  causal GPT models, classification, and small k.
- **That good orders never transfer.** The transfer analysis rests on one
  fixed set of four SST-2 examples.
- **Anything about the selection method.** The paper's entropy-based
  order selection is an instruction for practice, which belongs to the
  anthology; this account is the measurement only.

## Connections

- **Min et al. ([LIT-814](../literature.d/LIT-814.md), [THEORY-496](THEORY-496.md))** ablate a different axis, which
  label goes with which input, and find it matters little. Both say a
  context's effect on a fixed model is carried by its form; this one adds
  that the form's effect is idiosyncratic to the model.
- **Kirsanov et al. ([LIT-946](../literature.d/LIT-946.md), [THEORY-251](THEORY-251.md))** find that across draws of
  examples the class representations barely move while accuracy swings,
  with the failure at the vocabulary readout. They varied which examples
  were drawn, not their order, so that qualifies this account without
  settling its case.
- **Xie et al. ([LIT-797](../literature.d/LIT-797.md))** reproduce a 10–40 point order effect in their
  synthetic GINC data, where it follows from the prompt's mismatch with
  pretraining.
- **[CLAIM-248](../claims.d/CLAIM-248.md)** cites this result: one model is not enough, because what
  works for one model does not for another.
