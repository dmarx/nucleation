---
status: Open
title: 'On two-scale Lorenz 96 at ε = 0.5, K = 18, J = 20, F = 10, h_x = −1, h_y = 1, does a NARMAX discrepancy closure whose structure is chosen by a rule fixed before scoring still match the full system''s x₁ statistics (Kolmogorov–Smirnov distance) and beat a polynomial-plus-AR(1) closure on lead time at anomaly correlation 0.6, at δ = 0.05?'
version: 1
tags:
- probabilistic-modeling
- complex-systems
- natural-sciences
date: '2026-10-30'
line: distributed-agency
summary: >-
  The promotion condition formerly on THEORY-818, moved here when the
  status review of 2026-10-30 promoted it under ADR-065. Chorin and Lu
  chose the closure's orders by trial and error against statistics they
  then report; whether the result survives a selection rule fixed in
  advance and an independent rerun is this question.
---

# QUESTION-tmpe8p5t: On two-scale Lorenz 96 at ε = 0.5, K = 18, J = 20, F = 10, h_x = −1, h_y = 1, does a NARMAX discrepancy closure whose structure is chosen by a rule fixed before scoring still match the full system's x₁ statistics (Kolmogorov–Smirnov distance) and beat a polynomial-plus-AR(1) closure on lead time at anomaly correlation 0.6, at δ = 0.05?

## Why it is a question

THEORY-818 reports what Chorin and Lu (LIT-1304, read in NOTE-1028)
measured: on Lorenz 96 with no gap of time scales, a NARMAX closure with
one or two lags reproduces x₁'s statistics and doubles the forecast lead
time at δ = 0.05. Its model structure was chosen "by trial and error"
against the long-run mean and autocorrelation, which are among the
statistics then reported, and the forecast comparison is read from plotted
curves. The result is in-sample in its selection. Whether a short discrete
memory still suffices when the structure is fixed before scoring is open.

## What would answer it

A rerun of the two-scale Lorenz 96 test at the paper's parameters
(ε = 0.5, K = 18, J = 20, F = 10, h_x = −1, h_y = 1), by the record or
another group, that fits the discrepancy NARMAX with a structure chosen by
a rule fixed before scoring, and reports the Kolmogorov–Smirnov distance of
x₁ and the lead time at anomaly correlation 0.6 against the full system and
against the polynomial-plus-AR(1) closure, at δ = 0.05 at least. A rerun
whose model orders were tuned on the scored statistics, or a comparison
read off figures, does not settle it.
