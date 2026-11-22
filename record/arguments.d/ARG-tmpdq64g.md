---
status: Rejected
title: "Davies and Pfenning's bidirectional refinement checking, by analogy, shows that the move that fits a term to a type it is checked against is elaboration or coercion"
version: 1
form: analogy
grounds:
- THEORY-tmpei9b5
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
  Rejected as a route: in Davies and Pfenning's checker (THEORY-tmpei9b5)
  ascriptions are erased, subtyping is inclusion and no rule inserts or
  changes anything, so the move that makes a failing term pass is the
  programmer's edit, outside the system. Standing of the conclusion apart
  from this route: CLAIM-tmpnookt holds the clause, from the assistant's
  knowledge; CLAIM-tmpvq4ru tells against it for this system; no reading on
  the record yet tests it against a system that elaborates. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-tmpei9b5 CLAIM-tmpnookt CLAIM-tmpvq4ru CLAIM-tmpmk056 CLAIM-tmp764wb TERM-tmp8b1yl — Proposed; the reading, the claim this is about, the counter filed from the reading, and the entries it is stated against -->

# ARG-tmpdq64g: Davies and Pfenning's bidirectional refinement checking, by analogy, shows that the move that fits a term to a type it is checked against is elaboration or coercion

## The inference

CLAIM-tmpnookt's clause: checking only accepts or rejects, and "the
performative update that moves the term to fit (CLAIM-tmpmk056) is
elaboration or coercion". Davies and Pfenning's is a bidirectional
refinement checker in which a term is checked against a type the
programmer gives; if a move that fits a term is anywhere in such a system,
the analogy would carry it to the record's performative update.

## Critical questions

- **Is the respect the conclusion needs present in the source?** No.
  Ascriptions incur "no run-time overhead" (p. 6) and erase,
  |C : A| = |C| (p. 7); "We avoid coercions by considering only subtype
  relations which are inclusions" (p. 2). No rule of Figure 3 inserts or
  changes anything.
- **Where is the move, then?** With the programmer: "We leave the simple
  fix to the reader" for double (p. 10), η-expansion to meet the value
  restriction (p. 5), lifting a local definition so it can be annotated
  (p. 7). The first half of the clause, that checking only accepts or
  rejects, is borne out; the second has nothing in the system to map to.
- **Is the source the right one?** For checking, yes: it is the paper that
  introduced bidirectional checking for refinement types. For the clause,
  no single source decides: the authors say a coercive interpretation
  "could easily be" added (p. 2). So this rejects the route through this
  paper, not the clause.

## Verdict

Rejected as a route to the clause. CLAIM-tmpvq4ru files what the paper
does show; the clause stays with CLAIM-tmpnookt, untested by any reading
of an elaborating system.
