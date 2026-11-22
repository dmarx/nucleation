---
number: 84
status: Open
formerly:
- LEAD-tmpein2j
title: 'Find conditions under which a reduced process has a finite-dimensional Markovian augmentation beyond the scalar linear Gaussian case'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- complex-systems
- mathematics
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-222
summary: >-
  Named in [QUESTION-222](../questions.d/QUESTION-222.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-084: Find conditions under which a reduced process has a finite-dimensional Markovian augmentation beyond the scalar linear Gaussian case

## What it would do

Work the class stated in [QUESTION-222](../questions.d/QUESTION-222.md), with the dimension and the error in
terms of the eliminated spectrum; compare with the Kalman filter in the
linear Gaussian case, as [NOTE-989](../notes.d/NOTE-989.md) and [NOTE-1015](../notes.d/NOTE-1015.md) suggest; and rule whether
the level criteria apply to the augmented state.

Where the record names it:

- [QUESTION-222](../questions.d/QUESTION-222.md): "conditions under which the reduced process has a
  finite-dimensional Markovian augmentation"

## What would count

Conditions with a bound answer [QUESTION-222](../questions.d/QUESTION-222.md) for the class.

## Note of 2026-11-22: carried out for the linear Gaussian VAR(1)
<!-- inactive-ok-file: CASE-349 CLAIM-925 — new; the claim and study filed from this lead -->

Done on the branch claude/lead-084-markov-augmentation
(scratch/studies/lead-084/, 308 pytest checks). The class chosen is the
stable linear Gaussian VAR(1) with a coarse variable Y = LX of any
dimension, observed without noise: the first step beyond
[CLAIM-398](../claims.d/CLAIM-398.md)'s scalar case. [CLAIM-925](../claims.d/CLAIM-925.md) (demonstrated) gives the exact
augmentation, which is the Kalman filter, with at most n − m memory
coordinates; a bound on the excess error of keeping p lags, at the rate of
the filter's closed loop; that this rate is bounded by the eliminated
dynamics when one variable is eliminated, and not in general; and that the
augmentation leaves the transfer entropy from X unchanged.
[CASE-349](../cases.d/CASE-349.md) is the numerical study, which also found the minimal
augmentation equal to the Hankel rank of the Mori–Zwanzig memory on every
model tried.

What remains:

- **The ruling on levels.** The claim shows that dynamical independence
  gives the same verdict on the augmented state as on Y with its history.
  Whether the record's level criteria apply to the augmented state or to
  the instantaneous one is the owner's to rule, and is not filed.
- **The comparison [NOTE-1015](../notes.d/NOTE-1015.md) proposes,** of a past-conditioned variational
  slow-feature optimum with the Kalman state, was not done.
- **A proof that k_min equals the Mori–Zwanzig Hankel rank,** which
  [NOTE-989](../notes.d/NOTE-989.md) states and the study found on 16 models.
- **Beyond the class:** observation noise, VAR(p), and nonlinear classes.
