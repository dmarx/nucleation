---
status: Open
title: "Do trained language models learn in context by implicit Bayesian inference over a latent concept: do their in-context predictions track the posterior predictive of a latent-concept mixture fitted to their pretraining data, or carry a readable posterior that concentrates as the theorems say?"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-19'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-614](../theory.d/THEORY-614.md), moved here unchanged on
  2026-10-19. [THEORY-614](../theory.d/THEORY-614.md)'s title is a conditional theorem about the
  pretraining distribution under exact fit, and it says that whether
  trained networks learn in context this way is not shown. The old
  condition asked for evidence on exactly that disclaimed point, so it
  is a question in its own right.
---

# QUESTION-tmpfmvmj: Do trained language models learn in context by implicit Bayesian inference over a latent concept: do their in-context predictions track the posterior predictive of a latent-concept mixture fitted to their pretraining data, or carry a readable posterior that concentrates as the theorems say?

## Why it is a question

[THEORY-614](../theory.d/THEORY-614.md) (Xie et al., [LIT-797](../literature.d/LIT-797.md)) states Theorem 1 for a mixture of
hidden Markov models under exact fit. A prompt of concatenated examples
moves the posterior onto the prompt's concept, and the in-context
predictor becomes Bayes-optimal as examples accumulate, provided each
example's evidence outweighs the cost of the transitions between
examples. Its title ends: "whether trained networks learn in context
this way is not shown". Its promotion condition asked for evidence about
trained networks. That is the disclaimed clause, not the title's claim,
so on 2026-10-19 the promotion audit (batch 026) moved it here and
pointed [THEORY-614](../theory.d/THEORY-614.md)'s condition at the proof of Theorem 1.

The question is open because the analysis is of the distribution, not
of a network. The only experiments, on GINC, use data built to satisfy
the assumptions ([NOTE-633](../notes.d/NOTE-633.md)).

## What would answer it

The condition formerly on [THEORY-614](../theory.d/THEORY-614.md), unchanged. Evidence about a
trained language model, not about the data distribution. Either a
demonstration that its in-context predictions track the posterior
predictive of an explicit latent-concept mixture fitted to its
pretraining data, across prompt lengths and example lengths, including
the order and zero-shot effects the account predicts from mismatch. Or a
measured posterior over concepts, read from the network, that
concentrates as the theorems say. Further results on synthetic data
built to satisfy the assumptions, such as GINC, cannot settle it, and
neither can a gain of under one point on a natural benchmark.
