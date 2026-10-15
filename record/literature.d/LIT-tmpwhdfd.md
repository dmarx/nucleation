---
status: Active
status_note: >-
  read in full 2026-10-15 (NOTE for this LIT) from a scan of the published Algorithmica
  article (pp. 79–119, Springer-Verlag copyright line) posted among the reading
  handouts of MIT course 6.896, Spring 2004 (courses.csail.mit.edu/6.896/spring04/class/www/handouts/papers/snoopy-cache.pdf);
  no author or repository copy was found (Unpaywall and OpenAlex: closed; not on
  Sleator's CMU or Karlin's UW pages). Worth reading as the first competitive analysis
  of a rent-or-buy decision: a cache keeping a shared block pays 1 per write to
  keep its copy current, or drops it and pays p to fetch it again if it reads; dropping
  once the writes charged since the last read have cost p is within 2 of the off-line
  optimum on every sequence (Theorem 4.1), and no deterministic on-line rule does
  better (Theorem 3.1); with a third option the bound rises to 3 (Theorem 3.3).
  The paper states the principle generally (change state when the extra cost of
  staying equals the cost of changing) but never names rent-or-buy or ski rental,
  and its instance is the decision to stop maintaining a copy, the mirror of building
  a bin. For [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) and [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md) it gives a worst-case rule for
  when a bin pays without knowing future use: make it when the extra search already
  spent equals its cost; for [CLAIM-303](../claims.d/CLAIM-303.md) it shows that a recurrence count weighted
  by reconstruction cost is, in the worst case, the right criterion and within 2,
  and that the second-occurrence rule is that rule only when filing costs about
  one reconstruction; for [QUESTION-095](../questions.d/QUESTION-095.md) it prices upkeep against re-retrieval and
  nothing on precomputation or staleness, which it forbids rather than prices.
title: Competitive snoopy caching
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref gives
    November 1988, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the title found nothing. Read the same day (NOTE-tmp6n3s5).
tags:
- databases
- mathematics
date: '2026-10-15'
published: '1988-11-01'
doi: 10.1007/BF01762111
first_author: Karlin
keywords: []
implementations: []
summary: >-
  Karlin, Manasse, Rudolph and Sleator (1988), Algorithmica 3. For a shared-bus
  multiprocessor whose caches can either keep a replicated block (and pay one bus
  cycle for every write to it) or drop it (and pay p to fetch it again if it is
  read), the paper gives counter-based on-line algorithms whose total bus cost on
  every request sequence is at most twice that of the best off-line algorithm, and
  proves that no deterministic on-line algorithm can guarantee better than 2. The
  rule is: drop a copy once the writes it has caused since it was last read have
  cost as much as refetching it. With a third option (reading or writing through
  without fetching) the lower bound rises to 3, and the algorithm given is 3-competitive
  ignoring writebacks, 4 counting them; with associative caches the bound becomes
  the paging ratio. The paper never names rent-or-buy or ski rental; its rent is
  upkeep paid on an idle copy, and its purchase is the refetch after dropping, the
  reverse orientation of building a bin. Costs are fixed constants, the guarantees
  are worst case only, and the authors call the practical significance "unclear".
---

# LIT-tmpwhdfd: Competitive snoopy caching

Karlin, A. R., Manasse, M. S., Rudolph, L. and Sleator, D. D. (1988). Competitive snoopy caching. *Algorithmica* 3(1–4), 79–119. DOI 10.1007/BF01762111

## Key takeaways

Read in full ([NOTE-tmp6n3s5](../notes.d/NOTE-tmp6n3s5.md)). For a shared-bus multiprocessor whose caches can either keep a replicated block (and pay one bus cycle for every write to it) or drop it (and pay p to fetch it again if it is read), the paper gives counter-based on-line algorithms whose total bus cost on every request sequence is at most twice that of the best off-line algorithm, and proves that no deterministic on-line algorithm can guarantee better than 2. The rule is: drop a copy once the writes it has caused since it was last read have cost as much as refetching it. With a third option (reading or writing through without fetching) the lower bound rises to 3, and the algorithm given is 3-competitive ignoring writebacks, 4 counting them; with associative caches the bound becomes the paging ratio. The paper never names rent-or-buy or ski rental; its rent is upkeep paid on an idle copy, and its purchase is the refetch after dropping, the reverse orientation of building a bin. Costs are fixed constants, the guarantees are worst case only, and the authors call the practical significance "unclear".

## Why this is here

[QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): is sorting a collection amortized search, and does physical database design give the joint cost model the question on amortized retrieval lacks?
