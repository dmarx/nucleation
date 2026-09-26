---
number: 69
status: Read
formerly:
- NOTE-tmpoux3y
paper: LIT-032
title: 'Riehl & Shulman, type theory for synthetic ∞-categories'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv 1705.07442v5 (8 Jun 2023, 78 pp.),
    downloaded to raw4/1705.07442.pdf and extracted with PyMuPDF to
    raw4/1705.07442.full.txt and .j.txt. I read §§1–11, Appendix A (A.1–A.3)
    and the references, all of it. The inference-rule figures (Figs. 1–4)
    and the commutative diagrams (Figs. 5–7, the prism and simplex diagrams
    in §§5, 8, 11 and A) came through the extraction as flattened symbol
    runs. I read them against the surrounding prose, but I could not check
    every premise of every rule, nor the labelled faces of the 3-simplices
    in Figs. 5–7. I followed each proof in §§3–10 step by step at the level
    of its argument. I followed the §11.2 prism argument (Theorem 11.14)
    only in outline. I did not collate v5 against the Higher Structures
    1(1):147–224 version.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  A three-layer type theory adds a directed interval 2 to HoTT. Its layers
  are cubes, topes (the coherent theory of a strict interval) and types,
  and simplices become shapes that can be mapped out of by extension
  types. One contractibility condition, "Segal" (unique fillers for the
  2-1-horn), then yields associativity (Prop. 5.9) and 3-horn fillers
  (Prop. 5.21). It also makes every function a functor (Prop. 6.1), gives
  a dependent Yoneda lemma for covariant families (Thm. 9.5), and makes
  having a left adjoint a proposition when the adjoint's codomain is Rezk
  (Thm. 11.23). The bisimplicial-sets semantics is sketched. Segal and
  Rezk types are shown to match Segal and complete Segal spaces (Props.
  A.21, A.25), and soundness is not proved in full.
---

<!-- inactive-ok-file: LIT-040 — Deferred; the nLab two-level type theory page, named in Connections -->

# NOTE-069: Riehl & Shulman, type theory for synthetic ∞-categories

## Contribution

The paper gives the first workable synthetic theory of (∞,1)-categories inside homotopy type theory. It does not interpret types directly as categories, which runs into non-exponentiable maps and a proliferation of fibration kinds. Instead it keeps ordinary HoTT, interpreted in Reedy bisimplicial sets, and adds a strict directed interval 2. The category-like types are then *identified internally* as Segal and Rezk types. The route is Joyal's suggestion, pursued independently here (§1).

The technical device is a separate "shape" layer with extension types ⟨Π_{t:I|ψ} A | ^φ_a⟩. These let one say "an arrow f : 2 → A with f(0) ≡ x and f(1) ≡ y" *judgmentally* without non-fibrant types. The device is due to Lumsdaine and Shulman and was unpublished before this paper.

With it, the paper develops:
- composition, associativity and homotopies;
- functors and natural transformations;
- discrete types (the groupoids);
- covariant families and the Yoneda lemma;
- Rezk completeness;
- adjunctions.

The (∞,1)-coherence is free wherever it can be.

## Key insight

HoTT gets all the higher structure of ∞-groupoids for free from one rule, identity elimination. This paper gets the higher structure of (∞,1)-categories from one contractibility condition, stated in the internal language: Σ_{h} hom²_A(f, g; h) is contractible.

The single condition does so much because it is internal. Semantically it asserts that X^{Δ²} → X^{Λ²₁} is an equivalence *of bisimplicial sets*, and so it holds uniformly in every dimension. Applying it to A^2 (Cor. 5.6), and using the fact that products of simplices contain higher simplices, gives associativity (Prop. 5.9) and the inner 3-horns (Prop. 5.21) without a separate axiom.

Also, because every term of type theory is automatically compatible with the structure, every function between Segal types is a functor and every arrow in a function type is a natural transformation (§6). No coherence has to be checked by hand.

## Assumptions

- **Base theory.** This is intensional Martin-Löf type theory with:
  - Σ, Π (judgmental η), coproducts, identity types and a universe (notational only, Remark 2.5);
  - function extensionality.

  It has no univalence and no HITs (§2.1).
- **Three layers (§2).**
  - Cubes: finite products of 2.
  - Topes: ∧, ∨, ⊤, ⊥ and ≡, with no negation, implication or quantifiers.
  - Types: dependent on cube and tope contexts.
  - Tope equality is judgmental equality (rule 2.2).
  - Substitution into judgmental equality (∗) is *taken as a primitive rule*, because rule 2.2 breaks its admissibility (p. 10, credited to Licata).
- **Strict interval axioms (§3.1).** ≤ is reflexive, transitive, antisymmetric and total, with 0 ≤ x ≤ 1 and (0 ≡ 1) ⊢ ⊥.
- **Cofibrations are shape inclusions in the empty context.** A shape inclusion may not depend on Ξ or Φ. This restriction is semantically forced, because Leibniz exponentials do not stay fibrations in slices (p. 73–74).
- **Axiom 4.6, relative function extensionality.** An extension type of a family of contractible types is contractible. The authors do not know whether the other two funext formulations are equivalent for extension types. They show 4.8(ii) together with the homotopy extension property (Prop. 4.10) implies 4.6 (Prop. 4.11).
- **Only the smallest simplices.** Only n ≤ 3 is used, and Δⁿ is a meta-theoretic schema, not an internal family (p. 14). The general inner-horn statement is "presumably" a theorem-schema (p. 31) and is not proved.
- **Semantics (App. A).**
  - The model is the Reedy model structure on bisimplicial sets, with universes from Shulman 2015 (Thm. A.3).
  - It generalises to any right-proper Cisinski "model category with T-shapes" (Def. A.13), with Examples A.14–A.15.
  - Soundness is assumed modulo Lumsdaine–Warren coherence and an initiality theorem, neither proved (p. 66, Thm. A.18).

## Key results

- **Thm. 5.5.** A is Segal iff restriction (Δ² → A) → (Λ²₁ → A) is an equivalence.
- **Cor. 5.6.** Π-types of Segal types are Segal. This includes A^X for X a type *or a shape*.
- **Prop. 5.8 and 5.9.** Composition in a Segal type has identity laws (id_y ∘ f = f, f ∘ id_x = f) and is associative, (h ∘ g) ∘ f = h ∘ (g ∘ f). Associativity comes from applying the Segal condition to A^2 and restricting along the "middle shuffle" Δ³ → Δ² × 2.
- **Prop. 5.10 and 5.12.** (f = g) ≃ hom²_A(id_x, f; g), and (g ∘ f = h) ≃ hom²_A(f, g; h). Homotopies are the same as 2-simplices.
- **Prop. 5.20 and 5.21.** Pushout products of inner anodyne maps with cofibrations are inner anodyne, and the 3-1- and 3-2-horn inclusions are inner anodyne. The proof is Joyal's lemma rewritten with interval coordinates. The formal check needs 30 cases, which are left to "automation".
- **Prop. 6.1 and 6.3–6.6.** Every function between Segal types preserves identities and composition. Also:
  - hom_{A→B}(f, g) ≃ Π_a hom_B(fa, ga), called "transformation extensionality", which is a judgmental isomorphism;
  - naturality squares commute (Prop. 6.6);
  - horizontal composition carries a Gray interchanger (§6.3).
- **Prop. 7.3.** Discrete types (idtoarr an equivalence) are Segal.
- **Prop. 10.10.** A type is discrete iff it is Rezk and all its arrows are isomorphisms.
- **Thm. 8.5.** C : A → U is covariant iff the square C̃^2 → A^2 over C̃ → A (both by ev₀) is a homotopy pullback.
- **Thm. 8.8.** The total space of a covariant family over a Segal type is Segal. The paper gives both a type-theoretic and a categorical proof.
- **Prop. 8.13 (v5-repaired).** λx. hom_A(a, x) is covariant iff A is Segal.
- **Prop. 8.18 and Cor. 8.19.** The fibres of a covariant family over a Segal type are discrete, so hom_A(x, y) is discrete.
- **Prop. 8.21 and Thms. 8.26, 8.30–8.31.** Multivariable covariance holds iff covariance holds in each variable, and identity types of a covariant family form a covariant family. Π over a covariant family is covariant, and maps from a covariant family into a discrete Y form a contravariant family.
- **Thm. 9.1, the Yoneda lemma.** For A Segal, C covariant and a : A, evid : (Π_x hom(a, x) → C(x)) → C(a) and yon are inverse equivalences. Naturality in a is automatic, and naturality in C is Lemma 9.2.
- **Thm. 9.5, the dependent Yoneda lemma.** For C : Π_x (hom(a, x) → U) covariant, evaluation at (a, id_a) is an equivalence. It is derived from "initial objects": (a, id_a) is initial in Σ_x hom(a, x) (Lemma 9.8, Thm. 9.7). The inverse is yon(u, x, f) := (Λf)_* u (eq. 9.9). The paper reads this as a directed form of path induction.
- **Prop. 10.2.** isiso(f) is a proposition.
- **Prop. 10.3 and Cor. 10.4.** Natural isomorphisms are pointwise isomorphisms.
- **Prop. 10.9.** Rezk types are closed under X → −.
- **Thm. 11.8.** For Segal A and B, quasi-transposing adjunctions are equivalent to quasi-diagrammatic adjunctions. The proof goes component by component through Yoneda.
- **Thm. 11.13 and 11.14.** For Segal A and B, bi-diagrammatic adjunctions (two counits ε and ε′, each with one triangle identity) are equivalent to transposing adjunctions, and so are half-adjoint diagrammatic adjunctions (with μ, ω, τ matching Riehl–Verity's parental subcomputads).
- **Cor. 11.21 and 11.22.** Given (f, u, η), the adjunction data forms a proposition, and so does the data given (f, u, η, ε, α).
- **Thm. 11.23.** For A Segal, B Rezk and u : B → A, the types of left adjoints of u (transposing, half-adjoint, bi-diagrammatic, and truncated quasi-diagrammatic) are equivalent *propositions*. "Adjoints are literally unique."
- **Semantics (App. A).**
  - Thm. A.16: model categories with T-shapes have pseudo-stable extension types.
  - Thm. A.17: these satisfy relative funext.
  - Prop. A.21: Segal type ↔ Segal space.
  - Prop. A.25: Rezk type ↔ Rezk space.
  - Remark A.27: covariant fibrations ↔ left fibrations, via Kazhdan–Varshavsky, de Brito and Rasekh.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | One 2-1-horn contractibility condition yields identities, associativity and 3-dimensional coherence in a Segal type | strong | proof: Props. 5.8, 5.9, 5.16, 5.21, Cor. 5.22 |
| C2 | Segal types have *all* higher coherences, analogous to van den Berg–Garner and Lumsdaine for identity types | conjecture | stated as conjectured, not proved (p. 4); only the n ≤ 3 horns are proved |
| C3 | Every function between Segal types is a functor, and every arrow in a function type is a natural transformation | strong | proof: Props. 6.1, 6.3, 6.6 |
| C4 | Dependent Yoneda lemma for covariant families over Segal types | strong | proof: Thm. 9.5 via Lemma 9.8 and Thm. 9.7 |
| C5 | λx. hom(a, x) is covariant iff A is Segal | strong | proof: Prop. 8.13, with the converse direction repaired in v5 (pp. 40–41) |
| C6 | Left adjoints to a functor into a Segal type, from a Rezk type, are unique (a proposition) | strong | proof: Thm. 11.23; stronger than the abstract's "between Rezk types" |
| C7 | The type theory with shapes is sound for Reedy bisimplicial sets (and model categories with T-shapes) | weak | sketch: App. A.2 omits Lumsdaine–Warren coherence and initiality, and says so (p. 66, Thm. A.18) |
| C8 | Internal Segal and Rezk types are exactly Segal and complete Segal spaces in that model | strong | proof given the model: Props. A.21 (Joyal's lemma, cited from Lurie HTT 2.3.2.1) and A.25 (Joyal–Tierney 4.11) |
| C9 | Covariant families model ∞-groupoid-valued (∞,1)-functors | moderate | Remark A.27 assembles it from cited results (KV14, dB16, Ras17); not proved here |
| C10 | Replacing the strict interval by Joyal's disks would give (∞,n)-categories | assertion | "presumably" (p. 6, §3.1 remarks) |
| C11 | The cubical type theory of Cohen–Coquand–Huber–Mörtberg is, approximately, another instance of type theory with shapes (plus Kan operations) | informal argument | Remark 3.2 |

### What a non-specialist can and cannot verify

"Non-specialist" here means someone fluent in ordinary mathematics or programming-language type theory, but not in HoTT, model categories or (∞,1)-categories.

**Can verify** (self-contained, by elementary reasoning):
- The shape-layer combinatorics. These are finite case analyses in the theory of a total order:
  - the definitions of Δⁿ, ∂Δⁿ and Λ²₁ as topes (§3.2);
  - the connection squares (Prop. 3.5, including spotting its typo);
  - the retract arguments (Props. 3.6 and 3.7);
  - the five-case tope check that closes Prop. 5.21 (pp. 30–31).
- That the *type-theoretic* proofs have the shape claimed. They almost all run the same move: sum over the free endpoint, observe that both total spaces are contractible (one a based path space, the other by the Segal or covariance hypothesis), and conclude that the fibrewise map is an equivalence. Examples are Props. 5.10, 5.12, 8.18 and Lemma 8.15. This is checkable once "contractible" and "fibrewise equivalence iff total equivalence" are taken on trust.
- The 1-categorical skeletons: the isomorphism arguments in §10.1, the universal-arrow argument in Thm. 11.23, and the Yoneda proof in Thm. 9.1, which is "just the usual proof" (p. 47).
- The erratum's logic in Prop. 8.13. The earlier converse appealed to a result that presupposed its conclusion.

**Cannot verify without specialist background or outside sources:**
- Whether the *rules* are coherent as a type theory: admissibility of substitution and cut, and the need to postulate (∗) (p. 10).
- The whole of App. A.2's soundness claim. The paper itself does not prove it (C7).
- Joyal's combinatorial lemma and the Joyal–Tierney Quillen equivalence on which Props. A.21 and A.25 rest.
- The model-category facts behind Lemma A.4. That cofibration is monomorphism and that the Reedy structure is cartesian are cited.
- Remark A.27's identification with left fibrations.
- The correspondence of the half-adjoint data (μ, ω, τ) with Riehl–Verity's parental subcomputads (§11.1).
- The details of the prism proof of Thm. 11.14. Its diagrams (Figs. 5–7) did not survive extraction, so I could not check them either.
- Whether the formalization that surfaced the Prop. 8.13 gap has checked the rest. The paper does not say what was formalized or in which system.

**Bottom line:** the internal category theory of §§5–10 is checkable by a careful reader who learns the HoTT book's chapters 2–4. The claim that this type theory *means* (∞,1)-category theory cannot be checked from this paper by a non-specialist. That claim rests on the appendix and its citations, and the paper's own semantics is sketched.

## Method

This is not an empirical paper. The method is to specify a three-layer type theory (§2), specialise the shape layer to a strict interval (§3), and prove extension-type algebra (§4: currying, choice, composites and unions of cofibrations, relative funext). On top of that it develops category theory internally, by contractibility arguments and path induction (§§5–11), and then sketches a categorical semantics (App. A).

## Concepts

- **Cube, tope, shape:**
  - a cube is a finite power of 2;
  - a tope is a coherent-logic formula in cube variables;
  - a shape {t : I | φ} is a cube with a tope, read as a polytope in the directed cube.
- **Extension type ⟨Π_{t:I|ψ} A(t) | ^φ_a⟩:** dependent functions on the shape ψ that are *judgmentally* equal to a on the sub-shape φ. They generalise cubical path types.
- **hom_A(x, y):** the extension type ⟨Δ¹ → A | ^{∂Δ¹}_{[x,y]}⟩, the directed arrows in A.
- **Segal type:** for all composable f and g, Σ_h hom²_A(f, g; h) is contractible.
- **Rezk type:** a Segal type for which idtoiso : (x = y) → (x ≅ y) is an equivalence ("local univalence").
- **Discrete type:** idtoarr : (x = y) → hom_A(x, y) is an equivalence. These are the synthetic groupoids.
- **Covariant family:** C : A → U such that, for every f : hom(x, y) and u : C(x), Σ_v hom_{C(f)}(u, v) is contractible. Equivalently, each arrow has a unique lift starting at u (Prop. 8.4).
- **Inner anodyne:** a shape inclusion whose extension types into any Segal type are contractible. This is a meta-theoretic notion (Def. 5.19).
- **Flagged (∞,1)-category:** the semantic reading of a *Segal* type, meaning an (∞,1)-category A with an ∞-groupoid mapping G → A. Rezk types are the case G = core A (p. 4).

## Connections

- **HoTT:** extends the HoTT book (Uni13), especially Chs. 2, 4 and 9. The adjunction work mirrors Ch. 4's equivalences, Rezk completeness mirrors the Ch. 9 / Ahrens–Kapulkin–Shulman univalent categories, and Thm. 11.23 is compared with the HoTT book's Lemma 9.3.2.
- **Semantics:** rests on Shulman 2015 (univalence for Reedy presheaves), Rezk 2001 (complete Segal spaces), Joyal–Tierney 2006, and Lurie HTT 2.3.2.1.
- **Semantic analogues:** gives new synthetic proofs of the Yoneda results of Riehl–Verity 2017, Kazhdan–Varshavsky 2014, de Brito 2016 and Rasekh 2017. Prop. 9.10 corresponds to Rasekh's Thm. 5.6.
- **Adjunctions:** match Riehl–Verity 2016 (homotopy coherent adjunctions, parental subcomputads).
- **Alternatives:**
  - two-level type theory (Voevodsky's HTS; Annenkov–Capriotti–Kraus 2017) is considered and set aside, in favour of keeping all types fibrant and moving cofibrations into a separate syntax (pp. 5–6). This pairs the paper with [LIT-040](../literature.d/LIT-040.md) (nLab, two-level type theory), as the seed says;
  - Licata–Harper's 2-dimensional directed type theory is cited as putting in the categorical structure by hand (p. 2).
- **Cubical type theory:** Remarks 1.1, 3.2.
- **Within nucleation:** no document other than its seeded skim (NOTE-069) and the 2026-09-25 curation entry cites [LIT-032](../literature.d/LIT-032.md).

## Bearing on the record

- **[LIT-032](../literature.d/LIT-032.md) status.** It should move from Deferred to Active on this reading. It is a foundational, peer-reviewed paper whose main internal results are proved, and whose one known proof gap (Prop. 8.13) has been repaired in the text.
- **Pair with [LIT-040](../literature.d/LIT-040.md).** The paper is the reason "type theory with shapes" is listed under See also on the 2LTT page. It explains precisely why it does *not* use 2LTT: it keeps all types fibrant and gives cofibrations their own syntax. A reader of [LIT-040](../literature.d/LIT-040.md) should be pointed here.
- **No THEORY in nucleation depends on it.** If one were written, for example "directed identity elimination is the Yoneda lemma", the load-bearing result is Thm. 9.5. The semantic claim should be cited as sketched (C7).
- **Anthology: none.** There is nothing here for ML practice. Nothing in it concerns learning, computation or models, and there is no path from it to an ANTH document. Any claimed link, such as category-theoretic deep learning, would have to come from other papers.

## Limitations

- **The semantics is a sketch.** Soundness relies on an unproved initiality theorem and on Lumsdaine–Warren coherence, which "has to be proven separately for each kind of type-theoretic structure" (p. 66). The authors say so plainly.
- **Coherence is proved only at low dimension.** Only 3-dimensional horns are proved inner anodyne. The general schema and an analogue of "types are weak ω-groupoids" for Segal types are conjectures (pp. 4, 31).
- **Relative funext is an axiom.** The authors do not know whether its weaker forms suffice (p. 22).
- **Proof-theoretic fixes.** The rule (∗) is postulated to patch admissibility (p. 10), and implementation questions are explicitly set aside.
- **Scope of the fibrations.** Only ∞-groupoid-valued (covariant, discrete-fibred) families are treated. Cocartesian families with categorical fibres are left for later work (footnote 11).
- **Univalence in directed form.** No directed univalence and no universe of covariant families are developed, although the authors expect them to be needed (§2.1, footnote 4).
- **Extraction limits (this reading, not the paper).** The rule figures and higher-simplex diagrams were not machine-readable. Rule-level details (Figs. 1–4) and the face labels in Figs. 5–7 are unverified by me.

## Open questions

- **An analogue of van den Berg–Garner and Lumsdaine for Segal types.** Do all higher coherences follow internally from the Segal condition? A meta-theorem to that effect would close it (conjectured on p. 4).
- **Relative funext.** Are the three formulations of relative function extensionality equivalent (p. 22)?
- **Other interval theories.** Does replacing the strict interval by Joyal's disks give a working synthetic (∞,n)- or (∞,∞)-category theory (pp. 6, 14)?
- **Directed univalence.** A universe of covariant families, and modalities for the discrete, codiscrete and cohesive structure (Remark 7.5), are left open.
- **Soundness.** Closing it requires an initiality theorem for type theory with shapes.
- **Formalization.** How much of the paper has been checked? The p. 40 remark implies some of it has, but the paper does not say what. A pointer to the formalization would settle it. The seed's Rzk claim is unverified here.

## Corrections to the seeded skim

- **The adjunction result is stronger than the seed (and the abstract) says.** The seed repeats the abstract's "for a functor between Rezk types to have an adjoint is a mere proposition". Theorem 11.23 needs only that A is Segal and B is Rezk, for u : B → A. Its (ii)–(v) also show that the whole adjunction is then unique, not merely that its existence is a proposition. §11.2 proves the weaker Segal-only statements: given the unit η, or given (η, ε, α), the rest is a proposition (Cors. 11.21, 11.22).
- **The semantics is sketched, not proved.** The seed says the appendix "gives semantics in the Reedy model structure on bisimplicial sets". §A.2 says outright: "We will not give a complete proof, but only sketch the main ideas". Soundness depends on two things the paper omits: the Lumsdaine–Warren coherence construction and an initiality theorem, which "is commonly neglected ... there is as yet no general theorem" (p. 66). What is proved is:
  - the correspondences Segal type ↔ Segal space (Prop. A.21, by Joyal's lemma) and Rezk type ↔ Rezk space (Prop. A.25, via the Joyal–Tierney Quillen equivalence);
  - that pseudo-stable extension types exist and satisfy relative funext in any "model category with T-shapes" (Thms. A.16–A.17).
- **Joyal's conjecture is proved in the appendix.** The seed does not mention this. The internal Segal condition (an equivalence X^{Δ²} → X^{Λ²₁} of bisimplicial sets) is equivalent to the classical Segal-space condition, as Joyal conjectured (§1, p. 4). This is Prop. A.21.
- **Where the v5 correction to Prop. 8.13 appears.** The seed says it "is noted on the arXiv page". The erratum is in the text itself, p. 40–41. The converse direction (covariant representable ⇒ Segal) had appealed to Prop. 5.10, which already assumes Segal. It now instead makes the base type a retract of a contractible type. The fix was "pointed out to us a few years ago by Bastiaan Cnossen and rediscovered more recently when formalizing these results". The p. 1 footnote says v5 "corrects typos", which undersells a repaired proof step.
- **Rzk is not named.** The seed asks a reading to check "the Rzk proof assistant, which implements this simplicial type theory". The paper never names Rzk or any proof assistant. The only traces are "leave that for automation in a proof assistant" (p. 31) and "when formalizing these results" (p. 40). Any Rzk claim needs its own source.
- **Univalence and universes are not needed.** The type theory assumes function extensionality, as relative funext (Axiom 4.6), in the third, contractibility form, "somewhat surprisingly". It assumes neither univalence nor HITs. The universe is used "only for notational convenience" (Remark 2.5).
- **There is a typo in the paper.** Prop. 3.5 lists "Λf(0, s) ≡ f(s)" and "Λf(t, 0) ≡ f(t)" in its second column, where Λf(1, s) ≡ f(s) and Λf(t, 1) ≡ f(t) are meant. The first column's Λf(0, s) ≡ f(0) and Λf(t, 0) ≡ f(0) contradict them as printed.
