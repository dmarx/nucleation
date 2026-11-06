---
number: 376
status: Open
formerly:
- QUESTION-tmp3tq0j
title: 'Since the clone of polymorphisms that fixes the complexity of satisfying a constraint language does not fix the complexity of navigating between its solutions, what property of the language does, beyond Boolean languages with single-variable flips and under resource budgets?'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Dated note added at the twenty-seventh status review (ADR-057), at the
    status review's ruling (the owner delegated these rulings), on the full
    readings of Gopalan et al. and Schwerdtfeger (NOTE-1584, NOTE-1613),
    narrowing the sub-question on formulas without constants. It stays Open.
tags:
- mathematics
- logic
date: '2026-11-05'
line:
- realizability
- formal-apparatus
summary: >-
  A's question, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3, closing: "could the
  algebra of a constraint language predict something about the complexity
  of navigating its solution space?" Filed narrowed. For Boolean languages
  with constants and single flips, Gopalan et al., a work the lead added,
  answer it, and not through the clone: [CLAIM-565](../claims.d/CLAIM-565.md) gives a pair with
  one clone and opposite navigation. The Bulatov–Zhuk dichotomy A cites
  classifies decision problems over fixed finite languages and says nothing
  about connectivity. Open: finite domains beyond Boolean, other move sets,
  languages without constants, and budgets on the worst intermediate
  state. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-1555 NOTE-1572 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# QUESTION-376: Since the clone of polymorphisms that fixes the complexity of satisfying a constraint language does not fix the complexity of navigating between its solutions, what property of the language does, beyond Boolean languages with single-variable flips and under resource budgets?

## Why it is a question

A, in Response 3's closing, after proposing the Pol–Inv Galois connection
as "the algebraic component of the proposed theory": "For example, could
the algebra of a constraint language predict something about the
complexity of navigating its solution space?" A does not cite the work
that bears on it most.

**What is known.**

- **The algebra fixes satisfiability.** For a finite language over a finite
  domain, CSP(Γ) is polynomial when a weak near-unanimity polymorphism
  preserves Γ and NP-complete otherwise (Bulatov, [NOTE-1572](../notes.d/NOTE-1572.md); Zhuk,
  [NOTE-1555](../notes.d/NOTE-1555.md)). Neither says anything about reconfiguration or
  connectivity of solutions.
- **For Boolean languages with constants, the language fixes navigation,
  by another property.** Gopalan, Kolaitis, Maneva and Papadimitriou
  ([NOTE-1584](../notes.d/NOTE-1584.md)), corrected by Schwerdtfeger ([NOTE-1613](../notes.d/NOTE-1613.md)): st-connectivity
  under single flips is polynomial for safely tight languages and
  PSPACE-complete otherwise, and "the boundaries discovered here cut across
  Boolean clones". [CLAIM-565](../claims.d/CLAIM-565.md) gives the consequence: positive 1-in-3 SAT
  and positive NAE-3SAT have, with constants, the same clone and opposite
  navigation complexity. So the clone does not answer A's question even for
  Boolean languages; tightness, a condition on the components of the
  solution graphs and on what fixing constants gives, does.

The record's own question is whether that has a general form.

## What would answer it

- A classification of st-connectivity (or connectivity) for a class of
  finite-domain languages beyond Boolean, by a property of the language
  decidable from it, saying whether the property is algebraic in some
  refined sense, as faithful expressibility is a refined definability
  ("Thus, the use of faithful expressibility or some other refined
  definability technique seems unavoidable"), or not.
- The same for Boolean languages without constants, which Gopalan et al.
  leave open: "the complexity of connectivity for CNF(S)-formulas without
  constants is open."
- For budgets: a classification by language of the minmax problem Ito et
  al. pose ([NOTE-1595](../notes.d/NOTE-1595.md)), the least worst intermediate cost along a path,
  which is [CLAIM-571](../claims.d/CLAIM-571.md)'s threshold; their cases run from strongly
  NP-hard to 2-approximable.
- For A's configuration spaces, which are continuous, a finite-domain
  encoding of a family of them first; without one the question does not
  apply.

## What would not answer it

A classification of satisfiability alone, however refined, since the
Boolean case shows navigation can differ where it agrees; or a result for
one system, which has no complexity in this sense ([CLAIM-578](../claims.d/CLAIM-578.md)).

## Note of 2026-11-06: Claude, read

The sub-question for Boolean languages without constants is narrower than its quote suggests. Gopalan et al.'s §5 continues: "We can extend our dichotomy theorem for st-connectivity to CNF(S)-formulas without constants" ([NOTE-1584](../notes.d/NOTE-1584.md)), without proof in the version read. Schwerdtfeger's §6 reports that his thesis proves the st-connectivity and diameter dichotomies without constants, with connectivity only partly classified ([NOTE-1613](../notes.d/NOTE-1613.md); the thesis, arXiv 1510.06700, was not read). For navigation without constants the classification is reported; global connectivity is what stays open. The question stays Open.
