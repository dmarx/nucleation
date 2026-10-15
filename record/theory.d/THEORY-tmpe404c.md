---
status: Active
title: "For conjunctive queries without equality or comparisons, two queries are equivalent exactly when homomorphisms run both ways between the queries read as small databases, every such query has a minimal equivalent query unique up to isomorphism obtained by deleting atoms, and evaluating one against a database is NP-complete when the query is part of the input"
version: 1
tags:
- databases
- logic
- mathematics
date: '2026-10-15'
source:
- LIT-tmpkq8zv
summary: >-
  Chandra and Merlin (1977), [LIT-tmpkq8zv](../literature.d/LIT-tmpkq8zv.md), read in [NOTE-tmp5wypo](../notes.d/NOTE-tmp5wypo.md). Reading a
  conjunctive query as its natural model, equivalence becomes a pair of
  homomorphisms (Lemma 13), the minimal equivalent query is unique up to
  isomorphism (Theorem 12), and evaluation with the query as input is
  NP-complete (Theorem 7), as is deciding whether one query is a folding of
  another (Theorem 11). The paper states equivalence, not containment, and
  does not state that containment or equivalence is NP-complete; those are
  corollaries later work attributes to it. Nothing here reaches queries
  with equality, comparisons, negation or union.
supports:
- CLAIM-tmpze74h
---
<!-- inactive-ok-file: LIT-tmp3l2ha LIT-tmpu418n CLAIM-303 CLAIM-308 — read the same day or Proposed; named as works and claims this account bears on, not leaned on -->

# THEORY-tmpe404c: For conjunctive queries without equality or comparisons, two queries are equivalent exactly when homomorphisms run both ways between the queries read as small databases, every such query has a minimal equivalent query unique up to isomorphism obtained by deleting atoms, and evaluating one against a database is NP-complete when the query is part of the input

## Source

Chandra and Merlin (1977), [LIT-tmpkq8zv](../literature.d/LIT-tmpkq8zv.md), "Optimal implementation of
conjunctive queries in relational data bases", Proc. STOC 1977, pp. 77–90,
read in full in [NOTE-tmp5wypo](../notes.d/NOTE-tmp5wypo.md) from a scan of the published paper hosted for a
UBC course; statements checked against page images.

## What was actually shown

**The setting.** A conjunctive query is (x1,…,xk).∃y. A1 ∧ … ∧ Ar over
atoms with variables and constants; no equality, and distinct constants
denote distinct elements. Its natural model M_Q has the variables and
constants as elements and the atoms as tuples, with unary relations
marking the output variables and the constants.

**Equivalence (Lemma 13).** Q1 ≡ Q2 iff there are homomorphisms
M_Q1 → M_Q2 and M_Q2 → M_Q1. The proof shows one direction at a time:
a homomorphism from M_Q2 into M_Q1 makes every answer of Q1 an answer of
Q2 on every database. That half is the containment test later called a
containment mapping.

**Minimization (Theorems 10–12).** A folding (an endomorphism fixing the
outputs and constants, with its image as the new query) preserves
equivalence; every query has a folding to which every equivalent query
also folds, up to isomorphism. Deciding whether one query is a folding of
another is NP-complete, also for boolean queries (Theorem 11, from graph
colouring); in the paper's words, "minimizing a conjunctive query is
NP-hard". Isomorphism of conjunctive queries is equivalent to graph
isomorphism (Theorem 8).

**Evaluation (Theorems 6, 7).** With the query as part of the input,
deciding whether a boolean conjunctive query is true in a database is
NP-complete; for first-order queries it is PSPACE-complete, even on a
fixed two-element database.

**Optimal implementation (Theorem 16).** Minimizing first and then choosing
the expression of least polynomial degree gives a program within a
constant factor of optimal in the paper's cost model, at a cost
exponential in the query's length but independent of the database.

**What could have come out otherwise.** Two equivalent conjunctive queries
without homomorphisms each way, or two non-isomorphic minimal equivalents
of one query, would refute Lemma 13 or Theorem 12; a polynomial algorithm
for Theorem 11's problem would put an NP-complete problem in P.

## What this does not say

- **That containment of conjunctive queries is NP-complete, as a stated
  theorem.** The paper states equivalence. Membership in NP follows from
  Lemma 13; hardness follows from Theorem 11's construction. Neither is
  written down, though both are routinely cited to this paper.
- **Anything for richer languages.** Equality, comparisons, negation and
  union are excluded; the paper notes that with equality its notion of
  equivalence is not even transitive. With comparisons, containment
  becomes Π2p-complete (as [LIT-tmp3l2ha](../literature.d/LIT-tmp3l2ha.md) reports from later work).
- **That the search is hard in practice.** The NP-completeness is worst
  case over query shapes and in the size of the queries, not of any
  database. The authors' conclusion runs the other way: since queries are
  short, "It pays, in such cases, to optimize the query as much as
  possible".
- **That this is a theory of reuse.** The paper is about evaluating one
  query well. Reading Lemma 13 as the test for whether a stored answer
  covers a new question is [LIT-tmp3l2ha](../literature.d/LIT-tmp3l2ha.md)'s move, and reading it for filed
  arguments is the record's ([CLAIM-303](../claims.d/CLAIM-303.md)).

## Connections

- [LIT-tmp3l2ha](../literature.d/LIT-tmp3l2ha.md) (Levy et al. 1995) builds the theory of answering queries
  with views on Lemma 13 and Theorem 12; [THEORY-tmpxw8fg](THEORY-tmpxw8fg.md) states it.
- [CLAIM-303](../claims.d/CLAIM-303.md) prices reuse at c_a per use. If deciding that a stored answer
  covers a new question is containment, this is its base procedure and its
  worst case, in the size of the two descriptions. [CLAIM-308](../claims.d/CLAIM-308.md)'s fixed-cost
  premise ([THEORY-348](THEORY-348.md)) does not hold for that term when questions vary.
- [THEORY-348](THEORY-348.md)'s rent-or-buy bound assumes a fixed per-use price; this
  account gives one reason recognition cost is not fixed.
