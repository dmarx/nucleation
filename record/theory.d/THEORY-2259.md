---
number: 2259
status: Proposed
formerly:
- THEORY-tmp1mruk
promote_when: >-
  A proof, published by the authors or by others, of the soundness theorem
  the paper states and omits (if an expression of refinement type D
  evaluates to a value, the value has a refinement type below D), together
  with an implementation, the authors' or another, that infers refinement
  types as described from rectype declarations for the paper's own
  examples, singleton lists and bitstrings in standard form, without
  annotations.
title: 'Freeman and Pfenning propose refinement types for ML: subtypes of a datatype that the programmer declares as recursive types, closed under intersection and union into a finite lattice, and inferred by abstract interpretation only for programs already well-typed in ML, which keeps inference decidable and leaves the language of programs unchanged; an annotation is accepted only when the inferred refinement lies below it, and evaluation preserves the refinement type'
version: 1
tags:
- logic
- software-engineering
date: '2026-11-22'
source:
- LIT-3127
corroborates:
- CLAIM-949
summary: >-
  Freeman & Pfenning (1991), [LIT-3127](../literature.d/LIT-3127.md), read in [NOTE-2350](../notes.d/NOTE-2350.md) for [LEAD-215](../leads.d/LEAD-215.md). The
  paper that introduced refinement types. For the record it is the reading
  on which [CLAIM-949](../claims.d/CLAIM-949.md)'s correspondence of a descriptor with a
  refinement the entry inhabits can be tested ([ARG-209](../arguments.d/ARG-209.md)), and on which its
  correspondence of the direction of fit with inferring against checking
  is found unsupported ([ARG-208](../arguments.d/ARG-208.md), [CLAIM-965](../claims.d/CLAIM-965.md)). Proposed until the soundness
  theorem it states has a proof and the inference it describes an
  implementation.
---
<!-- inactive-ok-file: ARG-209 ARG-208 CLAIM-965 CLAIM-949 CLAIM-783 — Proposed or Rejected; the arguments and counter filed from this reading, and the claims it bears on -->

# THEORY-2259: Freeman and Pfenning propose refinement types for ML: subtypes of a datatype that the programmer declares as recursive types, closed under intersection and union into a finite lattice, and inferred by abstract interpretation only for programs already well-typed in ML, which keeps inference decidable and leaves the language of programs unchanged; an annotation is accepted only when the inferred refinement lies below it, and evaluation preserves the refinement type

## Source

Freeman & Pfenning (1991), [LIT-3127](../literature.d/LIT-3127.md), read in [NOTE-2350](../notes.d/NOTE-2350.md) from the authors'
preprint (pages 1 to 10).

## The account

ML's types are kept, and beneath each datatype the programmer declares
the distinctions that matter, as recursive types built from its
constructors: rectype α singleton = cons(α, nil). These "stand for
subtypes which one can think of as subsets" (p. 1), and "refinement types
are given only to programs which are already well-typed in ML"
(abstract). The declared refinements of a datatype close under
intersection and union into a finite lattice, ⊥ at the bottom; only
refinements of the same ML type are intersected, and "an expression has
type σ ∧ τ if it has both type σ and type τ" (p. 3). Inference runs after
ML's, as "abstract interpretation over a programmer-specified finite
lattice of refinements of each ML type", and finiteness "is necessary for
the decidability of refinement type inference" (p. 2). Annotations are
optional: (e : D′) is accepted when the inferred D satisfies D ≤ D′
(Figure 2, p. 8), and "any legal ML program continues to be legal if no
refinements are specified" (p. 2). Soundness: if e has refinement type D
and evaluates to v, v has a refinement type D′ ≤ D (p. 7, proof omitted).

## What it does not show

That any subset of a type can be a refinement: those that are not regular
tree sets, such as lists without repeated elements, cannot (p. 2). That
the subtyping of function types is complete: the authors say more
relations may hold than the rules establish (p. 6). Anything about
carrying evidence with a value: a refinement type is a judgement the
system derives, not an object stored with the term. And it is not a
bidirectional type system: it infers, and checks annotations against what
it inferred.

## Bearing

It corroborates [CLAIM-949](../claims.d/CLAIM-949.md) in one correspondence only, a descriptor as
a refinement its entry inhabits, narrowed to a finite declared lattice and
without carried evidence ([ARG-209](../arguments.d/ARG-209.md)). It does not support the correspondence
of the direction of fit with inference against checking ([ARG-208](../arguments.d/ARG-208.md)), and
grounds the counter that checking an annotation moves nothing ([CLAIM-965](../claims.d/CLAIM-965.md)).
It parallels [CLAIM-783](../claims.d/CLAIM-783.md)'s result that descriptors cannot conflict: a term
with σ and τ has σ ∧ τ, inhabited by its value.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 — Proposed; filed for LEAD-215 -->

A contrast from the same line of work. Davies and Pfenning
([THEORY-2260](THEORY-2260.md); [NOTE-2351](../notes.d/NOTE-2351.md)), citing this paper as [7], drop its
requirement that intersected types refine one simple type (p. 1), show
general intersections unsound with references unless introduction is
restricted to values (p. 3), and replace inference, "most likely
undecidable" for the result (p. 2), with bidirectional checking against
the programmer's ascriptions. So the decidability this account credits to
the finite declared lattice and the same-type restriction is what the
later system gives up, and the programmer states per function what this
one read off. No change.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 — Proposed; filed for LEAD-215 -->

The later account (no edge). Rondon, Kawaguchi and Jhala 2008
([THEORY-2262](THEORY-2262.md); [NOTE-2353](../notes.d/NOTE-2353.md)) cite this paper as where "The notion of
type refinements was introduced", "with refinements limited to
restrictions on the structure of algebraic datatypes, for which inference
is decidable" (p. 169). Their liquid types keep what made inference
decidable here, a finite vocabulary fixed in advance and refinements only
of programs already well-typed in ML. They change the vocabulary from
declared datatype refinements to logical qualifiers, conjoined, over base
types and functions, checked in a decidable logic. They also lack what
this account has: refinements of recursive datatypes. Not a rival and not
a correction; each is right of its own system.
