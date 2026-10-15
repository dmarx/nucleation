---
status: Active
status_note: >-
  read in full 2026-10-15 from the scan SIGMOD serves openly on sigmodrecord.org
  (sigmodrecord.org/publications/sigmodRecord/8301/pdfs/984523.984530.pdf, linked
  from the January 1983 issue page), 4 pp., printed pages 72–75; the ACM Digital
  Library refused requests from this environment, and Unpaywall and OpenAlex list
  no open copy. Worth reading as the first proof that choosing secondary indexes
  for a known mix of queries and updates, to minimize average transaction cost,
  is NP-hard, by a half-page reduction from minimum set cover: attributes are the
  sets, queries the elements, and each index pays a fixed upkeep on updates. For
  [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it shows that the trade of upkeep against per-query savings
  under a known workload can be stated exactly and cannot be solved exactly in general,
  but only as the number of attributes and query types grows; storage, build cost
  and the file's own order are outside its model, and it does not mention Comer
  1978 ([LIT-tmpij5df](LIT-tmpij5df.md)), so it is the citation for workload-based hardness and says
  nothing about what Comer proved.
title: The optimal selection of secondary indices is NP-complete
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: ACM SIGMOD
    Record 13(2), pp. 72–75, January 1983, so `published:` is the first of the month.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15,
    commit d1573d2) for the title found nothing. Read the same day (NOTE-tmpxc25d).
tags:
- databases
- mathematics
date: '2026-10-15'
published: '1983-01-01'
doi: 10.1145/984523.984530
first_author: Piatetsky-Shapiro
keywords: []
implementations: []
summary: >-
  Piatetsky-Shapiro (1983), ACM SIGMOD Record 13(2). For one relation, a known mix
  of equality queries and updates, single-attribute secondary indexes, and a fixed
  upkeep charge per index on each update, choosing the index set that minimizes
  average transaction cost is NP-hard: minimum set cover reduces to it, each subset
  becoming an attribute and each element a query that any one of its attributes'
  indexes can answer. The paper calls the problem NP-complete but states only the
  optimization version, and the proof is a sketch of about half a page. Storage
  is not in the model; the only price of an index is upkeep on updates. A variant
  with off-line updates under an update-cost budget is asserted NP-complete without
  proof. The paper does not cite or discuss Comer 1978.
---

# LIT-tmpkl6wl: The optimal selection of secondary indices is NP-complete

Piatetsky-Shapiro, G. (1983). The optimal selection of secondary indices is NP-complete. *ACM SIGMOD Record* 13(2), 72–75. DOI 10.1145/984523.984530

## Key takeaways

Read in full ([NOTE-tmpxc25d](../notes.d/NOTE-tmpxc25d.md)). For one relation, a known mix of equality queries and updates, single-attribute secondary indexes, and a fixed upkeep charge per index on each update, choosing the index set that minimizes average transaction cost is NP-hard: minimum set cover reduces to it, each subset becoming an attribute and each element a query that any one of its attributes' indexes can answer. The paper calls the problem NP-complete but states only the optimization version, and the proof is a sketch of about half a page. Storage is not in the model; the only price of an index is upkeep on updates. A variant with off-line updates under an update-cost budget is asserted NP-complete without proof. The paper does not cite or discuss Comer 1978.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) cited Comer 1978 for "optimal index selection is NP-complete". Comer could not be obtained, and a secondary account says it proves something else. This paper is the candidate for the workload-based result.
