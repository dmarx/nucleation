---
status: Proposed
promote_when: >-
  A check of the paper's two theorems independent of the authors' own
  proofs, a mechanized proof or a later published reproof, of progress and
  preservation for intersection types with intersection introduction
  restricted to values and without distributivity in a language with
  mutable references, and of the soundness of the bidirectional checker
  with respect to that system; together with an implementation, the
  authors' or another, that checks the paper's §5 examples against their
  ascriptions as described, accepting inc and rejecting double, with
  ascriptions erased and no coercion inserted.
title: "Davies and Pfenning: intersection types are unsound with effects unless intersection introduction is restricted to values and distributivity is dropped; inference being impractical, a bidirectional checker takes types from the programmer's ascriptions, checks terms against them and erases them, inserting nothing"
version: 1
tags:
- logic
- software-engineering
date: '2026-11-22'
source:
- LIT-tmp57uqz
corroborates:
- CLAIM-tmpnookt
summary: >-
  Davies & Pfenning (2000), LIT-tmp57uqz, read in NOTE-tmpaiy4v for
  LEAD-tmp3xevc. The paper that introduced bidirectional checking for
  intersection and refinement types. For the record it is the test, in a
  system where checking is a mode of its own, of CLAIM-tmpnookt's
  correspondence of the direction of fit with synthesis against checking,
  which it bears out narrowly (ARG-tmp7pf1t), and of its clause that the
  move fitting a term to a type is elaboration or coercion, which it does
  not (ARG-tmpdq64g, CLAIM-tmpvq4ru). Proposed until its theorems are
  checked independently and its checker implemented as described.
---
<!-- inactive-ok-file: ARG-tmp7pf1t ARG-tmpdq64g CLAIM-tmpvq4ru CLAIM-tmpnookt CLAIM-tmp764wb CLAIM-783 TERM-tmp7s2aa THEORY-tmp1mruk — Proposed or Rejected; the arguments and counter filed from this reading, and the entries it bears on -->

# THEORY-tmpei9b5: Davies and Pfenning: intersection types are unsound with effects unless intersection introduction is restricted to values and distributivity is dropped; inference being impractical, a bidirectional checker takes types from the programmer's ascriptions, checks terms against them and erases them, inserting nothing

## Source

Davies & Pfenning (2000), LIT-tmp57uqz, read in NOTE-tmpaiy4v from the
authors' copy (pages 1 to 11).

## The account

Refinement types need intersections, "because a given function may have
more than one property" (p. 1). But with mutable references a cell can be
typed nat ref ∧ pos ref, written as a nat and read as a pos, and a program
of type pos evaluates to zero (pp. 1–2). The repair is two restrictions:
"the introduction rule for intersections is restricted to values" (p. 3),
since a computation that allocates may type its new cell differently in
each branch of the intersection (p. 6), and the distributivity law
(A → B) ∧ (A → B′) ≤ A → (B ∧ B′) is dropped, since it would get round the
first (p. 3). Progress and preservation then hold (Theorem 5, p. 5).

The system has no principal types and its inference is "most likely
undecidable" (p. 2), so the source language is bidirectional. It
"distinguishes terms for which a type can be synthesized from terms which
can be checked against a given type", and an ascription C : A "checks C
against A and then yields A as the synthesized type", with "no run-time
overhead" (p. 6). The programmer ascribes types, mostly to function
definitions, and the checker passes them down: to a λ's body, to an
application's argument, to each case branch. Subtyping is inclusion, so
there are no coercions (p. 2), and a checked term is sound by erasure
(Theorem 7, p. 7). Checking is not complete: some well-typed terms must be
restructured before any annotation will do (p. 7).

## What it does not show

That checking is complete, or which programs can be annotated. That
inference is undecidable: it is conjectured. That the value restriction
costs little beyond the authors' examples. Anything about elaboration;
coercion only as an extension the authors call easy (p. 2). Whether an
ascription that its term already meets is, in the record's terms, a
description or a requirement.

## Bearing

It corroborates CLAIM-tmpnookt in one correspondence, narrowed: checking
holds a term to a type given in advance by the programmer, and a term that
fails is the one to change, while synthesis mostly reports declared types
rather than reading a type off the term (ARG-tmp7pf1t). It gives no
support to the clause that the move fitting a term to a type is elaboration
or coercion (ARG-tmpdq64g) and grounds the counter that the move is the
programmer's (CLAIM-tmpvq4ru), which extends CLAIM-tmp764wb to a
bidirectional system. Its value restriction gives TERM-tmp7s2aa's caution,
that a witness is a value, a second reason beside Freeman and Pfenning's
(THEORY-tmp1mruk): effects, not only divergence; and it marks where
CLAIM-783's witness argument would stop.
