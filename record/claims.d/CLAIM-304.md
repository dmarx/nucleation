---
number: 304
status: Active
formerly:
- CLAIM-tmpzk2fj
title: 'A rendering can keep a distinction recoverable in principle and make it
  infeasible to recover: if pseudorandom generators exist, a uniformly random bit
  can be encoded so that an unbounded receiver recovers it except with probability
  at most 2⁻⁽ⁿ⁺¹⁾, while no efficient receiver does non-negligibly better than chance'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    bears_on gains QUESTION-111, a relation the synthesis review of
    2026-11-11 found missing, on its text: "QUESTION-111 asks where the
    line falls for communicative distinctions", and QUESTION-111's
    "CLAIM-304 shows the gap exists". The line is unchanged under
    ADR-085: the target's line is already this entry's. No other change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the reduction from a receiver with advantage to a distinguisher, or
  the non-existence of secure pseudorandom generators.
tags:
- information-theory
- pragmatics
- mathematics
date: '2026-10-15'
line:
- formal-apparatus
- pragmatic-transport
rests_on:
- CLAIM-302
grounds:
- CASE-083
- THEORY-352
complements:
- CLAIM-199
summary: >-
  A14's first failure mode, computational inaccessibility, and A18's fourth candidate:
  "Recoverable in principle ≠ recoverable within budget." [CLAIM-199](CLAIM-199.md)
  shows a garbling can help a bounded receiver. This is the other direction: a nearly
  lossless rendering can defeat every efficient one. The construction is the record's,
  from [CLAIM-302](CLAIM-302.md)'s witness; A18 asked for one and warned
  against "a vague appeal to an inverse being hard".
bears_on:
- QUESTION-111
---
<!-- inactive-ok-file: CLAIM-117 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-304: A rendering can keep a distinction recoverable in principle and make it infeasible to recover: if pseudorandom generators exist, a uniformly random bit can be encoded so that an unbounded receiver recovers it except with probability at most 2⁻⁽ⁿ⁺¹⁾, while no efficient receiver does non-negligibly better than chance

## The claim

A14 §1: "A distinction may survive a transformation in principle while
becoming too computationally expensive for the receiver to recover." A18:
"A suitable formal construction must specify both the transformation and
the restricted decoder family."

Construction, from [CASE-083](../cases.d/CASE-083.md). Render a bit b as a sample from G(Uₙ) if
b = 1 and from U₂ₙ if b = 0. An unbounded receiver guesses 1 exactly
when the sample is in G's image. It is never wrong when b = 1, and wrong
when b = 0 with probability at most 2ⁿ/2²ⁿ = 2⁻ⁿ, so with b uniform its
overall error is at most 2⁻⁽ⁿ⁺¹⁾. The rendering preserves b almost exactly. Any efficient receiver that guessed b with
non-negligible advantage would be a test distinguishing G(Uₙ) from U₂ₙ,
which a secure generator rules out: a receiver right with probability
½ + ε is a distinguisher with gap 2ε (Goldreich's Definition 3.2; the
guarantee is asymptotic, for the ensemble indexed by n). The construction
is the record's; the book supplies its ingredients, not it ([CLAIM-302](CLAIM-302.md)).

## What it bears on

- [CLAIM-199](CLAIM-199.md). Its receivers are restricted by a rule class: the
  one-coordinate receiver gains from an XOR it cannot compute. Here they
  are restricted by a budget, and the rendering loses for all of them.
  A15 §4: "fidelity isn't generally monotonic in either representation
  size or computational effort."
- [CLAIM-117](CLAIM-117.md) asks whether translation preserves the dynamics of
  interpretation. A14: even if the dynamics correspond mathematically, a
  bounded receiver may not be able to recover or enact the
  correspondence.
- [QUESTION-111](../questions.d/QUESTION-111.md) asks where the line falls for communicative distinctions. This
  shows only that it can fall anywhere.

## What it does not say

That ordinary renderings do this. Nothing communicative is a
pseudorandom generator. The construction shows the gap between keeping a
distinction and making it available is not an artefact of a chosen rule
class.
