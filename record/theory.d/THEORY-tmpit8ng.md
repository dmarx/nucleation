---
status: Proposed
promote_when: 'A result beyond the one-dimensional case where the NTK and the NNGP differ by more than a within-class rescaling. That could be a derivation for multi-dimensional or multi-class data, or a measurement of NC1, with a stated metric, on networks trained in a verified lazy regime (the tangent kernel measured to stay fixed) on real data. The measurement should show NC1 staying at its initial value while the same architecture, trained out of the lazy regime, collapses. The account is refuted by a lazy-regime network, kernel verified static, whose hidden features'' NC1 falls substantially below its value at initialization. More Gaussian-mixture simulations of NNGP against NTK cannot settle it, and neither can finite networks whose regime is not checked.'
title: 'Training a wide network in the lazy, kernel regime does not make its features more collapsed than at initialization, so neural collapse, where it occurs, is something only feature learning produces'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-20'
source:
- LIT-985
summary: >-
  The general reading that [THEORY-294](THEORY-294.md) held before the
  promotion audit narrowed it to the one-dimensional, zero-bias, two-class
  case it proves. Kothapalli and Tirer (2024),
  [LIT-985](../literature.d/LIT-985.md), read in
  [NOTE-774](../notes.d/NOTE-774.md), draw it as their conclusion: the lazy
  regime does not collapse anything, so the data-dependence of collapse has
  to come from a kernel that moves with the data. Beyond the solved case
  their support is simulation on two-class Gaussian data, where the NTK
  comes out less collapsed than the NNGP. Filed under
  [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis
  evidence can confirm or reject.
extends:
- THEORY-294
answers:
- QUESTION-192
---

# THEORY-tmpit8ng: Training a wide network in the lazy, kernel regime does not make its features more collapsed than at initialization, so neural collapse, where it occurs, is something only feature learning produces

## Source

Kothapalli and Tirer (2024), [LIT-985](../literature.d/LIT-985.md), read in [NOTE-774](../notes.d/NOTE-774.md): Theorem 5.1 (the solved case, claim C2) and Figures 2–3 (claim C3, "the NTK is not more collapsed than the NNGP in higher dimensions", moderate: Gaussian data, two classes, 10 draws).

## What is asserted, and by whom

The thesis is that lazy training never lowers within-class variability below its value at initialization, for wide networks in general and not only in the case where the tangent kernel is a within-class rescaling of the initialization kernel. Collapse is then a signature of feature learning. Kothapalli and Tirer state it as the moral of their analysis; the abstract states the higher-dimensional part as an empirical finding.

## What the record holds toward it

- [THEORY-294](THEORY-294.md) (Active): the exact result for one-dimensional data with the two classes on opposite sides of the origin and zero bias, where the equality is close to built in.
- The paper's Gaussian simulations in higher dimension, which find the NTK less collapsed than the NNGP, consistent with the thesis but not a test of lazy training of finite networks.

## What would confirm or reject it

A verified-lazy network on real data whose NC1 stays at its initial value while the same architecture, trained out of the lazy regime, collapses would confirm it; one whose NC1 falls well below its initial value with the kernel verified static would reject it. [QUESTION-192](../questions.d/QUESTION-192.md) asks the same thing as a question; this entry is the answer Kothapalli and Tirer propose.
