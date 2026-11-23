---
status: Proposed
title: 'Lippl and Lindsey show that in diagonal linear and one-hidden-layer ReLU networks both multi-task learning and pretraining then fine-tuning are biased to reuse pretrained features and to learn a sparse set of new ones, that the two biases trade off exactly, and that fine-tuning has a nested feature selection regime, reached by rescaling the weights after pretraining, which favours a sparse subset of the pretrained features'
version: 1
source:
- LIT-tmpkuq67
tags:
- learning-theory
- representation-learning
date: '2026-11-23'
promote_when: >-
  A rigorous derivation or an independent replication confirms, for
  diagonal linear networks, the fine-tuning penalty of Corollary 2 and the
  law that ℓ-order and feature dependence sum to one, and shows in a
  teacher-student task whose main features are a subset of the
  pretrained ones that rescaling the weights after pretraining by a factor
  below one lowers fine-tuning's generalization error; or the implicit
  bias of gradient descent in ReLU networks is shown to match the explicit
  penalty of Proposition 3.
summary: >-
  From the reading of [LIT-tmpkuq67](../literature.d/LIT-tmpkuq67.md) in [NOTE-tmpw2i45](../notes.d/NOTE-tmpw2i45.md), carrying out the lead
  that asked for it. The theory Anguita and colleagues ([THEORY-2077](THEORY-2077.md))
  extend. Its rescaling, which keeps the pretrained function when the
  readout is compensated, gives [CLAIM-tmp7n00e](../claims.d/CLAIM-tmp7n00e.md)'s case of equal present
  function with different later learning. Proposed until its promote_when
  is met.
---
<!-- inactive-ok-file: THEORY-2077 CLAIM-tmp7n00e — Proposed; the reading that extends this one, and the claim filed by the lead run of 2026-11-23 -->

# THEORY-tmpw69kb: Lippl and Lindsey show that in diagonal linear and one-hidden-layer ReLU networks both multi-task learning and pretraining then fine-tuning are biased to reuse pretrained features and to learn a sparse set of new ones, that the two biases trade off exactly, and that fine-tuning has a nested feature selection regime, reached by rescaling the weights after pretraining, which favours a sparse subset of the pretrained features

## The account

Train a network on an auxiliary task, then on a main task, either jointly
(multi-task learning) or in sequence with the readout re-initialized
(pretraining then fine-tuning). Each paradigm finds the main-task
interpolant that minimizes a penalty set, dimension by dimension or unit
by unit, by what the auxiliary task learned. For a feature the auxiliary
task did not use, the penalty is ℓ1-like, so new features are learned
sparsely; for a large pretrained feature it is a weighted ℓ2, so large
pretrained features are reused. Locally, the sparsity of the penalty and
its dependence on the pretrained feature sum to one, so one is bought
with the other. Between the limits lies a regime that favours a sparse
subset of the pretrained features, nested feature selection. For
fine-tuning it is wide and is entered by shrinking the weights after
pretraining; for multi-task learning it is narrow. In ReLU networks
fine-tuning, and not multi-task learning, also benefits from features
correlated with the pretrained ones.

## Evidence

Corollary 2 applies known implicit-bias results for diagonal linear
networks from infinitesimal initialization; Proposition 3 is an explicit
penalty on weight change for ReLU networks, offered as a proxy for
implicit bias; Proposition 4 is the conservation law. Teacher-student
experiments agree, one of the ReLU findings being, by the authors'
account, a postdiction.
