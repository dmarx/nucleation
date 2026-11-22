---
number: 215
status: Open
formerly:
- LEAD-tmp3xevc
title: 'Read the type-theoretic sources for the account of specification, propositions as problems, realizability, refinement types and bidirectional typing, to test the correspondences the record states from memory'
version: 4
stage: underway
priority: medium
method:
- reading
tags:
- logic
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
advances:
- CLAIM-949
summary: >-
  Filed beside [CLAIM-949](../claims.d/CLAIM-949.md) under the dialectic regime, 2026-11-22. That claim
  relates specification to type theory from the assistant's knowledge; no
  source is held. Candidates: Kolmogorov 1932 on the logic of problems;
  Kleene 1945 on realizability; Martin-Löf 1984, Intuitionistic Type
  Theory; Freeman and Pfenning 1991 on refinement types; Dunfield and
  Krishnaswami 2021, a survey of bidirectional typing. The owner started
  the readings on 2026-11-22, one delegated reader per work, each filed in
  its own pull request into staging.
---
<!-- inactive-ok-file: CLAIM-949 — Proposed; the claim this lead tests -->

# LEAD-215: Read the type-theoretic sources for the account of specification, propositions as problems, realizability, refinement types and bidirectional typing, to test the correspondences the record states from memory

## What to do

Register and read, under the read-and-file skill:

- Kolmogorov (1932), on the interpretation of intuitionistic logic as a
  calculus of problems: does a question as the record means it fit his
  problem?
- Kleene (1945), on realizability: how close is the record's realization to
  his realizer?
- Martin-Löf (1984), Intuitionistic Type Theory: types, universes, and what
  a change of type would mean for revising a question.
- Freeman and Pfenning (1991), on refinement types: is a descriptor's
  narrowing a refinement in their sense?
- Dunfield and Krishnaswami (2021), a survey of bidirectional typing: does
  inference against checking match the direction of fit, and where does
  elaboration sit?
- Rondon, Kawaguchi and Jhala (2008), Liquid Types: the predicate form
  {x : A | φ(x)} that [CLAIM-949](../claims.d/CLAIM-949.md) actually writes, which Freeman and
  Pfenning's finite lattice of refinements is not. Added 2026-11-22 at
  the owner's request, on the Freeman and Pfenning reader's suggestion.
- Davies and Pfenning (2000), on intersection types and computational
  effects: bidirectional refinement checking, the sharp test of the
  direction-of-fit correspondence that Freeman and Pfenning leave
  untested ([CLAIM-965](../claims.d/CLAIM-965.md)). Added the same day for the same reason.
- Proposed, not started (the owner's call): Flanagan (2006), Hybrid Type
  Checking, which inserts run-time checks where static checking cannot
  decide. It is the nearest case of the elaboration [CLAIM-949](../claims.d/CLAIM-949.md) names, which
  none of the three refinement systems read shows. Suggested by the Liquid
  Types reader.

## What would count

Each correspondence in [CLAIM-949](../claims.d/CLAIM-949.md) confirmed, narrowed or refuted against its
source, with the claim revised or defeated accordingly.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-2259 ARG-209 ARG-208 CLAIM-965 — Proposed or Rejected; filed from this reading -->

The fourth item, Freeman and Pfenning (1991), is read: [LIT-3127](../literature.d/LIT-3127.md), [NOTE-2350](../notes.d/NOTE-2350.md),
[THEORY-2259](../theory.d/THEORY-2259.md), with [ARG-209](../arguments.d/ARG-209.md), [ARG-208](../arguments.d/ARG-208.md) and [CLAIM-965](../claims.d/CLAIM-965.md) (pull request "Read Freeman and
Pfenning 1991"). A descriptor's narrowing is a refinement in their sense,
narrowed to a finite declared lattice and without carried evidence; their
intersection matches the witness argument, the witness being a value;
and in their system checking an annotation is word to world, as inference
is, so the bidirectional correspondence is left to the Dunfield and
Krishnaswami reading.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 ARG-211 ARG-212 CLAIM-974 — Proposed or Rejected; filed from this reading -->

Davies and Pfenning (2000), added to the readings at the owner's request,
is read: [LIT-3128](../literature.d/LIT-3128.md), [NOTE-2351](../notes.d/NOTE-2351.md), [THEORY-2260](../theory.d/THEORY-2260.md), with [ARG-211](../arguments.d/ARG-211.md),
[ARG-212](../arguments.d/ARG-212.md) and [CLAIM-974](../claims.d/CLAIM-974.md) (pull request "Read Davies and Pfenning
2000"). In the paper that introduced bidirectional refinement checking,
the checked type is the programmer's, given in advance, and a failing term
is the one to change; synthesis mostly passes on declared types; and no
rule moves a term, so the elaboration clause has nothing in this system to
map to. The value restriction gives the witness a second reason to be a
value. Whether a met ascription is a requirement is left to the owner, as
two alternatives in [ARG-211](../arguments.d/ARG-211.md).

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 ARG-214 ARG-213 CLAIM-975 — Proposed or Rejected; filed from this reading -->

Read beyond the five candidates, at the owner's request after the Freeman
and Pfenning reading: Rondon, Kawaguchi and Jhala 2008, "Liquid Types"
([LIT-3130](../literature.d/LIT-3130.md), [NOTE-2353](../notes.d/NOTE-2353.md), [THEORY-2262](../theory.d/THEORY-2262.md), with [ARG-214](../arguments.d/ARG-214.md),
[ARG-213](../arguments.d/ARG-213.md) and [CLAIM-975](../claims.d/CLAIM-975.md); pull request "Read Rondon, Kawaguchi and
Jhala 2008"). The descriptor as a refinement inhabited holds in the
predicate form, narrowed: inferable descriptors are conjunctions from a
finite qualifier set, checking is conservative, and no evidence is
carried. Inference is informative update, the strongest conjunction the
qualifiers and the check allow; checking moves nothing, and a failure may
lie in the program, the qualifiers or the checker. A reading the lead
might add: Flanagan 2006, "Hybrid Type Checking", which inserts the
run-time checks this paper proposes, the nearest case of the elaboration
[CLAIM-949](../claims.d/CLAIM-949.md) names. Offered, not added to the list here.
