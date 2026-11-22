---
status: Rejected
title: 'Liquid type inference, and the checking of liquid programs against types given in advance, by analogy, show that the direction of fit is the split between inferring a type from a term and checking a term against a type given'
version: 1
form: analogy
grounds:
- THEORY-tmp01mu6
concludes:
- CLAIM-tmpnookt
uses:
- TERM-tmp8b1yl
tags:
- logic
- philosophy-of-language
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  Rejected as a route. Half holds: liquid inference is informative update,
  weakening a description until the program passes it and never moving the
  program. Half does not: types given in advance are checked through the
  same constraints, a program that fails is reported and not moved, and
  the failure may lie in the vocabulary or the checker rather than the
  program. Standing of the conclusion apart from this route:
  [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) holds it, from the assistant's knowledge, untested until
  [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md) reads Dunfield and Krishnaswami; [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md) and
  [CLAIM-tmpcmt21](../claims.d/CLAIM-tmpcmt21.md) tell against its checking half for the two refinement
  systems read. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp01mu6 CLAIM-tmpnookt CLAIM-tmp764wb CLAIM-tmpcmt21 TERM-tmp8b1yl ARG-tmp5r67s — Proposed or Rejected; the reading, the claim this is about, the counters that tell against it, the term, and the earlier argument on the same route -->

# ARG-tmp246r1: Liquid type inference, and the checking of liquid programs against types given in advance, by analogy, show that the direction of fit is the split between inferring a type from a term and checking a term against a type given

## The inference

[CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md): inference reads a type off a term, word to world, a
descriptor; checking holds a term to a type given in advance, world to
word, a requirement; the move that makes a term fit is elaboration or
coercion. Liquid types have both: types inferred for λ, if, let and
instantiation, and types given in advance for constants and interfaces,
such as sub's, against which arguments are checked ([THEORY-tmp01mu6](../theory.d/THEORY-tmp01mu6.md)).

## Critical questions

- **Is inference word to world?** Yes. Solve starts from "a trivial
  assignment, in which each liquid type variable is assigned the
  conjunction of all logical qualifiers" and weakens it until the
  constraints hold (p. 166): the description gives way, the program does
  not. That is [TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)'s informative update, and the inferred type is
  the strongest descriptor the vocabulary and check allow.
- **Is checking world to word?** No. A type given in advance enters the
  same subtyping constraints; a program that fails has no type, "If
  Infer(Γ, e, Q) = Failure then there is no S s.t. Γ ⊢_Q e : S" (p. 166),
  and is listed, not changed. Requirement appears only when a programmer
  changes the program (p. 168), outside the system, as in Freeman and
  Pfenning's ([ARG-tmp5r67s](ARG-tmp5r67s.md)).
- **Is the move that fits a term present?** Named, not present: "we can use
  the results of the inference to insert a minimal set of run-time checks"
  (p. 160), by hybrid type checking, which the paper cites and does not
  do. And a failure may not call for a move of the program at all: the
  qualifier set or the checker may be at fault ([CLAIM-tmpcmt21](../claims.d/CLAIM-tmpcmt21.md)).
- **Is the source the right one?** Not for the checking half. It is an
  inference system with types given at its edges, not a bidirectional one.

## Verdict

Rejected as a route to the correspondence as stated. The inference half is
borne out; the checking half is not, and [CLAIM-tmpcmt21](../claims.d/CLAIM-tmpcmt21.md) files what the
paper does show.
