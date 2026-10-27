---
status: Answered
title: 'For finite X and Y, does every finite-budget information-bottleneck optimum nest under the β → ∞ optimum, what test on a pair of optimal encoders decides whether two finite budgets nest, and do the optima nest at every pair of budgets when Y is a function of X or when X and Y are both binary?'
version: 1
tags:
- information-theory
- learning-theory
- representation-learning
date: '2026-10-27'
line: learned-structure
refines:
- QUESTION-220
summary: >-
  The settled part of [QUESTION-220](QUESTION-220.md), split off by the status review of
  2026-10-27 under [ADR-049](../decisions.d/ADR-049.md), because [THEORY-743](../theory.d/THEORY-743.md), [THEORY-753](../theory.d/THEORY-753.md) and [THEORY-757](../theory.d/THEORY-757.md)
  (Active) answer it. Every finite-β optimum is a stochastic coarsening of
  the causal partition. Two budgets nest iff some pair of optimal encoders
  forms X → T₂ → T₁, a convex-hull test on decoder points. The optima nest
  at every pair of budgets when Y is a function of X and when X and Y are
  both binary.
---

# QUESTION-tmpt5ucu: For finite X and Y, does every finite-budget information-bottleneck optimum nest under the β → ∞ optimum, what test on a pair of optimal encoders decides whether two finite budgets nest, and do the optima nest at every pair of budgets when Y is a function of X or when X and Y are both binary?

## The question

[QUESTION-220](QUESTION-220.md) asks what condition on P(X, Y) guarantees that the
information-bottleneck optimum at a coarser budget is a (possibly noisy)
function of the optimum at a finer one. Three parts of that are settled:
nesting under the top level, the test for a given pair of budgets, and
two classes of distribution where nesting always holds.

## The answer

- **Under the top level, yes.** [THEORY-743](../theory.d/THEORY-743.md), Active: every IB optimum at
  every β gives one encoder to all inputs sharing p(y|x), so it is a
  stochastic coarsening of the minimal sufficient partition, the β → ∞
  limit.
- **The test.** [THEORY-753](../theory.d/THEORY-753.md), Active: the bottleneck is refinable from λ₁ to
  λ₂ > λ₁ iff some pair of optimal encoders forms X → T₂ → T₁, that is,
  iff the coarse encoder is a garbling of a fine one. With affinely
  independent fine decoder points this is a convex-hull inclusion that a
  linear programme decides.
- **Two classes, yes.** [THEORY-757](../theory.d/THEORY-757.md), Active: refinable at every pair of
  budgets when Y is a function of X, by nested erasures of Y, and when X
  and Y are both binary. Binary Y alone does not suffice.

A condition on P(X, Y) beyond these cases, and the size of the loss when
nesting fails, remain [QUESTION-220](QUESTION-220.md)'s.
