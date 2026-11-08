---
name: synthesis-review
description: A periodic review of the record's accounts - that each line, or part of one, has a SYNTHESIS that maps it faithfully; that claims which only map their components become accounts; and that integrations whose parts the record holds are filed as claims when they add something. Use it when the owner asks for a synthesis review or a current-account refresh, at a status review, or after a run of filings in one line. ADR-078 holds the invariants; ADR-075 the audit and the test for a claim whose premises are claims; ADR-tmp72iro what a SYNTHESIS is; ADR-083 coverage.
---
<!-- .claude/skills/synthesis-review/SKILL.md -->
<!-- inactive-ok-file: ADR-078 ADR-075 ADR-tmp72iro ADR-083 ADR-082 — Proposed; the decisions this skill carries out, until the owner adopts them -->

# Synthesis review

A SYNTHESIS is an account of a scope of the record's argument: a line, or a
part of one. It names every component, attributes each link to the entry
that states it, and adds nothing. Whatever adds to its components is a CLAIM
(ADR-tmp72iro). A synthesis review looks across the record and asks three
questions:

- **Coverage.** Does each line, or each major part of one, have an account?
  Is each account faithful to its components as they now stand?
- **Arm A, claims that are accounts.** Which CLAIMs only map their
  components, and so are accounts filed as claims?
- **Arm B, integrations held in parts.** Where does the record hold the
  parts of a link that no entry states? Does that link add enough to be
  filed as a claim?

An account earns no standing, so filing one needs no admission. A claim
does. ADR-075's test (step 5) is how a claim whose premises are claims
shows it has content of its own. Most Arm B candidates turn out to be
stated already in a component's body or notes. Then the account records
where, and nothing new is filed.

## 1. Stage 1: rank candidates mechanically

Run `python3 -I scratch/formal/synthesis_candidates.py --top 12`. It reads
the record and ranks four kinds of candidate. It decides nothing.

- **A: CLAIMs that may be accounts.** These are claims whose premises
  (`rests_on`) number three or more and span two or more lines, scored up
  for premises that are themselves theses and for account-shaped wording.
- **B1: `complements` clusters.** These are three to twelve in-force claims
  within one line, joined by `complements`, which means "answers a
  different part of the same question".
- **B2: open questions** with three or more answers or bearings across
  lines.
- **B3: deep chains.** These are Active theses at `rests_on` depth three or
  more.

Add by hand what the script cannot see:

- the lines and parts of lines with no account (the current-account view
  lists them last);
- accounts whose components have been revised since the account was
  written;
- integrations that curation entries record as left;
- integrations the owner asked for or named, which the workbench entries
  record.

## 2. Stage 2: shortlist

Take the strongest candidates, a dozen at most, across the arms. Prefer
in-force components to Proposed ones. Prefer lines the current-account view
lists as having no account. Drop a candidate whose components are mostly
one entry's restatements. A claim whose body has an "Admission" section has
been tested already; leave it unless its premises have changed since.

## 3. Stage 3: audit each shortlisted candidate

For each, read the candidate and every component in full. A reader's
brief states the tests neutrally. It does not say how earlier rounds came
out, and it does not ask for strictness or leniency. Then:

- **Run ADR-075's checks:**
  - attribution: whose each component is;
  - coverage: what the scope's account leaves out that the record holds;
  - fidelity: whether each component is stated rightly;
  - standing: each component's status;
  - integration: what is claimed beyond the components.
- **State in one sentence what the candidate adds to its components.** If
  no such sentence can be written, it adds nothing, and it belongs in an
  account.
- **Test that sentence as a claim** (ADR-075, step 5). It has content of
  its own if it passes one of three routes:
  - *a separating case*: a coherent case in which every premise holds (no
    premise's `defeated_if` is met) and the sentence fails;
  - *a derivation*: a valid, nontrivial inference no claim already holds;
  - *a discriminating prediction*: a dependency, mechanism or outcome the
    components leave open.
- **Check a realistic separating case against the claim.** If the case is
  not stipulated and could plainly occur, check it against the claim's own
  `defeated_if`. Such a case shows the claim is separate from its
  premises, and it may also show the claim is false. Say which it does.
- **Watch for a free parameter.** A word that absorbs every case ("a
  declared bearer", "relevant") makes the test pass trivially. Close it
  before testing, or the candidate fails.

## 4. Stage 4: act on the verdict

- **The scope's account comes first.** For each scope the shortlist
  touches, file its account, or revise the one there is as a new version.
  There is one account per scope (ADR-083). The account is a
  SYNTHESIS, Proposed:
  - every component in `integrates`, with its voice and status in the body;
  - each link it states attributed to the entry that states it;
  - nothing added. A link no component states goes under "Not stated on
    the record";
  - `defeated_if` is fidelity: a component misstated or misattributed, an
    in-force component of the scope left out, or a link no component
    states.
- **When a line's account falls into parts,** give each part its own
  account, and make the line's account one over them, with the part
  accounts in `integrates`.
- **When the parts barely relate,** run
  `python3 -I scratch/formal/line_parts.py --sections <the account>`, or
  run it with the part accounts as arguments. If two or more parts are
  mostly closed (most of their relations inside, little pointing in),
  report the line as a candidate to split. The split is a decision about
  the lines vocabulary, for the owner (ADR-082 is the first). Do not
  force one account over parts that do not hang together.
- **Arm A: the claim adds nothing.** It fails ADR-072's rule as a claim.
  Fold its mapping into its scope's account, and set the claim to
  Superseded by that account. Then repoint every claim's `rests_on` that
  named it to the premises it rested on, with a history note on each.
- **Arm A: the claim adds something.** It stays a CLAIM. Its scope's
  account integrates it. If the test turned up a separating case or a
  derivation the claim lacks, add it to the claim's body under
  "Admission".
- **Arm B: the link passes the test.** File it as a new CLAIM, Proposed,
  with its premises in `rests_on`, and the case or derivation in its body
  under "Admission". The link is the reviewer's, so the summary ends: "The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call." Its scope's account integrates it.
- **Arm B: the link is already stated.** File nothing new. The account
  records which entry states it.
- **Arm B: the link fails for another reason** (a free parameter, a
  component stated wrongly, a contradiction). Record the candidate and the
  reason. If the account names the link, it goes under "Not stated on the
  record".
- **Never set an account Current.** Setting one Current says its mapping
  has been reviewed by the owner. A Current account must integrate no
  Superseded claim or account; lint enforces this
  (`current_account_on_superseded_claim`,
  `current_account_on_superseded_account`).

File the ARGs that step 10 of `read-and-file` requires: support that is
load-bearing or contested.

## 5. Account for it

Write a curation entry, "Synthesis review of DATE", with four parts:

- **the ranking**: the stage-1 output's top rows, and what was added by
  hand;
- **the shortlist and verdicts**: one row per candidate, giving its arm,
  the sentence it adds, whether it passed and by which route, and the code
  filed or the reason not;
- **accounts filed or revised**, and relations repointed;
- **what the current-account view now shows**: the lines with an account,
  and the lines with none.

Add a changelog fragment. One review is one contribution (ADR-071).
