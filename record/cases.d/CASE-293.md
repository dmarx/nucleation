---
number: 293
status: Proposed
formerly:
- CASE-tmpw9202
title: 'A proposed study of postmortems: code each for the highest organizational level named among its contributing causes and for whether any action item targets a decision above the reviewing team''s authority, and compare reviews commissioned inside the organization with independent investigations, to test whether a blameless trace stops at the authority of the body that commissions it'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note added: an objection to the study's unit, filed for
    LEAD-189 from the SRE workbook chapter. No change of status or
    title.
standing: stipulated
kind: proposed-study
tags:
- society-and-governance
- software-engineering
date: '2026-11-18'
line:
- rightful-power
illustrates:
- CLAIM-750
bears_on:
- QUESTION-476
draws_on:
- THEORY-2000
summary: >-
  The lead filer's (Claude, in this session), proposed on 2026-11-18 with
  [CLAIM-750](../claims.d/CLAIM-750.md), whose prediction it would test, and accepted for filing
  by the owner ("all of the above please"). Code a corpus of postmortems
  for two things: the highest organizational level any contributing cause
  names, and whether any action item targets a decision above the
  reviewing team's authority. Compare internal blameless reviews with
  independent investigations such as the NTSB's. Its units, contributing
  causes and action items, are the postmortem format the SRE chapter
  describes. Not run. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-750 — new; the claim the study would test and the reading whose format it uses -->
<!-- inactive-ok-file: CASE-292 CLAIM-719 — Proposed; the entries the study bears on, cited with their standing -->

# CASE-293: A proposed study of postmortems: code each for the highest organizational level named among its contributing causes and for whether any action item targets a decision above the reviewing team's authority, and compare reviews commissioned inside the organization with independent investigations, to test whether a blameless trace stops at the authority of the body that commissions it

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

**The test** ([CLAIM-750](../claims.d/CLAIM-750.md)). The claim predicts that in internal reviews
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

## Note of 2026-11-22: piloted
<!-- inactive-ok-file: CASE-335 — new; the pilot and its finding, filed for LEAD-119 on 2026-11-22 -->

A pilot of this design is [CASE-335](CASE-335.md) ([LEAD-119](../leads.d/LEAD-119.md)): 30 public postmortems against 10 CSB reports, with the codes of this entry's "Coding" made ordinal in a codebook committed before coding. Of this entry's design problems, it answers none. Selection by publication is untouched. Authority was coded from the text alone. Follow-up is not measured. It adds a fourth problem: the internal and independent corpora differ in domain and severity, so a full run needs reviews of the same incidents, or of one domain. One coder, the assistant (Claude, Opus 5.5), of the same model family that wrote the claim tested and the codebook, coding with the prediction known: the pilot is not independent. The arms differ in domain and severity (software outages against chemical accidents) as well as in who reviews.

No status changes.

## Note of 2026-11-22: an objection to the study's unit
<!-- inactive-ok-file: CLAIM-1062 CASE-418 — new or Proposed; filed by the lead run on 2026-11-22, and the claim the study would test -->

[CLAIM-1062](../claims.d/CLAIM-1062.md), filed from Google's SRE workbook ([THEORY-2294](../theory.d/THEORY-2294.md)), objects that a single postmortem is the wrong unit for [CLAIM-750](../claims.d/CLAIM-750.md)'s prediction: the workbook routes questions about priorities set above the team to reviews of repeated incidents and to a process review with "organizational leaders". A design that codes postmortems one by one would miss upstream provenance kept there. A variant that samples cross-incident reviews, or follows a postmortem's named but unactioned conditions (as in [CASE-418](CASE-418.md)) into later reviews, would meet it. No status changes.
