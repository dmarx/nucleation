---
status: Read
paper: LIT-tmpcerv7
title: "'What is a Thing?': Topos Theory in the Foundations of Physics"
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (full text of arXiv:0803.0417 v1, 4 Mar 2008, the only
    arXiv version, 212 pp. from the arXiv PDF; text extracted with
    PyMuPDF). I read the abstract, §§1–15 and Appendix 1 (§16). Of
    Appendix 2, the textbook introduction to topos theory, §§17.1–17.2
    were read and §17.3 skimmed. The 73 references were sampled, not read
    through. I checked the proofs the paper gives for Thms 5.1, 5.4, 7.1,
    8.1, 8.4–8.6, 16.2 and Lemma 13.1 against the definitions, and compared
    the text with the record's readings of papers I–IV (NOTE-277,
    NOTE-292, NOTE-290, NOTE-285) to separate what is new from what is
    reprinted. Results the paper cites from de Groote, from Döring's
    antonymous-functions paper and from Hamilton–Butterfield–Isham were
    taken as stated. The published Springer text was not seen.
date: '2026-10-01'
summary: >-
  The Döring–Isham programme in one volume. A theory of a system is a
  representation of a typed language L(S) in a topos. In quantum theory,
  presheaves over the abelian von Neumann subalgebras V(H), daseinisation
  sends projectors injectively to clopen sub-objects of the spectral
  presheaf Σ, preserving ∨ but not ∧. A pure state gives sieve-valued truth
  values. Every bounded self-adjoint Â becomes an arrow Σ → ℝ^↔ whose value
  at a point is a pair of monotone functions, an interval that widens as
  contexts coarsen. Most of it reprints papers I–IV. New are the
  inverse-image corollary linking PL(S) and L(S), values in a pseudo-state,
  and the algebra of the quantity-value candidates. The Heyting structure
  on Sub_cl(Σ) is still only sketched.
---

# NOTE-tmpz02gq: 'What is a Thing?': Topos Theory in the Foundations of Physics

## Contribution

The paper collects papers I–IV of the topos programme ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md),
[LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md)) into one corrected text, with background from
Isham–Butterfield ([LIT-325](../literature.d/LIT-325.md)) and some new material. The new material is:

- a definition of the "value" of a physical quantity in a pseudo-state (§8.5);
- a proof that the daseinised propositions of the propositional language
  PL(S) are inverse images in the typed language L(S) (Thm 8.6, Cor 8.7);
- an account of the algebra of the candidate quantity-value objects (§9.3);
- daseinisation over Boolean subalgebras of P(H) as an alternative base
  category (§5.5.3);
- Kochen–Specker restated as a lifting obstruction (§6.6);
- a comparison with Heunen and Spitters' independent construction of Σ (§14).

There is no new no-go theorem and no new physics.

## Key insight

Quantum theory can be made to "look like" classical physics if Sets is
replaced by the presheaf topos Sets^{V(H)^op}:

- the spectral presheaf Σ plays the state space;
- clopen sub-objects of Σ play propositions;
- arrows Σ → ℝ^↔ play real-valued functions;
- sieves on contexts play truth values.

The price is that Σ has no points (that is Kochen–Specker), so a state
becomes a sub-object, the pseudo-state w^ψ = δ(|ψ⟩⟨ψ|). Truth then becomes
inclusion, w^ψ ⊆ δ(P̂), evaluated stage by stage. The authors call this
"neo-realism". Every proposition gets a truth value, but the values live in
a Heyting algebra of sieves, not in {0, 1}.

## Assumptions

- **Setting.**
  - H is a Hilbert space (separable in §13). B(H) is the algebra of bounded operators on it.
  - V(H) is the poset of unital abelian von Neumann subalgebras, ordered by inclusion. The trivial algebra ℂ1̂ is excluded (p. 56) and has to be re-admitted ad hoc as V(H₁)* in §13.3.
  - The topos is Sets^{V(H)^op}.
- **Physical quantities** are bounded self-adjoint operators. Unbounded ones are not treated.
- **Propositions** are "A ε Δ" with Δ a Borel subset of ℝ.
- **States** are vector states |ψ⟩. A density matrix ρ gives a truth object T^ρ, but ρ cannot be recovered from it (§6.3.2), so mixed states are only partly handled.
- **Dimension.** "Σ has no global elements" needs dim H > 2. This is stated where Kochen–Specker is introduced (pp. 50, 53, 70) and dropped everywhere else it is used (p. 13 fn. 14, p. 16, p. 62, p. 73).
- **Kochen–Specker** is assumed, not proved. Its equivalence with "no global elements of Σ" is shown only for discrete-spectrum operators ordered by functional dependence (Def. 5.1, p. 53) and for the dual presheaf on Boolean subalgebras (p. 70). For V(H) it is cited to Hamilton–Butterfield–Isham [35].
- **Logic.** PL(S) and L(S) carry intuitionistic deduction by choice (§3.2.1), so that non-Boolean topoi can host representations.
- **Systems (§§11–12).** The axioms for the category Sys and its topos realisations are offered as "partly 'experimental'" (p. 182), and several are labelled conjectures (Rule 6, p. 161).

## Key results

- **Daseinisation of projectors (§5).**
  - Definition: δ(P̂)_V := ⋀{α̂ ∈ P(V) | α̂ ⪰ P̂} (5.9), de Groote's V-support. Inner daseinisation is δ^i(P̂)_V := ⋁{β̂ ∈ P(V) | β̂ ⪯ P̂} (5.57).
  - Injectivity (Thm 5.1): P̂ ↦ δ(P̂) is injective into ΓO, because P̂ = ⋀_V δ(P̂)_V (5.12).
  - Order and joins: δ preserves order and ∨, δ(P̂ ∨ Q̂) = δ(P̂) ∨ δ(Q̂) (5.41). For meets only δ(P̂ ∧ Q̂) ⪯ δ(P̂) ∧ δ(Q̂) holds (5.42), strictly for Q̂ = 1̂ − P̂ (p. 60).
  - Consequence for PL(S): the axiom "A ε Δ₁ ∨ A ε Δ₂ ⇔ A ε Δ₁∪Δ₂" may be added (5.54), but not its conjunctive version (5.55).
  - Clopen sub-objects (Thm 5.4): each δ(P̂) is a clopen sub-object of Σ.
  - Optimality (Thm 16.2, eq. 5.66): S_{δ(P̂)_{V′}} = Σ(i_{V′V})(S_{δ(P̂)_V}). The restriction maps of a daseinised projector are surjective, so these sub-objects are the smallest compatible ones.
  - Complements: δ^o(1̂ − P̂)_V = 1̂ − δ^i(P̂)_V (5.59). The orthocomplement goes to inner daseinisation, not to Heyting negation. The outer and inner presheaves are isomorphic (p. 69).
- **Heyting structure (Thm 16.1).**
  - Sub_cl(Σ) is called a Heyting algebra.
  - ∧ and ∨ are stagewise ∩ and ∪.
  - ¬S is redefined as int ⋂_{V′⊆V} Σ(i_{V′V})⁻¹(S_{V′}ᶜ) (16.10), so that it stays clopen.
  - ⇒ is left to "a straightforward extension of this method" (p. 188).
- **Kochen–Specker as no global section.**
  - Σ on discrete-spectrum operators has no global elements iff Kochen–Specker holds, for dim H > 2 (p. 53).
  - The same holds for the dual presheaf D(B) = Hom(B, {0,1}) on Boolean subalgebras (p. 70).
  - §6.6 restates it: the name ⌜w^ψ⌝ : 1 → PΣ cannot be lifted through π : Σ → PΣ, which is the transpose of ⟦σ̃₁ = σ̃₂⟧. That is presented as a hint toward a cohomological (Postnikov-type) account, not developed.
- **Truth values (§6).**
  - The truth object of a pure state is T^ψ_V = {α̂ ∈ P(V) | ⟨ψ|α̂|ψ⟩ = 1} (6.26). It is injective in ψ up to phase.
  - The truth value is ν(A ε Δ; ψ)_V = {V′ ⊆ V | ⟨ψ|δ(Ê[A∈Δ])_{V′}|ψ⟩ = 1} (6.51).
  - Equivalently, δ(P̂) ∈ T^ψ iff w^ψ ⊆ δ(P̂), where w^ψ := δ(|ψ⟩⟨ψ|) (6.39).
  - T^ψ localises the atomic quasi-point {α̂ ⪰ |ψ⟩⟨ψ|}, a maximal filter in P(H) (6.31–6.32).
  - Some sub-object, P_clΣ, has Γ(P_clΣ) ≅ Sub_cl(Σ), and there is a monic O → P_clΣ (§6.5). Both are asserted with the checks omitted.
- **Daseinisation of self-adjoint operators (§7).**
  - Definition: δ^o(Â)_V = ∫ λ d(δ^i(Ê^A_λ)_V) and δ^i(Â)_V = ∫ λ d(⋀_{μ>λ} δ^o(Ê^A_μ)_V) (7.15–7.16). These are the best approximations to Â in V in the spectral order.
  - Spectra: sp(δ^o(Â)_V) ⊆ sp(Â) (7.23).
  - Both maps Â ↦ δ^o(Â), δ^i(Â) are injective (Thm 7.1). Both are non-linear.
- **Quantity-value objects (§8).**
  - The "non-commutative spectral theorem" (Thms 8.1–8.2): δ̆^o(A) : Σ → sp(Â)^⪰ ⊆ ℝ^⪰ and δ̆(A) = (δ̆^i(A), δ̆^o(A)) : Σ → ℝ^↔ are natural transformations, and Â ↦ δ̆(A) is injective.
  - ℝ^↔_V is the set of pairs (μ, ν) with μ order-preserving, ν order-reversing on ↓V, and μ ≤ ν.
  - The real-number object is ruled out: it is the constant presheaf ℝ, and the Gel'fand transforms of δ^o(Â)_V grow as V shrinks (8.4).
- **Observable and antonymous functions (§8.3).**
  - f_{δ^o(Â)_S}(F) = f_Â(C_N(F)) (Thm 8.4) and g_{δ^i(Â)_S}(F) = g_Â(C_N(F)) (Thm 8.5). These rest on Lemma 8.3, (δ^i_S)⁻¹(F) = C_N(F).
  - For a vector state, g_Â(T^ψ) < ⟨ψ|Â|ψ⟩ < f_Â(T^ψ) unless ψ is an eigenvector (8.49). This is cited from [20], not proved.
- **Values in a pseudo-state (§8.5, new).**
  - The composite w^ψ ↪ Σ → ℝ^↔ is a sub-object of ℝ^↔ (8.65).
  - If ψ is an eigenvector of Â and Â ∈ V, both components equal the eigenvalue at stage V.
  - Worked example for Â = |ψ⟩⟨ψ|: the outer component is constantly 1. The inner component is 1 exactly at subcontexts containing |ψ⟩⟨ψ| and 0 elsewhere (8.74).
- **PL(S) inside L(S) (Thm 8.6, Cor 8.7, new).** δ̆(P̂)⁻¹(δ̆(P̂)(δ^o(P̂))) = δ^o(P̂) for every non-zero projector. So daseinised propositions are inverse images of sub-objects of ℝ^↔.
- **Algebra of the quantity-value candidates (§9, App. 16).**
  - ℝ^↔ and ℝ^⪰ are commutative monoid objects, not groups.
  - ℝ^↔/≡ ≅ k(ℝ^⪰) via [μ, ν] ↦ [ν, −μ] (9.6).
  - k(ℝ^⪰) and k(ℝ^↔) are vector-space objects over the real-number object (Remarks 9.1–9.2). ℝ^↔ has only a "pseudo-subtraction" (9.17).
  - k(Γℝ^⪰) ≅ functions of bounded variation on Ob(V(H)) (§16.3).
  - Squares exist for elements [ν, 0] (16.36), which allows an "intrinsic dispersion" ∇(Â) = δ̆^o(A²) − δ̆^o(A)² (9.4). Arrows into ℝ^↔ cannot be squared.
  - Whether [δ̆(A)] into ℝ^↔/≡ determines Â is left open (p. 125).
- **Unitaries (§10).**
  - Covariance: Û δ^o(P̂)_V Û⁻¹ = δ^o(ÛP̂Û⁻¹)_{ℓ_U(V)} (10.16), and truth values transform covariantly (10.26).
  - Û ↦ ℓ*_Û is an anti-representation of U(H) by arrows of the topos (10.29).
  - Natural isomorphisms Σ ≅ Σ^Û and ℝ^⪰ ≅ (ℝ^⪰)^Û intertwine δ̆(A) with δ̆(Û⁻¹ÂÛ) (Thms 10.1–10.3). The proof of 10.1 is omitted.
  - Daseinised unitaries of a Lie-group representation commute at each stage, so they do not represent the group (10.9).
- **Systems (§§11–13).**
  - Sys is a symmetric monoidal category under composite ⋄ (unit the trivial system 1) and under disjoint sum ⊔ (unit 0). Its arrows are translations of local languages.
  - Each arrow j : S₁ → S is to be realised by the inverse-image part of a geometric morphism τ_φ(j), with arrows φ(j) : Σ_{S₁} → τ_φ(j)Σ_S and β_φ(j) : τ_φ(j)R_S → R_{S₁} (Def. 12.3).
  - The trivial system's topos is Sets (13.7).
  - Classical physics satisfies the commutativity condition (12.20) exactly.
  - Quantum disjoint sums satisfy it: β ∘ μ*(δ̆(A₁⊕A₂)) ∘ φ(i) = δ̆(A₁) (13.22), via Lemma 13.1.
  - Tensor-product composites do not: the natural pull-back gives δ(Â₁)_{V_W} ⊗ 1̂ at W (13.43), which differs from δ(Â₁ ⊗ 1̂)_W at contexts W not of the form V₁ ⊗ ℂ1̂ (13.44–13.45). The authors attribute this to "operator entanglement" and state that no operator B̂ gives the pulled-back arrow, without proof (p. 172).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Daseinisation represents PL(S) in the Heyting algebra Sub_cl(Σ), injectively, preserving ∨ and order but not ∧ | strong for injectivity, order and ∨ (Thms 5.1, 5.4, eqs. 5.12–5.18); weak for "Heyting" | Thm 16.1 leaves ⇒ unwritten and the laws unchecked |
| C2 | Kochen–Specker is equivalent to Σ having no global elements | strong for discrete spectra and for D on Bl(H), given KS and dim H > 2 | Def. 5.1 and p. 70 are definitional; the V(H) version is cited [35] |
| C3 | A pure state gives sieve-valued truth values to all propositions, and pseudo-states w^ψ are "as close to microstates as one can get" | strong for the construction (6.26–6.39); the "closest" is informal | a pseudo-state is not even minimal in Sub_cl(Σ) (p. 85) |
| C4 | Every bounded self-adjoint operator is faithfully represented by an arrow Σ → ℝ^↔ (or ℝ^⪰), and the quantity-value object is not the real-number object | strong | Thms 7.1, 8.1–8.2; eq. 8.4 |
| C5 | δ̆(A) gives the state-independent "range" of A; its value in w^ψ recovers the eigenvalue for eigenstates | moderate | §8.4–8.5; interval reading leans on cited results (8.47–8.49) |
| C6 | Daseinised propositions are L(S) inverse images (PL(S) sits inside L(S)) | strong | Thm 8.6 and Cor 8.7, short correct proofs |
| C7 | Classical physics fits the Sys axioms exactly; quantum theory fits disjoint sums but not composites | strong for the classical and disjoint-sum cases (13.22); the "no B̂" claim is asserted | §§11.4, 13.2–13.3 |
| C8 | "The second source of real numbers [probabilities] has gone completely" (§15) | weak | only probability-one information enters truth objects; no Born probabilities are recovered in the paper |
| C9 | Quantum computation is "classical" computation in Sets^{V(H)^op} (§14.1.3) | assertion | labelled a conjecture, with no argument |

## Concepts

- **Context / stage.** An object V of V(H), an abelian von Neumann subalgebra. The paper also calls it a "classical snapshot" or "world-view".
- **Spectral presheaf Σ.** Σ_V is the Gel'fand spectrum of V. Restriction is restriction of multiplicative functionals.
- **Daseinisation (outer δ^o, inner δ^i).** The best approximation of P̂ (or Â) in each context, from above or below, in the projector order (or the spectral order).
- **Outer presheaf O.** P(V) at stage V, with δ^o as restriction. Daseinised projectors are its global elements.
- **Truth object T^ψ.** A sub-object of P_clΣ collecting what is true with probability one in ψ.
- **Pseudo-state w^ψ.** δ(|ψ⟩⟨ψ|), a sub-object of Σ that stands in for a missing point.
- **ℝ^⪰, ℝ^⪯, ℝ^↔.** The presheaves of order-reversing functions, order-preserving functions, and pairs (μ ≤ ν) of both on ↓V. Heunen and Spitters identify ℝ^↔ with the interval domain (§8.4).
- **Neo-realism.** A theory is "realist" when propositions are sub-objects of a state object and have truth values in the topos's Ω, whatever Ω is.
- **Operator entanglement.** Contexts W ∈ V(H₁ ⊗ H₂) not of the form V₁ ⊗ V₂.

## Connections

- **Papers I–IV.** This is the merged text of [LIT-343](../literature.d/LIT-343.md) (§§2–4 here), [LIT-335](../literature.d/LIT-335.md) (§§5–6), [LIT-299](../literature.d/LIT-299.md) (§§7–10) and [LIT-310](../literature.d/LIT-310.md) (§§11–13). The record's readings of them ([NOTE-277](NOTE-277.md), [NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md), [NOTE-285](NOTE-285.md)) apply here section for section. In particular:
  - the Heyting structure is as sketched as in [LIT-335](../literature.d/LIT-335.md) (its Thm 2.5 is this paper's Thm 16.1);
  - the composite-system failure and the unproved "no B̂" claim are as [LIT-310](../literature.d/LIT-310.md) had them.
- **Isham–Butterfield ([LIT-325](../literature.d/LIT-325.md)) and Kochen–Specker ([LIT-298](../literature.d/LIT-298.md)).** §5.1 reprints the origin of the programme: the Isham–Butterfield observation that a global element of Σ over discrete-spectrum operators is a FUNC valuation, and that the dual presheaf on Boolean subalgebras carries Kochen–Specker. §5.5.3 revives the Boolean base category that [LIT-325](../literature.d/LIT-325.md) introduced and "has not been used much thereafter". [THEORY-020](../theory.d/THEORY-020.md) already draws its Boolean-context half from those two readings.
- **Abramsky–Brandenburger ([LIT-016](../literature.d/LIT-016.md)).** It is not cited and postdates this paper. Both programmes locate contextuality in the absence of a global section over contexts. This one goes on to build a logic and a state-substitute in the topos; Abramsky–Brandenburger stay with empirical models and the global-section criterion. §6.6's hope for a cohomological description of the obstruction is what the cohomology line in the record later supplied for empirical models ([LIT-277](../literature.d/LIT-277.md), [LIT-278](../literature.d/LIT-278.md)).
- **Ghose ([LIT-276](../literature.d/LIT-276.md)).** That essay claims a sheafification restores Boolean logic. This paper's §15 places instrumentalism in Sets and neo-realism in the presheaf topos, linked if at all by a functor. That is a different and better-hedged proposal, and it does not support [LIT-276](../literature.d/LIT-276.md) ([THEORY-024](../theory.d/THEORY-024.md)).
- **Arsiwalla ([LIT-102](../literature.d/LIT-102.md)).** It points readers to this programme as the worked formal-language approach to pregeometry. §§2.2.1 and 4.4 are where that approach meets space-time ("M" as a ground type, regions as a locale).
- **Not held in either record.**
  - Heunen–Spitters (arXiv:0709.4364), whose internal-C*-algebra derivation of Σ §14.1.2 leans on.
  - de Groote's papers on observables and Stone spectra.
  - Corbett's qr-numbers.
  - Döring's antonymous-functions paper [20].

  Each was searched for in literature.d by arXiv id or name.

## Bearing on the record

- **[THEORY-037](../theory.d/THEORY-037.md): does not meet the promotion condition.** [THEORY-037](../theory.d/THEORY-037.md) waits for "a later Döring–Isham paper" that proves Sub_cl(Σ) is Heyting, with ⇒ written out and the pseudo-complement laws checked. This is the later paper, and it does neither. Thm 16.1 gives ∧, ∨ and the interior-corrected ¬, and leaves ⇒ to "a straightforward extension" (p. 188). The rest of [THEORY-037](../theory.d/THEORY-037.md) is supported again, from the same text:
  - δ^o(1̂ − P̂) = 1̂ − δ^i(P̂), not ¬δ(P̂) (5.59);
  - only δ(P̂ ∧ Q̂) ⪯ δ(P̂) ∧ δ(Q̂) holds (5.42);
  - the conjunctive axiom is not available (5.55).
- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected): consistent with the rejection.** The paper never claims that a global section or a sheafification restores Boolean logic. Its quantum topos is non-Boolean and has no global sections by design.
- **[THEORY-020](../theory.d/THEORY-020.md): consistent.** The Boolean base category (§5.5.3) and the dual-presheaf restatement of Kochen–Specker (p. 70) are the facts [THEORY-020](../theory.d/THEORY-020.md) draws from [LIT-325](../literature.d/LIT-325.md), reprinted here unchanged.
- **No new THEORY is indicated.** The candidate account, "quantity values are monotone intervals over contexts", is already in [NOTE-290](NOTE-290.md) for paper III.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Mostly reprinted.** Most of the text is papers I–IV, as the authors say (p. 14).
- **Proofs.** Several are sketched or omitted:
  - Thm 16.1 (⇒ in Sub_cl(Σ));
  - naturality and monicity of ι : O → P_clΣ (p. 88, "we will spare the reader the ordeal");
  - Thm 10.1;
  - the "no B̂" claim for composites (p. 172).
- **Probabilities.** Truth objects keep only probability-one information, and a density matrix is not recoverable from its truth object. So the formalism as given does not reproduce Born probabilities. The conclusion's claim that probability "has gone completely" (p. 183) is a description of this loss, not a reconstruction. The authors defer measures on Σ to Heunen–Spitters (p. 81).
- **No choice of quantity-value object.** ℝ^⪰, ℝ^↔, k(ℝ^⪰) and k(ℝ^↔) are all kept. The conclusion prefers ℝ^↔ "from a physical perspective", but §13 reverts to ℝ^⪰ for notational convenience.
- **Composites fail.** Quantum composites do not satisfy the authors' own commutativity rule (12.20). The scheme is "almost" satisfied (p. 182).
- **No theory beyond quantum theory is constructed.** That is the stated goal (§15), and the authors concede that none is given.

## Open questions

- Write out ⇒ on Sub_cl(Σ) and check the Heyting laws. This is the open item [THEORY-037](../theory.d/THEORY-037.md) waits on.
- Does the class [δ̆(A)] in ℝ^↔/≡ determine Â (p. 125)?
- Are there pseudo-states not of the form w^ψ, and is there a pseudo-state object W_φ (§6.4.3, §14.3)? In infinite dimension, de Groote's non-atomic quasi-points give candidates whose physical meaning the authors leave open.
- Is there a cohomological (Postnikov-type) description of the obstruction to lifting w^ψ (§6.6)?
- Can the Sys rules be changed, or the context category enlarged, so that tensor-product composites satisfy (12.20)?
- Is there a "gros topos" holding all quantum systems at once, i.e. is M(Sys) a site (§15)?

## Corrections

- none to a seeded skim (there was no seed)
- **The dimension condition is stated only in places.** "Σ has no global elements" appears with dim H > 2 on pp. 50, 53 and 70, and without it on p. 13 (fn. 14), p. 16, p. 62 and p. 73. Paper II and paper III dropped it throughout ([NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md)), so this is a partial repair.
- **Thm 16.1 is not a Heyting subalgebra statement.** Negation in Sub_cl(Σ) is redefined with an interior (16.10), so it differs from negation in Sub(Σ). Sub_cl(Σ) is therefore not a Heyting subalgebra of Sub(Σ), and "Heyting" here rests on an implication that is never written down.
- **Notation slips in §13.**
  - Lemma 13.1's proof computes the inner daseinisation of P̂ (13.10) and writes the result as δ, outer (13.11). The conclusion holds because outer daseinisation of Â is inner daseinisation of its spectral projectors.
  - (13.29) says the geometric morphism is "induced by π"; the functor defined just above is n.
  - Footnote 114 re-uses δ̆(Â) in §13 for δ̆^o(Â), where §8 used it for the pair (δ̆^i, δ̆^o).
