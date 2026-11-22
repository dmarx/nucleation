---
status: Active
status_note: >-
  read in full 2026-11-22 (NOTE-tmpaiy4v) from the authors' copy on Frank
  Pfenning's faculty page at Carnegie Mellon, the published text with the
  ACM permission notice, paginated 1 to 11; worth reading as the paper that
  introduced bidirectional checking for intersection and refinement types,
  and the record's first reading of a type system in which checking is a
  mode of its own.
title: 'Intersection Types and Computational Effects'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read on 2026-11-22 for LEAD-tmp3xevc, at the owner's
    request. Not held before: no hit in record/ for the DOI, the title or
    "Davies"; the nearest held work is Freeman and Pfenning 1991
    (LIT-tmp858eb), which this paper cites as [7]. Identifier, authors,
    venue and pages checked on Crossref, no email address sent; Crossref
    gives only the month, and the copy says "Montreal, Canada, September
    2000", so the date is the first of the month. Read from the PDF at
    https://www.cs.cmu.edu/~fp/papers/icfp00.pdf, linked from Pfenning's
    publications page (https://www.cs.cmu.edu/~fp/publications.html): an
    author's copy on a faculty page, lawful under ADR-074. Its pages are
    numbered 1 to 11, for the proceedings' 198 to 208. Davies' thesis,
    "Practical Refinement-Type Checking" (2005), suggested as a
    supplement, was not consulted, so it has no entry (ADR-114).
tags:
- logic
- software-engineering
date: '2026-11-22'
published: '2000-09-01'
doi: '10.1145/351240.351259'
url: 'https://www.cs.cmu.edu/~fp/papers/icfp00.pdf'
first_author: 'Davies'
keywords:
- intersection types
- refinement types
- computational effects
- mutable references
- value restriction
- subtyping
- bidirectional type checking
summary: >-
  Davies & Pfenning (2000), ICFP '00, ACM SIGPLAN, pp. 198–208. Intersection
  types, the form of type refinement types need, are unsound once a language
  has mutable references; restricting intersection introduction to values,
  as Standard ML restricts polymorphism, and dropping the distributivity law
  of subtyping restores soundness (progress and preservation are proved).
  Since type inference for the result is "most likely undecidable" and
  principal types do not exist, the authors give a bidirectional checker:
  the programmer ascribes types, chiefly to function definitions, terms are
  checked against them or have types synthesized, and ascriptions are
  erased, with no coercion inserted. Read in NOTE-tmpaiy4v for
  LEAD-tmp3xevc's test of CLAIM-tmpnookt; the reading is THEORY-tmpei9b5.
---
<!-- inactive-ok-file: THEORY-tmpei9b5 ARG-tmp7pf1t ARG-tmpdq64g CLAIM-tmpvq4ru CLAIM-tmpnookt — Proposed or Rejected; this work's reading, the arguments and counter filed from it, and the claim it tests -->

# LIT-tmp57uqz: Intersection Types and Computational Effects

Davies, R. and Pfenning, F. (2000). "Intersection Types and Computational
Effects." In Proceedings of the Fifth ACM SIGPLAN International Conference
on Functional Programming (ICFP '00), Montreal, pp. 198–208. ACM Press. DOI
10.1145/351240.351259.

## Key takeaways

- With mutable references, a cell can be given nat ref ∧ pos ref, written
  through one and read through the other, and a term of type pos evaluates
  to zero (pp. 1–2). "Similar counterexamples can be constructed for other
  computational effects such as exceptions" (p. 2).
- The fix: "the introduction rule for intersections is restricted to
  values" (p. 3), and the distributivity rule
  (A → B) ∧ (A → B′) ≤ A → (B ∧ B′) is omitted, since it would get round
  the value restriction (p. 3). Progress and preservation are proved
  (Theorem 5, p. 5).
- "Type inference for this language is most likely undecidable, and
  principal types do not exist" (p. 2), so the source language is
  bidirectional: it "distinguishes terms for which a type can be
  synthesized from terms which can be checked against a given type", with
  an ascription C : A that "checks C against A and then yields A as the
  synthesized type" and "incurs no run-time overhead" (p. 6).
- Checking is sound by erasure (Theorem 7, p. 7); completeness is not
  claimed, and some well-typed terms must be restructured before they can be
  checked (p. 7).

## Standing in the record

Filed by LEAD-tmp3xevc to test, in a bidirectional system, CLAIM-tmpnookt's
correspondence of the direction of fit with synthesis against checking and
its clause that the move fitting a term to a type is elaboration or
coercion. It bears out the first narrowly (ARG-tmp7pf1t) and gives no
support to the second (ARG-tmpdq64g, CLAIM-tmpvq4ru).
