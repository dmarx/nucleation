---
status: Proposed
title: 'In a Contextuality-by-Default test on free binary answers, estimated signalling is biased upward when true signalling is small, so a detection test that uses it stays valid at a large cost in power, and an absence verdict needs a bound that credits only the signalling a confidence bound guarantees'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  On the four-context cyclic systems of CASE-tmpjp6vg, or on any other
  stated family, either a detection test using the plug-in signalling
  estimate rejects a system on the noncontextual boundary well above its
  nominal rate (more than twice it, beyond Monte Carlo error), or an
  absence test using the plug-in or one-standard-error soft-thresholded
  estimate keeps a nominal 5% rate on the boundary at every true
  signalling level; or the upward bias of the plug-in estimate at zero
  true signalling departs from 4·√(2/π)·√(2/n) beyond Monte Carlo error.
tags:
- contextuality
- mathematical-statistics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- CASE-tmpjp6vg
- THEORY-177
complements:
- CLAIM-tmpu482h
- CLAIM-245
summary: >-
  Found by LEAD-182's power simulation (CASE-tmpjp6vg), 2026-11-22. The
  signalling term of the CbD criterion is a sum of absolute differences,
  and its plug-in estimate folds the sampling noise upward: at zero true
  signalling by about 4·√(2/π)·√(2/n), 0.23 at 400 respondents a context.
  Detection with it is conservative, and a 0.19 violation without true
  signalling needs over 4,000 respondents a context for power 0.75. The
  same bias makes an absence verdict anti-conservative: 84% false absence
  on the boundary. A Bonferroni bound crediting only guaranteed signalling
  is valid. CLAIM-105's defeat condition asks for "a signalling estimator
  with bias correction"; this says what the bias costs and which way it
  cuts. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpjp6vg CLAIM-tmpu482h CASE-tmpl2va4 — new; the simulation this claim rests on, its companion and the design that applies it -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; the claim whose defeat condition asks for this estimator -->
<!-- inactive-ok-file: LEAD-182 — Open; the lead this was found for -->

# CLAIM-tmpalxab: In a Contextuality-by-Default test on free binary answers, estimated signalling is biased upward when true signalling is small, so a detection test that uses it stays valid at a large cost in power, and an absence verdict needs a bound that credits only the signalling a confidence bound guarantees

## The claim

In a cyclic system the CbD criterion is Δ_C = s_odd(E) − (n − 2) − Δ,
where Δ sums, over contents, the absolute difference between the
content's marginal means in its two contexts (THEORY-177). When the
answers are free, Δ has to be estimated, and the natural estimate,
Σ|d̂_q|, is biased upward wherever a true difference is small beside its
standard error. At zero true signalling each |d̂_q| is a folded normal,
with mean √(2/π) times its standard error; for four contents and n
respondents a context, about 4·√(2/π)·√(2/n). The simulation
(CASE-tmpjp6vg) finds 0.226 at n = 400 and 0.112 at 1,600, as predicted.

Three consequences, each found in the simulation:

1. **Detection is valid.** An overestimated Δ underestimates Δ_C, so a
   test that declares contextuality when a lower bound of the plug-in
   Δ_C is above 0 errs on the safe side. Its boundary false-detection
   rate was at most 0.068 across the grid, near 0 at low signalling.
2. **Its power is lowest exactly where the data look cleanest.** The bias
   shrinks as 1/√n, like the standard error, so it never becomes
   negligible relative to it. A 0.19 violation with no true signalling
   is detected with power 0.24 at 2,500 respondents a context and 0.65 at
   4,000; with signalling of 0.3, 0.80 at 1,600. Assuming the signalling
   away, as a symmetric response format does, would make the test look
   cheaper than it is.
3. **Absence is the opposite case.** An upper bound on Δ_C that uses the
   plug-in Δ is too low, so declaring noncontextuality when it is below 0
   is anti-conservative: 84% false absence on the boundary at zero
   signalling, and 17% for a truly contextual system at n = 400.
   Shrinking each difference by one standard error does not repair it
   (21% on the boundary) and spoils detection (up to 62% false
   detection). What works is a bound that credits only the signalling a
   lower confidence bound guarantees, combined by Bonferroni with an
   upper bound on the correlations: at most 3% false absence. It can
   certify absence only where signalling is small.

## What it does not say

- That the plug-in test is the best valid detection test. A
  likelihood-ratio test against the noncontextual set might be more
  powerful; it was not built.
- That published CbD verdicts are wrong. Detections reported with a
  bootstrap on the plug-in statistic, such as the Snow Queen study
  (LIT-tmp43x53), err if at all toward missing contextuality. But a
  published "noncontextual" verdict at a modest sample size, from a
  point estimate below zero, is not by itself evidence of absence.
- Anything about human judgements. It is a property of the estimator on
  stated models.

## What it bears on

CLAIM-325's defeat condition asks for contextuality "at adequate power,
with its signalling accounted for". This claim says what accounting for
signalling costs: the power has to be computed with the signalling
estimated, not assumed. CLAIM-105's defeat condition counts changes
"beyond sampling error", which its note of 2026-10-29 says "needs a
signalling estimator with bias correction and a stated sampling error";
here the bias is quantified and its direction shown to differ between the
two verdicts. And CLAIM-219's first horn, that the data read show no
contextuality proper, rests on nulls whose power the record has not
computed in this way.
