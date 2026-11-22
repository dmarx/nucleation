---
number: 2170
status: Proposed
formerly:
- THEORY-tmpcij35
title: 'Dandi, Pesce, Cui, Krzakala, Lu and Loureiro prove that after one maximal-update gradient step on Gaussian single-index data a two-layer network''s first-layer weights are a random bulk plus a rank-one spike along the target, and give the resulting feature covariance''s asymptotic spectrum, whose bulk widens and lengthens its tails beside outliers of order d from the feature means, and the exact test error of the ridge-fitted readout, a functional of the whole deterministic equivalent'
promote_when: >-
  An independent reading or replication confirms, for the stated setting,
  the rank-one spike approximation of Lemma 3.1 and the deterministic
  equivalent of Theorem 4.6, and that the bulk spectrum and test error it
  gives match simulation as in Figures 1 and 2.
version: 1
tags:
- learning-theory
- representation-learning
- mathematical-statistics
date: '2026-11-22'
source:
- LIT-2983
summary: >-
  Dandi and colleagues, [LIT-2983](../literature.d/LIT-2983.md), read in [NOTE-2258](../notes.d/NOTE-2258.md). The spike of one
  large gradient step is in the weights; in the features, learning shows
  chiefly as a reshaped bulk, with outliers from the means. Grounds
  [CLAIM-799](../claims.d/CLAIM-799.md)'s narrow point that the spiked picture of learned features is
  a theorem, and qualifies it ([ARG-166](../arguments.d/ARG-166.md)).
---
<!-- inactive-ok-file: CLAIM-799 ARG-166 — Proposed or new; the claim this reading bears on and the argument for its support -->

# THEORY-2170: Dandi, Pesce, Cui, Krzakala, Lu and Loureiro prove that after one maximal-update gradient step on Gaussian single-index data a two-layer network's first-layer weights are a random bulk plus a rank-one spike along the target, and give the resulting feature covariance's asymptotic spectrum, whose bulk widens and lengthens its tails beside outliers of order d from the feature means, and the exact test error of the ridge-fitted readout, a functional of the whole deterministic equivalent

## Source

Dandi, Pesce, Cui, Krzakala, Lu and Loureiro, "A Random Matrix Theory
Perspective on the Spectrum of Learned Features and Asymptotic
Generalization Capabilities", arXiv 2410.18938, [LIT-2983](../literature.d/LIT-2983.md), read in
[NOTE-2258](../notes.d/NOTE-2258.md).

## What was actually shown

- Lemma 3.1: for n0 = Ω(d^(1+ε)), W¹ = W⁰ + u(w⋆)ᵀ up to a term vanishing
  in operator norm; "the hidden layer weights after one GD step are
  approximately low rank".
- Theorem 4.6 and Corollary 4.7: a deterministic equivalent of the feature
  covariance's resolvent and the Stieltjes transform of its bulk.
- Theorem 4.8: the test error "is given by the following
  low-dimensional, deterministic formula".
- §5, Fig. 1: the bulk "is modified from the unspiked RF spectrum ...,
  displaying in particular a wider support and longer tails in this
  particular instance", beside "outlying eigenvalues of order Θ(d),
  arising from the means".

What could have failed: the deterministic equivalent could have
disagreed with simulation, or the bulk stayed at its random-features
shape with all the learning in outliers.

## What this does not say

- Not that the feature matrix is a spiked random matrix whose outliers set
  the error; the outliers are partly an artefact of the finite
  second-layer support ("spurious spikes"), and the error depends on the
  whole equivalent.
- Nothing beyond one step, Gaussian data and a single-index target.
- No threshold, detectability transition, criticality or dynamics.
- That heavier tails go with better generalization is cited as empirical
  and shown in one instance, not proved.
