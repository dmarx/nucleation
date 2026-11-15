---
status: 'Proposed'
title: 'The organizational-normativity line is split in two: organizational-normativity keeps what a normative judgment needs and the wrong beyond harm; what wholes and parts owe each other, and what those who govern an arrangement others depend on owe, become the line dependence-and-domination, because those parts relate to the first two almost only through its root questions'
version: 1
tags:
- record
date: '2026-11-15'
summary: >-
  The synthesis review of 2026-11-15 (pull request #505) gave
  organizational-normativity an account over four parts: what a normative
  judgment needs; the wrong beyond harm and becoming normatively less
  informed; what wholes and parts owe and claim; and what those who govern
  an arrangement others depend on owe. 93 of the line's 102 stored
  relations fall inside a part. Of the nine that cross, seven point at the
  root questions QUESTION-128 and QUESTION-129, and two are CLAIM-687's
  complements. By ADR-083's signal the line is a candidate to split. The
  assistant proposed a split in two and the owner approved it ("yes on the
  two line split", 2026-11-15). organizational-normativity keeps the first
  two parts and both root questions, with a narrower blurb. A new line,
  `dependence-and-domination`, "Wholes, parts and dependence", takes the
  29 entries of the third and fourth parts. Three of them keep
  organizational-normativity second, because they refine or bear on a
  root question (ADR-085). Rejected: keeping one line; a line of its own
  for the fourth part; a split in four; moving the parts into
  distributed-agency.
---
<!-- inactive-ok-file: ADR-082 ADR-083 ADR-085 ADR-087 ADR-089 ADR-090 ADR-099 — Proposed; the decisions on lines, splits and accounts this applies -->
<!-- inactive-ok-file: SYNTHESIS-038 — Proposed; the line's account, revised at pull request #505 -->
<!-- inactive-ok-file: ARG-110 CLAIM-428 CLAIM-614 CLAIM-624 CLAIM-669 CLAIM-670 CLAIM-671 CLAIM-673 CLAIM-682 CLAIM-685 CLAIM-686 CLAIM-687 CLAIM-690 TERM-122 TERM-123 TERM-124 — Proposed; moved or cited, with their standing -->

# ADR-tmpbthzh: The organizational-normativity line is split in two: organizational-normativity keeps what a normative judgment needs and the wrong beyond harm; what wholes and parts owe each other, and what those who govern an arrangement others depend on owe, become the line dependence-and-domination, because those parts relate to the first two almost only through its root questions

## Context

A line is "a named line of the record's own argument, so that a line can
be set aside as a whole and what depends on it can be found" (the `lines`
vocabulary, ADR-032). organizational-normativity was split from
will-organization by ADR-089 with 23 entries, for "whether an
organization's own dynamics ground norms of function and failure, and what
judging an organization needs beyond them". By 2026-11-15 it held 71,
filed from "About Plantation Paradise", "Analyze technological
civilization trap" and the exchanges around them.

The synthesis review of 2026-11-15, pull request #505 (not yet merged when
this was written), gave the line an account over four part accounts, with
SYNTHESIS-038 (version 4) as the line's account over them:

1. **what a normative judgment needs** (19 components): viability does not
   establish what ought to persist, a judgment is well-defined once its
   relata are fixed and can then be false (CLAIM-363), some judgments need
   histories, and a self-maintaining system's failure norm is set by its
   own upkeep; with the root questions QUESTION-128 and QUESTION-129;
2. **the wrong beyond harm, and becoming normatively less informed** (24):
   a bounded duty of answerability (CLAIM-614, CLAIM-624) and the routes
   by which an organization loses sight of what it owes;
3. **what wholes and parts owe and claim** (20): what a whole owes its
   parts, with ground and bearer kept apart (QUESTION-460), when a whole's
   need of a part becomes the part's authority (QUESTION-461), the routes
   into exploitation (CLAIM-669, CLAIM-670), control over the terms as
   what sorts a dependence (CLAIM-690), exploitation and domination
   relative to a declared standard (TERM-123, TERM-124), and the
   domination threshold (CLAIM-682, CLAIM-686);
4. **what those who govern an arrangement others depend on owe** (9): A's
   claims from "Analyze technological civilization trap" on separable
   dimensions of power, the burden of justification, accountability that
   rises with indispensability (CLAIM-687), the erosion of governing
   capacity (CLAIM-673), declining a technology, and reflexive institutions
   (CLAIM-685), with the concordance term TERM-122.

Counting stored front-matter relations as `scratch/formal/line_parts.py`
does, by the part each starts in, 93 of 102 fall within parts:

| part | inside |
|---|---|
| what a normative judgment needs | 24 |
| the wrong beyond harm and becoming less informed | 38 |
| what wholes and parts owe and claim | 29 |
| what those who govern an arrangement owe | 2 |

Of the nine that cross, seven point into the first part, and all seven are
`refines` or `bears_on` onto QUESTION-128 or QUESTION-129. The other two
are CLAIM-687's `complements` onto CLAIM-624 (second part) and CLAIM-682
(third). The second and third parts are mostly closed, so by ADR-083's
signal the line is a candidate to split. The review left the split to the
owner, with ADR-082 as the precedent.

The assistant proposed a split in two, and the owner approved it on
2026-11-15: "yes on the two line split". This is the owner's decision,
made on the assistant's proposal.

## Decision

- **One line is added** to the closed `lines` vocabulary:
  `dependence-and-domination`, "Wholes, parts and dependence". Its blurb
  names what wholes and parts owe each other; when dependence becomes
  domination or exploitation; that control over the terms, not the size
  of the dependence, decides which way a dependence runs; and what those
  who control an arrangement others depend on owe. It says that
  "organization" here is TERM-074's sense 1, a relational arrangement, by
  default, and that the bearers of obligations, agents or roles, are kept
  apart from the ground of the obligation. Both are the separations the
  owner asked the line's accounts to keep, and the components keep them:
  every bearer a component of the two parts names is an agent or a role.
  It says it was split from organizational-normativity.
- **organizational-normativity keeps the first two parts** and its root
  questions, QUESTION-128 and QUESTION-129. Its blurb is narrowed to them
  and points to the new line.
- **The 29 entries of the third and fourth parts move.** In each, `line`
  changes organizational-normativity to dependence-and-domination in place.
  Other lines are kept. Each entry gets a version and a history note. No
  status, title or relation changes.
  - Every entry whose first line was organizational-normativity now has
    dependence-and-domination first. QUESTION-464, whose first line is
    distributed-agency, keeps it first and has dependence-and-domination
    second.
- **An entry that argues within organizational-normativity keeps it**
  (ADR-082, version 2; ADR-085). It does when it refines a question, or
  answers, objects to or bears on an entry, whose first line is
  organizational-normativity. Three do, and carry it second:
  - QUESTION-460 refines QUESTION-128;
  - QUESTION-468 refines QUESTION-129;
  - CLAIM-685 bears on QUESTION-128.

  These are three of the seven crossings into the first part; the other
  four come from the second part, which stays. No moved entry rests on an
  entry of the first two parts. CLAIM-687's `complements` onto CLAIM-624 is
  not participation (ADR-085), so CLAIM-687 drops organizational-normativity.
  No entry outside the two parts answers, refines, objects to or bears on a
  moved entry, so no entry gains the new line. The readings that bear on
  QUESTION-460 and QUESTION-461 take their lines from the entries that use
  them, derived, not stored (ADR-090).
- **The fourth part is not a line of its own.** It has only two relations
  inside it, and it hangs together by its source, one exchange, more than
  by its relations. Its relations to the rest of the line are CLAIM-685's
  bearing on QUESTION-128, a root question, and CLAIM-687's complements
  onto CLAIM-624 and onto CLAIM-682, which is in the third part. Its
  subject, what the controllers of an arrangement others depend on owe, is
  the third part's question asked of the controllers: CLAIM-687's body
  says who owes is "those who control" the arrangement, "the agents
  CLAIM-682's second condition names".
- **The accounts follow the split, after #505 merges.** #505 owns the
  four part accounts and SYNTHESIS-038 until it merges, and this decision
  does not touch them. Once it has merged, the part accounts of the third
  and fourth parts take the new line, the new line gets an account over
  them, and SYNTHESIS-038 is revised over the first two parts, keeping its
  version 4 counts as the record of why the line was split.

## Alternatives considered

- **Keep one line.** What argues for it: TERM-122, TERM-123 and TERM-124
  apply CLAIM-363's relata in their bodies, and part 3's questions refine
  the old root questions (QUESTION-460 refines QUESTION-128, QUESTION-468
  refines QUESTION-129). But both are a few relations against 29 inside
  the third part, and setting organizational-normativity aside would take
  the inquiry into domination and exploitation with it, which is the
  opposite of what a line is for. The split leaves those relations
  crossing lines, as ADR-082's split did: the two refinements are kept as
  participation by the second line the questions carry, and the terms'
  use of CLAIM-363 is a dependency the argument chain reports.
- **A line of its own for the fourth part.** It has two relations inside,
  and it would be a line held together by one exchange. Besides a root
  question, its relations within the line go to CLAIM-682, in the third
  part, and CLAIM-624. As a line of its own it would make the relation to
  the third part a crossing too, and gain nothing.
- **Split in four.** The first two parts share the root questions: four
  of the seven crossings into the first part come from the second. Apart,
  they would leave the wrong beyond harm without the question it bears on.
- **Move the third and fourth parts into distributed-agency.** Five of
  their entries already carry it, and they keep it. But distributed-agency
  asks "what an organized whole is, and how its operative direction
  relates to its members'". Whether a dependence is domination, and what
  its controllers owe, is a normative question about the terms of an
  arrangement, and distributed-agency is already one of the record's
  largest lines.

## Consequences

- The current-account view shows two lines where there was one. Until the
  accounts are restructured after #505, the new line has no account of its
  own, and SYNTHESIS-038's part accounts still name organizational-normativity
  as their line.
- `luria lint` may report more `rests_on` steps across lines, for example
  from ARG-110 (dependence-and-domination) into CLAIM-428
  (distributed-agency), as before. They are dependencies, and they are
  reported, not failures.
- ADR-099 placed the claims on domination and exploitation through
  dependence (CLAIM-669, CLAIM-670, CLAIM-671) in organizational-normativity.
  They are now in dependence-and-domination first. ADR-099 takes a
  history note saying so; its body is unchanged.
- The name and blurb of the new line are the assistant's proposal. The
  owner may rename it before merging. A rename is a vocabulary edit plus
  the same 29 `line` values.
