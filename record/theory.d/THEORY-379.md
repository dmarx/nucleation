---
number: 379
status: Proposed
formerly:
- THEORY-tmpllt85
promote_when: >-
  A reading of Fagin's own proof (LIT-1108, the PODS 1996 paper or its
  JCSS 1999 journal version) that states the theorem with its probability
  model: what independence of the orderings means, what "arbitrarily high
  probability" quantifies over, and the exact strictness condition on the
  combining function for the matching lower bound. It is refuted if that
  proof states a different bound or different conditions. Further
  secondary statements of the bound, including more of Fagin, Lotem and
  Naor, cannot settle it: the record already holds one.
title: "When the orderings of m attribute-sorted lists of N objects are probabilistically independent, Fagin's Algorithm finds the top k objects under any monotone combining function with O(N^((m−1)/m) k^(1/m)) accesses with arbitrarily high probability, and for strict combining functions no correct algorithm does essentially better in the worst case with high probability; without independence the bound is not claimed"
version: 1
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
---
<!-- inactive-ok-file: LIT-1108 — Unavailable or unread; the source of the bound, cited as reported by LIT-1115 -->

# THEORY-379: When the orderings of m attribute-sorted lists of N objects are probabilistically independent, Fagin's Algorithm finds the top k objects under any monotone combining function with O(N^((m−1)/m) k^(1/m)) accesses with arbitrarily high probability, and for strict combining functions no correct algorithm does essentially better in the worst case with high probability; without independence the bound is not claimed

## Source

Fagin (1996; journal version 1999), [LIT-1108](../literature.d/LIT-1108.md), not read: no lawful copy
could be fetched. The statement is as Fagin, Lotem and Naor (2001),
[LIT-1115](../literature.d/LIT-1115.md), report it in Sections 1 and 3 and footnotes 2 and 17,
read in [NOTE-924](../notes.d/NOTE-924.md).

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
