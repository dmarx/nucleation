---
status: Active
status_note: >-
  read in full 2026-10-15 from the scan of the published CACM article (pp. 202–208,
  with ACM's running heads and copyright line) on Sleator's CMU page (www.cs.cmu.edu/~sleator/papers/amortized-efficiency.pdf);
  the ACM Digital Library's open-access PDF refused direct requests from this environment.
  Worth reading as the founding worst-case comparison of an online rule with the
  best offline one: on a sequentially scanned list where reaching position i costs
  i, move-to-front costs at most twice what any rule in the class costs on the same
  sequence, even one that knows the future (four times counting its own moves),
  while a fixed list sorted by frequency, transpose and frequency count are not
  within any constant; and for paging no online rule beats n/(n − n_MIN + 1) times
  Belady's MIN, a bound LRU and FIFO meet up to an additive n_MIN. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md)
  it shows that in a single pile searched from the top, putting the found item on
  top is within 2 of the best dynamic policy, not of the best arrangement, and that
  sorting ahead of need never pays (Theorem 3); bins are outside its model. For
  [QUESTION-095](../questions.d/QUESTION-095.md) it prices one term, retrieval misses under a fixed cache size and
  the cost of not knowing future requests, and nothing on precomputation, upkeep
  or staleness.
title: Amortized efficiency of list update and paging rules
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref (or the proceedings page)
    on 2026-10-15: Crossref gives February 1985. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for the authors
    and the title found nothing. Read the same day (NOTE-tmpy8giy).
tags:
- databases
- mathematics
date: '2026-10-15'
published: '1985-02-01'
doi: 10.1145/2786.2793
first_author: Sleator
keywords: []
implementations: []
summary: >-
  Sleator and Tarjan (1985), CACM 28(2). For a list searched sequentially from the
  front, where reaching the i-th item costs i, moving each accessed item to the
  front costs at most twice what any other rule costs on the same sequence, including
  rules that know the whole sequence in advance (four times, counting move-to-front's
  own moves), with no probabilistic assumption. A fixed list sorted by access frequency,
  and the transpose and frequency-count rules, are not within any constant factor
  of that. Rearranging ahead of need never pays in this model (Theorem 3). For paging,
  where only a small fast memory is cheap, no rule that cannot see the future can
  do better in the worst case than n/(n − n_MIN + 1) times the offline optimum MIN,
  and LRU and FIFO attain that bound up to an additive n_MIN; with equal memories
  the ratio is the memory size. The model is a single linear list (or a two-level
  memory) with uniform items and access cost depending only on position; it says
  nothing about partitions, bins or search that is not a scan.
---

# LIT-tmpt85t0: Amortized efficiency of list update and paging rules

Sleator, D. D. and Tarjan, R. E. (1985). Amortized efficiency of list update and paging rules. *Communications of the ACM* 28(2), 202–208. DOI 10.1145/2786.2793

## Key takeaways

Read in full ([NOTE-tmpy8giy](../notes.d/NOTE-tmpy8giy.md)). For a list searched sequentially from the front, where reaching the i-th item costs i, moving each accessed item to the front costs at most twice what any other rule costs on the same sequence, including rules that know the whole sequence in advance (four times, counting move-to-front's own moves), with no probabilistic assumption. A fixed list sorted by access frequency, and the transpose and frequency-count rules, are not within any constant factor of that. Rearranging ahead of need never pays in this model (Theorem 3). For paging, where only a small fast memory is cheap, no rule that cannot see the future can do better in the worst case than n/(n − n_MIN + 1) times the offline optimum MIN, and LRU and FIFO attain that bound up to an additive n_MIN; with equal memories the ratio is the memory size. The model is a single linear list (or a two-level memory) with uniform items and access cost depending only on position; it says nothing about partitions, bins or search that is not a scan.

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): is sorting a collection amortized search, and does physical database design give the joint cost model the question on amortized retrieval lacks?
