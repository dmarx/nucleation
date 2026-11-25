---
number: 2262
status: Proposed
formerly:
- THEORY-tmp01mu6
promote_when: >-
  The proofs of the paper's two theorems, which it leaves to a technical
  report, checked by the record or published by the authors or others:
  that a liquid typing implies an exact typing under which evaluation does
  not get stuck, and that inference terminates, returns only valid liquid
  types, and fails only when no liquid type over the qualifiers exists,
  with the unique strongest solution it relies on; together with a run of
  DSOLVE or a later liquid-type checker that infers, from the qualifiers
  given, the types the paper's Section 2 reports for max, sum and foldn.
title: 'Liquid types make inference decidable'
statement: >-
  Rondon, Kawaguchi and Jhala's liquid types are dependent types {ν : B | φ}
  whose predicates, wherever a type must be inferred, are conjunctions of
  qualifiers from a finite set the programmer supplies; inference refines
  Hindley-Milner types by weakening an assignment of every qualifier to the
  strongest conjunction that a conservative check in a decidable logic
  verifies, which keeps checking and inference decidable; the program is
  never changed, and one with no such type is reported, not repaired
version: 1
tags:
- logic
- software-engineering
date: '2026-11-22'
source:
- LIT-3130
corroborates:
- CLAIM-949
- CLAIM-984
summary: >-
  Rondon, Kawaguchi & Jhala (2008), [LIT-3130](../literature.d/LIT-3130.md), read in [NOTE-2353](../notes.d/NOTE-2353.md) for
  [LEAD-215](../leads.d/LEAD-215.md). The predicate form of refinement types, made inferable by
  a finite qualifier vocabulary. For the record it is the reading on which
  [CLAIM-949](../claims.d/CLAIM-949.md)'s descriptor as a refinement {x : A | φ(x)} the entry
  inhabits is tested in the form the claim writes ([ARG-214](../arguments.d/ARG-214.md)); on which
  inference is informative update and checking is not shown to be
  requirement ([ARG-213](../arguments.d/ARG-213.md)); and which grounds [CLAIM-975](../claims.d/CLAIM-975.md), that a
  failed check does not show that the program fails. Proposed until its
  theorems' proofs are checked and its inference reproduced.
---
<!-- inactive-ok-file: CLAIM-949 ARG-214 ARG-213 CLAIM-975 THEORY-2259 CLAIM-965 — Proposed or Rejected; the claim this corroborates, the arguments and claim filed from this reading, and the entries it is read against -->

# THEORY-2262: Liquid types make inference decidable

## Source

Rondon, Kawaguchi & Jhala (2008), [LIT-3130](../literature.d/LIT-3130.md), read in [NOTE-2353](../notes.d/NOTE-2353.md) from
the authors' copy (proceedings pages 159 to 169).

## The account

A base refinement {ν : B | e} "specifies the set of values c of the base
type B such that the predicate [c/ν]e evaluates to true" (p. 160), and
these build dependent function types. The programmer supplies logical
qualifiers, predicates over ν, program variables and a placeholder; "A
liquid type over Q is a dependent type where the refinement predicates are
conjunctions of qualifiers from Q⋆" (p. 160). The typing rules require
liquid types at λ-abstractions, conditionals, lets and polymorphic
instantiation: "By forcing the types to be liquid, we bound the space of
possible solutions, thus making inference efficiently decidable" (p. 164).
Subtyping reduces to implications, checked by an embedding into the
decidable logic EUFA that is conservative (p. 164), and every liquid type
refines an ML type. Inference takes ML types as templates, generates
subtyping constraints, and solves them by predicate abstraction, starting
from every qualifier and weakening, to "the strongest conjunction of
qualifiers from Q⋆ that satisfies all the constraints" (p. 160), the
unique minimum solution (p. 166). Infer terminates, is sound, and returns
Failure only when no liquid type over Q exists (Theorem 2, p. 166); a
liquid typing implies an exact one under which evaluation does not get
stuck (Theorem 1, p. 163). Nothing is inserted into the program. When
typing fails, the remedies named are a new qualifier, a run-time check, or
a fix by the programmer (pp. 160, 168).

## What it does not show

That the inferred type is the strongest true of the program: it is the
strongest from Q⋆ that the conservative check verifies, and for a
function's inputs the strongest that covers the calls the program makes
(p. 167). That a failure lies in the program: the paper names three causes
it cannot yet separate (p. 169). That anything is carried with the term:
derivations and solver checks are not kept, and the inferred types are
printed "as documentation" (p. 167). The proofs, which are in a technical
report not read. And it is not a bidirectional system: it infers, and
checks given types through the same subtyping constraints.

## Bearing

It corroborates [CLAIM-949](../claims.d/CLAIM-949.md) in one correspondence, a descriptor as a
refinement its entry inhabits, now in the predicate form the claim
writes, with the vocabulary of inferable descriptors finite and
conjunctive and no evidence carried ([ARG-214](../arguments.d/ARG-214.md)). It shows inference as
informative update and gives no support to checking as requirement
([ARG-213](../arguments.d/ARG-213.md)), and grounds [CLAIM-975](../claims.d/CLAIM-975.md), which widens [CLAIM-965](../claims.d/CLAIM-965.md)
from Freeman and Pfenning's system ([THEORY-2259](THEORY-2259.md)) to this one. It
cites Freeman and Pfenning as the origin of refinements, "limited to
restrictions on the structure of algebraic datatypes" (p. 169).
