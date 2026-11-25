---
number: 152
status: Proposed
formerly:
- TERM-tmp94y6v
title: 'specification: a set of tests that fixes which realizations count as admissible, the realizations being whatever passes them all; partial when it leaves differences that would matter undecided, and stored when it outlasts the inquiry or design that set it and constrains what follows'
version: 1
tags:
- epistemology
- philosophy-of-technology
- design-rationale
date: '2026-11-22'
line:
- record-as-apparatus
complements:
- TERM-151
- TERM-134
- TERM-095
draws_on:
- THEORY-162
summary: >-
  Filed under the dialectic regime at the owner's "could we maybe benefit
  from a term?", after the account of specification was laid out on
  2026-11-22. The word carries the record's account ([CLAIM-470](../claims.d/CLAIM-470.md), [CLAIM-475](../claims.d/CLAIM-475.md),
  [CLAIM-477](../claims.d/CLAIM-477.md), [SYNTHESIS-114](../syntheses.d/SYNTHESIS-114.md)) in some 46 entries and had no definition. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: TERM-151 TERM-134 CLAIM-477 CLAIM-783 CLAIM-942 SYNTHESIS-114 — Proposed; the term filed with this, and the entries it is stated against -->

# TERM-152: specification: a set of tests that fixes which realizations count as admissible, the realizations being whatever passes them all; partial when it leaves differences that would matter undecided, and stored when it outlasts the inquiry or design that set it and constrains what follows

## Definition

A **specification** is a set of tests, each a predicate read as a test in
[TERM-134](TERM-134.md)'s sense, that together fix which **realizations** are admissible:
the admissible ones are those that pass every test, their intersection
([CLAIM-783](../claims.d/CLAIM-783.md)). A specification constrains; a realization is what meets it.

Three qualifications the record's account uses:

- **partial**: it leaves undecided some differences that would matter to
  the purpose it serves. A question is a partial specification of its
  answer ([CLAIM-470](../claims.d/CLAIM-470.md)).
- **stored**: it outlasts the inquiry or design that set it and constrains
  what follows, cheapening some later questions and hardening against
  others ([CLAIM-475](../claims.d/CLAIM-475.md), [CLAIM-761](../claims.d/CLAIM-761.md)).
- **revised**: its tests are changed by what realizing or inquiring showed,
  which is where inquiry differs from mere search ([TERM-095](TERM-095.md)'s reflexive
  case).

Each test in a specification also has a **direction of fit** ([TERM-151](TERM-151.md)): it
describes what a realization already is, or requires what one must be
made to be. A specification of findings is made of the first, a
specification of requirements of the second ([CLAIM-942](../claims.d/CLAIM-942.md)).

## Not to be confused with

- **A description.** A description is a specification all of whose tests
  were written from one realization, so that it passes them; most
  specifications admit many realizations, and some admit none.
- **A model or design.** A design is one realization proposed to meet a
  specification, not the specification.
- **The constraint a specification is realized by.** [CLAIM-477](../claims.d/CLAIM-477.md) holds that
  specifications are themselves realized and maintained by something; that
  maintaining apparatus ([TERM-089](TERM-089.md)) is not the specification.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-2259 — Proposed; filed for LEAD-215 -->

A parallel, from Freeman and Pfenning's refinement types ([THEORY-2259](../theory.d/THEORY-2259.md);
[NOTE-2350](../notes.d/NOTE-2350.md)). An ML type with its declared refinements is a specification in
this term's sense, layered: the ML type admits a set of values, each
refinement a subset, and a term's principal refinement is the narrowest
the declarations can say of it. The declarations are stored
specification: written once, they constrain every later program, and
their finiteness is what keeps checking decidable ("Finiteness is
important, since it is necessary for the decidability of refinement type
inference", p. 2). No change.

## Note of 2026-11-25: Martin-Löf, read
<!-- inactive-ok-file: THEORY-tmp62cvo NOTE-tmp60upv CLAIM-tmpjs6hp — Proposed or Skimmed; filed for LEAD-215 -->

A qualification, from Martin-Löf's Intuitionistic Type Theory
([THEORY-tmp62cvo](../theory.d/THEORY-tmp62cvo.md); [NOTE-tmp60upv](../notes.d/NOTE-tmp60upv.md); [CLAIM-tmpjs6hp](../claims.d/CLAIM-tmpjs6hp.md)). The book uses this
term's pair in so many words: "a is a program ... which meets the
specification A" (p. 6), and its forms of judgement keep the two apart, a
realization judged only against a specification already formed: "a
judgement of the form a ∈ A presupposes that A is a set" (p. 5). But its
sets are not sets of tests: "a set A is defined by prescribing how a
canonical element of A is formed" (p. 8). A set of tests in this term's
sense is, there, the set of elements of a given set such that a property
holds, whose elements carry their proofs (p. 53), and, over no given set, a
category, which is not a set (p. 21). The definition stands; the claim
holds the qualification.
