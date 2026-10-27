---
status: Answered
title: 'Under smooth invertible changes of the parameter coordinates, which first-order frustration diagnoses among a learner''s demands are invariant: pairwise Euclidean gradient angles, common strict first-order descent, or budgeted feasibility with the update geometry transported?'
version: 1
tags:
- information-geometry
- loss-landscapes
- representation-learning
date: '2026-10-27'
line: learned-structure
refines:
- QUESTION-127
summary: >-
  The coordinate part of [QUESTION-127](QUESTION-127.md), split off by the status review of
  2026-10-27 under [ADR-049](../decisions.d/ADR-049.md), because [CLAIM-366](../claims.d/CLAIM-366.md) (Active) settles it in full.
  Common strict descent, 0 ∉ conv{g_i}, is invariant under smooth
  invertible reparameterization. The sign of a Euclidean gradient inner
  product is not, and a negative inner product does not exclude common
  descent. A budgeted test is invariant when the metric is pulled back.
  These are the first three rows of A35 §2's table.
---

# QUESTION-tmpel2n2: Under smooth invertible changes of the parameter coordinates, which first-order frustration diagnoses among a learner's demands are invariant: pairwise Euclidean gradient angles, common strict first-order descent, or budgeted feasibility with the update geometry transported?

## The question

A35 §2 of the exchange of 2026-10-17 sorted five diagnostics by their
expected invariance. The first three are about charts of one parameter
space, and this question asks about those three.

## The answer

[CLAIM-366](../claims.d/CLAIM-366.md), Active, proves all three rows:

- **Common strict first-order descent** (0 ∉ conv{g_i}) is invariant under
  smooth invertible reparameterization. The chart's Jacobian is invertible,
  so it maps the descent cone of one chart onto that of the other.
- **The sign of a Euclidean gradient inner product** is not invariant. A
  negative inner product does not exclude common descent.
- **Budgeted feasibility** is invariant once the update geometry is pulled
  back along the change of chart.

The other two rows, function-preserving symmetries and finite-step
trajectories, are not changes of chart, and they remain [QUESTION-127](QUESTION-127.md)'s.
