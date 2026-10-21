---
number: 379
status: Active
formerly:
- THEORY-tmpllt85
title: "Fagin's Algorithm finds the top k of N objects held in m attribute-sorted lists under any monotone combining function, and when the lists' orderings are independent with at least m − 1 of them uniformly random it does so with O(N^((m−1)/m) k^(1/m)) sorted and random accesses with arbitrarily high probability; with dependent orderings the bound can fail"
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Narrowed and promoted from Proposed to Active by the promotion audit
    (batch 077, ADR-047 v2 and v4). The promote_when asked for a reading
    of Fagin's proof; the review re-derived the upper bound and the
    algorithm's correctness step by step instead, which ADR-047 v2 counts
    as meeting it, and checked the bound by simulation. The title now
    states the probability model the derivation needs (independent
    orderings, at least m − 1 uniformly random) and drops the lower bound
    for strict combining functions, which the review did not re-derive.
    That lower bound is carried by THEORY-tmpylmuq, Proposed, which
    extends this entry and inherits the promote_when.
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-1115
- LIT-1108
summary: >-
  Fagin (1996/1999), [LIT-1108](../literature.d/LIT-1108.md), as reported by Fagin, Lotem and Naor
  (2001), [LIT-1115](../literature.d/LIT-1115.md), read in [NOTE-924](../notes.d/NOTE-924.md). Fagin's own paper could not
  be obtained, and the reporting paper declines to describe the
  probability model ("off track"). It does correct one misreading: the
  only probabilistic assumption is independence of the lists' orderings,
  not a uniform distribution of grades. For two lists the bound is
  √(Nk). It does not hold for anti-correlated attributes, where any
  algorithm can need about half the objects.
extended_by:
- THEORY-tmpylmuq
---
<!-- inactive-ok-file: LIT-1108 — Unavailable or unread; the source of the bound, cited as reported by LIT-1115 -->
<!-- inactive-ok-file: THEORY-tmpylmuq — Proposed; the lower bound this entry dropped when it was narrowed, open -->

# THEORY-379: Fagin's Algorithm finds the top k of N objects held in m attribute-sorted lists under any monotone combining function, and when the lists' orderings are independent with at least m − 1 of them uniformly random it does so with O(N^((m−1)/m) k^(1/m)) sorted and random accesses with arbitrarily high probability; with dependent orderings the bound can fail

## Source

Fagin (1996; journal version 1999), [LIT-1108](../literature.d/LIT-1108.md), not read: no lawful copy
could be fetched. The statement is as Fagin, Lotem and Naor (2001),
[LIT-1115](../literature.d/LIT-1115.md), report it in Sections 1 and 3 and footnotes 2 and 17,
read in [NOTE-924](../notes.d/NOTE-924.md).


## Note (2026-10-21): re-derived and narrowed

The promotion audit re-derived the two parts of this title that it now
keeps.

- **Correctness, for any monotone combining function.** Let Y be k
  objects seen in every list by the stopping depth T. An object never
  seen under sorted access ranks below depth T in every list, so each of
  its grades is at most the corresponding grade of every member of Y, and
  by monotonicity its combined grade is at most theirs. The top k can be
  taken from the objects seen.
- **The upper bound.** Let X_t count the objects in the top t of every
  list. With the orderings independent and at least m − 1 of them
  uniformly random, E X_t = N(t/N)^m. Membership of distinct objects in
  one uniform top-t set is negatively correlated, and the lists are
  independent, so Var X_t ≤ E X_t. At t = c·N^((m−1)/m) k^(1/m),
  Chebyshev gives P(T > t) ≤ c^m/(c^m − 1)², which goes to 0 as c grows.
  Sorted accesses are mT and random accesses at most m(m − 1)T, so the
  cost is O(N^((m−1)/m) k^(1/m)) with probability as close to 1 as
  wanted, the constant depending on m and on that probability.
- **Simulation.** Over 200 runs each for N from 10⁴ to 10⁶, m from 2 to 4
  and k from 1 to 10, the stopping depth divided by N^((m−1)/m) k^(1/m)
  had median 0.86–1.00 and 95th percentile 1.11–1.68.
- **Why uniformity is in the title.** Independence alone is not enough.
  Two deterministic lists in opposite orders are independent, and FA
  then needs depth about N/2 for k = 1, not √N. This is consistent with
  the reporting paper's correction that grades need not be uniformly
  distributed: what the bound needs is uniformly random orderings.

The lower bound for strict combining functions, which this entry used to
state, was not re-derived. It is now [THEORY-tmpylmuq](THEORY-tmpylmuq.md).

## What was actually shown

**As reported.** Fagin's Algorithm reads all m lists in parallel until k
objects have been seen in every list, then looks up every object seen and
returns the k best. It is correct for monotone combining functions. "If
there are N objects in the database, and if the orderings in the sorted
lists are probabilistically independent, then the middleware cost of FA is
O(N (m−1)/m k1/m ), with arbitrarily high probability" (exponents lost in
extraction: N^((m−1)/m) k^(1/m)). "Fagin shows that his algorithm is
optimal with high probability in the worst case if the aggregation
function is strict (so that, intuitively, we are dealing with a notion of
conjunction), and if the orderings in the sorted lists are
probabilistically independent."

**Conditions as reported.** Independence of the orderings is the only
probabilistic assumption: footnote 17 says "the only probabilistic
assumption in [?] is that the orderings given by the sorted lists are
probabilistically independent", against a claim that the result needs
uniformly distributed grades. The optimality half needs a strict function
(score 1 exactly when every grade is 1). FA's access pattern ignores the
function, so for max, which is not strict, it is not optimal: a simple
algorithm uses at most mk sorted accesses.

## What this does not say

- **Anything for dependent attributes.** In the anti-correlated case
  ([THEORY-361](THEORY-361.md)) every algorithm can need about half the objects; when
  attributes are positively correlated the cost can be far below the
  bound. The bound is for one probability model of the data.
- **That it is an instance guarantee.** It is a high-probability worst-case
  bound. Fagin, Lotem and Naor's threshold algorithm is never worse than
  FA in sorted accesses and is instance optimal ([THEORY-363](THEORY-363.md)).
- **What the probability model is, exactly.** The reporting paper does
  not say, and the record has not read the proof.

## Connections

- [THEORY-363](THEORY-363.md) and [THEORY-361](THEORY-361.md): the same problem, priced per instance
  and in the anti-correlated case.
- [THEORY-358](THEORY-358.md): Treisman's conjunction displays are built so that colour
  and shape are anti-correlated across distractors, so this bound is not
  the one that applies to them.
