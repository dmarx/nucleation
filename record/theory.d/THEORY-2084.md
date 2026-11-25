---
number: 2084
status: Proposed
formerly:
- THEORY-tmpw8s3h
title: 'ULMFiT matches 10× labels with 100 examples'
statement: >-
  Howard and Ruder report that a language model pretrained on WikiText-103
  and fine-tuned to text classification by their method, given 100 labelled
  examples, matches the error that training from scratch reaches with ten
  times more labelled data on IMDb and twenty times on AG, and a hundred and
  fifty times with unlabelled task text added; they credit general-domain
  pretraining, though the low-shot comparison does not separate it from
  their fine-tuning method
version: 1
source:
- LIT-2852
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent replication with seeds of the low-shot comparison on IMDb
  or AG shows a pretrained and fine-tuned model reaching from-scratch
  error with about an order of magnitude fewer labelled examples; or an
  ablation crossing pretraining with label count, the fine-tuning
  procedure held fixed, attributes the saving to pretraining.
corroborates:
- CLAIM-756
summary: >-
  From the reading of [LIT-2852](../literature.d/LIT-2852.md) in [NOTE-2141](../notes.d/NOTE-2141.md). The cost measure the
  owner's point at U37 needed: labelled samples to a level. Proposed until
  its promote_when is met.
---

# THEORY-2084: ULMFiT matches 10× labels with 100 examples

## The account

Pretrain an LSTM language model on general text, fine-tune it on the
target task's text and then as a classifier, with per-layer learning
rates, a slanted triangular schedule and gradual unfreezing. On IMDb and
AG, 100 labelled examples match the error that training from scratch
reaches with ten and twenty times more labels; with the task's
unlabelled text also used, a hundred and fifty times. The authors credit
pretraining; their low-shot comparison is the whole method against
training from scratch, and their only ablation of pretraining is at full
data, where it helps most on the smallest dataset.

## Evidence

One figure of single runs on validation error, and ablation tables at
full data. Pretraining and unlabelled data are not counted as cost.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2059 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Hernandez and colleagues ([THEORY-2059](THEORY-2059.md)) use the same measure, from-
scratch data equivalence, and generalize it to a power law in fine-tuning
data and model size, with no special fine-tuning method to confound it;
like this account they leave pretraining's cost uncounted. Corroborating.
