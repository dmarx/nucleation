---
number: 1062
status: Proposed
formerly:
- CLAIM-tmpauu5r
title: 'Single postmortems can''t show where blame stops'
statement: >-
  A single postmortem's causes and action items are the wrong unit for
  testing where a blameless practice's trace stops: Google's practice routes
  questions about priorities set above the team to reviews of repeated
  incidents, to a cross-functional review with organizational leaders and to
  a vice-president's review, so an organization could keep upstream
  provenance across incidents while each postmortem stops at the team
version: 1
role: counter
warrant: interpretive
tags:
- software-engineering
- society-and-governance
- ethics
date: '2026-11-22'
line:
- rightful-power
- organizational-normativity
bears_on:
- QUESTION-476
objects_to:
- CLAIM-750
grounds:
- THEORY-2294
summary: >-
  The assistant's (Claude, in this session), filed for [LEAD-189](../leads.d/LEAD-189.md) on
  2026-11-22 as an objection to [CLAIM-750](CLAIM-750.md), from the reading of Google's
  SRE workbook chapter on postmortem culture ([THEORY-2294](../theory.d/THEORY-2294.md)). The
  workbook keeps the single postmortem at the level of systems and the
  teams' action items, and puts questions about priorities set above the
  team ("Is feature velocity trumping reliability fixes?") in reviews
  across incidents and of the process. If upstream provenance is kept
  there, a coding of postmortems one at a time, as [CASE-293](../cases.d/CASE-293.md) proposes and
  [CASE-335](../cases.d/CASE-335.md) did, would find the trace stopping at the team when the
  practice as a whole does not. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-418 — new; the reading the objection draws on and the specimen beside it -->
<!-- inactive-ok-file: CLAIM-750 CASE-293 CASE-335 CLAIM-905 — Proposed; the claim objected to and the studies whose unit it questions -->

# CLAIM-1062: Single postmortems can't show where blame stops

## The objection

[CLAIM-750](CLAIM-750.md) predicts that in postmortems commissioned inside the
organization, contributing causes and action items stop at or below the
commissioning body's authority. Its proposed study ([CASE-293](../cases.d/CASE-293.md)) and the
pilot ([CASE-335](../cases.d/CASE-335.md), [CLAIM-905](CLAIM-905.md)) code postmortems one by one.

Google's workbook ([THEORY-2294](../theory.d/THEORY-2294.md), [NOTE-2391](../notes.d/NOTE-2391.md)) describes a practice
in which the single postmortem is not where upstream questions are meant
to be asked:

- **Repeated incidents.** "Is feature velocity trumping reliability
  fixes?"; "Is the faulty service overdue for a refactor?"; "If you
  uncovered a systemic process or technical problem, it's time to take a
  step back and consider the overall service health."
- **A review of the process.** "A cross-functional group of developers,
  SREs, and organizational leaders reviews the overall postmortem
  process."
- **An executive's review.** Every postmortem after a user-affecting
  outage "must have at least one P[01] bug"; "I personally review
  exceptions" (Ben Treynor Sloss, VP).
- **Analytics.** Postmortems are stored and analysed "to write reports
  about their postmortem trends and identify their most vulnerable
  systems".

If those channels reach the decisions that set staffing, priorities and
deadlines, the practice keeps upstream provenance across incidents while
each postmortem stops at the team. Then a per-postmortem coding would
confirm [CLAIM-750](CLAIM-750.md)'s prediction about documents and miss the practice.

## What it concedes

- That the single postmortem stops at the team: the workbook's own good
  postmortem does ([CASE-418](../cases.d/CASE-418.md)), and the pilot found the same.
- That the workbook gives no evidence that these channels reach above the
  teams. It describes them; it does not say what they found.

## What would settle it

Evidence of what cross-incident reviews produce: whether reviews of
repeated incidents, or the process review, issue findings or actions
addressed to the decisions above the teams. If they do, [CLAIM-750](CLAIM-750.md)'s
conditional answer to [QUESTION-476](../questions.d/QUESTION-476.md) needs restating for the practice
rather than the document. If they do not, or are not recorded, the
objection fails and [CLAIM-750](CLAIM-750.md)'s unit stands.

## Where it sits

- An objection to [CLAIM-750](CLAIM-750.md)'s operationalization, not to its mechanism,
  which the same reading corroborates.
- It applies to [CLAIM-905](CLAIM-905.md) and [CASE-335](../cases.d/CASE-335.md) as well, which code single
  postmortems; it does not touch their CSB arm, whose reports are each a
  whole investigation.

## Note of 2026-11-23: what holds it back

The result its own 'What would settle it' names is missing: evidence of what
Google's reviews of repeated incidents and its cross-functional process
review produce, that is, whether any finding or action reaches decisions
above the teams. [THEORY-2294](../theory.d/THEORY-2294.md), promoted at this review, says only that
these channels exist.
