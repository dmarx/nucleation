---
number: 328
status: Read
formerly:
- NOTE-tmp2pyyh
paper: LIT-382
title: 'A Topos Perspective on the Kochen-Specker Theorem: IV. Interval Valuations'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of arXiv quant-ph/0107123 v1 (24 Jul 2001, the
    only arXiv version), from the arXiv PDF, 31 PDF pp. (title page plus
    printed pp. 1–30). The title page is dated "24 July 2001". I read the
    abstract, §1, §2 (the review: §2.1 O and V; §2.2 the spectral presheaf;
    §2.3 the coarse-graining presheaf and augmented propositions; §2.4 G as
    the clopen power object of Σ, with its proof; §2.5 sieve-valued
    valuations; §2.6 valuations from states; §2.7 interval valuations, truth
    sets and supports), §3 (§3.1 prospectus; §3.2.1 Theorem 3.1, global
    elements of G; §3.2.2 Theorem 3.2, subobjects of Σ; §3.3 the
    correspondence on O with "elementary supports", eqs. 3.17–3.28), §4 (the
    relation-R schema, items (i)–(vi)), §5 (conclusion), the
    acknowledgements and all 7 references. Nothing was skipped. The text was
    extracted with PyMuPDF; diagram (2.10) was reconstructed from the
    surrounding text. I checked the proofs of Theorems 3.1 and 3.2, the
    support characterisation (3.21)–(3.22), the items of §4, and the §2.4
    argument from Kadison–Ringrose Theorem 4.3.13, which was taken as stated
    and not looked up. The IJTP version of record was not read.
    Bibliographic data were checked against the arXiv abstract page and
    Crossref. There is no Anthology of the SOTA entry for this paper
    (searched the anthology's literature.d for the arXiv id and title). This
    is part IV of the series whose part I is LIT-325, read as one series
    with Butterfield & Isham (1999, part II) and Hamilton, Isham &
    Butterfield (2000, part III).). The first NOTE on this paper, which was
    seeded from its abstract alone.
date: '2026-10-01'
summary: >-
  Butterfield & Isham show, over the poset V of commutative von Neumann
  subalgebras, that sieve-valued valuations and "interval valuations"
  (assignments of support projectors, or of subsets of Gelfand spectra)
  determine each other under stated conditions. If supports s(α, V) =
  inf{P̂ | α_V(P̂) = true_V} form a global element of the coarse-graining
  presheaf G, then α_{V₁}(P̂) = {V₂ ⊆ V₁ | G(s(α, V₁)) ≤ G(P̂)} is a
  sieve-valued valuation obeying FUNC (Theorem 3.1). There is an analogue
  for "tight" subobjects of Σ (Theorem 3.2). Both are satisfied by every
  state's valuation ν^ρ. The ordering ≤ (or ⊆) is shown to be the natural
  relation securing sievehood, null, monotonicity, exclusivity and unit
  (§4). The review §2.4 also supplies the proof, via state extension, that
  G ≅ CloΣ: restricting the clopen set of P̂ to V₂ gives the clopen set of
  its coarse-graining. Part III had only asserted this.
---

# NOTE-328: A Topos Perspective on the Kochen-Specker Theorem: IV. Interval Valuations

## Contribution

This is the last paper of the series. It completes part III's programme on the base category V.

1. **G ≅ CloΣ, proved (§2.4).** For V₂ ⊆ V₁ and P̂ ∈ L(V₁), {κ|_{V₂} | κ ∈ σ(V₁), κ(P̂) = 1} = {λ ∈ σ(V₂) | λ(G(P̂)) = 1}. So the coarse-graining presheaf is isomorphic to the presheaf of clopen subsets of the spectra *with direct image under restriction* as its arrow map (eq. 2.11).
2. **The correspondence between sieve-valued and interval valuations (§3).** It is made into two theorems, one for interval valuations that are global elements of G (supports) and one for "tight" subobjects of Σ. On the operator category O it is stated heuristically through "elementary supports" (§3.3).
3. **The choice of relation (§4).** It surveys how the properties of a valuation defined by "a(V₂) R coarse-graining of P̂" depend on the relation R, and shows that R = ≤ (or ⊆) is the natural choice.

## Key insight

A sieve-valued valuation is just a coarse-grained comparison with a single "support" region per context: P̂ is true at V₂ iff the support at V₂ lies under P̂'s coarse-graining there. If the supports cohere under coarse-graining (a global element of G), all the properties of a generalised valuation, including sievehood and FUNC, follow from monotonicity of coarse-graining.

For a quantum state ρ the support at V is the least projector of V that ρ makes certain. For a pure state ψ this is the least projector in V above |ψ⟩⟨ψ|, i.e. the outer daseinisation of the state's own projector. That identification is my gloss; the paper does not use the term. So the state's whole sieve-valued semantics is fixed by one global element of G.

## Assumptions

- **Base category V** as in part III: commutative von Neumann subalgebras of B(H), ordered by inclusion. ℂ1̂ is not excluded. O is kept "for heuristic reasons" (§2.1). W is set aside (fn. 3).
- **KS cited (§2.2):** "(for dim H > 2) the presheaf Σ over V has no global elements".
- **Augmented propositions (§2.3):** a projector at V is a proposition about the whole stage V, as in part III. The notation V(P̂) := {κ ∈ σ(V) | κ(P̂) = 1} is introduced.
- **The state-extension theorem.** Kadison–Ringrose Thm 4.3.13 (iv) is used to extend a character λ of V₂ to a character κ of V₁ with κ(P̂) = 1 (eqs. 2.8–2.9). It is credited to Halvorson (fn. 4) and taken as stated.
- **Theorems 3.1–3.2** assume only that α assigns *some set of arrows* to each (V, P̂). Sievehood is a conclusion, not an assumption.
- **The O-section (§3.3)** is explicitly "heuristic". Its claims are "strictly true" only on O_d, the discrete-spectrum operators, because f(σ(Â)) ⊆ σ(f(Â)) can be strict (3.19) and an infimum of Borel sets need not be Borel (Def. 3.1).
- **Interpretation (fn. 6).** Interval valuations are not offered as a solution to the measurement problem (contrast the modal interpretation, Vermaas [7]).

## Key results

- **G ≅ CloΣ (§2.4, eqs. 2.7–2.11).**
  - *The presheaf.* CloΣ(V) = {V(P̂) | P̂ ∈ L(V)} is the clopen subsets of σ(V), with the direct image under restriction as arrow map (2.7).
  - *The easy inclusion.* The restriction image of V₁(P̂) lies inside V₂(G(P̂)).
  - *The converse.* A character λ of V₂ with λ(G(P̂)) = 1 extends to a character κ of V₁ with κ(P̂) = c for any c between sup{λ(Ê) | Ê ∈ V₂, Ê ≤ P̂} and inf{λ(Ê) | Ê ∈ V₂, P̂ ≤ Ê}. The infimum is 1, because every such Ê ≥ G(P̂), so c = 1 is allowed.
  - *The isomorphism.* N_V(P̂) = V(P̂) is natural (diagram 2.10) and invertible.
  - *A step left implicit.* The extension theorem gives a state, while a character is needed. The paper says this follows "using the fact that the set of pure states of a commutative C*-algebra is its spectrum". The implicit step is that the extensions of the pure λ with κ(P̂) = 1 form a non-empty weak*-compact face of the state space, whose extreme points are pure. That step is standard and repairable.
- **Every global element γ of G gives a subobject of Σ (2.32).** The stronger notion maps into the weaker one: global elements of G are "tight" subobjects, and not every subobject is one.
- **The support sufficient condition (Theorem 3.1).** Let α assign sets of arrows, with supports s(α, V) := inf T^α(V). Assume (i) i_{V₂V₁} ∈ α_{V₁}(P̂) iff s(α, V₂) ≤ G(P̂), and (ii) s(α, V₂) = G(s(α, V₁)) (the supports are a global element of G). Then:
  - (a) α is sieve-valued;
  - (b) α obeys FUNC; this needs only (i);
  - (c) α_{V₁}(P̂) = {V₂ | G(s(α, V₁)) ≤ G(P̂)} (3.3).
  - *Proof check.* The proof is short and correct. It uses only monotonicity and functoriality of G, G_{V₃V₂}∘G_{V₂V₁} = G_{V₃V₁}; I checked the latter, which the paper uses without comment.
  - *The state valuations satisfy it.* ν^ρ satisfies (i) "trivially", and (ii) by part III §4.3.
- **Mutual determination (§3.2.1).** Starting from α, the valuation rebuilt from its supports equals α iff α obeys (i), which is "trivially" true by definition. Starting from any assignment a(V) ∈ L(V), the valuation α^a has supports exactly a, by (3.6). And α^a is a sieve whenever a is a global element of G.
- **The tight-subobject analogue (Theorem 3.2).** Use intervals I^α(V) = ⋂_{P̂ ∈ T^α(V)} V(P̂) (2.27) in place of supports. Condition (i) becomes I^α(V₂) ⊆ V₁(P̂)|_{V₂}, and (ii) becomes "tightness", I^α(V₂) = I^α(V₁)|_{V₂} (3.9). The conclusions are (a) a sieve, (b) FUNC (using G ≅ CloΣ) and (c) α_{V₁}(P̂) = {V₂ | I^α(V₁)|_{V₂} ⊆ V₁(P̂)|_{V₂}} (3.11). The proof is correct.
  - *The state valuations satisfy it.* ν^ρ satisfies the conditions. The paper cites part III §4.4.1 for tightness. Tightness actually follows from the supports being a global element of G, together with (2.11). Part III §4.4.1 proves equality for T_ρ as a subobject of G, not for I^ρ. The conclusion holds; the citation is slightly off.
  - *Clopen needed for the converse.* Starting from an arbitrary a(V) ⊆ σ(V), the rebuilt interval I^{α_a}(V) ⊇ a(V), with equality "naturally" secured when a(V) is clopen. Points in the closure of a(V) cannot be separated by clopen supersets (§3.2.2).
- **On O (§3.3).**
  - *Elementary support.* s(ψ, Â) := inf_Borel{Δ | Ê[A ∈ Δ]ψ = ψ}, a "definition" only up to measure-theoretic niceties.
  - *The characterisation.* ν^ψ(A ∈ Δ) = {f_O | f(Δ) ⊇ f(s(ψ, Â))} (3.21), and likewise for ρ (3.22). I checked both directions; they are correct whenever the support is attained, as on O_d.
  - *Determination.* For pure states ν^ψ is determined by its "certainly true" pairs, since ψ is (§3.3.1).
  - *Supports are subobjects of Σ.* Supports satisfy f(s(ψ, Â)) ⊆ s(ψ, f(Â)), with equality on O_d (3.26–3.28).
- **The relation-R survey (§4).** Define α^{a,R}_{V₁}(P̂) := {V₂ | a(V₂) R G(P̂)} for a global element a of G (4.1). Then:
  - (i) α^{a,R} is sieve-valued iff R is stable under coarse-graining (4.4);
  - (ii) FUNC holds for every R whatsoever;
  - (iii) null holds iff no a(V₂) R 0̂;
  - (iv) monotonicity follows from upward stability of R (4.6–4.7);
  - (v) exclusivity holds for R = ≤ provided a ≠ 0̂;
  - (vi) unit holds iff a(V₂) R 1̂ always.
  - *Conclusion.* R = ≤ gives all of (i)–(v) provided a never assigns 0̂. I checked each item; they are correct.
  - *The analogous claims for ⊆.* For the Σ- and O-schemas (4.2–4.3), the analogous claims for R = ⊆ hold "provided some 'regularity conditions'": non-emptiness, tightness, and f(σ(Â)) = σ(f(Â)). They are stated without detail ("we will not go into details").

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Restricting the clopen region of P̂ in σ(V₁) to V₂ gives exactly the clopen region of its coarse-graining G(P̂); hence G ≅ CloΣ as presheaves | proof relying on a cited extension theorem (KR 4.3.13), with a standard step (pure extension) left implicit | §2.4, (2.7)–(2.11) |
| C2 | If supports form a global element of G and α is defined by "support ≤ coarse-grained P̂", α is a sieve-valued valuation obeying FUNC, with α_{V₁}(P̂) = {V₂ \| G(s) ≤ G(P̂)} | proof (short, correct) | Theorem 3.1 |
| C3 | The same holds with intervals (subsets of σ(V)) in place of supports, if the intervals form a tight subobject of Σ | proof (short, correct), using C1 | Theorem 3.2 |
| C4 | Every quantum state's valuation ν^ρ satisfies the hypotheses of Theorems 3.1 and 3.2; the probability-r valuations (r < 1) do not | the ν^ρ half is proved by citation to part III (partly mis-cited, conclusion correct); the r < 1 "not" is asserted | after Thm 3.1; after Thm 3.2; §2.7 |
| C5 | Sieve-valued and interval valuations "mutually determine" each other under conditions (i) and (ii) | proof; near-definitional, as the paper says ("trivially") | §3.2.1–3.2.2, (3.4)–(3.6), (3.14)–(3.16) |
| C6 | On O_d, ν^ψ(A ∈ Δ) = {f \| f(Δ) ⊇ f(s(ψ, Â))}, and similarly for ρ | proof (checked) on O_d; heuristic on O | §3.3.1, (3.21)–(3.22) |
| C7 | Elementary supports satisfy f(s(·, Â)) ⊆ s(·, f(Â)) "even if Â has in part a continuous spectrum" | assertion; doubtful in general (see Limitations) | (3.26) |
| C8 | For any R, α^{a,R} obeys FUNC; R = ≤ is a natural sufficient choice for sievehood, null, monotonicity, exclusivity and unit (a ≠ 0̂) | proof (each item immediate, checked) | §4 (i)–(vi) |
| C9 | The analogous R = ⊆ results hold for the Σ- and O-schemas under regularity conditions | assertion ("we will not go into details") | §4, end |

## Method

The method is order-theoretic and operator-algebraic. Supports are taken as infima in the complete lattices L(V). Gelfand duality between L(V) and the clopen subsets of σ(V) is used. One analytic input is the extension of characters, through Kadison–Ringrose's state-extension theorem. The main results are proved by unpacking definitions against monotonicity and functoriality of the coarse-graining maps. §4 is a property-by-property analysis of a parametrised definition.

## Concepts

- **V(P̂)** — the clopen set {κ ∈ σ(V) | κ(P̂) = 1}, the "region" of P̂ in the context's state space.
- **CloΣ** — the presheaf of clopen subsets of σ(V), with direct image under restriction. It is isomorphic to G (§2.4).
- **Truth set T^α(V)** — the projectors α makes totally true at V.
- **Support s(α, V)** — inf T^α(V). For a state this is the least projector of V with ρ-probability 1.
- **Interval valuation** — an assignment to each V either of an element of L(V) (sense (ii), a global element of G) or of a subset of σ(V) (sense (i), a subobject of Σ). Part III's sense (iii), a subobject of G, is recalled but not developed.
- **Tight subobject of Σ** — I(V₂) = I(V₁)|_{V₂}, rather than only ⊇ (3.9). Equivalently, a global element of the direct-image power presheaf.
- **Elementary support s(ψ, Â)** — the smallest Borel set of ψ-probability 1 on Â's spectrum, defined where it exists (Def. 3.1).
- **α^{a,R}** — the valuation defined from an interval valuation a by a binary relation R (4.1–4.3).

## Connections

- **Parts I–III.** §2 is a review that reproduces part III's definitions nearly verbatim; Defs. 2.1–2.4 here are part III's Defs. 2.3, 3.1, 3.3 and 3.4. It adds the proof part III lacked. §2.7 summarises part III §4's three senses of interval valuation. Part II's style of "naturalness" argument returns in §4. Part I's O-category valuations reappear in §3.3 with the new support characterisation (3.21)–(3.22). Read as a series:
  - *Part I* sets the semantics.
  - *Part II* argues that the semantics is generic.
  - *Part III* moves it to operator algebras.
  - *Part IV* shows that on that base a state's semantics reduces to one coherent assignment of regions, its supports.
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md); [NOTE-277](NOTE-277.md), [NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md)).**
  - *Daseinised projectors.* [LIT-335](../literature.d/LIT-335.md)'s daseinisation δ(P̂)_V = the least projector in V above P̂ is G here. [LIT-335](../literature.d/LIT-335.md)'s clopen sub-object δ(P̂) is the image of the global element V ↦ G(P̂) under the isomorphism N proved in §2.4. The present paper is where that isomorphism is actually proved in the series.
  - *Truth values.* [LIT-335](../literature.d/LIT-335.md)'s truth values ν(A ε Δ; |ψ⟩)_V = {V′ ⊆ V | ⟨ψ|δ(P̂)_{V′}|ψ⟩ = 1} ([NOTE-292](NOTE-292.md)) are this series' ν^ρ.
  - *The pseudo-state (my gloss).* Theorem 3.1(c) rewrites them as "support ≤ daseinised proposition", where the support of a pure state is δ^o(|ψ⟩⟨ψ|). That is the form later Döring–Isham writing calls a pseudo-state. That later work is not in the record, so the comparison is unverified against its text.
  - *DI III's "spread" is a different object ([NOTE-290](NOTE-290.md)).* [LIT-299](../literature.d/LIT-299.md)'s state-independent spread [λ(δ^i(Â)), λ(δ^o(Â))] at a point λ of the spectrum, and [NOTE-290](NOTE-290.md)'s "value = spread", are not these interval valuations. Here the intervals are state-dependent supports; there they are the ranges of daseinised operators at each spectral point. The two meet only in using V and daseinisation.
- **Modal interpretation (Vermaas [7]).** The paper names it in fn. 6 and distinguishes its aim from it.
- **Anthology of the SOTA.** No entry; nothing for ML practice.

## Bearing on the record

- **[THEORY-037](../theory.d/THEORY-037.md) (Proposed).**
  - *What it adds.* The paper proves (§2.4) the fact that underlies the claim's source: coarse-graining a projector is the direct image of its clopen region, so each projector defines a "tight" clopen subobject of Σ, a global element of CloΣ ≅ G. It also separates tight subobjects from mere subobjects (Theorem 3.2(ii), §3.2.2). That sharpens [THEORY-037](../theory.d/THEORY-037.md)'s caveat that clopen sub-objects are not all sub-objects.
  - *What it does not reach.* It constructs no Heyting operations on Sub_cl(Σ), no implication and no negation. It therefore does not meet [THEORY-037](../theory.d/THEORY-037.md)'s promote_when.
  - *Possible wording for the THEORY.* [THEORY-037](../theory.d/THEORY-037.md) could cite this paper for "δ(P̂) is a clopen sub-object of Σ because restriction images of clopens are clopens of the coarse-grained projector (Butterfield & Isham 2002, §2.4)", once it is registered.
- **[THEORY-020](../theory.d/THEORY-020.md) (Stone).** Supportive in detail.
  - *The Stone picture.* The isomorphism L(V) ≅ clopens of σ(V) is the Stone representation of the complete Boolean algebra L(V), via Gelfand duality.
  - *Why it bears on [THEORY-020](../theory.d/THEORY-020.md).* The extension result says every point of a coarser context's Stone space that satisfies the coarse-grained proposition lifts to a point of a finer context satisfying the original. So *pairwise*, between nested contexts, local two-valued valuations always extend. The KS obstruction appears only when compatibility is required over the whole poset at once.
  - *Status.* That fits [THEORY-020](../theory.d/THEORY-020.md)'s "the obstruction lies in how contexts overlap". The paper does not draw the connection, and does not mention Stone or ultrafilters.
- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected).** Consistent with the refutation; no new bearing. Truth values remain sieves on V regardless of global sections.
- **The owner's map.** For a reading of propositions as regions of a context's state space and states as coherent families of regions, this paper is the precise source. Truth is "the state's support region lies inside the proposition's coarse-grained region" (Theorems 3.1(c) and 3.2(c)). That is a containment-of-regions semantics, worth knowing if the map models concepts as regions. Nothing here concerns hyperplane arrangements or topes.
- **ML practice.** It carries nothing for ML practice.
- **For filing.** `quantum-foundations`, `mathematics` (operator algebras, lattices), `contextuality`, `logic` (valuation semantics).

## Limitations

- **The main theorems are near-definitional.** In Theorem 3.1, condition (i) is essentially conclusion (c) once (ii) holds. The paper itself calls the converse directions "trivially" true (§3.2.1–3.2.2). The correspondence is a clean repackaging, not a deep result. The abstract's "two main results" are accurately described but modest.
- **The deepest step is borrowed and compressed.** §2.4 rests on KR Thm 4.3.13. The move from a state extension to a character extension is not spelled out (a standard face/extreme-point argument).
- **The O-section is heuristic, and (3.26) appears wrong beyond O_d.** The claim that f(s(·, Â)) ⊆ s(·, f(Â)) holds "even if Â has in part a continuous spectrum" has two problems.
  - *Definition.* For a continuous spectral measure there is no smallest Borel set of full measure, so s(·, Â) is undefined as written.
  - *Counterexample (the reader's).* Read s as the closed support. Take a spectral measure uniform on [0,1] and f the indicator of {½}. Then f(s) = {0,1}, but s(f(Â)) = {0}. So the inclusion fails for Borel f. The paper's own §3.3 restricts its strict claims to O_d, and nothing on V depends on this.
- **Negative claims about probability-r valuations are asserted** without counterexamples (§2.7, after Thms 3.1 and 3.2).
- **§4's results for ⊆-schemas are stated without proof.** The regularity conditions are listed but their sufficiency is "not go[ne] into".
- **Nothing on probabilities, dynamics or composite systems.** As in the earlier parts, quantum probabilities enter only through "probability 1" (and the r-family).

## Open questions

- Which interval valuations that are *not* tight subobjects (only ⊇) still induce useful sieve semantics? The paper's conditions are sufficient, not necessary.
- Is there an intrinsic characterisation of the global elements of G that arise as supports of states? That would be a topos analogue of Gleason; part I's §6 asked for one, and this paper's support picture is a natural place to state it. Unanswered here.
- How do these interval valuations relate to Döring–Isham's daseinised-operator spreads ([LIT-299](../literature.d/LIT-299.md))? Both are built from V and coarse-graining; the paper predates that work, and the record holds no comparison.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- Identifiers confirmed. Title "A Topos Perspective on the Kochen-Specker Theorem: IV. Interval Valuations", by Butterfield and Isham (that order, on the title page, on arXiv and in Crossref), arXiv quant-ph/0107123, IJTP 41 (2002). The batch's description is correct.
- The paper cites part III as "J. Hamilton, J. Butterfield and C.J. Isham" (ref. [4]). Part III's own title page has Hamilton, Isham, Butterfield.
- The abstract's "two main results" (the correspondence; the naturalness of ≤) are what §§3–4 deliver. The most consequential mathematics, the proof that G ≅ CloΣ, sits in the "review" §2.4 and is not mentioned in the abstract.
