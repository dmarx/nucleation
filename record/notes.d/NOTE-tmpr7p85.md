---
status: Read
paper: LIT-tmpm1wb1
title: 'A new description of orthogonal bases'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 0810.0812 v1 (the only version;
    submitted 5 Oct 2008, 17 KB), from the arXiv PDF, 14 pp. I read the
    abstract, §§1–7, Remarks 2.2, 4.4 and 5.2, the footnote and all 15
    references. Nothing was skipped. `pdftotext` was not available in this
    session, so I extracted the text with PyMuPDF. The commutative diagram
    of Definition 2.1 and the string-diagram proofs of Lemmas 4.1, 4.2 and
    4.6 do not survive extraction. I reconstructed each from the algebra the
    text states around it. I re-derived Lemma 4.6's two bra-ket equations
    from the two forms of the Frobenius law, and I checked Lemma 4.1, the
    involution of Lemma 4.2, the Frobenius and unit laws for a
    non-normalised orthogonal basis, and the §6 identity m∘δ = Σ|φᵢ⟩⟨φᵢ|
    numerically myself (random complex 3-d examples). I did not read the
    published version (Mathematical Structures in Computer Science 23(3),
    2013), and I have not checked whether it corrects the slips noted
    below.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-27'
summary: >-
  Theorem 5.1 proves that on a finite-dimensional complex Hilbert space,
  commutative †-Frobenius monoids in FdHilb and orthogonal bases are in
  bijection: the basis is the monoid's copyable elements, and the monoid
  is the linear extension of copying and uniformly deleting that basis. §6
  adds that the monoid is special (m∘δ = id) exactly when the basis is
  orthonormal. Corollaries 7.1 and 7.2 lift this to categories: with fully
  structure-preserving maps the category is equivalent to the groupoid of
  finite sets labelled by positive reals (the basis norms), and with
  comonoid homomorphisms it is equivalent to FinSet.
---

<!-- inactive-ok-file: THEORY-017 — Proposed: the account this paper was filed to test; it stays Proposed on its remaining condition; the directive lapses when its status changes -->

# NOTE-tmpr7p85: A new description of orthogonal bases

## Contribution

Before this paper it was known (Coecke & Pavlovic 2007, the paper's [6]) that an orthonormal basis of a finite-dimensional Hilbert space defines a commutative special †-Frobenius structure. The maps are copying, δ: |φᵢ⟩ ↦ |φᵢ⟩⊗|φᵢ⟩, and uniform deletion, ε: |φᵢ⟩ ↦ 1 (§1, eqs. 1–2). This paper proves the converse and makes it exact.

- **Orthogonal bases.** Every commutative †-Frobenius monoid on a finite-dimensional Hilbert space arises this way from exactly one orthogonal basis, and the two constructions are mutually inverse (Theorem 5.1).
- **Orthonormal bases.** Adding speciality, m∘δ = id, gives exactly the orthonormal bases (§6).
- **Categories.** It lifts the correspondence to two categorical equivalences, with a norm-labelled groupoid of finite sets (Corollary 7.1) and with FinSet (Corollary 7.2).

A basis can therefore be axiomatised by composition and tensor product alone.

## Key insight

In FdHilb, "a basis" need not be taken as a list of vectors. It can be taken as a piece of algebra on the space: a commutative †-Frobenius monoid. The basis is then recovered as the vectors the comultiplication copies perfectly, δ(ψ) = ψ⊗ψ with ε(ψ) = 1.

The engine is that such a monoid, acting on itself by right multiplication, embeds H as a finite-dimensional commutative C*-algebra. By the spectral theorem that algebra is ℂⁿ, and its n characters, dualised, are the copyable vectors. The † condition makes them orthogonal, and speciality makes them unit length.

## Assumptions

- **The category.** FdHilb: finite-dimensional *complex* Hilbert spaces and (continuous) linear maps, with the usual tensor product and † the Hilbert adjoint (abstract, §1). The monoidal unit is ℂ. The paper does not say "complex" in the definition, but the proofs use ℂ as the unit and the C*-algebra spectral theorem. §6 says "on a finite-dimensional complex Hilbert space".
- **Frobenius monoid (Def. 2.1).** A quintuple (X, m, u, δ, ε), with (m, u) a monoid and (δ, ε) a comonoid, satisfying the Frobenius law in both forms, δ∘m = (m⊗id)∘(id⊗δ) = (id⊗m)∘(δ⊗id). I reconstructed the law from the garbled diagram and from its use in §3.
- **The † conditions.** A †-Frobenius monoid is (X, m, u) with δ = m† and ε = u†.
- **Special and commutative.** Special means m∘δ = id_X. Commutative means σ∘δ = δ, with σ the symmetry.
- **Copyable element (Def. 2.4).** A comonoid homomorphism α: I → X, i.e. δ∘α = α⊗α and ε∘α = 1. The counit condition excludes the zero vector.
- **Basis.** A basis is a set of vectors, not an equivalence class. No quotient by phases, scalings or orderings is taken. Two orthogonal bases that differ by a phase on one vector give two different monoids, since δ fixes the copied vector exactly. Permuting a basis gives the same set and so the same monoid.
- **Finite dimension throughout.** The proofs use dimension counting (Theorem 5.1) and "finite-dimensional involution-closed subalgebra" (Cor. 4.3).

## Key results

- **§3, basis ⇒ monoid.** For an orthogonal basis, (1) and (2) define a commutative †-Frobenius comonoid. δ alone recovers the basis, since any ψ with at least two non-zero coefficients makes δ(ψ) entangled, so δ(ψ) ≠ ψ⊗ψ. The one-non-zero-coefficient case, c·φᵢ with c ∈ {0,1}, is left implicit. The formulas (3) and (4) are stated for the normalised case (see corrections).
- **Lemma 4.1.** In any symmetric monoidal †-category, for a commutative †-Frobenius monoid, the adjoint of right multiplication is again a right multiplication: R_α† = R_α′, with α′ = (id ⊗ α†)∘m†∘u. The proof is diagrammatic (unit and Frobenius laws). I checked it numerically in FdHilb.
- **Lemma 4.2.** α ↦ R_α is an injective, involution-preserving monoid embedding of C(I, X) into C(X, X). In FdHilb it is also linear. Injectivity is by R_α∘u = α.
- **Corollary 4.3.** "Any †-Frobenius monoid in FdHilb is a C*-algebra": H embeds as an involution-closed subalgebra of B(H). Remark 4.4 says commutativity was not assumed. But Lemmas 4.1 and 4.2 are stated with "commutative" in the hypothesis, so as written the non-commutative case rests on the remark and on Vicary's [14]. The commutative case, which is all Theorem 5.1 needs, is covered.
- **Corollary 4.5.** The copyable elements of a commutative †-Frobenius monoid on H form a basis of H. By "the spectral theorem for finite-dimensional commutative C*-algebras" (Murphy [11]), the *-homomorphisms H → ℂ form a basis of H*. Their adjoints are comonoid homomorphisms ℂ → H. That unital multiplicative maps between finite-dimensional commutative C*-algebras automatically preserve the involution is asserted, not proved.
- **Lemma 4.6.** If φᵢ, φⱼ are copyable and ⟨φᵢ|φⱼ⟩, ⟨φᵢ|φᵢ⟩, ⟨φⱼ|φⱼ⟩ are cancellable, then all four inner products are real and equal. It rests on ⟨φᵢ|φᵢ⟩²⟨φᵢ|φⱼ⟩ = ⟨φᵢ|φᵢ⟩⟨φᵢ|φⱼ⟩² and its mirror. I re-derived that equation by pairing δ∘m(φᵢ⊗φᵢ) with φᵢ⊗φⱼ under the two Frobenius forms.
- **Corollary 4.7.** The copyable elements form an *orthogonal* basis. If two distinct ones were not orthogonal, Lemma 4.6 gives ‖φᵢ − φⱼ‖² = 0. The sentence "This will only be impossible to satisfy when H is one-dimensional" is garbled but harmless.
- **Theorem 5.1 (the main theorem, verbatim).** "Every commutative †-Frobenius monoid in FdHilb determines an orthogonal basis, consisting of its copyable elements, and every orthogonal basis determines a commutative †-Frobenius monoid in FdHilb via prescriptions (1) and (2). These constructions are inverse to each other." The inverse argument (pp. 9–10) has two halves. From the basis side, §3 already shows the copyable elements are exactly the basis. From the monoid side, δ and ε are determined by their values on a basis, so the monoid that copies the copyable elements is the original one.
- **Remark 5.2.** In FdHilb the "self-conjugate" condition that other papers impose on abstract basis vectors follows automatically from being a comonoid homomorphism. In other categories it is what guarantees involution preservation.
- **§6, orthonormal (no theorem number).** m∘δ = δ†∘δ = Σᵢ |φᵢ⟩⟨φᵢ|, which is the identity iff every ‖φᵢ‖ = 1. So commutative *special* †-Frobenius monoids in FdHilb correspond exactly to orthonormal bases. This is proved in one paragraph, and I checked the identity numerically for a non-normalised basis.
- **§6, arbitrary bases (cited, not proved).** On a finite-dimensional complex vector space, bases correspond exactly to special commutative Frobenius algebras, with no inner product involved. This is credited to John Baez (footnote) and derived in one sentence from Aguiar [2]: such algebras are strongly separable, hence semisimple, hence ≅ ℂⁿ "up to permutation". The summary table:

  | Type of basis | Algebraic structure |
  |---|---|
  | Arbitrary | Commutative special Frobenius algebra |
  | Orthogonal | Commutative †-Frobenius algebra |
  | Orthonormal | Commutative special †-Frobenius algebra |

- **§6, remark.** An arbitrary commutative Frobenius algebra corresponds to no kind of basis and can be "very wild". Speciality and the † axiom "can both serve independently to tame this wildness". This is asserted without an example.
- **Corollary 7.1.** Commutative †-Frobenius monoids in FdHilb, with morphisms preserving all four structure maps, form a category equivalent to the groupoid of finite sets equipped with functions to the positive reals (the basis norms) and norm-preserving bijections. It is supported by an unproved assertion that any fully structure-preserving homomorphism is an isomorphism, and unitary. The corollary's own label, "finite lists of real numbers", should say positive reals. The paper connects it to unitary 2d TQFTs (Kock [9]).
- **Corollary 7.2.** With morphisms preserving only comultiplication and counit, the category is equivalent to FinSet. The argument is by dualising to involution-preserving monoid homomorphisms and Gelfand duality between spectra, in one paragraph. The text refers to it as "lemma 7.2". The paper reads the free functor FinSet → FdHilb as equivalent to the forgetful functor from Frobenius monoids: "a finite set can be considered as a finite-dimensional Hilbert space with the extra structure of a commutative †-Frobenius monoid" (p. 12).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Commutative †-Frobenius monoids in FdHilb and orthogonal bases are in bijection, via copyable elements one way and copy/delete (1)–(2) the other | strong (proof) | Theorem 5.1 with Lemmas 4.1–4.6 and Cors. 4.3–4.7; the key step is a cited spectral theorem for finite-dimensional commutative C*-algebras |
| C2 | Such a monoid is special iff its basis is orthonormal; so commutative special †-Frobenius monoids ↔ orthonormal bases | strong (proof) | §6, one-paragraph computation m∘δ = Σ|φᵢ⟩⟨φᵢ|; checked numerically |
| C3 | Any †-Frobenius monoid in FdHilb, commutative or not, is a C*-algebra | moderate | Cor. 4.3 with Remark 4.4; the lemmas it uses are stated for the commutative case, and the general case defers to Vicary [14] |
| C4 | On a finite-dimensional complex vector space, bases ↔ special commutative Frobenius algebras | strong (cited) | §6, attributed to Baez; a one-sentence derivation via Aguiar [2] (strongly separable ⇒ semisimple ⇒ ℂⁿ) |
| C5 | The category of commutative †-Frobenius monoids with full homomorphisms ≃ the groupoid of finite sets labelled by positive reals | moderate (sketch) | Cor. 7.1; the claim that full homomorphisms are unitary isomorphisms is asserted |
| C6 | With comonoid homomorphisms, the category ≃ FinSet | moderate (sketch) | Cor. 7.2, by adjoints and Gelfand duality, in one paragraph |
| C7 | Arbitrary commutative Frobenius algebras correspond to no kind of basis and can be "very wild" | weak (assertion) | §6, no example given |
| C8 | The axiomatisation captures basis vectors through "the distinct ability to clone and delete classical data as compared to quantum data" (abstract) | weak (interpretive gloss) | Only the copying equation δ(ψ)=ψ⊗ψ is used; the no-cloning and no-deleting references [7], [12], [15] are never cited in the body |
| C9 | Commutative †-Frobenius monoids "model the classical interfaces" and "enable us to specify projector spectra, measurements, and classical data flows" | weak here (cited) | §2, one sentence citing Coecke & Pavlovic [6]; not shown in this paper |

## Method

- **Encode the basis as algebra (§3).** Define δ and ε by copying and deleting on the basis, and check the Frobenius and comonoid laws on basis tensors.
- **Turn the algebra into operators (§4).** Represent H inside B(H) by right multiplication, α ↦ R_α. Show by string diagrams that this is closed under adjoints, R_α† = R_α′, and injective.
- **Invoke the spectral theorem.** The image is a finite-dimensional commutative C*-algebra, so its characters give n linearly independent copyable vectors.
- **Show orthogonality.** A diagrammatic identity (Lemma 4.6) forces any two non-orthogonal copyable vectors to coincide.
- **Show the constructions are inverse (§5), then specialise (§6) and categorify (§7).**

## Concepts

- **†-Frobenius monoid** — (X, m, u) with (X, m, u, m†, u†) Frobenius (Def. 2.1). Also called a †-Frobenius comonoid when the emphasis is on δ, ε (Remark 2.2).
- **Special** — m∘δ = id_X. Here it corresponds to normalisation, not to "being a basis" as it does in FdVect.
- **Copyable element** — a comonoid homomorphism I → X: δ(ψ) = ψ⊗ψ and ε(ψ) = 1 (Def. 2.4). These are the basis vectors.
- **Right action R_α** — m∘(id⊗α): H → H, right multiplication by α. It is how H becomes an operator algebra.
- **Classical interfaces / classical data** — the paper's words (abstract, §2) for what these monoids model relative to the "quantum universe" of a symmetric monoidal †-category. The phrase "classical structure" does not occur in the paper, and "observable" occurs only in the title of reference [4].

## Connections

- **The Frobenius algebra in DisCoCat.** Kartsaklis et al. ([LIT-272](../literature.d/LIT-272.md)) use the commutative special Frobenius algebra a fixed basis induces on a corpus space, σ: vᵢ ↦ vᵢ⊗vᵢ and μ its adjoint, and cite this paper for it. Their σ is this paper's δ (eq. 1) and their μ = σ† is δ† (eq. 3), which "uncopies" only when the basis is orthonormal. [NOTE-246](NOTE-246.md) notes that the unit printed there is wrong and should be 1 ↦ Σᵢ vᵢ. That agrees with this paper's (4), which is itself right only in the orthonormal case.
- **DisCoCat 2010.** Coecke, Sadrzadeh & Clark ([LIT-273](../literature.d/LIT-273.md)) use only the compact structure (ε/η), which needs no Frobenius algebra. In that paper the basis enters only through the self-duality V* ≅ V. This paper is what the later Frobenius move adds on top: a basis *as* structure. That is why [LIT-272](../literature.d/LIT-272.md)'s composition is basis-dependent and [LIT-273](../literature.d/LIT-273.md)'s is not.
- **Van Rijsbergen.** Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md)) treats each observable's eigenbasis as a "point of view". This paper gives the algebraic object that *is* a basis. But a non-degenerate observable fixes its eigenbasis only up to phases, while a commutative †-Frobenius monoid fixes the vectors exactly, phases and norms included. So "observable" and "classical structure" are not the same data. An observable (with its eigenvalues) determines a family of orthonormal (special) such monoids, one per choice of phases.
- **Carroll.** Carroll's point ([LIT-123](../literature.d/LIT-123.md)) is that a bare Hilbert space has no preferred basis. This paper does not argue it, but Corollary 7.2's reading, and the §7 remark that such a basis "is determined up to unitary isomorphism by the norms of the basis elements", fit it. All orthonormal classical structures on a given H are unitarily equivalent, so the space alone distinguishes none. The finite set is "extra structure" (p. 12).
- **The C*-algebra route.** The proof goes through the finite-dimensional commutative C*-algebra spectral theorem, i.e. Gelfand duality in the finite case. This is the same algebra-of-observables machinery whose infinite-dimensional form is the GNS strand ([LIT-241](../literature.d/LIT-241.md), [THEORY-004](../theory.d/THEORY-004.md)), but the paper stays finite-dimensional.
- **What came after (verified by search, content not read).** Abramsky & Heunen, "H*-algebras and nonunital Frobenius algebras: first steps in infinite-dimensional categorical quantum mechanics" (arXiv 1011.6123), takes up the infinite-dimensional case, where Frobenius algebras must drop the unit. Its results are unverified here.
- **Anthology.** Nothing in the Anthology of the SOTA concerns Frobenius algebras or classical structures. Every "Frobenius" there is the matrix norm or Perron–Frobenius. No ANTH- citation is warranted.

## Bearing on the record

- **[THEORY-017](../theory.d/THEORY-017.md): what the paper proves, exactly.**
  - *Category and conditions.* FdHilb: finite-dimensional complex Hilbert spaces and linear maps, with † the Hilbert adjoint.
  - *The main theorem.* Theorem 5.1: commutative †-Frobenius monoids (δ = m†, ε = u†; commutative; Frobenius law; unit and counit laws; no speciality) are in bijection with orthogonal bases. The basis is the monoid's copyable elements.
  - *The special case.* §6, unnumbered: the monoid is special, m∘δ = id, iff the basis is normalised. So commutative special †-Frobenius monoids ↔ orthonormal bases, and here speciality does exactly the work of normalisation.
  - *What kind of correspondence.* It is a bijection between sets, for each fixed H: "These constructions are inverse to each other". A basis is an unordered set of vectors, determined exactly, with no quotient by phases or scalings. A permuted basis is the same set. The categorical equivalences come in §7 as corollaries, not in Theorem 5.1. With all structure preserved, the category is equivalent to finite sets with positive-real labels (Cor. 7.1). With comonoid maps, it is equivalent to FinSet (Cor. 7.2).
  - *Completeness of the proof.* Complete in outline for the commutative case, with small slips. §3's (3) and (4) are the orthonormal formulas, the one-coefficient case of §3 is omitted, the involution-preservation of characters is asserted, and "lemma 7.2" should be "Corollary 7.2". It relies on the cited spectral theorem for finite-dimensional commutative C*-algebras (Murphy [11]), i.e. finite-dimensional Gelfand duality. The arbitrary-basis/FdVect statement relies on Aguiar's semisimplicity of strongly separable algebras and is cited, not proved.
  - *Infinite dimensions.* The paper says nothing. Every statement is in FdHilb, and the proofs use finiteness. This matches [THEORY-017](../theory.d/THEORY-017.md)'s decision to stay finite-dimensional.
  - *Vocabulary.* The paper does not use "classical structure". It says the monoids "model the classical interfaces" and "classical data flows" (§2, citing [6]), and the abstract's "clone and delete classical data" gloss is not developed in the body.
  - *Verdict.* [THEORY-017](../theory.d/THEORY-017.md)'s sentence, "on such a space, commutative special †-Frobenius algebras correspond to orthonormal bases", is proved: Theorem 5.1 with §6. It needs three precisions.
    - The headline theorem is the orthogonal one, and speciality is normalisation.
    - The space must be *complex*. As my own check, not from the paper: on the real 2-dimensional Hilbert space ℝ², the algebra ℂ (basis 1, i, multiplication rescaled by 1/√2) is a commutative special †-Frobenius algebra with no copyable vectors at all. The real case, which is the setting of [LIT-273](../literature.d/LIT-273.md)'s and [LIT-272](../literature.d/LIT-272.md)'s corpus spaces and of [THEORY-004](../theory.d/THEORY-004.md)'s orthogonal ambiguity, is therefore not covered by this theorem.
    - "Orthonormal basis" means the vectors themselves, phases included. That matters, because [THEORY-017](../theory.d/THEORY-017.md) also says an observable fixes its eigenbasis only "up to phases".
  - *Suggested wording.* "Coecke, Pavlovic & Vicary prove (Theorem 5.1 and §6) that on a finite-dimensional *complex* Hilbert space the commutative †-Frobenius algebras are in bijection with the orthogonal bases, the basis being the vectors the comultiplication copies. The special ones correspond exactly to the orthonormal bases, with the vectors fixed exactly, phases included. The categorical literature later calls these 'classical structures'; this paper speaks of 'classical interfaces' and 'classical data'."
- **[THEORY-017](../theory.d/THEORY-017.md)'s two marked inferences.** The paper says nothing about probability distributions, measurement statistics, contextuality or lattices of projections, so it neither supports nor refutes either inference as stated. The nearest it comes is Corollary 7.2 and its gloss that a classical structure *is* a finite set carried by the space (p. 12). That fits the Boolean-structure inference in spirit: the projections diagonal in the basis correspond to subsets of that set. But the paper does not state it, and the inference remains [THEORY-017](../theory.d/THEORY-017.md)'s own.
- **[NOTE-246](NOTE-246.md) ([LIT-272](../literature.d/LIT-272.md) C3) is accurate, with two qualifications.**
  - *The statement itself.* "Any vector space with a fixed basis carries a commutative special Frobenius algebra whose σ copies and μ 'uncopies' the basis" is true.
  - *Where it is proved.* This paper covers it only in the Hilbert-space form (§3, orthonormal) and in the §6 FdVect remark, which is cited to Baez/Aguiar. The easy direction originates in Coecke & Pavlovic 2007, as this paper's §1 says, and this paper's own contribution is the converse.
  - *The σ† = μ condition.* [NOTE-246](NOTE-246.md)'s point that σ† = μ requires orthonormality is correct and matches §6: for an orthogonal but non-normalised basis, δ† is a *different*, non-special multiplication, δ†(φᵢ⊗φᵢ) = ‖φᵢ‖²φᵢ.
  - *The unit.* Its correction of the unit to 1 ↦ Σᵢ vᵢ matches (4).
  - *Two places where [NOTE-246](NOTE-246.md) overstates this paper.* Its Connections says "Commutative special Frobenius algebras on finite-dimensional spaces correspond to choices of orthonormal basis". Without † they correspond to *arbitrary* bases (§6 table), so the sentence needs "†-" and "Hilbert". Its §5 entry cites Coecke–Pavlovic–Vicary for the spider normal form, but this paper contains no normal-form or spider theorem.
- **ML practice.** It carries nothing. This is algebra about bases, and it does not belong in the Anthology.
- **For filing.**
  - *Tags proposed.* `mathematics` first. `quantum-foundations`, because it is framed as giving categorical quantum mechanics its account of classical data within quantum theory (abstract, §2).
  - *Tags not proposed.* `logic`: there is no quantum logic here. `contextuality`: it is not addressed. `information-theory`: the copying is algebraic, not information-theoretic.

## Limitations

- **Finite-dimensional and complex only.** Nothing is said about infinite-dimensional spaces or real scalars, and the proof uses both restrictions.
- **The operational reading is a gloss.** The "clone and delete classical data" interpretation is stated, not argued. No-cloning is never invoked in a proof, and the references for it are uncited in the body.
- **Formulas and cross-references.** §3's (3) and (4) are stated as if for orthogonal bases but hold only for orthonormal ones. The comonoid-homomorphism definition on p. 4 is written with domain and codomain swapped (δ∘f = (f⊗f)∘δ′). §7 refers to "lemma 7.2".
- **Sketches and citations.** The categorical corollaries (7.1, 7.2) are sketches. The non-commutative Corollary 4.3 and the FdVect classification are delegated to [14] and to Baez/Aguiar.
- **The "wildness" of non-special, non-† commutative Frobenius algebras is asserted without an example.**

## Open questions

- **Real Hilbert spaces.** What do commutative (special) †-Frobenius algebras classify there? My example ℂ-over-ℝ suggests direct sums of ℝ and ℂ factors rather than bases. That is unverified against the literature, and it would settle how far the "Frobenius algebra = basis" identification reaches the real vector spaces of distributional semantics.
- **Infinite dimensions.** What survives there, with nonunital algebras? That is the subject of the Abramsky & Heunen line (not read). Reading it would say whether [THEORY-017](../theory.d/THEORY-017.md)'s finite-dimensional restriction can be lifted.
- **Observables and phases.** The phase data a classical structure carries beyond an observable's eigenbasis: is it ever physically or semantically meaningful, or always gauge?

## Corrections to the seeded skim

- none (there was no seed or dossier for this work)
- Identification note for filing: the arXiv abstract page lists only v1 (5 Oct 2008, 17 KB), category quant-ph, with no journal-ref and the related DOI 10.1017/S0960129512000047. Crossref gives it as *Mathematical Structures in Computer Science* 23(3), pp. 555–567, published online 9 Nov 2012 and in print June 2013. The "(2012)" on some citations is the online date. The arXiv PDF lists the authors' affiliation as Oxford University Computing Laboratory. I read the arXiv v1, not the journal version.
- The headline result is about *orthogonal* bases, not orthonormal ones. The abstract and Theorem 5.1 characterise orthogonal bases as commutative †-Frobenius monoids. Orthonormal bases are the special ones (§6). The record's phrasing "commutative special †-Frobenius algebras … are exactly orthonormal bases" is the §6 refinement, not the main theorem.
- The abstract's operational gloss (the comultiplication copies basis vectors, and "we rely on the distinct ability to clone and delete classical data as compared to quantum data") is not developed in the body. No-cloning (Wootters–Zurek, Dieks) and no-deleting (Pati–Braunstein) appear as references [7], [12] and [15], but none of them, nor [8] (Joyal–Street), is cited anywhere in the text. The body proves an algebraic classification and says nothing about cloning.
- §3 is titled for orthogonal bases, but its displayed formulas hold only for orthonormal ones. For an orthogonal basis with ⟨φᵢ|φᵢ⟩ = nᵢ, δ†(|φᵢ⟩⊗|φᵢ⟩) = nᵢ|φᵢ⟩, not |φᵢ⟩ as (3) says, and the unit is ε†(1) = Σᵢ |φᵢ⟩/nᵢ, not Σᵢ |φᵢ⟩ as (4) says (checked numerically). The Frobenius, unit and commutativity laws still hold, so Theorem 5.1 is unaffected, and §6's m∘δ = Σᵢ |φᵢ⟩⟨φᵢ| is correct for the general case.
