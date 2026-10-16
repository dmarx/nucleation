---
status: Active
title: "Chains of human function learners, each trained on the previous learner's responses, forget their starting function and in 28 of 32 families converge within a few generations to a positive linear function, the bias earlier studies report, whatever function trained the first learner; this is convergence to the learners' favoured function, not shown to be convergence to their prior"
version: 1
tags:
- cognition
- probabilistic-modeling
- learning-and-conditioning
date: '2026-10-16'
source:
- LIT-820
summary: >-
  Kalish, Griffiths & Lewandowsky (2007), [LIT-820](../literature.d/LIT-820.md), read in [NOTE-616](../notes.d/NOTE-616.md). 288
  participants in 32 nine-generation chains, four starting conditions.
  28 families converged to a positive linear function; 3 converged to the
  negative linear one and 1 had not converged. The bias was taken from
  earlier studies, not measured on these learners, and stationarity was
  not established. It supports the claim that human transmission chains
  settle on what learners favour in this task, not that they reach the
  Bayesian prior, and it cannot tell sampling learners from MAP learners.
supports:
- CLAIM-090
- CLAIM-234
---
<!-- inactive-ok-file: LIT-768 — Unavailable; Bartlett's serial reproduction, named as the experimental lineage, not leaned on -->
<!-- inactive-ok-file: THEORY-155 CLAIM-090 — Proposed; the theorem this result is offered for and a claim that cites it, named in Connections, not leaned on -->

# THEORY-tmpaw5e2: Chains of human function learners, each trained on the previous learner's responses, forget their starting function and in 28 of 32 families converge within a few generations to a positive linear function, the bias earlier studies report, whatever function trained the first learner; this is convergence to the learners' favoured function, not shown to be convergence to their prior

## Source

Kalish, Griffiths & Lewandowsky (2007), "Iterated learning:
Intergenerational knowledge transmission reveals inductive biases",
[LIT-820](../literature.d/LIT-820.md), read in [NOTE-616](../notes.d/NOTE-616.md).

## What was actually shown

**The design.** Four conditions (positive linear, negative linear,
nonlinear and random starting functions) × 8 families × 9 generations =
288 participants. Each learner was trained on the previous learner's test
responses, with no filter between generations. The bias, toward linear
functions with a positive slope, was stated before the experiment from
Brehmer (1971, 1974), Busemeyer et al. (1997) and Kalish, Lewandowsky and
Kruschke (2004).

**The result (Figs. 3A–F).** 28 of 32 families converged to a positive
linear function. 11 families produced a negative linear function at least
once (all 8 negative-linear families, 2 random, 1 nonlinear). 3 converged
to it (2 negative, 1 random), and 1 had not converged after nine
generations. The median correlation with y = x rose across generations in
the three conditions not already at ceiling.

**The simulation (Fig. 2).** Bayesian learners with a prior on lines
centred on slope 1, started from 20 points on y = 1 − x, produce a
positive linear function within a few generations over 1,000 chains.

**What could have come out otherwise.** The endpoints could have depended
on the starting function. Apart from the three negative endpoints, they
did not.

## What this does not say

- **That the chains converged to the prior.** The prior is a qualitative
  description ("favours positive linear") taken from earlier studies, not
  a distribution measured on these learners. "Converges to the prior" is
  tested only as "converges to the prior's mode", and the authors say
  stationarity is unconfirmed ([NOTE-616](../notes.d/NOTE-616.md), C3, weak).
- **That people are posterior samplers.** A strong positive-linear mode
  would be reached by sampling and MAP learners alike, so the experiment
  cannot separate them. Participants were not assumed or shown to sample.
- **That there is one attractor.** Three families ended on the negative
  linear function, which the authors read as weight in the stationary
  distribution (C4, weak).
- **That cultural forms are tailored to biases.** The discussion's claims
  about Bartlett and culture are not supported here; no stories or norms
  were transmitted (C5).
- **That it generalises.** One task, with one-dimensional input and output,
  undergraduates from one university, nine generations, and medians and
  representative chains with no test statistics. Slider responses within 5
  units counted as correct in training, so motor and response noise is
  transmitted too, unmodelled.

## Connections

- **The theorem it is offered for.** [THEORY-155](THEORY-155.md) states that
  posterior-sampling chains converge to the shared prior (Griffiths and
  Kalish, [LIT-769](../literature.d/LIT-769.md)). This is the nearest human test the record holds, and it
  does not meet [THEORY-155](THEORY-155.md)'s `promote_when`: the prior was neither
  measured nor manipulated, and the long-run distribution was not compared
  with it ([NOTE-616](../notes.d/NOTE-616.md), Bearing on the record).
- **The filtered chain.** Kirby, Cornish and Smith ([LIT-771](../literature.d/LIT-771.md)) measured no
  bias and used an experimenter's filter. This experiment has no filter
  and a bias known in advance; its weakness is the opposite one, a task far
  from language. [CLAIM-066](../claims.d/CLAIM-066.md) makes that contrast.
- **The record's own argument.** [CLAIM-090](../claims.d/CLAIM-090.md) cites this result as its
  evidence from human chains, partial counter-evidence included, and
  [CLAIM-234](../claims.d/CLAIM-234.md) lists it among the iterated-learning readings, none of which
  measures stance or speech-act function along a chain.
- Bartlett's serial reproduction ([LIT-768](../literature.d/LIT-768.md)) is the experimental lineage,
  filed unread.
