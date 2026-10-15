---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' 25-page version on Stanford InfoLab's
  papers server (infolab.stanford.edu/pub/papers/cube.ps, TeX run of 8 January 1996),
  not the SIGMOD typesetting, which the ACM Digital Library refused (403); the two
  were not compared. Worth reading as the standard source on choosing which precomputed
  answers to store when each query is answered from its cheapest stored ancestor:
  the lattice of group-by views, the linear cost model (rows of the ancestor scanned),
  NP-completeness, and a greedy rule whose total benefit, the saving against storing
  the base view alone, is at least 1 − ((k−1)/k)^k ≥ (e−1)/e ≈ 63% of the optimum
  for a budget of k views, tight, unchanged with fixed query frequencies, and only
  0.63 − f under a space budget when no view exceeds a fraction f of it. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md)
  and [QUESTION-095](../questions.d/QUESTION-095.md) it shows the precomputed-answer term the four earlier readings
  lacked, with a stored answer's value counted over every query it serves and marginal
  on what is already stored (sharpening [CLAIM-303](../claims.d/CLAIM-303.md)'s break-even); it does not price
  build cost (space is a proxy), upkeep or staleness (the data are static and derived
  answers exact), timing or deadlines, uncertain workloads, or the medium of retrieval,
  so it is a model of the speed bugs only in naming the category, an analogy with
  one usable term for filed arguments, silent on the bias of reused inferences,
  and not about LEGO bins.
title: Implementing data cubes efficiently
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: SIGMOD '96,
    pp. 205–216; Crossref gives 1996 only. The conference ran 4–6 June 1996, and
    `published:` uses its first day. Not held in the Anthology of the SOTA: a grep
    of its record/ (clone of 2026-10-15, commit d1573d2) for the title found nothing.
    Read the same day (NOTE-tmpb6yin).
tags:
- databases
- operations-research
date: '2026-10-15'
published: '1996-06-04'
doi: 10.1145/233269.233333
first_author: Harinarayan
keywords: []
implementations: []
summary: >-
  Harinarayan, Rajaraman and Ullman (1996), SIGMOD '96. Treats a data cube's group-by
  queries as a lattice in which a query can be answered from any stored ancestor,
  prices a query at the number of rows of the smallest materialized ancestor, and
  chooses which views to precompute. Choosing k views to maximize the total reduction
  in query cost (the "benefit") is NP-complete; a greedy rule that adds the view
  of largest marginal benefit gets at least 1 − ((k−1)/k)^k ≥ (e−1)/e ≈ 63% of the
  optimal benefit, a bound that is tight, holds unchanged with query-frequency weights,
  and weakens to 0.63 − f under a space budget when no view takes more than a fraction
  f of it. The cost of building views is represented only by their size, maintenance
  and updates are not modelled, the data are static, and the bound is on benefit,
  not on query cost. On TPC-D data the greedy order reaches nearly the minimum total
  query time with five views and barely more space than the base view.
---

# LIT-tmptn63k: Implementing data cubes efficiently

Harinarayan, V., Rajaraman, A. and Ullman, J. D. (1996). Implementing data cubes efficiently. In *Proceedings of the 1996 ACM SIGMOD International Conference on Management of Data*, pp. 205–216. DOI 10.1145/233269.233333

## Key takeaways

Read in full ([NOTE-tmpb6yin](../notes.d/NOTE-tmpb6yin.md)). Treats a data cube's group-by queries as a lattice in which a query can be answered from any stored ancestor, prices a query at the number of rows of the smallest materialized ancestor, and chooses which views to precompute. Choosing k views to maximize the total reduction in query cost (the "benefit") is NP-complete; a greedy rule that adds the view of largest marginal benefit gets at least 1 − ((k−1)/k)^k ≥ (e−1)/e ≈ 63% of the optimal benefit, a bound that is tight, holds unchanged with query-frequency weights, and weakens to 0.63 − f under a space budget when no view takes more than a fraction f of it. The cost of building views is represented only by their size, maintenance and updates are not modelled, the data are static, and the bound is on benefit, not on query cost. On TPC-D data the greedy order reaches nearly the minimum total query time with five views and barely more space than the base view.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): the four works on physical design already read choose ways of reaching stored data. None covers a precomputed answer, which is the cockpit's case (speeds computed before landing and left as bugs). This paper chooses which answers to precompute.
