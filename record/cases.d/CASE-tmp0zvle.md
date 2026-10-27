---
status: Active
title: 'How the record''s grammar grows: after its scaffold, this record filed documents on all 32 days, added vocabulary terms on 18, fields or relations to schemes on 8, whole vocabularies on 3, schemes on 1 and a remote project on 1, so the owner''s ordering of levels holds; but each refinement came in the same pull request as the documents that needed it and, nine times in ten, an ADR, so the levels are rarer events of one loop of work, not slower processes of their own, and the grammar''s rates fell while filing rose'
version: 1
standing: documented
kind: executed-study
tags:
- design-rationale
- complex-systems
date: '2026-10-27'
variant_of:
- CASE-tmpqou64
illustrates:
- CLAIM-tmpmx2ql
- CLAIM-tmpl228b
line: nucleating-argument
summary: >-
  Run on 2026-10-27 at the owner's direction, after [CASE-tmpqou64](CASE-tmpqou64.md): "some of
  the most important rates are when and how schema refinement happens",
  with the ordering documents, vocabularies, scheme fields, schemes,
  projects. scratch/formal/schema_rates.py reads every change to luria.yaml
  in this record, in luria's own and in strata-g's. The ordering holds by
  days with an event. How the refinement happens: on demand, by decision,
  and nested, the rarer level arriving with the commoner ones in one pull
  request.
---
<!-- inactive-ok-file: CLAIM-tmpmx2ql CLAIM-tmpl228b — Proposed; the claims the measurement bears on -->

# CASE-tmp0zvle: How the record's grammar grows: after its scaffold, this record filed documents on all 32 days, added vocabulary terms on 18, fields or relations to schemes on 8, whole vocabularies on 3, schemes on 1 and a remote project on 1, so the owner's ordering of levels holds; but each refinement came in the same pull request as the documents that needed it and, nine times in ten, an ADR, so the levels are rarer events of one loop of work, not slower processes of their own, and the grammar's rates fell while filing rose

## The case

[CASE-tmpqou64](CASE-tmpqou64.md) measured how often a declared thing is revised. The owner
pointed past it, the same day: "some of the most important rates are when and
how schema refinement happens. authoring documents happens faster than
vocabularies expand, which happens faster than the fields that comprise a
scheme are added/modified, which happens faster than new SCHEMEs are
specified, which happens faster than new projects are spun up". The last
level is not visible inside one record, "although you can weakly guess at it
from the rate at which codes to remote schemes are defined".

**Method.** scratch/formal/schema_rates.py compares each commit's luria.yaml
with its parent's and counts declarations at each level:

- a vocabulary term;
- a vocabulary;
- a member of a scheme, which is a field or a relation;
- a scheme;
- a remote, a project the record can cite.

It counts as documents the files authored commits add to a scheme's
directory. Each event is assigned to its unit of work: the pull request where
the commit can be tied to one, otherwise the commit. For each unit it notes
whether documents were filed and whether an ADR was added, and for a new term,
whether a document changed in the same unit carries the term. The scaffold
commit, which declares the starting grammar at once, is left out of the
rates below.

**Rates in nucleation**, 2026-09-25 to 2026-10-27 (32 days):

| level | added | per day | days with one | first half / second half |
|---|---|---|---|---|
| document | 5030 | 158 | 32 | 2271 / 2759 |
| vocabulary term | 106 | 3.3 | 18 | 82 / 24 |
| scheme member (field or relation) | 79 | 2.5 | 8 | 67 / 12 |
| vocabulary | 8 | 0.25 | 3 | 6 / 2 |
| scheme | 5 | 0.16 | 1 | 5 / 0 |
| remote project | 1 | 0.03 | 1 | 1 / 0 |

Besides the additions, members were redeclared 26 times on 9 days, and terms
were reworded 10 times and removed twice.

**How the refinements came in**, against a baseline of every pull request
that touched the record (296):

| units that added a… | filing documents | adding an ADR | also adding a term |
|---|---|---|---|
| any pull request (baseline) | 86% | 16% | |
| term (35) | 100% | 91% | |
| member (9) | 100% | 89% | 67% |
| vocabulary (4) | 100% | 75% | 100% |
| scheme (2) | 100% | 100% | 100% |

Of the 106 terms added after the scaffold, 94% appear in the frontmatter of
a document changed in the same unit. Commit subjects agree: "moral-psychology
joins the topics ([ADR-018](../decisions.d/ADR-018.md))", "[ADR-042](../decisions.d/ADR-042.md): a required kind field on CASE".

**Projects.** Two weak signals:

- **Remotes.** This record's remotes name three projects: the anthology and
  luria from the scaffold, and Mathematics of Meaning from 2026-10-11.
- **First commits.** The records in this session were begun on these dates:
  strata-g on 2026-06-24, luria (extracted from strata-g) on 2026-08-03, and
  nucleation on 2026-09-07. The anthology's and Mathematics of Meaning's
  start dates were not read.

That gives about five projects in four months, against five schemes added
here in one day.

**The other two records.** Their grammars are small (ADR and DP only).
Since its luria.yaml was written, luria added two terms and four members,
and strata-g added nothing. They filed 33 and 10 ADRs and principles over
the same weeks. Both moved their grammars onto luria.yaml whole, so its
history does not show how their grammars were built.

**Limits.**

- One month.
- One record with a grammar of any size.
- Units are pull requests, and a large pull request is more likely to carry
  both a term and an ADR. The baseline is not matched for size, so "by
  decision" rests on the 91% against 16% and on the commit subjects, not on
  a matched comparison.
- Five schemes on one day and one remote are single events, so their rates
  are not estimates.

## What it shows

- **The owner's ordering holds by frequency.** By days with an event:
  documents 32, terms 18, members 8, schemes 1, remotes 1 here, and projects
  about one a month across the owner's records. Whole vocabularies (3 days)
  fall between members and schemes. A term grows an existing vocabulary,
  while a new vocabulary arrives with the field that will hold it (44% of
  member units added one).
- **The levels are nested, not parallel.** Every unit that added a scheme
  also added members, a vocabulary and terms. Two thirds of the units that
  added a member also added a term. A rarer refinement arrives with the
  commoner ones, in the same unit of work as the documents that needed it.
  It is triggered by those documents: 94% of new terms were used at once.
  It is also ratified there: nine in ten of those units added an ADR,
  against one in six of all units. So the slow levels are not slower
  processes running on their own clocks. They are rarer outcomes of one
  loop, in which filing a document can meet a misfit, and the misfit is
  fixed by a decision at the lowest level that holds it.
- **The separation widens.** From the first half of the month to the
  second, filing rose by a fifth, term additions fell to under a third,
  member additions to under a fifth, and schemes from five to none. The
  ratio of documents filed to terms added went from about 28 to about 115.
  The grammar is settling while the record grows.

## What would change it

A record begun with a small grammar and grown by use, measured over a longer
period, would show whether the falling rates are settling or only the end of
a founding period. So would a second large record, such as the anthology. A
size-matched baseline would test "by decision".
