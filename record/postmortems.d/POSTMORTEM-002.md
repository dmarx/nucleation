---
number: 2
status: Superseded
formerly:
- POSTMORTEM-tmp7fylf
title: 'The session''s changes to luria.yaml of 2026-11-19: a work for the owner''s manuscript, the explication form, and the LEAD scheme'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Converted to a retrospective, RETRO-004, by the decision adding
    the RETRO scheme (ADR-115): it reviews how a change or a batch
    went, which is now a RETRO's job; a POSTMORTEM is kept for something
    that went wrong. Retired by status; the body is unchanged.
superseded_by:
- RETRO-004
tags:
- record
- taxonomy
date: '2026-11-20'
reviews:
- ADR-106
- ADR-107
- ADR-109
prompted:
- ADR-111
pull_requests:
- https://github.com/dmarx/nucleation/pull/528
- https://github.com/dmarx/nucleation/pull/533
- https://github.com/dmarx/nucleation/pull/536
- https://github.com/dmarx/nucleation/pull/535
discussions:
- https://claude.ai/code/session_01HcmtbsDR5i5G9oxErMDiB4
summary: >-
  The owner asked on 2026-11-20 for a postmortem of the session's
  luria.yaml changes. The work vocabulary entry is used and fine. The
  explication form works but was filed before its source was read, and
  rewritten twice. The LEAD scheme holds 197 leads but its stage ladder
  does not discriminate (96 per cent at idea), it has no priority field
  for triage, question dependencies are unused, leads cannot target
  theories or terms, there is no blocked state, and its derived converses
  are declared but never written. Recommendations for one decision, and
  three process rules.
---
<!-- inactive-ok-file: RETRO-004 ADR-115 — Draft or Proposed; the retrospective this was converted to, and the decision converting it -->

# POSTMORTEM-002: The session's changes to luria.yaml of 2026-11-19: a work for the owner's manuscript, the explication form, and the LEAD scheme

## What changed

| Change | Commits | Decision | Landed in |
|---|---|---|---|
| A work, cost-structure-of-possibility | 9868fd550 | [ADR-106](../decisions.d/ADR-106.md) | pull request 528 |
| The explication argument form; an ARG may conclude a TERM; TERM `argued_by` | 982f11a7b, revised in 44c192ec3 and fe0aa5921 | [ADR-107](../decisions.d/ADR-107.md) | pull request 533, folded into 528 |
| The LEAD scheme, three vocabularies, `advanced_by` on QUESTION and CLAIM, `operationalizes` on CASE, QUESTION `presupposes` (178 lines) | d80bac44a | [ADR-109](../decisions.d/ADR-109.md) | pull request 536, landed through 535 |

Main's concretization also rewrote the temporary decision and claim codes
inside the config's blurbs (eed84a74e, 58c495fdd).

## How each has been used (main at ace6ccba2, 2026-11-20)

- **The work ([ADR-106](../decisions.d/ADR-106.md)).** 23 entries name it. Nothing to fix.
- **The explication form ([ADR-107](../decisions.d/ADR-107.md)).** One ARG uses it, [ARG-119](../arguments.d/ARG-119.md), the
explication of learning. No TERM carries a stored `argued_by`.
- **The LEAD scheme ([ADR-109](../decisions.d/ADR-109.md)).** 197 leads: 194 Open, 3 Done; stage 190
idea, 4 specified, 3 underway; methods empirical 99, reading 63, formal
58, conceptual 27, historical 13, operationalization 7. 55 point at a
CASE; 12 presuppose another lead, none a question. No QUESTION uses
`presupposes`.

## What worked

- The backlog audit of 2026-11-19 had a home for 184 opportunities, and 52
proposed-study cases are now linked from leads to their designs.
- The method vocabulary covered every opportunity found without an "other".
- The owner's review of [LEAD-006](../leads.d/LEAD-006.md) changed its scope, from building an
environment to investigating task composition, with no schema friction.
- Each decision carried its first application in the same pull request
([ADR-071](../decisions.d/ADR-071.md)), so each was judged by what it did.

## What did not

1. **The explication form was filed before its source was read.** The form
names Carnap; its critical questions were written first and rewritten
twice within hours once Carnap was read (44c192ec3, fe0aa5921).
2. **The stage ladder does not discriminate.** [ADR-109](../decisions.d/ADR-109.md) makes `specified`
require a stated cost, which almost no source gives; 52 cases with full
designs sit at `idea` beside one-line hunches.
3. **No priority.** The owner raised the backlog as a triage problem, and the
backlog cannot be sorted for triage: the audit's ratings live only in the
curation entry of 2026-11-19 (224759), and the generated index lists leads
by line only.
4. **Question dependencies unused.** The owner supported dependencies among
questions; QUESTION `presupposes` has no uses.
5. **Scope unruled.** Leads advance only questions and claims; the audit set
aside opportunities whose only target is a THEORY (replications that would
meet a `promote_when`) or a TERM (owed operationalizations) without a
decision that this is right.
6. **No blocked state.** About 30 reading leads wait on copies the owner must
supply or a host must allow; that can be said only in prose.
7. **Derived converse blurbs mislead.** `advanced_by`, `operationalizes`,
   `presupposed_by` and `argued_by` appear in no source, and the blurbs
   say they are written by `luria link --fix`. They are not meant to be:
   for a directed pair luria stores the primary side and computes the
   derived side for every reader, never writing it back. The blurbs were
   wrong, not the record. (The first version of this postmortem called the
   missing fields a defect and read a dry run's 161 pending
   back-references as theirs; those are completions of undirected pairs
   elsewhere. Corrected 2026-11-20 by the filer, on reading luria's code.)
8. **Bulk filing.** 184 leads were generated by script in one pull request,
checked by script and spot-read, not reviewed one by one.

## What the change cost the process

- **A schema change gates what stacks on it.** Filing the LEAD scheme with
readings on pull request 536 made 538, 539 and 540 stack on it: a
five-deep fold, and repeated conflicts later on dated notes appended to
the same entries.
- **Temporary codes in config blurbs.** ADR and CLAIM temporary codes in
`luria.yaml` depended on main's concretization to be rewritten. It worked,
and it is brittle.
- **A YAML parse error.** An unquoted colon in a blurb broke parsing on the
branch; parsing `luria.yaml` locally before pushing would have caught it.

## Recommendations

1. **A priority field on LEAD**, high, medium or low, backfilled from the
audit's ratings, with the index sorted by it.
2. **A stage ladder that discriminates**: drop the cost from `specified` and
add a `costed` stage, or keep the rule and say `idea` covers designed
studies.
3. **Correct the converse blurbs** to say the fields are computed for every
reader and never stored.
4. **Rule on scope**: whether a lead may advance a THEORY or a TERM, and
whether a `blocked` stage or status is wanted.
5. **Backfill question dependencies or drop the field.**
6. **Process**: read a form's source before filing the form; parse
`luria.yaml` locally before pushing; cite no temporary codes in config;
land a schema change alone and early, so that content does not stack on
it.

Recommendations 1 to 5 are carried out by [ADR-111](../decisions.d/ADR-111.md), named in
`prompted`, with its first application. This scheme's own decision
([ADR-112](../decisions.d/ADR-112.md)) applies recommendation 6's third rule.
