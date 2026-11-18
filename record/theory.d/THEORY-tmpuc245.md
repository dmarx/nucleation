---
status: Proposed
promote_when: >-
  A reading of the chapter, or of Google's later SRE workbook on the same
  practice, confirms that a blameless postmortem is to identify the
  contributing causes of an incident and its follow-up actions without
  indicting any individual or team, and that the reason given is that
  blame keeps people from bringing issues to light. Whether the practice
  achieves this is not asserted.
title: 'Lunney and Lueder state Google''s blameless postmortem as a review that records an incident''s contributing causes and the follow-up actions to prevent recurrence without indicting any individual or team, on the ground that blame keeps people from bringing issues to light, so that correction is aimed at systems and processes rather than at people'
version: 1
tags:
- software-engineering
- society-and-governance
date: '2026-11-18'
source:
- LIT-tmpo6c2h
bears_on:
- QUESTION-476
corroborates:
- CLAIM-742
summary: >-
  Lunney and Lueder (2016), LIT-tmpo6c2h, read in NOTE-tmpu2cx9. The
  practice the owner's QUESTION-476 asks about, in its practitioners'
  words: correction kept, blame withheld, on the ground of disclosure. It
  corroborates CLAIM-742 as a documented practice that keeps correction
  without blame; it is not evidence that the practice works, and it says
  nothing about decisions above the reviewing team. The wording is the
  filer's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpu2cx9 — new; the reading -->
<!-- inactive-ok-file: CLAIM-742 — Proposed; the claim this corroborates -->

# THEORY-tmpuc245: Lunney and Lueder state Google's blameless postmortem as a review that records an incident's contributing causes and the follow-up actions to prevent recurrence without indicting any individual or team, on the ground that blame keeps people from bringing issues to light, so that correction is aimed at systems and processes rather than at people

Lunney and Lueder (2016), LIT-tmpo6c2h, read in NOTE-tmpu2cx9.

## The account

A postmortem records "the root cause(s), and the follow-up actions to
prevent the incident from recurring". To be blameless "it must focus on
identifying the contributing causes of the incident without indicting any
individual or team for bad or inappropriate behavior", because under blame
"people will not bring issues to light for fear of punishment". "You can't
"fix" people, but you can fix systems and processes".

## Bearing

- **CLAIM-742**: corroborates. A practice in which the grounds of
  correction are explicitly separated from blame exists, is codified, and
  is defended on its own ground.
- **QUESTION-476**: bears on. It is the practice the question asks about.
  It answers the first half (it keeps correction and gives up blame, by
  design) and leaves the second (does the trace reach decisions above the
  reviewers?) open.

## What it does not show

- That postmortems find or fix more than blame-based reviews would; the
  chapter's "Google weathers fewer outages" comes without figures.
- Anything about the level at which contributing causes are found, or
  whether action items are completed.
