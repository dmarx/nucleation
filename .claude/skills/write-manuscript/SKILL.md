---
name: write-manuscript
description: How a manuscript is manifested and fleshed out from the record as a view over its argument - from a work in the `works` vocabulary and a motivating draft (an assistant's write-up, an owner's outline) to a cited, reviewed working draft in scratch/manuscripts/, with its analysis executed and its gaps fed back to the record. Use it when the owner asks to draft, flesh out, refresh or revise a manuscript tied to the record's arguments, or to turn an exchange's write-up into one. ADR-tmpbdfmk holds the invariants; ADR-104 the membership rule.
---
<!-- .claude/skills/write-manuscript/SKILL.md -->

# Writing a manuscript from the record

A manuscript is a view over the record's argument, written for a reader
outside the record. The record holds the argument; the manuscript arranges
part of it into a paper, says what each step rests on and how firmly, and
marks what it adds. It is a working document in
`scratch/manuscripts/<work>/`, under version control and outside the
record: luria does not read `scratch/`.

ADR-tmpbdfmk holds what must stay true. This file says how it is done now,
and it is meant to change: when a step turns out wrong or missing, edit it
in the same pull request as the work that showed it, and say so in the
changelog fragment.

The worked examples are `scratch/manuscripts/from-obstruction-to-reorganization/`
(its README and REVIEW file show the procedure end to end) and
`scratch/manuscripts/governance-of-possibility/`, the first written under
this skill.

## 1. The work

- **There is a `works` term for it.** If not, add one by decision, on the
  model of ADR-104 and ADR-106: the term, its label and blurb, and its first
  members. The blurb names the request, the draft and, once it exists, the
  directory.
- **Members are found by reading** (ADR-104's rule): a CLAIM or ARG whose
  proposition the manuscript states or uses as a step. A citation in a
  reference list alone does not count. Membership says nothing of status
  (ADR-032).
- **The directory takes the work's name.** One work, one directory; a
  successor draft of the same work renames the term to it (ADR-135).

## 2. The motivating draft

The owner often starts a manuscript with a write-up made elsewhere, such as
an assistant's article at the end of an exchange, or an outline. It is a
motivating draft: it fixes the scope, the order and the questions, and it is
not the record's text.

- **Keep it whole.** Save it verbatim in the scratchpad, and point every
  digester, drafter and reviewer at that file.
- **Audit it before using it**, as the read-and-file skill's step 9b audits
  a synthesis, and record the audit in the curation entry of the work's
  decision:
  - *map* each section to the codes that hold it;
  - *fidelity*: every statement it makes about the record (a code's title,
    its status, "Nucleation holds…") checked against the entry;
  - *attribution*: the owner's contributions named as the owner's, an
    assistant's own claims not told as the record's;
  - *what it adds*: each integration tested by ADR-075's routes; what passes
    is filed, what fails is a recap or a gap;
  - *gaps*: steps it asserts without deriving, numbers that do not check,
    tests proposed without a design, outcomes stipulated as if found.
- **File what it adds**, in the voices of whoever put it forward, in the
  work's pull request, before drafting on it (read-and-file steps 9 and 9a).

## 3. Background digests

Before drafting, read the regions of the record the manuscript draws on,
one digest per region, in `background/`. A digest is a dated snapshot:

- a header saying what was read and when, starting from the line accounts;
- only what the record holds, by section: TERMs as a table with quoted
  definitions; CLAIMs with status, warrant, role, premises and a short
  quotation; CASEs with what was run and found; open QUESTIONs and LEADs;
- a last section, marked as the digester's own reading: what the
  manuscript can rest on, what is only Proposed, what is missing, and the
  tensions between entries.

Digests are delegated in parallel, one region each. A digester writes only
its own file and edits nothing in the record.

## 4. Analysis

Every model, figure or "testable" construction in the manuscript is run,
not stipulated.

- Put it in `analysis/`: the model, the study that sweeps it, tests, and a
  README saying what it establishes and what it does not.
- The tests include the exact conditions of the record's entries the model
  relies on, and at least one negative control that can fail.
- Fix seeds; keep the outputs (JSON and a short results file) beside the
  code; date the run.
- A result that bears on an entry goes back to the record as a CASE or a
  dated note (step 8), and the manuscript cites the entry, not the script.

## 5. Draft

- **Files by part**, each under about 500 lines, in reading order, each
  beginning with its path as a comment.
- **Every step cites the entry that holds it, with its standing**: Active
  or Proposed, and demonstrated, empirical or interpretive. Codes are
  written bare. Statuses are as of the draft's date.
- **Voices stay separate.** The owner's theses are named as the owner's;
  another assistant's as theirs; the drafting assistant's own additions as
  its own.
- **Integrations are marked.** Where the manuscript joins steps the record
  keeps apart, it says so, and collects those joins in one place (a section
  or a table) as the manuscript's own, not entries the record holds.
- **Use the motivating draft for scope and order, not text.** Rewrite from
  the digests and the entries; quote the draft only as the draft.
- **State limits early**: how the argument was developed, and what in the
  manuscript is model rather than evidence.
- Drafters are delegated by part, in parallel, each given the digests, the
  audit, the analysis results and the list of the other parts' scope.

## 6. Gaps go back to the record

What the argument needs and the record does not hold is not settled inside
the manuscript.

- A missing step with content of its own is filed as a Proposed CLAIM, a
  QUESTION or a LEAD, in the drafting assistant's voice, in the manuscript's
  pull request (read-and-file step 9a's rule).
- Anything left open is listed in the README's open items, with what would
  settle it.
- A claim filed for the manuscript is a member if the manuscript states it
  or uses it as a step.

## 7. Independent review

- **A reviewer who did not draft** reads the whole draft and every cited
  entry, without the drafters' reasoning. The brief states the tests
  neutrally and does not say how the drafting went.
- It checks every statement it can against the entry: quotations,
  standings, attributions, figures; it spot-checks the rest and says how
  many.
- It searches the record for points of contact the draft does not use.
- It gives a verdict, the structural problems ranked, the factual
  corrections, and a revision plan, in `REVIEW-<date>.md` beside the draft.

## 8. Revise, and land

- **Revise on the review**, item by item; the README says which items were
  taken, which not, and why.
- **A last fact-check** of the revised text against the entries.
- **The README** gives: provenance (the motivating draft, its date and
  turn; the digests; the review), status (outside the record; what is the
  manuscript's own), the files in reading order, the analysis and how to
  run it, and the open items for the owner.
- **One pull request into staging**, cut from staging once the work's
  decision and any entries the draft cites have merged there. It carries
  the draft, the entries filed for it (step 6), dated notes the analysis
  calls for, and a changelog fragment. Commit and push as each part lands.

## 9. Refresh

When the record moves, a manuscript drifts. A refresh, on the owner's
request or when its members change status:

- re-reads the digests' regions and adds a dated update at the head of each
  digest rather than rewriting it;
- rechecks every cited standing and replaces temporary codes with their
  permanent ones;
- reruns the analysis and dates the new outputs;
- adds a dated refresh note to the README saying what changed, by section;
- revisits membership.
