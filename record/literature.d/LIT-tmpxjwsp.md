---
status: Active
status_note: >-
  read in full 2026-10-15 from the conference version as published, the PDF of SIGMOD
  2000 pp. 117–128 served by ACM SIGMOD's SIGMOD Record site for the June 2000 proceedings
  issue (sigmodrecord.org/publications/sigmodRecord/0006/pdfs/Synchronizing%20a%20Database%20to%20Improve%20Freshness.pdf),
  with the proofs it defers checked in the authors' 1999 Stanford technical report
  as hosted on a KTH course page. Worth reading as the standard definition of a
  copy's freshness and age under Poisson change, and for the result that, under
  a fixed refresh budget, refreshing every item equally beats refreshing in proportion
  to change rate for any distribution of rates, while the freshness-optimal allocation
  gives nothing to items that change too fast to follow. For [QUESTION-114](../questions.d/QUESTION-114.md) it is
  the first reading that prices staleness instead of forbidding it, but as an objective
  under a fixed budget, with no reads, no query savings and no build cost, so it
  supplies the staleness term and not the joint model; for [CLAIM-303](../claims.d/CLAIM-303.md) it models the
  re-checking term per unit time and by rate of change, not per use, and does not
  price the cost of a stale use.
title: Synchronizing a Database to Improve Freshness
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: SIGMOD 2000. Crossref gives
    16 May 2000 for the proceedings. Not held in the Anthology of the SOTA: a grep
    of its record/ (clone of 2026-10-15, commit d1573d2) for the title and authors
    found nothing. Read the same day (NOTE-tmp4d27w).
tags:
- databases
- information-retrieval
- operations-research
date: '2026-10-15'
published: '2000-05-16'
doi: 10.1145/342009.335391
first_author: Cho
keywords: []
implementations: []
summary: >-
  Cho and Garcia-Molina (2000), SIGMOD 2000. For a local copy of N items, each changing
  as an independent Poisson process with a known rate and refreshed at fixed intervals
  under a fixed total refresh rate, refreshing every item equally keeps the copy
  fresher and younger on average than refreshing in proportion to change rate, under
  any distribution of rates (proved in the technical report by convexity). The freshness-optimal
  allocation is neither: it rises and then falls with change rate, and gives no
  refresh at all to items that change too fast for the budget, while the age-optimal
  allocation rises slowly with change rate. On estimates from 270 web sites, proportional,
  uniform and optimal refresh give freshness 0.12, 0.57 and 0.62. Every item matters
  equally, staleness is a time average with no access or query model, the refresh
  budget is fixed rather than priced, and refresh, change and its detection are
  free of any other cost.
---

# LIT-tmpxjwsp: Synchronizing a Database to Improve Freshness

Cho, J. and Garcia-Molina, H. (2000). Synchronizing a database to improve freshness. In *Proc. ACM SIGMOD 2000*, pp. 117–128. DOI 10.1145/342009.335391

## Key takeaways

Read in full ([NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md)). For a local copy of N items, each changing as an independent Poisson process with a known rate and refreshed at fixed intervals under a fixed total refresh rate, refreshing every item equally keeps the copy fresher and younger on average than refreshing in proportion to change rate, under any distribution of rates (proved in the technical report by convexity). The freshness-optimal allocation is neither: it rises and then falls with change rate, and gives no refresh at all to items that change too fast for the budget, while the age-optimal allocation rises slowly with change rate. On estimates from 270 web sites, proportional, uniform and optimal refresh give freshness 0.12, 0.57 and 0.62. Every item matters equally, staleness is a time average with no access or query model, the refresh budget is fixed rather than priced, and refresh, change and its detection are free of any other cost.

## Why this is here

[QUESTION-114](../questions.d/QUESTION-114.md) lacked a price for staleness. This is the first reading that prices it rather than forbidding it, as freshness or age under a fixed refresh budget. Uniform refresh beats refresh in proportion to change rate, but the optimum is neither: it rises then falls with change rate for freshness, and items changing too fast get no refresh at all. Staleness is the objective here, not a cost weighed against reads or build, so it supplies the term, not the joint model.
