---
number: 14
status: Open
formerly:
- LEAD-tmp0523n
title: 'Run the curation-completeness study: an agent given a source and the record as it stood produces the filing''s accounting, scored against the filing and its later corrections'
version: 1
stage: specified
priority: high
method:
- empirical
tags:
- epistemology
- design-rationale
- model-comparison
date: '2026-11-19'
line:
- records-of-inquiry
advances:
- QUESTION-108
- CLAIM-266
operationalized_in:
- CASE-251
summary: >-
  Owner-accepted; the record's own history supplies the ground truth.
  Named in [QUESTION-108](../questions.d/QUESTION-108.md) and [CASE-251](../cases.d/CASE-251.md). Filed by the backlog audit of
  2026-11-19.
---
<!-- inactive-ok-file: CASE-318 CLAIM-881 — new; the curation-completeness pilot and the claim filed from it, cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: CASE-251 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-014: Run the curation-completeness study: an agent given a source and the record as it stood produces the filing's accounting, scored against the filing and its later corrections

## What it would do

Replay past filings: give an agent the source and the record as it stood,
collect its accounting, and score it against what was filed and what later
corrections added.

Where the record names it:

- [QUESTION-108](../questions.d/QUESTION-108.md): "a study of curation completeness scored on the record's
  own corrected filings, which bears on the third mechanism"
- [CASE-251](../cases.d/CASE-251.md): "The record's own history supplies ground truth for it"

## What would count

Accountings that miss what later corrections caught measure the third
mechanism of [QUESTION-108](../questions.d/QUESTION-108.md); near-complete accountings say curation is not
where the record loses information.

## Note of 2026-11-22: a pilot run, and what remains

A pilot was run ([CASE-318](../cases.d/CASE-318.md); materials under scratch/studies/lead-014/).
Four corrected readings of arXiv works were chosen by a rule written
before outcomes, a codebook was fixed before any replay, and each filing
was replayed from its source and a checkout of the record at its parent
commit, then scored. Pooled recall against what the filings held was
95/138 (0.69); against what later corrections added, 0/6. Five of the six
correction items needed works other than the source, so for single-work
readings the corrections measure accuracy, not curation
([CLAIM-881](../claims.d/CLAIM-881.md)). The replays also found items neither the filings nor
the corrections hold.

What remains: the study as specified. It needs (1) separate replay agents
that see only their worktree and source, which the worker that ran the
pilot could not spawn; (2) a scorer who is not the replayer, ideally not of
the same model family; (3) the episodes of omission [CASE-251](../cases.d/CASE-251.md) names, which
are exchanges, and so the exchange texts saved in the repository first;
(4) [CASE-251](../cases.d/CASE-251.md)'s three arms. The lead's status and stage are unchanged.
