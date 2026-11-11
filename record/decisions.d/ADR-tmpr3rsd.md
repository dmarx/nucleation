---
status: Proposed
title: 'An entry shows the accounts that integrate it: `integrates` gets a derived converse, `integrated_by`, on every scheme an account can integrate, so a part of a line''s argument is visible from its members and not only from the current-account view'
version: 1
tags:
- record
date: '2026-11-10'
summary: >-
  The synthesis reviews of 2026-11-10 divided lines into parts, each with
  an account, and kept some densely linked parts together in one line. The
  owner asked whether tags or some other abstraction express what such a
  cluster has in common. Measured, no `topics` tag both covers a part and
  is specific to it, because tags record what a work is about, at the grain
  of a field. Some parts hang from a root question or a hub claim, and
  six have none. The one thing that names every part is its account, and
  `integrates` runs one way: no entry shows which account it belongs to.
  This decision gives `integrates` a derived converse, `integrated_by`,
  declared on the seven schemes an account can integrate, and stored on
  no entry (ADR-079). On the record of 2026-11-10 it annotates 163
  entries, 18 of them with two or more accounts. Rejected: cluster-level
  tags; a stored `part` field; leaving it to the current-account view.
---
<!-- inactive-ok-file: ADR-079 ADR-083 ADR-084 ADR-085 — Proposed; the derived converses, the accounts and the line rule this builds on -->

# ADR-tmpr3rsd: An entry shows the accounts that integrate it: `integrates` gets a derived converse, `integrated_by`, on every scheme an account can integrate, so a part of a line's argument is visible from its members and not only from the current-account view

## Context

ADR-083 and ADR-084 made a SYNTHESIS the account of a scope of the
record's argument, a line or a part of one, and let a line's account be
built over its parts' accounts. The reviews of 2026-11-10 used this for
four lines:

- organizational-affect: valence, corporate affect, and feeling;
- readiness: keeping, reaching, and withdrawing, the last since split off
  as transient-support;
- learned-structure: six parts;
- nucleating-argument: drift, anchors, and costs, from earlier.

Readiness's keeping and reaching parts were kept in one line, because
they share 28 linked pairs.

The owner asked whether tags or some other abstraction express what such
a cluster has in common. Measured over the parts' components:

- **Tags do not.** The `topics` vocabulary says what a work is about, at
  the grain of a field. The best-fitting tag is never both covering and
  specific:
  - loss-landscapes is on all 9 connectivity components, and on 26
    entries record-wide;
  - consciousness is on 6 of the 7 feeling components, and on 28
    record-wide;
  - operations-research leads both readiness parts kept together, so it
    cannot tell them apart.
- **Some parts hang from one entry:**
  - acquisition from QUESTION-039, which 9 of its 12 components refine;
  - last-layer collapse from QUESTION-051 (5 of 6);
  - withdrawal from QUESTION-398 (9 of 30);
  - reaching from CLAIM-571 (9 of 24);
  - valence from CLAIM-440 (8 of 26).
- **Six parts have no such entry:** corporate affect, feeling, nesting,
  concepts, the costs of anchoring, and keeping.

The one thing that names every part is its account. But `integrates` is
declared on SYNTHESIS with no converse. A claim's page does not say which
part, or which line's account, it belongs to. The current-account view is
the only place the parts can be seen.

ADR-079 already stores each directed relation on one side and derives its
converse when the record is read. Examples are `refined_by`,
`answered_by` and `bearing`.

## Decision

- **`integrates` gets a converse, `integrated_by`.** It is labelled
  "Accounted for in". SYNTHESIS's `integrates` names it as its converse.
- **It is declared on every scheme an account can integrate:** CLAIM,
  TERM, CASE, THEORY, QUESTION, ARG and SYNTHESIS. On a SYNTHESIS it names
  the line account built over a part account.
- **It is derived, never stored** (ADR-079). No entry is edited. Every
  page of an integrated entry lists the accounts that integrate it, Current
  or Proposed, once the views are regenerated.
- **A superseded account still appears, with its status.** The page shows
  every account that names the entry, and says which are in force.

## Alternatives considered

- **Cluster-level tags.** They would mix two grains in one closed
  vocabulary, a field and a part of one argument. They would also carry no
  standing, and they would have to be kept in step with accounts by hand.
- **A stored `part` field on each entry.** This is a second axis beside
  `line` doing an account's job, as ADR-082 said when it rejected a part
  field. It would also be stored on many entries, which ADR-079 avoids for
  any relation that can be derived.
- **Leave it to the current-account view.** The view shows parts from the
  account's side. A reader on a claim's page, or a filer adding a relation
  to it, would still not see which account must be revised when the claim
  changes.
- **Root questions alone.** Where a part asks one question, a root
  QUESTION that its members refine or bear on is the record's own way to
  say so, and it is filed separately where it has content of its own
  (ADR-072). But six parts have none, and not every part asks one
  question. A converse covers every part without inventing a question.

## Consequences

- On the record of 2026-11-10, 163 entries gain an "Accounted for in"
  list: 72 claims, 45 questions, 21 cases, 16 terms, 3 ARGs and 6 part
  accounts. Eighteen are in two or more accounts. One is CLAIM-355, in the
  evidence-for-experience account, the feeling part and organizational
  affect's line account.
- **A component's revision now shows which accounts to recheck.** ADR-083
  makes leaving out or misstating a component an account's defeater, so
  this is the list a filer needs.
- **No question-to-subquestion relation is added.** `refines` is one
  already: "the broader question this one is a part or a sharpening of",
  with the derived converse `refined_by`. The root questions filed beside
  this decision use it.
