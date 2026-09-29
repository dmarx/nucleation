---
status: Read
paper: LIT-325
title: 'A topos perspective on the Kochen–Specker theorem: I. Quantum states as generalized valuations'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/9803055 v4 (13 Oct 1998; v1
    was 20 Mar 1998), from the arXiv PDF, 59 pp. The title page is dated
    "May 1998", with a footnote "Small clarifications added concerning
    operators with continuous spectra; September 1998". I read the abstract,
    §1 (§§1.1–1.4), §2 (categories W and O, the spectral presheaf, the dual
    presheaves), §3 (partial → generalized valuations, Theorem 3.1,
    algebraic properties), §4 (definition of generalized valuation, Theorems
    4.1–4.4, valuations from vectors, density matrices and projectors, the
    spin-½ and spin-1 examples), §5 (the category W of Boolean subalgebras,
    coarse-graining axioms, Theorem 5.1), §6 (conclusion), Appendix A
    (presheaves, sieves, Ω, global and local sections) and all 22
    references. Nothing was skipped. The text was extracted with PyMuPDF;
    the matrices of eqs. (4.33)–(4.37) and the commutative diagrams in the
    Appendix were reconstructed from the surrounding text. Every proof given
    was followed. The paper itself leaves some verifications as exercises
    (listed under Limitations). I did not read the IJTP version of record.).
    The first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Isham & Butterfield show that, for bounded self-adjoint operators with
  discrete spectrum, a global section of the spectral presheaf Σ(Â) = σ(Â)
  on the category O_d, whose arrows are functional relations B̂ = f(Â), is
  literally a valuation obeying the value rule and FUNC. A global section
  of the dual presheaf D(W) = Hom(W, {0,1}) on the poset W of Boolean
  subalgebras of projectors is literally a Kochen–Specker 0/1 assignment.
  The Kochen–Specker theorem (cited, not reproved) is therefore equivalent
  to "no global sections" when dim H > 2 (§§2.2–2.3). In place of the
  missing global valuations, they construct contextual truth values in the
  Heyting algebra of sieves: ν^ρ(A ∈ Δ) = {f: B̂ → Â | tr(ρ Ê[B ∈ f(Δ)]) =
  1}. For every density matrix these satisfy functional composition, null,
  monotonicity, exclusivity and unit conditions (§4.4, §5.3, Theorem 5.1).
---

# NOTE-tmp1cgp9: A topos perspective on the Kochen–Specker theorem: I. Quantum states as generalized valuations

## Contribution

Before this paper, the Kochen–Specker (KS) theorem was a statement about the impossibility of certain real- or 0/1-valued functions. Isham and Butterfield observe that the conditions on those functions, the value rule plus FUNC V(f(Â)) = f(V(Â)), are exactly the matching conditions of a global section of a presheaf over a category of "contexts". KS becomes the statement that certain presheaves have no global sections (§2).

They then use the presheaf topos to do what KS forbids classically: assign every proposition "A ∈ Δ" a truth value.

- **The truth values are contextual.** Each is a sieve on the operator Â, so it lives in the Heyting algebra Ω(Â) of sieves at that stage.
- **They are multi-valued.** Ω(Â) is a distributive but intuitionistic logic, larger than {0,1}.
- **Every quantum state yields one.** Every pure or mixed state gives such a "generalized valuation" (§§3–5).

## Key insight

A partial truth value for "A ∈ Δ" is the set of coarse-grainings f(Â) for which the weaker proposition "f(A) ∈ f(Δ)" is certainly true. That set is closed under further coarse-graining, and that closure is exactly the definition of a sieve.

So the natural home for quantum truth values is the subobject classifier of the presheaf topos over the category of contexts. Kochen–Specker says only that no section of the spectral presheaf picks out a *single* value everywhere. It says nothing against sections of Ω, which always exist.

## Assumptions

- **Valuation (§1.1).** A valuation is a real function V on bounded self-adjoint operators satisfying:
  - the value rule, V(Â) ∈ σ(Â);
  - FUNC, V(B̂) = h(V(Â)) whenever B̂ = h(Â).

  Global valuations are considered only on operators with purely discrete spectrum (§1.1). The continuous case is handled through propositions "A ∈ Δ" and spectral projectors.
- **Categories.**
  - *O and O_d (§2.1).* O is all bounded self-adjoint operators, and O_d those with discrete spectrum. There is an arrow f_O: B̂ → Â iff B̂ = f(Â) for some Borel f, unique up to equivalence on σ(Â). O is a preorder, not a poset (eq. 2.6).
  - *O\* (§3.3.5).* O\* is O minus the multiples of 1̂. It is introduced to remove "minimally true" values and make negation non-trivial (§4.4).
  - *W (§2.1).* W is the poset of Boolean subalgebras of the projection lattice P(H), under inclusion. W\* drops the trivial algebra {0,1}.
- **Presheaves.** A presheaf is a contravariant functor to Set. A global section is a family γ_A ∈ X(A) with X(f)(γ_A) = γ_B for all arrows (eq. A.22). No sheaf (gluing) condition and no Grothendieck topology is used anywhere. Everything is in the presheaf topos Set^{C^op}.
- **KS is taken as given.** No global valuation exists when dim H > 2, citing Kochen & Specker [1] and Bell [3]. The paper does not reprove it.
- **Generalized valuation (Defs. 4.1–4.2).** Sieve-valued maps satisfying:
  - (i) functional composition, ν(h(A) ∈ h(Δ)) = h*(ν(A ∈ Δ));
  - (ii) null, ν(A ∈ ∅) = 0;
  - (iii) monotonicity;
  - (iv) exclusivity, i.e. if Δ₁ ∩ Δ₂ = ∅ and ν(A ∈ Δ₁) = true_A, then ν(A ∈ Δ₂) < true_A;
  - optionally (v) the unit condition.
- **Non-Borel images (Theorem 4.1, eq. 4.2).** If f(Δ) is not Borel, Ê[f(A) ∈ f(Δ)] is *defined* as the infimum of the projectors in W_{f(A)} above Ê[A ∈ Δ].

## Key results

- **KS as no global section (§2.2).** A global section of the spectral presheaf Σ: O_d^op → Set is a choice γ_A ∈ σ(Â) with f(γ_A) = γ_{f(A)}, "precisely the condition FUNC". Hence "for operators with a discrete spectrum, the Kochen–Specker theorem is equivalent to the statement that, if dim H > 2, there are no global sections of the spectral presheaf". The proof is the observation itself. Functoriality of Σ is checked in eqs. 2.7–2.8.
- **Dual presheaf on W (§2.3, Def. 2.3).** D(W) = Hom(W, {0,1}), with restriction as the arrow map. A global section assigns each projector a 0/1 value with V(α ∨ β) = V(α) + V(β) when α ∧ β = 0, which is the KS assignment used in finite counterexamples. So "the dual presheaf D: W^op → Set has no global sections" when dim H > 2.
  - *Stone duality (my gloss).* Hom(W, {0,1}) is the Stone space of W, i.e. its ultrafilters. The paper does not use the words "ultrafilter" or "Stone".
- **The same on all of O (§2.3.2).** The composite D∘W on O, with a natural transformation T: Σ → D∘W on O_d (eqs. 2.11–2.12). The authors call this "perhaps the most physically transparent statement of the Kochen–Specker theorem in the language of presheaves".
- **Obstruction theory, anticipated (§2.2, §6).** The authors draw an analogy between KS and the non-existence of cross-sections of a non-trivial principal bundle (the Gribov effect). They ask whether the non-existence of global valuations "can be related to the non-vanishing of some topos-based cohomology structure". They propose finding "a new proof based on some theory of obstructions" as an open problem.
- **Partial valuations → generalized valuations (§3).**
  - *Partial valuation (Def. 3.1).* A partial valuation is a local section of Σ. Example: V^{M,m} on ↓M̂ (Def. 3.2).
  - *Generalized valuation (Defs. 3.3–3.4).* ν^V(A ∈ Δ) = {f: B̂ → Â | B̂ ∈ dom V, V(B̂) ∈ f(Δ)} is a sieve.
  - *Theorem 3.1.* ν^V(C ∈ h(Δ)) = h*(ν^V(A ∈ Δ)), with full proof.
  - *Algebra (§3.4).* ν^V satisfies null, monotonicity and exclusivity. It satisfies *strong* disjunction (eq. 3.22) but only weak conjunction (eq. 3.25), and it can fail the unit condition: ν^V(A ∈ σ(Â)) = dom V ∩ ↓Â (eq. 3.31), so "A only 'partially exists'".
- **Topos reading (§4.2).**
  - *Theorem 4.2.* Every generalized valuation is a natural transformation N^ν: G → Ω, with G the coarse-graining presheaf (Def. 4.3, "essentially the same thing as" the Borel power object BΣ). Equivalently, it is a subobject of G, and a global element of Ω^G.
  - *Why this escapes KS.* A generalized valuation *is* a global section, but of Ω^G, not of the dual presheaf to which KS applies (§4.2.5).
  - *Theorem 4.3.* A generalized valuation induces a natural transformation V^ν: Σ → Ω, and hence a partial section of Σ. Partial → generalized → partial is the identity; generalized → partial → generalized need not be (eqs. 4.27–4.28, §4.5).
- **Generalized valuations from states (§§4.3–4.4).**
  - *Pure states.* ν^ψ(A ∈ Δ) = {f: B̂ → Â | Ê[B ∈ f(Δ)]ψ = ψ} (Def. 4.4).
  - *Mixed states (Def. 4.5).* ν^ρ(A ∈ Δ) = {f | tr(ρ Ê[B ∈ f(Δ)]) = 1}. It is proved to be a sieve and to satisfy functional composition, null, monotonicity, exclusivity and the unit condition (eqs. 4.43–4.55).
  - *Failures.* Both strong disjunction and strong conjunction fail, as the spin-1 example shows (eqs. 4.33–4.39). The failure of disjunction is "a fundamental consequence of the superposition principle".
  - *Examples.*

    | system | state | proposition | value |
    |---|---|---|---|
    | spin-½ | eigenstate of Sx | Sz = ±½ | only minimally true in O, empty in O\* |
    | spin-½ | same | Sz ∈ σ(Sz) | true (unit condition) |
    | spin-1 | ψ = (0,1,0) | Sx = ±1 | the non-trivial sieve {t1̂ + rSx²} |
    | spin-1 | same | Sx ∈ {−1, 1} | true_Sx (eq. 4.38) |

  - *Negation (eq. 4.56).* Negation is trivial in O, because 1̂ is initial (footnote 14). This motivates O\*.
- **Threshold family (eq. 4.57).** ν^{r,ρ} is defined with tr(ρ Ê) ≥ r. It satisfies everything except exclusivity, and exclusivity too when ½ ≤ r ≤ 1. This is stated, and not proved in detail.
- **Theorem 4.4.** For a finite-rank projector P̂ of rank n, ν^P = ν^{ρ_P} with ρ_P = P̂/n, so projector valuations add nothing new in finite dimension. There is a full proof.
- **Boolean-subalgebra version (§5).**
  - *Local valuations and the valuation presheaf.* Local valuations Val(W, Ω(W)) (Def. 5.1) form the valuation presheaf 𝒱 (Def. 5.2). Its global sections are *not* equivalent to the O-based definition (§5.1), and their existence is left open.
  - *Coarse-graining.* Axioms (Def. 5.3): coarse-graining, monotonicity, retraction and composition. The canonical coarse-graining is φ_{W₁W₂}(α) = inf{β ∈ W₂ | α ≤ β} (Def. 5.4); that it satisfies the axioms is "left as a straightforward exercise".
  - *Theorem 5.1.* For any coarse-graining presheaf Θ and any density matrix ρ, ν^ρ_W(α) = {W′ ⊆ W | tr(ρ θ_{WW′}(α)) = 1} is a generalized valuation on W. There is a full proof.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For discrete-spectrum operators, a global section of the spectral presheaf Σ on O_d is exactly a FUNC-respecting valuation, so KS ⇔ Σ has no global sections (dim H > 2) | strong (definitional equivalence plus cited KS) | §2.2; functoriality proved in eqs. 2.7–2.8; KS cited [1] |
| C2 | Global sections of the dual presheaf D on W are exactly KS 0/1 assignments, so KS ⇔ D has no global sections | strong (definitional plus cited KS) | §2.3.1 |
| C3 | Every partial valuation yields a sieve-valued generalized valuation satisfying functional composition, null, monotonicity, exclusivity and strong disjunction, but not necessarily the unit condition | strong (proof) | Defs. 3.3–3.4, Thm 3.1, §3.4 |
| C4 | Every density matrix ρ yields a generalized valuation ν^ρ on O satisfying all of (i)–(v), with strong disjunction and strong conjunction failing | strong (proof) | §4.4, eqs. 4.42–4.55; spin-1 counterexample eqs. 4.33–4.39 |
| C5 | Generalized valuations are subobjects of the coarse-graining presheaf G, equivalently arrows G → Ω, equivalently global elements of Ω^G | strong (proof plus standard topos facts) | Thm 4.2, §4.2.4–5 |
| C6 | Generalized valuations and partial valuations are related by maps whose composite is the identity on partial valuations but not on generalized ones | strong (proof or example) | Thm 4.3, §4.5 |
| C7 | For any coarse-graining presheaf on W, each ρ yields a generalized valuation on W | strong (proof), except the canonical coarse-graining's axioms | Thm 5.1; Def. 5.4 left as an exercise |
| C8 | ν^{r,ρ} satisfies the conditions, with exclusivity iff r ≥ ½ | weak (asserted) | eq. 4.57, "straightforward to show" |
| C9 | ν^P for projectors satisfies the conditions | weak (asserted) | §4.6, "for reasons of space, we shall not go into the details"; the finite-rank case reduces to C4 by Thm 4.4 |
| C10 | The sieve logics give a "neo-realist" semantics that keeps distributivity, unlike the non-distributive projection lattice | informal argument | §1.2, §6. The philosophical case is deferred to Part II |
| C11 | Generalized valuations from states do not yield quantum probabilities by any measure on sieves | moderate (example) | spin-½ example after eq. 4.32 |

## Method

Category and topos theory applied to the operator algebra, in five steps.

1. **Contexts.** Build a category of contexts, either operators ordered by functional dependence or Boolean subalgebras ordered by inclusion.
2. **Values as a presheaf.** Put the "values" on it as a presheaf: spectra, or duals of Boolean algebras.
3. **KS.** Read KS as the absence of global elements.
4. **Truth values.** Replace 0/1 truth values with the subobject classifier Ω, whose sieves form a Heyting algebra.
5. **Valuations.** Axiomatise "generalized valuations" as maps into Ω satisfying analogues of FUNC and the value-rule consequences. Construct them from partial valuations and from states, and prove the axioms.

The Appendix gives a self-contained account of presheaves, sieves, pull-back, the Heyting operations (eqs. A.15–A.18), subobject classification (eqs. A.20–A.21), and global and local sections (§A.2.3–4).

## Concepts

- **Stage of truth / context** — an object of the base category, Â in O or W in W. The truth value of a proposition depends on it.
- **Spectral presheaf Σ** — on O_d, Σ(Â) = σ(Â), with Σ(f)(λ) = f(λ). (The later literature uses the name for the Gelfand-spectrum presheaf over commutative subalgebras. That is not this paper's object.)
- **Dual presheaf D** — on W, D(W) = Hom(W, {0,1}), with restriction maps.
- **Coarse-graining** — "f(A) ∈ f(Δ)" is a coarse-graining of "A ∈ Δ", and Ê[A ∈ Δ] ≤ Ê[f(A) ∈ f(Δ)] (eq. 1.8).
- **Sieve** — a set of arrows into Â closed under precomposition. true_A = ↓Â is the principal sieve, and false_A = ∅.
- **Totally true / totally false / minimally true** — the value ↓Â, the value ∅, and the value "only multiples of 1̂" respectively (§3.3.4–5).
- **Generalized valuation** — Defs. 4.1, 4.2 and 5.5.
- **Partial valuation** — a local section of Σ (Def. 3.1). This is the modal-interpretation notion.
- **FUNC** — the functional composition principle, V(h(Â)) = h(V(Â)).

## Connections

- **[LIT-016](../literature.d/LIT-016.md) (Abramsky & Brandenburger 2011) and [THEORY-012](../theory.d/THEORY-012.md).**
  - *What [NOTE-016](NOTE-016.md) credits.* [NOTE-016](NOTE-016.md) records that [LIT-016](../literature.d/LIT-016.md) credits Isham–Butterfield "for the insight that Kochen–Specker is non-existence of global sections of a presheaf" and separates its own approach from the topos one. The reading confirms both.
  - *Where the two agree.* IB's dual presheaf D on W is the state-independent, possibilistic special case of [LIT-016](../literature.d/LIT-016.md)'s picture. Take the contexts to be all Boolean subalgebras, and the sections over a context to be all 0/1 homomorphisms. Then a global section of D is a global section of the event presheaf with every quantum-possible outcome allowed, and "no global section" is [LIT-016](../literature.d/LIT-016.md)'s *strong contextuality* for the KS scenario.
  - *Where they differ.* Four ways:
    - IB have no distributions and no no-signalling, so [THEORY-012](../theory.d/THEORY-012.md)'s probabilistic criterion and the signed-section theorem (Thm 5.9) have no counterpart here.
    - IB's base is infinite (all operators or all Boolean subalgebras). [LIT-016](../literature.d/LIT-016.md)'s scenarios are finite measurement covers.
    - IB's contexts are ordered by coarse-graining (a category with many non-maximal objects). [LIT-016](../literature.d/LIT-016.md)'s are a cover with restriction to intersections.
    - IB never use a sheaf or gluing condition. Their "global section" is a limit over the whole base category, not the gluing of a compatible family over a cover. In [LIT-016](../literature.d/LIT-016.md) the event functor ℰ is a sheaf and the question is whether a *compatible family* extends.
  - *Precise statement.* IB 1998 owns "KS ⇔ no global section of the spectral presheaf Σ on O_d, equivalently of the dual (Stone) presheaf D on W". It does not own the empirical-model criterion of [THEORY-012](../theory.d/THEORY-012.md), which is [LIT-016](../literature.d/LIT-016.md)'s.
- **[LIT-277](../literature.d/LIT-277.md) (cohomology of contextuality).** §2.2 and §6 explicitly ask for a cohomological obstruction theory for KS, by analogy with obstruction classes for sections of non-trivial bundles. [LIT-277](../literature.d/LIT-277.md)'s Čech obstruction is a realisation of that programme, in [LIT-016](../literature.d/LIT-016.md)'s setting rather than the topos one. [THEORY-012](../theory.d/THEORY-012.md) already records that it is sufficient, not necessary. IB's remark is the earliest statement of that wish in the record.
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md); pending readings).** These are the mature form. The base becomes commutative von Neumann subalgebras, Σ becomes the Gelfand-spectrum presheaf, and propositions become clopen subobjects of Σ via daseinisation. In this paper those are respectively footnote 6, Σ on O_d, and the coarse-graining map φ of Def. 5.4 (the inf of projectors above α, i.e. outer daseinisation in later terms). The 1998 paper already contains the canonical coarse-graining that Döring–Isham call daseinisation, in Def. 5.4 and Theorem 4.1. It does not use that name, and I infer the identification from the formula.
- **[NOTE-249](NOTE-249.md) ([LIT-276](../literature.d/LIT-276.md)).** That reading found the paper cites Isham–Butterfield 1998 only for "an example is the Kochen–Specker obstruction", and makes false claims about Boolean logic. This reading confirms the relevant fact. Isham–Butterfield's truth-value logic is a Heyting algebra fixed by the base category ("the Heyting algebra of the sieves at any particular stage of truth … is precisely fixed by the structure of the base category", §6). It does not turn Boolean when a presheaf has a global section. That supports [NOTE-249](NOTE-249.md)'s correction.
- **Aerts–Gabora ([LIT-340](../literature.d/LIT-340.md), [LIT-312](../literature.d/LIT-312.md)).** They share a word and nothing else. Their "contextuality" is state change under context, while IB's is the dependence of a truth value on the stage of the presheaf.

## Bearing on the record

- **[THEORY-012](../theory.d/THEORY-012.md).** Its "What this does not say" and [LIT-016](../literature.d/LIT-016.md)'s summary attribute "KS as non-existence of global sections" through [LIT-016](../literature.d/LIT-016.md). This reading confirms the attribution and fixes its scope.
  - *The precise form.* Isham & Butterfield (1998, §§2.2–2.3) show that a global section of the spectral presheaf Σ(Â) = σ(Â), over discrete-spectrum operators ordered by functional dependence, is a FUNC valuation. They also show that a global section of the dual presheaf Hom(W, {0,1}) over Boolean subalgebras is a KS 0/1 assignment. KS, cited, is therefore equivalent to the absence of global sections when dim H > 2.
  - *Not a new proof.* The equivalence is definitional. The paper proves no new KS-type result.
  - *Not the commutative-subalgebra version.* The spectral presheaf over commutative (von Neumann) subalgebras, "the spectral presheaf" of the later literature, is Part III (quant-ph/9911020) and Döring–Isham, not this paper.
  - *Suggestion.* If [THEORY-012](../theory.d/THEORY-012.md) or any record document writes "KS as no global section of the spectral presheaf (Isham–Butterfield 1998)", add "over self-adjoint operators ordered by functional dependence (Σ(Â) = σ(Â)), equivalently the dual presheaf on Boolean subalgebras".
- **The map's role (§0, row 8: "Your §2.1 (no global ultrafilter → presheaf over contexts → Kochen–Specker) *is* their spectral-presheaf program").** The characterisation holds, and holds more literally than the map may know.
  - *Ultrafilters.* D(W) = Hom(W, {0,1}) is, by Stone duality, the set of ultrafilters of the Boolean context W. D is therefore exactly "the presheaf of ultrafilters over Boolean contexts", and KS is exactly "no global ultrafilter". The owner's §2.1 construction is IB's Def. 2.3 and §2.3.1, with Stone duality made explicit.
  - *The Heyting truth values.* Sieve-valued truth over contexts is §§3–5 here.
  - *What the map should not attribute to this paper.* Three things:
    - The commutative-subalgebra / Gelfand-spectrum version (Part III, Döring–Isham).
    - Any probabilistic or empirical criterion ([LIT-016](../literature.d/LIT-016.md)).
    - Any cohomological obstruction ([LIT-277](../literature.d/LIT-277.md)). IB only pose the problem.
  - *"Topes".* The map's gloss "Xiong's regions are topes" is the owner's. IB have no geometry of hyperplane arrangements.
- **[THEORY-013](../theory.d/THEORY-013.md).** No bearing. There are no behavioural data and no marginals.
- **ML practice.** It carries nothing, and it does not belong in the Anthology. ([NOTE-016](NOTE-016.md) notes the only topos/ML link in the Anthology, Belfiore–Bennequin [ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md), and that it does not build on this line.)

## Limitations

- **The KS equivalence is a reformulation.** It rests entirely on the cited KS theorem, and the paper proves nothing new about which sets of operators obstruct valuations.
- **Continuous spectra.** Σ is defined only on O_d. The continuous-spectrum spectral presheaf is postponed, "a more sophisticated approach that involves the spectral theorem for commutative von Neumann algebras" (§2.2).
- **Several verifications are left to the reader.**
  - that the canonical coarse-graining satisfies the axioms (Def. 5.4);
  - that ν^P satisfies the conditions (§4.6);
  - the threshold family ν^{r,ρ} (eq. 4.57);
  - that the diagram-chase in §5.3.5 commutes.
- **Typographical slips in the extracted v4 text.** Eq. (4.4) switches between K and J mid-formula; the proof of Theorem 4.1 ends "⊆ J" for "⊆ K"; and reference [16] has the wrong arXiv number.
- **Choice of category.** O and O\* give different negation behaviour. In O, negation is trivial (1̂ is initial, footnote 14), and the authors leave open which to use.
- **No probabilities.** Generalized valuations from states discard quantum probabilities: both Sz outcomes are null for an Sx eigenstate. The authors say these cannot underwrite a stochastic hidden-variable theory (after eq. 4.32). The ½ ≤ r ≤ 1 family is offered only as a hint toward a "topos perspective on the probabilistic statements".
- **Global sections of the valuation presheaf 𝒱 on W** (Def. 5.2) are not shown to exist.

## Open questions

The paper poses its own.

- **A topos Gleason theorem.** Do extra conditions make every generalized valuation satisfying the unit condition of the form ν^ρ (§6)?
- **The logic of generalized valuations.** What is the logical structure of the space of all generalized valuations, as subobjects of G?
- **Other coarse-grainings.** Are there coarse-graining presheaves on W other than the canonical one?
- **Entanglement.** How is entanglement reflected in ν^ψ for ψ ∈ H₁ ⊗ H₂?
- **Obstruction theory.** Is there an obstruction-theoretic, cohomological proof of KS? For the finite, [LIT-016](../literature.d/LIT-016.md) setting, [LIT-277](../literature.d/LIT-277.md) answers partially: its obstruction is sufficient and not complete ([THEORY-012](../theory.d/THEORY-012.md)). For the topos setting, the reader does not know of a complete answer (unverified).

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary, with one precision. The seed's "a certain presheaf defined on the category of self-adjoint operators" is right for the paper's main statement: the spectral presheaf Σ on O_d (Def. 2.2), whose base is operators ordered by functional dependence, not commutative subalgebras. The paper gives a second, equivalent form on the poset W of Boolean subalgebras of the projection lattice (the dual presheaf D, Def. 2.3), and a third on all of O (D∘W). The base category of commutative von Neumann subalgebras, with Gelfand spectra, is *not* in this paper. Footnote 6 mentions the abelian-subalgebra category and credits Kochen–Specker with noting it. It is Part III (quant-ph/9911020) that takes it up.
- Series identifiers. The seed's "from memory" arXiv ids for Parts II–IV are now verified against arXiv abstract pages: II is quant-ph/9808067 ("Conceptual Aspects, and Classical Analogues"); III is quant-ph/9911020 ("Von Neumann Algebras as the Base Category"; its authors, Hamilton, Isham & Butterfield, and venue were not checked); IV is quant-ph/0107123 ("Interval Valuations"). This paper's own reference [16] misprints Part II as "quant-ph/980867".
- Dates. arXiv v1 is 20 Mar 1998 (v2 25 Mar, v3 31 Aug, v4 13 Oct 1998). Under nucleation's first-appearance convention, `published:` would be 1998-03-20 rather than the journal's 1998-11-01. The seed's value is left below for the owner to decide. IJTP 37(11):2669–2733 was not checked against the publisher.
