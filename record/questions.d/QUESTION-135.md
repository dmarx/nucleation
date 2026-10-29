---
number: 135
status: Open
formerly:
- QUESTION-tmpw9b04
title: 'When does spectral differentiation among learned features correspond to stabilizing coexistence among the processes that implement them, and what besides the feature geometry decides it?'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the readings of Mehta et al. and
    Chizat and Bach. The question is unchanged.
tags:
- representation-learning
- ecology
- complex-systems
date: '2026-10-18'
line: distributed-agency
refines:
- QUESTION-083
summary: >-
  From the synthesis the owner relayed on 2026-10-18. In symmetric
  resource-mediated competition the interaction matrix is the Gram matrix
  of the components' feature vectors, A = UᵀU, so representational
  redundancy and competitive overlap are one object ([CLAIM-369](../claims.d/CLAIM-369.md)). In
  the two-component case invasion growth equals λ_min(A) ([CASE-118](../cases.d/CASE-118.md)).
  But the same A supports coexistence or exclusion depending on the growth
  rates. An answer says when the Gram spectrum of a learned representation
  predicts that the processes carrying its features will coexist, and what
  else, such as supply, task distribution or evaluation opportunities, has
  to be fixed for it to.
---
<!-- inactive-ok-file: CLAIM-193 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# QUESTION-135: When does spectral differentiation among learned features correspond to stabilizing coexistence among the processes that implement them, and what besides the feature geometry decides it?

## Why it is a question

The record already treats a representation as fixed by its kernel up to
symmetries ([THEORY-004](../theory.d/THEORY-004.md)), and holds that a linear probe family sees only
differences in normalized kernel ([CLAIM-193](../claims.d/CLAIM-193.md)). [CLAIM-369](../claims.d/CLAIM-369.md) shows that,
in symmetric resource competition, the kernel is also the competition
matrix. That suggests that how differentiated a set of features is
spectrally might predict whether the processes implementing them coexist.

[CASE-118](../cases.d/CASE-118.md) shows where the suggestion holds and where it fails. With
equal growth rates the rare component's invasion growth is exactly
λ_min(A) = 1 − ρ. With growth rates 1 ± δ the same A supports
coexistence only for |δ| < (1 − ρ)/(1 + ρ). So feature geometry is
necessary context and not sufficient. The supply, meaning the tasks,
resources or evaluation opportunities the system offers, also decides.
That is [CLAIM-152](../claims.d/CLAIM-152.md)'s target-relativity: what a representation supports
depends on what it is asked for.

## What would answer it

Conditions, in a stated class of learning systems, under which the Gram
spectrum of the learned features predicts the recovery rates of the
processes carrying them, together with the further quantities that must
be fixed for the prediction to hold. The answer should keep three
measurements apart:

- structural differentiation, from feature geometry;
- functional differentiation, from conditional performance across
  contexts;
- dynamical stabilization, from recovery when rare and from persistence.

It bears on [QUESTION-125](QUESTION-125.md). A change in feature geometry, such as an
eigengap opening, and a change in coexistence, such as a component
becoming able to invade, need not happen at the same parameter values. A
model in which they come apart in either direction would be informative.

## What would not answer it

Heterogeneous embeddings, or a well-conditioned Gram matrix, with no
account of recovery dynamics.

## Note of 2026-10-29: a large-system instance, and a model with no spectral condition

Two works read on this date bear on the question.

- Mehta, Cui, Wang and Marsland, LIT-1231 (NOTE-tmpwkbtk): in random
  quadratic programming the variance σ_c of the constraint vectors sets
  how many components survive, and more differentiated constraints
  coexist more. That is a large-system instance of the suggestion above,
  with the supply K and the costs m entering through the growth rates, as
  CASE-118 found for two components.
- Chizat and Bach, LIT-1232 (NOTE-tmpbs06i), supply no spectral
  condition. Their coexistence notion is first-order, the sign of F′, not
  the growth-rate comparison CASE-118 uses.

The question is unchanged and stays Open.
