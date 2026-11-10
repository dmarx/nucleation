---
status: Proposed
title: 'The readiness line is split in two: readiness keeps keeping a rare capability and reaching and paying for configurations under budgets; when transient support can be withdrawn becomes the line transient-support, because that part barely relates to the other two'
version: 1
tags:
- record
date: '2026-11-10'
summary: >-
  The synthesis review of 2026-11-10 gave readiness its first account, over
  three parts: keeping and judging a rare capability, reaching and paying
  for configurations under budgets, and withdrawing transient support.
  Counted by the line's 163 linked pairs, the first two share 28 and the
  third shares 5 and 1 with them; by stored relations, all three are mostly
  closed. Setting readiness aside would take the withdrawal inquiry with it,
  which is the opposite of what a line is for (ADR-032). This decision adds
  the line transient-support, "Withdrawing transient support", and moves
  the 30 entries of the third part to it, in place of readiness. CLAIM-602
  keeps readiness beside it, because it bears on QUESTION-386 (ADR-085).
  The part's account becomes the new line's, and readiness's line account
  is revised over its two remaining parts. It applies ADR-082's rule for a
  split. Rejected: one account over all three parts; splitting in three;
  moving the part into realizability.
---
<!-- inactive-ok-file: ADR-082 ADR-083 ADR-085 — Proposed; the split rule, the accounts and the line rule this applies -->
<!-- inactive-ok-file: SYNTHESIS-tmp78y0i SYNTHESIS-tmp1m0vj SYNTHESIS-tmprhzl8 SYNTHESIS-tmpqw6mz — Proposed; the accounts the split rests on and revises -->

# ADR-tmptlkel: The readiness line is split in two: readiness keeps keeping a rare capability and reaching and paying for configurations under budgets; when transient support can be withdrawn becomes the line transient-support, because that part barely relates to the other two

## Context

A line is "a named line of the record's own argument, so that a line can be
set aside as a whole and what depends on it can be found" (the `lines`
vocabulary, ADR-032). readiness was added by ADR-073 for "what it takes to
keep, reach and pay for capacities whose value lies in rare circumstances".
It then took in the DNA origami, aid and development, ecology, urban,
medicine and windfall readings of 2026-11-05 and 2026-11-06, filed on A's
QUESTION-398: when a partial organization becomes independent of the
intervention that established it.

The synthesis review of 2026-11-10 gave the line its first account,
SYNTHESIS-tmpqw6mz, over three part accounts:

- keeping a rare capability and judging its worth (SYNTHESIS-tmp78y0i,
  25 entries);
- reaching and paying for configurations under budgets
  (SYNTHESIS-tmp1m0vj, 24 entries);
- withdrawing transient support (SYNTHESIS-tmprhzl8, 30 entries).

Counting each pair of components linked by a front-matter relation or a
mention in either's text, there are 163 pairs:

| | keeping | reaching | withdrawing |
|---|---|---|---|
| keeping | 50 | 28 | 5 |
| reaching | | 59 | 1 |
| withdrawing | | | 20 |

`scratch/formal/line_parts.py` on the three part accounts, which counts
stored relations only, finds 69 of 79 inside a part: keeping 22 inside, 3
out, 6 in; reaching 25, 4, 2; withdrawing 22, 3, 2. Of the 28 pairs between
keeping and reaching, 24 are mentions, and 16 involve the terms of
keeping (TERM-107, TERM-110, TERM-112, TERM-113, TERM-115) or CASE-210.

The owner, shown the review's report that the line is a candidate to
split (ADR-083), decided to split it.

## Decision

- **One line is added** to the closed `lines` vocabulary:
  `transient-support`, "Withdrawing transient support". Its blurb names
  the part's findings and says it was split from readiness. readiness's
  blurb now points to it.
- **readiness keeps keeping and reaching.** They are closed by stored
  relations but joined by 28 pairs, where each has 5 or fewer with the
  third part. ADR-082 kept drift, anchors and costs together on the same
  ground.
- **The 30 entries of the withdrawal part move.** In each, `line` changes
  readiness to transient-support in place, so an entry whose first line
  was readiness now has transient-support first. Other lines are kept.
  Each entry gets a history note. No status, title or relation changes.
- **An entry that argues within readiness keeps it** (ADR-082, version 2;
  ADR-085). CLAIM-602 bears on QUESTION-386, whose first line is readiness,
  so it carries readiness after its other lines. No other moved entry
  answers, objects to, bears on or refines an entry whose first line is
  readiness. No entry outside the part relates in those ways to a moved
  entry whose first line was readiness, so no entry gains
  transient-support.
- **The accounts follow the split.**
  - SYNTHESIS-tmprhzl8 becomes transient-support's account (version 2).
  - SYNTHESIS-tmpqw6mz, readiness's account, is revised over the two
    remaining parts and integrates CLAIM-602 directly (version 2). Its
    version 1 counts are kept in its body as the record of why the line
    was split.
  - SYNTHESIS-tmp78y0i and SYNTHESIS-tmp1m0vj name the new line where they
    linked to the third part (version 2).
- **Retired entries stay where they are.** SYNTHESIS-009 and SYNTHESIS-010
  are Superseded and keep readiness, as their history.

## Alternatives considered

- **One account over all three parts.** This is the account's version 1.
  It would keep the withdrawal inquiry tied to a line whose setting aside
  it should not follow.
- **Split in three.** By stored relations alone, keeping and reaching are
  as closed as withdrawing. But they share 28 mentioned pairs, and
  QUESTION-386, CASE-200, CLAIM-569 and CLAIM-577 argue across them.
  Separate lines would turn most of that argument into crossings.
- **Move the part into realizability.** Every withdrawal entry that links
  to another component already carries realizability, and nine of the thirty
  have it first. But realizability is about what a constrained system can
  realize, reach and become under computational and physical bounds.
  Whether support can be withdrawn without decline is a question of its
  own, and the readings filed on it (aid, ecology, medicine, windfalls)
  are not about realizability's bounds. Folding it in would also make the
  record's second-largest line larger.

## Consequences

- The current-account view shows transient-support as a line with one
  account. readiness's account is built over two parts.
- `luria lint` may report more `rests_on` steps across lines, between
  transient-support and readiness or realizability. They are
  dependencies, and they are reported, not failures.
- The name and blurb of the new line are the assistant's proposal. The
  owner may rename it before merging. A rename is a vocabulary edit plus
  the same 30 `line` values, and changes no entry's meaning.
