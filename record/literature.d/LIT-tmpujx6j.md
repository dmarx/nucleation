---
status: Active
status_note: >-
  read 2026-11-22 (NOTE-tmpf58r7) in full from Google's own open edition of
  the book at sre.google, licensed CC BY-NC-ND 4.0; worth reading here as
  Google's later, practical statement of blameless postmortem culture,
  with a real postmortem shown whole and a section on how leaders and
  incentives keep the culture up, which bears on whether a blameless trace
  reaches decisions above the reviewing team (QUESTION-476, CLAIM-750).
title: 'Postmortem Culture: Learning from Failure (workbook)'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read on 2026-11-22 for LEAD-189. Checked on 2026-11-22:
    not held in record/literature.d by title, chapter authors (Rogers,
    Suriar, Lueder), book title or URL. Chapter 10 of The Site Reliability
    Workbook: Practical Ways to Implement SRE (O'Reilly, 2018), by Daniel
    Rogers, Murali Suriar, Sue Lueder, Pranjal Deo and Divya Sudhakar,
    with Gary O'Connor and Dave Rensin (byline on the page). The chapter's
    own title is the same as the SRE book's chapter 15 (LIT-2784); this
    entry's title adds "(workbook)" to keep the two apart. No DOI; OpenAlex
    gives the workbook's chapters as 2018 with no day, so `published:` is
    the first of January 2018 (ADR-002). The web edition carries
    "Copyright © 2018 Google, Inc. Published by O'Reilly Media, Inc.
    Licensed under CC BY-NC-ND 4.0". Read from
    https://sre.google/workbook/postmortem-culture/ (HTML converted to
    text). No email address was sent to any service.
tags:
- software-engineering
- society-and-governance
date: '2026-11-22'
published: '2018-01-01'
url: 'https://sre.google/workbook/postmortem-culture/'
first_author: 'Rogers'
keywords:
- 'postmortem'
- 'blameless postmortem'
- 'postmortem culture'
- 'action items'
- 'organizational incentives'
implementations: []
summary: >-
  Daniel Rogers, Murali Suriar, Sue Lueder, Pranjal Deo and Divya Sudhakar
  (2018), "Postmortem Culture: Learning from Failure", chapter 10 of The
  Site Reliability Workbook, read in NOTE-tmpf58r7. It sets a "bad"
  postmortem of a real Google outage beside the "good" one actually
  written, and says how leaders keep the culture blameless. Blamelessness
  means the root cause "Focuses on "what" went wrong, not "who" caused the
  incident" and action items "Are aimed at improving the system instead of
  improving people". The good postmortem lists a staffing limit among what
  went poorly ("The installer" has limited staffing") and none of its
  fourteen action items addresses it; a question put to a manager about
  training is rewritten as a process suggestion; a vice-president's
  blameful question is redirected to a generic one. It bears on
  QUESTION-476 and CLAIM-750 (THEORY-tmpm653d, CASE-tmptkkgm).
---
<!-- inactive-ok-file: NOTE-tmpf58r7 THEORY-tmpm653d CASE-tmptkkgm — new; the reading, its theory and the specimen taken from it -->
<!-- inactive-ok-file: CLAIM-750 — Proposed; the claim the reading bears on -->

# LIT-tmpujx6j: Postmortem Culture: Learning from Failure (workbook)

Daniel Rogers, Murali Suriar, Sue Lueder, Pranjal Deo and Divya Sudhakar, with Gary O'Connor and Dave Rensin (2018). "Postmortem Culture: Learning from Failure". Chapter 10 in *The Site Reliability Workbook: Practical Ways to Implement SRE*. O'Reilly. https://sre.google/workbook/postmortem-culture/

## Key takeaways

*From the reading (NOTE-tmpf58r7).*

- A real Google postmortem (satellite machines sent to diskerase, 2014)
  shown twice: a "bad" version that blames named engineers, and the
  "good" one actually written, which blames "No individual or team".
- The good postmortem names a staffing limit among what went poorly;
  all its fourteen action items are technical, each with an engineer as
  owner.
- Leaders are to "consistently exemplify blameless behavior"; blameful
  questions to managers and from a vice-president are redirected into
  questions about process.
- Repeated incidents are to prompt "Is feature velocity trumping
  reliability fixes?", a question about a priority set above the team.

## Standing in the record

Registered for LEAD-189, which named "Google's SRE workbook chapter on
postmortems". It shows one real blameless postmortem whole, which the
SRE book's chapter (LIT-2784) does not.
