---
status: Active
status_note: >-
  read in full 2026-11-22 ([NOTE-tmpew427](../notes.d/NOTE-tmpew427.md)) from the authors' preprint on Frank
  Pfenning's faculty page at Carnegie Mellon, not the version of record;
  worth reading as the paper that introduced refinement types, the record's
  first reading of a type system in which a type is narrowed by subtypes
  every value of which already has the type it refines.
title: 'Refinement Types for ML'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read on 2026-11-22 for LEAD-tmp3xevc, at the owner's
    request. Not held before: no hit in record/ for the DOI, the title,
    "Pfenning", "refinement type", "subsort", "datasort" or "intersection
    type". Identifier, authors, venue and pages checked on Crossref, no
    email address sent; Crossref gives only the year, so the date is the
    first day of the conference (24 to 28 June 1991, Toronto), the
    proceedings appearing as SIGPLAN Notices 26(6), June 1991. Read from
    the PDF at https://www.cs.cmu.edu/~fp/papers/pldi91.pdf, linked from
    Pfenning's publications page (https://www.cs.cmu.edu/~fp/publications.html):
    an author's manuscript on a faculty page, lawful under ADR-074. It is
    the "To appear" preprint, paginated 1 to 10, not 268 to 277.
tags:
- logic
- software-engineering
date: '2026-11-22'
published: '1991-06-24'
doi: '10.1145/113445.113468'
url: 'https://www.cs.cmu.edu/~fp/papers/pldi91.pdf'
first_author: 'Freeman'
keywords:
- refinement types
- intersection types
- subtyping
- abstract interpretation
- type inference
- Standard ML
summary: >-
  Freeman & Pfenning (1991), PLDI '91, ACM SIGPLAN, pp. 268–277. A
  system of subtypes for ML: the programmer declares recursive subtypes
  (rectype) of a datatype, such as singleton lists or bitstrings without
  leading zeros; these close under intersection and union into a finite
  lattice for each datatype, and refinement types are inferred by abstract
  interpretation over it, given only to programs already well-typed in ML.
  The language of programs is unchanged; an annotation is accepted only
  when the inferred refinement lies below it. Read in [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md) for
  [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md)'s test of [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md); the reading is [THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md).
---
<!-- inactive-ok-file: THEORY-tmp1mruk ARG-tmptph3p ARG-tmp5r67s CLAIM-tmp764wb CLAIM-tmpnookt — Proposed or Rejected; this work's reading, the arguments and counter filed from it, and the claim it tests -->

# LIT-tmp858eb: Refinement Types for ML

Freeman, T. and Pfenning, F. (1991). "Refinement Types for ML." In
Proceedings of the ACM SIGPLAN 1991 Conference on Programming Language
Design and Implementation (PLDI '91), Toronto, pp. 268–277. ACM Press. DOI
10.1145/113445.113468.

## Key takeaways

- A refinement type is a subtype of an ML type, "which one can think of as
  subsets" (p. 1), declared by the programmer with a rectype
  declaration; "refinement types are given only to programs which are
  already well-typed in ML" (abstract).
- Only refinements of the same ML type may be intersected. The declared
  refinements close under ∧ and ∨ into a finite lattice per datatype, with
  ⊥ at the bottom, and finiteness is "necessary for the decidability of
  refinement type inference" (p. 2).
- Inference is abstract interpretation over that lattice, run after ML
  type inference; an annotation (e : D′) is accepted when the inferred D
  satisfies D ≤ D′ (Figure 2, RESTRICT, p. 8).
- Soundness is stated, its proof omitted: if e evaluates to v and e has
  refinement type D, v has a refinement type D′ ≤ D (p. 7).
- Not every subset can be a refinement: lists without repeated elements and
  closed λ-terms cannot, being no regular tree sets (p. 2).

## Standing in the record

Filed by [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md) to test [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)'s correspondence of a
descriptor with a refinement the entry inhabits, and of the direction of
fit with inferring against checking. It bears out the first, narrowed to a
finite, declared lattice and without carried evidence, and does not bear
out the second ([ARG-tmptph3p](../arguments.d/ARG-tmptph3p.md), [ARG-tmp5r67s](../arguments.d/ARG-tmp5r67s.md), [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md)).
