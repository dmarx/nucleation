---
status: Open
title: 'When does the order in which stochastic gradient descent comes to occupy a network''s organizations over training time follow the order in which they come to dominate the Bayesian posterior as the sample grows, and what fixes the correspondence where it holds: an effective temperature set by learning rate and batch size, the accessibility of regions and the barriers between them, or the time allowed to equilibrate?'
version: 1
tags:
- learning-theory
- loss-landscapes
- mathematical-statistics
date: '2026-10-31'
line: learned-structure
refines:
- QUESTION-039
summary: >-
  The owner's challenge at U4 of the exchange "Analyze nucleation
  concepts" (2026-10-31). A3 had said that "Bayesian posterior dominance
  as sample size n changes is not the same process as gradient-based
  optimization as training time advances". The owner: "Isn't it? I think
  there's a David M Blei paper that discusses this." The paper is Mandt,
  Hoffman and Blei 2017 ([LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md)). A4 conceded the separation was "too
  strong" and kept a narrower one, which is this question. It refines
  [QUESTION-039](QUESTION-039.md), which asks what sets the order and moment of acquisition.
---
<!-- inactive-ok-file: QUESTION-039 THEORY-209 — Open or Proposed; the question this refines and Kunin's sampler reading, cited as open -->

# QUESTION-tmpiir0l: When does the order in which stochastic gradient descent comes to occupy a network's organizations over training time follow the order in which they come to dominate the Bayesian posterior as the sample grows, and what fixes the correspondence where it holds: an effective temperature set by learning rate and batch size, the accessibility of regions and the barriers between them, or the time allowed to equilibrate?

## Why it is a question

Singular learning theory orders a model's regions by free energy,
F_n ≈ nL_n + λ log n, so as n grows the posterior moves from simple,
high-loss regions to complex, low-loss ones ([THEORY-087](../theory.d/THEORY-087.md)). Training moves
through regions too, in time. Whether those are one journey is open, and
the exchange's sources disagree about how far they coincide.

A4 set out three relations, kept here:

| relation | status |
|---|---|
| SGD converges to a minimum, the MAP estimate under a flat prior | standard |
| constant-step SGD's stationary distribution approximates a posterior for a fixed dataset, under a locally quadratic loss and constant noise ([LIT-tmpwzrx7](../literature.d/LIT-tmpwzrx7.md), [LIT-tmpxo5z5](../literature.d/LIT-tmpxo5z5.md)) | shown, with assumptions |
| SGD's transient over training time reproduces the posterior's transitions over sample size | "not established" |

The record already holds the second row's neighbours: Kunin et al.'s
modified-loss Gibbs distribution ([THEORY-209](../theory.d/THEORY-209.md)) and the stationary Gaussian of
underdamped Langevin SGD ([THEORY-779](../theory.d/THEORY-779.md)). The third row is the question.

Two sources pull opposite ways.

- **Toward correspondence.** Chen et al. ([LIT-tmpogi33](../literature.d/LIT-tmpogi33.md)) conjecture that
  "the learning process in TMS, be it through SGD or Bayesian learning"
  moves from high loss and low complexity to low loss and high complexity.
  A3 cited this paper for the separation and did not report the
  conjecture.
- **Toward a modified correspondence.** Hennick and De Baerdemacker
  ([LIT-tmp107c0](../literature.d/LIT-tmp107c0.md)) read SGD's local steady state, where one exists, as a tempered
  posterior that "accounts for local accessibility constraints". Their
  correction is the third candidate in the title.

The two variables are different. n changes the target. Training time
changes the iterate under a fixed target. A correspondence needs a map
between them, and nothing so far supplies one.

## What would count as an answer

A model where both orders can be computed, such as the toy model of
superposition ([LIT-323](../literature.d/LIT-323.md)) or the two-parameter models of [CASE-152](../cases.d/CASE-152.md). Run
SGD at several learning rates and batch sizes, and compute the posterior's
phase order across n. Then either a map from training time to an effective
sample size under which the orders agree, with the conditions it needs,
or a stated case where they cannot agree, because a region dominant in the
posterior is not accessible to the dynamics. A14 found that its own
attempt at the second fails: the region it offered is invariant under
gradient flow but unstable, so noise escapes it.
