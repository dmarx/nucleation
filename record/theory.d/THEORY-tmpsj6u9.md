---
status: Proposed
promote_when: >-
  A replication on a dataset with real, not simulated, mixed-granularity
  annotations, or an independent reimplementation, that reproduces the
  gap in leaf accuracy over a baseline discarding coarse labels on
  CIFAR-100 or FGVC-Aircraft at ρ ≥ 0.9, and the recovery of withheld
  fine labels well above that baseline. Not met by a restatement that
  cites this paper. Not defeated by a showing that a Euclidean or
  differently weighted variant does as well, which the title does not
  assert against.
title: "Ghadimi Atigh and colleagues find that an image classifier with a class tree embedded as hyperbolic prototypes, trained on labels from any level of the tree with a coarse label as a uniform target over its leaves, an entailment-cone penalty toward the label's cone and a Busemann pull toward the label's boundary direction, reaches far higher leaf accuracy than one that discards the coarse labels, and recovers withheld fine labels, when most labels are coarse"
version: 1
tags:
- representation-learning
date: '2026-11-22'
source:
- LIT-2993
corroborates:
- CLAIM-839
- CLAIM-816
summary: >-
  Ghadimi Atigh, van Spengler, Long, Ayoughi, Kasarla & Mettes (2026),
  [LIT-2993](../literature.d/LIT-2993.md), read in [NOTE-tmpyyvdy](../notes.d/NOTE-tmpyyvdy.md). Supervision as a region whose
  narrowness matches the label's specificity, with depth by radius. The
  sharp edges: coarsening is simulated uniformly at random; some leaf
  labels always remain; the prototypes are fixed, so nothing moves but
  the images; and the radial placement has to be enforced by a separate
  Busemann term, which hurts when few labels are coarse. Its
  "coarse-to-fine" names a label projection, not an order of learning.
  Proposed until replicated.
---

# THEORY-tmpsj6u9: Ghadimi Atigh and colleagues find that an image classifier with a class tree embedded as hyperbolic prototypes, trained on labels from any level of the tree with a coarse label as a uniform target over its leaves, an entailment-cone penalty toward the label's cone and a Busemann pull toward the label's boundary direction, reaches far higher leaf accuracy than one that discards the coarse labels, and recovers withheld fine labels, when most labels are coarse

## Source

Ghadimi Atigh, van Spengler, Long, Ayoughi, Kasarla & Mettes (2026),
"Hyperbolic Learning with Supervision from any Granularity", AISTATS
2026, PMLR 300:2674–2682, [LIT-2993](../literature.d/LIT-2993.md), read in [NOTE-tmpyyvdy](../notes.d/NOTE-tmpyyvdy.md).

## What was actually shown

- **Observed:** on CIFAR-100 with 95% of leaf labels replaced by random
  ancestors, leaf accuracy 20.22% for a baseline that discards coarse
  labels, 56.13% with all three losses (Table 1); on FGVC-Aircraft at
  ρ = 0.95, 4.14% against 62.55% (Table 2).
- **Observed:** withheld fine labels on the training set recovered at
  69.88% (ρ = 0.95) and 62.50% (ρ = 0.975), against 20.30% and 12.36%
  (Table 3).
- **Observed:** the Busemann term lowers accuracy at ρ = 0.5 and raises it
  at high ρ (Table 1).
- Three runs per setting; one external baseline.

## What this does not say

- Anything about learning dynamics, checkpoints or the order in which
  distinctions are acquired.
- That real annotators' coarse labels behave like uniform random
  ancestors.
- That entailment cones alone place samples at the right depth: the
  paper adds the Busemann term because they do not.
