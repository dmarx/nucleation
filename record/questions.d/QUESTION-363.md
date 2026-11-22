---
number: 363
status: Open
formerly:
- QUESTION-tmpiir0l
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
  Hoffman and Blei 2017 ([LIT-1898](../literature.d/LIT-1898.md)). A4 conceded the separation was "too
  strong" and kept a narrower one, which is this question. It refines
  [QUESTION-039](QUESTION-039.md), which asks what sets the order and moment of acquisition.
---
<!-- inactive-ok-file: CASE-tmpgqbyq CLAIM-tmpg8m7a CLAIM-tmp9zqvq CLAIM-tmpraadt — new, filed 2026-11-22 by LEAD-175's study -->
<!-- inactive-ok-file: THEORY-tmpm3ux2 — Proposed; the reading of Lee et al. filed 2026-11-22 -->
<!-- inactive-ok-file: THEORY-1353 — Proposed or Open; cited from the reading of Dong (2026) as open -->
<!-- inactive-ok-file: THEORY-209 — Open or Proposed; the question this refines and Kunin's sampler reading, cited as open -->
<!-- inactive-ok-file: CLAIM-834 CLAIM-828 CLAIM-812 — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" and cited in the note of that date -->

# QUESTION-363: When does the order in which stochastic gradient descent comes to occupy a network's organizations over training time follow the order in which they come to dominate the Bayesian posterior as the sample grows, and what fixes the correspondence where it holds: an effective temperature set by learning rate and batch size, the accessibility of regions and the barriers between them, or the time allowed to equilibrate?

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
| constant-step SGD's stationary distribution approximates a posterior for a fixed dataset, under a locally quadratic loss and constant noise ([LIT-1898](../literature.d/LIT-1898.md), [LIT-1899](../literature.d/LIT-1899.md)) | shown, near a minimum with positive-definite Hessian, so in one basin where the posterior has no phases; what is matched is the noise scale ε/S to 1/N ([THEORY-1255](../theory.d/THEORY-1255.md)) |
| SGD's transient over training time reproduces the posterior's transitions over sample size | "not established"; a partial datum below ([THEORY-1275](../theory.d/THEORY-1275.md)) |

The record already holds the second row's neighbours: Kunin et al.'s
modified-loss Gibbs distribution ([THEORY-209](../theory.d/THEORY-209.md)) and the stationary Gaussian of
underdamped Langevin SGD ([THEORY-779](../theory.d/THEORY-779.md)). The only correspondence between
examples processed and sample size in the readings is iterate averaging,
in a regular model in one basin after equilibration ([THEORY-1257](../theory.d/THEORY-1257.md)). The
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
  the posterior at its own sample size is ([THEORY-1275](../theory.d/THEORY-1275.md), recomputed).
- **Hennick and De Baerdemacker's tempering is a temperature.** Their
  steady state is the posterior at an effective sample size set by the
  noise, and only within a region of constant effective diffusion. The
  weights between regions, where "accessibility" would act, are not
  derived ([THEORY-1258](../theory.d/THEORY-1258.md)). Their theory excludes phase transitions.

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

## Note of 2026-11-04: Dong, "The Kinetics of Training", read

Dong (2026; [THEORY-1353](../theory.d/THEORY-1353.md)) answers for transformers that barriers and
drive set the order, not an effective temperature. Of six native knobs,
learning rate, batch size and minibatch noise among them, "zero qualify"
as a temperature by its test, an isotropic, state-independent noise with a
Gibbs stationary law: "lr is a clock, never a temperature". That need not
contradict [THEORY-1255](../theory.d/THEORY-1255.md), whose stationary covariance, set by learning rate
and batch size, is anisotropic and so fails the test's isotropy. No status
changes.

## Note of 2026-11-06: the partial datum rechecked

[THEORY-1275](../theory.d/THEORY-1275.md) was narrowed and promoted on a second checker's re-run of its computation
(scratch/formal/tms_critical_sizes_check.py). Two corrections to the datum above. The chain's
critical sample sizes rise in training order at the point estimates of the learning coefficients,
but at ±1 standard deviation of Table K.1 the order fails in 36 of 81 combinations, mostly because
the first two steps swap. And SGD on 1,000 samples ends at the 5-gon or at 4-gon variants in the
eight transition runs the paper shows (App. B); the 5⁺-gon of Eq. 10 is never the posterior's
phase, since the 6-gon beats it for every n above about 202. Two tests that [THEORY-1275](../theory.d/THEORY-1275.md)'s old
condition asked for belong here: posterior sampling across n that confirms the chain's critical
sample sizes, as Fig. 2 did for 5 → 6; and SGD at n = 1,000 and on both sides of n ≈ 600, across
learning rates, batch sizes and initialisations, showing whether the 6-gon is reached. What would
refute the reading's order: a chain whose antecedents' critical sizes fall as training proceeds,
once λ uncertainty is propagated.

## Note of 2026-11-21: the exchange "Rich Get Richer Power Laws"

A37 §5 of that exchange keeps this question's two orders apart and adds a
third: "A **Bayesian phase transition** occurs when the dominant posterior
region changes. A **dynamical transition** occurs when an optimizer's
trajectory reorganizes, perhaps after a plateau. A **semantic
transition** occurs when a new task-relevant distinction becomes stable
and decodable. These may be related, but they're not equivalent." The
question so far compares the first two. The third is a different kind of
event: a change in what the model can do, measured by probes or held-out
fit, which may happen inside one posterior region and one stretch of
trajectory. A43 §13 splits it further into "t_encoded", "t_stable" and
"t_behavioral" ([CLAIM-828](../claims.d/CLAIM-828.md)). A gated feature model shows the stability
crossing and the visible onset separated by a delay that grows with how
long the feature sat below threshold.

Two consequences for an answer here. First, a match between SGD's order
and the posterior's order does not by itself date the semantic events. An
answer that uses probe accuracy as its clock for training measures the
third order, not the first. Second, where the training order is read
from local learning-coefficient estimates, a change in the estimate can be
a sloppy direction coming into resolution rather than a move between
singular regions ([CLAIM-812](../claims.d/CLAIM-812.md)). The owner's U23, that singular
learning theory's account of transitions may serve the exchange's
picture of staged learning, is [CLAIM-834](../claims.d/CLAIM-834.md). No status changes.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Leaves the question open ([NOTE-tmp2pgi8](../notes.d/NOTE-tmp2pgi8.md)). The paper takes Bayesian
singular learning as an analogy for training's stages ("While there are
many differences between Bayesian inference and modern neural network
training, an analogy to the singular learning process informs our
methodology for stage division", §2) and says "the general connection
between the singular learning process in Bayesian inference and stagewise
development in deep learning remains to be understood" (§5). It cites
Chen et al. ([THEORY-1275](../theory.d/THEORY-1275.md)) as its only empirical precedent. No relation
written.

## Note of 2026-11-22: Lee, Smith, Adam and Hoogland, read

Bears on it; leaves it open. Lee et al. ([THEORY-tmpm3ux2](../theory.d/THEORY-tmpm3ux2.md), [NOTE-tmp1sot8](../notes.d/NOTE-tmp1sot8.md))
predict influence dynamics from the Bayesian posterior's transitions and
observe them along SGD training, in a deep linear network and small
language models. Their stated gap is this question: "The primary
theoretical gap remains the link between the Bayesian learning process
of SLT and the non-equilibrium dynamics of SGD" (§5). Their influence
estimates are local, from SGLD started at each SGD checkpoint, so the
agreement they report is between SGD's stages and posteriors localized
on SGD's own path, not the global Bayesian order in n.

## Note of 2026-11-22: the two tests run ([LEAD-175](../leads.d/LEAD-175.md))

Both tests of the note of 2026-11-06 were run in Chen et al.'s model
([CASE-tmpgqbyq](../cases.d/CASE-tmpgqbyq.md); scratch/studies/lead-175/).

**SGD.** None of 1,008 runs reached the 6-gon. They covered n from 300
to 2,000, batch 1 to 100, rates 0.001 to 0.2, the paper's 4-gon start,
the 5-gon, the 5⁺-gon and prior draws, and up to 45,000 epochs. From the
5-gon the move is closed outright: the dropped feature gets an exactly
zero gradient from every sample, so SGD's noise is zero in the
coordinates the crossing needs ([CLAIM-tmpg8m7a](../claims.d/CLAIM-tmpg8m7a.md)). From the live 5⁺-gon it
was not taken ([CLAIM-tmp9zqvq](../claims.d/CLAIM-tmp9zqvq.md)). For this model "inaccessible", not "not
reached", is the answer. Of the title's candidates, accessibility is the
one that acts. The noise is no temperature in those directions, in line
with [THEORY-1353](../theory.d/THEORY-1353.md).

**Posterior.** Sampling exp(−nL) puts 5 → 5⁺ near n = 780 and 5 → 6
near 270. The formula gives 1,600–2,500 and 601. The chain's first two
steps have no crossing above n ≈ 1 ([CLAIM-tmpraadt](../claims.d/CLAIM-tmpraadt.md)). Chen et al.'s NUTS
likelihood has a factor ½ that their formula's nL lacks. On their scale
the sampled 5 → 6 is at about 530–560, consistent with their Fig. 2. The
posterior favours the 6-gon at n = 1,000 on either scale. No status
changes.
