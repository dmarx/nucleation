---
status: Proposed
promote_when: >-
  Geodesics in output-distribution space between many pairs of minima, of
  more than one architecture, compared on the same endpoints with
  loss-fitted curves (Garipov) and nudged-elastic-band paths (Draxler),
  with the loss along each reported as numbers with error bars, and with
  a control showing whether any chain constrained only to keep its
  neighbours' outputs close also stays low. The account is supported if
  the geodesic is low-loss where the control is not, and refuted by
  functionally similar minima whose distribution-space geodesic crosses a
  barrier. One more pair of weight-matched networks cannot settle it.
title: "Between two trained networks that compute nearly the same function, a chain of models minimising the summed Jensen–Shannon divergence between neighbours, a discretised Fisher–Rao geodesic found without labels, can be a low-loss path where the straight line in weights has a barrier"
version: 1
tags:
- loss-landscapes
- information-geometry
- anthology-candidate
date: '2026-10-16'
source:
- LIT-662
answers:
- QUESTION-069
summary: >-
  Tan, Long, Zhao & Laine (2023), [LIT-662](../literature.d/LIT-662.md), read in [NOTE-521](../notes.d/NOTE-521.md). Two ResNet-20s
  at 4× width with LayerNorm, CIFAR-10, permuted by Git Re-Basin's weight
  matching: the straight line between them still has a large loss barrier,
  and a chain of 25 models optimised from it to minimise Σ JSD between
  neighbours on unlabelled training images keeps train and test loss low.
  One pair, one figure, no numbers in the text. The hypothesis that every
  geodesic between SGD solutions is mode-connecting is stated, not
  tested, and a chain whose neighbours agree in output may be low-loss
  almost by construction.
---
<!-- inactive-ok-file: THEORY-109 THEORY-111 THEORY-112 — Proposed; the connectivity accounts this path family is set beside, not leaned on -->

# THEORY-tmpltw3b: Between two trained networks that compute nearly the same function, a chain of models minimising the summed Jensen–Shannon divergence between neighbours, a discretised Fisher–Rao geodesic found without labels, can be a low-loss path where the straight line in weights has a barrier

## Source

Tan, Long, Zhao & Laine (2023), [LIT-662](../literature.d/LIT-662.md) (Tiny Paper, ICLR 2023), read in
full in [NOTE-521](../notes.d/NOTE-521.md). [NOTE-521](../notes.d/NOTE-521.md) held this account back because the evidence is
one figure; it is filed Proposed for that reason.

## What was actually shown

**The geometry.** A classifier with the empirical input distribution is a
joint distribution p(x, ŷ; θ) = p(x)p(ŷ|x; θ). Under the Fisher–Rao metric
the length of a path is √8 times the integral of √dJSD (Eq. 1). Dropping
the square root and summing over a discrete chain gives an energy,
Σᵢ JSD(pᵢ‖pᵢ₊₁) (Eq. 2), whose minimiser is the constant-speed geodesic.

**The experiment.** Two ResNet-20s at 4× width, with LayerNorm in place of
BatchNorm, trained on CIFAR-10 from two seeds and permuted by Git
Re-Basin's weight matching. 25 models are placed on the straight line
between them and optimised by SGD to minimise the summed JSD, using
training images only, no labels. After optimisation, train and test
cross-entropy are low at every model on the chain; on the straight line
both rise sharply in the middle (Fig. 2). The optimisation lowers the summed
√JSD while lengthening the chain in Euclidean weight space.

**What could have come out otherwise.** The distribution-space geodesic
could have crossed a loss barrier. On this pair it did not.

## What this does not say

- **That geodesics in general connect modes.** "All geodesics between SGD
  solutions are mode-connecting paths" is stated in §1 and not tested
  beyond one pair.
- **That the geodesic is special.** The endpoints already have low loss,
  and a chain whose neighbours agree in output stays close to their
  outputs. The objective may be finding a path along which the function
  barely changes, which is mode connectivity almost by construction
  ([NOTE-521](../notes.d/NOTE-521.md), Limitations). The promote_when's control is for this.
- **That it is better than Garipov's curves.** The comparison is left to
  future work.
- **That it works without the permutation, or between narrow networks.**
  "Narrow" here means 4× width, narrow only beside the 32× Git Re-Basin
  needed for linear connectivity.
- **That 25 models approximate the continuous geodesic.** Not checked.

## Connections

- **[THEORY-109](THEORY-109.md)** holds that trained solutions are joined by simple curves
  found by fitting low loss. This finds such a curve by shortening the
  path in output space instead, with no labels.
- **[THEORY-112](THEORY-112.md)** holds that once symmetries are factored out most of the
  linear barrier disappears, with a residual at small width. This paper
  starts where weight matching's straight line still fails.
- **[THEORY-111](THEORY-111.md)** says that along a low-loss linear path every layer's
  features interpolate the endpoints'. Here the path is curved in weights
  and short in outputs.
- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks whether connectedness belongs to the solutions or
  to the path family searched. This is a different path family that finds
  a path where the line does not.
- **Lin, Li & Wu ([LIT-682](../literature.d/LIT-682.md))**'s "geodesic" is a different object: the
  shortest Euclidean path inside the minimum manifold.
