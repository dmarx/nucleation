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
  do (ADR-068): eight invariants here, and the steps in
  .claude/skills/write-manuscript/SKILL.md. The steps are drawn from how
  the manuscript from-obstruction-to-reorganization was made, from
  2026-11-20 to 2026-11-22 (its commits, pull requests 555 to 623,
  workbench entries and RETRO-006 to RETRO-008), with the reviews'
  lessons put in at the points where they arose; its first application
  is the manuscript governance-of-possibility, in this decision's pull
  request.
  Rejected: leaving the procedure in that manuscript's README, holding
  manuscripts inside the record, and a review that must precede the
  owner's reading.
---

# ADR-tmpbdfmk: A manuscript is written from the record as a view over its argument, by a written protocol: its invariants are held in this decision, and its steps in a skill that changes with practice

## Context

The record has more works in its `works` vocabulary than drafts. The first
draft, `scratch/manuscripts/from-obstruction-to-reorganization/`, was
written out from a ChatGPT exchange on 2026-11-20 (pull request 555) and
expanded at the owner's direction before any review. Then came, in order:

- an independent review in four inputs, kept beside the draft;
- a census the review called for, with a codebook fixed before coding and
  a second coder;
- a revision on the review's plan, and a fact-check;
- cited digests of the record's regions, at a restructuring;
- a second fact-check;
- a status review ordered by the manuscript's citations (556);
- the draft's derived entries, filed in a pull request of their own at the
  owner's request (557), with an admission audit;
- the owner's rulings, inline on the promotion pull requests (582, 599);
- refreshes (584, 597, 609), the last with a third fact-check;
- the manuscript's leads, run (621, 623).

RETRO-006, RETRO-007 and RETRO-008 reviewed parts of this. They found:

- the drafter's restatements overreached, in one direction;
- integrations were stated as principles before they were tested;
- the refreshes were hand-copied;
- no devlog notes were taken;
- a finding rested on one reader's classification.

The manuscript's README records the product, not this process; the process
is in git, the pull request bodies, the workbench entries and the
retrospectives. A first version of this decision was written from the
README alone, and the owner asked for it to take the practice into
account (devlog of 2026-11-23).

On 2026-11-23 the owner asked for ChatGPT's article "Regulation as the
Governance of Possibility" to be treated as a motivating draft, for the
from-obstruction-to-reorganization manuscript to be taken as the example of
the procedure, and for the manuscript to be fleshed out (work
governance-of-possibility, ADR-tmpsfjxu). In the same exchange the owner
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
3. **Nothing in a manuscript is new to the record.** Restatements are
   fine. Where it joins entries the record keeps apart, it says so, and
   each join no entry maps to is filed in the record before the manuscript
   is ready: as an account (SYNTHESIS) of its scope, with the join under
   "Not stated on the record" unless a component states it, and as a claim
   too when it passes ADR-075's test. It never presents a join as held
   (the owner's ruling of 2026-11-23).
4. **Voices stay separate** (ADR-068's sixth invariant). The owner's theses
   are named as the owner's, an assistant's as theirs.
5. **A motivating draft is audited before it is used.** An assistant's
   write-up or an outline fixes scope and order. What it says the record
   holds is checked against the entries, and what it adds is tested
   (ADR-075) and filed or listed as a gap before the draft builds on it.
6. **Results are executed, not stipulated.** A model, figure or study the
   manuscript reports is run: a computed one as code with tests and a
   negative control, a hand-coded one with a codebook fixed before coding
   and a second coder. Its outputs are kept beside it with their date. A
   finding that rests on one reader's interpretive classification is
   checked by a second reader or by the owner before it is reported
   (RETRO-007).
7. **Gaps go back to the record.** A step the argument needs and the record
   lacks is filed as a Proposed entry or listed as an open item for the
   owner; it is not settled in the manuscript's prose.
8. **Every substantive version is checked by a reader who did not write
   it, and the record is searched for what it should cite.** Relevant
   entries and readings the search finds uncited are cited, or listed with
   the reason they were left (the owner's ruling of 2026-11-23). The first draft is reviewed against every cited entry, the review
   kept beside the draft and its plan put to the owner to accept or amend.
   Each later version (a revision, a restructuring, a refresh) is
   fact-checked against the entries before it is put to the owner as
   ready. The owner may read and direct a draft at any stage.

**The steps, held in `.claude/skills/write-manuscript/SKILL.md`.** The skill
covers the work and its membership (ADR-104's rule), the motivating draft's
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
  is a view over, and two copies of the argument would drift (DP-003). The
  `works` field already ties the two.
- **A skill without a decision.** The steps change with practice, but the
  invariants are what make a manuscript trustworthy as a view; ADR-068
  separates the two for the same reason.
- **"An independent review precedes the owner's reading"**, this
  decision's first wording of invariant 8. False to the practice: the
  owner read and directed the first manuscript before its review, and the
  checks that mattered were repeated, one after each version.

## Consequences

- The first application is in this decision's pull request:
  `scratch/manuscripts/governance-of-possibility/`, written from ChatGPT's
  article by the skill.
- from-obstruction-to-reorganization was written before the protocol and is
  not rewritten to it. Its next refresh follows the skill. That refresh
  would replace its 55 temporary codes, all now permanent, and run the
  membership pass ADR-135 left as separate work.
- CLAUDE.md gains a line naming the skill, beside read-and-file.
