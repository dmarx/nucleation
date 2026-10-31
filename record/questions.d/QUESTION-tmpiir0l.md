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
| constant-step SGD's stationary distribution approximates a posterior for a fixed dataset, under a locally quadratic loss and constant noise (LIT-tmpwzrx7, LIT-tmpxo5z5) | shown, near a minimum with positive-definite Hessian, so in one basin where the posterior has no phases; what is matched is the noise scale ε/S to 1/N (THEORY-tmp7gcht) |
| SGD's transient over training time reproduces the posterior's transitions over sample size | "not established"; a partial datum below (THEORY-tmpzcsl4) |

The record already holds the second row's neighbours: Kunin et al.'s
modified-loss Gibbs distribution (THEORY-209) and the stationary Gaussian of
underdamped Langevin SGD (THEORY-779). The only correspondence between
examples processed and sample size in the readings is iterate averaging,
in a regular model in one basin after equilibration (THEORY-tmp8ggnh). The
third row is the question.

**What the readings found (2026-10-31).**

- **Chen et al. do not conjecture coincidence.** Their abstract's
  "journey" from high loss and low complexity to low loss and high
  complexity is a shared direction. Their §5.1 says there is "no necessary
  relation between these two kinds of transitions". Their Bayesian
  antecedent hypothesis runs one way: transitions seen in training have
  Bayesian counterparts. The exchange's reading, repeated in the first
  filing's workbench and curation entries, overstated this.
- **A partial datum.** Along the chain SGD takes in their toy model, the
  Bayesian counterparts fall at n ≈ 190, 370 and 1,600–2,500, in training
  order. But SGD trained on 1,000 samples skips the 6-gon, which the
  posterior has favoured since n ≈ 600, and ends at the 5- or 5⁺-gon. No
  single map from training time to sample size makes training end where
  the posterior at its own sample size is (THEORY-tmpzcsl4, recomputed).
- **Hennick and De Baerdemacker's tempering is a temperature.** Their
  steady state is the posterior at an effective sample size set by the
  noise, and only within a region of constant effective diffusion. The
  weights between regions, where "accessibility" would act, are not
  derived (THEORY-tmpe0idn). Their theory excludes phase transitions.

So the maps the readings supply run from noise scale to sample size, not
from training time to sample size. Of the title's three candidates:
- **The effective temperature** is the bridge in both stationary accounts.
- **Barriers and distance** are Chen et al.'s stated reason for the
  missing 6-gon, but they do not show it.
- **Time to equilibrate** is assumed by Mandt et al. and by Hennick and De
  Baerdemacker, and analysed by neither.

## What would count as an answer

A model where both orders can be computed, such as the toy model of
superposition ([LIT-323](../literature.d/LIT-323.md)) or the two-parameter models of [CASE-152](../cases.d/CASE-152.md). Run
SGD at several learning rates and batch sizes, and compute the posterior's
phase order across n. Then either a map from training time to an effective
sample size under which the orders agree, with the conditions it needs,
or a stated case where they cannot agree, because a region dominant in the
posterior is not accessible to the dynamics. Chen et al.'s 5-gon to
6-gon transition is the candidate case. "Inaccessible" and "not reached
in 4,500 epochs at one setting" are not yet told apart; SGD at n = 1,000
across several learning rates and batch sizes would separate them. A14 found that its own
attempt at the second fails: the region it offered is invariant under
gradient flow but unstable, so noise escapes it.
