---
number: 357
status: Open
formerly:
- QUESTION-tmphn7l4
title: 'Outside MNIST and CIFAR-10, or under a second probe family such as a regularized nonlinear readout, do encoders constrained to preserve their input''s information exactly still span a range of downstream quality that includes worse than the raw input?'
version: 1
tags:
- representation-learning
- information-theory
date: '2026-10-30'
line: learned-structure
summary: >-
  The promotion condition formerly on [THEORY-227](../theory.d/THEORY-227.md), moved here when the status
  review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). Tschannen et al. ([LIT-247](../literature.d/LIT-247.md),
  read in [NOTE-749](../notes.d/NOTE-749.md)) showed the spread on MNIST halves, with CIFAR-10 for two
  experiments, under a linear probe only.
---

# QUESTION-357: Outside MNIST and CIFAR-10, or under a second probe family such as a regularized nonlinear readout, do encoders constrained to preserve their input's information exactly still span a range of downstream quality that includes worse than the raw input?

## Why it is a question

[THEORY-227](../theory.d/THEORY-227.md) holds the existence result: invertible encoders all keep the true
mutual information, and under a linear probe on MNIST halves some score above
raw pixels and one, trained adversarially, scores well below. Whether such a
spread of quality among exactly information-preserving encoders is general, or
belongs to small images and linear probes, is open.

## What would answer it

A replication outside MNIST and CIFAR-10, or with a second probe family (for
example a regularized nonlinear readout), in which encoders constrained to
preserve the input's information exactly again span a range of downstream
quality that includes worse than the raw input. The answer is no if, among
exactly information-preserving encoders, downstream quality under the probes in
use is constant, or is ordered by some information quantity of the encoder
alone. Comparisons of MI estimates cannot settle it, since the question is
about true mutual information, which the estimators do not measure.
