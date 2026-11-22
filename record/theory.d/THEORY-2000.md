---
number: 2000
status: Proposed
formerly:
- THEORY-tmpuc245
promote_when: >-
  A reading of the chapter, or of Google's later SRE workbook on the same
  practice, confirms that a blameless postmortem is to identify the
  contributing causes of an incident and its follow-up actions without
  indicting any individual or team, and that the reason given is that
  blame keeps people from bringing issues to light. Whether the practice
  achieves this is not asserted.
title: 'Lunney and Lueder state Google''s blameless postmortem as a review that records an incident''s contributing causes and the follow-up actions to prevent recurrence without indicting any individual or team, on the ground that blame keeps people from bringing issues to light, so that correction is aimed at systems and processes rather than at people'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note added: the SRE workbook chapter, read for LEAD-189,
    meets the promote_when; promotion left to the owner. No change of
    status or title.
tags:
- software-engineering
- society-and-governance
date: '2026-11-18'
source:
- LIT-2784
bears_on:
- QUESTION-476
corroborates:
- CLAIM-742
summary: >-
  Lunney and Lueder (2016), [LIT-2784](../literature.d/LIT-2784.md), read in [NOTE-2082](../notes.d/NOTE-2082.md). The
  practice the owner's [QUESTION-476](../questions.d/QUESTION-476.md) asks about, in its practitioners'
  words: correction kept, blame withheld, on the ground of disclosure. It
  corroborates [CLAIM-742](../claims.d/CLAIM-742.md) as a documented practice that keeps correction
  without blame; it is not evidence that the practice works, and it says
  nothing about decisions above the reviewing team. The wording is the
  filer's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-742 — Proposed; the claim this corroborates -->

# THEORY-2000: Lunney and Lueder state Google's blameless postmortem as a review that records an incident's contributing causes and the follow-up actions to prevent recurrence without indicting any individual or team, on the ground that blame keeps people from bringing issues to light, so that correction is aimed at systems and processes rather than at people

Lunney and Lueder (2016), [LIT-2784](../literature.d/LIT-2784.md), read in [NOTE-2082](../notes.d/NOTE-2082.md).

## The account

A postmortem records "the root cause(s), and the follow-up actions to
prevent the incident from recurring". To be blameless "it must focus on
identifying the contributing causes of the incident without indicting any
individual or team for bad or inappropriate behavior", because under blame
"people will not bring issues to light for fear of punishment". "You can't
"fix" people, but you can fix systems and processes".

## Bearing

- **[CLAIM-742](../claims.d/CLAIM-742.md)**: corroborates. A practice in which the grounds of
  correction are explicitly separated from blame exists, is codified, and
  is defended on its own ground.
- **[QUESTION-476](../questions.d/QUESTION-476.md)**: bears on. It is the practice the question asks about.
  It answers the first half (it keeps correction and gives up blame, by
  design) and leaves the second (does the trace reach decisions above the
  reviewers?) open.

## What it does not show

- That postmortems find or fix more than blame-based reviews would; the
  chapter's "Google weathers fewer outages" comes without figures.
- Anything about the level at which contributing causes are found, or
  whether action items are completed.

## Note of 2026-11-22: the SRE workbook read; this theory's promote_when is met
<!-- inactive-ok-file: THEORY-tmpm653d — new; the reading filed by the lead run on 2026-11-22 -->

The `promote_when` asks for "A reading of the chapter, or of Google's later SRE workbook on the same practice" confirming that a blameless postmortem identifies contributing causes and follow-up actions "without indicting any individual or team", and that the reason given is that blame keeps people from bringing issues to light. The workbook's chapter 10, read in full on 2026-11-22 (THEORY-tmpm653d, NOTE-tmpf58r7), confirms both: in the good postmortem "No individual or team is blamed for the incident", and naming individuals makes people "afraid of being publicly shamed. They may be motivated to cover up facts critical to understanding and preventing recurrence." The reading is of another book by other authors (Sue Lueder is an author of both), and independent of the reading that filed this theory. Promotion is left to the owner; no status change.
