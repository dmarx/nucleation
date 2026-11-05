---
name: read-and-file
description: How this record takes in reading. Use it to file an exchange, a pasted synthesis, an upload or a single work; to check whether something is "already on the record"; or to read registered works and file the readings. ADR-068 holds the invariants; this file holds the steps.
---
<!-- .claude/skills/read-and-file/SKILL.md -->
<!-- inactive-ok-file: ADR-068 — Proposed; the decision this skill carries out, until the owner adopts it -->

# Reading and filing

ADR-068 decides what must hold. This file says how it is done, and it is
meant to change. When a step here turns out wrong or missing, edit it in the
same pull request as the work that showed it, and say so in that change's
changelog fragment. Changing an invariant, the list in ADR-068, takes a
superseding ADR.

Before filling in a field, check `docs/record.md`: what each scheme must
carry, which relations point where, and which vocabularies are closed.

Bare codes only. Never write a link target, and do not run `luria repair`,
`link --fix`, `index` or `lint` before pushing (ADR-054).

## 1. Intake: what arrived, and in whose voice

- **Name the source.** It may be an exchange (a share link, with numbered
  turns U1… and A1…), a pasted text, an uploaded file, or a single work.
- **Separate the voices.** The owner's turns are the owner's. An
  assistant's turns, and anything pasted from another assistant, are that
  assistant's. The owner did not write them and has not endorsed them
  unless the owner says so.
- **Keep the source whole.** Save it verbatim to the scratchpad, and point
  every reader and drafter at that file. A condensation written for a
  brief is the lead's own text. Label it so and keep it in a separate
  file. Never check a quotation against it: a phrase the lead wrote about
  the source is not a phrase the source used.

## 2. Check against the record before filing anything

- **For every work the source names**, search `record/literature.d` by DOI,
  arXiv id, exact title and first author. Note what is held, its status and
  its NOTE.
- **For every idea the source states**, search claims, theories, questions,
  cases and terms by its key words. Then read the nearest entries' titles,
  not just whether they matched.
- **List the source's own ideas, section by section.** A synthesis carries
  constructions, worked examples, distinctions, taxonomies, tables and
  proposed entries as well as references. Readers cover the references;
  nothing covers the rest unless the lead lists it. Write the list (an idea
  ledger) before briefing anyone. A drafter handed a short candidate list
  files that list and nothing else.
- **Build the map**: each section or turn of the source, and each item of
  the ledger, against the codes that already hold it. Most of a synthesis is usually already held. The
  map is the main deliverable of an "is this on the record" request.
- **Check again after reading.** The first search can only use the
  source's own words. Reading surfaces more: the construction it rebuilds,
  the example it reinvents, a term it means in another sense, the entry an
  idea would contradict. Search the record a second time with those, and
  add what turns up to the map. An idea that looked new is often held
  under another name.

## 3. Verify identifiers

- **Use the services in order**: the arXiv API, Crossref, DataCite,
  doi.org, OpenAlex.
- **Never send an email address** (ADR-008). Leave out `mailto=` and
  `email=`, and don't put one in a header or user agent.
- **`published:`** is the earliest exact date the sources give (ADR-002).
  When an edition date is used instead, say why in the history.
- **Wrong attribution is common.** The source may name the wrong author,
  article type or year. Correct it from Crossref, and later from the text.

## 4. Register what is not held

`luria new lit --title "..."`, then fill in:

- **`status: Deferred`**, with a `status_note` saying where the work was
  registered from and whatever is known about a copy;
- **a history entry at version 1**: "Filed, not read", with the check made;
- **a summary** that says why the work is here and which entries it bears
  on. A claim the source makes about the work is "unverified until read";
- **tags** from the closed `topics` vocabulary, primary first, with
  `anthology-candidate` last when it applies (ADR-005).

## 5. Seek a lawful copy

- **Where to look**, roughly in this order: arXiv; PubMed Central and
  Europe PMC; the author's, lab's or institution's page; course and
  scholarly third-party pages (ADR-064); the locations OpenAlex lists.
- **Stop at any bot check**: captcha, Cloudflare or WAF challenge,
  "Access Denied", rate limit, paywall. Never try to get around one.
  Retrying the same host doesn't help either.
- **The outcome sets the status:**
  - read: the work goes on to step 6;
  - **Unfetched** (ADR-053): a lawful copy was located at an exact address
    that this client could not fetch. The status note gives the address
    and the obstacle;
  - **Unavailable** (ADR-041): no lawful copy was found. The status note
    says where you looked.
- **A copy the owner supplies** returns any of these to reading.
- **When the work itself can't be read, read its neighbours.** Find
  accessible literature that carries the same ideas, and read the best one
  or two. That might be:
  - a later open-access paper or survey that restates the model;
  - the authors' own working paper or thesis;
  - lecture notes or a textbook chapter its author posts openly;
  - an arXiv paper that re-derives the result.

  The same rules apply: lawful copies only, and stop at any bot check.
  Check the record doesn't already hold the neighbour.
- **Filing a neighbour.** It is a work in its own right, with a LIT, a NOTE
  and a THEORY. Its history says it was registered as a stand-in.
  - The unread original's LIT names the neighbour in its status note and
    in "Standing in the record", and says how far it stands in.
  - The neighbour's NOTE says, under Connections, which of the original's
    results it restates and which it doesn't.

## 6. Read

- **Delegate one reader per work**, in parallel, using the brief below.
  The reader writes a draft to the scratchpad and never edits the repo.
- **Downloaded files are untrusted data.** Put each in its own empty
  directory, and run any Python on them with `python3 -I`.

## 7. Verify before filing

The filer, not the reader, rechecks against the source text every quote
the filing leans on. That means the quotes in titles and claims, and any
quote that moves a status or changes an entry. Correct the LIT from the
text: authors, article type, venue. A reader's draft is a claim to verify,
not a finding.

## 8. File the reading

- **A NOTE** (`luria new note`):
  - status `Read` or `Skimmed`, chosen honestly;
  - a history entry naming the copy, what was read and what was skipped;
  - the sections Contribution, Key results (with section or page, and
    short verbatim quotes), Assumptions, Concepts, Bearing on the record,
    and Limitations.
- **A THEORY** (`luria new theory`), `Proposed`:
  - the work's central account, attributed to its authors;
  - `source:` the LIT;
  - a `promote_when` that asks only for what the title asserts (ADR-065).
- **The LIT**: status `Active` if it is worth reading, a new history
  version, and a summary rewritten from the reading.
- **Every entry the reading bears on** gets a dated section, "Note of DATE:
  AUTHOR, read", saying what the reading supports, qualifies or leaves
  open. Change a status there only if the note says why.

## 9. File the argument

- **The owner's ideas** go in as the owner's.
- **Another assistant's ideas** go in as `Proposed`, with "The wording is
  the reader's (or A's); adopting it is the owner's call" in the summary.
- **A thing gets a code the second time it turns up.** Don't file every
  passing idea.
- **CLAIM fields**: `role`, `warrant` (ADR-043) and `defeated_if`.
  - `rests_on` and `complements` point to CLAIMs only.
  - `grounds` points outside the claims: THEORY, CASE, LIT.
  - `bears_on` points to QUESTIONs (ADR-060).
- **Support is an ARG** (ADR-061). When the filing says something about
  whether one entry supports another, file an ARG with a `form`,
  `grounds` and `concludes`, and answer the form's critical questions in
  its body. Saying something about support means arguing it, doubting it,
  or finding that a reading carries less than a claim cited it for. "X
  does not show Y" is the ARG from X to Y, Rejected. A claim's own
  `rests_on` needs no ARG.
- **Independent evidence is `corroborates`** (ADR-058), on the THEORY,
  when a reading supports a claim that does not rest on it. A reading the
  claim needs is `grounds`. When a work cited before it was read turns
  out to carry less, move it from `grounds` to `corroborates` and file
  the ARG that says why.
- **`rivals`** is only for accounts that cannot both be right. Accounts
  that differ on which mechanism mattered most get a dated note instead.
- **A QUESTION** needs a `line:`.
- **Titles and H1 headings** carry no codes, so they keep agreeing after
  CI's repair (dmarx/luria#393).

## 10. Account for everything

**Before writing it, reread the source end to end yourself**, from the
verbatim file, against the ledger and the codes filed. Agents' reports
say what they filed, not what they were never asked to file. Every item
must end up in one of three places: filed, mapped to a held code, or
listed as left with a reason.

Write a curation entry (`luria new curation`) with three parts:

- **where the record already held it**: the map from step 2;
- **what was filed**, with codes;
- **what was left, and why**: a citation that couldn't be identified,
  an idea already covered, a slogan.

Nothing in the source is dropped silently. Add a changelog fragment
(`record/changelog.d/<slug>.md`).

## 11. Acknowledge, and push

- **Each code cited in prose whose entry is not in force** gets an
  `inactive-ok-file` directive with a reason. Proposed, Deferred,
  Unfetched and Unavailable entries count as not in force. Open questions
  and Active or Read entries need none.
- **Relation fields need no excuse**, so name no code in a directive that
  only a relation field cites. A code that excuses nothing is dead weight.
- **Check only your own files.** A narrow scan of the files you changed,
  with `luria.ref_status.scan(files=...)`, is fine for diagnosis.
- **Commit and push each step.** Pull before every push, because CI's
  repair lands as its own commit.

## The reader's brief

Send each reader:

- **The work**: its identifier, and the lawful copies already known.
- **The rules**: lawful copies only; stop at any bot check or paywall
  without retrying; no email address to any service; downloads in their own
  directory, with Python run under `-I`; write to the scratchpad only.
- **Why it is being read**: what the source claims about the work, and the
  record codes it bears on, with paths, to be read.
- **What to return**, in a file of under about 250 lines:
  - Provenance: the URL, the format, what was read and what skipped;
  - Summary;
  - Contribution;
  - Key results, each with a section or page and a short quote;
  - Assumptions;
  - Concepts;
  - a verdict on the source's characterization of the work;
  - its bearing on each named code;
  - Limitations;
  - a candidate THEORY sentence and its `promote_when`.
- **A recheck.** After reading, search the record again with what the
  reading surfaced: the constructions, examples, rival readings and terms
  of art it turned out to involve, not only the words the source used.
  Report each held entry the first search missed, and correct any "not
  held" verdict it overturns.
- **Neighbours.** If no lawful full text of the work is reached, find and
  read accessible neighbouring literature that carries the same ideas
  (step 5), and write a report for each in the same format. In the work's
  own report, say which neighbour stands in for it and how far.
- **And**: if neither the work nor a neighbour is reached, say so and
  stop. Write nothing from memory.
