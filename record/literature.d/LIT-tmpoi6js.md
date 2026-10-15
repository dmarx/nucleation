---
status: Active
status_note: >-
  read in full 2026-10-15 from the ACM's typeset PDF of the SIGMOD '93 extended
  abstract (pp. 157–166), as posted on Columbia University's Ph.D. candidacy exam
  reading list in database systems (www.cs.columbia.edu/~gravano/Qual/Papers/13%20-%20Maintaining%20Views%20Incrementally.pdf);
  a scan with an OCR layer, so definitions and theorems were read from page images.
  The full version with the proofs (AT&T Bell Labs TR 921214-19-TM, 1992) was not
  found. Worth reading as the source of the two standard incremental view maintenance
  algorithms: counting, which stores one derivation count per derived tuple and
  is stated correct for nonrecursive views with stratified negation and aggregation
  under set or duplicate semantics ([THEORY-tmp2ber8](../theory.d/THEORY-tmp2ber8.md)), and DRed, which for recursive
  views under set semantics overdeletes, rederives what still has a derivation and
  then inserts, and is stated to give exactly what the new base derives ([THEORY-tmptzp8y](../theory.d/THEORY-tmptzp8y.md)).
  The theorems are stated without proof here, and cost claims are argued, not measured.
  For [QUESTION-105](../questions.d/QUESTION-105.md) it shows that, for revisions given as changes to base facts under
  a fixed program, the retained state can be a count per conclusion when support
  is acyclic and nothing beyond the materialization when it is not, with support
  rechecked at revision time; neither is provenance or a record of defeated alternatives.
  For [CLAIM-303](../claims.d/CLAIM-303.md) it shows the dependency-tracking cost can sit at derivation time
  (counting) or at revision time (DRed), without measuring either, and that a view
  kept this way never goes stale.
title: Maintaining Views Incrementally
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: SIGMOD 1993. Crossref gives
    June 1993 only, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the title and authors found nothing. Read the same day (NOTE-tmpgv5ap).
tags:
- databases
- logic
date: '2026-10-15'
published: '1993-06-01'
doi: 10.1145/170035.170066
first_author: Gupta
keywords: []
implementations: []
summary: >-
  Gupta et al. (1993), SIGMOD 1993. Two algorithms compute the changes to a stored
  derived relation (a view) from changes to the base relations, without recomputing
  it. Counting stores, for each derived tuple, the number of its derivations and
  propagates signed counts through delta rules stratum by stratum; it is stated
  correct for nonrecursive Datalog or SQL views with stratified negation and aggregation,
  under set or duplicate semantics, and is argued to cost little beyond evaluating
  the view. DRed (delete and rederive), for recursive views under set semantics
  only, deletes an overestimate of what a deletion invalidates, puts back those
  tuples that still have a derivation from what remains, then adds what insertions
  derive; it is stated to yield exactly the tuples derivable from the new base.
  The paper is an extended abstract: the theorems are stated without proof (proofs
  are referred to a 1992 AT&T report), cost claims are argued, not measured, and
  there are no experiments.
---

# LIT-tmpoi6js: Maintaining Views Incrementally

Gupta, A., Mumick, I. S. and Subrahmanian, V. S. (1993). Maintaining views incrementally. In *Proc. ACM SIGMOD 1993*, pp. 157–166. DOI 10.1145/170035.170066

## Key takeaways

Read in full ([NOTE-tmpgv5ap](../notes.d/NOTE-tmpgv5ap.md)). Two algorithms compute the changes to a stored derived relation (a view) from changes to the base relations, without recomputing it. Counting stores, for each derived tuple, the number of its derivations and propagates signed counts through delta rules stratum by stratum; it is stated correct for nonrecursive Datalog or SQL views with stratified negation and aggregation, under set or duplicate semantics, and is argued to cost little beyond evaluating the view. DRed (delete and rederive), for recursive views under set semantics only, deletes an overestimate of what a deletion invalidates, puts back those tuples that still have a derivation from what remains, then adds what insertions derive; it is stated to yield exactly the tuples derivable from the new base. The paper is an extended abstract: the theorems are stated without proof (proofs are referred to a 1992 AT&T report), cost claims are argued, not measured, and there are no experiments.

## Why this is here

[QUESTION-105](../questions.d/QUESTION-105.md) and [CLAIM-303](../claims.d/CLAIM-303.md)'s dependency tracking: counting keeps one derivation count per derived result for nonrecursive views, and delete-and-rederive handles recursive views under set semantics, keeping what has another derivation. The theorems are stated without proof and the costs are argued, not measured.
