---
name: write-manuscript
description: How a manuscript is manifested and fleshed out from the record as a view over its argument - from a work in the `works` vocabulary and a motivating draft (an assistant's write-up, an owner's outline) to a cited, fact-checked, reviewed working draft in scratch/manuscripts/, with its analysis executed, its gaps fed back to the record, its open items routed to the owner, and its refreshes as the record moves. Use it when the owner asks to draft, flesh out, refresh or revise a manuscript tied to the record's arguments, or to turn an exchange's write-up into one. ADR-143 holds the invariants; ADR-104 the membership rule.
---
<!-- .claude/skills/write-manuscript/SKILL.md -->

# Writing a manuscript from the record

A manuscript is a view over the record's argument, written for a reader
outside the record. The record holds the argument. The manuscript arranges
part of it into a paper and says what each step rests on and how firmly.
Preferably nothing in it is new: restatements are fine, and what it states
that no entry maps to is filed in the record, as an account (SYNTHESIS) of
its scope, before the manuscript is ready (step 6). The owner's ruling of
2026-11-23. It is a working document in
`scratch/manuscripts/<work>/`, under version control and outside the
record: luria does not read `scratch/`, and does not repair it either.

ADR-143 holds what must stay true. This file says how it is done now,
and it is meant to change. When a step turns out wrong or missing, edit it
in the same pull request as the work that showed it, and say so in the
changelog fragment.

**Where the procedure comes from.** The first manuscript,
`scratch/manuscripts/from-obstruction-to-reorganization/`, was made between
2026-11-20 and 2026-11-22 in pull requests 555, 556, 557, 582, 584, 597,
609, 621 and 623. It was reviewed in RETRO-006 and RETRO-007, and parts of
it in RETRO-008. Its README and `REVIEW-2026-11-20.md` show the product.
The commits, the pull request bodies, the workbench entries of 2026-11-20
and the retrospectives show the process, including what went wrong. Read
both before departing from a step here. The second manuscript,
`scratch/manuscripts/governance-of-possibility/`, is the first written
under this skill.

## 1. The work

- **There is a `works` term for it.** If there is none, add one by
  decision, on the model of ADR-104 and ADR-106: the term, its label and
  blurb, and its first members. The blurb names the request and the draft,
  and, once it exists, the directory. Changing `luria.yaml` waits on the
  owner's merge.
- **Members are found by reading**, under ADR-104's rule. A CLAIM or ARG is
  a member when the manuscript states its proposition or uses it as a
  step. A citation in a reference list alone does not count. Membership
  says nothing of status (ADR-032).
- **Membership is revisited.** When a successor draft takes over a work,
  or a refresh adds steps, run a membership pass under ADR-104 in its own
  pull request. Until one has run, the README says membership is as of
  its date. The first manuscript's membership was never revisited after
  its successor draft (ADR-135), and still lists its predecessor's
  members.
- **Whether a successor draft is the same work is the owner's ruling.** If
  it is, ADR-135 is the precedent: the term is renamed to the draft's
  directory.

## 2. The motivating draft

The owner often starts a manuscript from a write-up made elsewhere, such as
an assistant's article at the end of an exchange, or from an outline. It is
a motivating draft. It fixes the scope, the order and the questions, and it
is not the record's text.

- **Keep it whole.** Save it verbatim in the scratchpad, and point every
  digester, drafter and reviewer at that file.
- **Audit it before using it**, as the read-and-file skill's step 9b
  audits a synthesis. Record the audit in the curation entry of the work's
  decision, or in a curation entry of its own when the work already
  exists. The first manuscript's exchange was never filed or audited, and
  its corrections lived only in a commit message.
  - **Map** each section to the codes that hold it.
  - **Fidelity:** check every statement it makes about the record (a
    code's title, its status, "Nucleation holds…") against the entry.
  - **Attribution:** name the owner's contributions as the owner's, and do
    not tell an assistant's own claims as the record's.
  - **What it adds:** test each integration by ADR-075's routes. What
    passes is filed; what fails is a recap or a gap.
  - **Gaps:** steps it asserts without deriving, numbers that do not check,
    tests proposed without a design, outcomes stipulated as if found.
  - **Research already done:** for every study, experiment or test the
    draft proposes, check whether the record has already done it
    (step 3a). A motivating draft written by an assistant tends to frame
    held results as a programme still to run.
- **File what it adds**, in the voices of whoever put it forward, in the
  work's pull request, before drafting on it (read-and-file steps 9 and
  9a).

## 3. Background digests

Read the regions of the record the manuscript draws on, one digest per
region, in `background/`. Write them before drafting, when the scope is
known. The first manuscript wrote them only when Part I was restructured.
A digest is a dated snapshot:

- a header saying what was read and when, starting from the line accounts;
- only what the record holds, by section:
  - TERMs as a table with quoted definitions;
  - CLAIMs with status, warrant, role, premises and a short quotation;
  - CASEs with what was run and found;
  - open QUESTIONs and LEADs;
- a last section, marked as the digester's own reading: what the
  manuscript can rest on, what is only Proposed, what is missing, and the
  tensions between entries.

Digests are delegated in parallel, one region each. A digester writes only
its own file, edits nothing in the record, and commits a whole file, not a
partial one.

## 3a. What the record has already done

The owner, 2026-11-24, on the first motivating draft of the series
governance-of-becoming: "this is framed as a research program, but most of
the research has already been achieved ... you propose several experiments
which I agree would be interesting, but I think their role in our account
is largely already satisfied by prior work." A manuscript is a view over
work the record holds, so before it proposes anything, it looks for that
work.

- **For each proposed study, test or experiment** (in the motivating draft,
  a digest's "missing" list, or a draft), search the record for what
  already plays its role: executed-study and reported-study CASEs,
  demonstrated or empirical CLAIMs, readings (THEORY), and LEADs already
  run or closed. Search by the construction and the measure, not only the
  words.
- **Sort each one:**
  - *done*: an entry does what the study would do. The manuscript cites the
    entry and its standing, and proposes nothing.
  - *done in part*: an entry does it for a narrower case (a scalar where the
    study wants a perspective, a model where it wants a field case). The
    manuscript cites it and states the extension, which may be a LEAD.
  - *not done*: then, and only then, a LEAD (step 6).
- **Write the sort down** in a section of the README, "What the record has
  already done", with each study's verdict and the entry that settles it,
  and put a dated note on any LEAD filed earlier that the search finds
  redundant.
- **Do it again after drafting.** Drafters and digesters list gaps; each is
  checked the same way before it is filed as a LEAD or a QUESTION.

## 4. Analysis

Every model, figure or "testable" construction the manuscript reports is
run, not stipulated. So is every study the review calls for: the first
manuscript's census came from its review.

- **Where it goes.** Put it in `analysis/`: the model or coding scheme, the
  study that sweeps or tallies it, tests, and a README saying what it
  establishes and what it does not.
- **A computed study**:
  - has tests that include the exact conditions of the record's entries it
    relies on;
  - has at least one negative control that can fail;
  - fixes its seeds;
  - keeps its outputs (JSON and a short results file) beside the code,
    dated by the commit they were run at.
- **A study coded by hand**:
  - has its codebook fixed before coding;
  - has a second coder on a seeded random sample;
  - reports agreement per field;
  - marks as such a batch that one coder adds later;
  - says where the coders are instances of one model family.
- **A finding that rests on one reader's interpretive classification** is
  checked by a second reader or by the owner before it is filed or
  reported (RETRO-007).
- **One copy of the data.** When a study is filed as a CASE, keep one copy
  of its data and scripts, and have the other place cite it. The first
  manuscript's census was copied to `scratch/formal/decision-census/`, and
  the two copies diverged.
- **A result that bears on an entry** goes back to the record as a CASE or
  a dated note (step 6). The manuscript cites the entry.

## 5. Draft

- **Files by part**, each under about 500 lines, in reading order, each
  beginning with its path as a comment.
- **It is a manuscript, written for a reader outside the record**
  (ADR-tmpw306d). It argues for its thesis. Each step cites the entry that
  holds it, in parentheses, with the code bare. Standings, voices,
  provenance, the reviews and the record's process go in the README and a
  short note on method; the argument does not narrate them. Where a step's
  firmness matters to the argument (a conjecture, a model, a contested
  premise), the text says so in its own words.
- **Quote where a paraphrase would move scope.** Keep an entry's scope
  conditions (its "only", "unless", "when"). Never turn a sufficient
  condition into a definition, or a conjunction into an identity. These
  overreaches were the first manuscript's dominant error, and they ran one
  way: citing codes did not prevent them (RETRO-006).
- **Voices stay separate.** Name the owner's theses as the owner's, another
  assistant's as theirs, and the drafting assistant's own additions as its
  own.
- **Integrations are marked.** Where the manuscript joins steps the record
  keeps apart, say so in the text, and collect those joins in one place (a
  section or a table). They are on their way to the record (step 6), not
  the manuscript's to keep.
  - Before calling a join new, search the "Not stated on the record"
    sections of the accounts its components belong to. A join an account
    has declined is not new (RETRO-006).
  - When a join is drafted, put it to ADR-075's step 5 by an independent
    reader with a neutral brief. Under ADR-131 the test routes and does
    not reject; step 6 says where each verdict goes. Correct the text on
    the verdicts.
- **Expectations before results.** State each expectation with its
  falsifier before the results that grade it. Use a census, or another
  sampling frame, not hand-picked cases. Do not count a measure that holds
  by lint or policy as evidence.
- **Use the motivating draft for scope and order, not text.** Rewrite from
  the digests and the entries, and quote the draft only as the draft.
- **State limits early**: how the argument was developed (with AI
  assistants, who also study the record that holds it), and what in the
  manuscript is a model rather than evidence.
- **Drafters** are delegated by part, in parallel. Each gets the digests,
  the audit, the analysis results and the other parts' scope, lists the
  files it writes, and writes only those. One writer edits a given file at
  a time (ADR-139).

## 6. Joins and gaps go back to the record

What the manuscript states and the record does not hold is not settled
inside the manuscript, and is not thrown away either.

- **Restatements** of an entry are fine. Cite the entry.
- **Joins no entry maps to are filed as accounts** (the owner's ruling of
  2026-11-23). Group them by scope, and file or revise one SYNTHESIS per
  scope (ADR-083, ADR-084, ADR-129), on the synthesis-review skill's
  stage 4. The account integrates the components. It attributes each link
  to the entry that states it, and puts each join no component states
  under "Not stated on the record", with its ADR-075 verdict. A join that
  passes the test is also filed as a Proposed CLAIM, and the account
  integrates it. The manuscript then cites the account, or the claim, for
  each join.
- **A join an account has declined** is not stated as held. Check that the
  decline tested the join as the manuscript states it, against the record
  as it now stands. A decline made against another predicate, or before a
  distinction the record has since drawn, gets a dated note on the account
  saying so, and the join is filed as above.

- **A missing step with content of its own** is filed as a Proposed CLAIM,
  a QUESTION or a LEAD, in the drafting assistant's voice, in the
  manuscript's pull request (read-and-file step 9a's rule). Where two
  readings are open, file both as alternatives.
- **A measurement the manuscript proposes** becomes a LEAD with its design
  fixed when it is filed, and its defeaters stated as checks the record
  can run. Run the leads the owner triages. Feed each result back to its
  entry, to the manuscript and to the README.
- **Anything left open** is listed in the README's open items, with what
  would settle it.
- **Membership of what is filed.** A claim filed for the manuscript is a
  candidate member under ADR-104's rule. List it as one in the pull
  request; adding it is the owner's call.

## 6a. A targeted promotion review

The owner, 2026-11-24: "we can probably also use this as an exercise to
identify content on the record that is still in a proposed state but which
the record functionally treats as Active and should probably be promoted."
A draft shows which Proposed entries the argument leans on, so each draft
is followed by a review of those entries' standing.

- **The candidates** are the Proposed entries the draft uses as premises
  (cited as a step, not only mentioned), together with the Proposed entries
  they rest on.
- **For each candidate, record:**
  - its status and warrant;
  - how many entries rest on it, ground on it or use it;
  - whether its evidence or computation has been checked by someone other
    than its filer, and by whom (history notes, CASEs, a fact-check);
  - whether its `defeated_if` (CLAIM) or `promote_when` (THEORY) is met or
    open, and any objection standing against it;
  - whether the draft describes its standing correctly.
- **Recommend** promote, or keep with the reason. A result that is
  demonstrated and independently recomputed is the clearest case. An
  interpretive claim used as a premise many times is a candidate, not a
  promotion: its use is evidence of reliance, not of truth.
- **Put the table to the owner** as a checklist (ADR-124's form). The
  manuscript never confers standing, so a promotion is the owner's, or the
  assistant's only where the owner has delegated it, as on 2026-11-24 for
  independently recomputed demonstrated claims.
- **Keep it** in the README, "Standing review", dated, and refresh it at
  each refresh (step 9).

## 7. Independent review

- **Who.** A reviewer who did not draft reads the whole draft and every
  cited entry, without the drafters' reasoning. The brief states the tests
  neutrally and does not say how the drafting went.
- **What it checks.** Every statement it can (quotations, standings,
  attributions, figures) is checked against its entry. The rest is
  spot-checked, and the reviewer says how many.
- **Points of contact.** The record is searched, region by region with one
  searcher each, for points of contact the draft does not use: entries and
  readings (THEORY, CASE) that bear on a section and are not cited. The
  process history (decisions, reviews, skills) is one of the regions. In
  the first manuscript it is where the draft's central premise was found
  wrong.
- **Confirmed corrections.** The coordinator re-checks every correction
  against its entry before writing it into the review, and marks it
  confirmed.
- **What it produces.** A verdict, the structural problems ranked, the
  factual corrections, and a revision plan, in `REVIEW-<date>.md` beside
  the draft.
- **The draft is committed unchanged with its review**, and the plan is
  put to the owner. Revise on the plan as the owner accepts or amends it.

## 8. Revise, check, and land

- **Revise on the review**, item by item. The README says which items were
  taken, which not, and why, quoting the owner where the owner's direction
  overrode the plan.
- **Cite what the contact search found.** Each relevant entry or reading
  the search found uncited is read and cited where it bears, with its
  standing, or listed in the README with the reason it was left (the
  owner's ruling of 2026-11-23). A reading that bears on a join is also
  integrated by the join's account.
- **An independent fact-check after every substantive version**: after the
  revision, after any restructuring, and after each refresh.
  - A reader who did not write the text checks every quotation, standing
    and figure against its entry, and reproduces every figure.
  - Fix what it finds, and say in the commit how many problems it found.
  - The first manuscript's three fact-checks found 9, 37 and 7 errors.
- **The README** gives:
  - provenance: the motivating draft, its date and turn, the digests, the
    review and the fact-checks;
  - status: outside the record, what is the manuscript's own, and
    membership as of its date;
  - the files in reading order;
  - the analysis and how to run it;
  - the open items for the owner, numbered. Ruled items move to "Closed
    since the last list" with the ruling quoted and its pull request, and
    the numbering is kept.
- **Pull requests into staging**, cut from staging once the work's
  decision and any entries the draft cites have merged there (ADR-116).
  - The draft's pull request carries the draft, its gap entries, the
    dated notes the analysis calls for, devlog notes and the changelog
    fragment.
  - What the draft derives as a unit of its own (a census filed as a CASE,
    principles filed as accounts) goes in a pull request of its own
    (ADR-071; the owner's "in an independent PR", 557).
  - So does each later refresh.
  - Commit and push as each part lands.
- **Open items go to the owner** in the pull request's "Choices waiting on
  the owner".
  - On merge into staging, add them to the promotion pull request's
    choices section. Read it just before writing, and edit only that
    section (ADR-128).
  - The owner rules inline, or by ticking a box (ADR-124). Record each
    ruling in the README.
- **Devlog notes as the work goes**, tagged `retro`, in the manuscript's
  pull request (ADR-115). When the batch closes, check ADR-110's triggers
  for a retrospective. The first manuscript took none, and RETRO-006 had
  to reconstruct it.

## 9. Refresh

When the record moves, a manuscript drifts. A refresh is triggered when the
owner asks, when entries the manuscript **cites** change status or have
their codes concretized at a promotion, or after an adoption or status
review. It runs after the filings it describes have landed (ADR-139), and
it:

- **Digests.** Adds a dated update at the head of each digest, rather than
  rewriting it.
- **Standings.** Rechecks every cited standing.
- **Temporary codes.** Replaces temporary codes with permanent ones, using
  each entry's `formerly:`. luria does not repair `scratch/`, so this is
  done by hand, in the manuscript only. Never script the rewrite into
  record files (RETRO-007). The first manuscript still cites 55 temporary
  codes that have all been made permanent.
- **Figures.** Recomputes them: `scratch/formal/analytics/` for the
  record's own statistics, or the manuscript's own `analysis/`. Run them
  at a named commit after a promotion, keep the outputs dated, and let
  figures not recomputed keep their dates in the text.
- **The neighbourhood.** Files dated notes on the accounts and claims the
  manuscript's integrations correspond to, where the record has moved.
- **The README.** Adds a dated refresh note, saying what changed by
  section.
- **Membership.** Revisits it (step 1).
- **Checking.** Is followed by an independent fact-check (step 8).

The owner may also have a status review order its work by the
manuscript's citations, as pull request 556 did. The manuscript confers no
standing. It chooses the order, not the rulings. Afterwards, the review's
list of what the draft now gets wrong is applied to it.
