---
number: 292
status: Read
formerly:
- NOTE-tmph2vm6
paper: LIT-335
title: 'A topos foundation for theories of physics: II. Daseinisation and the liberation of quantum theory'
version: 2
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/0703062 v1 (7 Mar 2007, the
    only arXiv version), from the arXiv PDF, 34 pp. I read the abstract,
    §§1–5 (daseinisation; the Heyting algebra Sub_cl(Σ); optimality of
    daseinised sub-objects; truth values and truth objects; the presheaf
    P_clΣ), the acknowledgements and all 16 references. Nothing was skipped.
    I checked the proofs the paper gives: Thm 2.1, Thm 2.4, Thm 2.5 and Thm
    3.1 with Lemma 3.2. I also checked the paper's own statement that
    Kochen–Specker is equivalent to Σ having no global elements against
    Isham–Butterfield 1998 (arXiv quant-ph/9803055 v4, §2.3), which I
    searched for its statement of that theorem and its dual-presheaf
    definition. Papers I, III and IV of the series were read in full
    alongside. `pdftotext` was not available, so I extracted the text with
    PyMuPDF. The published J. Math. Phys. text (paywalled) was not seen.).
    The first NOTE on this paper, which was seeded from its abstract alone.
- version: 2
  date: '2026-10-01'
  note: >-
    Part III's author order corrected (Hamilton, Isham & Butterfield); KS
    II–IV are now registered, and the note names them.
date: '2026-09-29'
summary: >-
  A projector P̂ is mapped to the clopen sub-object δ(P̂) of the spectral
  presheaf Σ over the poset V(H) of abelian von Neumann subalgebras, by
  "daseinisation" (de Groote's V-support): δ(P̂)_V = the least projector
  in V above P̂. The map is injective and preserves ∨, but only δ(P̂∧Q̂) ⪯
  δ(P̂)∧δ(Q̂). This represents the propositional language PL(S) in the
  Heyting algebra Sub_cl(Σ). A pure state gives the truth object T^ψ, and
  "A ε Δ" gets the sieve-valued truth value {V′ ⊆ V | ⟨ψ|δ(Ê[A∈Δ])_{V′}|ψ⟩
  = 1}.
---

# NOTE-292: A topos foundation for theories of physics: II. Daseinisation and the liberation of quantum theory

## Contribution

The paper gives the quantum-theoretic representation of the propositional language PL(S) of paper I ([LIT-343](../literature.d/LIT-343.md)). The topos is Sets^{V(H)^op}, the presheaves over the poset V(H) of unital abelian von Neumann subalgebras of B(H), excluding ℂ1̂, ordered by inclusion. The state object is the spectral presheaf Σ, whose value at V is the Gel'fand spectrum Σ_V and whose restriction maps are λ ↦ λ|_{V′}.

The new ingredient relative to Isham–Butterfield ([LIT-325](../literature.d/LIT-325.md)) is de Groote's approximation of a projector from inside each context. This turns every projector into a clopen sub-object of Σ and gives a clean map from quantum propositions into a Heyting algebra. The second half defines truth objects: sub-objects of PΣ that play the role of states, because Σ has no global elements.

## Key insight

A context V cannot see P̂ unless P̂ ∈ V, so it sees the strongest proposition it can express that P̂ implies, namely δ(P̂)_V = ⋀{Q̂ ∈ P(V) | Q̂ ⪰ P̂}. Collected over all contexts, these coarse-grainings form a global element of the outer presheaf. Through Gel'fand duality they form a clopen sub-object of Σ, the quantum "subset of state space".

Nothing is lost, since the map is injective (Thm 2.1). Quantum logic's non-distributivity is traded for distributivity plus a one-sided inequality: ∨ is preserved exactly and ∧ only up to ⪯. Truth is then relative to the context and is valued in sieves: the proposition is true at stage V over exactly those subcontexts V′ ⊆ V in which its coarse-graining has probability 1 in the state.

## Assumptions

- **Contexts.** Unital abelian von Neumann subalgebras, not C*-subalgebras. The reason given is that their projection lattices are complete, which (2.1) needs (fn. 9). The trivial algebra ℂ1̂ is excluded (§2.1.1).
- **Topology.** Each Σ_V is a compact Hausdorff space (for von Neumann algebras, extremely disconnected). Projectors in V correspond to clopen subsets of Σ_V by a lattice isomorphism (2.24). Openness of the restriction maps r : Σ_V → Σ_{V′} is imported from de Groote (fn. 18).
- **Dimension.** Implicitly dim H > 2 wherever "Σ has no global elements" is used (see corrections).
- **States.** Pure states |ψ⟩ are primary. Density matrices give truth objects too (4.32), but ρ cannot in general be recovered from T^ρ.

## Key results

- **Outer presheaf (Def 2.1).** O_V = P(V), with restriction α̂ ↦ δ(α̂)_{V′}. V ↦ δ(P̂)_V is a global element of O (2.2), and P̂ = ⋀_V δ(P̂)_V (2.4).
- **Thm 2.1 (injectivity).** δ : P(H) → ΓO is injective. The proof is a case analysis in V₁ = {P̂₁, 1̂}″.
  - *Minor gap.* The proof needs P̂₁ ∉ {0̂, 1̂}, because {0̂,1̂}″ = ℂ1̂ is not a context. The WLOG step states only P̂₁ ≠ 1̂. The gap closes trivially: if {P̂₁,P̂₂} = {0̂,1̂}, any context separates them.
- **Order and joins (2.8), (2.11); inequality for meets (2.14)–(2.15).** δ(P̂) ⪰ δ(Q̂) iff P̂ ⪰ Q̂. δ(P̂ ∨ Q̂) = δ(P̂) ∨ δ(Q̂). δ(P̂ ∧ Q̂) ⪯ δ(P̂) ∧ δ(Q̂), strictly for Q̂ = 1̂ − P̂.
  - Local ∧ on ΓO is not defined. The authors therefore define "hyper-elements", γ(V′) ⪰ O(i)(γ(V)), on which ∧ and ∨ are both local (2.16)–(2.22).
- **Thm 2.4.** S_P̂ = {S_{δ(P̂)_V}}_V is a clopen sub-object of Σ, where S_α̂ = {λ | λ(α̂) = 1}. The proof is complete and elementary. Daseinisation (Def 2.5) is the map P̂ ↦ S_P̂.
- **Thm 2.5.** Sub_cl(Σ) is a Heyting algebra. ∧ and ∨ are stagewise ∩ and ∪.
  - *Negation.* (¬S)_V = int ⋂_{V′⊆V} {λ | λ|_{V′} ∉ S_{V′}} (2.39). The interior is needed because V may have infinitely many subalgebras.
  - *Implication.* "A straightforward extension … gives a consistent definition of S ⇒ T". It is not written out.
  - *My check.* The interior of an intersection of clopens in these spaces is clopen. Openness of restriction makes (2.39) restriction-stable, so ¬S is a sub-object. The pseudo-complement and relative pseudo-complement laws are not verified in the paper.
- **Daseinisation versus quantum logic (§2.4).** (2.44) δ(P̂∨Q̂) = δ(P̂)∨δ(Q̂). (2.45) δ(P̂∧Q̂) ⪯ δ(P̂)∧δ(Q̂). Both cannot be equalities, since P(H) is not distributive.
  - *Consequence for PL(S).* The axiom A ε Δ₁ ∨ A ε Δ₂ ⇔ A ε Δ₁∪Δ₂ can be added (2.57), but A ε Δ₁ ∧ A ε Δ₂ ⇔ A ε Δ₁∩Δ₂ cannot (2.58); only π(A ε Δ₁∩Δ₂) ⪯ π(A ε Δ₁ ∧ A ε Δ₂) holds (2.55).
- **Inner daseinisation and negation (§2.4.2).** δ^i(P̂)_V = ⋁{Q̂ ∈ P(V) | Q̂ ⪯ P̂} (de Groote's "core"), which gives an inner presheaf I. δ^o(1̂ − P̂)_V = 1̂ − δ^i(P̂)_V (2.62). The orthocomplement is thus carried to a different presheaf, not to the Heyting negation ¬δ(P̂).
  - O ≅ I in the topos is asserted without proof.
- **Thm 3.1 (optimality).** S_{O(i)(δ(P̂)_V)} = Σ(i)(S_{δ(P̂)_V}). The proof uses Lemma 3.2 and de Groote's openness result. So daseinised sub-objects are exactly those whose restriction maps are surjective at every stage (they are "as small as they can be" going down), while a general sub-object only maps K_V into K_{V′}. Hence Sub_cl(Σ) contains sub-objects that are not of the form δ(P̂).
- **Truth values (§4).**
  - *In a topos.* ν(x ∈ K) = χ_K ∘ ⌜x⌝ ∈ ΓΩ (4.4). In a presheaf topos this is the sieve {V′ ⊆ V | x_{V′} ∈ K_{V′}} (4.6).
  - *Why truth objects.* Σ has no global elements, so states cannot be points. In L(S) the alternative is a term T̃ of type PPΣ, and ν(A ε Ξ; T) is the evaluation of {s̃ | A(s̃) ∈ Δ̃} ∈ T̃ (4.15)–(4.18).
  - *Classical check.* The classical truth object T_s = {K | s ∈ K} (4.24) recovers ordinary truth values (4.25).
- **Quantum truth object (§4.2.4).** T^ψ_V = {α̂ ∈ O_V | ⟨ψ|α̂|ψ⟩ = 1} (4.29), taken from the earlier papers; its least element at V is δ(P̂_ψ)_V (4.30).
  - *Truth value.* ν(A ε Δ; |ψ⟩)_V = {V′ ⊆ V | ⟨ψ|δ(Ê[A∈Δ])_{V′}|ψ⟩ = 1} (4.31), (4.41). The map |ψ⟩ ↦ T^ψ is injective up to phase; ρ ↦ T^ρ is not.
- **P_clΣ (§4.3).** A presheaf with Γ(P_clΣ) ≅ Sub_cl(Σ), and a monic ⌜ι⌝ : O → P_clΣ. Naturality is left undone ("we will spare the reader the ordeal"), and monicity is "a straightforward exercise and the details will not be given".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Daseinisation δ : P(H) → Sub_cl(Σ) is injective and order-preserving | proof (elementary; minor WLOG gap, closable) | Thm 2.1, (2.8), §2.2.2 item 3 |
| C2 | δ preserves ∨ exactly and ∧ only up to ⪯, with strictness for complementary projectors | proof | (2.10)–(2.15), (2.44)–(2.45); Lemma 2.3's proof is one line ("straightforward consequence") but the statement is correct (δ_V is a left adjoint) |
| C3 | Sub_cl(Σ) is a Heyting algebra | informal argument / sketch | Thm 2.5. ∧, ∨ and ¬ are given, ⇒ is left to "straightforward extension", and the Heyting laws are not checked |
| C4 | Daseinised sub-objects are exactly the "optimal" ones, with surjective restrictions | proof, using de Groote's openness of restriction | Thm 3.1, Lemma 3.2 |
| C5 | Σ has no global elements, and this is equivalent to Kochen–Specker | cited, not proved; stated without the required dim H > 2 | pp. 3, 10, 24–25; the source is Isham–Butterfield / Hamilton–Isham–Butterfieldsham |
| C6 | A pure state gives a truth object T^ψ ⊆ O, and propositions get sieve-valued truth values (4.41) | definition plus short check | (4.29)–(4.31). That T^ψ is a sub-object is checked in the text |
| C7 | O is a sub-object of P_clΣ via a monic ⌜ι⌝, so T^ψ is a sub-object of P_clΣ | assertion (proof omitted) | §4.3.2 |
| C8 | O and I are isomorphic objects in the topos | assertion | §2.4.2, end |
| C9 | Daseinisation "liberates" projectors "from the shackles of quantum logic" | rhetoric | §2.4. What is shown is C2 |

## Method

Daseinisation is order-theoretic approximation, de Groote's V-support and core, carried out context by context. Gel'fand duality turns it into clopen subsets. Presheaf-topos bookkeeping (sieves, power objects, characteristic arrows) handles the rest, with standard results from Goldblatt, Bell and Kadison–Ringrose. There are no computations or examples beyond the complementary-projector witness for (2.14).

## Concepts

- **V(H).** The category of contexts: unital abelian von Neumann subalgebras of B(H) other than ℂ1̂, ordered by inclusion. A "Weltanschauung" in the paper's gloss.
- **Spectral presheaf Σ.** The Gel'fand spectra Σ_V, with restriction of characters as the maps. Points of Σ_V correspond to ultrafilters in P(V); paper III, eq. 3.28, states this explicitly ([LIT-299](../literature.d/LIT-299.md)).
- **Outer and inner daseinisation.** δ^o(P̂)_V = least projector in V above P̂ (de Groote's "V-support"). δ^i(P̂)_V = greatest projector in V below P̂ (de Groote's "core").
- **Outer and inner presheaves O, I.** P(V) at each stage, with daseinisation as restriction. O is Isham–Butterfield's coarse-graining presheaf G.
- **Clopen sub-object; Sub_cl(Σ).** A sub-object that is clopen at every stage. The algebra of such sub-objects is the representation target of PL(S).
- **Truth object.** A global element of P(PΣ) that replaces a microstate. For a pure state it is T^ψ.
- **Hyper-element.** A stagewise family with γ(V′) ⪰ O(i)(γ(V)). It is a device for defining local ∧ on O.

## Connections

- **Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md)) and its sequels (KS II–IV, registered 2026-10-01 as [LIT-381](../literature.d/LIT-381.md), [LIT-380](../literature.d/LIT-380.md) and [LIT-382](../literature.d/LIT-382.md)).** These are cited as [13]–[16]. Kochen–Specker ⇔ no global elements, the coarse-graining presheaf, generalised valuations valued in sieves, and T^ψ are all taken from there. The paper calls its own contribution "a satisfying (for us) completion of the earlier work" (§5). The base category is V(H), following Hamilton–Butterfield–Isham 2000 (KS III), not Isham–Butterfield 1998's category of self-adjoint operators under functional relations or its Boolean subalgebras W.
- **de Groote 2005 (math-ph/0507019, 0509020).** The source of δ^o and δ^i and of the openness result behind Thm 3.1. Not in the record.
- **Paper III ([LIT-299](../literature.d/LIT-299.md)).** It extends daseinisation to self-adjoint operators and identifies Gel'fand points with ultrafilters.
- **Abramsky–Brandenburger ([LIT-016](../literature.d/LIT-016.md)) and [THEORY-012](../theory.d/THEORY-012.md).** Same shape, different object. [THEORY-012](../theory.d/THEORY-012.md) says a model is noncontextual iff its compatible family of *distributions* over a finite measurement cover has a nonnegative global section. In this paper the presheaf is Σ over all abelian subalgebras. Its global elements are deterministic valuations on all projectors (Isham–Butterfield's dual presheaf in operator-algebraic form), and a state enters only through T^ψ, i.e. the propositions it makes certain.
  - *My comparison.* Σ's lack of global sections is the state-independent, possibilistic Kochen–Specker statement. It is the all-contexts, infinite analogue of the strong contextuality of the Kochen–Specker support tables in [LIT-016](../literature.d/LIT-016.md) and [LIT-277](../literature.d/LIT-277.md). It does not register probabilistic contextuality (Bell, Hardy), because Σ does not depend on the state. It says nothing about [THEORY-012](../theory.d/THEORY-012.md)'s second clause, since there are no probabilities, signed or otherwise; density matrices as "some sort of measure on Σ" are left as "one of the many interesting tasks for the future" (§4.2.4).
  - This confirms [NOTE-016](NOTE-016.md)'s account of the relation: Abramsky–Brandenburger credit Isham–Butterfield for the global-section insight but have measurement covers and a distribution functor, which the topos approach lacks.
- **[LIT-277](../literature.d/LIT-277.md) and [LIT-278](../literature.d/LIT-278.md) (Čech cohomology of contextuality).** No relation in this paper. There is no cohomology, no obstruction class and no finite criterion. Σ over the infinite poset V(H) is not a finite cover. Getting a computable witness would need a restriction of the kind [LIT-277](../literature.d/LIT-277.md) makes to finite Kochen–Specker covers. Neither paper builds that bridge.
- **[THEORY-017](../theory.d/THEORY-017.md) (only unitarily invariant structure is intrinsic).** Consistent with it. This paper keeps all contexts at once and privileges none. Choosing one abelian subalgebra, i.e. one basis or one MASA, is exactly the extra datum [THEORY-017](../theory.d/THEORY-017.md) says is not intrinsic. Paper III §5 makes the unitary covariance of the construction explicit ([LIT-299](../literature.d/LIT-299.md)).
- **[LIT-262](../literature.d/LIT-262.md) (van Rijsbergen).** Van Rijsbergen represents predicates by projectors in the orthomodular P(H). This paper is the explicit alternative: the same projectors pushed into a distributive Heyting algebra, at the price of C2.

## Bearing on the record

- **The map's role (§0, row 8: the spectral-presheaf program "owns §2.1").**
  - *The claim holds for the structural step, with the wrong owner named first.* "No global ultrafilter → presheaf over contexts → Kochen–Specker" is Isham–Butterfield 1998's dual presheaf on Boolean subalgebras (D(W) = Hom(W,{0,1}), i.e. ultrafilters) and their Kochen–Specker restatement ([LIT-325](../literature.d/LIT-325.md) §2.3, "if dim H > 2"). This paper uses that result; it does not prove it.
  - *What this paper owns.* It owns what one does after accepting that there are no global points:
    - propositions become clopen sub-objects via daseinisation;
    - their logic is Heyting, not orthomodular;
    - states become truth objects and truth values become sieves.
  - *Citation.* The map should cite Isham–Butterfield 1998 for the §2.1 step and this paper for the propositional apparatus.
- **"The fix is *their* presheaf" (map row 8).** The presheaf does not restore global points: Σ still has none. The "fix" is a change of logic (C2, C3) plus truth objects (C6).
  - A "Topos of Bricks" that instantiates their presheaf inherits both consequences.
    - Conjunction of non-co-measurable concepts is only bounded above: δ(P̂∧Q̂) ⪯ δ(P̂)∧δ(Q̂).
    - Negation is the Heyting pseudo-complement, not the orthocomplement. The orthocomplement goes to inner daseinisation instead (2.62).
  - The map's rows 1 and 3 lean on orthocomplement negation. That is a different logic from the one this programme supplies, and the owner's documents should say which logic §2.1 uses.
- **The map's §2 item 4 ("exhibit no-global-tope contextuality on real embeddings").**
  - *No finite witness.* This paper gives no finite or computable witness. Its no-global-section fact is about all abelian subalgebras of B(H) with dim H > 2.
  - *Finite families can have global sections.* A finite family of concept projectors generates a finite sub-poset of contexts, and the restricted presheaf may well have global sections. Kochen–Specker failure needs specific configurations (KS sets). Whether a given embedding family is contextual must be decided for that family, by the finite methods of [LIT-016](../literature.d/LIT-016.md) or [LIT-277](../literature.d/LIT-277.md)/[LIT-278](../literature.d/LIT-278.md), not by citing this programme.
  - *No topes.* Nothing here concerns hyperplane arrangements or topes. The identification "ultrafilter = tope" is the owner's, not the programme's.
- **ML practice.** It carries nothing for ML practice.
- **For filing.** `quantum-foundations` first. `contextuality` fits: this is a sheaf-theoretic form of Kochen–Specker. `logic` fits: this is the Heyting representation of a propositional language. `mathematics` fits as well. `anthology-candidate` is not proposed.

## Limitations

- **Proofs are incomplete in places.** The implication in Thm 2.5, the naturality and monicity of ⌜ι⌝ (§4.3.2) and O ≅ I are asserted, not proved. The Heyting laws for the interior-modified negation are not checked.
- **The dimension hypothesis is dropped.** Without it, "Σ has no global elements" is false for dim H = 2.
- **Truth objects are thin.** Only probability-1 facts about a state reach the truth values. The authors concede that no theory of truth objects exists, that density matrices are not recovered, and that superposition of truth objects is open (§5).
- **It restates rather than predicts.** Everything reproduces standard quantum theory's content in new form. There is no new physical prediction, and the authors say the main goal is tools for theories "beyond" quantum theory, which are not supplied.

## Open questions

- Is Sub_cl(Σ) a complete Heyting (or bi-Heyting) algebra in full generality, with the implication written out? It is not settled here, and I did not check later literature.
- What characterises the truth objects among the elements of P(PΣ)? Is there a superposition operation on truth objects, and how is a mixed state represented, as a measure on Σ (§4.2.4, §5)?
- For a finite family of projectors, with contexts the abelian algebras they generate, when does the restricted spectral presheaf fail to have a global section, and how does that compare with the Čech witnesses of [LIT-277](../literature.d/LIT-277.md) and [LIT-278](../literature.d/LIT-278.md)? This paper does not pose the question, but the map needs it answered.

## Corrections to the seeded skim

- Seeded from metadata. The seed's summary is right as far as it goes. The text adds three things. (a) "Daseinisation" is de Groote's construction, his "V-support" (outer) and "core" (inner), renamed (§2.1.1, §2.4.2); the paper says so. (b) The "outer presheaf" O is the "coarse-graining presheaf" G of the Isham–Butterfield papers, renamed (fn. 10). (c) The second half of the paper introduces truth objects, the state substitute. The seed does not mention them.
- The paper states without qualification that Σ "has no global elements (this statement is equivalent to the Kochen-Specker theorem)" (pp. 3, 10, 24–25). The equivalence it cites needs dim H > 2. Isham–Butterfield 1998 states the condition ("if dim H > 2", §2.3); this paper and paper III drop it.
  - *Counter-case.* For H = ℂ² every object of V(H) is a maximal abelian subalgebra, because the trivial algebra ℂ1̂ is excluded by definition (§2.1.1). No two objects are comparable, so a global element is just an independent choice of a spectral point in each Σ_V, and one exists. This is my check, not the paper's.
- The Kochen–Specker ⇔ no-global-section equivalence is not proved here. It is imported from the earlier papers ([13]–[16], [8]).
- Identifiers check against the arXiv listing: journal-ref J. Math. Phys. 49:053516 (2008); DOI 10.1063/1.2883742; "34 pages, no figures". arXiv v1 is 7 Mar 2007. The seed's `published: 2008-05-01` is the journal issue (flagged only, as for [LIT-343](../literature.d/LIT-343.md)).
