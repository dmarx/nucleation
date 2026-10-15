---
status: Active
status_note: >-
  read in full 2026-10-15 from the author's PostScript copy on the Stanford InfoLab
  papers server (infolab.stanford.edu/pub/papers/SelectionViews.ps, 15 pp., dated
  March 1997, linked from the warehousing project's publication page; Unpaywall
  and OpenAlex report the DOI closed). Worth reading as the general statement of
  view selection: AND-OR view graphs with query and update frequencies, and an objective
  of frequency-weighted query cost plus update-frequency-weighted maintenance cost
  under a space budget, with greedy guarantees of 1 − 1/e of the optimal benefit
  when space may overrun. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it gives the joint objective in
  form: reuse against per-update upkeep under capacity. It charges no build cost,
  leaves the maintenance cost abstract, and models only keeping views consistent,
  not tolerating or acting on stale ones. Its guarantees with maintenance cost hold
  only for AND view graphs in which every view is queried more often than it is
  updated. For the data cube of [LIT-tmptn63k](LIT-tmptn63k.md) it assumes no updates, so it does not
  add upkeep to that problem. That came in Gupta and Mumick's maintenance-time-constrained
  follow-up (ICDT 1999), read afterwards as LIT-tmpppd6p.
title: Selection of views to materialize in a data warehouse
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: ICDT '97,
    LNCS 1186, pp. 98–112; Crossref gives 1997 only. ICDT '97 opened in Delphi on
    8 January 1997, which `published:` uses. Not held in the Anthology of the SOTA:
    a grep of its record/ (clone of 2026-10-15, commit d1573d2) for the title found
    nothing. Read the same day (NOTE-tmp4p0w6).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '1997-01-08'
doi: 10.1007/3-540-62222-5_39
first_author: Gupta
keywords: []
implementations: []
summary: >-
  Gupta (1997), ICDT '97. Gupta states view selection on general AND-OR view graphs
  as minimizing frequency-weighted query cost plus update-frequency-weighted maintenance
  cost under a space budget. He proves greedy guarantees of 1 − 1/e (about 63%)
  of the optimal benefit, with the budget overrun by one view or up to double, but
  almost all of them assume no updates. Maintenance cost enters exactly one theorem:
  AND view graphs (each view has one way of being computed) in which every view
  is queried more often than it is updated. For OR view graphs, which include Harinarayan,
  Rajaraman and Ullman's data cube, the paper sets update costs aside outright,
  so it does not add upkeep to that problem. Maintenance is an abstract per-update
  charge for keeping a view consistent. Nothing prices building a view, tolerated
  staleness or deferred refresh, and there are no experiments.
---

# LIT-tmpn0tsb: Selection of views to materialize in a data warehouse

Gupta, H. (1997). Selection of views to materialize in a data warehouse. In F. Afrati and P. Kolaitis (eds.), *Database Theory — ICDT '97*, LNCS 1186, pp. 98–112. Springer. DOI 10.1007/3-540-62222-5_39

## Key takeaways

Read in full ([NOTE-tmp4p0w6](../notes.d/NOTE-tmp4p0w6.md)), from Gupta's own March 1997 preprint. Gupta states view selection on general AND-OR view graphs as minimizing frequency-weighted query cost plus update-frequency-weighted maintenance cost under a space budget. He proves greedy guarantees of 1 − 1/e (about 63%) of the optimal benefit, with the budget overrun by one view or up to double, but almost all of them assume no updates. Maintenance cost enters exactly one theorem: AND view graphs (each view has one way of being computed) in which every view is queried more often than it is updated. For OR view graphs, which include Harinarayan, Rajaraman and Ullman's data cube, the paper sets update costs aside outright, so it does not add upkeep to that problem. Maintenance is an abstract per-update charge for keeping a view consistent. Nothing prices building a view, tolerated staleness or deferred refresh, and there are no experiments.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): Harinarayan et al. ([LIT-tmptn63k](LIT-tmptn63k.md)) price no upkeep. The question needs the cost of keeping a precomputed answer current, which is staleness's price.
