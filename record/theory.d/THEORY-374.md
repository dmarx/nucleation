---
number: 374
status: Proposed
formerly:
- THEORY-tmpg43pg
promote_when: >-
  A reading of the primary proofs, Abiteboul and Duschka 1998 for certain
  answers and Duschka, Genesereth and Levy 2000 for inverse rules, that
  confirms each statement with its conditions (query and view language,
  open or closed world, data or expression complexity). The equivalent-
  rewriting part is already proved in LIT-1100. Another survey or
  textbook restating the results cannot settle it; one of those primary
  papers showing a narrower condition than the survey states would revise
  the title rather than refute it.
title: "Given views with conjunctive definitions, deciding that they answer a conjunctive query exactly is NP-complete in the size of the query and definitions, while a maximally-contained rewriting can be built in time polynomial in that size without saying whether it is exact; and finding all certain answers from the stored contents is polynomial in their size in many open-world cases but co-NP-hard in that size under the closed-world assumption even for conjunctive views and queries"
version: 1
tags:
- databases
- logic
date: '2026-10-15'
source:
- LIT-1116
- LIT-1100
answers:
- QUESTION-114
summary: >-
  Halevy (2001), [LIT-1116](../literature.d/LIT-1116.md), read in [NOTE-921](../notes.d/NOTE-921.md), reporting Levy et al.
  1995 ([LIT-1100](../literature.d/LIT-1100.md), read), Duschka, Genesereth and Levy, and Abiteboul
  and Duschka 1998 (not read). Reuse of stored views is graded: certifying
  an exact rewriting is NP-complete in the size of the definitions, building
  everything the views give (maximally contained) is polynomial, and the
  certain answers can cost a co-NP-hard search in the size of the stored
  data. Proposed because the last two parts rest on the survey's account.
  None of it prices recognition for definitions outside conjunctive queries
  and datalog, or says how costly recognition is on typical queries.
supports:
- CLAIM-314
- CLAIM-312
---
<!-- inactive-ok-file: LIT-1100 LIT-1111 CLAIM-303 CLAIM-308 QUESTION-114 — read the same day, Proposed or open; named as works and claims this account bears on, not leaned on -->

# THEORY-374: Given views with conjunctive definitions, deciding that they answer a conjunctive query exactly is NP-complete in the size of the query and definitions, while a maximally-contained rewriting can be built in time polynomial in that size without saying whether it is exact; and finding all certain answers from the stored contents is polynomial in their size in many open-world cases but co-NP-hard in that size under the closed-world assumption even for conjunctive views and queries

## Source

Halevy (2001), [LIT-1116](../literature.d/LIT-1116.md), "Answering queries using views: A survey",
VLDB Journal 10: 270–294, read in full in [NOTE-921](../notes.d/NOTE-921.md) from the publisher's
PDF on a Columbia course reading list. The exact-rewriting part is
Levy et al. 1995 ([LIT-1100](../literature.d/LIT-1100.md), [THEORY-389](THEORY-389.md)); the rest is the survey's
account of papers not read here.

## What was actually shown

**Three questions about stored views.** An equivalent rewriting answers the
query exactly from the views; a maximally-contained rewriting, relative to
a rewriting language, gives as many answers as any query in that language
can; the certain answers are the tuples in the query's answer on every
database consistent with the stored extensions, under the closed world
(extensions exact) or the open world (extensions possibly incomplete).

**Exact reuse.** By the size bound of [LIT-1100](../literature.d/LIT-1100.md), finding an equivalent
rewriting is in NP and NP-complete; footnote 7: "Note that checking the
correctness of a rewriting is NP-complete".

**Partial reuse.** The inverse-rules algorithm "produces the
maximally-contained rewriting in time that is polynomial in the size of the
query and the views", as a datalog program that may need recursion (with
functional dependencies or access-pattern limits). It "does not tell us
whether the maximally-contained rewriting is equivalent", which would
otherwise decide an NP-complete problem in polynomial time.

**All answers.** Open world: polynomial in the size of the view extensions
"in many practical cases"; co-NP-hard in that size once views may contain
union or the query ≠. Closed world: co-NP-hard even for conjunctive views
and query without comparisons (from 3-colourability). The survey places
materialized views for optimization in the closed world.

**What could have come out otherwise.** A polynomial algorithm deciding
exact rewriting, or one computing closed-world certain answers for
conjunctive views, would put an NP-complete problem in P.

## What this does not say

- **That recognition is expensive in practice.** All bounds are worst case.
  The survey calls the bucket algorithm's Π2p containment test "quite
  efficient in practice" because it is in the size of the query and
  definitions, and reports MiniCon scaling to hundreds of views.
- **Anything without definitions.** Every result assumes each stored view
  has a definition in the query's language. Coverage of a question by a
  stored item with no stated definition, or with one in prose, is outside.
- **Anything about cost-based choice.** Which usable view to use, and
  whether using one is cheaper, is handled by optimizers without
  guarantees; which views to store is named as open.
- **Anything about wrong answers.** Closed-world extensions are exact and
  open-world ones only incomplete; a stored answer that has become false
  ([CLAIM-303](../claims.d/CLAIM-303.md)'s staleness) has no place in the model.

## Connections

- [CLAIM-303](../claims.d/CLAIM-303.md): c_a separates into a cheap partial-recognition term and a hard
  exact-certification term, and a possible content term that grows with
  what was stored. [CLAIM-308](../claims.d/CLAIM-308.md)'s fixed price ([THEORY-348](THEORY-348.md)) holds for neither
  in general; it narrows that claim's scope, as [CLAIM-308](../claims.d/CLAIM-308.md) anticipated for
  drifting costs.
- [QUESTION-114](../questions.d/QUESTION-114.md): the survey puts recognition upstream of view selection
  ("the first step in determining the utility of a choice of views"), the
  step the record's view-selection readings ([LIT-1094](../literature.d/LIT-1094.md), [LIT-1091](../literature.d/LIT-1091.md)) assume.
- [THEORY-389](THEORY-389.md) (exact rewriting) and [THEORY-371](THEORY-371.md) (containment) are the
  proved parts underneath.
- [THEORY-341](THEORY-341.md) (Reiter): the closed-world certain-answer result is the
  stored-views counterpart of Reiter's assumption, and the cost runs the
  other way from the complete-database case.
