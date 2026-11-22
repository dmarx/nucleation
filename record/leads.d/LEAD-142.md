---
number: 142
status: Open
formerly:
- LEAD-tmpphu1p
title: 'Specify the decision signature and prove or refute the eigenspace candidate for the directed case'
version: 1
stage: idea
priority: medium
method:
- formal
tags:
- mathematical-statistics
- representation-learning
- philosophy-of-science
date: '2026-11-19'
line:
- pragmatic-transport
- formal-apparatus
advances:
- CLAIM-209
- QUESTION-052
summary: >-
  Named in [CLAIM-209](../claims.d/CLAIM-209.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-209 — Proposed; cited in the backlog audit of 2026-11-19 -->
<!-- inactive-ok-file: CASE-tmp5w2ty CLAIM-tmpc54vj CLAIM-tmpm4oom — Proposed; the study and findings of 2026-11-22, cited in the note of that date -->

# LEAD-142: Specify the decision signature and prove or refute the eigenspace candidate for the directed case

## What it would do

State the signature, then attempt the proof.

Where the record names it:

- [CLAIM-209](../claims.d/CLAIM-209.md): "No signature, family of decisions or class of
  transformations is stated."

## What would count

A proof answers [QUESTION-052](../questions.d/QUESTION-052.md) for the directed case.

## Note of 2026-11-22: carried out

The directed signature was stated and the proof attempted, with a numpy
study ([CASE-tmp5w2ty](../cases.d/CASE-tmp5w2ty.md)) and two findings
([CLAIM-tmpc54vj](../claims.d/CLAIM-tmpc54vj.md), [CLAIM-tmpm4oom](../claims.d/CLAIM-tmpm4oom.md)).

- **Signature stated and partly proved.** For input-decisions the directed
  candidate — the top-d left singular span of the conditional-expectation
  operator — equals the top-d eigenspace of the self-adjoint, reversible
  two-step operator T T*, so the directed input-decision case is a symmetric
  one, settled for linear probes by [THEORY-239](../theory.d/THEORY-239.md) ([CLAIM-tmpc54vj](../claims.d/CLAIM-tmpc54vj.md)).
- **Obstruction found.** Beyond linear probes no single span is the
  signature (nonlinear readouts, span-relative sufficiency,
  direction-dependent decisions), so [QUESTION-052](../questions.d/QUESTION-052.md)'s open residue is the
  nonlinear input case (= the symmetric case) and transport-direction
  decisions ([CLAIM-tmpm4oom](../claims.d/CLAIM-tmpm4oom.md)).

What remains: the nonlinear input-decision case (shared with the symmetric
line), a signature for transport-direction decisions, and the held-out
empirical test across realizations, media or languages that [CLAIM-209](../claims.d/CLAIM-209.md)'s
second defeat disjunct needs. The lead's status and stage are left for the
owner.
