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
<!-- inactive-ok-file: LIT-tmp9cdlq THEORY-tmpqj2d4 ARG-tmp68y3c — Proposed or Unavailable; the reading of Kleene through van Oosten that the dated note of 2026-11-22 cites -->
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

## Note of 2026-11-22: Kleene, read through van Oosten

Kleene 1945 (LIT-tmp9cdlq) has no lawful copy; van Oosten's historical
essay (LIT-tmpegqz0, read in NOTE-tmpajfia) stands in for it, and its account
is THEORY-tmpqj2d4. It bears on the bullet "A finding is an inhabitant":

- **Confirmed, as written.** A realizer of an existential is the witness
  kept with a realizer of its instance: "n realizes an existential
  statement ∃xφ(x) if and only if n = ⟨m, k⟩ and k realizes φ(m̄)" (p. 5).
  So "the record's realization, with the witness kept" holds.
- **Narrowed.** A Kleene realizer is not carried with the evidence that it
  passes. Realizability "is designed to handle “information” about
  formulas rather than proofs" (p. 4), and "n realizes F, where F is an
  atomic sentence, if and only if n = 0 and F is true" (p. 5): at a
  decidable test nothing is carried and the test is rechecked. The title's
  "an inhabitant carried with the evidence that it passes" gets no support
  from Kleene; its source would be proof-relevant type theory, Kreisel's
  typed realizability (1959, p. 11) or Martin-Löf, which this lead reads
  separately.
- **Qualified.** Realizability does not sit on the proof-relevant side of
  the claim's two. It is a classical relation between realizers and
  sentences, "read and checked by the classical mathematician" (p. 4), of
  the same shape as an institution's satisfaction (THEORY-1142), and in
  the effective topos it is the truth definition for arithmetic (p. 15). It
  is a model-theoretic semantics whose points are information, between the
  two readings.

The support judgement is ARG-tmp68y3c (analogy, Proposed); THEORY-tmpqj2d4
`corroborates` this claim for the witness correspondence. Neither the
defeated_if (a) nor (b) is met: the correspondences (b) names are not the
one Kleene bears on. No status changes; narrowing the claim is the owner's
call.
