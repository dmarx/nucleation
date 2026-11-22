---
status: Read
paper: LIT-tmp858eb
title: 'Freeman and Pfenning — Refinement Types for ML'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 for LEAD-tmp3xevc from the authors' "To appear"
    preprint, https://www.cs.cmu.edu/~fp/papers/pldi91.pdf, linked from
    Frank Pfenning's publications page at Carnegie Mellon: an author's
    manuscript on a faculty page, lawful under ADR-074. Ten pages, all read,
    including Figure 1 (the type of CASE bitstr) and Figure 2 (the
    inference rules); the references were checked only for the works the
    text leans on. Page numbers below are the preprint's (1 to 10), not the
    proceedings' (268 to 277). Text extracted with pdftotext and every
    quotation checked against it by script. Read directly by the filer, not
    delegated; no running-notes branch (ADR-108 is Proposed, and this
    session cannot delete remote branches).
date: '2026-11-22'
summary: >-
  Refinement types narrow ML's types without changing its programs. The
  programmer declares recursive subtypes of a datatype; these close under
  intersection and union into a finite lattice; inference is abstract
  interpretation over it, after ML inference, and decidable because the
  lattice is finite and only refinements of one ML type are intersected.
  An expression has σ ∧ τ when it has both. Annotations are accepted only
  when the inferred refinement already lies below them. Soundness is
  stated and its proof omitted.
---
<!-- inactive-ok-file: ARG-tmp5r67s CLAIM-tmp764wb CLAIM-tmpnookt CLAIM-783 CLAIM-tmpmk056 TERM-134 TERM-tmp7s2aa TERM-tmp8b1yl — Proposed or Rejected; this reading's account, what was filed from it, and the entries it bears on -->

# NOTE-tmpew427: Freeman and Pfenning — Refinement Types for ML

## Contribution

A way to give ML more precise types without losing what makes ML's types
usable: decidable inference, principal types, no required annotations. The
programmer names the distinctions that matter (singleton lists, bitstrings
in standard form) as recursive subtypes of a datatype; the system infers,
for every expression already well-typed in ML, which of those subtypes its
value must belong to. The paper is a "preliminary report" on Mini-ML (p. 1),
with a prototype (p. 8).

## Key results

1. **Refinements are subsets of a type that already holds the term
   (abstract; §1, p. 1).** "refinement types are given only to programs
   which are already well-typed in ML"; "we do not extend the language of
   programs for ML (only the language of types)". The constructor names in
   a rectype declaration "stand for subtypes which one can think of as
   subsets": at any α, nil is {nil} and cons(X, Y) the lists
   cons(x, y) with x ∈ X, y ∈ Y.
2. **The distinctions are declared, and finitely many (§1, pp. 1–2).**
   "subtype distinctions ... must be made explicitly by the programmer in
   the form of recursive type declarations." Inference is "abstract
   interpretation over a programmer-specified finite lattice of
   refinements of each ML type. Finiteness is important, since it is
   necessary for the decidability of refinement type inference in our
   system." Some subsets cannot be declared: "lists without repeated
   elements ... and closed terms in a λ-calculus", which are not regular
   tree sets (p. 2).
3. **Intersection, restricted (§1, p. 2; §2.2, p. 3).** "Intuitively, an
   expression has type σ ∧ τ if it has both type σ and type τ." Unlike the
   general intersection type discipline, "we can only intersect types which
   are refinements of the same ML type", which is what keeps inference
   decidable without annotations: "Here we avoid explicit typing, while
   still retaining decidability". A principal refinement type is the
   intersection of all the types a term has; cons's is the intersection of
   (α ∗ α ?nil) → α singleton, (α ∗ α singleton) → α list and
   (α ∗ α list) → α list, "generated automatically from the rectype
   declaration" (p. 2).
4. **The lattice, and its bottom (§3, pp. 4–5).** A rectype declaration
   "induces a lattice of subtypes of a given ML datatype with the
   operations of ∧ and ∨, understood as meet and join". The system adds the
   refinements it needs (?e, the empty bitstring alone), and ⊥ is the
   bottom. In the bitstring lattice drawn on p. 5, ?e and stdpos meet only
   at ⊥, while "we do not need to write e : ?e ∧ std, since ?e ∧ std is
   equivalent to ?e" (p. 5).
5. **Function types (§4, pp. 5–6).** Subtyping is contravariant in the
   argument; intersections of arrows are compared argument by argument, and
   the rules are sound but incomplete: "it is quite possible that more
   subtype relationships hold than can be established with the rules
   above" (p. 6).
6. **Polymorphism (§5, pp. 6–7).** Refinement type variables are bounded
   by ML type variables, so a quantifier over refinements is a finite
   intersection once the ML type is fixed; id gets
   ∀α. ∀rα :: α. rα → rα.
7. **Inference and checking (§6, pp. 7–8; Figure 2).** The system "first
   performs an ML type inference pass and then a refinement type inference
   pass using abstract interpretation"; erasing the refinements from the
   rules gives "a conventional inference system for Mini-ML". Recursive
   functions are typed by LOOP, which starts at ⊥ and computes "successive
   approximations ... until a fixpoint is reached". Refinement types "will
   be inferred and printed by type inference, or can be used by the
   programmer to annotate expressions" (p. 3); the only rule for an
   annotation, RESTRICT, types (e : D′) at D′ when e has inferred type D
   and D ≤ D′ (p. 8). No rule changes a term.
8. **Soundness, stated (§6, p. 7).** "For all valid type environments Γ and
   expressions e, if e evaluates to v and Γ ⊢ e : D :: L then
   Γ ⊢ v : D′ :: L for some D′ ≤ D." The proof is omitted ("by induction on
   the structure of the definition of the 'evaluates to' relation").

## Assumptions

Mini-ML without products or multi-argument constructors; ML types are
inferred first and refinements are computed beneath them. A rectype
declaration must be consistent with the datatype it refines, and a
recursive refinement uses its own type variable unchanged. Datatype
constructors must be all covariant or all contravariant for subtyping to be
computed. Soundness is for terminating evaluation only.

## Concepts

Refinement type; rectype declaration; regular tree set; datatype lattice
(meet ∧, join ∨, bottom ⊥); intersection and union normal form; principal
refinement type; apptype; contravariance; refinement type variable bounded
by an ML type variable; abstract interpretation; RESTRICT; LOOP and the
fixpoint from ⊥.

## Bearing on the record

The lead's three questions, answered in turn.

- **(a) Is a descriptor's narrowing a refinement in their sense?** Yes in
  the sense that matters, narrowed. A refinement is a subtype of a type the
  term already has, every value of it being a value of that type (result
  1), and the one rule by which a programmer states a refinement of a term,
  RESTRICT, accepts it only when the term's inferred refinement already
  lies below it, and moves nothing (result 7). So an annotation accepted is
  a descriptor in [TERM-134](../terms.d/TERM-134.md)'s sense: the term passes it when it is added. In
  the record's terms, the ML type is the coarse specification, the
  principal refinement the narrowest the declared lattice can say of the
  term, and any refinement between the two is a descriptor it passes. Three
  narrowings. The refinements are a finite lattice declared in advance,
  not any predicate (result 2): the form {x : A | φ(x)}, with φ arbitrary,
  that [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) writes is predicate subtyping, not this paper's. A
  refinement is of a type, not of one term: the descriptor's being written
  from one entry has no counterpart. And nothing is carried with the term:
  that it has a refinement is a derivation the system finds and does not
  store, so "provably inhabits" holds only in the sense that a derivation
  exists.
- **(b) Their intersection, and when it is empty.** It matches
  [CLAIM-783](../claims.d/CLAIM-783.md)'s part 6 and [TERM-tmp7s2aa](../terms.d/TERM-tmp7s2aa.md): a term that has σ and τ has σ ∧ τ
  (result 3), and if it evaluates to a value, that value is in both, so
  the intersection is not empty; the paper's own e : ?e ∧ std is the case.
  Intersections can be empty, ⊥, as ?e ∧ stdpos is (result 4), and no
  value has both. Two cautions. The witness must be a value: a term whose
  evaluation does not terminate can have ⊥, so a term is a witness only
  through its value (result 8). And the paper never treats an empty
  intersection as a conflict to report; ⊥ is an ordinary refinement, the
  starting point of LOOP.
- **(c) What is inferred and what is checked.** Inferred: every
  refinement type, by abstract interpretation, with no annotation needed.
  Checked: an annotation, against the inferred type, by D ≤ D′. Both ask
  whether the term as it stands fits; neither moves it, and a term that
  fails an annotation has no such type, to be changed by the programmer.
  So this paper does not bear out [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md)'s identification of the
  direction of fit with inferring against checking ([ARG-tmp5r67s](../arguments.d/ARG-tmp5r67s.md), [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md)). It
  is not a bidirectional system, and the lead's reading of Dunfield and
  Krishnaswami is the test of that correspondence; what it shows is that a
  type given in advance and checked can be word to world
  ([TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)'s point that the thing as it stands sets the direction).
- **[CLAIM-tmpmk056](../claims.d/CLAIM-tmpmk056.md)** (contrast). The system has informative update only:
  narrowing by inference and by accepted annotations. Performative update,
  moving the term, lies outside it, with the programmer.
- **[TERM-134](../terms.d/TERM-134.md)** (parallel). The finite, declared lattice is a closed
  vocabulary: a distinction the declarations lack cannot be inferred, and
  is added by a new declaration, as the record adds a topic by decision.
  The paper's motive is the record's walk from prose to mechanism: "the
  programmer is encouraged to make explicit the distinctions which
  currently must remain implicit or informal in code comments" (p. 2).

## Limitations

A preliminary report: Mini-ML only, no products, a naive prototype. The
soundness proof is omitted, and so is the operational semantics; the
subtyping rules for function types are admitted incomplete. How a type
error arises is not shown: the lastcons example (p. 1) promises a
compile-time error on nil, but the application rule takes the
intersection of the result types whose argument types lie above the
argument's, and the paper does not say what an empty such intersection
yields. Termination of LOOP is argued from the finiteness of the lattice,
not proved. The paper says nothing of evidence or proof terms: whether a
refinement judgement could be carried with a value is outside it.
