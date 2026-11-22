---
status: Proposed
title: 'Wang, Wu and Fan prove that in a deep network with random Gaussian weights at linear width and an odd-type activation a bounded input spike yields an outlier of a layer''s conjugate kernel only if it passes a BBP-type test at every layer up to it, so the number of outliers and their alignment with the input cannot increase with depth, and that after a few gradient steps at unit-order step size a two-layer network''s test-data conjugate kernel has a label-aligned outlier only above a threshold'
promote_when: >-
  An independent re-derivation, or a simulation, confirms for the stated
  setting the per-layer test and depth-wise non-increase of outliers and
  alignment of Theorem 3 and Corollary 4, and the two conditions of
  Theorem 5 (θ1 > γ0^(1/4) and z′(−1/λ1) > 0) for the test-data conjugate
  kernel's outlier.
version: 1
tags:
- learning-theory
- mathematical-statistics
- representation-learning
date: '2026-11-22'
source:
- LIT-2984
summary: >-
  Wang, Wu and Fan, [LIT-2984](../literature.d/LIT-2984.md), read in [NOTE-tmpa8a45](../notes.d/NOTE-tmpa8a45.md). At random weights an
  input spike survives each layer only past a BBP-type test, and depth can
  only lose outliers and alignment. After training the rank-one weight
  update exists for any step size, but the weights' top singular value
  separates only above one threshold and the kernel's outlier needs a
  second condition. Grounds [CLAIM-799](../claims.d/CLAIM-799.md) as a third case of signal before
  outlier ([ARG-tmppbt1o](../arguments.d/ARG-tmppbt1o.md)).
---
<!-- inactive-ok-file: CLAIM-799 ARG-tmppbt1o — Proposed or new; the claim this reading grounds and the argument for it -->

# THEORY-tmp9ltxi: Wang, Wu and Fan prove that in a deep network with random Gaussian weights at linear width and an odd-type activation a bounded input spike yields an outlier of a layer's conjugate kernel only if it passes a BBP-type test at every layer up to it, so the number of outliers and their alignment with the input cannot increase with depth, and that after a few gradient steps at unit-order step size a two-layer network's test-data conjugate kernel has a label-aligned outlier only above a threshold

## Source

Zhichao Wang, Denny Wu and Zhou Fan, "Nonlinear spiked covariance matrices
and signal propagation in deep neural networks", arXiv 2402.10127, COLT
2024, [LIT-2984](../literature.d/LIT-2984.md), read in [NOTE-tmpa8a45](../notes.d/NOTE-tmpa8a45.md).

## What was actually shown

- §2.1, after eq. 2.7: spikes with zℓ′(si,ℓ−1) > 0 "induce spike
  eigenvalues in the CK matrix Kℓ of the next layer, while spikes with
  zℓ′(si,ℓ−1) ≤ 0 are absorbed into the bulk spectrum of Kℓ."
- Theorem 3(c): the surviving eigenvector's squared overlap with the
  input's is a product of factors in (0, 1); hence the count and alignment
  "are both non-increasing in the network depth".
- Corollary 4: for a signal-plus-noise input, a spike for θᵢ if and only if
  θᵢ > γ0^(1/4) and i ∈ Iℓ.
- §2.2, Proposition 35 and Theorem 5: after a few steps W ≈ W₀ + a rank-one
  term for any η; the weights' top singular value separates "if and only
  if θ1 > γ0^(1/4)", and the test-data kernel "has a spike eigenvalue if
  and only if θ1 > γ0^(1/4) and z′(−1/λ1) > 0".

What could have failed: an input spike could have produced outliers in
later layers after vanishing in an earlier one, or the kernel's outlier
could have appeared whenever the weights' did.

## What this does not say

- Not that spikes grow with depth: that appears only in a simulation of a
  trained network (Fig. 2(b)).
- Nothing on what an absorbed spike leaves in the bulk or in the
  eigenvectors below threshold, so nothing on decodability.
- Nothing for non-odd activations, whose "uninformative spike eigenvalues"
  it assumes away, or beyond a few steps at η of order one.
