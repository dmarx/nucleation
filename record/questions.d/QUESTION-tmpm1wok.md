---
status: Open
title: 'Which diagnoses of frustration among a learner''s demands survive reparameterization and quotienting by function-preserving symmetries, which belong to an update geometry, and which only to a particular training organization?'
version: 1
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
  answered the first-order coordinate case, filed as CLAIM-tmpuia0a: the
  common-descent test is chart-invariant, gradient cosines are not, and a
  budgeted test needs the metric pulled back. The rest is open: function-
  preserving symmetries, which are not charts of one space, and training
  trajectories, where "same current function ≠ same learning dynamics".
  An answer sorts each diagnosis by what it is a property of.
---

# QUESTION-tmpm1wok: Which diagnoses of frustration among a learner's demands survive reparameterization and quotienting by function-preserving symmetries, which belong to an update geometry, and which only to a particular training organization?

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

CLAIM-tmpuia0a proves the first three rows. It does not answer the
question, for two reasons.

- **Function-preserving symmetries are not charts.** Permuting hidden
  units, rescaling across a ReLU, or the orthogonal map on a transformer's
  residual stream (THEORY-112) relate distinct points that compute the
  same function. Quotienting by them (CLAIM-263's protocol) is not a
  diffeomorphism of one parameter space, and at singular points the Fisher
  metric that would supply a principled geometry is degenerate
  (THEORY-082; CLAIM-305: a blow-up adds no observation). Whether a
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

For each diagnosis in use (the compatibility complex of CLAIM-tmp55mls,
the residual Φ_r of CLAIM-tmpue67e, governance regret, modular
localization), a statement of which group it is invariant under, with a
proof or a counterexample, and so whether it is a property of the
represented function, of a chosen update geometry, or of one training
organization with its optimizer. A40 §3.5 named the target: "Determine
which frustration diagnoses are properties of the represented function,
which belong to an update geometry, and which belong to a particular
training organization."
