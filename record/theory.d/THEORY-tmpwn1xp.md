---
status: Proposed
title: 'Ansuini, Laio, Macke and Zoccolan find that in trained image CNNs the TwoNN intrinsic dimension of a layer''s representations is orders of magnitude below the layer''s width, rises over the early layers and falls to about 12 to 25 in the last hidden layer, and is one to two orders below a 90 per cent variance PCA count, and that across architectures, not across seeds, its last-layer value correlates with test accuracy'
promote_when: >-
  An independent study, with an intrinsic-dimension estimator other than
  TwoNN or with TwoNN on other image networks, reproduces the rise-then-fall
  profile and the gap to a linear PCA count, and finds the last-layer
  intrinsic dimension correlating with accuracy across architectures.
version: 1
tags:
- representation-learning
- mathematical-statistics
date: '2026-11-22'
source:
- LIT-2998
summary: >-
  Ansuini and colleagues, LIT-2998, read in NOTE-tmptf55k. Representations
  of trained CNNs lie near curved low-dimensional manifolds: a nonlinear
  estimate of their dimension is far below width and below a linear PCA
  count, which does not tell trained from random networks apart. TERM-136
  takes its intrinsic sense from this reading.
---
<!-- inactive-ok-file: TERM-136 — Proposed; the term that draws on this reading -->

# THEORY-tmpwn1xp: Ansuini, Laio, Macke and Zoccolan find that in trained image CNNs the TwoNN intrinsic dimension of a layer's representations is orders of magnitude below the layer's width, rises over the early layers and falls to about 12 to 25 in the last hidden layer, and is one to two orders below a 90 per cent variance PCA count, and that across architectures, not across seeds, its last-layer value correlates with test accuracy

## Source

Alessio Ansuini, Alessandro Laio, Jakob H. Macke and Davide Zoccolan,
"Intrinsic dimension of data representations in deep neural networks",
NeurIPS 2019, arXiv 1905.12784, LIT-2998, read in NOTE-tmptf55k.

## What was actually shown

- Abstract, §3.1: "the ID is orders of magnitude smaller than the number
  of units in each layer"; it "initially grew, then reached a peak or a
  plateau and, finally, progressively decreased towards its final value".
- §3.2: last-hidden-layer ID across 14 ImageNet models is "a strong
  predictor of the performance" (r = 0.94); across 50 seeds of one
  network, "no correlation with accuracy (r=-0.003)".
- §3.3: the 90%-variance count is "about one or two orders of magnitude
  larger than the value of the ID computed with TwoNN"; a covariance-matched
  Gaussian has an ID "two orders of magnitude larger", growing with N;
  random weights give a "remarkably flat" ID profile.

What could have failed: the nonlinear and linear counts could have agreed,
or the profile could have been the same in random networks.

## What this does not say

- Not that representations are low-rank: the linear count is high; the
  manifolds are curved.
- Not a causal link from low ID to accuracy, and none within an
  architecture.
- IDs above about 20 are lower bounds, so the peak values are floors.
