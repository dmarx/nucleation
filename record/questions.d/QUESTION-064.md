---
number: 64
status: Open
formerly:
- QUESTION-tmppy48f
title: 'Does an anchor need endorsement as well as addressability, stable identity and discoverability: are entries the record has not accepted built on less than entries it has?'
version: 1
tags:
- design-rationale
- epistemology
date: '2026-10-12'
line: 'nucleating-argument'
refines:
- QUESTION-038
summary: >-
  [QUESTION-038](QUESTION-038.md) lists three candidates for what turns a persistent
  structure into an anchor. Clark and Chalmers' criteria for an external
  resource that counts as part of a mind ([LIT-097](../literature.d/LIT-097.md), read in [NOTE-180](../notes.d/NOTE-180.md))
  include endorsement, which [QUESTION-038](QUESTION-038.md) lacks. The record has its own
  form of endorsement, Proposed against Active, so the question can be
  tested on the record's citation graph.
---

# QUESTION-064: Does an anchor need endorsement as well as addressability, stable identity and discoverability: are entries the record has not accepted built on less than entries it has?

## Why it is a question

[QUESTION-038](QUESTION-038.md) asks what turns a structure that persists into one later
structure can be built on, and names three candidates: addressability,
stable identity and discoverability. Clark and Chalmers' Otto, whose
notebook stands in for his memory, is the closest case the record holds of
an external resource doing a mind's remembering. [NOTE-180](../notes.d/NOTE-180.md) records the
features that make that work: "constancy, direct availability, automatic
endorsement, and the admittedly 'arguable' past conscious endorsement".
The first two have counterparts in [QUESTION-038](QUESTION-038.md)'s list. Endorsement does
not.

The record has an endorsement condition of its own. A claim is Proposed or
Active, a reading is Read or Skimmed, a LIT is Deferred or Active, and the
owner's acceptance moves entries between them. If endorsement matters to
anchoring, Proposed and Deferred entries should be built on less than
Active ones, other things equal.

What would count as an answer:

- **Yes:** entries that are not yet accepted draw fewer `rests_on` and
  `grounds` edges than accepted ones of the same age and line, beyond
  what the record's `inactive-ok` discipline explains.
- **No:** they are built on as readily, so addressability without
  endorsement is enough.

[NOTE-180](../notes.d/NOTE-180.md) records that the criteria were read off one case, and that the
fourth is flagged "arguable". The active-memory objection, which Clark answers
by conceding that the notebook is static ([NOTE-363](../notes.d/NOTE-363.md)), cuts the other way here: for a collaborator
who keeps no memory, static storage is the virtue ([CLAIM-180](../claims.d/CLAIM-180.md)).
