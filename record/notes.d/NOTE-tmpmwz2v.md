---
status: Read
paper: LIT-tmpreakf
title: 'Some Possible Roles for Topos Theory in Quantum Theory and Quantum Gravity'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of arXiv gr-qc/9910005 v1 (2 Oct 1999, the only
    version; title page dated "28 September 1999", preprint
    Imperial/TP/98–99/76), from the arXiv PDF, 25 PDF pp. (title page plus
    printed pp. 1–24), text extracted with PyMuPDF. Read: abstract and
    title-page notes (submitted to *Foundations of Physics* for an issue in
    honour of Marisa Dalla Chiara; based on a lecture by Isham at "Towards a
    New Understanding of Space, Time and Matter", UBC 1999), §1 (§§1.1–1.4:
    realism in quantum theory, quantum gravity, "whence the continuum?",
    points to regions and synthetic differential geometry), §2 (categories,
    subobject classifiers, presheaf toposes, sieves, global sections), §3
    (§§3.1–3.7: reference frames, observers in cosmology, unitary evolution,
    causal sets, TQFT, continuous-time histories, presheaves of propositions
    and valuations), §4 (conclusion), all footnotes and the 14 references.
    Nothing was skipped. The Found. Phys. version of record was not read. No
    dossier existed. No entry exists in the Anthology of the SOTA (grep of
    record/literature.d for the arXiv id and title) or in nucleation.). The
    first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-10-01'
summary: >-
  Isham & Butterfield argue, without proving anything new, that presheaf
  toposes over a base of "contexts" suit physics because the subobject
  classifier Ω is fixed by the base. They say this answers the objection
  that many-valued logics are arbitrary (§2.2), and that it keeps the
  logic distributive (§1.1). They then sketch seven applications. Five are
  speculative one-paragraph proposals (frames, observers, causal sets,
  TQFT, synthetic-differential-geometry time in continuous histories). One
  (§3.7) recaps their Kochen–Specker results: KS ⇔ the dual presheaf D(Â)
  = Hom(W_A, {0,1}) on the operator category O has no global sections (dim
  H > 2), and every state ψ gives a FUNC-obeying sieve-valued valuation
  ν^ψ(A ∈ Δ) = {f_O : Â → B̂ | Ê[B ∈ f(Δ)]ψ = ψ}.
---

# NOTE-tmpmwz2v: Some Possible Roles for Topos Theory in Quantum Theory and Quantum Gravity

## Contribution

This is a programmatic essay, not a results paper. It does three things that the KS series' technical papers do not.

- **It states the motivations together.** The KS-theorem motivation (keep a "realist flavour" despite Kochen–Specker, §1.1) appears alongside a quantum-gravity motivation: doubt that space, time, quantity values and probabilities should be modelled by ℝ, or by sets at all (§§1.2–1.4).
- **It gives a conceptual argument for presheaf truth values.** The subobject classifier is unique up to isomorphism, so the many-valued logic is not arbitrary (§2.2, item 4, repeated in §3.7).
- **It catalogues candidate presheaf constructions in physics.** Only the last of them (§3.7) had been worked out.

It establishes no theorem. Everything in §3.7 is quoted from KS I–II. The equivalence of FUNC with naturality is proved in part II as Theorem 4.1 ([NOTE-329](NOTE-329.md)), and here it is stated as "it turns out".

## Key insight

The paper's lasting proposal is to treat a base category of "contexts" (frames, times, causal-set points, operators) as stages of truth. Physics is then done in presheaves over it, where the logic is intuitionistic but distributive and is determined by the base, not chosen. This places the Kochen–Specker valuations, and the broader doubt about ℝ and set-theoretic space, in one framework. The doubt about ℝ is what later becomes Döring–Isham's quantity-value objects that are not the reals, and their neo-realism.

## Assumptions

- **Quantum theory.** Standard: bounded self-adjoint operators on H, spectral projectors Ê[A ∈ Δ], and the Kochen–Specker theorem for dim H > 2 (cited, [4]).
- **Topos theory, at a minimum.** Only the subobject-classifier clause of the definition of a topos is presented, together with presheaves on a small category C (§2). Sieves on an object A are sets of arrows out of A closed under post-composition. For a poset they are upper sets (§2.3.1).
- **Interpretive premises.**
  - Classical physics satisfies two assumptions: (i) every quantity has a real value, and (ii) ideal measurement reveals it, "epistemology models ontology" (§1.1).
  - Strict instrumentalism is untenable, especially in quantum gravity (§1.1). This is asserted, with a pointer to their ref. [9].
  - There is "no good a priori reason" for continuum space or time, or for real-valued probability under the logical or propensity interpretations (§1.3). This is argued informally.
- **Scope of §3.7.** The base category is O (all bounded self-adjoint operators, with arrows Â → B̂ when B̂ = f(Â)). This is part I's category, not part III's von Neumann-algebra base.

## Key results

The paper's results are its claims and its recap. No new theorem is proved.

- **§1.1, the distributivity claim.** "Any topos has an associated internal logical structure that is distributive", in contrast to Birkhoff–von Neumann quantum logic, while being non-Boolean in general.
- **§2.2 item 4, the non-arbitrariness argument.** Ω is unique up to isomorphism and carries a Heyting-algebra structure. So "a major traditional objection to multi-valued logics—that the exact structure of the logic … seems arbitrary—does not apply here". This is repeated in §3.7 for the KS valuations.
- **§2.3.1, sieve operations for a general small category.** ∧ = ∩, ∨ = ∪, S₁ ⇒ S₂ = {f : A → B | ∀g : B → C, g∘f ∈ S₁ ⇒ g∘f ∈ S₂} (2.10), and ¬S = {f | ∀g, g∘f ∉ S} (2.11). Only S ∨ ¬S ≤ 1 holds (2.12). The characteristic arrow of a subobject K ⊆ X is χ_A(x) = {f : A → B | X(f)(x) ∈ K(B)} (2.13), with inverse K_χ(A) = χ_A⁻¹{1} (2.14).
- **§3.1 and §3.3, frames and unitary evolution.**
  - A wave function together with its transforms under the frame rotations U(e, e′) is a global section of a presheaf of copies of L²(ℝ³) over the category of orthonormal frames (one arrow between any two objects).
  - A Schrödinger-picture history is a global section of the presheaf t ↦ Hₜ over (ℝ, ≤), with transition maps U_{t′−t}.
- **§§3.2, 3.4–3.6, proposals.**
  - Observer-indexed Hilbert spaces or C*-algebras for cosmologies with horizons (§3.2).
  - Presheaves of Hilbert spaces on a causal set, following Markopoulou (§3.4).
  - TQFT's Atiyah functor on the cobordism category read as a "presheaf reformulation" (§3.5).
  - In Savvidou's continuous-time history algebra, [xₜ, pₜ′] = iħτδ(t′ − t) (3.6). The δ-function "suggests" modelling the external time t by the real-number object of a topos with nilpotent infinitesimals, as in synthetic differential geometry (§3.6).
- **§3.7, recap of KS I–II.**
  - The dual presheaf D(Â) = Hom(W_A, {0,1}), with restriction along W_{f(A)} ⊆ W_A, has global sections exactly the FUNC-obeying {0,1} valuations of all projectors (3.8). KS is therefore equivalent to "D has no global sections" when dim H > 2.
  - The coarse-graining presheaf G(Â) = W_A, with G(f_O)(Ê[A ∈ Δ]) = Ê[f(A) ∈ f(Δ)] (3.9).
  - A sieve-valued valuation ν defines a natural transformation G → Ω iff it obeys FUNC, ν(f(A) ∈ f(Δ)) = Ω(f_O)(ν(A ∈ Δ)) (3.11)–(3.12).
  - ν^ψ (3.13) and ν^ρ(A ∈ Δ) = {f_O | tr(ρ Ê[B ∈ f(Δ)]) = 1} (3.14) obey FUNC.
- **§1.3–1.4 and §3.7, interpretive positioning.** The topos proposal "combines aspects" of Literalism (Everett, quantum logic) and Extra Values (pilot wave, modal interpretations). It attributes values to all quantities beyond the eigenvalue–eigenstate link, and does so using only the orthodox formalism.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Kochen–Specker (dim H > 2) is equivalent to the dual presheaf D on O having no global sections | strong | definitional argument via (3.8), with KS cited; proved in KS I ([LIT-325](../literature.d/LIT-325.md)) |
| C2 | Every state ψ or ρ gives a sieve-valued valuation on G that obeys FUNC and generalises the eigenvalue–eigenstate link | strong (by reference) | (3.13)–(3.14); "one can check", with the proof in KS I |
| C3 | A sieve-valued valuation on G obeys FUNC iff it defines a natural transformation G → Ω (a subobject of G) | strong (by reference) | stated "it turns out"; proved as Thm 4.1 of part II ([NOTE-329](NOTE-329.md)) |
| C4 | The internal logic of any topos is distributive (Heyting), so the proposal departs from Birkhoff–von Neumann quantum logic while remaining non-Boolean | strong | standard topos theory, cited; correct |
| C5 | Because Ω is unique up to isomorphism, the many-valued logic is not arbitrary | moderate | correct for a *given* topos (§2.2); the choice of base category, and so of the topos, remains a free choice (O here, V in part III), so the arbitrariness is relocated, not removed. The paper does not discuss this |
| C6 | In any topos the subobjects of an object form a complete Heyting algebra (a locale) | moderate | true for presheaf (Grothendieck) toposes, which are all the paper uses; completeness fails for elementary toposes in general |
| C7 | There is no good a priori reason for continuum space or time, or for real-valued probabilities; propensities may be only partially ordered | weak | informal philosophical argument (§1.3, fn. 7) |
| C8 | The frame and unitary-evolution presheaves (§§3.1, 3.3) have "essentially trivial" internal logic | weak; half wrong | true for §3.1, where any two frames are joined by exactly one arrow, so the base is a groupoid and the topos is Boolean. False as stated for §3.3: the base (ℝ, ≤) is a non-trivial poset, and its sieves (upper sets of [t, ∞)) form a non-Boolean Heyting algebra. That is Isham's own 1997 sets-through-time example, and it matches §3.4's verdict that a causal set's sieve logic is "distinctly non-trivial" |
| C9 | Causal sets, TQFT, observer-dependent quantum cosmology and SDG time in continuous histories are natural sites for presheaf or topos methods | weak | one-paragraph proposals; no construction beyond definitions |
| C10 | The topos valuations combine the virtues of Literalism and Extra Values and retain a "realist flavour" | weak | interpretive argument (§3.7) |

## Concepts

- **Stage of truth / context.** An object of the base category C relative to which sieve-valued truth values are assigned (§2.3.1, §3).
- **Sieve.** Here, a set of arrows *out of* A closed under post-composition (§2.3.1). For a poset, an upper set. This is the same convention as Isham 1997 and the KS series.
- **Global section (point).** An arrow 1 → X, i.e. a family γ_A ∈ X(A) matching under every X(f) (2.15).
- **Dual presheaf D, coarse-graining presheaf G, FUNC.** As in KS I ([NOTE-271](NOTE-271.md)), here on O.
- **Literalism / Extra Values.** Two strategies for the measurement problem (§3.7, fn. 12, deferring to their ref. [9]). Literalism keeps the eigenvalue–eigenstate link (Everett, quantum logic). Extra Values gives it up and postulates additional values for selected quantities (pilot wave, modal interpretations).
- **Locale.** A complete Heyting algebra, presented as a point-free "theory of regions" (§1.4.1). In §1.4.1 and §2.3.1 a Heyting algebra is called "relatively complemented"; the standard term is relatively *pseudo*-complemented, and the defining property (1.3)/(2.7) given is the right one.
- **External / internal time.** In Savvidou's continuous-time histories, t labels the copy Hₜ, and s parametrises a Heisenberg motion generated by the time-averaged Hamiltonian (3.7) (§3.6).

## Connections

- **KS series.**
  - *Part I ([LIT-325](../literature.d/LIT-325.md), [NOTE-271](NOTE-271.md)).* §3.7 restates it on the operator category O, including the KS ⇔ no-global-sections equivalence and ν^ρ.
  - *Part II ([LIT-381](../literature.d/LIT-381.md), [NOTE-329](NOTE-329.md)).* Supplies the FUNC ⇔ natural-transformation theorem asserted in §3.7.
  - *Part III ([LIT-380](../literature.d/LIT-380.md), [NOTE-327](NOTE-327.md)).* Cited as in preparation. The paper does not anticipate the move to V.
  - *Part IV ([LIT-382](../literature.d/LIT-382.md), [NOTE-328](NOTE-328.md)).* Does not yet exist. Reference [3]'s promise of interval valuations goes unmentioned.
  - *Relation to the series.* The essay supplies the series' broader motivation, which the series papers themselves state only briefly (part I §1 has the via media between naive realism and quantum logic). It adds nothing technical.
- **Isham 1997 (this batch).** Not cited. Its sets-through-time example shows that the (ℝ, ≤) base of §3.3 here has a non-trivial logic, contradicting §3.3's remark (C8).
- **Döring–Isham ([LIT-343](../literature.d/LIT-343.md), [LIT-335](../literature.d/LIT-335.md), [LIT-299](../literature.d/LIT-299.md), [LIT-310](../literature.d/LIT-310.md); [NOTE-277](NOTE-277.md), [NOTE-292](NOTE-292.md), [NOTE-290](NOTE-290.md), [NOTE-285](NOTE-285.md)).**
  - *The doubt about ℝ.* §1.3's doubt that quantities should take values in ℝ becomes concrete in [LIT-299](../literature.d/LIT-299.md), whose quantity-value object ℝ^⪰ is only a monoid and not the real-number object ([NOTE-290](NOTE-290.md)). [LIT-378](../literature.d/LIT-378.md) restates the continuum argument at length.
  - *Realism.* The "realist flavour" of §1.1 becomes [LIT-343](../literature.d/LIT-343.md)'s "neo-realism", a term already used in Isham 1997.
  - *Systems in different topoi.* §3.2's idea of distinct observer-attached structures prefigures, loosely, [LIT-310](../literature.d/LIT-310.md)'s question of how the topoi of different systems relate ([NOTE-285](NOTE-285.md)). That paper is about subsystems, not observers.
  - *Not carried forward.* The SDG, causal-set and TQFT proposals are not taken up in the record's Döring–Isham papers.
- **Stone ([LIT-353](../literature.d/LIT-353.md)).** Fn. 9 names "Stone's representation theorem for Boolean algebras of 1936" as a landmark of the points-from-regions tradition (§1.4.1). The paper does not connect it to the dual presheaf in §3.7, although D(Â) = Hom(W_A, {0,1}) is exactly the Stone space of W_A.
- **[LIT-223](../literature.d/LIT-223.md) (category-theoretic structural realism).** Cites this paper, with Döring–Isham, for reformulating physics without structured sets. That fits §1.4's doubt about set-theoretic space.
- **[LIT-102](../literature.d/LIT-102.md) (Rejected).** Cites it for formal-language work it does not contain (see corrections).
- **Anthology of the SOTA.** No entry; nothing for ML practice.

## Bearing on the record

- **[THEORY-024](../theory.d/THEORY-024.md) (Rejected: Boolean logic is restored when a presheaf acquires a global section).** This paper is consistent with the refutation and adds one supporting instance.
  - *Ω depends on the base.* §2.2 item 4 says Ω "is fixed by the structure of the topos".
  - *The supporting instance.* §3.1 observes that a base with a unique arrow between any two objects gives the ordinary true/false logic. That is an instance of the fact [THEORY-024](../theory.d/THEORY-024.md) attributes to its reader: a presheaf topos is Boolean iff its base is a groupoid. Here, a two-valued logic coexists with global sections, so it is the base and not the sections that matters.
  - *Caution.* §3.3's claim that the (ℝ, ≤) presheaf has "essentially trivial" logic is wrong (C8). The global sections there are histories, and if the remark were taken literally it would read like the rejected claim. It should not be cited for that.
- **[THEORY-020](../theory.d/THEORY-020.md) (Stone; one Boolean context is classical, and the KS obstruction lies in overlaps).** Supportive, in the form already recorded from KS I.
  - *Each context alone.* Each D(Â) = Hom(W_A, {0,1}) is non-empty, being the Stone space of a single spectral algebra.
  - *Where KS sits.* KS appears only as the failure of the matching condition (3.8) across overlapping algebras.
  - *Stone named, but not here.* Fn. 9 is the record's only place where this group names Stone's 1936 theorem, but it names it in the points-from-regions context and draws no line to KS. It adds nothing that [LIT-325](../literature.d/LIT-325.md) §2.3 does not already give the THEORY.
- **[THEORY-037](../theory.d/THEORY-037.md) (Proposed: Sub_cl(Σ) is Heyting with pseudo-complement negation).** No bearing on its promote_when. Implication and negation are written out (2.10)–(2.11), but for sieves on an arbitrary small category, not for clopen sub-objects of a spectral presheaf. §1.1 does support the THEORY's framing that the topos logic is distributive and intuitionistic, unlike Birkhoff–von Neumann quantum logic. The claim that subobject lattices are complete Heyting (C6) concerns all subobjects, which [THEORY-037](../theory.d/THEORY-037.md) explicitly does not rely on.
- **ML practice.** It carries nothing for ML practice and does not belong in the Anthology.
- **For filing.**
  - `quantum-foundations` first.
  - `mathematics`: topos and presheaf exposition, SDG, locales.
  - `logic`: intuitionistic truth values, multi-valued logic.
  - `philosophy-of-science`: realism versus instrumentalism, the continuum, interpretations of probability.
  - `contextuality`: §3.7.

## Limitations

- **Almost nothing is shown.** §3.7 is a recap. §§3.1–3.6 are proposals at the level of a paragraph each. The authors say much "remains to be done" (§4). Its citable value lies in its motivations, not its results.
- **Arbitrariness is moved, not removed.** The headline argument (C5) shows that the logic is not arbitrary *given* the base. It does not address the choice of base category, which the series itself changed from O and W to V.
- **Formal looseness in the proposals.**
  - The TQFT "presheaf reformulation" (§3.5) is a functor to Hilbert spaces, not to Set, so it is not a presheaf in the paper's own sense (Def. 2.1).
  - In §1.4.2, non-standard infinitesimals are glossed as "nilpotent d ≠ 0" with reciprocals. Non-standard infinitesimals are not nilpotent; nilpotency belongs to the synthetic approach the paragraph goes on to contrast. The slip is expository and does not affect the SDG point.
  - The §3.3 logic claim is wrong (C8).
- **Small slips.**
  - "Kochen–Specher" (p. 14).
  - The Heyting definition is cross-referenced as "Section 1.3.1" (it is §1.4.1), and sieves as "Section 2.2" (they are §2.3.1).
  - Ref. [14] gives Isham's 1994 J. Math. Phys. paper as vol. 23 under the title "Quantum logic and the consistent histories approach". Isham 1997 cites it as 35, 2157–2185, "Quantum logic and the histories approach to quantum theory".
- **The philosophy is brisk.** It is honest about being brisk. Continuum scepticism (§1.3) and the Literalism/Extra Values positioning (§3.7) are stated in a few paragraphs, with fuller discussion deferred to their ref. [9] (Butterfield & Isham, "Spacetime and the philosophical challenge of quantum gravity", gr-qc/9903072), which is not in the record.

## Open questions

- Which base category is the right one, and is there a principled criterion that would make the choice non-arbitrary in the sense C5 needs? Unanswered here. Part III and Döring–Isham settle on abelian von Neumann subalgebras for technical reasons.
- Can external time in continuous histories actually be modelled by an SDG real-number object, so that the Liouville operator and the δ(t′ − t) commutator become well-defined (§3.6)? This is only a suggestion, and nothing in the record follows it up.
- What do uncertainty relations and non-locality look like in the sieve-valued framework (§4)? Posed by the authors. An explicit treatment would close it.
- Can probabilities with values in a partially ordered additive structure (§1.3) be made into a working probability theory for quantum gravity? Posed only.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Author order.** The batch lists this as "Butterfield & Isham (author order as printed)". The printed order is **Isham and Butterfield**: C. J. Isham, then J. Butterfield, on the arXiv title page. arXiv's metadata and Crossref (Found. Phys. 30(10), 1707–1735) agree, and so do the record's citing works: [LIT-223](../literature.d/LIT-223.md) and [LIT-102](../literature.d/LIT-102.md) both cite "Isham & Butterfield 2000". Part II of the KS series (1999) is the one printed "Butterfield & Isham". The two are easily confused.
- **Not a retrospective.** The batch describes the paper as a survey that "looks back over the programme". It is a forward-looking Festschrift lecture: "we wish to suggest some possible ways…" (§1). It was written while part III was "in preparation" (ref. [3]) and before part IV existed. Only §3.7 (about 2½ pages) concerns the KS work, and it recaps parts I–II. It does not survey the programme's later results, and it does not mention the 1997 consistent-histories topos paper (Isham 1997, this batch) at all.
- **[LIT-102](../literature.d/LIT-102.md).** [LIT-102](../literature.d/LIT-102.md) (ref. [53]) cites this paper, with Döring–Isham, for Isham's investigation of "the role of formal language". This paper contains no formal-language material; that begins with Döring–Isham I ([LIT-343](../literature.d/LIT-343.md)). The citation is accurate only for the general topos motivation.
