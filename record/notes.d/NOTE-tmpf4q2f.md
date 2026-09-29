---
status: Read
paper: LIT-299
title: 'A topos foundation for theories of physics: III. The representation of physical quantities with arrows δ̆°(A): Σ̲ → ℝ̲≽'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv quant-ph/0703064 v1 (7 Mar 2007, the
    only arXiv version), from the arXiv PDF, 38 pp. I read the abstract,
    §§1–6 (daseinisation of self-adjoint operators; the de Groote
    presheaves; the presheaves sp(Â)^⪰, ℝ^⪰, ℝ^⪯, ℝ^↔; observable and
    antonymous functions on filters; the physical interpretation of δ̆(A);
    the Grothendieck completion k(ℝ^⪰); unitary operators), the Appendix
    (injectivity of Â ↦ δ̆^o(A)) and all 18 references. Nothing was skipped.
    I checked the bounded-variation argument (§4.2), the squaring
    construction (§4.3) and the naturality claims that have one-line proofs.
    The results cited from de Groote and Döring (observable and antonymous
    functions, bijection with self-adjoint operators) were taken as stated,
    not checked. Papers I, II and IV of the series were read in full
    alongside. `pdftotext` was not available, so I extracted the text with
    PyMuPDF. The published J. Math. Phys. text (paywalled) was not seen.).
    The first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  Each bounded self-adjoint Â becomes an arrow δ̆^o(A) : Σ → ℝ^⪰, where
  ℝ^⪰ is the presheaf of real-valued order-reversing functions on ↓V. At λ
  ∈ Σ_V it sends V′ ⊆ V to λ(δ^o(Â)_{V′}), and δ^o(Â)_V is the
  spectral-order-least operator in V above Â. The map Â ↦ δ̆^o(A) is
  injective, but ℝ^⪰ is only an additive monoid, not the real-number
  object. Its Grothendieck completion k(ℝ^⪰) is an abelian-group object
  whose global elements are exactly the functions of bounded variation on
  V(H).
---

# NOTE-tmpf4q2f: A topos foundation for theories of physics: III. The representation of physical quantities with arrows δ̆°(A): Σ̲ → ℝ̲≽

## Contribution

The paper completes the quantum representation of the local language L(S) of paper I ([LIT-343](../literature.d/LIT-343.md)). It identifies a quantity-value object R_φ in Sets^{V(H)^op}, and it represents every bounded self-adjoint operator Â, which is every function symbol A : Σ → R, by an arrow Σ → R_φ. The real-number object, the constant presheaf ℝ, cannot serve: the Gel'fand transforms of the daseinised operators grow as V shrinks (3.3)–(3.4). The quantity-value object is therefore a presheaf of monotone real functions on ↓V, ℝ^⪰, adapted from M. Jackson's thesis.

The paper also:
- adds a symmetric variant ℝ^↔;
- group-completes ℝ^⪰ so that differences and some squares exist;
- shows how unitaries act on the topos.

## Key insight

A context V cannot hold Â, so it holds the best approximation of Â from above in the spectral order, δ^o(Â)_V. It can also hold the best approximation from below, δ^i(Â)_V. Going to smaller contexts V′ ⊆ V coarsens the approximation: δ^o(Â)_{V′} ⪰ δ^o(Â)_V. So a point λ ∈ Σ_V gives not a number but a monotone function V′ ↦ λ(δ^o(Â)_{V′}) on the subcontexts.

The value of a physical quantity in the topos is therefore a "spread" that widens as the context shrinks: [λ(δ^i(Â)_{V′}), λ(δ^o(Â)_{V′})] (3.51)–(3.52). The spread is state-independent, as classical functions on phase space are.

The same bookkeeping makes the context's local Boolean structure explicit. A point λ of Σ_V is exactly an ultrafilter F_λ = {P̂ ∈ P(V) | λ(P̂) = 1} of the Boolean lattice P(V) (3.28). The lack of global points is the lack of a coherent choice of such ultrafilters.

## Assumptions

- **Operators and contexts.** Operators are bounded; unbounded operators are not treated. Contexts are abelian von Neumann subalgebras, as in [LIT-335](../literature.d/LIT-335.md).
- **Spectral order.** Â ⪯_s B̂ iff Ê^B_λ ⪯ Ê^A_λ for all λ (Olson 1971). It makes B(H)_sa a boundedly complete lattice. It agrees with the usual order on projections and on commuting operators, and is coarser in general (§2.3.1).
- **Results cited from others.**
  - De Groote's results: spectral families survive daseinisation (2.13)–(2.14); the observable function f_A on filters and its bijection with B(H)_sa, determined by principal filters; f_{δ^o(Â)_V}(D) = f_A(C(D)) (3.31).
  - Döring's antonymous function g_A and its analogue (3.36), which is cited to "a forthcoming paper".
  - Jackson's presheaf of order-preserving functions.
- **The language.** L(S) is assumed to contain function symbols in bijection with a set of self-adjoint operators (Appendix).

## Key results

- **Daseinisation of self-adjoint operators (Def 2.4).**
  - *Definitions.* δ^o(Â)_V = ∫ λ d(δ^i(Ê^A_λ)_V) and δ^i(Â)_V = ∫ λ d(⋀_{μ>λ} δ^o(Ê^A_μ)_V). The outer one is built from inner daseinisation of the spectral family, because the spectral order is reversed.
  - *Properties.* δ^o(Â)_V = ⋀{B̂ ∈ V_sa | B̂ ⪰_s Â} (2.21). δ^i(Â)_V ⪯_s δ^o(Â)_V (2.18). Both equal Â if Â ∈ V. sp(δ^o(Â)_V) ⊆ sp(Â) (2.23): "daseinisation … 'collapses' eigenvalues".
  - *Nonlinearity.* Both maps are non-linear (item 5) and are not Borel functions of Â (item 3).
  - *Scaling.* They are positively homogeneous, and they swap under Â ↦ −Â (item 6).
  - *Spectral families.* Ê[δ^o(Â)_V > λ] = δ^o(Ê[A > λ])_V (2.28).
- **De Groote presheaves (Defs 2.5–2.6).** The outer one assigns V_sa to V, with δ^o as restriction, and V ↦ δ^o(Â)_V is a global element. De Groote has an example of a global element not of this form (cited).
- **Thm 3.1.** For each Â, the maps δ̆^o(A)_V : Σ_V → sp(Â)^⪰_V, with λ ↦ (V′ ↦ λ(δ^o(Â)_{V′})), form a natural transformation Σ → sp(Â)^⪰ ⊆ ℝ^⪰. The proof is the one-line restriction check (3.15), which is correct.
  - ℝ^⪰_V is the set of order-reversing μ : ↓V → ℝ, with restriction of functions as the maps (Def 3.2).
- **Thm 3.2.** δ̆(A) = (δ̆^i(A), δ̆^o(A)) : Σ → ℝ^↔ is natural. ℝ^↔_V is the set of pairs (order-preserving, order-reversing) (Def 3.3). The paper gives no proof ("easy to see"); it is the same one-line check.
- **Faithfulness (Appendix).** θ : Â ↦ δ̆^o(A) is injective. Evaluate at V_P̂ = {P̂,1̂}″ on the character with λ(P̂) = 1: this recovers f_A on every principal filter. De Groote's theorem then fixes Â.
  - The same holds for δ̆^i and δ̆ into ℝ^↔ (fn. 26). It is open whether the class [δ̆(A)] in ℝ^↔/≡ fixes Â.
  - *Minor gap.* The case P̂ ∈ {0̂, 1̂} is again not a context (cf. [LIT-335](../literature.d/LIT-335.md)), and the argument implicitly skips it.
- **Ultrafilters (§3.3, (3.28)).** λ ∈ Σ_V ↔ the ultrafilter F_λ of P(V). This is a bijection Q(V) ≅ Σ_V. For a vector state, F^ψ = {P̂ ⪰ P̂_ψ} is a maximal filter in P(H) but not an ultrafilter, because P(H) is not distributive (fn. 13).
- **Interpretation (§3.4).** ⟨ψ|Â|ψ⟩ = ∫_{g_A(F^ψ)}^{f_A(F^ψ)} λ d⟨ψ|Ê^A_λ|ψ⟩ (3.41). At a stage V containing the character λ^ψ, this range is [⟨ψ|δ^i(Â)_V|ψ⟩, ⟨ψ|δ^o(Â)_V|ψ⟩] (3.46). "No similar global construction or interpretation is possible, since the spectral presheaf Σ has no global elements".
- **Algebra of ℝ^⪰ (§3.5).** It is an additive commutative monoid object. Differences and products of order-reversing functions need not be order-reversing (3.56). δ^o(Â) + δ^o(B̂) ≠ δ^o(Â + B̂) in general (fn. 19). Propositions in L(S) are pull-backs δ̆^o(A)⁻¹(Ξ) for sub-objects Ξ ⊆ ℝ^⪰ (§3.6), and their meaning is "relational", needing a coherence rather than correspondence theory of truth. That last point is only asserted.
- **k(ℝ^⪰) (§4).**
  - *Group completion.* Γℝ^⪰, the order-reversing functions on Ob(V(H)), is a commutative monoid with group completion k(Γℝ^⪰). The map [λ,κ] ↦ λ − κ is injective.
  - *Bounded variation.* Its image is exactly the functions of bounded variation BV(Ob(V(H)), ℝ) (4.10)–(4.13). The variation I_f(V) is a sup over finite chains ending at V. I checked that f − I_f is order-reversing: for V₂ ⊆ V₁, I_f(V₁) ≥ I_f(V₂) + |f(V₁) − f(V₂)|. The converse is "a straightforward modification" of the real-line proof and is not given.
  - *Squares.* Squares exist for classes [λ,0], via [λ,0]² := [λ₊², −λ₋²] (4.19). Squares of general elements do not (fn. 23).
  - *Presheaf level.* The presheaf k(ℝ^⪰) is an abelian-group object with Γk(ℝ^⪰) ≅ k(Γℝ^⪰) ("easy to see"). ℝ^↔/≡ ≅ k(ℝ^⪰) via [μ,ν] ↦ [ν, −μ] (4.25).
  - *Dispersion.* The "intrinsic dispersion" ∇(Â) := δ̆^o(A²) − δ̆^o(A)² becomes definable (4.2). Nothing is proved about it, not even a sign.
- **Unitaries (§5).**
  - *Daseinisation.* δ^o(Û) and δ^i(Û) are defined by spectral integrals. δ^o(e^{iÂ})_V = e^{iδ^o(Â)_V} (5.8). Daseinised group representations are not representations, since everything commutes in V (5.9).
  - *Action on contexts.* ℓ_Û(V) = ÛVÛ⁻¹ is a poset automorphism of V(H) with ℓ_{Û₁}ℓ_{Û₂} = ℓ_{Û₁Û₂}. Û δ^o(P̂)_V Û⁻¹ = δ^o(ÛP̂Û⁻¹)_{ℓ_Û(V)} (5.16).
  - *Covariance.* Truth values transform covariantly (5.26). The pull-back ℓ*_Û is an anti-representation of U(H) (5.29). There are natural isomorphisms Σ ≅ Σ^Û and ℝ^⪰ ≅ (ℝ^⪰)^Û, and a commuting square for δ̆ (Thms 5.1–5.3). The proof of Thm 5.1 is "not included here"; the other two are routine.
- **Outlook (§6).** Build theories in Sets^{C^op} for a general category of contexts C that owes nothing to ℝ or ℂ, "contextual, multi-valued logic in an intrinsic way". Or use the topos of M-sets for a monoid M. This is suggested without an example.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every bounded self-adjoint Â gives a natural transformation δ̆^o(A) : Σ → ℝ^⪰ (and δ̆^i into ℝ^⪯, δ̆ into ℝ^↔) | proof (short, correct) | Thm 3.1, (3.15); Thm 3.2 asserted by the same check |
| C2 | Â ↦ δ̆^o(A) is injective, so L(S) is faithfully represented | proof relying on cited results (de Groote's bijection f_A ↔ Â; (3.31)) | Appendix (6.3)–(6.9) |
| C3 | The quantity-value object is not the real-number object of Sets^{V(H)^op} | proof (elementary) | (3.3)–(3.4): arrows into the constant presheaf would need equality where there is strict growth |
| C4 | Points of Σ_V are exactly the ultrafilters of P(V); F^ψ in P(H) is a maximal filter but not an ultrafilter | proof (elementary) plus remark | (3.27)–(3.28), fn. 13 |
| C5 | δ̆(A) gives a state-independent "spread" [λ(δ^i(Â)_{V′}), λ(δ^o(Â)_{V′})] that widens as V′ shrinks | proof of monotonicity; the interpretation is a gloss | (3.47)–(3.52) |
| C6 | For non-eigenstates, g_A(F^ψ) < ⟨ψ|Â|ψ⟩ < f_A(F^ψ), with these read as the least and greatest possible measurement results | cited, not proved (Döring 2005); instrumentalist reading disowned in fn. 14 | (3.41)–(3.46) |
| C7 | ℝ^⪰ is only a commutative-monoid object; its global elements' group completion is BV(Ob(V(H)), ℝ) | proof (one direction written; converse "straightforward") | §3.5, §4.2 |
| C8 | k(ℝ^⪰) is an abelian-group object with Γk ≅ kΓ, and squares of [λ,0] exist | proof for squares (checked); group-object and Γk ≅ kΓ asserted | §4.3–§4.4 |
| C9 | The unitary group acts on the topos covariantly (Thms 5.1–5.3; (5.26)) | proof for (5.16) and (5.26); Thm 5.1 unproved | §5.2 |
| C10 | The meaning of L(S)-propositions is relational and needs a coherence theory of truth | assertion | §3.6 |

## Method

Spectral-order lattice theory, de Groote's observable functions on filters of P(H), Jackson's monotone-function presheaves, Grothendieck completion of monoids, and presheaf naturality checks. There are no examples or computations beyond one-line witnesses.

## Concepts

- **Spectral order ⪯_s.** Comparison of spectral families, reversed. It is coarser than the operator order and coincides with it on projections and on commuting pairs.
- **Outer and inner daseinisation of Â.** The spectral-order least upper and greatest lower approximations of Â within a context.
- **ℝ^⪰, ℝ^⪯, ℝ^↔.** Presheaves of order-reversing, order-preserving, and paired functions ↓V → ℝ. These are the candidate quantity-value objects.
- **k(ℝ^⪰).** The Grothendieck group completion. Its global elements are the bounded-variation functions on V(H).
- **Observable and antonymous functions f_A, g_A.** Functions on filters of P(H) that encode all outer and inner daseinisations of Â at once.
- **Quasipoint.** De Groote's name for a maximal filter. In an abelian P(V) these are ultrafilters, i.e. Gel'fand points.
- **ℓ_Û.** The action of a unitary on the context category, ℓ_Û(V) = ÛVÛ⁻¹. Its pull-back gives Û-twisted presheaves.

## Connections

- **Paper II ([LIT-335](../literature.d/LIT-335.md)).** It supplies daseinisation of projectors, which this paper applies to spectral families.
- **Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md)).** The ultrafilter reading (3.28) is the operator-algebraic form of their dual presheaf on Boolean subalgebras, D(W) = Hom(W,{0,1}). Their Kochen–Specker ⇔ no global section theorem is the fact behind "no global construction … is possible" (§3.4).
- **Abramsky–Brandenburger ([LIT-016](../literature.d/LIT-016.md)) and [THEORY-012](../theory.d/THEORY-012.md).** There is no probabilistic layer here, and so nothing about global distributions or signed measures. The values of δ̆(A) are state-independent ranges, and the state enters only in the instrumentalist gloss (3.41)–(3.46). [THEORY-012](../theory.d/THEORY-012.md) is neither supported nor contradicted. The two formalisms share only the "no global section of a presheaf over contexts" shape.
- **[LIT-277](../literature.d/LIT-277.md) and [LIT-278](../literature.d/LIT-278.md) (cohomology).** No relation. There is no obstruction theory. k(ℝ^⪰) is an abelian-group object, so in principle sheaf cohomology with coefficients in it could be defined, but nothing of the kind is attempted.
- **[THEORY-017](../theory.d/THEORY-017.md) (unitary invariance; a basis is extra data).** §5 is the programme's explicit statement of unitary covariance. Unitaries permute contexts (ℓ_Û), and the whole construction is carried along (Thm 5.3, (5.26)). No single context is privileged, which fits [THEORY-017](../theory.d/THEORY-017.md)'s claim that a basis or context is extra, non-intrinsic data.
- **Jackson 2006 (thesis), Olson 1971, de Groote 2004–05, Döring 2005.** These are the imported technical sources. None is in the record.

## Bearing on the record

- **The map's role (§0, row 8; §2 item 1, "concepts-are-ultrafilters/topes = §2.1").**
  - *Ultrafilters.* This is the paper in the series that says, in so many words, that the local "points" of a context are ultrafilters of its Boolean projection lattice (3.28). It also says that the global object has no points (§3.4, via [LIT-325](../literature.d/LIT-325.md)). So the map's claim that the ultrafilter half of §2.1 is owned by this programme holds. The canonical citation for the step is Isham–Butterfield 1998 ([LIT-325](../literature.d/LIT-325.md) §2.3), and this paper is the von Neumann-algebra restatement.
  - *Topes.* Nothing here concerns hyperplane arrangements, oriented matroids or topes. An ultrafilter of P(V) for commuting projectors is a joint 0/1 assignment consistent with the Boolean algebra they generate. A tope of an arrangement of possibly non-orthogonal hyperplanes is a sign vector of a region. Identifying the two is the owner's step and needs its own argument; the programme does not supply it.
- **"Concept = graded axis" (map row 2) versus "value = spread".** If a concept is modelled as a self-adjoint operator (a graded axis), this paper says what its "value" is in a context that does not contain it. The value is not a number but a monotone interval-valued function over subcontexts, widening as contexts coarsen (C5). That is a concrete prediction-shaped statement a Topos-of-Bricks instantiation would inherit. It has no counterpart in the linear-representation literature, and the map does not mention it.
- **Algebraic caution.** Quantity values form only a monoid (C7). Sums of daseinised operators are not daseinisations of sums (fn. 19). Differences and squares need k-completion, and even then general squares fail (fn. 23). Any construction that adds or subtracts "concept values" across contexts inherits these restrictions.
- **ML practice.** It carries nothing for ML practice.
- **For filing.** Tags as seeded. `quantum-foundations` first. `contextuality` fits because values are context-indexed and no global point exists. `mathematics` fits (operator lattices, presheaves). `logic` is kept for the L(S) representation. `anthology-candidate` is not proposed.

## Limitations

- **Unproved steps.** Several are left open: Thm 3.2, Thm 5.1, the group-object structure of k(ℝ^⪰), Γk ≅ kΓ, and the converse of the bounded-variation characterisation. The key analytic facts are imported from de Groote and Döring, one of them from a paper "in preparation".
- **Bounded operators only.** Position and momentum, the paper's running examples in paper I, are outside the construction as given.
- **No choice of quantity-value object.** ℝ^⪰, ℝ^⪯, ℝ^↔ and k(ℝ^⪰) are all offered, with no criterion for choosing among them. Faithfulness of the quotient ℝ^↔/≡ is open.
- **Definitions without results.** The dispersion ∇(Â) and the complex and unitary extensions are defined but never used.
- **Same unstated dimension condition as paper II** (dim H > 2 for "no global elements").

## Open questions

- Does [δ̆(A)] ∈ Hom(Σ, ℝ^↔/≡) determine Â (fn. 26, §4.4.2)?
- Is ∇(Â) = δ̆^o(A²) − δ̆^o(A)² non-negative in any useful sense, and does it relate to the quantum variance in a state?
- Is there a principled choice among the candidate quantity-value objects? Is there an internal characterisation, as for the real-number object?
- How should unbounded operators and ring structure (products of quantities) be handled?

## Corrections to the seeded skim

- Seeded from metadata. The seed's summary is accurate. Additions from the text: the paper also constructs ℝ^⪯ and ℝ^↔ (inner and outer daseinisation combined) and the group completion k(ℝ^⪰), and it treats unitary operators as functors ℓ_Û on V(H) with a covariance theorem (Thm 5.3).
- Title: the arXiv listing gives "III. The Representation of Physical Quantities With Arrows". The PDF title page adds "δ̆^o(A) : Σ → ℝ^⪰", which is the seed's title. The series' own reference lists use an older working title, "III. Quantum theory and the representation of physical quantities with arrows δ̆^o(A) : Σ → ℝ^⪰". The seed title can stay.
- Like paper II, this paper asserts that Σ "has no global elements, i.e., no points" (§3.4) with no dimension condition. It needs dim H > 2 (see [LIT-335](../literature.d/LIT-335.md), corrections).
- The "physical interpretation" (§3.4) is instrumentalist by the authors' own footnote 14 ("Which we avoid in general, of course!"). The inequality g_A(F^ψ) < ⟨ψ|Â|ψ⟩ < f_A(F^ψ) for non-eigenstates, with g and f read as the least and greatest possible measurement results, is cited from Döring's antonymous-functions paper, not proved here.
- Identifiers check against the arXiv listing: journal-ref J. Math. Phys. 49:053517 (2008); DOI 10.1063/1.2883777; "38 pages, no figures". arXiv v1 is 7 Mar 2007. `published: 2008-05-01` is the journal issue (flagged only).
