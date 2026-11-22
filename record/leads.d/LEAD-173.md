---
number: 173
status: Open
formerly:
- LEAD-tmpuylfq
title: 'For each closure condition, in a linear Gaussian VAR, construct a case that meets the other four and fails it, or prove that the other four entail it'
version: 1
stage: idea
priority: high
method:
- formal
tags:
- complex-systems
- mathematics
date: '2026-11-19'
line:
- formal-apparatus
advances:
- QUESTION-252
summary: >-
  The question names this as its answer's form, and A84 names it as the
  next advance without an experiment; [LEAD-003](LEAD-003.md) covers only the empirical
  half. Named in [QUESTION-252](../questions.d/QUESTION-252.md). Filed by the backlog audit of 2026-11-19.
---

# LEAD-173: For each closure condition, in a linear Gaussian VAR, construct a case that meets the other four and fails it, or prove that the other four entail it

## What it would do

Declare target, projection, metric, horizon and budget, then work the five
conditions pairwise.

Where the record names it:

- [QUESTION-252](../questions.d/QUESTION-252.md): "for each condition, a construction meeting the other four
  and failing it, or a proof that the other four entail it."

## What would count

The full table of independences and entailments answers [QUESTION-252](../questions.d/QUESTION-252.md) for
the class.

## Note of 2026-11-22: carried out for VAR(1) and VAR(2)
<!-- inactive-ok-file: CASE-tmpo5jhq CLAIM-tmp186gy CLAIM-tmp9xo66 — new; the study and claims filed from this lead -->

Done on the branch claude/lead-173-five-conditions (scratch/studies/lead-173/).
The regime was declared as CASE-tmpo5jhq states: an external linear target
one step ahead, Mori's projection onto span(Y_t), relative excess error of
the memoryless reduced model against the optimal predictor over h = 2,
ε = 0 (and 0.01), and a budget of dim Y ≤ 2. Under it exactly three
entailments hold, D ⇒ M (VAR(1) only), P ∧ D ∧ M ⇒ A and, at ε = 0,
A ⇒ P, and every other configuration has a witness (CLAIM-tmp186gy).
Leaving one out: D and C can fail alone; M only from VAR(2); P only at
ε > 0; A never. With the target taken as Y's own future, P and A collapse
into D ∧ M (CLAIM-tmp9xo66); which declaration QUESTION-252 means is the
owner's call.

What remains: approximate versions with tolerances on P, D and M as well;
classes beyond VAR(2) (state-space with observation noise, nonlinear);
and A5's restricted-access form of the question. The stage and status are
the owner's to change.
