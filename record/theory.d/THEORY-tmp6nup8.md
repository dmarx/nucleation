---
status: Active
title: 'In two 7–8B chat models, the shift that finetuning induces along a difference-of-means persona vector correlates with how strongly the finetuned model then expresses that trait, r = 0.76–0.97 across synthetic datasets for evil, sycophancy and hallucination, above cross-trait baselines of 0.34–0.86; the last-prompt-token projection predicts a response''s trait at r = 0.75–0.83 overall but mainly by telling prompt types apart'
version: 1
tags:
- representation-learning
- self
date: '2026-11-03'
source:
- LIT-tmpyjvij
summary: >-
  Chen et al. (2025), [LIT-tmpyjvij](../literature.d/LIT-tmpyjvij.md), read in [NOTE-tmpp25f6](../notes.d/NOTE-tmpp25f6.md) (main text in
  full, appendices C.2, G.2 and M). Active as the reported measurements,
  with their sizes and scope: two models, three main traits, synthetic
  datasets and an LLM judge. It does not say that persona vectors are the
  mechanism of persona change, which the authors leave open, or that the
  method finds personas it was not told to look for.
---
<!-- inactive-ok-file: NOTE-tmpp25f6 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->

# THEORY-tmp6nup8: In two 7–8B chat models, the shift that finetuning induces along a difference-of-means persona vector correlates with how strongly the finetuned model then expresses that trait, r = 0.76–0.97 across synthetic datasets for evil, sycophancy and hallucination, above cross-trait baselines of 0.34–0.86; the last-prompt-token projection predicts a response's trait at r = 0.75–0.83 overall but mainly by telling prompt types apart

## Source

Chen, Arditi, Sleight, Evans and Lindsey (2025), [LIT-tmpyjvij](../literature.d/LIT-tmpyjvij.md),
arXiv:2507.21509v3; read in [NOTE-tmpp25f6](../notes.d/NOTE-tmpp25f6.md).

## What was actually shown

**Finetuning shift** (§4.2, Figure 6). For each finetuned model, the mean
last-prompt-token activation change from the base model, projected on the
unit persona vector, against the judge's post-finetuning trait score:
r = 0.76–0.97 over the datasets of Figure 5, for Qwen2.5-7B-Instruct and
Llama-3.1-8B-Instruct. Cross-trait correlations are r = 0.34–0.86 (footnote
6, Appendix G.2), so the vectors are specific but not cleanly so; negative
traits and humor shift together.

**Prompt-time projection** (§3.3, Appendix C.2). Overall r = 0.747
(evil), 0.798 (sycophancy), 0.830 (hallucination) under system-prompt
interpolation; within a condition 0.511, 0.669, 0.245. The authors: the
correlation arises "primarily from distinguishing between different prompt
types", and persona vectors "may be less reliable for more subtle behavioral
changes" (p. 5).

The finetuning correlation could have failed: emergent-misalignment
datasets that contain no trait expression could have moved behaviour
without moving the vector. In the reported data they did not.

## What this does not say

- That the vector is the trait's mechanism: penalizing movement along it
  during training fails, suspected because the trait is re-encoded in other
  directions (p. 9).
- That it holds at other scales or in models that refuse the eliciting
  prompts (§8).
- That a persona vector is a component of a persona distribution: the paper
  fits no distribution over personas.
