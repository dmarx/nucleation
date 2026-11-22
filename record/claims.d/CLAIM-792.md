---
number: 792
status: Proposed
formerly:
- CLAIM-tmpmtv1b
title: 'In this record the noticing of grammar misfits moved from incidental to procedural, from filing agents who met a missing word to review procedures built to look, while revisions of the grammar, as distinct from refinements, were noticed or decided mostly by the owner: what was delegated was noticing, by procedure and by category of change, not judgment about revision'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A recode of the census decisions by a coder outside the assistant family
  that finds the share of grammar changes noticed by review procedures did
  not rise over the record's first eight weeks, or that revisions were
  noticed or decided by assistants acting without the owner's request or
  a procedure the owner set up about as often as refinements were; or a
  longer series in which the pattern reverses. A single assistant-initiated
  revision does not defeat it.
tags:
- design-rationale
- philosophy-of-science
date: '2026-11-20'
line:
- record-as-apparatus
grounds:
- CASE-300
bears_on:
- QUESTION-388
- QUESTION-457
summary: >-
  A finding of the decision census ([CASE-300](../cases.d/CASE-300.md)), filed at the owner's
  direction from the manuscript on the record. It answers no question
  outright. It bears on [QUESTION-388](../questions.d/QUESTION-388.md) (what makes reconfiguration self-
  governed) and [QUESTION-457](../questions.d/QUESTION-457.md) (whether a collective keeping a governed record
  improves its improver). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-120 ADR-124 — Proposed or Open; filed on 2026-11-21 and cited in the refresh of this pull request -->


# CLAIM-792: In this record the noticing of grammar misfits moved from incidental to procedural, from filing agents who met a missing word to review procedures built to look, while revisions of the grammar, as distinct from refinements, were noticed or decided mostly by the owner: what was delegated was noticing, by procedure and by category of change, not judgment about revision

## The claim

The census of the record's decisions ([CASE-300](../cases.d/CASE-300.md)) coded, for each of the 88 that changed the grammar, who noticed the need, who proposed the change, who decided it and how the owner ratified it. Agreement on these fields between two coders on a random 30 was κ 0.82, 0.85, 1.00 and 1.00.

**Who noticed changed over the eight weeks.**

| Period | Changes | Noticed by filing agents | By review procedures | By the owner |
|---|---:|---:|---:|---:|
| 25 Sep–15 Oct | 43 | 16 | 4 | 9 |
| 16 Oct–5 Nov | 20 | 1 | 4 | 10 |
| 6–20 Nov | 25 | 3 | 12 | 7 |

- **Early.** Filing agents, reading a batch of works and finding no word for what they read, noticed most needs.
- **Late.** Review procedures noticed most needs. These are status reviews, synthesis and reading reviews, a line-splitting script and postmortems: procedures the owner asked for and assistants run.

**Who noticed depended on the kind of change.** Filing agents noticed 18 refinements and 2 revisions. The owner noticed 12 and 13, and review procedures 12 and 8. Assistants working unprompted noticed one revision.

**Delegation took three forms:**

- standing permission for a class of refinements, mostly vocabulary words ("The owner authorised extending the vocabulary as the record sees fit", [ADR-034](../decisions.d/ADR-034.md));
- ratification by merging a procedure's output ("merging it is the assent", `record/status-review/README.md`);
- one explicit, case-by-case hand-over of a revision ("The owner left the split to the assistant's judgement", [ADR-089](../decisions.d/ADR-089.md)).

## What it does not say

- **That the owner's share of noticing fell steadily.** It did not: 21%, then 50%, then 28%. An earlier expectation that noticing would move steadily from the owner to assistants was falsified by the same census.
- **That the procedures notice well.** Nothing measures how many misfits they miss.
- **That delegating noticing leaves the owner's capacity to judge revisions intact.** [CLAIM-602](CLAIM-602.md), [CLAIM-605](CLAIM-605.md) and [CLAIM-675](CLAIM-675.md) give reasons to measure it. This claim does not.
- **That it holds beyond one owner and one record.**

## Why it matters

[QUESTION-388](../questions.d/QUESTION-388.md) asks what separates a programmable system from one that governs its own reconfiguration. By this claim, the record's reconfiguration was self-governed at the level of the owner together with the owner's procedures, and not at the level of its assistants. The criteria for revision stayed with the owner.

[CLAIM-673](CLAIM-673.md) says an arrangement that does the work through which a collective governs it can erode the capacity to govern it. That makes the pattern a candidate for the risk [CLAIM-673](CLAIM-673.md) names. It is not shown to be an instance of it.

## Note of 2026-11-21: three more procedures built to look

The night after this claim was drafted added three procedures of the kind it
describes, each built after a misfit was met by hand:

- **[ADR-120](../decisions.d/ADR-120.md)**: reframes, which had no place in an entry, get a section
  of their own; the owner noticed the gap.
- **[ADR-126](../decisions.d/ADR-126.md)** (Active): an owner's earmark for the retrospective
  becomes a note the next retrospective must answer.
- **[ADR-124](../decisions.d/ADR-124.md)**: an adoption review, after 48 decisions were found
  Proposed while applied; its first pass adopted 34.

And one guard moved upstream: luria now refuses a title that cites a code,
after the same misfit caught the filer three times (dmarx/luria#403). Each
is a case of noticing becoming procedural; none was counted by the census.
