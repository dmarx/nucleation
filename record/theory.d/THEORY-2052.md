---
number: 2052
status: Proposed
formerly:
- THEORY-tmpxdk37
title: 'Transformers learn function classes in context'
statement: >-
  Garg and colleagues show that a transformer trained from scratch on
  prompts of input–output pairs from a simple function class learns unseen
  functions of that class in context about as well as the standard
  estimator: least squares for linear functions, near Lasso for sparse ones,
  better than greedy learning and boosting for depth-4 decision trees, and
  like a gradient-trained network for two-layer ReLU networks, and on linear
  functions it tracks least squares under several shifts of the prompt
  distribution
version: 1
source:
- LIT-2839
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
corroborates:
- CLAIM-118
promote_when: >-
  An independent replication trains a transformer on prompts from linear
  (or sparse linear) functions and finds held-out-function error close to
  least squares (or Lasso), including under at least one of the reported
  shifts such as noisy labels or mismatched orthants.
summary: >-
  From the reading of [LIT-2839](../literature.d/LIT-2839.md) in [NOTE-2103](../notes.d/NOTE-2103.md). Garg, Tsipras, Liang
  and Valiant (2022; arXiv 2208.01066, v3 Aug 2023) define in-context
  learning of a function class as a property of a fixed model and train
  small transformers from scratch to achieve it. On unseen 20-dimensional
  linear functions the trained model matches least squares, and it stays
  close under noisy labels, subspace inputs and mismatched orthants.
  Trained on sparse linear functions, depth-4 trees or two-layer networks,
  it nears Lasso, beats greedy tree learning and XGBoost, and matches a
  gradient-trained network. It is fragile under input scaling and skewed
  covariance, and the authors leave open what this means for language
  models. Here because A56 cited it for in-context learning as a learned
  algorithm. It is the behavioural counterpart to the exact identities of
  [THEORY-169](THEORY-169.md) and a case of [CLAIM-118](../claims.d/CLAIM-118.md)'s split between a learned interpreter
  and a discarded per-sequence fit. Read in its NOTE.
---

# THEORY-2052: Transformers learn function classes in context

## The account

In-context learning of a function class is a property of a fixed model: low expected error at a query given k pairs (x, f(x)) for f drawn from a distribution over the class. A 12-layer, 9.5M-parameter transformer trained on such prompts achieves it. On 20-dimensional linear functions it matches least squares at every k, which memorizing the 32M training functions cannot explain. Its local gradient aligns with the projected true weights. It stays close to least squares with noisy labels, a low-dimensional input subspace, or in-context and query inputs in different orthants. The same recipe yields Lasso-like use of sparsity, decision-tree learning better than greedy fitting or XGBoost, and two-layer-network learning matched to Adam on the same examples. Capacity helps, most under shift.

## What it does not show

- What algorithm is implemented: the evidence is behavioural.
- Anything about language models trained on text; the authors leave that open.
- Robustness in general: error grows under skewed covariance and when inputs are scaled by 1/3 or 3.
- That the model does gradient descent.

## Note of 2026-11-19: Brown and colleagues, read
A parallel ([NOTE-2160](../notes.d/NOTE-2160.md)): a from-scratch case of the de novo end of the spectrum Brown and colleagues leave open, where an outer loop provably yields in-context learning of unseen functions.
