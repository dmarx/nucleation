---
status: Proposed
promote_when: >-
  An independent analysis that, with the hystar package or the HysTAR
  model, again selects the two-threshold model over the one-threshold
  model in data simulated from a symptom network driven up and down by a
  stressor, and confirms the paper's simulation finding that information
  criteria detect hysteresis when the regimes differ in mean and the
  series is long; or a published version of the paper whose results stand
  as the preprint gives them.
title: 'de Jong, Ryan, van der Maas and Hamaker propose the hysteretic threshold autoregressive model to detect hysteresis in one person''s time series, as two switching thresholds of a measured control variable against one, show by simulation that it recovers hysteresis from a depression symptom network, and report that no empirical psychological series had yet been analysed with it'
version: 1
tags:
- complex-systems
- mathematical-statistics
- psychopathology-and-treatment
date: '2026-11-22'
source:
- LIT-tmpzu3i3
bears_on:
- QUESTION-045
summary: >-
  de Jong et al. (2023), [LIT-tmpzu3i3](../literature.d/LIT-tmpzu3i3.md), read in [NOTE-tmpmrw49](../notes.d/NOTE-tmpmrw49.md). The test
  [QUESTION-045](../questions.d/QUESTION-045.md)'s "individual data showing hysteresis" would need, with
  its conditions: a measured driver crossing an upper and then a lower
  threshold. Its depression case is simulated, and it reports no
  empirical psychopathology series. Proposed until its simulation results
  are reproduced or the paper is published as it stands.
---
<!-- inactive-ok-file: THEORY-058 — Proposed; the account whose promote_when names hysteresis in individual data -->

# THEORY-tmpan7c6: de Jong, Ryan, van der Maas and Hamaker propose the hysteretic threshold autoregressive model to detect hysteresis in one person's time series, as two switching thresholds of a measured control variable against one, show by simulation that it recovers hysteresis from a depression symptom network, and report that no empirical psychological series had yet been analysed with it

## Source

de Jong, Ryan, van der Maas & Hamaker (2023), [LIT-tmpzu3i3](../literature.d/LIT-tmpzu3i3.md), read in
[NOTE-tmpmrw49](../notes.d/NOTE-tmpmrw49.md).

## The account

Hysteresis is present "when the switches between two regimes are
associated with two different thresholds, one for each direction of the
state transition". In the HysTAR model an outcome series follows one
autoregressive regime or another; it switches up when a measured control
variable crosses r1 and back only when it falls below r0 < r1, and in
between it stays where it was. The ordinary threshold model is the case
r0 = r1, so comparing the two fits is a test for hysteresis in one
person's series. By simulation, the test works when the regimes differ in
mean, the series is long and the control variable is observed near both
thresholds. Fitted to data simulated from Cramer et al.'s 14-symptom
depression network, with stress moved up and down, it was preferred by
every information criterion and estimated thresholds of about −0.3 and
0.55. Its one empirical case is a speed–accuracy experiment; the authors
write that the model "has not been used to investigate hysteresis in
empirical psychological time series, so far", and that it detects
hysteresis without describing its mechanism.

## Bearing

- [QUESTION-045](../questions.d/QUESTION-045.md): makes the second kind of answer testable and states its
  conditions; it is not that answer.
- [THEORY-058](THEORY-058.md): supplies the test route 1 of its promote_when names; its
  depression evidence is simulation, which the route excludes.
