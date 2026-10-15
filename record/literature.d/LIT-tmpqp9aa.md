---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' arXiv preprint (arXiv cs/0204046v1,
  arxiv.org/pdf/cs/0204046v1), which is the full version of which the PODS 2001
  paper is the extended abstract; neither the PODS text nor the JCSS 2003 journal
  text was obtained (both returned 403), so the theorems read are the full version's
  and the preprint's Table 1, which halves the random-access term the theorems state,
  could not be checked against the journal. Worth reading as the source of the threshold
  algorithm's guarantee: for top-k retrieval under any monotone combining function
  from m lists each sorted by one attribute, TA is within m + m(m−1)c_R/c_S of every
  correct algorithm that makes no wild guesses, on every database, and that ratio
  is best possible when the function is strict (conjunction-like). For [CLAIM-310](../claims.d/CLAIM-310.md)
  and [THEORY-358](../theory.d/THEORY-358.md) it shows that a query on one attribute costs about k accesses whatever
  the collection's size, while a conjunction whose distractors each carry one of
  the target's two features is the paper's own counterexample (Example 6.3, Theorem
  6.4), costing about half the objects for any algorithm; Fagin's sublinear N^((m−1)/m)k^(1/m)
  holds only when the lists' orderings are independent, which Treisman's displays
  are built not to be. It says nothing about search times, the 1:2 present/absent
  ratio or whether vision reads sorted lists. For [QUESTION-114](../questions.d/QUESTION-114.md) it prices querying
  a given set of single-attribute orders, with no build, upkeep or space cost.
title: Optimal Aggregation Algorithms for Middleware
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: PODS 2001. Crossref gives May
    2001 only, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the title and authors found nothing. Read the same day (NOTE-tmpzuj15).
tags:
- databases
- information-retrieval
date: '2026-10-15'
published: '2001-05-01'
doi: 10.1145/375551.375567
first_author: Fagin
keywords: []
implementations: []
summary: >-
  Fagin et al. (2001), PODS 2001. Given m lists of the same N objects, each sorted
  by one attribute's grade, and a monotone function combining the grades, the threshold
  algorithm (TA) reads the lists in parallel, random-accesses each newly seen object's
  other grades, and stops once k seen objects score at least the combined score
  of the last grades read. It is correct for every monotone combining function,
  needs constant buffers, and is instance optimal among correct algorithms that
  make no "wild guesses": on every database its cost is within a constant factor
  of any such algorithm's, the factor being m + m(m−1)c_R/c_S, which is best possible
  when the combining function is strict (conjunction-like). Without the no-wild-guesses
  restriction no algorithm is instance optimal, and the counterexample is a two-list
  conjunction whose target sits in the middle of both lists, which any algorithm
  must search linearly. Fagin's Algorithm's sublinear cost O(N^((m−1)/m) k^(1/m))
  is cited from Fagin, not proved here, and holds only when the lists' orderings
  are probabilistically independent. The model prices queries over a given set of
  single-attribute sorted lists. It does not price building or keeping the lists,
  choosing an arrangement, or any computation beyond accesses.
---

# LIT-tmpqp9aa: Optimal Aggregation Algorithms for Middleware

Fagin, R., Lotem, A. and Naor, M. (2001). Optimal aggregation algorithms for middleware. In *Proc. PODS 2001*, pp. 102–113. DOI 10.1145/375551.375567. Journal version: *Journal of Computer and System Sciences* 66(4), 614–656 (2003), DOI 10.1016/S0022-0000(03)00026-6

## Key takeaways

Read in full ([NOTE-tmpzuj15](../notes.d/NOTE-tmpzuj15.md)). Given m lists of the same N objects, each sorted by one attribute's grade, and a monotone function combining the grades, the threshold algorithm (TA) reads the lists in parallel, random-accesses each newly seen object's other grades, and stops once k seen objects score at least the combined score of the last grades read. It is correct for every monotone combining function, needs constant buffers, and is instance optimal among correct algorithms that make no "wild guesses": on every database its cost is within a constant factor of any such algorithm's, the factor being m + m(m−1)c_R/c_S, which is best possible when the combining function is strict (conjunction-like). Without the no-wild-guesses restriction no algorithm is instance optimal, and the counterexample is a two-list conjunction whose target sits in the middle of both lists, which any algorithm must search linearly. Fagin's Algorithm's sublinear cost O(N^((m−1)/m) k^(1/m)) is cited from Fagin, not proved here, and holds only when the lists' orderings are probabilistically independent. The model prices queries over a given set of single-attribute sorted lists. It does not price building or keeping the lists, choosing an arrangement, or any computation beyond accesses.

## Why this is here

[CLAIM-310](../claims.d/CLAIM-310.md) and [THEORY-358](../theory.d/THEORY-358.md) (Treisman and Gelade): the Threshold Algorithm finds the best objects under a monotone combined score from lists each sorted by one feature, and is instance-optimal against algorithms that make no wild guesses. A conjunctive query's cost depends on how the features co-occur, from about k accesses to about half the collection when they are anti-correlated, as in Treisman's conjunction displays. Read from the authors' full version.
