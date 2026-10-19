---
status: Open
title: 'Is delete-and-rederive correct for recursive Datalog views with stratified negation and aggregation, and how large is its overestimate of deletions against the deletions actually needed?'
version: 1
tags:
- databases
- logic
date: '2026-10-19'
line: 'nucleating-argument'
refines:
- QUESTION-105
summary: >-
  Filed when the promotion audit (batch 042, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-387](../theory.d/THEORY-387.md). Theorem 7.1 of Gupta, Mumick and Subrahmanian
  ([LIT-1114](../literature.d/LIT-1114.md)) was re-derived for positive recursive Datalog under set
  semantics. The paper asserts the extension to stratified negation and
  aggregation and leaves its proof to an unseen 1992 report; it measures
  no overestimate. This question holds both.
---

# QUESTION-tmp5fubd: Is delete-and-rederive correct for recursive Datalog views with stratified negation and aggregation, and how large is its overestimate of deletions against the deletions actually needed?

## Why it is a question

[THEORY-387](../theory.d/THEORY-387.md) now states that, for positive recursive Datalog under set
semantics, DRed's three steps (overestimate the deletions, rederive what still
has a derivation from what remains, add what insertions derive) leave exactly
the tuples derivable from the new base, with no derivation counts stored. The
proof given for that case uses monotonicity: deletions can only remove tuples.
Under stratified negation a deletion in a lower stratum can add tuples in a
higher one, and under aggregation a deletion changes a value rather than
removing a tuple, so the same argument does not go through. The paper says
both are handled "in [GMS92]", a technical report the record has not found.
It also gives no bound or measurement of how many tuples the first step
deletes and the second puts back, and calls incremental maintenance "only a
heuristic".

## What would answer it

A proof, read by the record, of DRed's correctness with stratified negation
and aggregation, in the 1992 report or a later published treatment, or a
re-derivation, would answer the first part yes; a stratified program and a
change after which the maintained view differs from the recomputed one would
answer it no. A bound on the overestimate in terms of the change and the
program, or measurements across workloads against the true deletions and
against recomputation, would answer the second part. Worked examples settle
neither.
