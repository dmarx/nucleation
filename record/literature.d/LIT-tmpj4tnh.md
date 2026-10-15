---
status: Active
status_note: >-
  read in full 2026-10-15 from the author's preprint as presented at the 1977 Toulouse
  workshop, University of British Columbia Department of Computer Science Technical
  Report 77-16 (October 1977), served by UBC's technical-report archive (www.cs.ubc.ca/sites/default/files/tr/1977/TR-77-16.pdf);
  the published Plenum chapter (pp. 55–76) is closed (Unpaywall and OpenAlex: closed;
  Semantic Scholar: no open PDF) and was not seen. Worth reading as the source of
  the open/closed-world distinction and of the closed-world assumption as a formal
  object: add the negation of every ground atom the database does not entail, a
  convention Reiter says "presumes total knowledge about the domain". It shows that
  closed-world evaluation of any existential query reduces to open-world evaluation
  of atomic queries when the database stays consistent under the assumption, that
  consistent Horn and all definite databases do, and that a disjunctive database
  such as Pa ∨ Pb does not. For [CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md) it supplies the definition and the
  completeness assumption (stated, not proved as a soundness condition; a formal
  soundness result would be Clark's), and nothing about search time: non-entailment
  is a fixed relation, so "a closed-world assumption taken on a time bound" is the
  record's extension. It also cuts against reading [CASE-085](../cases.d/CASE-085.md) as a closed-world inference:
  a medic who knows the item is stocked holds a disjunction over compartments, Reiter's
  Example 5.1, where the assumption is inconsistent.
title: On Closed World Data Bases
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: a chapter
    in Gallaire and Minker (eds.), Logic and Data Bases (Plenum, 1978); Crossref
    gives the year only, so `published:` is the first of January. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the author and the title found nothing. Read the same day (NOTE-tmpjk9xt).
tags:
- logic
date: '2026-10-15'
published: '1978-01-01'
doi: 10.1007/978-1-4684-3384-5_3
first_author: Reiter
keywords: []
implementations: []
summary: >-
  Reiter defines the closed-world assumption (CWA) for a function-free first-order
  database as reasoning from DB together with the negation of every ground atom
  that DB does not entail, and contrasts it with the open-world assumption (OWA),
  under which only what DB entails is an answer. He shows that, when DB with these
  added negations is consistent, closed-world evaluation of any existential query
  reduces to ordinary (open-world) evaluation of atomic queries combined by union,
  intersection, difference and projection, so the negations never need to be listed.
  The CWA can make a consistent database inconsistent (Pa ∨ Pb yields ¬Pa and ¬Pb);
  consistent Horn databases, and all definite databases, stay consistent. Nothing
  in the paper concerns how long a search takes: non-entailment is a fixed logical
  relation, and the CWA's justification is stated as an assumption of total knowledge
  of the domain, not proved as a soundness condition.
supports:
- CLAIM-tmp3ejtf
---

# LIT-tmpj4tnh: On Closed World Data Bases

Reiter, R. (1978). On closed world data bases. In H. Gallaire and J. Minker (eds.), *Logic and Data Bases*, pp. 55–76. New York: Plenum. DOI 10.1007/978-1-4684-3384-5_3

## Key takeaways

Read in full ([NOTE-tmpjk9xt](../notes.d/NOTE-tmpjk9xt.md)), from Reiter's 1977 workshop report, not the printed chapter. Reiter defines the closed-world assumption (CWA) for a function-free first-order database as reasoning from DB together with the negation of every ground atom that DB does not entail, and contrasts it with the open-world assumption (OWA), under which only what DB entails is an answer. He shows that, when DB with these added negations is consistent, closed-world evaluation of any existential query reduces to ordinary (open-world) evaluation of atomic queries combined by union, intersection, difference and projection, so the negations never need to be listed. The CWA can make a consistent database inconsistent (Pa ∨ Pb yields ¬Pa and ¬Pb); consistent Horn databases, and all definite databases, stay consistent. Nothing in the paper concerns how long a search takes: non-entailment is a fixed logical relation, and the CWA's justification is stated as an assumption of total knowledge of the domain, not proved as a soundness condition.

## Why this is here

[CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md): the medic's "If I can't find it, it isn't there" ([CASE-085](../cases.d/CASE-085.md)) acts
on a failed search as if it showed absence. This is the inference, and
its soundness condition is the one [CLAIM-tmp3ejtf](../claims.d/CLAIM-tmp3ejtf.md) needs.
