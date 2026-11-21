---
status: Proposed
promote_when: >-
  An independent derivation or experiment confirming, for 1/√depth-scaled
  μP residual networks trained without a depth-scaled learning rate, that
  each block's random contribution scales as 1/√L and adds diffusively,
  its learned contribution scales as 1/L and adds coherently through
  cross-block gradient correlation, and the optimal learning rate is
  stable across depth.
title: 'Bordelon, Noci, Li, Hanin and Pehlevan show, by a physics-level dynamical mean-field derivation and experiments on ResNets and ViTs, that a residual network with μP scaling and branches scaled by 1/√depth has a joint infinite-width and infinite-depth feature-learning limit in which each preactivation evolves over layer time as a diffusion from random contributions uncorrelated across blocks, each of order 1/√L, plus a drift from learned updates that skip connections correlate across blocks, each of order 1/L, with no depth factor in the learning rate'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-tmpu5m2v
summary: >-
  The second source for the record's two drift rows in depth
  (CLAIM-tmp2yj4t), in DMFT and in so many words: diffusion from
  initialization, drift from learning, the skip connection as the
  correlating mechanism. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2041 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmp2yj4t LIT-tmpu5m2v NOTE-tmpo9k2m THEORY-tmpbyw89 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmpybeh6: Bordelon, Noci, Li, Hanin and Pehlevan show, by a physics-level dynamical mean-field derivation and experiments on ResNets and ViTs, that a residual network with μP scaling and branches scaled by 1/√depth has a joint infinite-width and infinite-depth feature-learning limit in which each preactivation evolves over layer time as a diffusion from random contributions uncorrelated across blocks, each of order 1/√L, plus a drift from learned updates that skip connections correlate across blocks, each of order 1/L, with no depth factor in the learning rate

## Source

Bordelon, Noci, Li, Hanin and Pehlevan, LIT-tmpu5m2v, read in NOTE-tmpo9k2m from arXiv 2309.16620v2 (8 Dec 2023).

## What was actually shown

Eq. 3, Appendices E.3–E.4, K.5 and M as quoted in the NOTE; transfer across width and depth in CIFAR-10, Tiny ImageNet and ImageNet experiments.

## What this does not say

It does not treat networks without skips or their contraction in depth, deeper blocks beyond K.2.1, or normalization layers; it is not a formal proof.

## Connections

THEORY-tmpbyw89 (Tensor Programs VI: the same rows); THEORY-2041 (Schoenholz: depth without skips); THEORY-187 (step size falling with depth in deep linear networks).
