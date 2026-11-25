---
number: 2053
status: Proposed
formerly:
- THEORY-tmpy398k
title: 'Label re-keying curbs meta-overfitting'
statement: >-
  Rajendran, Irpan and Jang show that meta-learners can overfit either by
  ignoring the support set (memorization) or by a base learner that fails on
  new tasks (learner overfitting), and that randomly re-keying each task's
  labels, the same key in support and query, which makes tasks mutually
  exclusive, improves meta-test performance on non-mutually-exclusive
  few-shot classification and pose regression, on top of Yin et al.'s
  meta-regularization
version: 1
source:
- LIT-2817
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-495
promote_when: >-
  The record accepts the ablations as reported: an independent study finds
  that removing label shuffling from a few-shot benchmark sharply lowers
  MAML's meta-test accuracy and that restoring it, or adding a label-
  keying augmentation, recovers most of the loss.
summary: >-
  From the reading of [LIT-2817](../literature.d/LIT-2817.md) in [NOTE-2089](../notes.d/NOTE-2089.md). Rajendran, Irpan and
  Jang (2020), NeurIPS 2020, arXiv 2007.05549. They separate memorization
  overfitting, where the model ignores the support set, from learner
  overfitting, where the base learner fails on new tasks even when tasks
  are mutually exclusive, and show that re-keying each task's labels at
  random (label shuffling for classification, shared noise for regression)
  improves meta-test performance, on top of Yin et al.'s meta-
  regularization; Mini-ImageNet MAML rose from 30% to 46%. Here because
  A54 used it beside Yin et al. ([LIT-2838](../literature.d/LIT-2838.md)) for [CASE-294](../cases.d/CASE-294.md): the
  reading supports the case's held-out task-generating processes, since
  learner overfitting survives shuffling, and adds two rules, several
  seeds and pre/post-update accuracy as the diagnostic. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-294 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2053: Label re-keying curbs meta-overfitting

## The account

An augmentation that raises the conditional entropy H(Y|X) by an invertible
key ε forces the learner to extract at least H(ε) bits from the support set
(Theorem 1), so the model cannot solve the training tasks from the query
input alone. On Mini-ImageNet with MAML, making tasks mutually exclusive by
shuffling within fixed class groups raised accuracy from 30% to 43%, and
shuffling across groups to 46%; on D'Claw from 72.5% to 83.1%; on Pascal3D
pose, noise on the targets improved MAML, MR-MAML, CNP and MR-CNP. Whether a
non-augmented run memorizes or overfits the learner depends on the seed.

## What it does not show

That augmentation closes the gap between training and test task
distributions (the authors say it may not); results beyond small
benchmarks; anything about large pretrained or in-context learners.
