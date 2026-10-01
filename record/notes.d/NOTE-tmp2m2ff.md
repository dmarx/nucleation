---
status: Read
paper: LIT-tmp6dqzs
title: 'A Topos Perspective on the Kochen-Specker Theorem: III. Von Neumann Algebras as the Base Category'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of arXiv quant-ph/9911020 v1 (5 Nov 1999, the
    only arXiv version), from the arXiv PDF, 28 PDF pp. (title page plus
    printed pp. 1–27). The title page is dated "31 October, 1999". I read
    the abstract, §1, §2 (§2.1 the categories O, W, V and the functors O →
    W, O → V, W → V; §2.2 the spectral presheaf Σ over V and the state
    presheaf S), §3 (§3.1 the coarse-graining presheaf G over V, "augmented
    propositions", the clopen presheaf CloΣ; §3.2 sieve-valued generalised
    valuations on V; §3.3 valuations from states, including the
    probability-r family), §4 (§4.1 interval valuations; §4.2 subobjects of
    Σ, Examples 1–2; §4.3 global elements of G; §4.4 subobjects of G, the
    probability-1 and probability-r cases, "semantic subobjects"; §4.5
    interval valuations from ideals and the ψ-annihilator example), §5
    (conclusions) and all 7 references. Nothing was skipped. The text was
    extracted with PyMuPDF. I checked the FUNC verification (3.18–3.20), the
    subobject arguments of Examples 1–2 (4.5, 4.9), the global-element claim
    for the state case (§4.3, which I re-derived both ways) and the ideal
    example (4.22–4.24). The IJTP version of record was not read.
    Bibliographic data were checked against the arXiv abstract page and
    Crossref. There is no Anthology of the SOTA entry for this paper
    (searched the anthology's literature.d for the arXiv id and title). This
    is part III of the series whose part I is LIT-325, read as one series
    with Butterfield & Isham (1999, part II) and Butterfield & Isham (2002,
    part IV).). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-10-01'
summary: >-
  Hamilton, Isham & Butterfield move the series' base category from
  operators (O) and Boolean subalgebras (W) to the poset V of commutative
  von Neumann subalgebras of B(H). There they restate Kochen–Specker as
  "the spectral presheaf Σ(V) = Gelfand spectrum of V has no global
  elements" (dim H > 2, cited, §2.2). They identify the coarse-graining
  presheaf G(V) = L(V), G(i)(P̂) = inf{Q̂ ∈ L(V₂) | P̂ ≤ Q̂} (Def. 3.1),
  with the presheaf CloΣ of clopen subsets of the spectra; the isomorphism
  is asserted, and part IV proves it. A state ρ yields the sieve-valued
  valuation ν^ρ_V(P̂) = {V′ ⊆ V | ρ(G(P̂)) = 1} (Def. 3.4) and the support
  projectors inf{P̂ ∈ L(V) | ρ(P̂) = 1}. These form a global element of G
  and hence an "interval valuation", a subobject of Σ (§§4.2–4.4). The
  probability-r valuations give subobjects of G but not global elements.
---

# NOTE-tmp2m2ff: A Topos Perspective on the Kochen-Specker Theorem: III. Von Neumann Algebras as the Base Category

## Contribution

The paper replaces the operator category O and the Boolean-subalgebra poset W of parts I–II with the poset V of commutative von Neumann subalgebras of B(H), ordered by inclusion. It argues that V is the better base: it identifies operators that generate the same algebra, contains all spectral projectors, and "subsumes both O and W" (§2.1).

On V it restates part I's machinery:

- the spectral presheaf, now Gelfand spectra;
- the coarse-graining presheaf, now projection lattices with the infimum coarse-graining;
- sieve-valued valuations and state-induced valuations.

It also notices that projectors in V are clopen subsets of σ(V), so that G is the "clopen power object" of Σ. Its new topic is "interval valuations", assignments of subsets of spectra. It relates these to sieve-valued valuations through the "truth set" of totally true projectors and its infimum, the state's support. Both the topic and the base category are developed further in part IV, and the base category in Döring–Isham.

## Key insight

In a commutative von Neumann algebra a projector is the same thing as a clopen subset of the Gelfand spectrum. So a proposition at a context is a "region" of that context's state space. Coarse-graining a projector to a smaller algebra (the least projector there above it) is the corresponding operation on regions.

The Kochen–Specker theorem forbids picking one point of each spectrum coherently. It does not forbid picking a region of each spectrum coherently. A quantum state does exactly that, through its support at each context, and the sieve-valued truth value of any proposition can be read off from those regions.

## Assumptions

- **V.** The objects are "the commutative von Neumann subalgebras of the algebra B(H)", with inclusions as the arrows (§2.1). The trivial algebra ℂ1̂ is not excluded. Döring–Isham later exclude it ([NOTE-292](NOTE-292.md)).
- **Functors.** V: O → V sends Â to V[A], the algebra it generates (Def. 2.1). VW: W → V sends W to W″ (Def. 2.2).
- **Spectral theory imported.** The Gelfand isomorphism V ≅ C(σ(V)) and the properties of σ(V) (compact Hausdorff, extremely disconnected, §4.5) are cited from Kadison–Ringrose [6]. Discontinuous Borel functions are handled by replacing f∘Ã with a continuous representative (fn. 5, "p. 324 in [6]").
- **KS cited, not reproved.** "No such valuations exist on all operators on a Hilbert space of dimension greater than two" (§2.2), citing Kochen & Specker [3].
- **States.** Normal states, i.e. density matrices, are what the support arguments use: they rely on "the map Â → tr(ρÂ) is weakly continuous". Strictly, tr(ρ ·) is ultraweakly continuous, which agrees with weak continuity on bounded sets, so the argument stands.
- **Interpretation of propositions (§3.1).** A projector P̂ ∈ L(V) is read as a proposition about the whole stage V. This "augmented proposition" (Def. 3.2) is the class of all "A ∈ Δ" with Â ∈ V and Ê[A ∈ Δ] = P̂. The authors reject reading it as a proposition about one operator, because coarse-graining to V₂ ∌ Â leaves no operator for it to be about (three cases, §3.1).

## Key results

- **KS on V (§2.2).** Restricted to self-adjoint elements, a character κ of V satisfies the value rule and FUNC, κ(B̂) = f(κ(Â)) (2.3). So a global element of Σ over V would be a KS valuation. Hence, citing KS, Σ over V "has no global elements" for dim H > 2.
  - The same construction works for the commutative subalgebras of any von Neumann algebra N (§2.2, end).
- **State presheaf (Def. 2.4).** S(V) is the state space of V, with restriction as the arrow map. Restrictions of a state on B(H) give global elements, but "there may be other global elements of S which are not obtainable in this way". This is not pursued. KS forbids a global element of S that is pure at every stage.
- **Coarse-graining presheaf on V (Def. 3.1).** G(V) = L(V), and G(i_{V₂V₁})(P̂) = inf{Q̂ ∈ L(V₂) | P̂ ≤ Q̂} (3.3). This is the W-version of part I §5.3, transferred.
- **Clopen power object (§3.1, end).** P̂ ↔ {κ ∈ σ(V) | κ(P̂) = 1} is a bijection between L(V) and the clopen subsets of σ(V), argued from the Gelfand transform of a projector being a continuous {0,1}-valued function. CloΣ's arrow map is *defined* through G (3.6). "There is an isomorphism between G and CloΣ" is then asserted.
  - The substantive fact behind it, that the restriction image of {κ | κ(P̂) = 1} is {λ | λ(G(P̂)) = 1}, is neither stated nor proved here. Part IV §2.4 proves it.
- **Sieve-valued generalised valuation on V (Def. 3.3).** A family ν_V: L(V) → Ω(V) satisfying:
  - (i) FUNC, ν_{V′}(G(i)(P̂)) = i*(ν_V(P̂)) (3.9);
  - (ii) null;
  - (iii) monotonicity;
  - optionally (iv) exclusivity and (v) unit.
  - By FUNC each such ν is a natural transformation G → Ω, hence a subobject of G (3.14).
- **From states (Def. 3.4).** ν^ρ_{V₁}(P̂) = {V₂ ⊆ V₁ | ρ[G(i_{V₂V₁})(P̂)] = 1} (3.17).
  - *FUNC.* Verified in (3.18)–(3.20) from functoriality of G; the check is correct. The other clauses are "the same, mutatis mutandis" as part I.
  - *Probability-r family.* ν^{ρ,r} with "≥ r" (3.21). Exclusivity holds for ½ ≤ r ≤ 1 and is dropped for r < ½ (as in part I, where this was asserted).
- **Interval valuations (§4).** These are assignments of subsets of σ(V), which induce subsets Δ_A = Ã[I(V)] of each operator's spectrum, with Δ_B = f(Δ_A). "Interval" means any subset, not necessarily connected (§4.1). Three versions are given.
  - *(a) Subobjects of Σ (§4.2).* These obey only I(V₁)|V₂ ⊆ I(V₂) (4.2). "One can think of the Kochen-Specker theorem as restricting the 'smallness' of the subobjects."
    - *Example 1 (4.3–4.5).* The "true subobject" I^ρ(V) = {κ | κ(Q̂) = 1}, where Q̂ = inf T^ρ(V) and T^ρ(V) = {P̂ ∈ V | tr(ρP̂) = 1}. It is shown that Q̂ ∈ T^ρ(V) (the support of ρ in V) and that I^ρ is a subobject. The argument is correct.
    - *Example 2 (4.6–4.9).* For a general sieve-valued ν, I^ν is a subobject iff the infima match, Q̂₁ ≥ Q̂ for V₁ ⊂ V. A sufficient condition is T^ν(V₁) ⊆ T^ν(V); it holds for ν^ρ and ν^{ρ,r}.
  - *(b) Global elements of G (§4.3).* These satisfy γ(V₂) = G(i)(γ(V₁)) (4.10).
    - *They are subobjects of Σ.* Every global element of G defines a subobject of Σ (4.11).
    - *The state supports are one.* The supports γ^ρ(V) = inf T^ρ(V) form a global element (4.12–4.14). The paper's argument is brief. I re-derived it: Q̂₂ ≤ G(Q̂₁), because G(Q̂₁) has probability 1; and G(Q̂₁) ≤ Q̂₂, because Q̂₂ ∈ T^ρ(V₁) and Q̂₂ ∈ L(V₂). The conclusion is correct.
    - *The probability-r case.* The ν^{ρ,r} supports are said not to form a global element. This is asserted without a counterexample.
  - *(c) Subobjects of G (§4.4).*
    - *Probability 1.* T_ρ(V) = {P̂ | tr(ρP̂) = 1} is a subobject of G, with equality T_ρ(V₂) = G(i)(T_ρ(V₁)) (4.16–4.19). The proof is correct.
    - *Probability r.* T_{ρ,r} is a subobject of G (4.21), because coarse-graining raises probability (4.17).
    - *Semantic subobjects.* Subobjects of G that are upward closed, omit 0̂ and are exclusive are proposed as a general class of generalised valuations. That is a definition (§4.4.3).
- **Interval valuations from ideals (§4.5).**
  - *Closed ideals.* Closed ideals of V correspond to closed subsets of σ(V). In an extremely disconnected space each closed set differs from a unique clopen set by a meagre set, so "any assignment of a closed ideal to each algebra" gives a clopen-valued interval valuation.
  - *Ideals of N.* An ideal of a non-commutative N restricts to each V. The lattice of closed two-sided ideals is a quantale, offered as an analogue of a spectrum for N, citing Mulvey–Pelletier.
  - *Example.* The left ideal ι_ψ = {Â | Âψ = 0} (4.22) gives, in each V, the projector 1̂ − sup P(ι_ψ(V)). This is the smallest projector in V containing ψ, so the ideal construction reproduces Example 1 for the vector state ψ (4.24). The argument is correct.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | KS ⇔ the Gelfand-spectrum presheaf Σ over V has no global elements (dim H > 2) | definitional equivalence plus cited KS | §2.2, (2.3) |
| C2 | V is a better base category than O or W: it subsumes both and avoids the problem of isomorphic operators | informal argument | §2.1; functors Defs. 2.1–2.2 |
| C3 | L(V) ≅ clopen subsets of σ(V), and G ≅ CloΣ as presheaves | the stage-wise bijection is argued; the presheaf isomorphism is asserted, CloΣ's maps being defined via G | §3.1, (3.6); proved in part IV §2.4 |
| C4 | Each state ρ gives a sieve-valued generalised valuation on V obeying FUNC; ν^{ρ,r} does too, with exclusivity iff r ≥ ½ | proof for FUNC; the other clauses "mutatis mutandis" | Def. 3.4, (3.18)–(3.20), (3.21) |
| C5 | The supports of ρ, inf{P̂ ∈ L(V) : ρ(P̂) = 1}, form a global element of G and hence a subobject of Σ (an interval valuation) | proof (brief; re-derived and correct) | §4.2 Ex. 1, §4.3 |
| C6 | A sieve-valued ν yields a subobject of Σ iff its truth-set infima match (Q̂₁ ≥ Q̂ for V₁ ⊂ V) | proof | (4.8)–(4.9) |
| C7 | The probability-r valuations give subobjects of G but not global elements of G | the subobject half is proved (4.17); the "not" half is asserted with no counterexample | §4.3 end, §4.4.2 |
| C8 | Every sieve-valued valuation corresponds to a subobject T_ν of G that is an upper set, omits 0̂ and is exclusive ("semantic subobject") | proof (direct) | §4.4.3 |
| C9 | Closed ideals, e.g. those restricted from ideals of a non-commutative N, give interval valuations; the ψ-annihilator reproduces the true subobject | general claim is a sketch (see Limitations); example is a proof | §4.5, (4.22)–(4.24) |

## Method

Operator-algebraic restatement of parts I–II. Commutative von Neumann algebras serve as contexts, with Gelfand duality (V ≅ C(σ(V))) to pass between projectors and clopen subsets of spectra. The paper then makes a case-by-case comparison of three topos-theoretic readings of "interval valuation": subobjects of Σ, global elements of G, and subobjects of G. Each is tested on the state-induced valuations. There are no worked finite-dimensional examples.

## Concepts

- **V** — the poset of commutative von Neumann subalgebras of B(H), ordered by inclusion.
- **Spectral presheaf Σ over V** — the Gelfand spectrum σ(V), with restriction of characters (Def. 2.3). This is the object the later literature calls "the spectral presheaf".
- **State presheaf S** — the state spaces of the V, with restriction (Def. 2.4).
- **Coarse-graining presheaf G over V** — L(V), with P̂ ↦ the least projector of L(V₂) above P̂ (Def. 3.1). This is Döring–Isham's outer daseinisation, under part I's name.
- **Augmented proposition** — all "A ∈ Δ" with Â ∈ V sharing one projector (Def. 3.2).
- **CloΣ** — the presheaf of clopen subsets of σ(V), the "clopen power object" of Σ.
- **Truth set T^ν(V)** — the projectors with ν_V(P̂) = true_V. Its infimum is the **support**; for a state this is the usual support projection of ρ restricted to V.
- **Interval valuation** — an assignment to each V of a subset of σ(V) (equivalently, of subsets of each operator's spectrum). "Interval" means any subset.
- **Semantic subobject** — a subobject of G with the upper-set, no-0̂ and exclusivity properties (§4.4.3).

## Connections

- **Part I ([LIT-325](../literature.d/LIT-325.md), [NOTE-271](NOTE-271.md)).** Part I's fn. 6 named the abelian-subalgebra category, and its §2.2 postponed continuous spectra to "a more sophisticated approach that involves the spectral theorem for commutative von Neumann algebras". This is that approach. Part I's coarse-graining on W (inf of projectors above, Def. 5.4) becomes Def. 3.1 here, and part I's remark that G on O is "essentially" the Borel power object of Σ becomes "G ≅ CloΣ".
- **Part II (Butterfield & Isham 1999).** Cited for the general motivations and classical analogues. §5 says these carry over to V but does not show it.
- **Part IV (Butterfield & Isham 2002).** Part IV §2 restates this paper's Defs. 2.3, 3.1, 3.3 and 3.4 almost word for word (as its Defs. 2.1–2.4). It *proves* G ≅ CloΣ via a state-extension theorem (Kadison–Ringrose Thm 4.3.13). It recaps §4 here as the three senses (i)–(iii) of "interval valuation", and turns the truth-set/support correspondence into Theorems 3.1–3.2. Read together, part IV is where this paper's §§3–4 are finished.
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md); [NOTE-277](NOTE-277.md), [NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md), [NOTE-285](NOTE-285.md)).**
  - *Base category.* [NOTE-292](NOTE-292.md) records that [LIT-335](../literature.d/LIT-335.md)'s base V(H) follows "Hamilton–Butterfield–Isham 2000", i.e. this paper. Confirmed: Σ over V, Gelfand spectra and restriction maps are all here.
  - *What Döring–Isham add.* Exclusion of ℂ1̂; de Groote's name "daseinisation" for Def. 3.1's coarse-graining; and propositions as clopen *sub-objects* of Σ, rather than global elements of CloΣ, collected into the Heyting algebra Sub_cl(Σ).
  - *What they share with this paper.* Truth values as sieves of subcontexts at which a state makes the coarse-grained projector certain; this is Def. 3.4 here, which [LIT-335](../literature.d/LIT-335.md) reuses for T^ψ.
- **Clifton; Halvorson & Clifton (refs [4]–[5]).** These are the modal-interpretation "beable subalgebra" work. They are named in fn. 4 as related; the paper does not engage with them.
- **Mulvey & Pelletier (ref [7]), quantales.** Mentioned only as an analogy (§4.5). Not in the record.
- **Anthology of the SOTA.** No entry; nothing for ML practice.

## Bearing on the record

- **[THEORY-037](../theory.d/THEORY-037.md) (Proposed: Sub_cl(Σ) is Heyting, negation a pseudo-complement).**
  - *What it supplies.* This is the first place in the series where projectors become clopen subsets of the Gelfand spectra over V, and where coarse-graining becomes an operation on them (G ≅ CloΣ). It is the stage-wise half of [LIT-335](../literature.d/LIT-335.md)'s "daseinisation sends P̂ to a clopen sub-object" and should be cited as its origin.
  - *What it does not supply.* No lattice operations, implication or negation on clopen sub-objects. It does not meet [THEORY-037](../theory.d/THEORY-037.md)'s promote_when, and does not touch the orthocomplement-versus-pseudo-complement point.
  - *A distinction [THEORY-037](../theory.d/THEORY-037.md) relies on.* This paper (and more sharply part IV) separates subobjects of Σ, whose components need only satisfy I(V₁)|V₂ ⊆ I(V₂), from global elements of CloΣ, which match exactly. Daseinised projectors are of the second, "tight" kind. That is consistent with [THEORY-037](../theory.d/THEORY-037.md)'s warning that clopen sub-objects are not all sub-objects.
- **[THEORY-020](../theory.d/THEORY-020.md) (Stone; the KS obstruction lies in how contexts overlap).** Supportive, in operator form.
  - *Each context taken alone.* Each V has its full spectrum of characters, and so all two-valued valuations of its projectors. The paper's L(V) ↔ clopen-subsets-of-σ(V) correspondence is the Stone representation of the complete Boolean algebra L(V), reached through Gelfand duality, though the paper names neither Stone nor ultrafilters.
  - *Where KS sits.* KS fails only in the matching under restriction between overlapping V (§2.2). This is the von Neumann-algebra form of the "join" [THEORY-020](../theory.d/THEORY-020.md) draws, alongside [LIT-313](../literature.d/LIT-313.md) and [LIT-299](../literature.d/LIT-299.md) ([NOTE-290](NOTE-290.md), which states the ultrafilter identification explicitly).
- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected).** Consistent with its refutation. The paper's truth values are sieves on V (lower sets of a poset with non-invertible arrows), whichever presheaf has or lacks global sections. The paper does not address Booleanness directly.
- **The owner's map (as recorded in [NOTE-271](NOTE-271.md) and [NOTE-290](NOTE-290.md)).** For the "no global ultrafilter → presheaf over contexts → KS" step, the canonical citation remains part I §2.3 (dual presheaf on W). This paper is the first in-series statement of the commutative-von-Neumann-subalgebra / Gelfand-spectrum form, which [NOTE-271](NOTE-271.md) said should not be attributed to part I.
- **ML practice.** It carries nothing for ML practice.
- **For filing.** `quantum-foundations`, `mathematics` (operator algebras, presheaves), `contextuality`, `logic` (sieve-valued truth).

## Limitations

- **G ≅ CloΣ is asserted.** Because CloΣ's arrow map is defined through G (3.6), the stated isomorphism is nearly tautological here. The non-trivial fact (restriction images of clopens are the clopens of coarse-grained projectors) is not addressed until part IV.
- **Probability-r negatives asserted.** That ν^{ρ,r} supports do not form a global element of G, and that they have "no non-trivial infimum" in many V, is asserted without example (§4.2, §4.3).
- **A slip in (4.8) for general ν, affecting only the probability-r remark.** The paper rewrites I^ν(V) = ⋂_{P̂ ∈ T^ν(V)} {κ | κ(P̂) = 1} as the clopen set {κ | κ(Q̂) = 1} with Q̂ = inf T^ν(V). That is right when Q̂ ∈ T^ν(V), as for states, but not in general. Characters of an infinite-dimensional V need not be normal, so the intersection can be strictly larger than the clopen set. Part IV keeps the intersection as the definition (its eq. 2.27) and flags the closure issue (§3.2.2).
- **§4.5 overstates.** Two points.
  - *Norm-closed ideals.* For a norm-closed ideal that is not weakly closed (e.g. the functions vanishing at one non-isolated point), "the functions in the ideal are then precisely those … orthogonal to the projector" is false. The meagre-set modification changes the ideal. The claim holds for weakly closed ideals, which is what the worked example uses.
  - *Left versus two-sided.* The example's ι_ψ is a left ideal, while the quantale remark concerns two-sided ideals.
  - *Not shown.* That ideal-induced assignments are subobjects of Σ is shown only for the example.
- **No new theorem about KS.** As in part I, KS is cited, and the move to V is a reformulation.
- **The state presheaf question (non-restriction global elements of S) is raised and dropped.**
- **Typographical.** "κ|V₁ ∉ I^ρ(V₁)" in Example 2 should read I^ν. A stray "y(iv)" appears before the exclusivity clause.

## Open questions

- Are there global elements of the state presheaf S not obtained by restricting a state on B(H)? (§2.2; not answered here.)
- Which subobjects of G are "semantic", and do they exhaust the generalised valuations of interest (a topos analogue of Gleason, as asked in part I §6)?
- Is there a natural class of interval valuations coming from ideals of non-commutative algebras (the quantale suggestion), and do they give subobjects of Σ in general?

## Corrections to the seeded skim

- none (there was no seed or dossier)
- Author order. The title page, the arXiv metadata and Crossref all give **Hamilton, Isham, Butterfield**. Part IV's reference [4] and [NOTE-292](NOTE-292.md) give "Hamilton, Butterfield and Isham" / "Hamilton–Butterfield–Isham", which is not the paper's order.
- Content versus [NOTE-271](NOTE-271.md)'s expectation. [NOTE-271](NOTE-271.md) says the commutative-subalgebra spectral presheaf is "Part III … and Döring–Isham, not this paper [part I]". Confirmed: Def. 2.3 here is the Gelfand-spectrum presheaf over V. In addition, this paper (not only Döring–Isham) already identifies the coarse-graining of projectors with clopen subsets of the spectra (CloΣ, §3.1). That is the outer daseinisation / clopen-sub-object picture of [LIT-335](../literature.d/LIT-335.md), without the name.
- Internal. The abstract places the interval material in "Section 3"; the body has it in §4.
