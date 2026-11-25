---
number: 1020
status: Proposed
formerly:
- CLAIM-tmp41bjo
title: 'When a language model''s logit representation is the output of a final layer norm with a bias, every context representation has the same component along the direction proportional to the reciprocals of the gains, so the representations span the whole space when that common component is nonzero and only a hyperplane when it is zero'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-073 as a delegated
    lead worker. Checked by a test on tiny random models
    (scratch/studies/lead-073/test_geometry.py) and in GPT-2 small and
    Pythia-70m.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a final layer norm f = γ ⊙ ĥ + β, with
  ĥ of mean zero and all gains nonzero, whose outputs have a varying
  component along 1/γ, or whose span is not as stated when the normalised
  states ĥ span the mean-zero hyperplane. A model whose logits read something
  other than the layer-norm output, or add an output bias, is outside the
  claim and does not defeat it.
tags:
- representation-learning
- mathematics
date: '2026-11-23'
line:
- learned-structure
- formal-apparatus
grounds:
- CASE-398
bears_on:
- QUESTION-149
summary: >-
  For f = γ ⊙ ĥ + β with ĥ of mean zero, fᵀ(1/γ) = βᵀ(1/γ) for every input,
  so all context representations share one component along n ∝ 1/γ. If the
  ĥ span the mean-zero hyperplane, the span F of the representations is
  the whole space when Σ βᵢ/γᵢ ≠ 0 and the hyperplane diag(γ)1^⊥ when it
  is 0. That common component acts on the logits as a context-independent
  bias, c·g(y)ᵀn. It settles the diversity condition's F half for any such
  model from two weight vectors. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-398 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-1020: When a language model's logit representation is the output of a final layer norm with a bias, every context representation has the same component along the direction proportional to the reciprocals of the gains, so the representations span the whole space when that common component is nonzero and only a hyperplane when it is zero

## The claim

A final layer norm outputs f = γ ⊙ ĥ + β, where ĥ = (h − mean h)/sd(h)
has mean zero. With all γᵢ ≠ 0, write u = 1/γ. Then
fᵀu = Σ ĥᵢ + Σ βᵢ/γᵢ = Σ βᵢ/γᵢ =: c′, the same for every input. So every f
lies in the affine hyperplane {x : xᵀu = c′}. If c′ = 0 that hyperplane
passes through the origin and F has dimension at most d − 1. If c′ ≠ 0,
and the ĥ span the mean-zero hyperplane (as they generically do), the f
span the whole space: the differences between them span diag(γ)1^⊥, which
is u^⊥, and any single f adds the direction off it.

So the F half of the diversity condition ([NOTE-746](../notes.d/NOTE-746.md), Definition 1) is settled
for such a model by one number computed from its weights, and the
component that makes F full is constant over contexts. Its effect on the
logits is c·g(y)ᵀn with n = u/|u| and c = c′/|u|, a per-token bias that no
context changes. In [NOTE-746](../notes.d/NOTE-746.md)'s model, which has no output bias, this is
how such a bias appears.

In GPT-2 small, c = −1.82 against |f| of about 190. In Pythia-70m,
c = −2.4e-4 against |f| of about 440 ([CASE-398](../cases.d/CASE-398.md)).

## What it does not say

- Nothing about G, the unembedding half of the diversity condition, which
  is a separate rank question.
- Not that a model with c ≠ 0 is far from one with c = 0. When c is as
  small as Pythia-70m's, the two differ by a per-token bias of order 1e-5
  in the logits.
