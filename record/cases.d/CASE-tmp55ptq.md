---
status: Proposed
title: 'A learner that has found f(x) = x² but computes it with a noisy multiplier, so its values on large inputs are often wrong while it adapts to x² + c from two examples: understanding without reliably correct output'
version: 1
standing: fictional
kind: construction
tags:
- epistemology
- learning-theory
- cognition
date: '2026-11-23'
line:
- learned-structure
variant_of:
- CASE-tmpkttf2
bears_on:
- QUESTION-493
- QUESTION-360
draws_on:
- THEORY-438
summary: >-
  The seventh of the set LEAD-001 asks for, the converse of
  CASE-tmpkttf2: understanding without reliably correct output, and so
  without knowledge of particular values. It alters CASE-tmpkttf2's rule
  learner in one respect: its multiplication errs with a probability that
  grows with the size of the operands. The construction is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-438 CLAIM-754 — Proposed; cited as the criteria applied, not relied on -->
<!-- inactive-ok-file: CASE-tmpkttf2 CLAIM-tmpf4pun CLAIM-tmpadjsm CLAIM-tmpngm72 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-tmp55ptq: A learner that has found f(x) = x² but computes it with a noisy multiplier, so its values on large inputs are often wrong while it adapts to x² + c from two examples: understanding without reliably correct output

## The case

Learner R′ holds the same program as CASE-tmpkttf2's R, x ↦ x · x, but
executes multiplication with an unreliable unit: each digit-level step
errs with a small probability, so a product of two k-digit numbers is
wrong with probability that grows with k. On 2, 3 and 4 it is right; on
37 it is right about 70% of the time; on 4,219 about 10%. Its errors are
independent of which input is asked, given its size: they are noise in
execution, not a wrong rule.

When the target shifts to x² + c, R′ is shown two pairs and sets c
correctly (two, not one, since one observation may be miscomputed). After
that its errors are those it had before, offset by c.

## What it separates

- **Understanding without reliably correct output.** R′ holds the
  structure: it generalizes to every input, and a changed target costs it
  one constant. Its outputs on large inputs are mostly wrong.
- **Understanding without knowledge of the particular value.** Over the
  family "what is 4,219²?", R′ is right one time in ten, so it does not
  know that value on A73's reliability criterion, while it understands the
  function whose value it is.

## Against the candidate answers

On QUESTION-493's candidate (A73), understanding is developmental value,
and R′ has it: it adapts to x² + c as cheaply as R, which is CLAIM-754's
developmental frontier. On THEORY-438's test, stable tracking under
structure-preserving change of input, R′ also counts: its error rate
depends on operand size, not on the structure, so what it tracks is
invariant under the changes that preserve x². So both readings of
understanding filed as alternatives, CLAIM-tmpf4pun and CLAIM-tmpadjsm,
agree that R′ understands. The case shows that understanding does not
entail knowledge of the values it bears on, which A73's ladder (a
retained answer below a reusable procedure below relational understanding)
could be read to imply.

## What it can show

That understanding and reliably correct output come apart in both
directions once this case is set beside CASE-tmpkttf2. Being a
construction, nothing about which real systems are like R′. One of the
separations CLAIM-tmpngm72 collects.
