---
number: 214
status: Open
formerly:
- LEAD-tmpxq8z2
title: 'Judge retention and drift with raters as the criterion: readers outside the project, blind to the hypothesis, score content units of the originating turn in each version against a rubric fixed in advance, with a second rater'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, triaging the manuscript's leads at
    the owner's "triage leads relevant to the manuscript that you could
    feasibly handle on your own and get started". One of two alternative
    protocols for the judgement LEAD-201 and LEAD-204 leave open; the other
    is LEAD-213. Which to adopt is ARG-028's open dispute and the owner's call.
stage: specified
priority: medium
method:
- empirical
- operationalization
tags:
- design-rationale
- epistemology
date: '2026-11-22'
line:
- nucleating-argument
- record-as-apparatus
advances:
- CLAIM-768
- CLAIM-778
- CLAIM-772
- CLAIM-191
- CLAIM-776
summary: >-
  Alternative (a) of two for the judgement [LEAD-201](LEAD-201.md) (retention of the
  owner's originating turn) and [LEAD-204](LEAD-204.md) (drift of ideas restated before
  coding) leave open: it takes [CLAIM-217](../claims.d/CLAIM-217.md)'s side of [ARG-028](../arguments.d/ARG-028.md), that raters are
  the criterion. People outside the project, blind to the hypothesis and to
  which version is which, list the content units of each originating turn
  and score each unit in each version as kept, altered or absent, on a
  rubric written and frozen before any data are seen; a second rater codes
  every item, and agreement is reported unit by unit. It needs the owner to
  recruit the raters, which is why the assistant cannot run it alone. The
  other alternative is [LEAD-213](LEAD-213.md). The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-028 CLAIM-206 CLAIM-217 — Proposed, Rejected, Deferred or new; the entries this filing made or touched -->

# LEAD-214: Judge retention and drift with raters as the criterion: readers outside the project, blind to the hypothesis, score content units of the originating turn in each version against a rubric fixed in advance, with a second rater

**One of two alternatives.** [LEAD-201](LEAD-201.md) and [LEAD-204](LEAD-204.md) stop at the same place: who judges, and on what scale, against a reference the record did not supply. [ARG-028](../arguments.d/ARG-028.md) leaves that open between [CLAIM-217](../claims.d/CLAIM-217.md) (raters are the criterion) and [CLAIM-206](../claims.d/CLAIM-206.md) (human judgements are one probe family among others). This lead takes the first side; [LEAD-213](LEAD-213.md) takes the second. The owner chooses; filing both lets either be run as soon as it is chosen.

## Design

**Material.** For [LEAD-201](LEAD-201.md): every claim filed in the owner's voice or from an owner's turn, with the turn (quoted in the claim, or recovered from the curation entry's exchange), the claim's first version and its current version from git history. For [LEAD-204](LEAD-204.md): each idea restated across sessions before it was coded (first statement, each restatement, session dates), drawn from [CLAIM-177](../claims.d/CLAIM-177.md)'s instances and [CASE-183](../cases.d/CASE-183.md)'s exchanges.

**Raters.** Two people outside the project, not shown the record's TERMs, conventions or hypotheses ([CLAIM-208](../claims.d/CLAIM-208.md)'s demand). They see only the turn and one version at a time, in random order, with no marker of which is first or current.

**Units and rubric, frozen first.** Rater 1 splits each originating turn into content units (one assertion, distinction or question each) before seeing any version. For each unit and each version both raters score: kept (the same content, any wording), altered (present but changed in scope, strength or object), absent. Separately, on a 3-point scale anchored by examples chosen outside the record, how far the version reads as the field's conventional framing rather than the turn's own. The rubric and anchors are written and committed before any scoring.

**Agreement.** Cohen's κ per field, and a confusion table; a disagreement is adjudicated by discussion and both codes kept.

**Reading.** Crossed with [LEAD-199](LEAD-199.md)'s revision count as [LEAD-201](LEAD-201.md)'s table sets out (settled and kept: conserved; settled and not kept: contracted). For [LEAD-204](LEAD-204.md), displacement is the share of units altered or absent at each restatement, plotted against restatement number.

## What it needs

The owner to recruit two raters, and about ten minutes per claim per rater. Nothing else is outside the assistant's reach: the assistant can assemble the material and the rater packets.

## What would count against it

A κ below 0.4 on kept/altered/absent: then the units are not reliably identifiable and the measure cannot carry [LEAD-201](LEAD-201.md).
