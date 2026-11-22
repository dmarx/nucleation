---
status: Read
paper: LIT-tmp57uqz
title: 'Davies and Pfenning — Intersection Types and Computational Effects'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-tmp3xevc from the authors' copy,
    https://www.cs.cmu.edu/~fp/papers/icfp00.pdf, linked from Frank
    Pfenning's publications page at Carnegie Mellon: an author's copy on a
    faculty page, lawful under ADR-074. Eleven pages, all read, including
    Figures 1 to 4 (typing, reduction, checking and structural subtyping
    rules) and the examples of §5; the references were checked only for the
    works the text leans on. Page numbers below are the copy's (1 to 11),
    which are the proceedings' 198 to 208 less 197. Text extracted with
    pdftotext, page by page, and every quotation checked against it by
    script. Read directly by the filer, not delegated; no running-notes
    branch (ADR-108 is Proposed, and this session cannot delete remote
    branches). Davies' 2005 thesis was not consulted.
date: '2026-11-22'
summary: >-
  Intersection types, which refinement types need because one function
  has several properties, are unsound with mutable references. Restricting
  intersection introduction to values and dropping distributivity restores
  soundness, with a proof. Inference being most likely undecidable and
  principal types absent, the paper gives a bidirectional checker: types
  are ascribed by the programmer, mostly to function definitions, checked
  against and passed down to subterms, synthesized where they can be read
  off, and erased. No rule changes a term or inserts a coercion.
---
<!-- inactive-ok-file: ARG-tmp7pf1t ARG-tmpdq64g CLAIM-tmpvq4ru CLAIM-tmpnookt CLAIM-tmp764wb CLAIM-tmpmk056 CLAIM-783 TERM-134 TERM-tmp7s2aa TERM-tmp8b1yl TERM-tmp3mop8 THEORY-tmp1mruk — Proposed or Rejected; this reading's account, what was filed from it, and the entries it bears on -->

# NOTE-tmpaiy4v: Davies and Pfenning — Intersection Types and Computational Effects

## Contribution

Two things, both needed before refinement types could go into a real
language. First, a sound type system with general intersection types for a
call-by-value language with mutable references, obtained by a value
restriction on intersection introduction and by dropping distributivity.
Second, a source language with a bidirectional checking algorithm, sound
with respect to that system, which needs annotations mostly at function
definitions. "Taken together, we see our system and associated
type-checking algorithm as a significant step towards the introduction of
intersection types into realistic programming languages" (p. 1).

## Key results

1. **Why intersections (§1, p. 1).** "For practical purposes, refinements
   require at least some form of intersection types, because a given
   function may have more than one property": double has
   (nat → nat) ∧ (pos → pos). The paper drops Freeman and Pfenning's
   requirement that intersected types refine the same simple type: "We do
   not impose this additional requirement here, since it is orthogonal to
   both soundness in the presence of effects and the issue of
   bidirectional type checking" (p. 1).
2. **The counterexample (§1, pp. 1–2).** let x = ref (ε1) : nat ref ∧ pos
   ref; then x := ε; then !x : pos. "Certainly, both of these are valid
   types for x, since the contents of the cell is both of type nat and type
   pos" (p. 2); yet the result is ε, zero, not of type pos. "Similar
   counterexamples can be constructed for other computational effects such
   as exceptions" (p. 2).
3. **The value restriction (§2.3, pp. 3–5).** "the introduction rule for
   intersections is restricted to values" (p. 3): V : A and V : B give
   V : A ∧ B only for a value V (tp conj, Figure 1, p. 4). The proof shows
   why: for a non-value M with derivations at A1 and A2, a step of M may
   allocate a cell, and "a new cell allocated in C1 and C2 may be assigned
   a different type in ∆1 and ∆2. It is precisely this observation which
   gives rise to the counterexample in the introduction" (p. 6). Without
   allocation, "the language would be sound even without a value
   restriction as long as the ref type constructor is non-variant" (p. 6).
   The cost appears small, "particularly since non-values may be η-expanded
   to values ... This only alters the semantics of the program when effects
   are involved" (p. 5).
4. **No distributivity (§2.2, p. 3).** (A → B) ∧ (A → B′) ≤ A → (B ∧ B′) is
   omitted: with it, (λx. ref ε) at (unit → nat ref) ∧ (unit → pos ref)
   would give the non-value application a type nat ref ∧ pos ref, getting
   round the value restriction. "It is somewhat surprising, however, that
   it is possible to simply drop the rule and obtain a sensible system"
   (p. 3). The ref constructor must be non-variant: reading needs it
   covariant, writing contravariant (p. 6).
5. **Soundness (§2.4, p. 5).** Theorem 5, progress and type preservation,
   proved. The type system "does not admit principal types": ref (ε1) has
   bits ref, nat ref and pos ref, none below the others (p. 5).
6. **Why bidirectional (§2, p. 2; §3, p. 6).** "Type inference for this
   language is most likely undecidable, and principal types do not exist.
   Therefore we present a more practical source language which includes
   some type information and an associated bi-directional type checking
   algorithm" (p. 2); "type inference is impractical and principal types do
   not exist. In this section we present the core of a programming language
   which allows the programmer to specify types" (p. 6). Earlier explicitly
   typed proposals "required types to be given for each bound variable",
   which fails because "the programmer may wish to associate different
   types with a variable in different branches of the intersection
   introduction rule" (p. 6).
7. **The two modes (§3.1–3.2, pp. 6–7; Figure 3, p. 8).** "Our proposal
   instead distinguishes terms for which a type can be synthesized from
   terms which can be checked against a given type. This schema can type
   only normal forms, so we include an explicit type ascription C : A
   which checks C against A and then yields A as the synthesized type for
   the whole expression. Unlike a cast operation in some dynamically typed
   languages, however, this ascription incurs no run-time overhead. In
   practice, we mostly ascribe types to function definitions" (p. 6).
   Synthesis (Γ ⊢ I ↑ A) covers variables, applications, dereference,
   constants and ascriptions; checking (Γ ⊢ C ↓ A) covers λ, let, fix,
   ref, case and intersection introduction for values (tc conj). The
   checked type comes from an ascription and is passed down: a λ checked
   against A → B checks its body against B; an application synthesizes the
   function's type and checks the argument against its domain (ti app); a
   fix checks its body against the type given, once per conjunct. Rules
   are read as an algorithm: "given Γ, C, and A we can check whether there
   is a derivation of Γ ⊢ C ↓ A" (p. 7).
8. **Erasure, and no coercions (§2, p. 2; §3.3, p. 7).** "We avoid
   coercions by considering only subtype relations which are inclusions,
   but this is not an essential restriction of our approach" (p. 2); an
   inclusion interpretation "allows us to give an untyped operational
   semantics without explicit coercions ... and could easily be extended
   to a coercive interpretation of subtyping and intersections" (p. 2).
   The progress theorem shows "types may, but need not be carried at
   runtime" (p. 2). Theorem 7 (Soundness of Type Checking): a checked or
   synthesized term's erasure, |C : A| = |C|, has the type in the
   assignment system (p. 7).
9. **Completeness fails, and the programmer restructures (§3.3, p. 7).**
   "while we can often directly annotate programs which are well-typed
   according to the type assignment system in Section 2, we may sometimes
   need to restructure it by lifting local function definitions": for
   λx. let f = λy. x in f x at (nat → nat) ∧ (pos → pos), "there is no
   annotation that we can add for the type of f that allows us to
   type-check the term with this type" (p. 7).
10. **Examples (§5, p. 10).** inc : (bits → bits) ∧ (nat → pos) checks; "ascribing
    simply inc : nat → nat instead of nat → pos would have been
    insufficient", since the recursive call must be known positive. double
    : (nat → nat) ∧ (pos → pos) = λx. x 0 "will fail to type-check for
    x : nat. Indeed, double ε evaluates to ε 0 which is not a valid
    representation of zero. We leave the simple fix to the reader."
11. **Polymorphism (§4, pp. 7–10).** Parametric polymorphism is added to
    the assignment system as "the infinite analog of intersection
    polymorphism", with a value restriction and no distributivity, and
    Theorem 10 proved; checking is not extended to it, and the
    decidability of its subtyping is open (p. 9).

## Assumptions

A call-by-value core language with references, general fixed points and
one datatype, bits, with subtypes nat and pos. Subtyping is inclusion, so
there is one untyped semantics. Intersections need not refine one simple
type. The checker's rules are nondeterministic (all synthesized types are
enumerated); the authors are "investigating an algorithm which synthesizes
all types of an inferable term and tracks applicable ones through the use
of boolean constraints" (p. 7).

## Concepts

Intersection type; refinement type; value restriction; distributivity;
non-variant ref; type assignment against source language; inferable
(synthesized, ↑) and checkable (↓) terms; ascription C : A; ordinary type
and the conjunct judgment A ↑ B°; erasure; inclusion against coercive
subtyping; valuability restriction (Harper and Stone, p. 11).

## Bearing on the record

The brief's four questions, then the other bearings.

- **(a) Where the checked type comes from; requirement or description.**
  From the programmer's ascription, and from the context it is passed
  down through: a λ's body is checked against the codomain of the type its
  λ was checked against, an argument against the domain of the function's
  synthesized type, case branches against the type of the whole (result
  7). The paper's words for it are the programmer's: "allows the
  programmer to specify types" (p. 6); "many more properties of programs
  to be stated by the programmer and statically verified by a compiler"
  (p. 1). The programmer's intent enters only as an ascription; nothing is
  checked against an intent not written. When a term fails, the failure
  is the term's: double fails its ascription and "We leave the simple fix
  to the reader" (result 10); the ascription stands. In that case the
  checked type is world to word. Whether an ascription the term already
  meets (inc) is a requirement or a description the paper does not say;
  both of the record's readings fit it, [TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)'s that the term as
  it stands settles it, and the parallel reading of Dunfield and
  Krishnaswami (pull request 707) that a met requirement is still one
  ([ARG-tmp7pf1t](../arguments.d/ARG-tmp7pf1t.md)). One thing the paper adds: an ascription is both, by
  site. It is checked against its term and then "yields A as the
  synthesized type" (p. 6) for every use, where it is relied on without
  looking at the term. And most synthesized types are such declared
  types, read from the context, not off the term: only constants and
  their constructors (ε ↑ nat; I 1 ↑ pos) are read off the term's shape.
  So synthesis here is mostly not a type written to fit the term.
- **(b) Does any rule move or change a term?** No. Ascriptions are erased
  and incur no run-time overhead, subtyping is inclusion, and coercions are
  avoided by design (result 8). Checking accepts or rejects. The moves that
  make a term pass are the programmer's: the fix to double, η-expanding a
  non-value to meet the value restriction, which "only alters the
  semantics of the program when effects are involved" (p. 5), and lifting
  a local function so it can be annotated (result 9). So the paper extends
  [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md) from Freeman and Pfenning's inference to a bidirectional
  system ([CLAIM-tmpvq4ru](../claims.d/CLAIM-tmpvq4ru.md)), and gives no support to [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)'s clause
  that the performative case is elaboration or coercion ([ARG-tmpdq64g](../arguments.d/ARG-tmpdq64g.md)):
  in the system that introduced bidirectional refinement checking there is
  none. It does not refute the clause in general: the authors say a
  coercive interpretation would be easy (p. 2), and that would be one.
  The correspondence of direction of fit with the two modes is restored
  only in part: the checked type is given in advance and a failure is laid
  on the term, but the synthesized type is mostly not read off the term.
- **(c) The value restriction and the witness.** It bears on
  [TERM-tmp7s2aa](../terms.d/TERM-tmp7s2aa.md)'s caution that the witness must be a value, by a second
  route. Freeman and Pfenning's reason was termination: a diverging term
  can have the empty refinement. Here it is effects: a term that has A and
  has B need not have A ∧ B unless it is a value, because running it may
  allocate a cell that each derivation types differently (result 3). The
  witness argument, that whatever passes each of two tests passes both,
  holds for a value and fails for a computation still to run. A parallel
  for [CLAIM-783](../claims.d/CLAIM-783.md), which argues that descriptors never conflict because the
  entry witnesses them: the entry there is a version, a value, so the
  argument stands; the paper marks where it would stop, at predicates
  about what is still to be done to the entry. The cell's own type shows
  why: nat ref ∧ pos ref is true of the cell's contents now, but a ref
  type also governs future writes, so it is a requirement as well as a
  description, and two descriptions of the contents conflict as
  requirements on what may be written (result 4).
- **(d) Why bidirectional, and what must be stated in advance.** Inference
  "is most likely undecidable, and principal types do not exist" (result
  6), so the properties wanted are stated by the programmer, mostly at
  function definitions, and the rest flows from them. What must be stated
  is what cannot be read off: a function's several properties (its
  intersection), and an invariant strong enough for recursion, since a
  weaker true ascription for inc "would have been insufficient" (result
  10). This is the contrast with Freeman and Pfenning ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md)),
  whose inference was decidable because the refinements were a finite
  lattice declared in advance and only refinements of one type were
  intersected: there the distinctions are stated once, as declarations,
  and read off each term; here, with the restriction dropped, they are
  stated per function and checked.
- **[CLAIM-tmpmk056](../claims.d/CLAIM-tmpmk056.md)** (contrast). Again informative update only, inside
  the system; performative update is the programmer's. The η-expansion
  case adds that the change can alter behaviour.
- **[TERM-tmp3mop8](../terms.d/TERM-tmp3mop8.md)** (parallel). Types "may, but need not be carried at
  runtime" (p. 2) and are erased by compilation (Theorem 7): the checker
  produces no certificate kept with the term. A checked term is a witness
  whose derivation is discarded.
- **[TERM-134](../terms.d/TERM-134.md)** (parallel). With the vocabulary of refinements open, as
  here, they cannot be inferred and must be written; with it closed and
  declared, as in Freeman and Pfenning, they can be. The record's closed
  topics vocabulary is the second kind.

## Limitations

Checking is shown sound, not complete, and the paper gives no
characterization of which well-typed programs can be annotated; the
example of a local function that cannot be annotated is one case. The
checker as given is nondeterministic and its cost is not analysed; the
efficient algorithm is future work. Decidability of type inference is
asserted as "most likely undecidable", not proved, and so is the
decidability of subtyping with polymorphism (p. 9). Polymorphism is in the
assignment system only, not in the checker. The claim that the value
restriction costs little expressive power rests on the authors' examples
("Our present examples do not indicate this", p. 11). The paper does not
discuss elaboration, and coercion only as a possible extension. It does
not say whether an ascription is written before or after its term, so it
cannot settle whether a met ascription describes or requires.
