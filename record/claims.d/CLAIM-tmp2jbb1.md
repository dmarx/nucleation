---
status: Proposed
title: 'On populations matched in turnover and aggregate statistics, a priced lagged block test finds a population held together by delayed transmission, with its lag, but rejects a commonly driven population only while the common input is observed, and gives a commonly driven population and an institutionally maintained one the same boundary'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation, found by a test or a rerun of
  scratch/studies/lead-026/; or a showing that the implementation departs
  from the block criterion and its price as CLAIM-157 and CLAIM-154 state
  them in a way that reverses one of the four verdicts: the transmitting
  population passes as a block, with its support peaking at the
  transmission lag; the commonly driven members fail alone while the driver
  is observed; they pass once it is hidden; the commonly driven and the
  institutionally maintained members both pass only joined to their
  external variable. A different model on which the test behaves better does
  not defeat it, since the claim is that the test as stated does not
  guarantee the separations, and one model shows that.
tags:
- individuation
- information-theory
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-115
- QUESTION-116
rests_on:
- CLAIM-157
- CLAIM-154
corroborates:
- CLAIM-194
grounds:
- CASE-tmprsqvj
summary: >-
  CASE-tmprsqvj runs CASE-101's populations, matched in turnover, member
  variance, member correlation and the aggregate's lag-1 autocorrelation,
  through CLAIM-157's block test, lagged over windows of 1 to 16 steps and
  priced by CLAIM-154. The test finds the population that transmits its
  norms at a lag of eight steps, with its support peaking at that lag. It
  rejects the commonly driven members alone only while their driver is
  among the observed variables, and once the driver is hidden they pass.
  It joins the driven members and the institutionally maintained members
  each to their external variable, so it cannot tell common input from
  institutional maintenance by membership. Only the direction of a
  feedback, which the price removes at longer windows, tells them apart,
  and against a deaf institution nothing does. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-167 LIT-005 — Proposed; the block criterion this applies, the claim on one-way drive it is read with, and Bourrat's paper -->
<!-- inactive-ok-file: CASE-tmprsqvj — new, filed with this claim -->

# CLAIM-tmp2jbb1: On populations matched in turnover and aggregate statistics, a priced lagged block test finds a population held together by delayed transmission, with its lag, but rejects a commonly driven population only while the common input is observed, and gives a commonly driven population and an institutionally maintained one the same boundary

## The claim

CASE-tmprsqvj simulates CASE-101's arms: common input (A), norms
transmitted at a lag of eight steps (B), an institution that trains,
selects and answers to its members (C), and one that does not answer (C0).
They are matched in turnover and in three aggregate statistics. CLAIM-157's
block test is lagged by fitting a linear autoregression over a window of W
steps, and CLAIM-154's rule prices every group of couplings.

- **Delayed transmission is found, with its lag.** B's members pass as a
  block at every window, and the support peaks at W = 8, the transmission
  lag. QUESTION-116's collective, weakly coupled at each instant and
  strongly coupled through time, is found in this model.
- **Common input is rejected only while it is observed.** A's members fail
  alone because their driver explains their correlation. With the driver
  unobserved, the same members pass, and so does every arm's population.
  QUESTION-116's test, "rejects a population whose members are correlated
  only because they receive the same input", is met only relative to an
  observed set that contains the input.
- **Common input and institutional maintenance get one boundary.** A's
  members pass only with their driver, and C's and C0's only with their
  institution, at every window. That is CLAIM-167's verdict on one-way
  drive. The direction of coupling, which CLAIM-167 makes the system's
  architecture, separates C from A only at windows of up to four steps,
  where the institution's response to its members clears the price. A deaf
  institution (C0) and a common driver (A) get the same verdict on every
  measure. This is CLAIM-194's made-versus-imposed boundary in population
  form.

Two qualifications of the record's statements come with it.

- **A one-step test is not blind to lagged coupling.** CLAIM-157 says a
  block test on synchronous dynamics will not see coupling that is "a write
  and a later read". That holds for the true one-step coupling, which is
  zero in B. It fails for a one-step model fitted to data, which sees the
  lag-8 coupling through the members' own persistence. The window does not
  decide whether the block is seen. It decides where its support peaks,
  and that gives the lag.
- **Intervening on the present misses stored norms.** Bourrat's Â
  (LIT-005) of B's members falls to 0.02 nats by 32 steps, while
  retention conditioned on the environment (Krakauer et al.'s A) stays at
  0.31. An intervention on the present values leaves the norms of the last
  eight steps in place. For a population that transmits at a lag, the
  candidate's state includes its stored past.

## What it does not say

- **That the block test fails as a criterion of individuality.** It finds
  what it measures: coupling, priced. What it cannot do here, separate a
  driven population from a made one, CLAIM-194 already says it cannot do.
- **That these verdicts hold for every parameterization.** One linear model
  with four calibrations, one price (a unit-information prior) and
  linear-Gaussian estimates were used.
- **That any information measure picks a boundary.** Unpriced, A*, A and Â
  all pick the largest candidate, the distractor included.
