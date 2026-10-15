---
status: Active
status_note: >-
  read in full 2026-10-15 from the publisher's PDF (VLDB Journal 10: 270–294) hosted
  on Columbia's database Ph.D. candidacy-exam reading list (www.cs.columbia.edu/~gravano/Qual/Papers/halevy01.pdf);
  reference list scanned, not read. Worth reading as the map of answering queries
  from stored views: equivalent rewritings for optimization against maximally-contained
  rewritings and certain answers for incomplete sources, with the complexity results
  of the field as it reports them ([THEORY-tmpg43pg](../theory.d/THEORY-tmpg43pg.md)). For [CLAIM-303](../claims.d/CLAIM-303.md) and [CLAIM-308](../claims.d/CLAIM-308.md) it
  shows that recognizing reuse is graded: certifying that stored answers settle
  a question exactly is NP-complete in the size of the question and definitions,
  extracting what they do give is polynomial (inverse rules) without saying whether
  it is all, and finding all certain answers from the stored contents is co-NP-hard
  in their size under the closed-world assumption. For [QUESTION-114](../questions.d/QUESTION-114.md) it puts this
  recognition step upstream of view selection, which it names as the open problem.
  Its results on certain answers and inverse rules are reported from papers the
  record has not read.
title: 'Answering Queries Using Views: A Survey'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: VLDB Journal 2001. Crossref
    gives December 2001 only, so `published:` is the first of the month. Not held
    in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit
    d1573d2) for the title and authors found nothing. Read the same day (NOTE-tmpxpujb).
tags:
- databases
- logic
date: '2026-10-15'
published: '2001-12-01'
doi: 10.1007/s007780100054
first_author: Halevy
keywords: []
implementations: []
summary: >-
  Halevy (2001), VLDB Journal 2001. A survey that separates two problems of answering
  queries from stored views: finding an equivalent rewriting, which query optimization
  needs, and finding a maximally-contained rewriting or all certain answers, which
  data integration needs when sources are incomplete. Its theoretical findings,
  mostly reported from other papers: an equivalent conjunctive rewriting exists
  only if one exists no longer than the query, so finding one is NP-complete in
  the size of the query and view definitions, and checking a candidate is itself
  NP-complete; the inverse-rules algorithm builds the maximally-contained rewriting,
  as a possibly recursive datalog program, in time polynomial in the query and views;
  and finding all certain answers is polynomial in the size of the stored data in
  many open-world cases, but co-NP-hard in that size under the closed-world assumption
  even for conjunctive views and queries, or open-world with union in the views
  or ≠ in the query. Choosing which views to store is left as the next problem;
  cost-based choice among rewritings is described for practical optimizers, without
  guarantees.
---

# LIT-tmpu418n: Answering Queries Using Views: A Survey

Halevy, A. Y. (2001). Answering queries using views: A survey. *The VLDB Journal* 10(4), 270–294. DOI 10.1007/s007780100054

## Key takeaways

Read in full ([NOTE-tmpxpujb](../notes.d/NOTE-tmpxpujb.md)). A survey that separates two problems of answering queries from stored views: finding an equivalent rewriting, which query optimization needs, and finding a maximally-contained rewriting or all certain answers, which data integration needs when sources are incomplete. Its theoretical findings, mostly reported from other papers: an equivalent conjunctive rewriting exists only if one exists no longer than the query, so finding one is NP-complete in the size of the query and view definitions, and checking a candidate is itself NP-complete; the inverse-rules algorithm builds the maximally-contained rewriting, as a possibly recursive datalog program, in time polynomial in the query and views; and finding all certain answers is polynomial in the size of the stored data in many open-world cases, but co-NP-hard in that size under the closed-world assumption even for conjunctive views and queries, or open-world with union in the views or ≠ in the query. Choosing which views to store is left as the next problem; cost-based choice among rewritings is described for practical optimizers, without guarantees.

## Why this is here

The survey of the problem [LIT-tmp3l2ha](LIT-tmp3l2ha.md) opened, for [CLAIM-303](../claims.d/CLAIM-303.md): reuse is graded. Certifying an exact rewriting is hard, while a maximally contained rewriting can be built in polynomial time; certain answers depend on the open- or closed-world assumption.
