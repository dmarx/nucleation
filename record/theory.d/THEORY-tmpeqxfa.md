---
status: Active
title: "For positive relational algebra on relations whose tuples are annotated from a commutative semiring, every query's annotated answer equals its answer over provenance polynomials N[X] in the input tuple ids, evaluated at the input annotations, so set, bag, c-table and event-table semantics all factor through the polynomials; revaluing inputs can remove output tuples but never add them, and nothing is shown for negation, difference or aggregation"
version: 1
tags:
- databases
- mathematics
- logic
date: '2026-10-15'
source:
- LIT-tmpjckak
answers:
- QUESTION-105
summary: >-
  Green, Karvounarakis and Tannen (2007), [LIT-tmpjckak](../literature.d/LIT-tmpjckak.md), read in [NOTE-tmpc5ict](../notes.d/NOTE-tmpc5ict.md).
  Union and projection add tags, join multiplies them; the usual RA identities
  hold exactly when the tags form a commutative semiring, and a map of tags
  commutes with every query exactly when it is a semiring homomorphism. The
  polynomials N[X] are the free commutative semiring, so the annotated answer
  in any semiring is the polynomial answer evaluated at the input annotations
  (Theorem 4.3). It is a sufficiency result for revisions that re-annotate
  existing inputs, not a minimality result, and it excludes added facts and
  every nonmonotone operation.
extended_by:
- THEORY-tmplwy86
---

# THEORY-tmpeqxfa: For positive relational algebra on relations whose tuples are annotated from a commutative semiring, every query's annotated answer equals its answer over provenance polynomials N[X] in the input tuple ids, evaluated at the input annotations, so set, bag, c-table and event-table semantics all factor through the polynomials; revaluing inputs can remove output tuples but never add them, and nothing is shown for negation, difference or aggregation

## Source

Green, Karvounarakis and Tannen (2007), [LIT-tmpjckak](../literature.d/LIT-tmpjckak.md) (PODS 2007), read in
[NOTE-tmpc5ict](../notes.d/NOTE-tmpc5ict.md) from the authors' postprint: Definitions 3.1, 3.2 and 4.1,
Propositions 3.4, 3.5 and 4.2, Theorem 4.3, Figures 3 and 5.

## What was actually shown

**The algebra.** A K-relation tags each tuple with an element of K, with
finitely many nonzero. Union adds tags, projection sums the tags of the
tuples it merges, join multiplies, selection multiplies by 0 or 1. The RA
identities (union and join associative and commutative, join distributing
over union, projection and selection commuting) hold if and only if K is a
commutative semiring (Proposition 3.4). Idempotence is not required, which
is why bags fit. Booleans give set semantics, the naturals bag semantics,
positive Boolean expressions c-tables, and sets of outcomes event tables.

**The factorization.** Tag each input tuple with its own id and compute in
N[X]. Because N[X] is free, any valuation of the ids in a commutative
semiring K extends to a unique homomorphism Eval_v (Proposition 4.2), and
homomorphisms commute with every RA+ query (Proposition 3.5). Hence
q(R) = Eval_v ∘ q(R̄) (Theorem 4.3): "the semantics of RA+ on K-relations
for any semiring K factors through the semantics of the same in provenance
semirings." In the paper's example the tuple (d, e) has polynomial
2r² + rs, and at p = 2, r = 5, s = 1 it gives 55, its multiplicity under bag
semantics.

**Why the record holds it Active.** Theorem 4.3 is derived in the text
from Propositions 3.5 and 4.2. Proposition 4.2 is the universal property of
polynomials, and the direction of Proposition 3.5 used here is immediate
from Definition 3.2, since every operation is a finite sum or product of
tags. Under a homomorphism "the support may shrink but never increase".

## What this does not say

- **That N[X] is the least that must be retained.** It is the most general
  annotation, sufficient for every commutative semiring at once. For a
  narrower family less suffices (for set-semantics deletion, which ids occur
  together in some monomial), and the paper proves no lower bound and gives
  no size bounds.
- **That it covers revision in general.** The revisions it covers re-annotate
  facts already present: deleting one is evaluating its id at 0, which is
  the record's application of Theorem 4.3, since the paper never mentions
  deletion. Adding a fact, deriving a tuple not in the current output, and
  any negation, difference, aggregation or defeat are outside. The authors
  expect negation to need "an additional operation akin to “proper
  subtraction” in N".
- **That lineage factors through it.** The paper's structure for
  why-provenance, (P(X), ∪, ∪, ∅, ∅), sets 0 = 1 and fails 0 · a = 0, so as
  written it is not a semiring and Theorem 4.3 does not apply to it
  literally. That why-provenance, one set of contributing tuples per
  output, is also coarser than the witness basis of [LIT-tmp8m5l3](../literature.d/LIT-tmp8m5l3.md) the paper
  cites for it.
- **That it captures strength of evidence or trust.** The polynomial records
  how inputs combine; strengths enter only through the valuation. Trust is a
  motive in the paper, not a semiring it gives, and probabilities are
  computed from event tables after the semiring calculation.

## Connections

- [QUESTION-105](../questions.d/QUESTION-105.md): a sufficiency answer for one family of revisions,
  re-annotation of existing input facts under a positive query. It meets
  the question's "provenance, dependencies" option, and leaves the
  "defeated alternatives" option, which needs nonmonotone revision, open.
  [THEORY-353](THEORY-353.md) and [THEORY-347](THEORY-347.md) hold the one-step answers for full belief and
  for bases; this is neither.
- [CLAIM-293](../claims.d/CLAIM-293.md) and [CASE-089](../cases.d/CASE-089.md): the polynomial is finer than topology (joint
  against alternative support, counts of derivations), but is identical in
  [CASE-089](../cases.d/CASE-089.md)'s two worlds; the difference is in the valuation.
- [CLAIM-303](../claims.d/CLAIM-303.md): filing one polynomial per output and evaluating it, instead of
  rerunning the query, is a concrete instance of the trade, with no costs
  given.
- [CLAIM-306](../claims.d/CLAIM-306.md): no negation, so nothing about absence; a tuple tagged 0 carries
  the zero polynomial.
- [THEORY-tmpbyiv8](THEORY-tmpbyiv8.md): the witness basis is the set-semantics shadow of the same
  derivations.
- [LIT-016](../literature.d/LIT-016.md) (read in [NOTE-016](../notes.d/NOTE-016.md)) uses the same move in another field: a semiring
  homomorphism from probabilities to Booleans carries a distribution to its
  support.
