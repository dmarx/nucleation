---
number: 974
status: Proposed
formerly:
- CLAIM-tmpvq4ru
title: "In Davies and Pfenning's bidirectional refinement checking no rule moves a term: checking against a type given accepts or rejects, ascriptions are erased, and subtyping is inclusion, so no coercion is inserted; the change that makes a failing term pass is the programmer's and can change what the program does, so where checking is a mode of its own the performative update still lies outside the checker"
version: 1
role: counter
warrant: interpretive
defeated_if: >-
  A rule of the paper's checker (Figure 3) or of its type assignment system
  (Figure 1) that changes a term, inserts a coercion or a conversion, or
  otherwise produces from the checked term a different term that the
  erasure theorem does not map back to it; or a reading of the paper in
  which an ascription can be accepted for a term with no derivation
  against it. A later bidirectional system with elaboration or coercive
  subtyping would not defeat this claim, which is about this paper's
  system; it would restore CLAIM-949's clause for that system.
tags:
- logic
- philosophy-of-language
- software-engineering
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
objects_to:
- CLAIM-949
grounds:
- THEORY-2260
complements:
- CLAIM-965
uses:
- TERM-151
summary: >-
  Filed from the reading of Davies and Pfenning ([THEORY-2260](../theory.d/THEORY-2260.md),
  [NOTE-2351](../notes.d/NOTE-2351.md)) for [LEAD-215](../leads.d/LEAD-215.md). It objects to one clause of
  [CLAIM-949](CLAIM-949.md), that the performative case which moves a term to fit a
  type is elaboration or coercion, for the system that introduced
  bidirectional refinement checking: there no rule moves a term, and the
  move is the programmer's. It carries [CLAIM-965](CLAIM-965.md)'s finding about
  Freeman and Pfenning's inference over to a system in which checking is a
  mode of its own. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2260 CLAIM-949 CLAIM-965 TERM-151 CLAIM-943 — Proposed; the reading this rests on, the claim it objects to, the claim it complements, and the term and claim it is stated against -->

# CLAIM-974: In Davies and Pfenning's bidirectional refinement checking no rule moves a term: checking against a type given accepts or rejects, ascriptions are erased, and subtyping is inclusion, so no coercion is inserted; the change that makes a failing term pass is the programmer's and can change what the program does, so where checking is a mode of its own the performative update still lies outside the checker

## The claim

[CLAIM-949](CLAIM-949.md) reads the direction of fit ([TERM-151](../terms.d/TERM-151.md)) as bidirectional
typing's split, and adds: "Checking only accepts or rejects; the
performative update that moves the term to fit ([CLAIM-943](CLAIM-943.md)) is
elaboration or coercion, which inserts what the term needs to inhabit the
type." [CLAIM-965](CLAIM-965.md) found no such move in Freeman and Pfenning's system,
but that system infers and is not bidirectional.

Davies and Pfenning's is bidirectional ([THEORY-2260](../theory.d/THEORY-2260.md)): it "distinguishes
terms for which a type can be synthesized from terms which can be checked
against a given type" (p. 6). In it:

- **Checking accepts or rejects.** The rules are read so that "given Γ, C,
  and A we can check whether there is a derivation of Γ ⊢ C ↓ A" (p. 7).
- **Nothing is inserted.** An ascription "incurs no run-time overhead"
  (p. 6) and is erased, |C : A| = |C| (p. 7). "We avoid coercions by
  considering only subtype relations which are inclusions" (p. 2), so
  subsumption changes no term.
- **The move that fits a term is the programmer's.** double fails its
  ascription, and "We leave the simple fix to the reader" (p. 10). A
  non-value that needs an intersection is η-expanded by hand, which "only
  alters the semantics of the program when effects are involved" (p. 5). A
  well-typed term that cannot be annotated must be restructured "by
  lifting local function definitions" (p. 7).

So in the system that introduced bidirectional refinement checking, the
checking mode is world to word in where its type comes from ([ARG-211](../arguments.d/ARG-211.md)),
but the update that makes a failing term fit is not in the system. It is
the programmer's edit, outside the checker, and it can change what the
program does.

## What it does not say

- Not that elaboration or coercion never fits a term to a type. The
  authors call a coercive interpretation of subtyping an easy extension
  (p. 2), and later systems elaborate; the claim is about this one.
- Not that the clause of [CLAIM-949](CLAIM-949.md) fails on its own terms, which is
  that claim's `defeated_if` (b): it names a mechanism this paper lacks,
  and a reading of an elaborating system is its test.
- Not that the programmer's edit is unprincipled. The checker says where
  the term fails; it does not say how to change it.
