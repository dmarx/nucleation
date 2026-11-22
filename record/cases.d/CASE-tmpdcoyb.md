---
status: Proposed
title: 'The record''s history from 2026-10-07 to 2026-11-22, counted at matched age, shows claims with inbound rests_on or grounds edges taking substantive revisions about 1.45 times as often as claims with none, and the fall in revision rate over an entry''s life tracking its age, not its edges'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from the study that carries out
    LEAD-199 (CASE-tmpdcoyb), run at the owner's "triage leads relevant to
    the manuscript that you could feasibly handle on your own and get
    started". The count was run by a delegated analyst; its scripts, data and hand-checks are committed under scratch/studies/lead-199/.
standing: documented
kind: executed-study
tags:
- design-rationale
- epistemology
date: '2026-11-22'
line:
- nucleating-argument
- record-as-apparatus
summary: >-
  LEAD-199's count, as it specified. Population: the 859 claim files on
  staging, followed through renames and formerly: fields, over the
  record's whole history (2026-10-07 to 2026-11-22, about 46 days). A
  revision is substantive if it changes the title, role, warrant,
  defeated_if or the body outside dated notes, after normalising away link
  markup, directives, cited codes and citation-only parentheses; schema
  backfills and bot commits are excluded. Exposure: the replayed count of
  other entries naming the claim in rests_on or grounds. Result, at matched
  age (Mantel-Haenszel by age bin): claims with any inbound edge are revised
  1.47 times as often as claims with none (95% interval 1.22 to 1.77; 1.45
  stratified by age and calendar week; 1.62 by risk-set matching over seven
  days), and title and status changes rise too. The raw fall from before to
  after the first edge (ratio 0.58) is the filing-day burst: it vanishes
  when each claim's first day is dropped (1.04). The 6+ group has 4 to 7
  events and an interval including 1. Classifier precision by hand-check:
  about 0.7 by intent, 0.9 by the letter. 148 of the 303 revisions after a
  first edge fall within a day of it, so edges and revisions come in the
  same working sessions.
---
<!-- inactive-ok-file: CASE-tmpdcoyb CLAIM-778 — Proposed, Rejected, Deferred or new; the entries this filing made or touched -->

# CASE-tmpdcoyb: The record's history from 2026-10-07 to 2026-11-22, counted at matched age, shows claims with inbound rests_on or grounds edges taking substantive revisions about 1.45 times as often as claims with none, and the fall in revision rate over an entry's life tracking its age, not its edges

## What was counted

LEAD-199 as specified, with the choices it left open stated (scratch/studies/lead-199/README.md lists the scripts):

- **Population.** 859 claims with a creation commit on staging; 347 have ever had an inbound edge, 138 from the commit that filed them. 810 edges were added and 79 removed; 730 are live.
- **Substantive revision.** A change to title, role, warrant, defeated_if or the body outside `## Note of …` sections, after normalisation (link markup, inactive-ok directives, the H1, whitespace and cited codes masked; parentheses holding only citations dropped). A field going from absent to present (the warrant backfill of 289 claims) is a schema backfill, not a revision. Commits by the CI bot, and repair, regenerate, promote and concretization commits, are excluded. Status changes are counted separately.
- **Exposure.** The inbound count replayed over time from every entry's frontmatter; a tie goes to "after", which works against the claim.
- **Age control.** Mantel-Haenszel rate ratios stratified by age bin (0–1, 1–3, 3–7, 7–14, 14–28, 28+ days), and by age × calendar week; and risk-set matching: each claim at the age it gets its first edge against claims filed within seven days that still have none, both followed for seven days. Intervals by cluster bootstrap over claims.

## Results (rates per 30 days at risk)

| Comparison | Substantive | Title | Status |
|---|---|---|---|
| MH by age, any inbound vs none | 1.47 [1.22, 1.77] | 1.41 [1.01, 1.89] | 1.33 [1.08, 1.63] |
| MH by age, 1–2 inbound | 1.44 [1.18, 1.74] | 1.22 [0.87, 1.68] | 1.27 [0.99, 1.60] |
| MH by age, 3–5 inbound | 1.68 [1.18, 2.31] | 2.24 [1.25, 3.47] | 1.52 [1.04, 2.08] |
| MH by age, 6+ inbound (4–7 events) | 1.34 [0.52, 2.39] | 2.52 [0.71, 4.57] | 2.04 [0.76, 3.54] |
| Risk-set matched, seven days | 1.62 [1.33, 1.94] | 1.55 [1.05, 2.13] | 1.47 [1.16, 1.78] |

Within claims, the substantive rate falls from 1.89 before the first edge to 1.10 after (ratio 0.58 [0.42, 0.81]), but dropping each claim's first day makes it 0.61 to 0.64 (1.04 [0.72, 1.62]): the fall is the filing-day burst, not the edge. Within each age bin the rates with edges are equal to or above those without; the decline across the life cycle is with age. Sensitivities on the any-inbound MH ratio: a lenient definition (a whole added section does not count) 1.46 [1.20, 1.76]; first day dropped 1.49 [1.23, 1.83]; commits touching more than 20 claims dropped 1.40 [1.13, 1.73]; both 1.39 [1.12, 1.79].

## Validity

- **Young record.** About 46 days; no claim is older than about six and a half weeks.
- **Classifier.** Two hand-checks of 20 changes each. The final classifier was 10 of 10 correct on non-substantive changes; of 10 substantive ones, 7 were clearly substantive, 2 were vocabulary sweeps (ADR-070's "endorsement" to "conferral"), which are substantive by the letter but are convention rewrites, and 1 was borderline. Precision about 0.7 by intent, 0.9 by the letter. False positives would have to concentrate on cited claims to explain the result, and the lenient and title-only variants run the same way.
- **Scrutiny.** 148 of the 303 revisions after a first edge fall within a day of it: edges and revisions are made in the same sessions and reviews, so an edge marks attention as well as constraint. This is the confound CLAIM-778's admission named.
- **Dating.** Author dates of branch commits; content changed only in merge resolutions is missed.
