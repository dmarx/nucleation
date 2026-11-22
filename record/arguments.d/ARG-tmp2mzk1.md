---
status: Proposed
title: 'Dandi and colleagues'' one-step theorem, read as a source for A32 §6, shows that the spiked picture of learned features is a theorem and not an analogy for one maximal-update step, and qualifies the separation of qualities: learning shows in the feature spectrum chiefly as a reshaped bulk, not only as an outlier crossing a threshold'
version: 1
form: source
grounds:
- THEORY-tmpcij35
concludes:
- CLAIM-799
uses:
- TERM-tmpf5ymd
tags:
- representation-learning
- learning-theory
- mathematical-statistics
date: '2026-11-22'
line:
- learned-structure
summary: >-
  CLAIM-799 cites Dandi and colleagues, through A32 §6, for work tying
  learned features to spiked random-matrix models, so that "the spectral
  perspective is not merely an analogy". The reading (THEORY-tmpcij35,
  NOTE-tmpdac0o) bears that out for one step: the weights are a bulk plus
  a rank-one spike by Lemma 3.1. It also shows learning in the features as
  a wider, longer-tailed bulk, so spectral detectability in the outlier
  sense is not the only spectral signature of learned structure. Nothing in
  it bears on the BBP threshold. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-799 THEORY-tmpcij35 TERM-tmpf5ymd — Proposed or new; the claim this argues, the reading it uses and the term it is stated in -->

# ARG-tmp2mzk1: Dandi and colleagues' one-step theorem, read as a source for A32 §6, shows that the spiked picture of learned features is a theorem and not an analogy for one maximal-update step, and qualifies the separation of qualities: learning shows in the feature spectrum chiefly as a reshaped bulk, not only as an outlier crossing a threshold

## The inference

A32 §6, in CLAIM-799: such work shows "the spectral perspective is not
merely an analogy. But they don't establish that DNN representations
generally behave as active matter, or that their learning dynamics are
critical." The reading: Lemma 3.1, "the hidden layer weights after one GD
step are approximately low rank", W¹ ≈ W⁰ + u(w⋆)ᵀ; and in the features the
bulk "is modified from the unspiked RF spectrum ..., displaying in
particular a wider support and longer tails", beside Θ(d) outliers "arising
from the means".

## Critical questions

- **Does the work say this, read in context?** Yes for the narrow point:
  the spiked model is proved, in the weights, for one step. No for the LIT's
  former gloss that the feature matrix's outliers "carry the learned
  directions and set the generalization error": the error is a functional
  of the whole deterministic equivalent (Theorem 4.8).
- **Is it said within the scope the claim needs?** For "not merely an
  analogy", yes, within one step on Gaussian single-index data. For
  "active matter" and "critical", the paper is silent, which fits A32's
  "don't establish".
- **Does the claim lean on it for more than it holds?** CLAIM-799's
  thesis is that spectral detectability, an outlier separating from the
  bulk, is distinct from acquisition. The reading adds a qualification the
  claim lacked: learned structure also shows as a change in the shape of
  the bulk by count (TERM-tmpf5ymd), so "spectrally undetectable" in the
  outlier sense is not "spectrally invisible". The thesis stands; its
  table's third quality needs that rider, now added in place.

## Verdict

Supports CLAIM-799's citation narrowly and qualifies the claim. Proposed.
