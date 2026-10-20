---
status: Open
title: 'Does lazy-regime training leave the within-class variability of a network''s features at its initial value beyond one-dimensional, zero-bias, two-class data, where the tangent and initialization kernels are not proportional?'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-19'
line: 'learned-structure'
refines:
- QUESTION-051
summary: >-
  The promotion condition formerly on [THEORY-294](../theory.d/THEORY-294.md). [THEORY-294](../theory.d/THEORY-294.md) was narrowed
  to Kothapalli and Tirer's Theorem 5.1 and promoted on 2026-10-19
  ([ADR-047](../decisions.d/ADR-047.md) v2): for a wide two-layer ReLU network with zero bias on
  one-dimensional data whose classes lie on opposite sides of the origin,
  the tangent kernel is a constant multiple of the initialization kernel,
  so NC1 is unchanged. Whether lazy training leaves NC1 in place where the
  kernels are not proportional is open.
---

# QUESTION-tmpx46z2: Does lazy-regime training leave the within-class variability of a network's features at its initial value beyond one-dimensional, zero-bias, two-class data, where the tangent and initialization kernels are not proportional?

## Why it is a question

[THEORY-294](../theory.d/THEORY-294.md) holds the proportional case. There both ReLU kernels are a
constant times x·x′ within a class and zero across, and NC1, a ratio of
two linear functionals of the kernel, cannot tell them apart. Beyond one
dimension the kernels are not proportional. The same paper's simulations
on two-class Gaussian mixtures up to 128 dimensions find the tangent
kernel's NC1 never below the initialization kernel's, and higher for
ReLU. That is not equality, and it is not a proof. The reading that
collapse needs feature learning rests on this wider case. Until
2026-10-19 it was [THEORY-294](../theory.d/THEORY-294.md)'s promote_when.

## What would answer it

- A derivation for multi-dimensional or multi-class data, or with
  nonzero bias, that bounds the tangent kernel's NC1 against the
  initialization kernel's.
- A measurement of NC1, with a stated metric, on networks trained in a
  verified lazy regime (the tangent kernel measured to stay fixed) on real
  data, beside the same architecture trained out of that regime.

Against it: a lazy-regime network, kernel verified static, whose hidden
features' NC1 falls well below its value at initialization.

What would not answer it: more Gaussian-mixture simulations comparing the
two infinite-width kernels, or finite networks whose regime is not
checked.
