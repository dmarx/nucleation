---
number: 171
status: Open
formerly:
- QUESTION-tmp06usk
title: "Do volume-maximizing joint-embedding objectives prefer equal-sized clusters as they are actually trained, and does the preference cost semantic transfer on naturally long-tailed data?"
version: 1
tags:
- representation-learning
- probabilistic-modeling
date: '2026-10-19'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-306](../theory.d/THEORY-306.md), moved here when [THEORY-306](../theory.d/THEORY-306.md)
  was narrowed to MSN's and SwAV's explicit prior and one study's
  imbalanced-batch measurement, and promoted on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v3).
  [LIT-231](../literature.d/LIT-231.md) reaches the same prior for VICReg only through an informal
  reduction of a simplified loss to K-means, and for SimCLR only through a
  cited equivalence. Its imbalance experiment uses two to eight ImageNet
  classes per batch, not a natural long tail.
answered_by:
- THEORY-tmp0gm1u
---

# QUESTION-171: Do volume-maximizing joint-embedding objectives prefer equal-sized clusters as they are actually trained, and does the preference cost semantic transfer on naturally long-tailed data?

## Why it is a question

Assran et al. ([LIT-231](../literature.d/LIT-231.md), read in full in [NOTE-850](../notes.d/NOTE-850.md)) show that MSN's
regularizer is a KL penalty pulling soft cluster sizes toward uniform and
that SwAV enforces equal sizes outright. With mini-batches of two to eight
ImageNet classes, SimCLR, MSN and VICReg lose 11 to 18 points of ImageNet
linear accuracy while MAE and data2vec do not ([THEORY-306](../theory.d/THEORY-306.md)). For VICReg the
prior is derived only for a simplified loss with γ ≫ α, with an informal
last step and a cited property of K-means. For SimCLR nothing is derived.
The imbalance is extreme and artificial, each cell is a single run, and
the methods compared differ in architecture. Until 2026-10-19 this was
[THEORY-306](../theory.d/THEORY-306.md)'s promote_when. [THEORY-306](../theory.d/THEORY-306.md)'s body disclaimed it, so the clause
moved here when the title was narrowed.

## What would answer it

For the prior: a derivation of the cluster-size preference for the losses
as used (VICReg with its hinge variance term, SimCLR at finite
temperature), or a measurement of the cluster-size distribution that
trained VICReg and SimCLR models induce on data with known unequal
classes. For the effect: the imbalance experiment repeated with batches
sampled uniformly from a naturally long-tailed dataset, at one
architecture across methods, with seeds. It would answer no for a method
if its learned partitions track unequal class sizes as well as an
instance-based method's do.

What would not answer it: more results with two-class batches, or gains
from a prior matched with labels.
