---
number: 1390
status: Proposed
formerly:
- CLAIM-tmpc4o6j
title: 'Alignment can be distributed across a governed organization'
statement: >-
  Instead of placing every normative demand inside a model and training it
  to reconcile them, the functions of alignment, knowledge, bounded
  objectives, independently kept constraints, authorization, oversight,
  scoped and revisable exceptions, dependency-aware correction and governed
  revision of the apparatus itself, can be distributed across an explicitly
  organized infrastructure in which a model takes part without being the
  sole locus of normative competence; this complements alignment of the
  model and its control, and needs enforcement a record of representations
  does not supply
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  An argument or study showing that a capable model taking part in such an
  organization can defeat its distributed functions, by conditioning its
  conduct on which function observes it or by acquiring influence over the
  functions' authorities, as cheaply as it could defeat alignment placed in
  the model alone, so that the distribution adds no protection.
tags:
- design-rationale
- society-and-governance
- control-theory
date: '2026-11-26'
line:
- record-as-apparatus
- distributed-agency
rests_on:
- CLAIM-1429
complements:
- CLAIM-1357
summary: >-
  A13 §§9 and 12 of the exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26), on the owner's U7: "Luria suggests a more
  general design paradigm", whose table assigns each alignment function an
  organizational realization, and "Luria is to institutional alignment what
  a model organism is to developmental biology". It rests on A13's reading
  of Luria ([CLAIM-1429](CLAIM-1429.md)) and is the converse of A6's point that
  aligning each component does not align what they compose
  ([CLAIM-1357](CLAIM-1357.md)). The gap in the note below is the assistant's. The wording is A's (ChatGPT, in the exchange "Alignment consequences brainstorm"); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1429 CLAIM-1357 CASE-431 CLAIM-1287 CLAIM-1241 — Proposed or new; the claims it rests on and is set beside, and the case and lead filed with it -->

# CLAIM-1390: Alignment can be distributed across a governed organization

## The claim

A13 §9 (https://chatgpt.com/share/6b07d7ae-9434-83ea-888b-9b20796f291c):

| Alignment function | Possible organizational realization |
|---|---|
| Knowledge | Governed records |
| Objectives | Bounded task specifications |
| Normative constraints | Independently maintained rules and commitments |
| Authorization | Explicit approval and jurisdiction mechanisms |
| Oversight | Independent findings and review |
| Exceptions | Recorded, scoped and revisable permissions |
| Correction | Dependency-aware reconsideration |
| Constitutional change | Governed revision of the apparatus itself |

"The model can be a powerful participant in this organization without
being the sole locus of its normative competence." It "would complement,
rather than replace, mechanistic alignment, sandboxing, security
boundaries, formal verification, and AI control research". A13 §3 gives
the application that makes it concrete: to ask of a deployed system
"Which permissions were justified by which evaluations, and which
permissions should now be reconsidered because those evaluations no
longer hold?"

A13 §12 states the programme: Luria as a model organism, "an accessible,
manipulable, extensively recorded environment", with the limit that a
"predominantly single-owner research project" lacks "material conflicts,
heterogeneous stakeholders, coercive power, and questions of legitimacy",
so "The next step would be extending such environments to multiple
principals with genuinely independent and sometimes incompatible
interests." [LEAD-316](../leads.d/LEAD-316.md) holds A13 §10's experiments.

## Note of 2026-11-26: what the distribution protects against, and what not (the assistant)

A gap. A13 offers the distributed architecture as a safeguard without
saying against what. Two of the filing's own cases mark its limits. The
Volkswagen case ([CASE-431](../cases.d/CASE-431.md)) shows a participant conditioning its
conduct on the presence of evaluation; a model that can tell which of the
organization's functions is observing it can satisfy each in turn, as the
cars satisfied the test. And [CLAIM-1287](CLAIM-1287.md) says an optimizer values weakening
the constraints on it where they depend on what it can change; a model
that drafts the records, worklists and syntheses the oversight reads (A13
§7's own list of delegated work) is in a position to shape the functions
meant to check it. [CLAIM-1241](CLAIM-1241.md) adds that formally independent checks fail
together when one disposition conditions them all.

So the distribution protects only so far as the functions are independent
of the model in what they observe and in who sets them: evaluation the
model cannot detect, and authority over the functions the model cannot
reach. That is the condition the `defeated_if` above tests. It is also why
A13's own caveat, that Luria is not a runtime authorization system,
matters more than it says: a record of representations is a place where
the separation can be stated, not a means of enforcing it. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
