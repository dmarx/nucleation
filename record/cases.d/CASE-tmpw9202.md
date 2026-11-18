---
status: Proposed
title: 'A proposed study of postmortems: code each for the highest organizational level named among its contributing causes and for whether any action item targets a decision above the reviewing team''s authority, and compare reviews commissioned inside the organization with independent investigations, to test whether a blameless trace stops at the authority of the body that commissions it'
version: 1
standing: stipulated
kind: proposed-study
tags:
- society-and-governance
- software-engineering
date: '2026-11-18'
line:
- rightful-power
illustrates:
- CLAIM-tmp5g7xc
bears_on:
- QUESTION-476
draws_on:
- THEORY-tmpuc245
summary: >-
  The lead filer's (Claude, in this session), proposed on 2026-11-18 with
  [CLAIM-tmp5g7xc](../claims.d/CLAIM-tmp5g7xc.md), whose prediction it would test, and accepted for filing
  by the owner ("all of the above please"). Code a corpus of postmortems
  for two things: the highest organizational level any contributing cause
  names, and whether any action item targets a decision above the
  reviewing team's authority. Compare internal blameless reviews with
  independent investigations such as the NTSB's. Its units, contributing
  causes and action items, are the postmortem format the SRE chapter
  describes. Not run. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp5g7xc — new; the claim the study would test and the reading whose format it uses -->
<!-- inactive-ok-file: CASE-292 CLAIM-719 — Proposed; the entries the study bears on, cited with their standing -->

# CASE-tmpw9202: A proposed study of postmortems: code each for the highest organizational level named among its contributing causes and for whether any action item targets a decision above the reviewing team's authority, and compare reviews commissioned inside the organization with independent investigations, to test whether a blameless trace stops at the authority of the body that commissions it

## The study

**Corpus.** Postmortems that organizations have published from their own
blameless reviews, and, as the comparison arm, reports of independent
investigators of the NTSB's kind ([CASE-292](CASE-292.md)). Where an organization has
given access, its internal postmortems of the same incidents.

**Coding, per postmortem.**

1. **Highest level named.** For each contributing cause, the highest
   organizational level whose decision it names: the operator; the
   reviewing team; the team's management; the organization's leadership
   (budgets, staffing, deadlines, priorities); outside regulators or
   customers. A cause stated as "the system", "the process" or "a gap"
   with no decision named is coded as such, not at a level.
2. **Action items above the team.** Whether any action item targets a
   decision outside the reviewing team's authority, and who owns it.
3. **Commissioning body.** Who commissioned and reviewed the postmortem,
   and the highest level of its authority.

**The test** ([CLAIM-tmp5g7xc](../claims.d/CLAIM-tmp5g7xc.md)). The claim predicts that in internal reviews
the highest level named rarely exceeds the commissioning body's authority,
that action items cluster at or below the reviewing team's, and that "the
system" without a named decision is common; and that independent
investigations name and target higher levels more often. Internal
reviews that reach above the team as often as independent ones would
defeat it.

## Design problems it must answer

- **Selection.** Published postmortems are chosen and edited for a public
  audience, which may strip internal organizational causes. The comparison
  needs internal versions, or a reason to think publication does not
  change the level named.
- **Authority.** Whether a decision lay above the reviewing team is often
  not stated in the postmortem itself and has to be coded from
  organization charts or interviews.
- **Follow-up.** An action item above the team that is written but never
  carried out counts for the claim. Completion is the same measure as in
  [CLAIM-719](../claims.d/CLAIM-719.md)'s note of 2026-11-18 and needs data postmortems rarely
  publish.

## What it would show

Where blameless tracing stops, by the commissioning body's authority. It
would not show that blame-based reviews go further, which needs a third
arm of reviews that assign blame.
