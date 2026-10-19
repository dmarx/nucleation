---
status: Open
title: 'Does the landmark readout of a learned contrastive density ratio keep its 1/m rate under a finite second moment of the ratio alone, without a uniform bound on it?'
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-19'
line: 'pragmatic-transport'
refines:
- QUESTION-052
summary: >-
  Filed when the promotion audit (batch 037, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-319](../theory.d/THEORY-319.md) to Tosh, Krishnamurthy and Hsu's redundancy and
  landmark bounds for the exact density ratio, re-derived step by step.
  Its former promote_when also asked whether a learned ratio keeps the
  rate without the uniform bound Theorems 10–11 assume. This question
  holds that clause.
---

# QUESTION-tmpdttll: Does the landmark readout of a learned contrastive density ratio keep its 1/m rate under a finite second moment of the ratio alone, without a uniform bound on it?

## Why it is a question

[THEORY-319](../theory.d/THEORY-319.md) now states that, for the exact ratio g* = p(x,z)/(p(x)p(z)), a
bounded label and E[g*²] finite, a linear readout of m landmark
evaluations comes within O(1/m) of the infer-then-predict function in mean
squared error. The source's error-propagation results for a learned ratio
(Theorems 10–11) add terms in (1 + g_max)²√ε_opt and (1 + g_max)⁴ε_opt,
where g_max is a uniform bound on the ratio. Many natural joint laws have
an unbounded ratio with a finite second moment, the paper's Gaussian model
among them.

## What would answer it

A bound on the readout's excess risk in terms of the excess logistic (or
direct) loss and E[g*²], with no g_max, would answer it yes. A family of
joint laws with E[g*²] bounded and learned ratios of vanishing excess loss
whose landmark readouts stay far from the infer-then-predict function would
answer it no. What cannot settle it: linear-probe accuracies of trained
contrastive networks, where neither the ratio nor its excess loss is
measured.
