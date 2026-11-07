---
status: Proposed
title: 'The nucleating-argument line is split in three: nucleating-argument keeps how an argument drifts, anchors and pays for anchoring; what a record of inquiry keeps and the record as its own apparatus become lines of their own, because their parts barely relate to the rest'
version: 1
tags:
- record
date: '2026-11-07'
summary: >-
  The nucleating-argument line's first account (ADR-tmpyihxy) fell into
  five parts. Counting the relations among their components showed three
  of them, drift, anchors and the costs of anchoring, linked densely to
  each other. The other two barely linked to anything. "What a record of
  a developing argument keeps" had 25 relations inside it, 8 out and 3
  in. "The record as its own apparatus" had 24 inside, 6 out and 1 in.
  The owner reads a line that wants several unrelated accounts as a
  signal that it holds several inquiries. This decision adds two lines,
  `records-of-inquiry` and `record-as-apparatus`, and moves those two
  parts' 43 entries to them. Each entry keeps its other lines, with a
  history note. nucleating-argument keeps the three linked parts. Each
  line gets its synthesis. Rejected: one account over all five parts;
  keeping one line and tagging parts by a new field; a split into five.
---
<!-- inactive-ok-file: ADR-tmpyihxy ADR-075 ADR-076 ADR-078 — Proposed; the decisions on line accounts, the audit, the scheme and the review this applies -->

# ADR-tmpyb8vm: The nucleating-argument line is split in three: nucleating-argument keeps how an argument drifts, anchors and pays for anchoring; what a record of inquiry keeps and the record as its own apparatus become lines of their own, because their parts barely relate to the rest

## Context

A line in this record is "a named line of the record's own argument, so
that a line can be set aside as a whole and what depends on it can be
found" (the `lines` vocabulary, ADR-032). nucleating-argument was named for
"how an argument developed across stateless sessions settles into stable,
addressable structure, and what a project memory contributes — the record
itself as the case".

Its first account, the unadmitted line account of ADR-tmpyihxy, organized
its 74 in-force entries into five parts:

1. drift;
2. anchors;
3. the costs and price of anchoring;
4. what a record of a developing argument keeps, and what that buys;
5. the record as its own apparatus.

The owner asked whether each part merits a synthesis of its own, with the
line's synthesis built over them. The owner also asked whether a line that
seems to want several syntheses should be read as a signal to split it into
separate inquiries.

`scratch/formal/line_parts.py --sections`, run on that account (version 1
of its synthesis), counted the relations among each part's components:

| part | inside | out | in |
|---|---|---|---|
| drift | 8 | 4 | 20 |
| anchors | 12 | 13 | 10 |
| costs of anchoring | 8 | 7 | 4 |
| what a record keeps | 25 | 8 | 3 |
| the record as apparatus | 24 | 6 | 1 |

The first three exchange most of their relations with one another; the
crossings among them are 10, 4, 3, 3, 3 and 1. The last two are each mostly
closed. Their few outward relations go to drift (six of eight from what a
record keeps) or to each other (three of six from the record as
apparatus), and almost nothing points into them. The content says the same:

- **What a record keeps** rests on demonstrated results about records of
  inquiry in general: CLAIM-294, CLAIM-299, CLAIM-300 and CLAIM-293, the
  last two of which already have formal-apparatus as their primary line.
  These are not about arguments made across sessions.
- **The record as apparatus** is about luria and inquiry as specification:
  CLAIM-469, CLAIM-470, CLAIM-475 and CLAIM-476, with TERM-089 and TERM-095.
  It is about what a record's grammar makes determinate, not about how an
  argument nucleates.

Setting nucleating-argument aside would today take those two inquiries with
it, which is the opposite of what a line is for.

## Decision

- **Two lines are added** to the closed `lines` vocabulary:
  - `records-of-inquiry`, "What a record of inquiry keeps";
  - `record-as-apparatus`, "The record as its own apparatus".

  Each blurb says it was split from nucleating-argument.
- **nucleating-argument keeps** drift, anchors and the costs of anchoring.
  Its blurb now names those, and points to the two new lines.
- **The 43 entries of the two parts move.** In each, `line` changes
  nucleating-argument to the new line. Other lines are kept: CLAIM-293 and
  CLAIM-300 stay primarily formal-apparatus. Each entry gets a history note.
  No status, title or relation changes.
- **Each line gets its synthesis** (ADR-tmpyihxy, version 2):
  - nucleating-argument gets one for each of its three parts, and a line
    synthesis over them;
  - each new line gets one of its own.

  Each was tested for admission in its own right, and is filed as admitted
  or as an unadmitted account accordingly.
- **The split is not retroactive to the argument chains.** A `rests_on`
  that crosses from a claim in one of the new lines into nucleating-argument
  is now a step between lines. The argument chain reports such steps, which
  is what a dependency across lines should look like.

## Alternatives considered

- **One account over all five parts.** That is the first version of
  ADR-tmpyihxy. It would hide that two parts are separate inquiries, and keep
  them tied to a line whose setting aside they should not follow.
- **One line, with parts tagged by a new field.** A part field would add a
  second axis beside `line` doing a line's job. It would also leave "set the
  line aside" retiring all three inquiries together.
- **Split into five.** Drift, anchors and costs are densely linked, and
  QUESTION-037, the line's root question, is theirs in common. Separate lines would make most of
  their relations cross-line and lose the cluster the counts show.

## Consequences

- The current-account view shows three lines where there was one.
  nucleating-argument's synthesis is built over its parts' syntheses.
- `luria lint` reports more `rests_on` steps that cross lines, between
  nucleating-argument and the two new lines. They are real dependencies
  across inquiries, and they are reported, not failures.
- The names and blurbs of the new lines are the assistant's proposal. The owner may rename them before merging. A rename is a vocabulary edit
  plus the same 43 `line` values, and changes no entry's meaning.
