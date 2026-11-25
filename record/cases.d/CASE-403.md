---
number: 403
status: Proposed
formerly:
- CASE-tmphawe9
title: 'Frozen circuit computing x²'
statement: >-
  A frozen circuit that computes x² exactly on every input and cannot learn:
  it tracks the function under every change of input that preserves it and
  gains nothing when the target shifts to x² + c
version: 1
standing: fictional
kind: construction
tags:
- epistemology
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
variant_of:
- CASE-409
bears_on:
- QUESTION-493
- QUESTION-360
draws_on:
- THEORY-438
summary: >-
  The ninth of the set [LEAD-001](../leads.d/LEAD-001.md) asks for, the one on which the candidate
  readings of understanding part. A circuit, the frozen end state of a
  learner like [CASE-409](CASE-409.md)'s R, computes x² exactly on every input and
  has no plasticity left. It tracks the structure perfectly and cannot
  learn x² + c at any budget. It tests A84's question whether
  understanding "necessarily entails greater future learnability". The
  construction is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-438 CLAIM-754 TERM-131 — Proposed; cited as the criteria applied, not relied on -->
<!-- inactive-ok-file: CASE-409 CASE-394 CLAIM-1092 CLAIM-1059 CLAIM-1142 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-403: Frozen circuit computing x²

## The case

Learner R of [CASE-409](CASE-409.md) is trained, then frozen: its program x ↦ x · x
is compiled into a fixed circuit with exact arithmetic and no parameter
any further experience can change. Call it F.

- On every input, F returns x², exactly. Under every change of input that
  preserves the structure (any integer, any representation of it), F
  tracks the function.
- When the target becomes x² + c, F can be shown any number of pairs and
  remains x². Its developmental frontier, in [CLAIM-754](../claims.d/CLAIM-754.md)'s sense, coincides
  with its operational one: there is nothing it can come to do that it
  cannot already do.
- F has stopped being a learning system in [TERM-131](../terms.d/TERM-131.md)'s sense; it was one,
  and its organization is the product of learning.

## What it separates

F separates the two criteria for understanding that [QUESTION-493](../questions.d/QUESTION-493.md)'s
candidate and the record hold:

- **Stable tracking** ([THEORY-438](../theory.d/THEORY-438.md): understanding as stable tracking under
  structure-preserving perturbation). F tracks x² perfectly, better than
  R′ of [CASE-394](CASE-394.md). On this criterion F understands x².
- **Developmental value** (A73: understanding shows as cheap acquisition
  of the next target). F acquires nothing. On this criterion F knows
  every value of x² and does not understand it.

Knowledge of the values is not in question: on A73's criteria F knows
them all, reliably and grounded in the rule.

## Against the candidate answers

A84 asks: "Does understanding necessarily entail greater future
learnability?" F is where the answer matters. Two readings, filed as
alternatives:

- [CLAIM-1092](../claims.d/CLAIM-1092.md) (the assistant's lean): understanding is stable tracking;
  F understands; learnability is the usual sign in a learner, not a
  condition. For a learner the two criteria coincide, as [CASE-409](CASE-409.md)
  shows; F is not a learner.
- [CLAIM-1059](../claims.d/CLAIM-1059.md): understanding is developmental value; F knows without
  understanding; understanding entails learnability by definition.

## What it can show

That the two criteria the record has for understanding are not
equivalent, and that their difference lies only in systems that cannot
learn further. Being a construction, nothing about real systems, though
a deployed model with frozen weights and no in-context adaptation for
the relevant task is near it. One of the separations [CLAIM-1142](../claims.d/CLAIM-1142.md)
collects, on the reading [CLAIM-1092](../claims.d/CLAIM-1092.md) takes.
