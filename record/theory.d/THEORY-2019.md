---
number: 2019
status: Proposed
formerly:
- THEORY-tmpbzf9h
title: 'Nichol, Achiam and Schulman show that Reptile, which repeatedly trains on a sampled task for k steps and moves the initialization toward the result, matches MAML on few-shot Omniglot and Mini-ImageNet with first-order gradients only, and that to leading order its update and MAML''s both combine joint training on the expected loss with a term that raises the inner product of gradients from different mini-batches of one task, a term that grows with the step size and the number of inner steps and vanishes at one step'
version: 1
source:
- LIT-2791
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-495
promote_when: >-
  The record accepts the Taylor-series result and the benchmark comparison
  as reported: the leading-order expansion is checked (by the record or a
  later reading), and an independent replication finds Reptile within a
  few points of MAML on few-shot Omniglot and Mini-ImageNet.
summary: >-
  From the reading of [LIT-2791](../literature.d/LIT-2791.md) in [NOTE-2102](../notes.d/NOTE-2102.md). Nichol, Achiam and
  Schulman (2018), OpenAI, arXiv 1803.02999. Reptile meta-learns an
  initialization by repeatedly training on a sampled task and moving the
  initialization toward the result; it matches MAML on few-shot Omniglot
  and Mini-ImageNet with first-order gradients only, and a Taylor
  expansion shows its update, like MAML's, is joint training plus a term
  rewarding generalization between mini-batches of one task, a term that
  grows with step size and inner steps and is absent at one step. The
  authors suggest plain SGD does part of this already and that joint
  training plus fine-tuning stays a strong baseline; their RL results were
  negative. Here because A54 proposed it as the meta-trained arm of CASE-
  tmphsr99: the reading supports it as a cheap arm, with joint training on
  the same tasks as its control and the inner budget k fixed. Read in its
  NOTE.
---

# THEORY-2019: Nichol, Achiam and Schulman show that Reptile, which repeatedly trains on a sampled task for k steps and moves the initialization toward the result, matches MAML on few-shot Omniglot and Mini-ImageNet with first-order gradients only, and that to leading order its update and MAML's both combine joint training on the expected loss with a term that raises the inner product of gradients from different mini-batches of one task, a term that grows with the step size and the number of inner steps and vanishes at one step

## The account

Reptile updates φ ← φ + ε(φ̃ − φ), where φ̃ is the result of k steps of SGD
or Adam on a sampled task (§3). With k = 1 this is SGD on the expected loss;
with k > 1 the expected update carries second-order terms. Expanding to
O(α²), MAML, first-order MAML and Reptile all equal a multiple of AvgGrad,
the gradient of the expected loss, minus a multiple of AvgGradInner, the
gradient of the inner product of gradients from two mini-batches of the
same task; the AvgGradInner coefficient grows with αk (§5.1). On the
sine-wave case, where joint training learns the zero function, Reptile
learns an initialization that fits a sampled wave after 32 steps (§4).
Few-shot accuracy is close to MAML's (§6.1). The authors suggest ordinary
SGD performs "a MAML-like update" and that joint training plus fine-tuning
remains a strong baseline (§7).

## What it does not show

Adaptation to tasks outside the training distribution; any RL success (the
authors report negative results); that the informal account, a point close to
all the tasks' solution manifolds, holds; the claim about ordinary SGD, which is a
suggestion from the expansion, not a tested result.
