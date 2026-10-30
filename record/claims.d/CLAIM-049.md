---
number: 49
status: Active
formerly:
- CLAIM-tmpduv33
title: 'An adaptive interpreter''s state includes its message, context knowledge and learned parameters, and learning can make some relational invariants more stable and others less'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the seventeenth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its one
    premise, CLAIM-074, is Active; no objection is filed against it;
    and nothing in the record meets its defeat condition. The title
    and defeat condition are unchanged. Status Proposed to Active.
    THEORY-155 and THEORY-489 are added as corroborated_by (ADR-058).
role: thesis
warrant: interpretive
defeated_if: >-
  Adapted and unadapted interpreters conserve the same relational
  observables at the same rates along reconstruction chains.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
rests_on:
- CLAIM-074
corroborated_by:
- THEORY-155
- THEORY-489
summary: >-
  A110 §22, recovered, with its case: a translator familiar with an
  underworld genre conserves its affiliative humour, a naive one turns
  it into a moral statement. The manuscript keeps one sentence (§11) on
  adapted receivers.
---
<!-- inactive-ok-file: CLAIM-059 CLAIM-074 CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-049: An adaptive interpreter's state includes its message, context knowledge and learned parameters, and learning can make some relational invariants more stable and others less

## The claim

A110 §22: "We can represent the effective state of an interpreter as
W_i = (U_i, K_i, θ_i), where U_i is the current message, K_i is contextual
knowledge, and θ_i denotes the relevant learned or adaptive parameters. A
reconstruction kernel acts on this enlarged state. This matters because the same
source expression need not produce the same target distribution under different
interpreters. A translator familiar with a historical underworld genre might
conserve its affiliative humor. An interpreter without that knowledge might
reconstruct it as a generic moral statement about irresponsible spending.
Learning can make some relational invariants more stable and others less stable."

## Where it went

Manuscript §11: "an adapted receiver may recover an implicit relation without
additional message bits", and §5's signal/interpreter distinction ([CLAIM-118](CLAIM-118.md)).
The enlarged state, and the claim that adaptation changes which invariants are
conserved, are not in it. It is the place where [CLAIM-074](CLAIM-074.md) meets [QUESTION-006](../questions.d/QUESTION-006.md), and where
[CLAIM-267](CLAIM-267.md)'s amplifying regime becomes possible.

## Parallels

In iterated learning the learners' own bias, not the source, fixes what a
chain conserves: Bayesian samplers converge to their prior ([THEORY-155](../theory.d/THEORY-155.md)), and
human function learners to a positive linear function whatever trained the
first ([THEORY-489](../theory.d/THEORY-489.md)). Neither varies the learners' adaptation, so they show
that the interpreter's state sets what survives a chain, not that learning
moves it.
