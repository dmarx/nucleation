---
status: Active
title: 'A rendering can keep a distinction recoverable in principle and make it
  infeasible to recover: if pseudorandom generators exist, a bit can be encoded
  so that its encoding determines it with error at most 2⁻ⁿ while no efficient receiver
  does better than chance'
version: 1
role: thesis
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
answers:
- QUESTION-tmpviyn9
rests_on:
- CLAIM-tmpvdl53
grounds:
- CASE-tmp51hxx
complements:
- CLAIM-199
summary: >-
  A14's first failure mode, computational inaccessibility, and A18's fourth candidate:
  "Recoverable in principle ≠ recoverable within budget." [CLAIM-199](CLAIM-199.md) shows a garbling
  can help a bounded receiver. This is the other direction: a nearly lossless rendering
  can defeat every efficient one. The construction is the record's, from [CLAIM-tmpvdl53](CLAIM-tmpvdl53.md)'s
  witness; A18 asked for one and warned against "a vague appeal to an inverse being
  hard".
---
<!-- inactive-ok-file: CLAIM-117 CLAIM-199 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-tmpzk2fj: A rendering can keep a distinction recoverable in principle and make it infeasible to recover: if pseudorandom generators exist, a bit can be encoded so that its encoding determines it with error at most 2⁻ⁿ while no efficient receiver does better than chance

## The claim

A14 §1: "A distinction may survive a transformation in principle while
becoming too computationally expensive for the receiver to recover." A18:
"A suitable formal construction must specify both the transformation and
the restricted decoder family."

Construction, from [CASE-tmp51hxx](../cases.d/CASE-tmp51hxx.md). Render a bit b as a sample from G(Uₙ) if
b = 1 and from U₂ₙ if b = 0. An unbounded receiver guesses 1 exactly
when the sample is in G's image. It is never wrong when b = 1, and wrong
when b = 0 with probability at most 2ⁿ/2²ⁿ = 2⁻ⁿ. So the rendering
preserves b almost exactly. Any efficient receiver that guessed b with
non-negligible advantage would be a test distinguishing G(Uₙ) from U₂ₙ,
which a secure generator rules out ([CLAIM-tmpvdl53](CLAIM-tmpvdl53.md)).

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
- [QUESTION-tmpviyn9](../questions.d/QUESTION-tmpviyn9.md) asks where the line falls for communicative distinctions. This
  shows only that it can fall anywhere.

## What it does not say

That ordinary renderings do this. Nothing communicative is a
pseudorandom generator. The construction shows the gap between keeping a
distinction and making it available is not an artefact of a chosen rule
class.
