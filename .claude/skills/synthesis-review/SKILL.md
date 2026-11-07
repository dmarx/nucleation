---
name: synthesis-review
description: A periodic review of the record for synthesis opportunities - CLAIMs that are syntheses filed as claims and should move into the SYNTHESIS scheme, and integrations whose parts the record holds but no entry states. Use it when the owner asks for a synthesis review or a current-account refresh, at a status review, or after a run of filings in one line. ADR-078 holds the invariants; ADR-075 the audit and admission test it applies; ADR-076 the scheme it files into.
---
<!-- .claude/skills/synthesis-review/SKILL.md -->
<!-- inactive-ok-file: ADR-078 ADR-075 ADR-076 — Proposed; the decisions this skill carries out, until the owner adopts them -->

# Synthesis review

A synthesis review looks across the record, not at one source. It asks two
questions:

- **Arm A, migration.** Which CLAIMs are syntheses filed as claims, and
  should move into the SYNTHESIS scheme?
- **Arm B, opportunity.** Where does the record hold the parts of an
  integration that no entry states?

The review files nothing it cannot admit. Most candidates turn out to be
atomic claims, or integrations already exhausted by their components, and
the review says so and moves on. The salience a SYNTHESIS entry gives has
to be earned (ADR-075, step 5).

## 1. Stage 1: rank candidates mechanically

Run `python3 -I scratch/formal/synthesis_candidates.py --top 12`. It reads
the record and ranks four kinds of candidate. It decides nothing.

- **A: CLAIMs that may be syntheses.** These are claims whose premises
  (`rests_on`) number three or more and span two or more lines, scored up
  for premises that are themselves theses and for account-shaped wording.
- **B1: `complements` clusters.** These are three to twelve in-force claims
  within one line, joined by `complements`, which means "answers a
  different part of the same question".
- **B2: open questions** with three or more unintegrated answers or
  bearings across lines.
- **B3: deep chains.** These are Active theses at `rests_on` depth three or
  more that no synthesis integrates.

Add by hand what the script cannot see:

- syntheses that curation entries record as left;
- syntheses the owner asked for, which the workbench entries record;
- integrations the owner has named.

Entries a SYNTHESIS already integrates or supersedes are out of scope.

## 2. Stage 2: shortlist

Take the strongest candidates, a dozen at most, across both arms. Prefer
in-force components to Proposed ones. An integration of Proposed claims is
Proposed at best. Prefer lines the current-account view does not yet
cover. Drop a candidate whose components are mostly one entry's
restatements.

## 3. Stage 3: audit each shortlisted candidate

For each, read the candidate and every component in full. Then:

- **State the integrating claim in one sentence, apart from its
  components.** If no such sentence can be written, the candidate is not a
  synthesis. For Arm A it is an atomic claim and stays a CLAIM. Say so.
- **Run ADR-075's five checks:**
  - attribution: whose each component is;
  - coverage: what the integration leaves out that the record holds;
  - fidelity: whether each component is stated rightly;
  - standing: each component's status;
  - integration: what it claims beyond the components.
- **Run the admission test, and say which route it passed:**
  - *hypothesis*: a coherent case in which every component holds and the
    integration fails;
  - *derived*: a valid, nontrivial inference no claim holds;
  - *integration*: a dependency, mechanism or prediction the components
    leave open.

## 4. Stage 4: act on the verdict

- **Arm A, admitted.** File a SYNTHESIS carrying the claim's title, body
  and defeater, with `admission: admitted`, its route, its role, every
  component in `integrates` and its premises in `premises`. Carry its
  `grounds` and `uses` unchanged (a reading's `corroborates` comes with it,
  being stored on the reading), and keep its standing
  (ADR-077): an Active claim becomes Current, a Proposed one stays
  Proposed, and a Deferred or Rejected one is not moved. Set the CLAIM to
  Superseded by it. Then audit the relations pointing at the CLAIM:
  - repoint those that describe the current account (an ARG's `concludes`,
    a CASE's `illustrates`, a reading's `corroborates`, a synthesis's
    `integrates` and `premises`);
  - leave those that record history;
  - leave `complements` until dmarx/luria#358 is fixed.
- **Arm A, not admitted.** It stays a CLAIM. Record the verdict.
- **Arm B, admitted.** File a new SYNTHESIS, Proposed. The integration is
  the reviewer's, so its summary ends: "The integration's wording is the
  assistant's (Claude, in this session); adopting it is the owner's call."
  Its components keep their own voices, named in the body.
- **Arm B, not admitted.** File nothing. Record the candidate and the
  reason.
- **Never set a new synthesis Current.** Adoption is the owner's; only a
  move carries Current, from a claim that was Active.

File the ARGs that step 10 of `read-and-file` requires: support that is
load-bearing or contested.

## 5. Account for it

Write a curation entry, "Synthesis review of DATE", with four parts:

- **the ranking**: the stage-1 output's top rows, and what was added by
  hand;
- **the shortlist and verdicts**: one row per candidate, giving its arm, its
  integrating sentence, whether and by which route it was admitted, and the
  code filed or the reason not;
- **relations repointed**, for each migration;
- **what the current-account view now shows**: lines covered, and lines
  still without a synthesis.

Add a changelog fragment. One review is one contribution (ADR-071).
