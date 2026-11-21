---
status: Proposed
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
- LIT-tmp9tr5w
summary: >-
  The width side of the record's reading of parameterizations as rate
  allocations ([CLAIM-tmpqwoxz](../claims.d/CLAIM-tmpqwoxz.md)): per-layer rates ε^(r_l) with ε = 1/n, and
  the kernel regime as a body slower than the readout by a factor growing
  with width. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: THEORY-212 THEORY-813 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmpqwoxz THEORY-tmpbyw89 THEORY-tmpecd1x THEORY-tmpig1z0 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-tmp7n7a9: Yang and Hu show that in any nontrivial stable abc-parametrization of a wide MLP each layer's update changes its output by a power of width, so that the network either learns features, when the smallest exponent is zero, or has every feature and feature kernel fixed in the infinite-width limit while its output evolves by kernel gradient descent, and that μP is the unique stable parametrization with every exponent zero and the readout updated and initialized maximally

## Source

Yang and Hu, [LIT-tmp9tr5w](../literature.d/LIT-tmp9tr5w.md), read in [NOTE-tmpl3qeq](../notes.d/NOTE-tmpl3qeq.md) from arXiv 2011.14522v3 (15 Jul 2022, 65 pp.).

## What was actually shown

Definition 3.2, Proposition 5.3, Corollary 3.9, Theorems 5.6, G.4 and H.13 as quoted in the NOTE.

## What this does not say

Nothing about width-growing training times, finite width, or depth (Tensor Programs VI); it does not use the language of time scales except in citing Mei and colleagues.

## Connections

[THEORY-212](THEORY-212.md) (the per-layer, finite-size form); [THEORY-tmpecd1x](THEORY-tmpecd1x.md) (Chizat and colleagues on lazy training); [THEORY-tmpig1z0](THEORY-tmpig1z0.md) (the spectral condition, an equivalent statement of μP); [THEORY-tmpbyw89](THEORY-tmpbyw89.md) (the depth counterpart); [THEORY-813](THEORY-813.md).
