---
status: Proposed
promote_when: >-
  A controlled comparison: the same architecture trained on the same data
  with and without dropout (several seeds each), the same behaviour's
  circuit found in each, and the compensation measured the same way, as
  the share of the logit difference that survives knocking out the main
  output heads. Confirmed if compensation is large with dropout and small
  or absent without it; refuted if models trained without dropout
  compensate as much. Finding backup heads in more models trained with
  dropout cannot settle it, since that is the observation it would
  explain.
title: 'The attention heads in GPT-2 small that take over the indirect-object prediction when its main name mover heads are knocked out exist because the model was trained with dropout, which optimized it to be robust to disabled components, as Wang, Variengien, Conmy, Shlegeris and Steinhardt hypothesize'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmp1iis8, the reading of Wang et al. (2022) in
    full. The paper states the hypothesis in one sentence and does not
    test it. The compensation it would explain is measured and held in
    THEORY-tmpccb5u.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmpj9tel
summary: >-
  Wang et al. (2022), LIT-tmpj9tel, read in NOTE-tmp1iis8, §3.4: "We
  hypothesize that this compensation phenomenon is caused by the use of
  dropout during training. Thus, the model was optimized for robustness to
  dysfunctional parts." The compensation is real (a 5% loss of logit
  difference after knocking out the three name movers); the cause is not
  examined. Appendix F: "Both the reason and the mechanism of this
  compensation effect are still unclear."
---
<!-- inactive-ok-file: CLAIM-367 — Proposed; the claim about training-time conditions this bears on, cited as open -->

# THEORY-tmpmd4za: The attention heads in GPT-2 small that take over the indirect-object prediction when its main name mover heads are knocked out exist because the model was trained with dropout, which optimized it to be robust to disabled components, as Wang, Variengien, Conmy, Shlegeris and Steinhardt hypothesize

## Source

Wang et al. (2022), LIT-tmpj9tel, read in full in NOTE-tmp1iis8: §3.4 and
Appendix F.

## What is asserted

That redundancy in the trained network, heads that stay quiet in normal
operation and write the answer once the main heads are removed, is a
product of a training condition: dropout, which randomly disables
activations during training and so rewards computations that survive
missing parts.

## What the record holds toward it

- **The compensation**, measured (THEORY-tmpccb5u): knocking out name
  movers 9.9, 9.6 and 10.0 costs 5% of the logit difference, the negative
  name movers become less negative (10.7 turns positive), and eight backup
  heads become the main contributors.
- **Nothing on the cause.** No model trained without dropout is examined.
  The authors' footnote adds that perfect redundancy is unlikely under SGD,
  and more likely when one analyses a sub-distribution of the training data.

## Why it stays Proposed

It is a one-sentence hypothesis with an unexamined alternative, which is
the record's observation, not the paper's. Mean
ablation of heads that later heads read from changes those later heads'
inputs, and attention heads can change what they attend to when their
inputs change, which the backup heads' altered behaviour shows. So
compensation could come from how attention responds to the ablation, with
or without dropout.

## Connections

- **CLAIM-367 and CASE-113.** If it holds, it is a case of a property of a
  trained network (redundancy that hides components from single
  knockouts) whose source is a condition of the training regime, the
  optimizer–model–data system of CLAIM-367, not the network alone.
- **THEORY-tmpccb5u** holds the compensation this would explain.
