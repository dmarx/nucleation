---
number: 215
status: Open
formerly:
- QUESTION-tmpxmcgr
title: "Does Landauer's bound hold without assuming reversible microdynamics, and does any logically reversible operation have a positive entropy floor?"
version: 1
tags:
- thermodynamics
- information-theory
date: '2026-10-20'
line: 'formal-apparatus'
summary: >-
  The open part of the promotion condition formerly on [THEORY-030](../theory.d/THEORY-030.md). [THEORY-030](../theory.d/THEORY-030.md)
  was narrowed and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) on a derivation that
  assumes the memory and its environment evolve reversibly together and
  start uncorrelated. Whether the bound survives without that assumption
  (the Earman–Norton charge that it is circular), what Landauer 1961 itself
  states, and whether any logically reversible step has a positive floor
  are open.
---
<!-- inactive-ok-file: LIT-328 — Unavailable; named as the reading that would add the original statement -->

# QUESTION-215: Does Landauer's bound hold without assuming reversible microdynamics, and does any logically reversible operation have a positive entropy floor?

## Why it is a question

[THEORY-030](../theory.d/THEORY-030.md) now holds a derivation: if a memory and everything it can dump
entropy into evolve reversibly, starting uncorrelated, then a step that
loses H(X | f(X)) of logical distinguishability must raise the
environment's entropy by at least that much, k ln 2 per bit, and a step
that is injective on the logical states has no floor. That is a theorem
about the stated dynamics. Bennett presents the principle as a restatement
of the Second Law, concedes the Earman–Norton dilemma "with some justice",
and Norton calls the literature "too fragile" ([LIT-114](../literature.d/LIT-114.md) §7.2). The
derivation assumes the very reversibility that dilemma questions. Until
2026-10-20 this was [THEORY-030](../theory.d/THEORY-030.md)'s promote_when.

## What would answer it

- A derivation of the same bound from weaker assumptions, or a reading of
  Earman and Norton that shows the reversible-dynamics derivation circular.
- A demonstrated positive lower bound on the entropy cost of a logically
  reversible operation, or an erasure of unknown data done with less than
  k ln 2 of entropy export per bit; either would refute the account.
- A close reading of Landauer 1961 ([LIT-328](../literature.d/LIT-328.md)), which would add the original
  statement but not settle the question.
