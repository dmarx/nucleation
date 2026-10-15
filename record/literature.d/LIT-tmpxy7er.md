---
status: Active
status_note: >-
  read in full 2026-10-15 from the published Journal of the ACM version (28(3),
  pp. 615–628), which ACM serves free (OpenAlex/Unpaywall: bronze) but refused to
  this environment with 403, fetched instead as the copy on a University of Maryland
  course page (www.cs.umd.edu/users/gasarch/COURSES/858/S13/tables.pdf) and compared
  with the author's Stanford report STAN-CS-79-753 (i.stanford.edu/pub/cstr/reports/cs/tr/79/753/CS-TR-79-753.pdf),
  which has the same results. Worth reading as the paper that set up what is now
  called the cell-probe model, with lookup cost counted as the worst-case number
  of cells read and arrangement and search strategy left arbitrary: for static membership,
  sorted order with binary search (⌈lg(n+1)⌉ probes) is optimal once the key space
  exceeds a Ramsey-number threshold, provided cells hold only stored keys or pointer
  symbols; it is beaten for small key spaces (one probe for m ≤ 2n − 2), and for
  large ones as soon as one cell may hold an encoded value (two probes for m ≥ 2^{16n²}).
  For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) it shows that "founding cell-probe paper" holds but "when
  storage in sorted order beats other arrangements" does not as worded: the theorem
  says nothing beats sorting under a no-encoding restriction for huge universes,
  and the rest of the paper shows other arrangements beating it. It counts lookup
  probes only; building the arrangement is free, so it bears nothing on whether
  sorting is amortized search or on the cost of organising set against lookups later.
title: Should Tables Be Sorted?
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref (or the proceedings page)
    on 2026-10-15: Crossref gives July 1981. Not held in the Anthology of the SOTA:
    a grep of its record/ (clone of 2026-10-15, commit d1573d2) for the authors
    and the title found nothing. Read the same day (NOTE-tmp60fit).
tags:
- information-retrieval
date: '2026-10-15'
published: '1981-07-01'
doi: 10.1145/322261.322274
first_author: Yao
keywords: []
implementations: []
summary: >-
  Yao (1981), JACM 28(3). For storing a set of n keys from a universe {1,…,m} in
  a table so that the membership query (is x in S?) is answered with the fewest
  worst-case adaptive probes, Yao proves that when the table cells may hold only
  keys of S or a bounded number of pointer symbols, sorted order with binary search
  (⌈lg(n+1)⌉ probes) is optimal once m exceeds a Ramsey-number threshold N(n, p,
  q), whatever the arrangement rule, table size or hashing scheme. The threshold
  is astronomically large, and for small universes sorted order is beaten (one probe
  suffices for m = 3 with n = 2, and for m ≤ 2n − 2 with n > 2). The optimality
  also fails as soon as one cell may hold an arbitrary value from the universe:
  with a single extra "directory" cell, two probes suffice for m ≥ 2^{16n²}. Only
  query cost is counted; building the table is free and unconstrained, so the paper
  says nothing about the cost of arranging or about trading arrangement cost against
  lookups.
---

# LIT-tmpxy7er: Should Tables Be Sorted?

Yao, A. C.-C. (1981). Should tables be sorted? *Journal of the ACM* 28(3), 615–628. DOI 10.1145/322261.322274

## Key takeaways

Read in full ([NOTE-tmp60fit](../notes.d/NOTE-tmp60fit.md)). For storing a set of n keys from a universe {1,…,m} in a table so that the membership query (is x in S?) is answered with the fewest worst-case adaptive probes, Yao proves that when the table cells may hold only keys of S or a bounded number of pointer symbols, sorted order with binary search (⌈lg(n+1)⌉ probes) is optimal once m exceeds a Ramsey-number threshold N(n, p, q), whatever the arrangement rule, table size or hashing scheme. The threshold is astronomically large, and for small universes sorted order is beaten (one probe suffices for m = 3 with n = 2, and for m ≤ 2n − 2 with n > 2). The optimality also fails as soon as one cell may hold an arbitrary value from the universe: with a single extra "directory" cell, two probes suffice for m ≥ 2^{16n²}. Only query cost is counted; building the table is free and unconstrained, so the paper says nothing about the cost of arranging or about trading arrangement cost against lookups.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): is sorting a collection amortized search, and does physical database design give the joint cost model the question on amortized retrieval lacks?
