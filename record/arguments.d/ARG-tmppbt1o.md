---
status: Proposed
title: 'Wang, Wu and Fan''s trained two-layer network, as an existence case, shows the update in the weights for every step size while the weights'' top singular value separates only above one threshold and the test-data kernel''s outlier needs a second condition, so the separation of acquisition from spectral detectability holds a third time, with two thresholds in series'
version: 1
form: existence
grounds:
- THEORY-tmp9ltxi
concludes:
- CLAIM-799
tags:
- representation-learning
- learning-theory
- mathematical-statistics
date: '2026-11-22'
line:
- learned-structure
summary: >-
  In Wang, Wu and Fan's §2.2 ([THEORY-tmp9ltxi](../theory.d/THEORY-tmp9ltxi.md), [NOTE-tmpa8a45](../notes.d/NOTE-tmpa8a45.md)) a few
  gradient steps add a rank-one term along the target to the first-layer
  weights for any step size, yet the weights' largest singular value
  leaves the bulk only if θ1 > γ0^(1/4) (Proposition 35), and the
  test-data conjugate kernel has an outlier only if, in addition,
  z′(−1/λ1) > 0 (Theorem 5). That is [CLAIM-799](../claims.d/CLAIM-799.md)'s signal before outlier,
  beside Park and colleagues' case ([ARG-tmps8aog](ARG-tmps8aog.md)). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-799 THEORY-tmp9ltxi ARG-tmps8aog CLAIM-837 — Proposed or new; the claim this argues, the reading it uses, the parallel argument and a parallel claim -->
<!-- inactive-ok-file: CASE-301 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# ARG-tmppbt1o: Wang, Wu and Fan's trained two-layer network, as an existence case, shows the update in the weights for every step size while the weights' top singular value separates only above one threshold and the test-data kernel's outlier needs a second condition, so the separation of acquisition from spectral detectability holds a third time, with two thresholds in series

## The inference

[CLAIM-799](../claims.d/CLAIM-799.md), from A32 §2: a spectral threshold "is not necessarily the
moment when the network first learns anything. The signal existed below
the threshold." Wang, Wu and Fan, §2.2: after a few gradient steps at η of
order one, W ≈ W₀ + (ηbσ/n)Xᵀyaᵀ, a change "approximately rank-1", for any
η > 0. Proposition 35: "The largest singular value smax(W) falls outside
the limit of its empirical singular value distribution if and only if
θ1 > γ0^(1/4)". Theorem 5: the test-data conjugate kernel "has a spike
eigenvalue if and only if θ1 > γ0^(1/4) and z′(−1/λ1) > 0". The update
exists before either outlier; the weights' outlier comes before the
kernel's.

## Critical questions

- **Is the case coherent?** Yes: both thresholds are proved in one model,
  under the stated assumptions (Gaussian single-index data, frozen second
  layer, odd-type activation, proportional limit).
- **Does it separate the very things the conclusion says can come apart?**
  In part. It separates the update's existence from the weights' spectral
  outlier, and that outlier from the kernel's. It does not measure
  decodability: below threshold the paper says nothing of what a readout
  could recover, and its depth result, "the input signal diminishes as the
  depth of the NN increases", is about outlier alignment, not about the
  information present. So the case supports the separation on the spectral
  side only; [CLAIM-799](../claims.d/CLAIM-799.md) holds decodability apart, the paper does not.

## Verdict

Supports [CLAIM-799](../claims.d/CLAIM-799.md) as a third existence case, after its own construction
([CASE-301](../cases.d/CASE-301.md)) and Park and colleagues ([ARG-tmps8aog](ARG-tmps8aog.md)), and adds that the
thresholds can come in series, weights then features, as [CLAIM-837](../claims.d/CLAIM-837.md) has for
a hidden layer and its readout. Proposed.
