---
status: Proposed
title: 'Blackwell''s order on rendering procedures grounds the thesis that what survives translation is what a receiver can reconstruct'
version: 1
form: formal-application
tags:
- information-theory
- philosophy-of-language
date: '2026-10-28'
line: pragmatic-transport
rests_on:
- CLAIM-050
concludes:
- CLAIM-115
summary: >-
  [CLAIM-115](../claims.d/CLAIM-115.md) rests on [CLAIM-050](../claims.d/CLAIM-050.md), so the manuscript's thesis about what a
  receiver can reconstruct takes Blackwell's order as its formal ground.
  That order describes a decision-maker free to use any rule, and the
  thesis and its tests are about bounded receivers. Since [CLAIM-199](../claims.d/CLAIM-199.md) and
  [CLAIM-050](../claims.d/CLAIM-050.md)'s version 4 the order is the ceiling on what a rendering makes
  possible, so the inference is narrowed, not defeated. [CLAIM-225](../claims.d/CLAIM-225.md)
  undercuts it.
---
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-087 CLAIM-199 — Proposed; the conclusion, the improvement claim and the reconciliation, cited as open -->

# ARG-tmpa4q9l: Blackwell's order on rendering procedures grounds the thesis that what survives translation is what a receiver can reconstruct

## The inference

[CLAIM-050](../claims.d/CLAIM-050.md) applies Blackwell's order to rendering procedures: a rendering
is at least as informative as another if every risk attainable with the
second is attainable with the first, over a designed distribution of
situations. [CLAIM-115](../claims.d/CLAIM-115.md) makes survival relative to what "a receiving system
can still reconstruct and act upon", and rests on [CLAIM-050](../claims.d/CLAIM-050.md). So the order
is offered as the formal measure of what survives.

## Critical questions

- **Does the mapping premise hold?** In part. A rendering is an
  experiment about the situation, and a generator that sees only the text
  makes its image a garbling of the text. That mapping is exact, and
  [CLAIM-225](../claims.d/CLAIM-225.md) derives it.
- **Are the model's assumptions met in the new domain?** Not as the thesis
  uses them, and this is the question that fails. Blackwell's order
  quantifies over every decision rule. [CLAIM-115](../claims.d/CLAIM-115.md)'s defeat condition is
  stated on "Human judgements of communicative fidelity", which are a
  bounded receiver's, and [TERM-034](../terms.d/TERM-034.md) defines fidelity "relative to an
  interpreter". [CLAIM-225](../claims.d/CLAIM-225.md): "the line uses that standard for its formal
  ground, and a receiver's standard for its thesis and its tests." A
  garbling that real receivers do better with, on even one task, "shows
  that their standard is not Blackwell's order for that task", and
  [CLAIM-087](../claims.d/CLAIM-087.md) predicts such a garbling.

## Verdict

Proposed. [CLAIM-225](../claims.d/CLAIM-225.md) was conceded on 2026-10-10 and reconciled by [CLAIM-199](../claims.d/CLAIM-199.md):
Blackwell's order bounds what a rendering makes possible for any receiver,
and a given receiver's access is usable information, which a garbling can
raise for that receiver but not above that bound. [CLAIM-050](../claims.d/CLAIM-050.md)'s version 4
says "ceiling" in its title. Xu et al. ([LIT-1309](../literature.d/LIT-1309.md), [THEORY-846](../theory.d/THEORY-846.md)) give the two
standards as Shannon and V-information. On that reading the order is a
bound on the thesis's quantity, not its measure, and the inference holds
only as far as a bound carries. What would settle it is a
receiver-restricted order with its own results, or an argument that
judged access tracks ideal informativeness ([CLAIM-225](../claims.d/CLAIM-225.md), "What would answer
it").

[CLAIM-225](../claims.d/CLAIM-225.md) undercuts this argument. Its own text says "It does not say
[CLAIM-050](../claims.d/CLAIM-050.md) is false", and its objection to [CLAIM-050](../claims.d/CLAIM-050.md) stays, for the
defeat-condition point.

Filed 2026-10-28 by the [ADR-061](../decisions.d/ADR-061.md) migration, from [CLAIM-225](../claims.d/CLAIM-225.md).
