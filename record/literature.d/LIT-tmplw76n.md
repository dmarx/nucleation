---
status: Active
status_note: >-
  read in full 2026-11-22 (NOTE-tmpnd1kd) from the authors' copy linked from
  Ranjit Jhala's research page; worth reading as the predicate form of
  refinement types, {ν : B | φ}, and as the paper that makes it inferable by
  restricting φ, where a type must be inferred, to conjunctions of a finite
  set of qualifiers.
title: 'Liquid Types'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered and read on 2026-11-22 for LEAD-tmp3xevc, at the owner's
    request. Not held before: no hit in record/ for the DOI, the title,
    "Rondon", "Jhala", "liquid type", "logically qualified" or "Houdini";
    the one hit for "predicate abstraction" is a reference list in
    NOTE-1231 (Clarke et al.'s CEGAR), and the Freeman and Pfenning
    curation entry names liquid types as unread. Identifier, title, venue,
    pages (159 to 169) and date checked on Crossref, no email address sent;
    Crossref misspells the second author "Kawaguci", corrected from the
    paper. Crossref gives 7 June 2008, the first day of PLDI '08 (7 to 13
    June 2008, Tucson). Read from
    https://ranjitjhala.github.io/static/liquid_types.pdf, linked as
    "PLDI 2008" from Jhala's research page
    (https://ranjitjhala.github.io/research.html): an author's copy on a
    faculty page, lawful under ADR-074. It carries the ACM copyright block
    and no page numbers; its eleven pages are the proceedings' 159 to 169.
    The address under Jhala's UCSD pages
    (https://goto.ucsd.edu/~rjhala/papers/liquid_types.pdf) reset the
    connection and was not needed.
tags:
- logic
- software-engineering
date: '2026-11-22'
published: '2008-06-07'
doi: '10.1145/1375581.1375602'
url: 'https://ranjitjhala.github.io/static/liquid_types.pdf'
first_author: 'Rondon'
keywords:
- dependent types
- Hindley-Milner
- predicate abstraction
- type inference
- logical qualifiers
- refinement types
- array bounds checking
implementations:
- DSOLVE (OCaml), https://github.com/ucsd-progsys/dsolve
summary: >-
  Rondon, Kawaguchi & Jhala (2008), PLDI '08, ACM SIGPLAN, pp. 159–169.
  Dependent types {ν : B | φ} for ML, inferred without annotations by
  restricting φ, at λ-abstractions, conditionals, lets and polymorphic
  instantiation, to conjunctions of logical qualifiers from a finite set
  the programmer supplies. Hindley-Milner types give templates, the typing
  rules give subtyping constraints, and predicate abstraction weakens the
  assignment of every qualifier until the constraints hold, giving the
  strongest conjunction that a conservative check in a decidable logic can
  verify. A program with no such type is reported, not changed. DSOLVE cuts
  the annotation that DML's array-bounds benchmarks needed from 31% of
  program text to under 1%. Read in NOTE-tmpnd1kd for LEAD-tmp3xevc's test
  of CLAIM-tmpnookt; the reading is THEORY-tmp01mu6.
---
<!-- inactive-ok-file: CLAIM-tmpnookt THEORY-tmp01mu6 ARG-tmprmcn5 ARG-tmp246r1 CLAIM-tmpcmt21 — Proposed or Rejected; this work's reading, the arguments and claim filed from it, and the claim it tests -->

# LIT-tmplw76n: Liquid Types

Rondon, P. M., Kawaguchi, M. and Jhala, R. (2008). "Liquid Types." In
Proceedings of the 29th ACM SIGPLAN Conference on Programming Language
Design and Implementation (PLDI '08), Tucson, pp. 159–169. ACM. DOI
10.1145/1375581.1375602.

## Key takeaways

- A base refinement {ν : B | e} "specifies the set of values c of the base
  type B such that the predicate [c/ν]e evaluates to true" (p. 160). A
  liquid type over Q is one whose refinement predicates "are conjunctions
  of qualifiers from Q⋆" (p. 160), the qualifiers with their placeholders
  instantiated by program variables in scope.
- Decidability is bought three ways: a conservative implication check in
  the decidable logic EUFA, liquid types only for programs well-typed in
  ML, and the liquid restriction at λ, if, let and instantiation, so that
  "inference becomes decidable, as the space of possible types is
  bounded" (p. 160).
- Inference starts from every qualifier and weakens: the solution is the
  unique minimum, "the strongest conjunction of qualifiers from Q⋆ that
  satisfies all the constraints" (p. 160; §4.3, p. 166).
- Failure is reported and is ambiguous: a safe program may not type
  "due either to an inappropriate choice of qualifiers or the
  conservativeness of our notion of subtyping" (p. 160). The remedies
  named (adding qualifiers, inserting run-time checks, fixing the program)
  are all outside the checker.
- No evidence is kept with the program: the inferred types go to .annot
  files "as documentation" (p. 167).

## Standing in the record

Filed by LEAD-tmp3xevc as the predicate form of the refinement that
CLAIM-tmpnookt writes, {x : A | φ(x)}, after Freeman and Pfenning's
(LIT-tmp858eb, which this paper cites as introducing refinements) turned
out to be a declared finite lattice. It bears out the descriptor as a
predicate refinement the entry inhabits, narrowed where the descriptor
is to be inferred (ARG-tmprmcn5); it bears out inference as informative
update and not checking as requirement (ARG-tmp246r1); and it grounds
CLAIM-tmpcmt21, that a failed check here does not show that the program
fails.
