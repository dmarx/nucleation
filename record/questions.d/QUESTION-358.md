---
number: 358
status: Open
formerly:
- QUESTION-tmpiwx25
title: 'Does an independent computation of the linearized plane Couette and Poiseuille operators in the energy norm reproduce transient growth of order R, resonance of order R² and a minimal destabilizing perturbation of order R⁻², with leading constants near those of Trefethen et al.''s Table 1?'
version: 1
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-10-30'
line: formal-apparatus
summary: >-
  The promotion condition formerly on [THEORY-304](../theory.d/THEORY-304.md), moved here when the status
  review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). The lower bounds are
  [CLAIM-383](../claims.d/CLAIM-383.md)'s derivation; the upper orders and the constants rest on one
  computation ([LIT-932](../literature.d/LIT-932.md), read in [NOTE-839](../notes.d/NOTE-839.md)). Reddy & Henningson (1993) and
  Schmid & Henningson's monograph are the obvious independent sources,
  unread.
---

# QUESTION-358: Does an independent computation of the linearized plane Couette and Poiseuille operators in the energy norm reproduce transient growth of order R, resonance of order R² and a minimal destabilizing perturbation of order R⁻², with leading constants near those of Trefethen et al.'s Table 1?

## Why it is a question

[THEORY-304](../theory.d/THEORY-304.md) holds the scalings Trefethen, Trefethen, Reddy and Driscoll computed
for the linearized shear flows in the energy norm. [CLAIM-383](../claims.d/CLAIM-383.md) derives the lower
bounds (growth at least cR, resonance at least cR², a destabilizing perturbation
of norm at most CR⁻²). That growth is no more than order R, and the constants of
Table 1, rest on that one computation, which credits the results to earlier
work the record has not read.

## What would answer it

An independent computation or review of the linearized plane Couette and
Poiseuille operators, such as Reddy & Henningson (1993) or Schmid & Henningson's
monograph, read here and reproducing the O(R) transient growth, O(R²) resonance
and O(R⁻²) minimal destabilizing perturbation with constants near those of
Table 1. A correct computation in the energy norm showing growth bounded
independently of R would refute the scalings; [CLAIM-383](../claims.d/CLAIM-383.md) already excludes it.
Experiments on transition cannot settle it: they bear on the transition
conjecture, not on the linear scalings.
