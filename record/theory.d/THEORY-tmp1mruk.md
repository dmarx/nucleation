---
status: Proposed
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
- LIT-tmp858eb
corroborates:
- CLAIM-tmpnookt
summary: >-
  Freeman & Pfenning (1991), [LIT-tmp858eb](../literature.d/LIT-tmp858eb.md), read in [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md) for [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md). The
  paper that introduced refinement types. For the record it is the reading
  on which [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)'s correspondence of a descriptor with a
  refinement the entry inhabits can be tested ([ARG-tmptph3p](../arguments.d/ARG-tmptph3p.md)), and on which its
  correspondence of the direction of fit with inferring against checking
  is found unsupported ([ARG-tmp5r67s](../arguments.d/ARG-tmp5r67s.md), [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md)). Proposed until the soundness
  theorem it states has a proof and the inference it describes an
  implementation.
---
<!-- inactive-ok-file: ARG-tmptph3p ARG-tmp5r67s CLAIM-tmp764wb CLAIM-tmpnookt CLAIM-783 — Proposed or Rejected; the arguments and counter filed from this reading, and the claims it bears on -->

# THEORY-tmp1mruk: Freeman and Pfenning propose refinement types for ML: subtypes of a datatype that the programmer declares as recursive types, closed under intersection and union into a finite lattice, and inferred by abstract interpretation only for programs already well-typed in ML, which keeps inference decidable and leaves the language of programs unchanged; an annotation is accepted only when the inferred refinement lies below it, and evaluation preserves the refinement type

## Source

Freeman & Pfenning (1991), [LIT-tmp858eb](../literature.d/LIT-tmp858eb.md), read in [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md) from the authors'
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

It corroborates [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) in one correspondence only, a descriptor as
a refinement its entry inhabits, narrowed to a finite declared lattice and
without carried evidence ([ARG-tmptph3p](../arguments.d/ARG-tmptph3p.md)). It does not support the correspondence
of the direction of fit with inference against checking ([ARG-tmp5r67s](../arguments.d/ARG-tmp5r67s.md)), and
grounds the counter that checking an annotation moves nothing ([CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md)).
It parallels [CLAIM-783](../claims.d/CLAIM-783.md)'s result that descriptors cannot conflict: a term
with σ and τ has σ ∧ τ, inhabited by its value.
