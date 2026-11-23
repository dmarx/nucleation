---
status: Proposed
title: 'A manuscript is written from the record as a view over its argument, by a written protocol: its invariants are held in this decision, and its steps in a skill that changes with practice'
version: 1
tags:
- record
date: '2026-11-23'
summary: >-
  At the owner's request of 2026-11-23 ("let's also document a
  protocol/procedure for manifesting and fleshing out a manuscript draft
  from a view over the argument like this"), manuscripts tied to the
  record's arguments follow a protocol in two layers, as reading and filing
  do ([ADR-068](ADR-068.md)): eight invariants here, and the steps in
  .claude/skills/write-manuscript/SKILL.md. The procedure is the one the
  manuscript from-obstruction-to-reorganization converged on between
  2026-11-20 and 2026-11-21, written down; its first application is the
  manuscript governance-of-possibility, in this decision's pull request.
  Rejected: leaving the procedure in that manuscript's README, and holding
  manuscripts inside the record.
---

# ADR-tmpbdfmk: A manuscript is written from the record as a view over its argument, by a written protocol: its invariants are held in this decision, and its steps in a skill that changes with practice

## Context

The record has two manuscripts drafted in its working tree, and more works
in its `works` vocabulary than drafts. The first draft,
`scratch/manuscripts/from-obstruction-to-reorganization/`, was written out
from a ChatGPT exchange on 2026-11-20 and then reworked: cited digests of
the record's regions (`background/`), a census run as code with a second
coder (`analysis/`), an independent review kept beside the draft
(`REVIEW-2026-11-20.md`), a revision on it, a fact-check, and refreshes as
the record moved. Its README is the only place that procedure was written,
and only as that draft's history.

On 2026-11-23 the owner asked for ChatGPT's article "Regulation as the
Governance of Possibility" to be treated as a motivating draft, for the
from-obstruction-to-reorganization manuscript to be taken as the example of
the procedure, and for the manuscript to be fleshed out (work
governance-of-possibility, [ADR-tmpsfjxu](ADR-tmpsfjxu.md)). In the same exchange the owner
asked for the procedure to be documented.

## Decision

Manuscripts tied to the record's arguments are written by a protocol in two
layers.

**The invariants, held here.** Changing one takes a superseding ADR:

1. **A manuscript is a view, outside the record.** It lives in
   `scratch/manuscripts/<work>/`, one directory per work in the `works`
   vocabulary. No entry, vocabulary or relation is changed by writing it;
   what the manuscript needs from the record is filed in the record.
2. **Every step cites the entry that holds it, with its standing.** A
   reader can tell, step by step, what the record accepts, what it only
   proposes, and what is demonstrated, empirical or interpretive.
3. **The manuscript's own joins are marked.** Where it integrates entries
   the record keeps apart, it says so and collects those integrations as
   its own; it never presents them as held.
4. **Voices stay separate** ([ADR-068](ADR-068.md)'s sixth invariant). The owner's theses
   are named as the owner's, an assistant's as theirs.
5. **A motivating draft is audited before it is used.** An assistant's
   write-up or an outline fixes scope and order. What it says the record
   holds is checked against the entries, and what it adds is tested
   ([ADR-075](ADR-075.md)) and filed or listed as a gap before the draft builds on it.
6. **Results are executed, not stipulated.** A model, figure or test the
   manuscript reports is run as code with tests and a negative control, and
   its outputs are kept beside it with their date.
7. **Gaps go back to the record.** A step the argument needs and the record
   lacks is filed as a Proposed entry or listed as an open item for the
   owner; it is not settled in the manuscript's prose.
8. **An independent review precedes the owner's reading.** A reviewer who
   did not draft checks the text against every cited entry and writes the
   review beside the draft, and the revision says what it took from it.

**The steps, held in `.claude/skills/write-manuscript/SKILL.md`.** The skill
covers the work and its membership ([ADR-104](ADR-104.md)'s rule), the motivating draft's
audit, background digests, analysis, drafting, gaps, review, revision,
landing and refresh. When a manuscript finds a step wrong or missing, the
skill is edited in the same pull request, and the changelog fragment says
what changed and why.

## Alternatives

- **Leave the procedure in the first manuscript's README.** That is where
  it was. It is one manuscript's history, written after the fact, and a
  second manuscript would have to reconstruct the procedure from it; the
  owner asked for it to be documented.
- **Hold manuscripts inside the record**, as a scheme of their own. A
  manuscript is a view the owner revises as prose, for an outside reader;
  the record's grammar (one claim per entry, a status per claim) is what it
  is a view over, and two copies of the argument would drift ([DP-003](../../docs/design-principles.md#dp-3)). The
  `works` field already ties the two.
- **A skill without a decision.** The steps change with practice, but the
  invariants are what make a manuscript trustworthy as a view; [ADR-068](ADR-068.md)
  separates the two for the same reason.

## Consequences

- The first application is in this decision's pull request:
  `scratch/manuscripts/governance-of-possibility/`, written from ChatGPT's
  article by the skill.
- from-obstruction-to-reorganization was written before the protocol and is
  not rewritten to it; its next refresh follows the skill.
- CLAUDE.md gains a line naming the skill, beside read-and-file.
