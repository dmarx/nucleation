---
number: 39
status: Open
formerly:
- LEAD-tmp3x8zu
title: 'Find the structural condition on the joint distribution under which information-bottleneck optima are nested, or an example of incomparable optima at finite beta'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- information-theory
- learning-theory
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-220
summary: >-
  Named in [NOTE-976](../notes.d/NOTE-976.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: QUESTION-244 — Answered; cited as the split-off half the lead asks for -->

# LEAD-039: Find the structural condition on the joint distribution under which information-bottleneck optima are nested, or an example of incomparable optima at finite beta

## What it would do

Work beyond the special cases the record holds, with the size of the loss.

Where the record names it:

- [NOTE-976](../notes.d/NOTE-976.md): "An example of incomparable optima at finite"

## What would count

A condition or a counterexample answers [QUESTION-220](../questions.d/QUESTION-220.md).

## Note of 2026-11-22: half already held, by [CLAIM-387](../claims.d/CLAIM-387.md) and [CLAIM-392](../claims.d/CLAIM-392.md)

The lead audit of this date found the lead's second disjunct already
held. Incomparable information-bottleneck optima at finite beta are
[CLAIM-387](../claims.d/CLAIM-387.md) (Active) for deterministic encoders and [CLAIM-392](../claims.d/CLAIM-392.md) (Active) for
stochastic ones, and [QUESTION-244](../questions.d/QUESTION-244.md) (Answered) records them. [QUESTION-220](../questions.d/QUESTION-220.md)
was split on 2026-10-21 and again on 2026-10-27 so that it keeps only the
structural condition on P(X, Y) beyond [THEORY-757](../theory.d/THEORY-757.md)'s special cases, the
size of the loss, and [THEORY-163](../theory.d/THEORY-163.md)'s colour hierarchy; so a counterexample
no longer answers it, though "What would count" above says it does. The
structural condition is not held. No status or stage is changed here.

## Note of 2026-11-22: a sufficient structural condition, a closure, and a bound on the loss
<!-- inactive-ok-file: CLAIM-939 CLAIM-940 CLAIM-941 CASE-360 — new; filed from this lead -->

The lead was worked on the branch claude/lead-039-ib-nesting, formally,
with numerical support under scratch/studies/lead-039/. Three claims and
a study were filed, all Proposed:

- [CLAIM-939](../claims.d/CLAIM-939.md) (demonstrated): optima nest at every pair of budgets
  whenever p(Y|x) takes at most two distinct values, for any finite Y.
  This widens [THEORY-757](../theory.d/THEORY-757.md)'s binary case; the step that used binary Y holds
  because φ(r) = r(1 − r) Σ_y Δ_y²/s_y(r) is a sum of concave
  harmonic-mean terms.
- [CLAIM-940](../claims.d/CLAIM-940.md) (demonstrated): refinability at every pair of budgets is
  closed under independent products. With the first, every source that is
  an independent product of two-row and function pairs nests, with any
  number of distinct rows.
- [CLAIM-941](../claims.d/CLAIM-941.md) (demonstrated): forcing nesting costs at most the chord
  gap I(λ₁) − (λ₁/λ₂) I(λ₂) of the information curve.
- [CASE-360](../cases.d/CASE-360.md): the study. No exception to either theorem; clear
  failures in a fifth to a third of random three-row sources (uncertified).

What remains: a condition that is necessary as well as sufficient (none is
proposed; random three-row sources both nest and fail); the exact size of
the loss, which needs an optimization over garblings; the other direction
of forcing nesting (extending the coarse optimum); and [THEORY-163](../theory.d/THEORY-163.md)'s colour
hierarchy. The stage and status are unchanged.
