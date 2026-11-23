---
status: Proposed
title: 'A learner that memorized f(2) = 4, f(3) = 9 and f(4) = 16 and one that found f(x) = x²: the same answers on the table and the same knowledge of its values, parted when the target shifts to x² + c'
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
bears_on:
- QUESTION-493
- QUESTION-360
draws_on:
- THEORY-438
summary: >-
  The sixth of the set LEAD-001 asks for, separating knowledge from
  understanding. It files as a case the example QUESTION-493's candidate
  (A73 §7) gives and QUESTION-360's note records: two learners agree on
  every tabulated value, and on a shift of target to x² + c the rule
  learner adapts from one example while the table learner must relearn
  every entry. The construction is A73's; its filing as a case, and the
  verdicts, are the assistant's (Claude, in this session); adopting them
  is the owner's call.
---
<!-- inactive-ok-file: CLAIM-519 CLAIM-754 TERM-079 THEORY-438 — Proposed; cited as the criteria applied, not relied on -->
<!-- inactive-ok-file: CASE-tmp55ptq CASE-tmphawe9 CLAIM-tmpf4pun CLAIM-tmpadjsm CLAIM-tmpngm72 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-tmpkttf2: A learner that memorized f(2) = 4, f(3) = 9 and f(4) = 16 and one that found f(x) = x²: the same answers on the table and the same knowledge of its values, parted when the target shifts to x² + c

## The case

Two learners are trained on the pairs (2, 4), (3, 9), (4, 16) and queried
only on 2, 3 and 4.

- **T** stores the three pairs and answers by lookup. On any other input
  it returns a default.
- **R** holds the rule x ↦ x² with one parameter-free program, and answers
  by computing it.

On the declared family {2, 3, 4} both are right every time. Then the
target becomes f(x) = x² + c for an unknown c, and each learner is shown
one new pair, (2, 4 + c).

- R updates one constant and is right on every input.
- T updates one entry and is right on 2 only; it needs every pair again.

Its facts are its definition: nothing here is measured.

## What it separates

- **Knowledge without understanding.** On A73's criteria both learners
  know each tabulated value: true, reliable over the family, and grounded
  in observations of f. Only R has what makes the next target cheap, and
  only R gets inputs outside the table right. So knowledge of the values
  is shared and understanding of f is not.
- **Present outputs do not separate them.** Over the declared family, no
  test of outputs can, which is CLAIM-519's result for world models
  (a lookup policy reproduces any agent's interaction distribution over a
  fixed interface and horizon). Only change separates them: new inputs,
  or a changed target.

## Against the candidate answers

A73 calls understanding "developmental value": the two "agree now and
part when the target becomes x² + c". The case agrees, and it is
CLAIM-754's developmental frontier (what a learner can come to do within
a further acquisition budget) moved by what was learned. It also meets
THEORY-438's test, stable tracking under structure-preserving change of
input: R tracks x² on new inputs and T does not. The two readings of
understanding agree here. They part on CASE-tmphawe9, a rule with no
capacity to learn, where the alternatives CLAIM-tmpf4pun and
CLAIM-tmpadjsm give different verdicts. CASE-tmp55ptq is R with noisy
arithmetic. Whether T believes its values in TERM-079's sense is thin:
a pure lookup draws no further inferences, so its belief is degenerate
rather than absent.

## What it can show

That knowledge and understanding come apart in a learner, and that only
a change of input or target shows it. Being a construction, nothing about
which real systems are table-like. One of the separations CLAIM-tmpngm72
collects.
