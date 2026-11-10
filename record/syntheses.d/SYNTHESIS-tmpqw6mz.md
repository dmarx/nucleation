---
status: Proposed
title: 'The readiness line is three accounts, of keeping a rare capability and judging its worth, of reaching and paying for configurations under budgets, and of when transient support can be withdrawn, which meet at disuse and at budget and funding rules that remove capacities no one chose to give up; the first two are joined by many mentions and few relations, the third barely relates to either, and no link between the parts that no part states passes the claim test'
version: 1
defeated_if: >-
  A part account or component misstated or misattributed here; an
  in-force component of the readiness line that no part account
  integrates; or a link between the parts stated here that no part
  account and no component states.
tags:
- operations-research
- society-and-governance
- complex-systems
date: '2026-11-10'
line:
- readiness
integrates:
- SYNTHESIS-tmp78y0i
- SYNTHESIS-tmp1m0vj
- SYNTHESIS-tmprhzl8
bears_on:
- QUESTION-386
- QUESTION-395
- QUESTION-398
summary: >-
  The account of the readiness line, over the accounts of its three
  parts: keeping and judging a rare capability (SYNTHESIS-tmp78y0i), reaching and
  paying for configurations (SYNTHESIS-tmp1m0vj) and withdrawing transient support
  (SYNTHESIS-tmprhzl8). The first two meet at budget rules and slack (CASE-200,
  CLAIM-577, QUESTION-386) and at what a reserve costs (CLAIM-569); the
  first and third at disuse (CLAIM-558) and at rebuilding (CLAIM-632 with
  CLAIM-605). Counted by relations alone, all three parts are mostly
  closed; counted with mentions, the support part still is, and the line
  is reported as a candidate to split. The account adds nothing of its
  own; its standing is its components'.
---
<!-- inactive-ok-file: CASE-200 CASE-210 CASE-225 CLAIM-603 CLAIM-632 TERM-107 TERM-110 TERM-112 TERM-113 — Proposed; components cited with their standing -->
<!-- inactive-ok-file: ARG-053 — Rejected; a component of SYNTHESIS-tmp78y0i, the inference that part rejects -->
<!-- inactive-ok-file: SYNTHESIS-009 SYNTHESIS-010 — Superseded; the readiness line's former syntheses, returned to CLAIM-632 and CLAIM-600 -->

# SYNTHESIS-tmpqw6mz: The readiness line is three accounts, of keeping a rare capability and judging its worth, of reaching and paying for configurations under budgets, and of when transient support can be withdrawn, which meet at disuse and at budget and funding rules that remove capacities no one chose to give up; the first two are joined by many mentions and few relations, the third barely relates to either, and no link between the parts that no part states passes the claim test

*The account of the readiness line ("Readiness and slack", ADR-073), over
the accounts of its three parts (ADR-083). It integrates every entry whose
`line` includes readiness on 2026-11-10, 79 entries, through the parts.
SYNTHESIS-009 and SYNTHESIS-010 also carry the line; both are Superseded
by the claims they returned to (CLAIM-632 and CLAIM-600, ADR-084), which
the parts integrate, and they are not integrated again.*

## The parts

- **Keeping and judging (SYNTHESIS-tmp78y0i), 25 entries.** Readiness is a
  probability of response to an imposed contingency (TERM-115), so use
  and cancellation counts do not show waste (CASE-210, CLAIM-561,
  ARG-053 Rejected); a capacity's value depends on the others it works
  with (CLAIM-587); records per capacity bound readiness and do not
  identify it (CLAIM-632, Proposed); and a capability kept for rare
  events decays without practice outside operation (CLAIM-558).
- **Reaching and paying (SYNTHESIS-tmp1m0vj), 24 entries.** A transition has a
  threshold of its own (CLAIM-571); feasible, reachable and reliably
  reached come apart (CLAIM-567); obstructions have distinct remedies
  (CLAIM-568, CLAIM-556); a form costs separately to build, keep and move
  (CLAIM-569); several resources give a frontier (CLAIM-585); and a
  spend-matching budget loses transitions without a sign in output
  (CLAIM-577).
- **Withdrawing support (SYNTHESIS-tmprhzl8), 30 entries.** Supplied upkeep never
  becomes optional (CLAIM-597); supply that does the work lowers kept
  capacity (CLAIM-602) and can cross a deadline (CLAIM-605); and the
  conditions for safe withdrawal are stated jointly in CLAIM-600. Eighteen
  of its thirty entries are replication questions moved from readings,
  with no link to any component.

## Where they meet

Every link here is stated by a component; the part accounts give each
with its words.

- **Budget rules, slack and the funding loop (SYNTHESIS-tmp78y0i with SYNTHESIS-tmp1m0vj).**
  QUESTION-386 (A's, Open) asks when allocating by observed activity loses
  a rare capability. CASE-200 (Proposed) is "one mechanism for
  QUESTION-386", on a reconfiguration reserve, with CLAIM-558's decay the
  competence version; CLAIM-577 (Active) is the pure case, and
  QUESTION-394's note names A's simulator as its test. TERM-106 refines
  TERM-107: a reconfiguration reserve is slack measured against output.
- **What a reserve costs (SYNTHESIS-tmp78y0i with SYNTHESIS-tmp1m0vj).** CLAIM-569 (Active)
  bears on QUESTION-395 and QUESTION-386, and CLAIM-632 cites it for the
  construction cost a waste verdict must not overlook. CLAIM-572
  complements CLAIM-561: provisional dispatch is its hedge at o = 0.
- **Disuse and rebuilding (SYNTHESIS-tmp78y0i with SYNTHESIS-tmprhzl8).** CLAIM-558 complements
  CLAIM-602 and corroborates CLAIM-600; CLAIM-602 bears on QUESTION-386;
  CLAIM-632 cites CLAIM-605 for a reserve that may be impossible to
  rebuild below a threshold. CLAIM-597's body says a capacity kept by
  standing supply is "easy to read as waste while it is working".
- **Resource types (SYNTHESIS-tmp1m0vj with SYNTHESIS-tmprhzl8).** CLAIM-601 uses TERM-105.

## Whether the line falls into parts

It does, and the parts barely relate. Counting each pair of the 79
components linked by a front-matter relation or a mention in either's
body or summary, there are 163 pairs:

| | SYNTHESIS-tmp78y0i | SYNTHESIS-tmp1m0vj | SYNTHESIS-tmprhzl8 |
|---|---|---|---|
| SYNTHESIS-tmp78y0i | 50 | 28 | 5 |
| SYNTHESIS-tmp1m0vj | | 59 | 1 |
| SYNTHESIS-tmprhzl8 | | | 20 |

Of the 28 pairs across SYNTHESIS-tmp78y0i and SYNTHESIS-tmp1m0vj, 4 are front-matter relations
and 24 are mentions; 16 of the 28 involve a term of SYNTHESIS-tmp78y0i (TERM-107,
TERM-110, TERM-112, TERM-113, TERM-115) or CASE-210. Counted as
`scratch/formal/line_parts.py` counts, by stored relations only and
directed, 69 of 79 relations fall within a part: SYNTHESIS-tmp78y0i 22 inside, 3 out,
6 in; SYNTHESIS-tmp1m0vj 25 inside, 4 out, 2 in; SYNTHESIS-tmprhzl8 22 inside, 3 out, 2 in.
Twenty-one components link to no component at all: eighteen replication
questions in SYNTHESIS-tmprhzl8 and QUESTION-434, QUESTION-435 and QUESTION-444 in
SYNTHESIS-tmp78y0i. So SYNTHESIS-tmprhzl8 is mostly closed by either count, and SYNTHESIS-tmp78y0i and
SYNTHESIS-tmp1m0vj are closed by relations and joined by mentions. The line is a
candidate to split (ADR-083), the support part most clearly; every
SYNTHESIS-tmprhzl8 entry that links to another component already carries
realizability. The split is the owner's decision about the lines
vocabulary.

## Not stated on the record

Links between the parts tested at this review by ADR-075's step 5 and
not filed:

- **Readiness records and a foreclosed transition** (SYNTHESIS-tmp78y0i with
  SYNTHESIS-tmp1m0vj): already inside CLAIM-632's premise that the records estimate
  every capacity a response needs.
- **When a certification expires** (SYNTHESIS-tmp78y0i with SYNTHESIS-tmprhzl8's decay): a free
  parameter, the map from a skill's effect size to a capacity's
  probability.
- **A funding loop with a deadline** (SYNTHESIS-tmp78y0i with SYNTHESIS-tmprhzl8): needs a
  premise no component holds, that learning from practice outside
  operation needs capacity already present.
- **A savings buffer as a transition threshold** (SYNTHESIS-tmp1m0vj with SYNTHESIS-tmprhzl8):
  equates two resource types TERM-105 keeps apart.
- **Supply rate as maintenance requirement** (SYNTHESIS-tmp1m0vj with SYNTHESIS-tmprhzl8):
  a relabelling of CLAIM-597's formula.
- **The three requirements of a form, each lost by its own mechanism**
  (all three parts): a conjunction, and CLAIM-632 already names
  construction cost and the threshold against a waste verdict.

## What it does not say

- That the readiness argument applies to any real organization; its
  constructions and models say their organizational readings are
  analogies.
- That the line should be split; that is reported, not decided.
- Anything with standing of its own.
