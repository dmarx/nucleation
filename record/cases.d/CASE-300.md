---
number: 300
status: 'Active'
formerly:
- CASE-tmpnkuie
title: 'Who changes the record''s grammar'
statement: >-
  Who changes the record's grammar, how, and with what result: of its 114
  decisions to 2026-11-20, 88 changed the grammar, 62 by refinement, 25 by
  revision and 1 by restraint; the misfit each answered had nearly always
  been forced into a category or kept in prose first; removals were carried
  through every entry using the term while a change of meaning in place
  reached none; and the noticing moved from filing agents to review
  procedures while judgment about revisions stayed with the owner
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Corrected at the owner's ruling of 2026-11-21: anthology-candidate did
    not change meaning, and revisiting its flags is the anthology's
    process. The term audit's row for it moves from redefinition in place
    to widening or restatement, and the finding that entries do not
    follow a change of meaning alone is withdrawn. See the note of
    2026-11-21.
standing: documented
kind: executed-study
tags:
- design-rationale
- philosophy-of-science
date: '2026-11-20'
variant_of:
- CASE-178
illustrates:
- CLAIM-419
- CLAIM-181
bears_on:
- QUESTION-458
- QUESTION-388
- QUESTION-457
line:
- record-as-apparatus
summary: >-
  Run on 2026-11-20 for the owner's manuscript on the record (scratch/
  manuscripts/from-obstruction-to-reorganization/ on its own branch), and
  filed at the owner's direction. Every decision record was coded against a
  codebook fixed before coding, by four coders with a second coder on a
  random 30; every change to a vocabulary term in the record's history was
  audited for whether the entries carrying it were changed with it. The
  data and scripts are in scratch/formal/decision-census/. [CASE-178](CASE-178.md) measured
  how often the grammar grew; this measures who changed it, how, and what
  the changes did.
---
<!-- inactive-ok-file: ADR-124 — Proposed or Open; filed on 2026-11-21 and cited in the refresh of this pull request -->

<!-- inactive-ok-file: ADR-047 ADR-076 ADR-077 ADR-080 — Superseded; cited as decisions the census coded -->
<!-- inactive-ok-file: ARG-028 CLAIM-181 — Proposed; cited in this filing of 2026-11-20 -->

# CASE-300: Who changes the record's grammar

## The case

**Method.** Two analyses, both reproducible from `scratch/formal/decision-census/`.

**The census.** Every decision record from [ADR-001](../decisions.d/ADR-001.md) to [ADR-114](../decisions.d/ADR-114.md), read in full and coded against `census/CODEBOOK.md`, which was fixed on 2026-11-20 before any decision was coded. The codebook asks of each decision:

- whether it changed the grammar: `luria.yaml` declarations, lint patterns and views;
- its level and operation;
- whether it was a **refinement** (adds a distinction; what counted as an answer, a criterion or a unit of inquiry still counts the same way), a **revision** (changes one of those) or **restraint** (a proposed change declined or narrowed);
- which component of an inquiry it touched, in [TERM-095](../terms.d/TERM-095.md)'s terms;
- what triggered it;
- who noticed the need, who proposed the design, who decided, and how the owner ratified it;
- what form the misfit took before the decision;
- the size of any migration, the outcome, and any later error.

Four coders, all assistant subagents of one model, coded the 114 decisions in batches. A fifth coded a random 30 (seed 20261120) without seeing the first coding.

**The term audit.** `term_changes.py` reads every authored commit to `luria.yaml` from the repository's first commit to `09950cdf` (2026-11-20). For every vocabulary term whose declaration was reworded, or that was removed, it records:

- whether a decision record was added or changed in the same unit of work;
- how many entries carried the term just before the change;
- how many of those were touched in the same unit, a proxy for being re-read.

For vocabularies used by one scheme only, carriers are counted in that scheme's directory.

**Agreement on the 30 decisions coded twice.**

| Field | Agreement | κ |
|---|---:|---:|
| Grammar change | 0.97 | 0.92 |
| Refinement, revision or restraint | 0.90 | 0.84 |
| Trigger | 0.87 | 0.81 |
| Who noticed | 0.87 | 0.82 |
| Who proposed | 0.90 | 0.85 |
| Who decided | 1.00 | 1.00 |
| Ratification | 1.00 | 1.00 |
| Form of the misfit | 0.73 | 0.65 |
| Outcome | 0.77 | 0.38 |

The outcome field is not used. The coders split on a convention the codebook left open: whether a Proposed decision already applied counts as in force.

## Results

**How the grammar changed.** 88 of the 114 decisions changed the grammar: 62 refinements, 25 revisions and 1 restraint. The revisions include five kinds:

- **What counts as an answer** was redefined ([ADR-049](../decisions.d/ADR-049.md), [ADR-059](../decisions.d/ADR-059.md)).
- **Boundaries between kinds of entry** were redrawn ([ADR-058](../decisions.d/ADR-058.md), [ADR-060](../decisions.d/ADR-060.md), [ADR-061](../decisions.d/ADR-061.md)).
- **An abstraction was withdrawn** ([ADR-084](../decisions.d/ADR-084.md)).
- **Entries were reassigned to new lines** ([ADR-073](../decisions.d/ADR-073.md), [ADR-082](../decisions.d/ADR-082.md), [ADR-087](../decisions.d/ADR-087.md), [ADR-089](../decisions.d/ADR-089.md), [ADR-100](../decisions.d/ADR-100.md)).
- **Senses changed in place** ([ADR-036](../decisions.d/ADR-036.md), [ADR-048](../decisions.d/ADR-048.md)).

| Period | Changes | Refine | Revise | Restraint |
|---|---:|---:|---:|---:|
| 25 Sep–15 Oct | 43 | 37 | 6 | 0 |
| 16 Oct–5 Nov | 20 | 8 | 11 | 1 |
| 6–20 Nov | 25 | 17 | 8 | 0 |

The level moved over time. Early changes were vocabularies and their terms (35 of 43). Late changes were relations (13 of 25), fields, views and lines.

**What the misfit looked like before it was noticed.**

| Form | Changes |
|---|---:|
| Already forced into the nearest category | 43 |
| Held only in prose | 20 |
| No misfit yet: the change anticipated a need | 17 |
| The grammar had made the record assert something false | 4 |
| Unknown | 4 |

In 63 of the 71 changes made in answer to a misfit, the move had first been forced into a category or kept in prose.

**Who noticed, proposed, decided and ratified.**

| Period | Changes | Owner | Filing agents | Assistant in session | External assistant | Review procedure | Unknown |
|---|---:|---:|---:|---:|---:|---:|---:|
| 25 Sep–15 Oct | 43 | 9 | 16 | 1 | 0 | 4 | 13 |
| 16 Oct–5 Nov | 20 | 10 | 1 | 3 | 1 | 4 | 1 |
| 6–20 Nov | 25 | 7 | 3 | 2 | 0 | 12 | 1 |

| Noticed by | Refinements | Revisions |
|---|---:|---:|
| Filing agents | 18 | 2 |
| Owner | 12 | 13 |
| Review procedures | 12 | 8 |
| Assistant in session | 5 | 1 |

Ratification of the 88 changes:

- 48 record the owner's approval of that change;
- 6 cite a standing permission ("The owner authorised extending the vocabulary as the record sees fit", [ADR-034](../decisions.d/ADR-034.md));
- 4 were ratified by merge or by a review procedure the owner delegated to;
- 30 record no owner involvement.

The owner decided 49 changes, an assistant 6 and a review procedure 2; 31 do not say who decided.

**Costs and errors.**

- 58 changes state a migration: 2,664 existing entries in all, median 6.
- 10 grammar changes were followed by a recorded error that the change caused: [ADR-015](../decisions.d/ADR-015.md), [ADR-043](../decisions.d/ADR-043.md), [ADR-047](../decisions.d/ADR-047.md), [ADR-057](../decisions.d/ADR-057.md), [ADR-076](../decisions.d/ADR-076.md), [ADR-077](../decisions.d/ADR-077.md), [ADR-090](../decisions.d/ADR-090.md), [ADR-104](../decisions.d/ADR-104.md), [ADR-107](../decisions.d/ADR-107.md) and [ADR-109](../decisions.d/ADR-109.md).
- 4 were undone within days: [ADR-015](../decisions.d/ADR-015.md) in part, [ADR-076](../decisions.d/ADR-076.md), [ADR-077](../decisions.d/ADR-077.md) and [ADR-080](../decisions.d/ADR-080.md).

**The term audit.** 34 events: 25 declarations reworded and 9 terms removed. Every one came with a decision record in the same unit of work, and one unit was a lone commit.

| Kind of change | Carrying entries touched in the same unit |
|---|---|
| Removal, where the term was in use | All of them: `identity` 41 of 41, `self-and-personhood` 42 of 42, and the four SYNTHESIS terms [ADR-084](../decisions.d/ADR-084.md) removed (12, 5, 9 and 3, all touched) |
| Split | The entries that moved: `Deferred` 177 of 345, `ecology` 13 of 50, the split lines |
| Widening or restatement | Almost none, and none needed: `learning-theory` 1 of 92; `anthology-candidate` 0 of 237 (see the note of 2026-11-21) |
| Redefinition in place | None found |

## What it shows

- **The record answers noticed misfits by changing its grammar, after the grammar has absorbed them.** [CLAIM-181](../claims.d/CLAIM-181.md)'s account, that a move the grammar cannot hold "is forced into one or lost until the misfit is noticed", holds for the misfits that were eventually noticed. [CLAIM-419](../claims.d/CLAIM-419.md)'s amendment by decision is the usual response.
- **The grammar is revised as well as refined.** That includes what counts as an answer, the instance of [CLAIM-470](../claims.d/CLAIM-470.md)'s distinctive clause.
- **Traceability reaches the grammar where entries move.** Every change is announced by decision, and entries follow when they must move. No change of meaning alone is in the history, so the census does not show whether entries follow one.
- **Noticing moved from incidental to procedural.** Filing agents met missing words early; review procedures built to look found later needs. Revision stayed mostly with the owner.

## What it cannot show

- **Misfits never noticed, or noticed and left.** Only decisions are coded. The census cannot see these, so it is no denominator for [CLAIM-419](../claims.d/CLAIM-419.md)'s caveat.
- **That any change improved the inquiry.** Every figure is counted in the record's own grammar ([ARG-028](../arguments.d/ARG-028.md), [CLAIM-266](../claims.d/CLAIM-266.md)).
- **Re-reading.** "Touched in the same unit" is a proxy for it, not a measure of it.
- **Independence of the coders.** All coders were instances of one model, and agreement may partly reflect shared bias. A human second coder would address this.
- **Generality.** One owner, one record and eight weeks.

## What would change it

- A human recode of the 30-decision sample with materially lower agreement on refinement against revision or on who noticed.
- An audit of the source exchanges finding that most misfits were never sent to a decision. That would show the 63 of 71 to be the visible minority, not the pattern.

## Note of 2026-11-21: the census is a day behind

The census counts the 114 decisions to 2026-11-20. By the end of 2026-11-21
the record held about twenty more: [ADR-115](../decisions.d/ADR-115.md) and [ADR-116](../decisions.d/ADR-116.md), and decisions filed
that night on reframings, the dialectic regime, earmarks, merging into
staging, the promotion pull request and an adoption review, several filed as
alternatives of which the owner chose one. The adoption review
([ADR-124](../decisions.d/ADR-124.md)) also moved 34 decisions from Proposed to Active, so the
census's statuses are stale. A rerun of the census scripts on the current
record would update both; until then its figures hold as of 2026-11-20.

## Note of 2026-11-21: anthology-candidate was not redefined

The owner, on pull request 582: "the flag didn't change meaning, visiting these is the responsibility of processes on the anthology to consider if they want to add these candidates or not. pretty sure no action is required on Nucleation's end." The audit had classed [ADR-048](../decisions.d/ADR-048.md)'s rewording of the flag's blurb as a redefinition in place that reached none of its 237 entries. The flag records what [ADR-005](../decisions.d/ADR-005.md) made it record, that someone judged the anthology may want the work. [ADR-048](../decisions.d/ADR-048.md) changed what that implies about the work's filing here, not what the flag records. So no carry-through was needed, and the audit has no redefinition in place. [CLAIM-791](../claims.d/CLAIM-791.md) is corrected to match (version 2). The counts are unchanged; only the classification of one row moved.
