---
number: 2162
status: Proposed
formerly:
- THEORY-tmpu3iio
title: 'Low-amplified directions sway predictions most'
statement: >-
  Xu finds that in ten trained language models, replacing the final hidden
  state's component along the 5% of directions the centred, norm-folded
  unembedding amplifies least moves the logits less than equal-length random
  changes but changes the next-token distribution and the loss several times
  more; the prediction change per unit of logit distance stays near random
  over most of the spectrum and peaks at that bottom band, where the two
  leading candidate tokens differ disproportionately, while in total the top
  band's removal costs as much loss or more
promote_when: >-
  An independent replication on at least one of the ten models finds the
  bottom band's equal-length prediction-change ratio above one and the
  prediction change per unit of logit distance peaking at the bottom band,
  with the top band's total loss effect at least the bottom band's; or the
  paper passes peer review with these results intact.
version: 1
tags:
- representation-learning
- information-geometry
date: '2026-11-21'
source:
- LIT-2967
corroborates:
- CLAIM-835
bears_on:
- QUESTION-511
summary: >-
  Xu, [LIT-2967](../literature.d/LIT-2967.md), read in [NOTE-2249](../notes.d/NOTE-2249.md). The logit metric WᵀW and the
  predictive Fisher pulled back to the final state disagree most along the
  unembedding's least-amplified directions, per unit of logit distance and
  against equal-length random changes; not a reversal, since the top band
  matters as much in total. The record's best evidence that [CLAIM-835](../claims.d/CLAIM-835.md)'s
  disagreement occurs in trained models.
---
<!-- inactive-ok-file: CLAIM-835 — Proposed or new; the reading this account comes from and the claim it bears on -->

# THEORY-2162: Low-amplified directions sway predictions most

## Source

Weilun Xu, "The Smallest Singular Directions of the Unembedding Matter
Disproportionately for Next-Token Prediction", [LIT-2967](../literature.d/LIT-2967.md), arXiv 2605.17084v2,
read in [NOTE-2249](../notes.d/NOTE-2249.md).

## What was actually shown

- At equal state length, the bottom band's changes move logits less and
  change prediction and loss "several times as large" as random, in every
  model (§3.1).
- Per unit of logit distance, the prediction change "stays within about a
  factor of two of that of random changes" across most of the spectrum,
  with the excess over the last few bands (§3.2).
- Per unit of squared state length, the Fisher term "rises above random at
  both ends" (App. D): U-shaped.
- The top band's removal "increases the loss as much as removing the
  bottom band's, or more, in nine of the ten models" (App. E.2).
- The leading pair's contrast share tracks the consequence spectrum,
  correlations 0.95 to 0.98 (§4.1).

What could have failed: the bottom band could have changed predictions no
more than random per unit length, or the excess could have been spread
over the spectrum; it was not.

## What this does not say

- Not that the predictive metric ranks the smallest singular direction
  above the largest: the disagreement is in the quotient of the metrics.
- Not that the bottom band is low in representation variance: it holds
  1.5 to 6.6 times its share.
- Nothing about training: final checkpoints only; §7's origin is a
  hypothesis.
- Not invariant under invertible maps of the state ([THEORY-018](THEORY-018.md)); the
  quotient of metrics is, the singular ranking is not.
