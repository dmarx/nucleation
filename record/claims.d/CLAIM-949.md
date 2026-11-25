---
number: 949
status: Proposed
formerly:
- CLAIM-tmpnookt
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
  (LEAD-215) shows that one of the correspondences named, question
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
- CLAIM-943
grounds:
- THEORY-1142
uses:
- TERM-152
- TERM-151
summary: >-
  Filed under the dialectic regime at the owner's "relate specification to
  type theory", 2026-11-22. The record holds the model-theoretic side of
  specification (Goguen and Burstall's institutions, [THEORY-1142](../theory.d/THEORY-1142.md), Active)
  and two type-theory works on other matters ([LIT-032](../literature.d/LIT-032.md), [LIT-040](../literature.d/LIT-040.md)), but no
  reading of propositions as types, realizability, refinement types or
  bidirectional typing; the correspondences below are stated from the
  assistant's knowledge and wait on [LEAD-215](../leads.d/LEAD-215.md). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-3213 THEORY-2309 ARG-244 — Proposed or Unavailable; the reading of Kleene through van Oosten that the dated note of 2026-11-22 cites -->

<!-- inactive-ok-file: THEORY-2310 ARG-247 CLAIM-1327 — Proposed; the reading of Dunfield and Krishnaswami (2021) and the entries filed from it, or the entries it bears on -->
<!-- inactive-ok-file: CLAIM-783 CLAIM-943 TERM-152 — Proposed or Open; the claims, terms and lead this joins -->

# CLAIM-949: The record's account of specification is model-theoretic, a set of tests and the versions that pass them all, as an institution pairs sentences with the models that satisfy them; type theory is its proof-relevant counterpart, in which a specification is a type, a question a problem, a realization an inhabitant carried with the evidence that it passes, adding a descriptor a refinement the entry provably inhabits, which is why descriptors cannot conflict, and the direction of fit is bidirectional typing's split between inferring a type from a term and checking a term against a type given

## Two ways to say what a specification is

**Model-theoretic, the record's own.** [TERM-152](../terms.d/TERM-152.md) defines a
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
  term to fit ([CLAIM-943](CLAIM-943.md)) is elaboration or coercion, which inserts
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
  assistant's knowledge, and [LEAD-215](../leads.d/LEAD-215.md) plans the readings.
- Not that a claim's grounds are a proof in the formal sense. They are
  evidence of varying strength; the claim is that the record carries them
  with what they support, as a proof-relevant system does.
- Not that the record should adopt a type theory as its formalism.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-2259 ARG-209 ARG-208 CLAIM-965 — Proposed or Rejected; filed from the reading for LEAD-215 -->

Freeman and Pfenning 1991 ([THEORY-2259](../theory.d/THEORY-2259.md), corroborates; [NOTE-2350](../notes.d/NOTE-2350.md); [LIT-3127](../literature.d/LIT-3127.md)), the
first of [LEAD-215](../leads.d/LEAD-215.md)'s readings to bear on two of this claim's
correspondences.

- **A descriptor as a refinement the entry inhabits: borne out, narrowed**
  ([ARG-209](../arguments.d/ARG-209.md)). Their refinements are subsets of a type the term already has,
  and an annotation is accepted only when the term's inferred refinement
  already lies below it (RESTRICT, p. 8), moving nothing; a term with σ and
  τ has σ ∧ τ (p. 3), inhabited by its value. Three narrowings: the
  refinements are a finite lattice declared in advance, so {x : A | φ(x)}
  with φ arbitrary is predicate subtyping, not theirs; a refinement is of
  a type, not written from one term; and nothing is carried with the term,
  so "provably inhabits" means only that a derivation exists. The paper
  gives no support to the proof-relevant reading.
- **The direction of fit as inferring against checking: not borne out
  here** ([ARG-208](../arguments.d/ARG-208.md), Rejected as a route; [CLAIM-965](CLAIM-965.md), a counter). In their
  system checking an annotation is word to world, as inference is, and no
  rule moves a term. The paper is not bidirectional, so this leaves the
  correspondence untested rather than refuted; the reading of Dunfield and
  Krishnaswami is its test.

Neither reaches this claim's `defeated_if` (b), which asks for a
correspondence that fails on its own terms: the first holds narrowed, and
the second was not tested by this paper. No change to the claim's status.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 ARG-211 ARG-212 CLAIM-974 — Proposed or Rejected; filed from the reading for LEAD-215 -->

Davies and Pfenning 2000 ([THEORY-2260](../theory.d/THEORY-2260.md), corroborates; [NOTE-2351](../notes.d/NOTE-2351.md);
[LIT-3128](../literature.d/LIT-3128.md)), the paper that introduced bidirectional checking for
refinement types, and so the test the Freeman and Pfenning reading left
open for the bullet "The direction of fit is bidirectional typing".

- **Checking holds a term to a type given in advance: borne out,
  narrowed** ([ARG-211](../arguments.d/ARG-211.md)). The checked type is the programmer's
  ascription, passed down to subterms (pp. 6–8), and a term that fails it
  is the one to change: double fails, and "We leave the simple fix to the
  reader" (p. 10). Whether an ascription the term already meets is a
  requirement the paper does not say; [ARG-211](../arguments.d/ARG-211.md) sets out the two
  readings as alternatives for the owner.
- **Inference reads a type off the term: narrowed.** Most synthesized
  types are declared ones: an ascription "checks C against A and then
  yields A as the synthesized type" (p. 6), and variables synthesize what
  the context declares. Only constants are typed from their shape. The
  same ascription is a requirement on its term and a description to its
  uses.
- **The performative case is elaboration or coercion: not borne out
  here** ([ARG-212](../arguments.d/ARG-212.md), Rejected as a route; [CLAIM-974](CLAIM-974.md), a counter).
  Ascriptions are erased, subtyping is inclusion, "We avoid coercions"
  (p. 2), and the moves that make a failing term pass, the fix, an
  η-expansion, a lifted definition, are the programmer's. A coercive
  extension is called easy (p. 2), so this leaves the clause untested
  against an elaborating system rather than refuted.

Defeat condition (b) is not met: one correspondence holds narrowed, and
the elaboration clause names a mechanism this system lacks rather than one
that fails. No change to the claim's status.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 ARG-214 ARG-213 CLAIM-975 — Proposed or Rejected; filed from the reading for LEAD-215 -->

Rondon, Kawaguchi and Jhala 2008 ([THEORY-2262](../theory.d/THEORY-2262.md), corroborates;
[NOTE-2353](../notes.d/NOTE-2353.md); [LIT-3130](../literature.d/LIT-3130.md)), the predicate form of refinement types,
read after Freeman and Pfenning's turned out to be a declared lattice.

- **A descriptor as a refinement the entry inhabits: borne out in the
  form written here, narrowed** ([ARG-214](../arguments.d/ARG-214.md)). Their base refinement
  {ν : B | e}, e any boolean expression, is "the set of values c of the
  base type B such that the predicate [c/ν]e evaluates to true" (p. 160):
  this claim's {x : A | φ(x)}. Inference only weakens a description until
  the program passes it, and the program never moves. Three narrowings:
  where a type is inferred, φ must be a conjunction of qualifiers from a
  finite set given in advance, no disjunction, which is what keeps
  inference decidable; a type given in advance can carry any predicate but
  is checked by a conservative implication check, so a predicate the term
  passes can fail to check; and nothing is carried with the term, so
  "provably inhabits" means only that the check succeeded.
- **The direction of fit as inferring against checking: half borne
  out** ([ARG-213](../arguments.d/ARG-213.md), Rejected as a route; [CLAIM-975](CLAIM-975.md), a counter).
  Inference is informative update. Checking against a type given in
  advance moves nothing, a program that fails is reported, and the failure
  may lie in the qualifier set or the checker rather than the program. The
  run-time checks the paper proposes inserting, by Flanagan's hybrid type
  checking, would be the elaboration this claim names; the paper does not
  do it, and the record has not read Flanagan.
- **Proof relevance: no support.** Derivations and solver checks are not
  kept; inferred types are printed "as documentation" (p. 167).

Neither reaches this claim's `defeated_if` (b): the first correspondence
holds narrowed, and the second is still untested on a bidirectional
system. No change to the claim's status.

## Note of 2026-11-22: Kleene, read through van Oosten

Kleene 1945 ([LIT-3213](../literature.d/LIT-3213.md)) has no lawful copy; van Oosten's historical
essay ([LIT-3221](../literature.d/LIT-3221.md), read in [NOTE-2420](../notes.d/NOTE-2420.md)) stands in for it, and its account
is [THEORY-2309](../theory.d/THEORY-2309.md). It bears on the bullet "A finding is an inhabitant":

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
  the same shape as an institution's satisfaction ([THEORY-1142](../theory.d/THEORY-1142.md)), and in
  the effective topos it is the truth definition for arithmetic (p. 15). It
  is a model-theoretic semantics whose points are information, between the
  two readings.

The support judgement is [ARG-244](../arguments.d/ARG-244.md) (analogy, Proposed); [THEORY-2309](../theory.d/THEORY-2309.md)
`corroborates` this claim for the witness correspondence. Neither the
defeated_if (a) nor (b) is met: the correspondences (b) names are not the
one Kleene bears on. No status changes; narrowing the claim is the owner's
call.

## Note of 2026-11-22: Dunfield and Krishnaswami, read

Their survey of bidirectional typing ([LIT-3247](../literature.d/LIT-3247.md), read in [NOTE-2421](../notes.d/NOTE-2421.md), account
[THEORY-2310](../theory.d/THEORY-2310.md)) tests the bullet "The direction of fit is bidirectional
typing". It supports, and narrows (evidence; [ARG-247](../arguments.d/ARG-247.md)):

- **Supported.** The authors call a synthesized type "a fact" and a
  checked one "a requirement" (§4.4), and argue for checking because
  inference "finds all behaviours, not only the intended behaviours"
  (§9.1). Synthesis as description and checking as requirement is their
  reading too. "Checking only accepts or rejects" is borne out: the term
  is an input in both modes (§1), and Coquand's checkExp "returns a
  boolean" (§9.1).
- **Narrowed.** The modes are information flow, "the management of
  information flow" (§8.4): which part of a judgment is known. They can
  be reversed, combined or refined (§6) while the term still answers for
  a mismatch, so where the type comes from is not who must fit whom.
  The two coincide in the standard Pfenning recipe. [CLAIM-1327](CLAIM-1327.md) files the
  objection this makes to [CLAIM-943](CLAIM-943.md).
- **Left open.** Elaboration and coercion are only cited (§1, references).
  The one change to a term the survey treats is the programmer's
  annotation, which under type erasure changes no behaviour (§2, §3.2).
  [LEAD-245](../leads.d/LEAD-245.md) plans the reading that would settle the elaboration clause.

Defeat condition (b) is not met: the correspondence holds, more narrowly
than stated. The status is the owner's.

## Note of 2026-11-22: Kolmogorov, read
<!-- inactive-ok-block: THEORY-2308 — Proposed; the reading of 2026-11-22, its argument and the claim it was read for -->

Kolmogorov, "Zur Deutung der intuitionistischen Logik" (1932), read in full
for [LEAD-215](../leads.d/LEAD-215.md) ([LIT-3229](../literature.d/LIT-3229.md), [NOTE-2422](../notes.d/NOTE-2422.md), [THEORY-2308](../theory.d/THEORY-2308.md)). It bears on the first
correspondence, a question as a problem, and on nothing else here.

**The correspondence is confirmed in what it asserts, and narrowed.** A
Kolmogorov problem, like [CLAIM-470](CLAIM-470.md)'s question, demands rather than asserts,
has no truth value ("für die Aufgaben hat man keinen dieser Richtigkeit
entsprechenden Begriff", p. 61, n. 8), fixes what counts as solving it and
may have many solutions; his conditional problems match questions under a
presupposition. It is narrower in two respects: a problem is solved or not
and has no answer space, so a question with several admissible answers is
a disjunction of problems, not one; and a problem's sense is "von dem
Zustand unserer Kenntnisse unabhängig" (p. 65), with a failed supposition
counted as solved (p. 59), so nothing in the calculus revises a problem as
[CLAIM-470](CLAIM-470.md)'s last clause revises a question. It is wider in one: fully
stated, a problem carries "die erlaubten Konstruktionsmittel" (p. 59,
n. 2), which the record puts in the inquiry ([TERM-095](../terms.d/TERM-095.md)), not the question.
[ARG-245](../arguments.d/ARG-245.md) argues this and does not find defeater (b) met.

**A correction of attribution.** The body's "Kolmogorov read a proposition
as a problem and its proof as a solution" is not this paper's. Kolmogorov
keeps statements and problems apart and faults Heyting because "bei Heyting
fehlt allerdings eine klare Unterscheidung zwischen Aussagen und Aufgaben"
(p. 65, n. 17). What he reads as problems are the formulas of intuitionistic
logic, whose objects "sind in Wirklichkeit keine theoretischen Aussagen,
sondern vielmehr Aufgaben" (p. 58). Identifying propositions with problems
is the later BHK and propositions-as-types gloss. A wording that fits the
reading: "Kolmogorov read the formulas of intuitionistic logic as problems,
kept apart from statements, and their proofs as solutions". The text and
status are unchanged; revising them is the owner's call.

## Note of 2026-11-25: Martin-Löf, read
<!-- inactive-ok-file: THEORY-2307 NOTE-2419 ARG-249 ARG-253 ARG-255 CLAIM-1208 CLAIM-1289 — Proposed or Skimmed; filed from the reading for LEAD-215 -->

Martin-Löf 1984, Intuitionistic Type Theory ([THEORY-2307](../theory.d/THEORY-2307.md),
corroborates; [NOTE-2419](../notes.d/NOTE-2419.md), Skimmed; [LIT-3232](../literature.d/LIT-3232.md)), the source this
claim names for "Martin-Löf's types are the same reading" and for
universes.

- **A question is a problem, a realization an inhabitant: borne out,
  narrowed** ([ARG-249](../arguments.d/ARG-249.md)). The book reads a ∈ A as "a method of solving
  the problem (doing the task) A" and as "a program ... which meets the
  specification A" (pp. 5–6), and makes the problem one reading of the
  same form of judgement as the set, which Kolmogorov, as the reading in
  pull request 708 reports, did not. Narrowed by [CLAIM-1289](CLAIM-1289.md): a
  Martin-Löf set is given by how its elements are formed, so a
  specification of tests is a type only over a kind of thing already
  given (the "such that" set, p. 53); over whatever might be proposed it
  is a category, which is not a set (p. 21).
- **A realization carried with the evidence that it passes, and a
  descriptor as a refinement inhabited: borne out, with the evidence
  kept** ([ARG-253](../arguments.d/ARG-253.md)). The elements of {x ∈ A : B(x)} "are pairs (a,b)
  with b ∈ B(a)", "the witnessing information" (p. 53). This is the first
  reading under [LEAD-215](../leads.d/LEAD-215.md) that supports the proof-relevant reading itself;
  the refinement systems kept no evidence.
- **Defeater (a) gets its test** ([CLAIM-1208](CLAIM-1208.md)). Martin-Löf drops a
  proof, writing "A true", only where nothing depends on it (pp. 33, 47);
  so the record is proof-relevant wherever a later step depends on an
  entry's evidence, as the status reviews do when they take a work out of
  a claim's grounds.
- **A question's revision as a change of type handled by universes:
  narrowed** ([ARG-255](../arguments.d/ARG-255.md)). A function into a universe computes a type
  from an earlier result (p. 91), but only among types the universe codes,
  which is the choice among answer spaces already admitted. A new form of
  set is outside every universe given, "because we are not able to
  exhibit once and for all all possible set forming operations" (p. 87).
  Whether the next universe meets it (reading A) or only an extension of
  the theory does (reading B, the filer's lean) is filed as alternatives
  in [ARG-255](../arguments.d/ARG-255.md).
- **The direction of fit as inference against checking: not tested.** The
  book gives rules, not an algorithm. **Stored specification as a
  library: not tested.**
- **Model-theoretic against proof-relevant.** The book sets itself
  against meaning given "only through semantics, which is usually done
  following Tarski and assuming set theory" (p. 3), the route
  [THEORY-1142](../theory.d/THEORY-1142.md)'s institutions take; so the claim's framing of the two
  accounts is the book's own.

Defeater (b) is not met: one correspondence holds with the evidence
carried, two hold narrowed, and the one on bidirectional typing was not
tested. No change to the claim's status.
