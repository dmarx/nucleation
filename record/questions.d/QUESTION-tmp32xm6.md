---
status: Open
title: 'Is it the difference in task, and not depth and initialisation alone, that leaves features with no counterpart in the other model and makes merging fail: at matched width, do models trained from different initialisations on disjoint tasks lose cross-model feature correlation faster with depth than models trained on the same task, with merging failing at that depth?'
version: 1
tags:
- loss-landscapes
- representation-learning
date: '2026-10-29'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-113](../theory.d/THEORY-113.md), moved here when the
  eleventh status review narrowed it to what Stoica et al. measured, with
  their explanation given as theirs, and promoted it, as [THEORY-114](../theory.d/THEORY-114.md)'s
  moved to [QUESTION-312](QUESTION-312.md).
---

# QUESTION-tmp32xm6: Is it the difference in task, and not depth and initialisation alone, that leaves features with no counterpart in the other model and makes merging fail: at matched width, do models trained from different initialisations on disjoint tasks lose cross-model feature correlation faster with depth than models trained on the same task, with merging failing at that depth?

## Why it is a question

[THEORY-113](../theory.d/THEORY-113.md) holds that cross-model feature correlation fell with depth
between ResNets trained on disjoint halves of a label set, and that
merging only the early layers recovered most of the ensemble. Stoica et
al. attribute the failure of full merging to features with no counterpart
in the other model. Kornblith et al.'s fall in similarity with depth is a
same-task finding, and the paper runs no same-task control, so whether the
task difference adds anything to depth is not shown.

## What would answer it

[THEORY-113](../theory.d/THEORY-113.md)'s former promote_when, unchanged:

A control the source does not run. Measure cross-model feature
correlation layer by layer, and the accuracy of merging at each depth,
for pairs trained from different initialisations on the same task and
on disjoint tasks, at matched width. The account is supported if the
disjoint-task pairs lose correspondence faster with depth, and merging
fails at the depth where they do. It is refuted if same-task pairs show
the same depth profile and the same merge failure, since then depth and
initialisation, not task difference, are what remove the counterpart.
It is also refuted if a merge that matches features one to one, after a
better alignment than permutation, closes the gap to the ensemble
without within-model merges or unmerged late layers. Further results in
which partial zipping beats full merging would not settle it, because
they are expected on either reading.
