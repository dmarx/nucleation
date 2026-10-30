---
status: Proposed
title: 'Merging models trained on different tasks from different initialisations fails where their features have no counterpart in the other model, and such features grow more common with depth'
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-30'
source:
- LIT-665
extends:
- THEORY-113
promote_when: >-
  A control the source does not run. Measure cross-model feature
  correlation layer by layer, and the accuracy of merging at each depth,
  for pairs trained from different initialisations on the same task and on
  disjoint tasks, at matched width. The account is supported if the
  disjoint-task pairs lose correspondence faster with depth, and merging
  fails at the depth where they do. It is refuted if same-task pairs show
  the same depth profile and the same merge failure, since then depth and
  initialisation, not task difference, are what remove the counterpart. It
  is also refuted if a merge that matches features one to one, after a
  better alignment than permutation, closes the gap to the ensemble without
  within-model merges or unmerged late layers. Further results in which
  partial zipping beats full merging would not settle it, because they are
  expected on either reading.
bears_on:
- QUESTION-316
summary: >-
  The wide form THEORY-113 held before the eleventh status review narrowed
  it, kept as a Proposed reading by the ADR-047 kind-1 sweep of
  2026-10-30: the source asserts it, and THEORY-113, Active, is its
  evidence.
---
<!-- inactive-ok-file: ADR-047 — Superseded by ADR-057, which keeps its evidence rulings; cited for the kind-1 rule this entry is filed under -->

# THEORY-tmpnozcu: Merging models trained on different tasks from different initialisations fails where their features have no counterpart in the other model, and such features grow more common with depth

## Source

Stoica, Bolya, Bjorner, Ramesh, Hearn & Hoffman (2023), ZipIt!, LIT-665,
read in NOTE-523. What its ResNets on disjoint halves of a label set
showed is THEORY-113, which this entry extends.

## The claim

Stoica et al. explain why permute-then-average fails for models trained on
different tasks. Permutation maps each feature of one model to exactly one
of the other, which assumes every feature has a counterpart. Models trained
on different tasks need not learn the same features, so the permuted
average lands outside both task basins (§3; NOTE-523, C1). Such unmatched
features grow more common with depth: cross-model feature correlation falls
from early to late layers, which is why the late layers should stay
separate (C5). Merging a feature with a redundant one in its own model
recovers what one-to-one matching cannot (C2, C4).

The evidence has no same-task control. Kornblith et al.'s fall in
similarity with depth is a same-task finding, so the depth profile may not
come from the task difference at all.

## What would settle it

The promote_when, which is QUESTION-316: the depth profile of
correspondence and of merge accuracy at matched width for same-task and
disjoint-task pairs, and a one-to-one merge after a better alignment than
permutation. Further results in which partial zipping beats full merging
cannot settle it.
