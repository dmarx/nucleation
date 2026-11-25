---
number: 2133
status: Proposed
formerly:
- THEORY-tmp7n7a9
promote_when: >-
  A check of Corollary 3.9, Theorem H.13 and Proposition 5.3 against their
  proofs in Appendix H, or an independent statement of the same
  classification, confirming for tanh or σ-gelu MLPs at width-independent
  training time that r > 0 is equivalent to fixed features and kernel
  gradient descent, r = 0 to feature learning, and that μP is unique with
  all r_l = 0 and the readout maximal.
title: 'Yang and Hu show that in any nontrivial stable abc-parametrization of a wide MLP each layer''s update changes its output by a power of width, so that the network either learns features, when the smallest exponent is zero, or has every feature and feature kernel fixed in the infinite-width limit while its output evolves by kernel gradient descent, and that μP is the unique stable parametrization with every exponent zero and the readout updated and initialized maximally'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2943
summary: >-
  The width side of the record's reading of parameterizations as rate
  allocations ([CLAIM-775](../claims.d/CLAIM-775.md)): per-layer rates ε^(r_l) with ε = 1/n, and
  the kernel regime as a body slower than the readout by a factor growing
  with width. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-2170 — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: THEORY-212 THEORY-813 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-775 THEORY-2134 THEORY-2135 THEORY-2139 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2133: Yang and Hu show that in any nontrivial stable abc-parametrization of a wide MLP each layer's update changes its output by a power of width, so that the network either learns features, when the smallest exponent is zero, or has every feature and feature kernel fixed in the infinite-width limit while its output evolves by kernel gradient descent, and that μP is the unique stable parametrization with every exponent zero and the readout updated and initialized maximally

## Source

Yang and Hu, [LIT-2943](../literature.d/LIT-2943.md), read in [NOTE-2226](../notes.d/NOTE-2226.md) from arXiv 2011.14522v3 (15 Jul 2022, 65 pp.).

## What was actually shown

Definition 3.2, Proposition 5.3, Corollary 3.9, Theorems 5.6, G.4 and H.13 as quoted in the NOTE.

## What this does not say

Nothing about width-growing training times, finite width, or depth (Tensor Programs VI); it does not use the language of time scales except in citing Mei and colleagues.

## Connections

[THEORY-212](THEORY-212.md) (the per-layer, finite-size form); [THEORY-2135](THEORY-2135.md) (Chizat and colleagues on lazy training); [THEORY-2139](THEORY-2139.md) (the spectral condition, an equivalent statement of μP); [THEORY-2134](THEORY-2134.md) (the depth counterpart); [THEORY-813](THEORY-813.md).

## Note of 2026-11-22: Dandi and colleagues, read

Dandi and colleagues ([LIT-2983](../literature.d/LIT-2983.md), [NOTE-2258](../notes.d/NOTE-2258.md), [THEORY-2170](THEORY-2170.md)):
**background.** Their step size η = Θ(d) is the maximal-update scaling,
the regime in which this account says features are learned; their
one-step theorem, a rank-one spike along the target in the first-layer
weights, is a concrete instance of what is learned there. No relation.
