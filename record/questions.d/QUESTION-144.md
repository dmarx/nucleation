---
number: 144
status: Open
formerly:
- QUESTION-tmpnm9ml
title: 'Beyond a finite state space, does an observable commute with a Markov generator exactly when its mean and second moment are conserved in every state, and is there a component form of that condition on general state spaces?'
version: 1
tags:
- mathematics
- probabilistic-modeling
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The general-space clause of [THEORY-158](../theory.d/THEORY-158.md)'s former promote_when, moved here
  on 2026-10-19, when [THEORY-158](../theory.d/THEORY-158.md) was narrowed to the finite state space and
  promoted. Baez and Fong state the moment form on σ-finite measure spaces
  (Theorems 2–3). The record has read Theorem 3, but has not re-derived it,
  and Theorem 2 is stated there as a consequence. The paper gives no
  component form beyond finite X.
---

# QUESTION-144: Beyond a finite state space, does an observable commute with a Markov generator exactly when its mean and second moment are conserved in every state, and is there a component form of that condition on general state spaces?

## Why it is a question

[THEORY-158](../theory.d/THEORY-158.md) holds Baez and Fong's Theorem 1 on a finite state space, where
four conditions are equivalent: [O, H] = 0; every polynomial in O has a
constant mean; O and O² have constant means; and O is constant on each
connected component of the transition graph. The record re-derived the
cycle. Until 2026-10-19 [THEORY-158](../theory.d/THEORY-158.md)'s promote_when also allowed "a checked
extension of the component form to general state spaces". At the owner's
direction, from the promotion audit's batch 008 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was
narrowed to the finite case, and the general-space clause moved here.

It is open because, on σ-finite measure spaces, the source gives only the
moment form. Theorem 3 covers a single stochastic operator and is proved by
Chebyshev's inequality. Theorem 2 covers Markov semigroups and is stated as
a consequence. Neither has been re-derived here, and there is no component
form.

## What would answer it

A checked derivation of the moment form for Markov semigroups on general
state spaces, under stated conditions, or a checked extension of the
component form to general state spaces, with the notion of "component"
that it needs.
