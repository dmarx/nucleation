---
status: Proposed
title: 'Martin-Löf''s set of the elements such that a property holds, whose elements pair a witness with a proof that it has the property, shows by analogy that a realization passing a specification''s tests is held as an inhabitant carried with the evidence that it passes, and that the refinement a descriptor makes is inhabited with that evidence, the first reading under LEAD-215 in which the evidence is kept'
version: 1
form: analogy
grounds:
- THEORY-tmp62cvo
rests_on:
- CLAIM-783
concludes:
- CLAIM-949
uses:
- TERM-153
- TERM-154
- TERM-134
tags:
- logic
- epistemology
date: '2026-11-25'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  The route by which the reading of Martin-Löf (THEORY-tmp62cvo) bears on
  CLAIM-949's proof-relevant reading, LEAD-215's questions (b) and (e): a
  realization as an inhabitant carried with its evidence, and a descriptor
  as a refinement the entry provably inhabits. The three refinement systems
  read before kept no evidence (ARG-209, ARG-214); here the evidence is
  the second component of every element of {x ∈ A : B(x)} (p. 53). The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp62cvo CLAIM-949 CLAIM-783 TERM-153 TERM-154 ARG-209 ARG-214 — Proposed; the reading, the claims, the terms and the earlier arguments this joins -->

# ARG-tmpneexr: Martin-Löf's set of the elements such that a property holds, whose elements pair a witness with a proof that it has the property, shows by analogy that a realization passing a specification's tests is held as an inhabitant carried with the evidence that it passes, and that the refinement a descriptor makes is inhabited with that evidence, the first reading under LEAD-215 in which the evidence is kept

## The inference

Source, THEORY-tmp62cvo: "To have an element a ∈ A such that B(a) holds
means to have an element a ∈ A together with a proof of B(a), namely an
element b ∈ B(a). So the elements of the set of all elements of A
satisfying B(x) are pairs (a,b) with b ∈ B(a), i.e. elements of
(Σx ∈ A)B(x)" (p. 53). A canonical proof of (∃x ∈ A)B(x) "is a pair
(a,b), where b is a proof of the fact that a satisfies B" (p. 42); the
projections give the witness p(c) ∈ A and the proof q(c) ∈ B(p(c))
(pp. 44–46). Conjunction is the Σ over a constant family, A & B = A × B
(p. 43), with pairs of proofs as its elements (p. 44).

Target, CLAIM-949 with CLAIM-783, TERM-153 and TERM-154: a realization is
an inhabitant carried with the evidence that it passes; a descriptor
refines the specification to {x : A | φ(x)}, which the entry provably
inhabits; descriptors never conflict, the entry witnessing them all.

Mapping: a to the entry (TERM-154's witness); b to the evidence that it
passes (TERM-153's certificate); the "such that" set to the refinement a
descriptor makes; a pair of proofs of B(a) and C(a) to the evidence that
the entry passes two descriptors at once.

## Critical questions

- **Are the two alike in the respects the conclusion needs?** Yes, and in
  the respect the earlier readings lacked. Freeman and Pfenning's and the
  liquid refinements hold a term in a refinement by a derivation found and
  not kept (ARG-209, ARG-214); here the refinement's elements are the pairs,
  so the evidence is part of what inhabits it. The book's example shows it
  doing work: a real is "a sequence of rational numbers toghether [sic]
  with a proof that it satisfies the Cauchy condition", and "Only by means
  of the proof q(c) do we know how far to go for the approximation
  desired" (pp. 53–54).
- **Does the witness argument of CLAIM-783 carry over?** Yes, with the
  certificate. If a ∈ A, b ∈ B(a) and c ∈ C(a), then (b,c) ∈ B(a) & C(a)
  and (a,(b,c)) ∈ (Σx ∈ A)(B(x) & C(x)), by &-introduction and
  Σ-introduction (pp. 39, 44). The derivation is the filer's, from the
  book's rules; the book does not state it.
- **Are there differences that defeat it?** Two that narrow it. The
  record's evidence is not a construction in the book's sense: a claim's
  grounds are evidence of varying strength, as CLAIM-949 itself says, and
  a NOTE's quotations are not a method that computes anything. And the
  book distinguishes a proof of a proposition, the element b, from a proof
  of the judgement b ∈ B(a), a derivation (p. 6); TERM-153 calls the
  certificate "the derivation that x satisfies φ", which is the second, so
  the term runs the two together. Neither defeats the analogy, which is
  about what is carried with a realization, not about its formal status.

## Verdict

Supports CLAIM-949's proof-relevant reading and its descriptor
correspondence, with the evidence carried, as no refinement system read
under LEAD-215 does. Proposed.
