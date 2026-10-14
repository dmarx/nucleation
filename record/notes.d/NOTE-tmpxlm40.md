---
status: Read
paper: LIT-956
title: 'Sayed Ahmed — Back and forth between algebraic geometry, algebraic logic, sheaves and forcing'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arXiv:1811.01754v1, 2 November 2018,
    the only version, 36 pp.), text extracted with pdftotext: §§1–7 and
    the single reference. The sheaf, topos and Heyting parts (§2, §5,
    §5.2) were read closely, the duality and forcing parts (§§3–4, 6–7)
    in full but without checking the cylindric-algebra examples against
    Comer or Németi, which are not held. The paper is not the long
    survey the filing expected: it is a short research note whose main
    theorems are stated with sketched proofs or none.
date: '2026-10-14'
summary: >-
  Distributive lattices with join-preserving idempotent operators are
  represented, after Comer, as continuous sections of a sheaf of
  quotient algebras over the prime spectrum of their fixed-point part. A
  small site is said to give a notion of forcing, with Kripke–Joyal
  clauses, and a Łukasiewicz conjunction is forced through a tensor
  product. Most theorems are stated without proof, and negation is never
  written out.
---
<!-- inactive-ok-file: THEORY-037 CLAIM-038 — Proposed; the account and claim this reading bears on, named and not leaned on -->

# NOTE-tmpxlm40: Sayed Ahmed — Back and forth between algebraic geometry, algebraic logic, sheaves and forcing

## Contribution

The paper sets two uses of sheaves side by side. In the first, a bounded
distributive lattice with operators (a "BLO") is recovered as the
algebra of continuous sections of a sheaf whose stalks are its quotients
by the prime ideals of its "zero-dimensional" part. This generalises
Comer's sheaf duality for cylindric algebras and, with two-element
stalks, Stone duality. In the second, presheaves on a site are used as
the universe of a forcing construction, with an added clause for a
Łukasiewicz conjunction. Little of either is new as stated, and the new
parts are announced more than proved.

## Key insight

An algebra of formulas is the gluing of its complete extensions. Each
point of the base is a complete theory, each stalk the formulas modulo
that theory, and a formula is the section that picks its class at every
point (Example 2.6). Forcing is the same move turned round: forcing
conditions are the objects of a site, and the "ramified language" is
their Yoneda image in presheaves (Theorem 5.1).

## Assumptions

- **Distributivity throughout.** Every algebra in §§3–4 and 7 has a
  bounded distributive lattice reduct. Nothing is said about
  non-distributive or orthocomplemented lattices.
- **BLO operators** (Definition 3.5) preserve order and joins, are
  idempotent, fix 0 and 1, and have finite "dimension sets". The
  zero-dimensional part Zd A is their common fixed points.
- **Theorem 4.1** assumes an object C whose contravariant hom functor
  is an equivalence between the lattice reducts and their Priestley
  spaces.
- **A site** is "a cartesian category C with a notion of localization",
  localizations stable under pullback (Definition 2.3). Theorem 5.1
  needs it small.
- **Definition 2.4** defines a topos as "a functor category of sheaves",
  which is narrower than the elementary topos the paper also describes
  (p. 8) and is not the standard definition.

## Key results

- **Example 2.2.** In Set^P, the truth-value object Ω(p) is the family
  of upward-closed sets over O_p = {q : p ≤ q}, with restriction
  U ↦ U ∩ O_q. For a complete Heyting algebra H, sheaves on H, the
  Heyting-valued universe V^H and the category Set_H of H-valued sets
  are "equivalent" (stated, no proof given; this is Fourman and Scott's
  result, not cited).
- **Example 2.6.** A theory T of a multi-dimensional modal logic is the
  algebra of continuous sections of the sheaf ⋃_{∆ ∈ X_T} {∆} × Fm/∆
  over the Stone space of its complete extensions.
- **Theorem 4.1.** For A with Priestley space X of Zd A and stalks
  G_x = A/Ig^A(x), A ≅ Hom_top(Hom(Zd A, 2), ⋃_{x∈X} G_x), naturally.
  No proof is given. The map η(a) = σ_a is said to be "as easily
  checked an isomorphism".
- **Theorem 5.1.** A small algebraic site defines a notion of forcing,
  with presheaves on it as names. The Kripke–Joyal clauses are listed
  for ∈, =, ∧, →, ∨, ∀, ∃ (p. 19): I ⊩ φ → ψ iff for every u : J → I,
  J ⊩ φ(c.u) implies J ⊩ ψ(c.u). The ∨ and ∃ clauses are printed
  without the covering families a Grothendieck topology requires. There
  is no clause for ¬, and no pseudo-complement is ever written.
- **Fuzzy forcing (§5.1).** I ⊩ φ ⊗ ψ iff there is a monomorphism
  u : J → I with I ⊗ J ⊩ φ ∧ ψ, the tensor induced from a monoidal site
  by Yoneda. "We will give an equivalent definition below" is not
  fulfilled.
- **§5.2.** For a many-sorted higher-order theory T, the category E(T)
  of definable types and total functions is a topos whose subobject
  classifier's global elements form the Lindenbaum–Tarski algebra of T,
  and E(T) ≃ Set^Ω. With an MV algebra the corresponding category of
  fuzzy sets is only a quasi-topos with an "almost" subobject
  classifier; identifying ⊗ with ∧ gives a Heyting algebra H whose
  category is a reflective subcategory (Theorems 5.3–5.5, stated
  without proof).
- **§6.** An MV-valued universe V^L with ‖x ∈ y‖ = Σ_t (‖x = t‖ ⊗ y(t))
  and ‖x ⊆ y‖ = Π_t (x(t) ⊗ (1 → ‖t ∈ y‖)) (p. 28); Theorem 6.1 (V^L
  models MV predicate logic with extensionality, pairing, infinity and
  power set, "like the standard proof"); Theorems 6.3–6.4 (truth in a
  generic extension). Theorem 6.6 claims Zorn's lemma holds in V^B while
  choice is independent. Its proof uses the Heyting algebra O(ℕ^op) and
  calls it an MV algebra "because it is linear". A linear Heyting algebra
  is a Gödel algebra, whose conjunction is the minimum, not Łukasiewicz's,
  so the step is doubtful.
- **§7.** Grätzer–Schmidt (Theorem 7.2, sketched): ideals correspond
  isomorphically to congruences iff the lattice is distributive and
  relatively complemented with 0. Regular ideals of Γ(X, δ) correspond
  to open subsets of X (Theorem 7.5). If simple lattices in a class have
  amalgamation and some strongly regular pair has a non-surjective
  epimorphism, then epimorphisms fail to be surjective among the simple
  lattices (Theorem 7.6, the one theorem proved in full). Corollaries
  for cylindric, quasipolyadic and Pinter's algebras rest on the
  author's earlier and "preprint" results.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A BLO is isomorphic to the continuous sections of its dual sheaf over the Priestley space of its zero-dimensional part | weak | Theorem 4.1, stated; the isomorphism is "easily checked" |
| C2 | A small site gives a notion of forcing whose names are presheaves | weak | Theorem 5.1, a sketch reproducing the standard presheaf construction |
| C3 | Łukasiewicz conjunction can be forced through a tensor product on a monoidal site | weak | one defining clause, §5.1 |
| C4 | Many-valued theories are interpreted in a quasi-topos with an almost subobject classifier | weak | Theorems 5.3–5.5, stated |
| C5 | Failure of surjective epimorphisms transfers from strongly regular to simple algebras under amalgamation | moderate | Theorem 7.6, proved via the duality |

## Concepts

- **BLO.** A bounded distributive lattice with join-preserving,
  idempotent unary operators, abstracting quantifiers as modalities.
- **Zero-dimensional part Zd A.** The elements every operator fixes; for
  a locally finite algebra of formulas, the sentences.
- **Stalk G_x.** The quotient A/Ig^A(x) at a prime ideal x of Zd A.
- **Regular ideal.** One generated by its intersection with Zd A.
- **Ramified language.** The names of a forcing construction, here the
  presheaves on the site of conditions.
- **Almost subobject classifier.** The paper's term for the Heyting
  reduct H that classifies subobjects in the reflective subcategory but
  not in the quasi-topos of fuzzy sets.

## Connections

The sheaf duality is Comer's for cylindric algebras, itself a
generalisation of Stone duality, here moved to Priestley spaces for
distributive lattices. The forcing material follows the standard
presheaf and Heyting-valued constructions (Scott, Fourman–Scott, the
Kripke–Joyal semantics) and the logic of partial elements cited to
"[Handbook]". The epimorphism results continue Madarász and Sayed Ahmed
(2007), the only work in the bibliography. None of these is held.

## Bearing on the record

- **[QUESTION-055](../questions.d/QUESTION-055.md) and [LIT-956](../literature.d/LIT-956.md)'s own status note.** The LIT says the paper
  "supplies the sheaf and topos machinery behind the Heyting-over-contexts
  option for negation". It does so only weakly. It states that truth
  values over a poset of conditions are upward-closed sets and that the
  logic of sheaves on a Heyting algebra is intuitionistic. But it never
  writes negation or the pseudo-complement, never treats a site of
  contexts, and proves none of these facts. A textbook source would serve
  the question better.
- **[THEORY-037](../theory.d/THEORY-037.md).** Its promote_when asks for a proof that the clopen
  sub-objects of the spectral presheaf form a Heyting algebra, and
  excludes "the general fact that Sub(X) is Heyting in any topos". This
  paper offers at most that general fact, and asserts it rather than
  proving it. It cannot promote [THEORY-037](../theory.d/THEORY-037.md) and does not bear on
  daseinisation.
- **[CLAIM-038](../claims.d/CLAIM-038.md) (a communicative object as a context-indexed system).** The
  paper's sheaves are over prime spectra of distributive lattices and
  over forcing posets, not over a cover of contexts. It neither
  supports nor tests [CLAIM-038](../claims.d/CLAIM-038.md).
- **[THEORY-042](../theory.d/THEORY-042.md) (sectors).** The record's observation, not the paper's: the
  representation of Theorem 4.1 is a product of stalks glued over the
  spectrum of a fixed-point subalgebra, the same shape as an algebra
  decomposed over its centre into sectors. It is proved here, if at all,
  for distributive lattices, not for the orthomodular lattices that
  [THEORY-042](../theory.d/THEORY-042.md) concerns.
- **No THEORY is filed.** What the paper asserts is either standard and
  better sourced elsewhere, or stated without proof.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Theorems 4.1, 5.1 and 5.3–5.5 are stated with sketches or without
  proof, and Theorem 7.3 is proved by "Easy". Several clauses are
  garbled in the text (Definition 3.2(2), the ∨ clause on p. 19).
- The Zorn's-lemma argument (Theorem 6.6) treats a Gödel algebra as an
  MV algebra.
- The paper has one reference, the author's own; the results it relies
  on (Comer, Fourman–Scott, Kripke–Joyal, Grätzer–Schmidt, Németi) are
  named in passing or not at all.
- It concerns distributive lattices only. Nothing in it reaches the
  orthocomplemented or orthomodular case.

## Open questions

- Does a Comer-style sheaf representation exist for orthomodular
  lattices over the spectrum of their centre, and does it reproduce the
  superselection product of [THEORY-042](../theory.d/THEORY-042.md)? The paper does not ask.
- A proof of Theorem 4.1, and a forcing clause for negation in the
  fuzzy case, are left to be supplied.
