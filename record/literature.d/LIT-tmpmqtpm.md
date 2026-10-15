---
status: Active
status_note: >-
  read in full 2026-10-15 from the paper as published in the CIDR 2007 proceedings
  (cidrdb.org/cidr2007/papers/cidr07p07.pdf, which redirects to www.cidrdb.org;
  printed pp. 68–78, CC BY 2.5). Worth reading as the founding account of indexing
  by query: each range select partitions in place the part of a column copy it had
  to scan, records the new boundaries in an AVL tree, and so makes later queries
  touch only the pieces at the edges of their range. On 10^7 values under uniformly
  random ranges the first cracking query costs 0.38 s against 0.27 s for a scan
  and about 3.3 s for sort-then-search, and upfront sorting overtakes cracking only
  after about 10^5 queries. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it shows sorting as amortized
  search in a literal sense, with a measured break-even, but gives no cost model
  and no rule for when a reorganization is worth making; the claim that only ranges
  of interest get organized is not tested, since every workload is uniform. For
  [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md) the analogy holds for organizing as a by-product of retrieval and
  fails on the mechanism: cracking splits everything it searched around an ordered
  key, and reorganizes on every query whatever the chance of reuse, where the case
  sets aside only the found brick, and only when it is rare and often used.
title: Database Cracking
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref (or the proceedings page)
    on 2026-10-15: CIDR 2007 has no DOI; the conference opened on 7 January 2007,
    which `published:` uses. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-15, commit d1573d2) for the authors and the title
    found nothing. Read the same day (NOTE-tmp6iazx).
tags:
- databases
date: '2026-10-15'
published: '2007-01-07'
url: https://cidrdb.org/cidr2007/papers/cidr07p07.pdf
first_author: Idreos
keywords: []
implementations: []
summary: >-
  Idreos, Kersten and Manegold (2007), CIDR. Database cracking builds an index as
  a by-product of answering range queries. Each select partitions, in place, the
  part of a copy of the column that the query had to touch, so that the qualifying
  values lie contiguously, and records the new boundaries in a small tree; later
  queries touch only the pieces at the edges of their range, so per-query cost falls
  as the column is split into more pieces. On a 10^7-value column under uniformly
  random range queries, the first cracking select costs 0.38 s against 0.27 s for
  a scan and about 3.3 s for sort-then-search, and cumulative cost stays below sorting's
  until about 10^5 queries, after which upfront sorting wins. The authors claim
  that only ranges of past interest get organized, but every experiment uses uniformly
  random ranges, so that claim is not measured; there is no cost model, no rule
  for when a reorganization is worth making, and updates, concurrency and out-of-memory
  data are left as open problems.
---

# LIT-tmpmqtpm: Database Cracking

Idreos, S., Kersten, M. L. and Manegold, S. (2007). Database cracking. In *Proceedings of the 3rd Biennial Conference on Innovative Data Systems Research (CIDR 2007)*, Asilomar. https://cidrdb.org/cidr2007/papers/cidr07p07.pdf

## Key takeaways

Read in full ([NOTE-tmp6iazx](../notes.d/NOTE-tmp6iazx.md)). Database cracking builds an index as a by-product of answering range queries. Each select partitions, in place, the part of a copy of the column that the query had to touch, so that the qualifying values lie contiguously, and records the new boundaries in a small tree; later queries touch only the pieces at the edges of their range, so per-query cost falls as the column is split into more pieces. On a 10^7-value column under uniformly random range queries, the first cracking select costs 0.38 s against 0.27 s for a scan and about 3.3 s for sort-then-search, and cumulative cost stays below sorting's until about 10^5 queries, after which upfront sorting wins. The authors claim that only ranges of past interest get organized, but every experiment uses uniformly random ranges, so that claim is not measured; there is no cost model, no rule for when a reorganization is worth making, and updates, concurrency and out-of-memory data are left as open problems.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): is sorting a collection amortized search, and does physical database design give the joint cost model the question on amortized retrieval lacks?
