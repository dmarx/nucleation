---
status: Open
title: 'Does the conditional probability update for the spatial hypercube queueing model with server-specific service rates converge geometrically to the exact stationary distribution, and is a bound on how far the rates differ needed for it?'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-06'
line:
- readiness
- formal-apparatus
summary: >-
  Opened by the twenty-ninth status review when it checked Hua, Luo,
  Swersey and Wen's convergence proof ([THEORY-1426](../theory.d/THEORY-1426.md), [NOTE-1618](../notes.d/NOTE-1618.md)). The proof
  holds for equal rates and has a gap for unequal ones. The iteration
  converged in re-run instances where the paper's assumption fails.
---

# QUESTION-tmpfbbtg: Does the conditional probability update for the spatial hypercube queueing model with server-specific service rates converge geometrically to the exact stationary distribution, and is a bound on how far the rates differ needed for it?

## Why it is a question

Hua, Luo, Swersey and Wen's Theorem 1 states geometric convergence "Under
Assumption 3.1", a bound on how far the rates differ within each layer of
busy units ([THEORY-1426](../theory.d/THEORY-1426.md), [NOTE-1618](../notes.d/NOTE-1618.md)). The abstract and the conclusion state
it without the condition.

The proof in the paper's E-Companion (EC.1.3) bounds
|µ^{k+1}(n) p^{k+1} − µ^k(n) p^k| by µ̄n |p^{k+1} − p^k|. That is valid
only when the layer's departure rate does not change between iterations.
With equal rates the rate is fixed at nν, and the argument holds. With
unequal rates the dropped term |µ^{k+1}(n) − µ^k(n)| p^k has no bound.

The status review re-implemented the algorithm in
scratch/formal/hua_hypercube_convergence_check.py, with the exact solution
of the full generator as the control. It reached the exact distribution
in all 10 instances tried, and 6 of them violate Assumption 3.1, one with
rates within ±20% of each other. So the theorem may be true for unequal
rates without being proved. The assumption may also be stronger than
convergence needs.

## What would answer it

A complete proof for unequal rates, under Assumption 3.1 or a weaker
condition. Or an instance in which the iteration fails to converge, or
converges to the wrong distribution.
