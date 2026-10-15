---
status: Active
status_note: >-
  read in full 2026-10-15 from a scan of the published STOC 1977 paper (pp. 77–90)
  hosted in the directory of UBC's course CPSC 504 (www.cs.ubc.ca/~laks/cpsc504/chandra-merlin-1977.pdf),
  because ACM's open-access PDF refused requests from this environment; key statements
  checked against page images, the OCR layer being poor. Worth reading as the source
  of the homomorphism criterion for conjunctive queries: two are equivalent iff
  homomorphisms run both ways between the queries read as small databases (Lemma
  13), every one has a minimal equivalent unique up to isomorphism (Theorem 12),
  and evaluating a conjunctive query with the query as input is NP-complete (Theorem
  7), as is recognizing a folding (Theorem 11) ([THEORY-tmpe404c](../theory.d/THEORY-tmpe404c.md)). It states equivalence,
  not containment, and does not state that containment is NP-complete; both are
  corollaries later work attributes to it. For [CLAIM-303](../claims.d/CLAIM-303.md) it gives the base procedure,
  and the worst-case cost, of deciding that a stored answer covers a new question,
  in the size of the two descriptions; it says nothing about prose arguments or
  typical cost.
title: Optimal Implementation of Conjunctive Queries in Relational Data Bases
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: STOC 1977. Crossref gives 1977
    for the item and 4 May 1977 as the symposium's start, which `published:` uses.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the title and authors found nothing. Read the same day (NOTE-tmp5wypo).
tags:
- databases
- logic
date: '2026-10-15'
published: '1977-05-04'
doi: 10.1145/800105.803397
first_author: Chandra
keywords: []
implementations: []
summary: >-
  Chandra and Merlin (1977), STOC 1977. Defines conjunctive queries (existentially
  quantified conjunctions of atoms, no equality, constants naming distinct elements)
  and proves that two are equivalent exactly when there are homomorphisms each way
  between their natural models (Lemma 13). Every conjunctive query has a minimal
  equivalent query, unique up to isomorphism, reached by folding (Theorem 12), and
  that minimal query yields an evaluation program within a constant factor of optimal
  in the paper's cost model (Theorem 16). The hardness results are that evaluating
  a boolean conjunctive query on a database is NP-complete when the query is part
  of the input (Theorem 7), and that deciding whether one query is a folding of
  another is NP-complete (Theorem 11). The paper does not state a containment theorem
  or the NP-completeness of containment or equivalence as such; both are standard
  corollaries of Lemma 13's proof and Theorem 11's construction, and later papers
  cite them to it.
---

# LIT-tmpkq8zv: Optimal Implementation of Conjunctive Queries in Relational Data Bases

Chandra, A. K. and Merlin, P. M. (1977). Optimal implementation of conjunctive queries in relational data bases. In *Proc. STOC 1977*, pp. 77–90. DOI 10.1145/800105.803397

## Key takeaways

Read in full ([NOTE-tmp5wypo](../notes.d/NOTE-tmp5wypo.md)). Defines conjunctive queries (existentially quantified conjunctions of atoms, no equality, constants naming distinct elements) and proves that two are equivalent exactly when there are homomorphisms each way between their natural models (Lemma 13). Every conjunctive query has a minimal equivalent query, unique up to isomorphism, reached by folding (Theorem 12), and that minimal query yields an evaluation program within a constant factor of optimal in the paper's cost model (Theorem 16). The hardness results are that evaluating a boolean conjunctive query on a database is NP-complete when the query is part of the input (Theorem 7), and that deciding whether one query is a folding of another is NP-complete (Theorem 11). The paper does not state a containment theorem or the NP-completeness of containment or equivalence as such; both are standard corollaries of Lemma 13's proof and Theorem 11's construction, and later papers cite them to it.

## Why this is here

The equivalence result underneath [LIT-tmp3l2ha](LIT-tmp3l2ha.md): two conjunctive queries are equivalent exactly when each maps homomorphically into the other, and every query has a unique minimal equivalent. That containment and equivalence are NP-complete is the corollary later work attributes to it; the paper does not state it.
