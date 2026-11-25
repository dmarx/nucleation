---
number: 2007
status: Proposed
formerly:
- THEORY-tmp3hfjg
title: 'Test-time training improves robustness to shift'
statement: >-
  Sun and colleagues show that fine-tuning a jointly trained network's
  shared features on a self-supervised task formed from each unlabeled test
  image, before predicting, improves image classification under distribution
  shift without hurting the original distribution, that keeping the update
  across a stream of test images improves it further, and that the gain
  tracks the alignment of the self-supervised and main-task gradients
version: 1
source:
- LIT-2821
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-095
corroborates:
- CLAIM-118
promote_when: >-
  An independent replication on CIFAR-10-C or ImageNet-C shows standard
  TTT beating the fixed jointly trained model, online TTT beating standard
  TTT, no loss on the original test set, and a positive correlation
  between gain and gradient inner product.
summary: >-
  From the reading of [LIT-2821](../literature.d/LIT-2821.md) in [NOTE-2128](../notes.d/NOTE-2128.md). Sun, Wang, Liu,
  Miller, Efros and Hardt (2020), ICML 2020, arXiv 1909.13231. The paper
  that named test-time training: before predicting, a jointly trained
  network fine-tunes its shared features on a self-supervised task
  (rotation prediction) built from the single unlabeled test image, then
  discards the update or, in the online version, keeps it for the next
  image. It improves classification under corruption, video and CIFAR-10.1
  shifts without hurting the original test set, and the gain tracks the
  alignment of the two tasks' gradients (proved for convex losses). Here
  because the owner raised test-time training at U26: its discarded and
  kept updates are the two sides of [CLAIM-118](../claims.d/CLAIM-118.md), and its appendix prices the
  work moved to test time ([QUESTION-095](../questions.d/QUESTION-095.md)). Read in its NOTE.
---

# THEORY-2007: Test-time training improves robustness to shift

## The account

A ResNet is trained on classification and rotation prediction with a shared feature extractor. At test time the extractor takes gradient steps on the rotation loss of the test image's augmented copies, then predicts. Under 15 corruption types at five levels, on video frames and on CIFAR-10.1, this beats both the plain model and the jointly trained model held fixed. Carrying the update from one test image to the next (online TTT) improves further, beats an unsupervised domain-adaptation oracle on 13 of 15 corruptions, and tolerates gradually changing shift. In a convex model, one step helps whenever the two losses' gradients have positive inner product; on the deep model the measured inner product correlates with the gain (r = 0.93 and 0.89).

## What it does not show

That it works beyond image classification with rotation prediction, or with self-supervised tasks whose gradients are not aligned with the main task's; that the convex guarantee holds for deep networks (only a correlation); anything about cost beyond A2's slowdown factor; any account of when moving the work to test time pays.
