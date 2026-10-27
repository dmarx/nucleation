---
number: 127
status: Open
formerly:
- QUESTION-tmpm1wok
title: 'Which diagnoses of frustration among a learner''s demands survive quotienting by function-preserving symmetries, which belong only to an update geometry, and which only to a particular training organization with its optimizer?'
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Narrowed under ADR-049 at the status review of 2026-10-27. The
    part about smooth changes of chart is QUESTION-tmpel2n2, Answered
    by CLAIM-366. This question keeps function-preserving symmetries
    and trajectories.
tags:
- information-geometry
- loss-landscapes
- representation-learning
date: '2026-10-18'
line: learned-structure
summary: >-
  A34 §6G of the exchange of 2026-10-17: "When do two functionally
  equivalent parameterizations yield equivalent frustration diagnoses?"
  The owner, at U35: "interesting question, double click on this." A35
  answered the first-order coordinate case, filed as [CLAIM-366](../claims.d/CLAIM-366.md): the
  common-descent test is chart-invariant, gradient cosines are not, and a
  budgeted test needs the metric pulled back. The rest is open: function-
  preserving symmetries, which are not charts of one space, and training
  trajectories, where "same current function ≠ same learning dynamics".
  An answer sorts each diagnosis by what it is a property of.
refined_by:
- QUESTION-tmpel2n2
---

# QUESTION-127: Which diagnoses of frustration among a learner's demands survive quotienting by function-preserving symmetries, which belong only to an update geometry, and which only to a particular training organization with its optimizer?

## Why it is a question

A34 §6G: "A raw parameter gradient, gradient angle, or norm value can
depend on the chosen coordinates." "An architecture-sensitive modular norm
is more informative than an arbitrary Euclidean parameter norm, but it is
still a specified geometry; it is not automatically invariant under every
function-preserving reparameterization." A34: "Without it, some supposed
differences in organizational strain may reflect coordinate choices rather
than different learning dynamics." The owner, at U35: "interesting
question, double click on this."

A35 §2 sorted five diagnostics:

| Diagnostic | A35's expected invariance |
|---|---|
| Pairwise Euclidean gradient angles | Not invariant under general reparameterization |
| Common strict first-order descent, all tangent directions allowed | Invariant under smooth invertible coordinate changes |
| Budgeted feasibility, update geometry transported | Locally invariant under the same changes |
| Actual finite-step trajectories | Not necessarily invariant unless the update rule and its state transform too |
| Feasibility of specified changes to the represented function | Invariant under function-preserving parameterization, with the function class and allowed changes fixed |

[CLAIM-366](../claims.d/CLAIM-366.md) proves the first three rows. It does not answer the
question, for two reasons.

- **Function-preserving symmetries are not charts.** Permuting hidden
  units, rescaling across a ReLU, or the orthogonal map on a transformer's
  residual stream ([THEORY-112](../theory.d/THEORY-112.md)) relate distinct points that compute the
  same function. Quotienting by them ([CLAIM-263](../claims.d/CLAIM-263.md)'s protocol) is not a
  diffeomorphism of one parameter space, and at singular points the Fisher
  metric that would supply a principled geometry is degenerate
  ([THEORY-082](../theory.d/THEORY-082.md); [CLAIM-305](../claims.d/CLAIM-305.md): a blow-up adds no observation). Whether a
  frustration verdict is constant on symmetry orbits is open.
- **Trajectories carry the optimizer.** A35: "two parameterizations can
  compute the same current function while yielding different future
  trajectories under SGD, Adam, weight decay, or another fixed optimizer."
  And: "If we are evaluating an actual training system, optimizer
  dependence is part of what we're trying to explain—not necessarily a
  nuisance to quotient away."

A39 §5 restated it as an open question: "Which frustration diagnoses
survive reparameterization or quotienting by function-preserving
symmetries?" A40 §3.5 split it into three invariances: coordinates,
function-preserving symmetries, and future learning dynamics.

## What would count as an answer

For each diagnosis in use (the compatibility complex of [CLAIM-347](../claims.d/CLAIM-347.md),
the residual Φ_r of [CLAIM-365](../claims.d/CLAIM-365.md), governance regret, modular
localization), a statement of which group it is invariant under, with a
proof or a counterexample, and so whether it is a property of the
represented function, of a chosen update geometry, or of one training
organization with its optimizer. A40 §3.5 named the target: "Determine
which frustration diagnoses are properties of the represented function,
which belong to an update geometry, and which belong to a particular
training organization."

## Note of 2026-10-27: the coordinate part split off

The status review of this date split this question under ADR-049. Changes
of chart are QUESTION-tmpel2n2, Answered by CLAIM-366. This question keeps
what is still open: function-preserving symmetries, which are not charts
of one space, and trajectories, which carry the optimizer.
