---
status: Active
title: 'In a one-layer transformer whose MLP has 512 ReLU neurons, a sparse autoencoder with 4,096 features trained on that layer''s activations yields features that a blinded rater and an automated pipeline judged far more interpretable than the neurons, that for the four features examined in detail correspond to no neuron, and whose effects on the output, which the autoencoder never saw, agree with their activations; splicing in the reconstruction recovers 79% of the loss reduction the MLP provides, measured against zero-ablating it'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpz50gz, the reading of Bricken et al. (2023)
    in full. One study, but the title claims no more than it measured,
    keeps its hedges (the four detailed features, the zero-ablation
    baseline), and nothing in the record contradicts it; MIB's result
    (THEORY-tmp4lqc8) is about a different test (ADR-047 v3). The paper's
    reading of feature splitting is the Proposed THEORY-tmpz7jrx.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpn9ui7
extended_by:
- THEORY-tmpz7jrx
summary: >-
  Bricken et al. (2023), [LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md), read in [NOTE-tmpz50gz](../notes.d/NOTE-tmpz50gz.md): the detailed
  investigations, the global analysis and the appendices, for run A/1 of
  model A. Median rubric score 0 for neurons and 12 for feature intervals
  (one author, 162 units); held-out logit prediction 74% against 58%; the
  Arabic, DNA, base64 and Hebrew features have no matching neuron. It says
  nothing about deeper models or other sites, nothing about whether the
  model is "composed of" these features, and nothing about how features
  compare with neurons as carriers of a known causal variable.
---
<!-- inactive-ok-file: THEORY-tmpz7jrx CLAIM-tmpwr001 — Proposed; the wider account filed from the same reading and the claim this bears on, cited as open -->
# THEORY-tmpkq43g: In a one-layer transformer whose MLP has 512 ReLU neurons, a sparse autoencoder with 4,096 features trained on that layer's activations yields features that a blinded rater and an automated pipeline judged far more interpretable than the neurons, that for the four features examined in detail correspond to no neuron, and whose effects on the output, which the autoencoder never saw, agree with their activations; splicing in the reconstruction recovers 79% of the loss reduction the MLP provides, measured against zero-ablating it

## Source

Bricken, Templeton, Batson, Chen, Jermyn et al. (2023), *Towards
monosemanticity*, [LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md), read in full in [NOTE-tmpz50gz](../notes.d/NOTE-tmpz50gz.md) from the
article's HTML: the detailed investigations of individual features, Global
Analysis, and the appendices on proxies, ablations, the rubric and
automated interpretability.

## What was actually shown

**The setting.** A transformer with one attention block and one MLP of
512 ReLU neurons (residual stream 128), trained on 100 billion Pile
tokens. The autoencoder A/1 has 4,096 features, of which 3,636 are live
and not "ultralow density"; it was trained on 8 billion MLP activations
with an MSE and L1 loss, seeing nothing downstream of the MLP.

**Interpretability.** One author, blinded, scored 412 activation intervals
over 162 features and neurons on a 0–14 rubric: median 0 for neurons
("could not even form a hypothesis"), 12 for feature intervals. Claude 2's
explanations predicted held-out activations better for features than for
neurons, and predicted held-out top logit tokens at 74% for features and
58% for neurons, against 50% chance.

**Not neurons.** The Arabic-script feature's most correlated neuron
responds to many languages, and its three largest neuron coefficients are
negative. No neuron has Hebrew among its top examples. The base64
feature's best-correlated neuron reaches 0.18.

**Effects agree with activations.** Logit weights, ablation of the
feature over a context, and sampling with the feature pinned high all
point the way its activations do, for the four detailed features and, by
the authors' report, in the feature browser for all. On a transformer with
shuffled weights the autoencoder finds mostly single-token features whose
other features the authors could not interpret.

**Loss.** Replacing the MLP's activations with A/1's reconstruction costs
21% of the loss that zero-ablating the MLP would. The authors call this
baseline "especially bad" and the percentage an overestimate.

**What could have come out otherwise.** The features could have been
rotated copies of neurons, or patterns of the data with no matching
effects on the output. The shuffled-weights control shows that the second
outcome happens when the model has not learned anything.

## What this does not say

- **Not about deeper models or other sites.** One MLP layer whose effect
  on the logits is nearly linear; the authors say this makes linear
  features likelier here.
- **Not that all features are interpretable.** Lower activation intervals
  are less consistent, and the detailed cases are chosen to be easy.
- **Not that the model is composed of these features.** The authors are
  "agnostic" on that, and the feature set depends on width and penalty
  ([THEORY-tmpz7jrx](THEORY-tmpz7jrx.md)).
- **Not that features carry known causal variables better than neurons.**
  That is a different test, and in MIB they did worse ([THEORY-tmp4lqc8](THEORY-tmp4lqc8.md)).

## Connections

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The paper itself treats activation structure and
  role as separate evidence, and a control shows activation structure
  arising from data alone. A supporting case of the claim's distinction,
  not a test of it.
- **[LIT-323](../literature.d/LIT-323.md).** The empirical counterpart of the superposition hypothesis's
  prediction that more features than neurons are stored.
- **[THEORY-tmp4lqc8](THEORY-tmp4lqc8.md).** Compatible: better interpretability and worse
  localization of supplied variables are both measured, by different
  tests.
