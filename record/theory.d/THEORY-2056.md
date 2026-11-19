---
number: 2056
status: Proposed
formerly:
- THEORY-tmpzauel
title: 'Yin and colleagues show that when meta-training tasks are not mutually exclusive, MAML and conditional neural processes can learn a single function that solves every training task without using its training data, reaching lower meta-training error than an adapting solution yet failing on new tasks, that standard weight regularization does not prevent this, and that penalizing the information held in the meta-parameters not used for adaptation does'
version: 1
source:
- LIT-2838
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-495
promote_when: >-
  The record accepts the memorization result as reported: an independent
  study (such as Rajendran et al., LIT-2817) reproduces near-chance or
  sharply worse meta-test performance for MAML or CNP on non-mutually-
  exclusive tasks, with high pre-update training accuracy, and a gain from
  penalizing the information in the non-adapted meta-parameters.
summary: >-
  From the reading of [LIT-2838](../literature.d/LIT-2838.md) in [NOTE-2116](../notes.d/NOTE-2116.md). Yin, Tucker, Zhou,
  Levine and Finn (2020), ICLR 2020, arXiv 1912.03820. They show that when
  meta-training tasks are not mutually exclusive, MAML and conditional
  neural processes can memorize one function that solves every training
  task without using its training data, with lower meta-training error
  than an adapting solution and poor performance on new tasks; ordinary
  weight regularization does not prevent it, while penalizing the
  information in the meta-parameters not used for adaptation does. Here
  because A54 used it for meta-overfitting, a design rule of CASE-
  tmphsr99: the reading supports the rule and adds pre-update accuracy on
  training tasks as its diagnostic. It also bears on [CLAIM-758](../claims.d/CLAIM-758.md), since
  the authors name this loss of adaptability task-level overfitting. Read
  in its NOTE.
---
<!-- inactive-ok-file: CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2056: Yin and colleagues show that when meta-training tasks are not mutually exclusive, MAML and conditional neural processes can learn a single function that solves every training task without using its training data, reaching lower meta-training error than an adapting solution yet failing on new tasks, that standard weight regularization does not prevent this, and that penalizing the information held in the meta-parameters not used for adaptation does

## The account

If a task can be inferred from the test input alone, a meta-learner can
ignore the task training set, so that I(ŷ*; D | x*, θ) = 0 (Definition 1).
On non-mutually-exclusive sinusoids, pose prediction and modified
Omniglot and MiniImagenet, MAML and CNP often converge to this solution,
which has lower training error than the adapting one; pre-update accuracy
on training tasks is high and meta-test accuracy low. Weight decay and
Bayes-by-Backprop do not cure it; meta-regularization of the
non-adapted weights does (NME Omniglot 20-way 1-shot, 7.8% to 83.3%). The
authors distinguish this from conventional overfitting as task-level and
function-level.

## What it does not show

That memorization occurs in large pretrained models or in-context
learners; that mutually exclusive task design is sufficient against all
meta-overfitting (Rajendran et al. add learner overfitting); anything
about adaptation to task families outside the meta-training distribution.
