---
number: 2185
status: Proposed
formerly:
- THEORY-tmp8sxta
title: 'Yang, Steinhardt and Hu find that ResNet-18 trained on CIFAR-10 with labels merged into five two-class super-classes meets neural collapse on the coarse labels yet keeps the original classes as sub-clusters, recoverable without labels well enough that a linear probe on the recovered labels reaches over 93 per cent on the ten-class test set, and that the sub-clusters form before the label-driven merging, persist to 1,000 epochs and are absent in VGG'
promote_when: >-
  An independent replication with several seeds, on CIFAR-10 coarsened to
  five super-classes and a ResNet trained to zero training error, reports
  NC1 near zero on the coarse labels and ten-class accuracy from label-free
  clustering plus a linear probe within a few points of standard training,
  the sub-clusters' separation appearing before the coarse merging, and no
  such sub-clusters in a VGG run.
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-11-22'
source:
- LIT-2957
bears_on:
- QUESTION-202
summary: >-
  Yang, Steinhardt and Hu, [LIT-2957](../literature.d/LIT-2957.md), read in [NOTE-2276](../notes.d/NOTE-2276.md). Neural
  collapse on coarse labels leaves the fine classes in the residual
  variation, linearly decodable after label-free clustering. Grounds
  [CLAIM-800](../claims.d/CLAIM-800.md)'s point that a geometric measure can saturate while finer
  information persists ([ARG-186](../arguments.d/ARG-186.md)), and qualifies [THEORY-788](THEORY-788.md).
---
<!-- inactive-ok-file: CLAIM-800 ARG-186 THEORY-788 — Proposed or new; the claim this reading grounds, the argument for it and the reading it qualifies -->

# THEORY-2185: Yang, Steinhardt and Hu find that ResNet-18 trained on CIFAR-10 with labels merged into five two-class super-classes meets neural collapse on the coarse labels yet keeps the original classes as sub-clusters, recoverable without labels well enough that a linear probe on the recovered labels reaches over 93 per cent on the ten-class test set, and that the sub-clusters form before the label-driven merging, persist to 1,000 epochs and are absent in VGG

## Source

Yongyi Yang, Jacob Steinhardt and Wei Hu, "Are Neurons Actually
Collapsed? On the Fine-Grained Structure in Neural Representations", ICML
2023, arXiv 2306.17105, [LIT-2957](../literature.d/LIT-2957.md), read in [NOTE-2276](../notes.d/NOTE-2276.md).

## What was actually shown

- §4, Fig. 3: on the coarse labels "Neural Collapse does happen".
- §1, §4.3: CLP can "achieve > 93% accuracy on the original CIFAR-10 test
  set", "even though only 5 coarse labels are provided the entire time."
- §1, §4.1: "The effect of input distribution emerges earlier in training,
  while the effect of labels appears at a later stage."
- §1: the structure "persists even after a very long training period
  (e.g. 1,000 epochs)"; also with DenseNet-121, on coarse CIFAR-100 and
  under random coarsening; weaker where merged sub-classes are similar.
- §8, App. H: VGG "only displays Neural Collapse".

What could have failed: the residual within-class variation could have
been unstructured, as the unconstrained-feature model implies, leaving the
probe at chance within each super-class.

## What this does not say

- Not that collapse never happens: VGG collapses fully.
- Not a decodability order in time: the early fine structure is seen in
  distances, not in a probe run per epoch.
- Nothing beyond CIFAR-scale vision, single runs.
