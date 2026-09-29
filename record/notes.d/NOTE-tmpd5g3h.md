---
status: Read
paper: LIT-310
title: 'A topos foundation for theories of physics: IV. Categories of systems'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/0703066 v1 (7 Mar 2007, the
    only arXiv version), from the arXiv PDF, 38 pp. I read the abstract,
    §§1–5 (the category Sys, disjoint sums and composites, translations,
    topos realisations, classical physics, the rules of Def 3.2, the quantum
    disjoint sum and the quantum composite), the acknowledgements and all 11
    references. Nothing was skipped. I checked the classical constructions,
    Lemma 4.2, the disjoint-sum pull-back (4.18)–(4.24) and the composite
    construction (4.29)–(4.45) against the definitions of papers II–III.
    Papers I–III of the series were read in full alongside. `pdftotext` was
    not available, so I extracted the text with PyMuPDF. The published J.
    Math. Phys. text (paywalled) was not seen.). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Proposes axioms for a category Sys of physical systems,
  symmetric-monoidal under composite ⋄ and under disjoint sum ⊔, whose
  arrows are translations of local languages. Each arrow j : S₁ → S is
  realised by a left-exact functor τ(j) between the systems' topoi,
  together with arrows φ(j) : Σ_{S₁} → τ(j)Σ_S and β(j) : τ(j)R_S →
  R_{S₁}. Classical physics satisfies the scheme exactly. In quantum
  theory the disjoint sum H₁⊕H₂ satisfies it (the pulled-back arrow of
  Â₁⊕Â₂ is δ̆(A₁)), but the composite H₁⊗H₂ does not: the natural
  pull-back of δ̆(A₁) differs from δ̆(A₁⊗1̂) off the image of V(H₁), which
  the authors attribute to "operator entanglement".
---

# NOTE-tmpd5g3h: A topos foundation for theories of physics: IV. Categories of systems

## Contribution

The paper extends the single-system programme of papers I–III ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md)) to collections of systems. It proposes a category Sys whose arrows are "physically meaningful" translations of physical quantities, with local languages giving a functor L : Sys → Loc^op.

It proposes rules (Def 3.2) for realising Sys in a category M(Sys) of topoi with left-exact functors as arrows. The rules are:
- a pull-back of physical quantities along the triple (τ(j), φ(j), β(j));
- a pull-back of propositions, φ(j)⁻¹(τ(j)(K)).

It then tests the rules on classical physics, where they work, and on quantum theory, where they work for disjoint sums and fail for tensor-product composites.

## Key insight

In classical physics a composite's state space is a categorical product S₁ × S₂. Its projections pull a constituent's quantities back to the composite exactly, so "the energy of particle 1" means the same function in both descriptions.

In the quantum topos there is no such projection Σ_{H₁⊗H₂} → Σ_{H₁}. The context category V(H₁⊗H₂) contains many contexts that are not of the form V₁⊗V₂ ("operator entanglement"). The best available pull-back of δ̆(A₁) therefore agrees with δ̆(A₁⊗1̂) only on contexts coming from V(H₁). Elsewhere it approximates A₁ inside V_W, the largest H₁-part of the context. So the composite's topos "knows" more contexts than any translation from a constituent can reach.

## Assumptions

- **The collection of systems.** Sys is small. It is closed under sub-systems, composites and disjoint sums. All its systems share the ground types Σ and R and differ only in their function symbols (§2.1).
- **Disjoint sums and composites.** For disjoint sums, F_{S₁⊔S₂}(Σ,R) ≅ F_{S₁} × F_{S₂} (2.1, 2.12). For composites no such decomposition is postulated; only the translations A₁ ↦ A₁⋄1 exist.
- **Axioms.** ⊔ and ⋄ are associative and commutative up to isomorphism (2.9–2.10, 2.13–2.14). They satisfy distributivity (S₁⊔S₂)⋄S ≅ (S₁⋄S)⊔(S₂⋄S) (2.16), a trivial system 1 with S⋄1 ≅ S (2.17), and an optional empty system 0 (2.18–2.19). Coherence axioms are "very plausible" and not checked. Bifunctoriality holds only if arrows are restricted to sub-system and composite arrows (§2.2.4).
- **Every system has a trivial quantity.** Each language contains I with ∀s̃₁ ∀s̃₂ I(s̃₁) = I(s̃₂) (2.8).
- **Arrows between topoi.** The arrows of M(Sys) are left-exact functors, chosen so that monics, and hence propositions, can be pulled back (§3.1.2).
- **Quantum setting.** Separable Hilbert spaces. For disjoint sums, only block-diagonal operators Â₁⊕Â₂ are used (fn. 20). For composites, H₁⊗H₂ with the translation Â₁ ↦ Â₁⊗1̂.

## Key results

- **Classical physics (§2.4).**
  - *Construction.* Every arrow j gives a map σ(j) : Σ_{S₁} → Σ_S, the inclusion into a disjoint union or the projection from a product. Pulling back along it, σ(L(j))(f) = f ∘ σ(j) (2.33), makes the square (2.30) commute.
  - *Trivial and empty systems.* The trivial system goes to {∗} (2.26) and the empty system to ∅ (2.27).
  - *Strength.* This is exact and elementary.
- **Rules (Def 3.2).**
  - *Objects and quantities.* The state object, the quantity-value object, quantities as arrows and propositions as sub-objects are as in I–III.
  - *States.* Truth objects instead of microstates (Rule 3). The unit of M(Sys) is Sets (Rule 4, (3.14)).
  - *Arrows.* Each arrow gets a triple (τ(j), φ(j), β(j)). The pull-back is φ(L(j))(μ) = β(j) ∘ τ(j)(μ) ∘ φ(j) (3.5). The target condition, which "may, or may not" hold, is φ(L(j))(A_{φ,S}) = [L(j)(A)]_{φ,S₁} (3.18).
  - *Conjectures.* For a sub-system, φ(j) is monic (Rule 6a). It is also conjectured that R_{S₁} ≅ τ(j)(R_S) and that φ(j) is epic for epic j (Rule 6b).
- **Geometric morphisms from functors (Thm 4.1, cited from Mac Lane–Moerdijk).** A functor ϕ : C → D induces ϕ* : Sets^{D^op} → Sets^{C^op}, F ↦ F ∘ ϕ^op. This is left exact, with left adjoint ϕ_!.
- **Quantum disjoint sum (§4.2).**
  - *The functor.* m : V(H₁) → V(H₁⊕H₂), V ↦ V ⊕ ℂ1̂_{H₂}, which is order-preserving. μ* is the induced inverse image.
  - *Lemma 4.2.* δ(Â₁⊕Â₂)_{V₁⊕V₂} = δ(Â₁)_{V₁} ⊕ δ(Â₂)_{V₂}. The proof is correct: projectors in V₁⊕V₂ split, so inner daseinisation of each spectral projector splits. It is applied with V₂ = ℂ1̂_{H₂}, where δ(Â₂) = max sp(Â₂)·1̂ (4.21), even though ℂ1̂ is not an object of V(H₂). The formula is still right.
  - *Spectra.* Σ_{V⊕ℂ1̂} ≅ Σ^{H₁}_V ∪ {λ₀}, where λ₀ is the one extra character that is 1 on 0̂⊕1̂. φ(i) is the inclusion, and β(i) is the evident isomorphism μ*ℝ^⪰ ≅ ℝ^⪰_{H₁} (4.20).
  - *Result.* The pull-back of δ̆(⟨A₁,A₂⟩) is δ̆(A₁) (4.24), so (3.18) holds for i₁ and i₂. I checked this; it follows from Lemma 4.2 and the definitions.
- **Quantum composite (§4.3).**
  - *The functor.* n : V(H₁⊗H₂) → V(H₁)*, W ↦ V_W, the largest V with V⊗ℂ1̂ ⊆ W. This is well defined: V_W⊗1̂ = W ∩ (B(H₁)⊗1̂). V(H₁)* adjoins ℂ1̂_{H₁}, and Σ and ℝ^⪰ are extended to it (a single character; ℝ).
  - *The pull-back.* τ(p₁) = ν*, φ(p)_W(λ) = λ|_{V_W} (4.40) and β(p)(α)(W′) = α(V_{W′}) (4.39). The resulting arrow is, at each W, the Gel'fand transform of δ(Â₁)_{V_W} ⊗ 1̂ (4.44)–(4.45). It agrees with δ̆(A₁⋄1) at every W of the form V₁⊗ℂ1̂ (fn. 27).
  - *Where it fails.* "It is relatively easy to show" that δ(Â₁⊗1̂)_W ≠ δ(Â₁)_{V_W} ⊗ 1̂ in general (4.46). Hence φ(L(p))(δ̆(A₁)) ≠ δ̆(A₁⋄1) (4.47), and (3.18) fails. "There appears to be no operator B̂" whose arrow equals the pull-back.
  - *Status.* Neither (4.46) nor the non-existence claim is proved. Fn. 25 adds that it is open whether δ(Â₁⊗1̂)_W = δ(Â₁)_{V₁}⊗1̂ even for W = V₁⊗V₂ with V₂ non-trivial.
  - *Authors' summary.* The scheme holds for classical physics and "quantum physics 'almost' does" (§5).
- **Speculation (§5).**
  - *A "gros topos".* A single topos Sh(M(Sys)) for all systems of a theory-type, if M(Sys) is a site. It is posed, not attempted.
  - *Interpolating functors.* An "interpolating chain" of functors between a neo-realist topos and an instrumentalist one.
  - *Quantum gravity.* A claim that quantum gravity must be built in a topos U ≠ Sets.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Systems form a category Sys, symmetric-monoidal under ⋄ and under ⊔, with arrows given by language translations | assertion / axioms ("not cast in stone") | §2.2.4. Coherence is not checked; bifunctoriality holds only for restricted arrows |
| C2 | Classical physics satisfies the rules exactly, via pull-back along σ(j) | proof (elementary) | §2.4, (2.33), (3.9)–(3.10) |
| C3 | Propositions pull back along any triple whose functor preserves monics | proof (standard topos facts) | §3.1.2 |
| C4 | The unit of M(Sys) is Sets, because V(ℂ) has one object | argument inconsistent with the series' definition of V(H), which excludes ℂ1̂ | Rule 4, (4.9); see corrections |
| C5 | Quantum disjoint sums satisfy (3.18): the pull-back of δ̆(A₁⊕A₂) is δ̆(A₁) | proof (checked) | Lemma 4.2, (4.18)–(4.24) |
| C6 | For composites, the natural pull-back of δ̆(A₁) equals δ(Â₁)_{V_W}⊗1̂ at each W, agreeing with δ̆(A₁⋄1) exactly on contexts V₁⊗ℂ1̂ | proof (construction checked) | (4.29)–(4.45), fn. 27 |
| C7 | This pull-back differs from δ̆(A₁⋄1) in general, and no operator B̂ has it as δ̆(B) | assertion ("relatively easy to show"; "there appears to be no") | (4.46)–(4.47), §4.3 |
| C8 | The failure reflects "operator entanglement": V(H₁⊗H₂) has contexts not of the form V₁⊗V₂ | informal argument (interpretation) | §4.3; the premise about contexts is true, and the causal link is a gloss |
| C9 | The translation is "as good as possible" | assertion | §4.3, "Comments on these results" |
| C10 | Quantum gravity should be formulated in a topos other than Sets | assertion (programmatic) | §5 |

## Method

Categorical axiomatics (monoidal categories, translations of local languages after Bell), geometric morphisms induced by functors between base categories (Mac Lane–Moerdijk VII), and the daseinisation machinery of papers II–III.

## Concepts

- **Sys.** The category of systems. An arrow j : S₁ → S is a translation L(j) of S's quantities into S₁'s.
- **Disjoint sum ⊔ and composite ⋄.** The two monoidal structures on Sys. The unit of ⋄ is the trivial system 1; the unit of ⊔ is the empty system 0.
- **Topos realisation.** A triple (ρ_{φ,S}, L(S), τ_φ(S)) per system, plus a triple (τ(j), φ(j), β(j)) per arrow.
- **Translation representation φ(L(j)).** The pull-back of arrows Σ_S → R_S to arrows Σ_{S₁} → R_{S₁}.
- **Operator entanglement.** The authors' name for the fact that V(H₁⊗H₂) is richer than contexts of the form V₁⊗V₂.
- **Augmented context category V(H)*.** V(H) with ℂ1̂ readmitted as a bottom element.
- **Gros topos.** A single topos of sheaves over a site of topoi, housing every system of a theory-type.

## Connections

- **Papers I–III ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md)).** This paper uses I's languages and translations and III's δ̆ and ℝ^⪰. It repeats II's truth objects as Rule 3.
- **Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md)).** Its sequels are cited ([7]–[11]) for the physical meaning of contexts. Nothing on composites is taken from them.
- **Abramsky–Brandenburger ([LIT-016](../literature.d/LIT-016.md)), [THEORY-012](../theory.d/THEORY-012.md), [LIT-277](../literature.d/LIT-277.md), [LIT-278](../literature.d/LIT-278.md).** No relation.
  - *Composites without Bell.* The paper treats composite quantum systems but never Bell non-locality, product measurement covers, or no-signalling. Those are exactly what [LIT-016](../literature.d/LIT-016.md) adds for composites (measurement covers, locality as factorisability).
  - *Where the failure sits.* The composite failure here concerns translating a constituent's quantity arrows into the composite topos. It does not concern contextuality or non-local correlations. The "entanglement" in the title of §4.3 is about the context poset of H₁⊗H₂, not about any state.
- **[THEORY-017](../theory.d/THEORY-017.md) (a tensor factorisation is extra data).** A related point. Here the factorisation H₁⊗H₂ is given, and the constituent quantities translate faithfully only on the sub-poset of contexts V₁⊗ℂ1̂ that the factorisation picks out. Everything else in V(H₁⊗H₂) is invisible to the constituent. This is the topos-side face of [THEORY-017](../theory.d/THEORY-017.md)'s claim that parts are supplied from outside the space.
- **Mereology entries.** None in the record engages physical composition in these terms. I checked no specific entry for a direct link, and none is claimed.

## Bearing on the record

- **The map's role (§0, row 8: instantiate "their presheaf … as the Topos of Bricks").**
  - This is the one paper in the series about building a whole from parts. Its result is a caution: the programme's quantum topoi do not compose along ⊗ in the way its rules require (C6–C7). Only disjoint sums compose cleanly (C5).
  - If the "Topos of Bricks" is meant to assemble a concept system from brick-wise topoi, or to translate a sub-model's concept operators into a larger model, this paper predicts a mismatch. The larger model has contexts that mix the parts (not of the form V₁⊗V₂), and on those contexts translated quantities are not the larger model's own quantities.
  - If instead the Topos of Bricks is a single presheaf topos over one context category, this paper is not needed. The owner's documents should say which is meant before citing it.
- **The map's §2 item 5 (`𝒜^∞`, "stable across every adequate model's concept algebra").** The paper's own open question, a "gros topos" housing all systems of a theory-type (§5), has the same shape as a cross-model object. It is posed, not solved. Citing this paper for a cross-model topos would overstate it.
- **The rest of §2.1.** Nothing here bears on ultrafilters, Kochen–Specker, or topes.
- **ML practice.** It carries nothing for ML practice.
- **For filing.** Tags as proposed. `quantum-foundations` first. `mereology` is justified by the paper's subject (composition and individuation of systems). `mathematics` and `logic` cover the categorical and linguistic machinery. `philosophy-of-science` covers the realism and instrumentalism discussion and idealised systems. `anthology-candidate` is not proposed.

## Limitations

- **The rules are provisional.** The rules and axioms are self-described as "partly 'experimental'", and several (Rule 6, (3.20), the epic conjecture) are conjectures.
- **The main negative result is not proved.** Neither (4.46) nor "no B̂" is shown, and fn. 25 leaves open an easier case.
- **The trivial-system derivation contradicts the series' own convention** (C4).
- **The composite realisation does not quite fit the rules.** It needs an augmented category V(H₁)*, and several notational slips obscure the direction of the arrows (see corrections).
- **Only two arrow types are treated for quantum theory** (disjoint-sum inclusions and composite projections). Genuine sub-systems (Rule 6a) are not realised for any quantum example.
- **Physically thin.** There is no dynamics and no states on composites (how T^ψ for an entangled ψ relates to the constituents' truth objects is not discussed). Nothing is said about locality or about how partial trace appears.

## Open questions

- Prove (4.46), and decide whether any B̂ realises the pulled-back arrow, i.e. whether the failure is a theorem.
- Is there a different context category, or a different choice of functor V(H₁⊗H₂) → V(H₁)* or of β, under which tensor-product composites satisfy (3.18)?
- How do truth objects of entangled states restrict to the constituents? What is the topos analogue of the partial trace?
- Can M(Sys) be made a site so that a "gros topos" exists for quantum systems (§5)?

## Corrections to the seeded skim

- Seeded from metadata. The seed's summary is accurate as far as it goes. The text adds the finding: the scheme works for disjoint sums, and composites fail the paper's own commutativity condition (3.18); the seed does not say so.
- The trivial system is internally inconsistent. Rule 4 postulates that the trivial system's topos is Sets. It derives this (4.9) from "exactly one abelian subalgebra of B(ℂ) … namely ℂ itself". But paper II excludes the trivial algebra ℂ1̂ from V(H) by definition ([LIT-335](../literature.d/LIT-335.md), §2.1.1), and this paper says so itself (§4.3: "The trivial algebra ℂ1̂_{H₁} is not an object in the category V(H₁)").
  - *Consequence.* Under the series' convention V(ℂ) is empty, and the presheaf topos over the empty category is the degenerate one-object topos, not Sets. Rule 4 holds only if ℂ1̂ is readmitted, as the paper does ad hoc elsewhere with the augmented category V(H₁)*.
  - This is my observation; the paper does not note it.
- Notational slips that could mislead a reader checking the construction:
  - *Wrong direction.* (4.19) calls μ* "the functor … τ_φ(j) : τ_φ(S₁) → τ_φ(S)", which is the wrong direction; μ* goes from the sum's topos to S₁'s.
  - *Composition order.* (4.23) writes the pull-back as φ(i) ∘ μ*(δ̆) ∘ β_φ(i), the reverse of the order in (3.5) and (3.17).
  - *Undefined symbol.* The geometric morphism for the composite is said to be "induced by π" when the functor defined is n (4.31).
  - *Target mismatch.* The functor used for the composite has target V(H₁)*, not V(H₁). So τ_φ(p₁) is not literally a functor out of τ_φ(S₁) = Sets^{V(H₁)^op} as Rule 5(c) requires.
- Tag proposal: add `mereology`, whose blurb is "composition, individuation of systems". The paper is about sub-systems, composites and what counts as a system (§2.1–§2.2.3), and that is its main subject after quantum theory. Add `philosophy-of-science` for §2.1 and §5, on idealised systems and neo-realist versus instrumentalist interpretations. Drop `contextuality`: the paper does not treat contextuality as such. The context category appears only as V(H₁⊗H₂) being richer than V(H₁)×V(H₂), which is not something a browser of contextuality would come for. Keep `logic`, for translations of local languages.
- Identifiers check against the arXiv listing: journal-ref J. Math. Phys. 49:053518 (2008); DOI 10.1063/1.2883826; "38 pages, no figures". arXiv v1 is 7 Mar 2007. `published: 2008-05-01` is the journal issue (flagged only).
