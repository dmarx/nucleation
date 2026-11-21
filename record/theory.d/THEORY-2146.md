---
number: 2146
status: Proposed
formerly:
- THEORY-tmpybeh6
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
- LIT-2955
summary: >-
  The second source for the record's two drift rows in depth
  ([CLAIM-767](../claims.d/CLAIM-767.md)), in DMFT and in so many words: diffusion from
  initialization, drift from learning, the skip connection as the
  correlating mechanism. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2041 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-767 THEORY-2134 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2146: Bordelon, Noci, Li, Hanin and Pehlevan show, by a physics-level dynamical mean-field derivation and experiments on ResNets and ViTs, that a residual network with μP scaling and branches scaled by 1/√depth has a joint infinite-width and infinite-depth feature-learning limit in which each preactivation evolves over layer time as a diffusion from random contributions uncorrelated across blocks, each of order 1/√L, plus a drift from learned updates that skip connections correlate across blocks, each of order 1/L, with no depth factor in the learning rate

## Source

Bordelon, Noci, Li, Hanin and Pehlevan, [LIT-2955](../literature.d/LIT-2955.md), read in [NOTE-2228](../notes.d/NOTE-2228.md) from arXiv 2309.16620v2 (8 Dec 2023).

## What was actually shown

Eq. 3, Appendices E.3–E.4, K.5 and M as quoted in the NOTE; transfer across width and depth in CIFAR-10, Tiny ImageNet and ImageNet experiments.

## What this does not say

It does not treat networks without skips or their contraction in depth, deeper blocks beyond K.2.1, or normalization layers; it is not a formal proof.

## Connections

[THEORY-2134](THEORY-2134.md) (Tensor Programs VI: the same rows); [THEORY-2041](THEORY-2041.md) (Schoenholz: depth without skips); [THEORY-187](THEORY-187.md) (step size falling with depth in deep linear networks).
