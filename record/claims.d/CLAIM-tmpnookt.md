---
status: Proposed
title: 'The record''s account of specification is model-theoretic, a set of tests and the versions that pass them all, as an institution pairs sentences with the models that satisfy them; type theory is its proof-relevant counterpart, in which a specification is a type, a question a problem, a realization an inhabitant carried with the evidence that it passes, adding a descriptor a refinement the entry provably inhabits, which is why descriptors cannot conflict, and the direction of fit is bidirectional typing''s split between inferring a type from a term and checking a term against a type given'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) The record's practice turns out
  proof-irrelevant in the sense that matters: an entry's passing its
  predicates is never carried with, or checked against, any evidence
  beyond the entry itself, so the type-theoretic reading adds nothing to
  the model-theoretic one. (b) A reading of the type-theoretic sources
  (LEAD-tmp3xevc) shows that one of the correspondences named, question
  as problem, descriptor as refinement inhabited, direction of fit as
  inference against checking, fails on its own terms, not only in
  emphasis.
tags:
- logic
- epistemology
- design-rationale
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
rests_on:
- CLAIM-470
- CLAIM-783
- CLAIM-tmpmk056
grounds:
- THEORY-1142
uses:
- TERM-tmp94y6v
- TERM-tmp8b1yl
summary: >-
  Filed under the dialectic regime at the owner's "relate specification to
  type theory", 2026-11-22. The record holds the model-theoretic side of
  specification (Goguen and Burstall's institutions, [THEORY-1142](../theory.d/THEORY-1142.md), Active)
  and two type-theory works on other matters ([LIT-032](../literature.d/LIT-032.md), [LIT-040](../literature.d/LIT-040.md)), but no
  reading of propositions as types, realizability, refinement types or
  bidirectional typing; the correspondences below are stated from the
  assistant's knowledge and wait on [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-783 CLAIM-tmpmk056 TERM-tmp94y6v — Proposed or Open; the claims, terms and lead this joins -->

# CLAIM-tmpnookt: The record's account of specification is model-theoretic, a set of tests and the versions that pass them all, as an institution pairs sentences with the models that satisfy them; type theory is its proof-relevant counterpart, in which a specification is a type, a question a problem, a realization an inhabitant carried with the evidence that it passes, adding a descriptor a refinement the entry provably inhabits, which is why descriptors cannot conflict, and the direction of fit is bidirectional typing's split between inferring a type from a term and checking a term against a type given

## Two ways to say what a specification is

**Model-theoretic, the record's own.** [TERM-tmp94y6v](../terms.d/TERM-tmp94y6v.md) defines a
specification as a set of tests and its realizations as whatever passes
them all ([CLAIM-783](CLAIM-783.md)). That is the semantics of an institution
([THEORY-1142](../theory.d/THEORY-1142.md)): a set of sentences E picks out the class E* of models that
satisfy every one, and a class of models picks out the sentences true in
all of them. Passing is a fact about the realization; nothing more is
carried.

**Proof-relevant, type theory's.** In type theory a specification is a
type, and a realization is a term that inhabits it, given together with the
derivation that it does. Read through the record's account:

- **A question is a problem.** Kolmogorov read a proposition as a problem
  and its proof as a solution; Martin-Löf's types are the same reading. A
  question, as [CLAIM-470](CLAIM-470.md) has it, fixes which differences would count as an
  answer: it is a type, partial when it has many inhabitants.
- **A finding is an inhabitant, and the word "realization" is shared.**
  Kleene's realizability calls the program that witnesses a proposition its
  realizer: the record's realization, with the witness kept.
- **A descriptor is a refinement the entry inhabits.** Adding a predicate φ
  to a type A gives the refinement {x : A | φ(x)}, a subtype. A descriptor
  is one the entry already passes, so the entry itself, with the evidence
  that it passes, is an inhabitant of every refinement descriptors build:
  each is non-empty constructively. That is [CLAIM-783](CLAIM-783.md)'s result that
  descriptors never conflict, the entry being their witness, said as a
  typing fact. An imposition refines toward a type the entry does not yet
  inhabit, which may be empty: the objection the record files when
  predicates conflict.
- **The direction of fit is bidirectional typing.** Bidirectional systems
  split typing into inference, which reads a type off a term (the type is
  written to fit the term: word to world, a descriptor), and checking, which
  holds a term to a type given in advance (world to word, a requirement).
  Checking only accepts or rejects; the performative update that moves the
  term to fit ([CLAIM-tmpmk056](CLAIM-tmpmk056.md)) is elaboration or coercion, which inserts
  what the term needs to inhabit the type.
- **Stored specification is a library.** [CLAIM-475](CLAIM-475.md)'s stored specification,
  past inquiry that cheapens later questions, is a library of definitions
  and lemmas, which make later types easy to state and inhabit and hard to
  state otherwise.

## Why the difference matters to the record

The record's practice is closer to the second. An entry that passes its
predicates is held with the evidence that it does: a claim with its grounds
and the premises it rests on, a reading with the passages that support it,
a status with the argument that moved it. The account of specification
says only that passing happens. Reading it type-theoretically would make
the evidence part of the realization, as the record's own entries already
treat it, and would make a question's revision ([CLAIM-470](CLAIM-470.md)'s one
difference) a change of type, which type theory handles with universes,
types computed from other types.

## What it does not say

- Not read. No source for these correspondences is held; they come from the
  assistant's knowledge, and [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md) plans the readings.
- Not that a claim's grounds are a proof in the formal sense. They are
  evidence of varying strength; the claim is that the record carries them
  with what they support, as a proof-relevant system does.
- Not that the record should adopt a type theory as its formalism.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-tmp1mruk ARG-tmptph3p ARG-tmp5r67s CLAIM-tmp764wb — Proposed or Rejected; filed from the reading for LEAD-tmp3xevc -->

Freeman and Pfenning 1991 ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md), corroborates; [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md); [LIT-tmp858eb](../literature.d/LIT-tmp858eb.md)), the
first of [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md)'s readings to bear on two of this claim's
correspondences.

- **A descriptor as a refinement the entry inhabits: borne out, narrowed**
  ([ARG-tmptph3p](../arguments.d/ARG-tmptph3p.md)). Their refinements are subsets of a type the term already has,
  and an annotation is accepted only when the term's inferred refinement
  already lies below it (RESTRICT, p. 8), moving nothing; a term with σ and
  τ has σ ∧ τ (p. 3), inhabited by its value. Three narrowings: the
  refinements are a finite lattice declared in advance, so {x : A | φ(x)}
  with φ arbitrary is predicate subtyping, not theirs; a refinement is of
  a type, not written from one term; and nothing is carried with the term,
  so "provably inhabits" means only that a derivation exists. The paper
  gives no support to the proof-relevant reading.
- **The direction of fit as inferring against checking: not borne out
  here** ([ARG-tmp5r67s](../arguments.d/ARG-tmp5r67s.md), Rejected as a route; [CLAIM-tmp764wb](CLAIM-tmp764wb.md), a counter). In their
  system checking an annotation is word to world, as inference is, and no
  rule moves a term. The paper is not bidirectional, so this leaves the
  correspondence untested rather than refuted; the reading of Dunfield and
  Krishnaswami is its test.

Neither reaches this claim's `defeated_if` (b), which asks for a
correspondence that fails on its own terms: the first holds narrowed, and
the second was not tested by this paper. No change to the claim's status.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-tmpei9b5 ARG-tmp7pf1t ARG-tmpdq64g CLAIM-tmpvq4ru — Proposed or Rejected; filed from the reading for LEAD-tmp3xevc -->

Davies and Pfenning 2000 ([THEORY-tmpei9b5](../theory.d/THEORY-tmpei9b5.md), corroborates; [NOTE-tmpaiy4v](../notes.d/NOTE-tmpaiy4v.md);
[LIT-tmp57uqz](../literature.d/LIT-tmp57uqz.md)), the paper that introduced bidirectional checking for
refinement types, and so the test the Freeman and Pfenning reading left
open for the bullet "The direction of fit is bidirectional typing".

- **Checking holds a term to a type given in advance: borne out,
  narrowed** ([ARG-tmp7pf1t](../arguments.d/ARG-tmp7pf1t.md)). The checked type is the programmer's
  ascription, passed down to subterms (pp. 6–8), and a term that fails it
  is the one to change: double fails, and "We leave the simple fix to the
  reader" (p. 10). Whether an ascription the term already meets is a
  requirement the paper does not say; [ARG-tmp7pf1t](../arguments.d/ARG-tmp7pf1t.md) sets out the two
  readings as alternatives for the owner.
- **Inference reads a type off the term: narrowed.** Most synthesized
  types are declared ones: an ascription "checks C against A and then
  yields A as the synthesized type" (p. 6), and variables synthesize what
  the context declares. Only constants are typed from their shape. The
  same ascription is a requirement on its term and a description to its
  uses.
- **The performative case is elaboration or coercion: not borne out
  here** ([ARG-tmpdq64g](../arguments.d/ARG-tmpdq64g.md), Rejected as a route; [CLAIM-tmpvq4ru](CLAIM-tmpvq4ru.md), a counter).
  Ascriptions are erased, subtyping is inclusion, "We avoid coercions"
  (p. 2), and the moves that make a failing term pass, the fix, an
  η-expansion, a lifted definition, are the programmer's. A coercive
  extension is called easy (p. 2), so this leaves the clause untested
  against an elaborating system rather than refuted.

Defeat condition (b) is not met: one correspondence holds narrowed, and
the elaboration clause names a mechanism this system lacks rather than one
that fails. No change to the claim's status.
