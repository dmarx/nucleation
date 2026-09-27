---
status: Read
paper: LIT-tmp7e2en
title: 'H*-algebras and nonunital Frobenius algebras: first steps in infinite-dimensional categorical quantum mechanics'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1011.6123 v3, from the arXiv PDF,
    29 pp. The arXiv abstract page lists three versions, v1 (29 Nov 2010, 30
    KB), v2 (25 Feb 2011, 30 KB) and v3 (6 Jul 2011, 31 KB, comment "29
    pages. Final version"). The PDF carries the stamp "arXiv:1011.6123v3"
    and a regenerated date line, "October 29, 2018". I read the abstract,
    §§1–6 (every subsection, 2.1–2.3, 3.1–3.3, 4.1–4.5, 5.1–5.4), all seven
    footnotes and all 37 references. Nothing was skipped. `pdftotext` was
    not available in this session, so I extracted the text with PyMuPDF. The
    string diagrams do not survive extraction. These are the pictures of
    axioms (A), (U), (C), (M), (F) and (H), the proofs of Lemmas 4, 5 and 6
    and Proposition 7, the proof of Theorem 21, and the element-annotated
    relational diagrams in the proofs of Lemmas 26 and 27 and Proposition
    34. The axioms and (H) are also written algebraically in the text, and I
    worked from those forms. Lemma 5's a∗ is given algebraically, and
    Theorem 21's a∗ₙ = (id ⊗ a†)∘δ(eₙ) is given in the text. For Lemmas 4
    and 6 and Proposition 7, only the chains of axiom labels survive, and I
    did not reconstruct those proofs step by step. For Proposition 34, the
    equations the diagrams encode are stated in the text, and I worked from
    them. I did not read v1 or v2, and I did not read the published version
    (AMS PSAPM 71, 2012), so I have not checked whether they differ from
    v3.). The first NOTE on this paper, which was seeded from its abstract
    alone.
date: '2026-09-27'
summary: >-
  In the category Hilb of complex Hilbert spaces of arbitrary dimension, a
  Frobenius algebra with a unit exists only in finite dimension (Lemma 3).
  So the paper drops the unit, and Theorem 22 proves that a nonunital
  commutative special †-Frobenius algebra corresponds to an orthonormal
  basis (the basis being the algebra's copyable vectors) if and only if it
  is semisimple, if and only if it satisfies Ambrose's H*-axiom (H), and
  if and only if it is a directed colimit of finite-dimensional unital
  ones. Whether (H) is automatic, i.e. whether a nonzero "radical"
  Frobenius algebra exists (Proposition 23), is left open. In categories
  of relations and of nonnegative ℓ²-matrices, Frobenius algebras
  decompose as disjoint unions of abelian groups and do satisfy (H)
  (Theorems 30–38).
---

<!-- inactive-ok-file: THEORY-017 — Proposed: the account whose finite-dimensional boundary this paper was filed to test; the directive lapses when its status changes -->

# NOTE-tmp4nt96: H*-algebras and nonunital Frobenius algebras: first steps in infinite-dimensional categorical quantum mechanics

## Contribution

Coecke, Pavlovic & Vicary ([LIT-274](../literature.d/LIT-274.md)) characterised orthonormal bases of *finite-dimensional* Hilbert spaces as commutative special †-Frobenius algebras. The unit of such an algebra, ε†(1) = Σᵢ|i⟩, does not exist in infinite dimension, and Lemma 3 shows that this is not an accident: a Frobenius algebra in Hilb is unital iff it is finite-dimensional.

This paper finds the replacement. Drop the unit, and add Ambrose's (1945) H*-axiom (H), which can be stated in any symmetric monoidal †-category. With that axiom, orthonormal bases of Hilbert spaces of *any* dimension, separable or not, are recovered exactly (Theorem 22).

It then isolates what remains unknown. Does the nonunital Frobenius law already force (H)? In Hilb that question is equivalent to asking whether a nonzero radical Frobenius algebra exists (Proposition 23). The paper answers the corresponding question positively in categories of relations, locally bifinite relations, some quantale-valued relations and nonnegative ℓ²-matrices (§5).

## Key insight

In infinite dimension, what makes a comultiplication "a basis" is not the unit (there is none) but an involution on points: the regular representation a ↦ R(a) = μ∘(id ⊗ a) must turn a ↦ a∗ into the Hilbert adjoint, R(a∗) = R(a)† (axiom (H)).

This is exactly Ambrose's definition of an H*-algebra. By Gelfand theory, it is equivalent to semisimplicity: the characters of the algebra, which are its copyable vectors, separate points. Characters are orthonormal automatically, by (M) and (F). Semisimplicity is then what makes them span a dense subspace, and so form an orthonormal basis.

In finite dimension the unit hands you (H) for free (Lemma 5, "the central idea" of CPV's proof, p. 8). In infinite dimension you must either assume (H) or prove that the radical part vanishes.

## Assumptions

- **The categories.** Symmetric monoidal †-categories (§2). The main one is Hilb, Hilbert spaces "of unrestricted dimension" (p. 2) with bounded (continuous) linear maps, † the adjoint and the standard tensor product.
  - *Scalars.* The scalars are implicitly complex. The monoidal unit is ℂ. The Wedderburn statement (Theorem 8) is "over the complex numbers". Proposition 13 takes coefficients αᵢ ∈ ℂ, and ℓ²(X) is ℂ-valued (§4.3).
  - *Separability.* Nothing except Theorem 21 assumes it. The index set of the direct sum has "the cardinality of I [equal to] the dimension of H" (p. 11).
  - *Other categories.* fHilb, Rel, fRel, lbfRel (locally bifinite relations), Mat(S), Mat_ℓ²(ℂ) and its nonnegative part Mat_ℓ²(ℝ₊), Rel(Q) for commutative cancellative quantales Q, and PInj (sets and partial injections).
- **Axioms (§2.1 and §3), for a comultiplication δ: A → A⊗A with μ = δ†.**
  - (A) coassociativity: (id ⊗ δ)∘δ = (δ ⊗ id)∘δ.
  - (U) counit: (id ⊗ ε)∘δ = id.
  - (C) commutativity: σ∘δ = δ.
  - (M) speciality: δ†∘δ = id, i.e. δ is an isometry and μ a coisometry.
  - (F) Frobenius: δ∘δ† = (δ† ⊗ id)∘(id ⊗ δ). Its mirror (F′) follows from (C).
- **The redefinition (p. 7).** A *Frobenius algebra* is (A, δ) satisfying (A), (C), (M) and (F), with no unit. One that also has an ε satisfying (U) is called *unital*. Footnote 1 says the unital version is "more specifically termed a special commutative dagger Frobenius algebra (sometimes also called a separable algebra, or a Q-system)". So **"Frobenius algebra" in this paper always means commutative and special (δ isometric), and nonunital unless stated otherwise.** The words "quasi-special" and "normalisable" do not occur.
- **Axiom (H) (§3.2).** There is an operation a ↦ a∗ on points I → A with μ∘(a∗ ⊗ id) = (a† ⊗ id)∘μ†, equivalently R(a∗) = R(a)†. Continuity of ∗ is not required, and in Hilb it is automatic (footnote 4, citing Ambrose Thm 2.3).
- **H*-algebra (Ambrose 1945, §4.1).** A not-necessarily-unital Banach algebra whose underlying space is a Hilbert space H, such that for each x there is x∗ with ⟨xy | z⟩ = ⟨y | x∗z⟩ for all y, z, and similarly on the right. It is *proper* if aA = 0 ⇒ a = 0. By monoidal well-pointedness this is equivalent to (H) in Hilb (p. 11).
- **Copyable element (§4.2).** A point a: I → A with δ∘a = a⊗a. Zero is copyable and is excluded where it matters. A basis is a *set of vectors fixed exactly*, as in [LIT-274](../literature.d/LIT-274.md): phases are not quotiented.
- **The structure theorem (§4, pp. 10–11).** A Frobenius algebra "admits the structure theorem" if it is isomorphic as a coalgebra (equivalently, by †, as an algebra) to a Hilbert direct sum ⊕_I(ℂ, δ_ℂ), with δ_ℂ(1) = 1⊗1.
- **Morphisms (Definition 18).** In Frob(D) and HStar(D), f: A → A′ with (f ⊗ f)∘δ = δ′∘f and f†∘f = id. These are isometric coalgebra homomorphisms.

## Key results

- **Lemma 3 (§2.3).** "A Frobenius algebra in Hilb is unital if and only if it is finite-dimensional."
  - *Proof.* The proof is by citation, to Kock 3.6.9 and Kaplansky 1948. It is backed by the observation that a unit gives a compact structure η = δ∘ε†, which exists in Hilb only in finite dimension.
  - *Why the unit fails.* The deleting map |eᵢ⟩ ↦ 1 is unbounded in infinite dimension: "these can be defined in finite dimension only" (p. 5). Equivalently, the would-be unit Σᵢ|eᵢ⟩ does not converge.
  - *The copying map survives.* Copying, |i⟩ ↦ |ii⟩, extends continuously in any dimension.
- **Lemma 4.** In any †-monoidal category, (M), (F) and (F′) imply (A).
  - *Independence of (U), (C) and (F).* The paper gives three examples. An orthonormal basis of a separable infinite-dimensional space fails only (U). The group algebras of finite noncommutative groups fail only (C). A nontrivial commutative Hopf algebra fails only (F).
- **Lemma 5.** (F) and (U) imply (H), with a∗ = (a† ⊗ id)∘δ∘ε†.
- **Lemma 6.** In a monoidally well-pointed category, (H) and (A) imply (F).
- **Proposition 7.** Any Frobenius algebra in a †-compact category is unital. The proof is by citation to Carboni 1991.
  - *The consequence.* In the unital, well-pointed case, (F) and (H) are "essentially equivalent" (p. 10).
- **Lemma 9.** (M) makes a monoid in Hilb a Banach algebra.
  - *Proof.* P = μ†μ is a projection, so ‖xy‖² = ⟨x⊗y | P(x⊗y)⟩ ≤ ‖x‖²‖y‖².
  - *The Remark after it.* It cites Ingelstam: a semigroup satisfying (H) has automatically continuous multiplication and is a Banach algebra "after adjusting by a constant".
- **Lemma 10.** Given (A) and (H), (M) implies properness, via Ambrose's decomposition A = A′ ⊕ A″ into the trivial ideal and a proper part.
- **Proposition 11.** A structure satisfying (A), (H) and (M) is an H*-algebra and satisfies (F). Conversely, an H*-algebra satisfies (A), (H), (M) and (F).
  - *Commutativity.* The statement omits (C). The surrounding text (p. 11) says "(A), (C), (M) and (H)".
- **Theorem 12 (Ambrose 1945, cited).** "Any proper commutative H*-algebra (of arbitrary dimension) is isomorphic to a Hilbert space direct sum of one-dimensional algebras."
- **Propositions 13–15 (§4.2).** These are the basis-side facts.
  - *Proposition 13.* Given (A) alone, nonzero copyables are linearly independent (after Hofmann).
  - *Proposition 14.* Given (M) alone, nonzero copyables have norm exactly 1, since ‖a‖ = ‖δa‖ = ‖a⊗a‖ = ‖a‖².
  - *Proposition 15.* Given (F) alone, copyables are pairwise orthogonal. The proof is CPV's Cor. 4.7, reproduced as an explicit bra-ket computation.
  - *Copyables and characters (pp. 13–14).* Copyables correspond exactly to comonoid homomorphisms (ℂ, δ_ℂ) → (A, δ) and, by †, to characters (A, μ) → (ℂ, μ_ℂ): the Gelfand spectrum.
- **Theorem 16.** "A Frobenius algebra in Hilb admits the structure theorem and hence corresponds to an orthonormal basis if and only if it is semisimple."
  - *Sufficiency.* The closed span S of the copyables is a coalgebra summand with an orthonormal basis. S = A iff the Gelfand transform is injective, iff A is semisimple.
  - *Necessity.* It is argued in one sentence, from the ideal lattice of ⊕ℂ being a complete atomic Boolean algebra.
- **Proposition 17.** A Frobenius algebra in Hilb satisfies (H) iff it is semisimple. One direction cites Ambrose. For the other, define x∗ by conjugating coefficients in the basis.
- **§4.3, categorical form.**
  - *Proposition 19.* Every set in PInj carries exactly one H*-algebra structure, the diagonal δ(a) = (a, a). It is unital only for singletons, which is "another good argument against demanding (U)" (p. 16).
  - *The adjunction.* ℓ²: HStar(PInj) ⇄ HStar(Hilb): U, with U taking an algebra to its copyables. Ambrose's theorem "can now be restated as saying that this adjunction is in fact an equivalence" (p. 16).
  - *For Frobenius algebras.* Whether the analogous adjunction for Frob is an equivalence is "not yet clear".
- **Theorem 20.** A Frobenius algebra in Hilb is an H*-algebra, and so corresponds to an orthonormal basis, iff it is a directed colimit in Frob(Hilb) of unital Frobenius algebras. Concretely, it is the colimit of the finite restrictions δ_F on ℓ²(F), for F finite.
- **Theorem 21 (separable only).** A Frobenius algebra on a *separable* Hilbert space is an H*-algebra iff there is a sequence eₙ with eₙa → a for all a and with (id ⊗ a†)∘δ(eₙ) convergent. This is an approximate unit.
  - *The converse.* It takes eₙ to be the sum of the first n copyables.
- **Theorem 22 (the summary theorem, statement reproduced).** For a Frobenius algebra in Hilb the following are equivalent:
  - (a) it is induced by an orthonormal basis;
  - (b) it admits the structure theorem;
  - (c) it is semisimple;
  - (d) it satisfies (H);
  - (e) it is a directed colimit (with respect to isometric homomorphisms) of finite-dimensional unital Frobenius algebras;
  - (f) if the space is separable, also: it has "a suitable form of approximate identity".
- **Recovering [LIT-274](../literature.d/LIT-274.md) (p. 18).** "The finite-dimensional result follows immediately from our general result and Lemma 5." That is, (U) and (F) give (H), and then (d) ⇒ (a). The paper adds that Theorem 1 "follows easily" from Abrams's thesis: (M) together with a unit gives semisimplicity, and a commutative semisimple unital Frobenius algebra is a direct sum of fields. On this account the only new ingredient CPV needed was Proposition 15.
- **Footnote 5, orthogonal bases (sketch).** With properness, (A), (C) and (H), but *without* (M), a monoid in Hilb "corresponds to an orthogonal basis". In infinite dimension δ must be postulated monic, "to prevent e.g. the trivial algebra δ(a) = 0". This is the infinite-dimensional counterpart of CPV's Theorem 5.1, and it is asserted, not proved.
- **§4.5, the main question.** "In the presence of (A), (C), and (M), does (F) imply (H)?" It is "open, both for Hilb and for the general case".
- **Proposition 23.** Every Frobenius algebra in Hilb decomposes as A ≅ S ⊕ R, as (co)algebras.
  - *The two parts.* S is the H*-algebra spanned by the copyables. R is radical: it has no copyables and no characters.
  - *What it reduces the question to.* "Does there exist a nontrivial radical Frobenius algebra?" The paper calls it "rather difficult".
- **§5, no destructive interference.**
  - *Theorem 24 (summary).* Nonunital Frobenius algebras in these categories "decompose as direct sums of abelian groups, and satisfy (H)".
  - *The steps.* In Rel, ∼ ("xy is defined") is an equivalence relation (Lemmas 26 and 27, Proposition 28). Each class is an abelian group (Lemma 29, after Huntington, and Theorem 30). So (H) holds with a∗ = a⁻¹ (Theorem 31). The argument uses no units, and so it carries over to lbfRel (Theorem 32).
  - *Rel(Q).* For a cancellative quantale Q, M(a, b, ab)² = 1 (Proposition 34). (H) is proved when q² = 1 ⇒ q = 1 (Theorem 35).
  - *Mat_ℓ²(ℝ₊).* Every summand is a *finite* abelian group of order d, with M ≡ 1/√d (Propositions 36 and 37). (H) holds (Theorem 38).
- **Propositions 39 and 40, back in Hilb.** A Frobenius algebra in Hilb satisfies (H) iff, in some basis, the matrix of δ has nonnegative entries.
  - *Which basis diagonalises it.* It is not the basis in which δ is nonnegative. For a group summand ℂ[G], the copyables are the Fourier characters. The only copyable group element is the identity (§5.4).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A Frobenius algebra in Hilb (with (A), (C), (M), (F)) has a unit iff it is finite-dimensional | strong (cited proof) | Lemma 3, by citation to Kock and Kaplansky, backed by the compact-structure argument (p. 6) |
| C2 | For a nonunital commutative special †-Frobenius algebra on a complex Hilbert space of any dimension: induced by an orthonormal basis ⇔ structure theorem ⇔ semisimple ⇔ (H) ⇔ directed colimit of finite unital ones (⇔ approximate identity, if separable) | strong (proof, partly by citation) | Theorem 22, assembled from Theorems 16, 20 and 21 and Proposition 17. The key steps are Gelfand theory, and Ambrose [Amb45] for semisimplicity of proper H*-algebras (Proposition 17) and for Theorem 21's converse |
| C3 | Commutative H*-algebras in Hilb are exactly orthonormal bases, in arbitrary dimension; ℓ² ⊣ U is an equivalence HStar(PInj) ≃ HStar(Hilb) | strong (classical theorem, cited) | Theorem 12 (Ambrose 1945) and the §4.3 restatement. The equivalence is asserted from Ambrose, not proved here |
| C4 | Nonzero copyables of a Frobenius algebra are linearly independent, of norm exactly 1, and pairwise orthogonal | strong (proof) | Propositions 13–15, each short and complete. I re-derived 14 and 15 |
| C5 | CPV's finite-dimensional theorem (orthonormal version) is a special case | strong (proof) | p. 18: Lemma 5 gives (H) from (U), then Theorem 22 (d)⇒(a). The sentence says Lemma 5 "shows that the algebra is C*", but Lemma 5 gives (H), not a C*-identity |
| C6 | Dropping (M) but assuming properness and a monic δ, (A), (C), (H) algebras correspond to orthogonal bases in any dimension | weak (sketch) | Footnote 5 only. No norm condition is stated. My derivation, below, shows the basis norms must be bounded above for δ to be bounded |
| C7 | Whether (F) implies (H) given (A), (C), (M) is open in Hilb, and is equivalent to the non-existence of nonzero radical Frobenius algebras | strong for the reduction (proof), open for the question | Proposition 23, which relies on Heunen [Heu10] Lemma 19 and Proposition 9 |
| C8 | In Rel and lbfRel, Frobenius algebras are disjoint unions of abelian groups and satisfy (H) | strong (proof) | Lemmas 26–29 and Theorems 30–32. The element-annotated diagram steps did not survive extraction, and I followed them from the stated relations |
| C9 | In Rel(Q), Q cancellative, Frobenius algebras satisfy (H) | moderate (proof, conditional) | Theorem 35 requires q² = 1 ⇒ q = 1. The unconditional version in Theorem 24 and the abstract is not shown |
| C10 | In Mat_ℓ²(ℝ₊), every summand is a finite abelian group with weight 1/√d, and (H) holds; in Hilb, (H) ⇔ δ has a nonnegative matrix in some basis | strong (proof) | Propositions 36–40 |
| C11 | H*-algebras "provide a categorical way to speak about … quantum observables in arbitrary dimension" (abstract) | weak (interpretive) | Observables are identified with bases throughout and never separately defined. Only discrete spectra are covered, and §6 defers continuous observables and PVMs |

## Method

- **Pose the problem (§2).** A unit gives a compact structure, and Hilb has compact structure only in finite dimension. So the unit goes.
- **Find a substitute axiom (§3).** Curry μ into the regular representation R. Demand that R carry an involution on points to the categorical †, which gives (H). Compare (H) with (F) abstractly (Lemmas 5 and 6, Proposition 7).
- **Identify (H) with Ambrose's H*-algebras in Hilb (§4.1).** Then prove the structure theorem directly by Gelfand theory, with characters = copyables (§4.2). Add categorical, colimit and approximate-unit characterisations (§§4.3–4.4).
- **Localise the gap (§4.5).** Split off the semisimple part, leaving a radical remainder.
- **Settle the gap where there is no destructive interference (§5).** Reduce to Rel via the 0-reflecting homomorphism to the Boolean semiring, then weigh the entries by cancellativity or positivity.

## Concepts

- **Frobenius algebra (this paper's sense)** — δ: A → A⊗A satisfying (A), (C), (M), (F). It is commutative and special by definition, and nonunital unless said "unital" (p. 7).
- **Axiom (H)** — there is an a ↦ a∗ on points with R(a∗) = R(a)†. It is a "transfer of variables" (§3.2).
- **H*-algebra** — Ambrose's (1945) Banach algebra on a Hilbert space with adjoint multiplication operators. It is *proper* if it has no nonzero annihilator. It is not Baez's 2-H*-algebra (footnote 3).
- **Admits the structure theorem** — it is coalgebra-isomorphic to a Hilbert direct sum of copies of (ℂ, 1 ↦ 1⊗1). This is the paper's precise form of "corresponds to an orthonormal basis".
- **Copyable** — a point with δ(a) = a⊗a. It is also called primitive (Hofmann) or grouplike (Hopf algebras) (footnote 6). By †, copyables are the characters, i.e. the Gelfand spectrum.
- **Semisimple / radical** — Jacobson radical zero, versus the algebra equalling its radical. The radical is the intersection of the maximal regular ideals (p. 18).
- **Destructive interference** — the paper's informal name for the presence of cancelling (non-positive) matrix entries. §5 proves everything positive exactly where it is absent.

## Connections

- **[LIT-274](../literature.d/LIT-274.md) (Coecke, Pavlovic & Vicary, read in [NOTE-247](NOTE-247.md)).** This paper is the direct continuation.
  - *What it takes from CPV.* Lemma 5, "the central idea in their proof" (p. 8), and Proposition 15, which is CPV's Cor. 4.7.
  - *What it restates.* "Theorem 1 [CPV09]" is the *special/orthonormal* form, i.e. CPV §6, because (M) is built into the definition here. CPV's orthogonal Theorem 5.1 has only footnote 5 as its infinite-dimensional analogue.
  - *A different proof route.* CPV go through finite-dimensional C*-algebras and their spectral theorem. This paper goes through Gelfand theory for commutative *Banach* algebras and Ambrose's H*-algebras. It also remarks that CPV's result already follows from Abrams's thesis plus Proposition 15.
  - *The same notion of basis.* In both papers a basis is fixed exactly, phases included.
- **GNS and C*-algebras ([LIT-241](../literature.d/LIT-241.md), [THEORY-004](../theory.d/THEORY-004.md)).** The paper never mentions GNS, states or representations of C*-algebras. Its algebra is H itself, made into a Banach algebra by μ. The C*-identity plays no role. The analytic tools are the Gelfand spectrum, the Gelfand transform and the Jacobson radical of commutative Banach algebras (§4.2, citing Pedersen). So it runs parallel to the GNS strand, and does not pass through it.
- **Carroll ([LIT-123](../literature.d/LIT-123.md)).** Carroll sets non-separable spaces aside because there "an algebra of observables" must be supplied (Haag, p. 5). This paper's results hold in Hilb of arbitrary dimension, non-separable included. Only Theorem 21 assumes separability, because it uses sequences. What it supplies in every dimension is, again, an algebra on the space: a basis *is* an H*-algebra structure. So it is consistent with Carroll's remark, and does not engage Haag's issue.
- **Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md)) and DisCoCat ([LIT-272](../literature.d/LIT-272.md), [LIT-273](../literature.d/LIT-273.md)).** There is no direct connection. All three work in finite dimension, and [LIT-272](../literature.d/LIT-272.md)'s stipulated Frobenius algebra is the unital finite case this paper starts from. For the real scalars of those corpus spaces, see Bearing on the record.
- **Later work (verified by search, abstract only, not read).** Poinsot, "Hilbertian Frobenius algebras", arXiv 2003.04149 (v1, 6 Mar 2020). Its abstract claims three things:
  - that commutative Hilbertian Frobenius algebras split as the Jacobson radical (= the annihilator) ⊕ the closed span of the grouplikes;
  - that "every commutative special Hilbertian algebra, that is, with a coisometric multiplication, is semisimple";
  - that such Frobenius structures on a given Hilbert space are in one-to-one correspondence with its "bounded above orthogonal sets".

  If this holds, it answers this paper's §4.5 question positively in Hilb: (M) makes the radical zero. Also see Heunen & Reyes, "Frobenius structures over Hilbert C*-modules", arXiv 1704.05725 (abstract only), for a C*-module generalisation. Both results are unverified here.
- **Anthology.** Nothing in the Anthology of the SOTA concerns Frobenius algebras, H*-algebras or classical structures. Every "Frobenius" there is the matrix norm or Perron–Frobenius. No ANTH- citation is warranted.

## Bearing on the record

- **[THEORY-017](../theory.d/THEORY-017.md)'s infinite-dimensional boundary: what this paper settles.**
  - *Exact objects.* The category is Hilb, complex Hilbert spaces of *any* dimension, separable or not, with bounded maps.
    - *The Frobenius notion.* A (nonunital) Frobenius algebra is δ: A → A⊗A with coassociativity (A), commutativity (C), speciality (M) δ†δ = id, and the Frobenius law (F). No unit is assumed. "Quasi-special" is not a notion in this paper. Speciality is always imposed, and that is what forces unit-norm copyables (Proposition 14).
    - *An H*-algebra.* It is Ambrose's: a Banach algebra on a Hilbert space in which each left and right multiplication operator has an adjoint of the same kind, ⟨xy | z⟩ = ⟨y | x∗z⟩. Categorically this is axiom (H).
  - *Main theorem (Theorem 22).* A Frobenius algebra in Hilb is induced by an orthonormal basis, via |i⟩ ↦ |ii⟩ with the basis being exactly its nonzero copyables, **iff** it satisfies (H), iff it is semisimple, iff it is a directed colimit of finite-dimensional unital ones. The separable case adds an approximate-unit condition.
    - *The H*-algebra case.* Commutative (proper) H*-algebras ↔ orthonormal bases holds in every dimension (Ambrose, Theorem 12). The correspondence is exact at the level of vectors, phases included, as in [LIT-274](../literature.d/LIT-274.md).
  - *What fails in infinite dimension, exactly.*
    - *The unit.* There is no unit: ε: |i⟩ ↦ 1 is unbounded, Σᵢ|i⟩ does not converge, and Lemma 3 says unital ⇔ finite-dimensional. So there is no unital Frobenius algebra and no compact (self-dual) structure η = δ∘ε†.
    - *Bases that survive.* The copying map survives, and so every orthonormal basis still gives a Frobenius algebra (bounded, indeed isometric, δ).
    - *The open converse.* The converse is not known from this paper. A Frobenius algebra might carry a nonzero radical summand R with no copyables (Proposition 23), and then it would not be a basis. The paper leaves open whether such an R exists. Poinsot's 2020 abstract (unread) claims that speciality rules it out.
  - *Norm conditions.* Under (M), every copyable has norm exactly 1, so only orthonormal bases arise. Without (M) (footnote 5, a sketch), one gets orthogonal bases, and the paper states no norm condition.
    - *My own derivation, not the paper's.* If δ(uᵢ) = nᵢ·uᵢ⊗uᵢ on an orthonormal uᵢ, the copyables are aᵢ = nᵢuᵢ with ‖aᵢ‖ = nᵢ. Then ‖δ‖ = supᵢ nᵢ, so a *bounded* δ requires the copyables' norms to be **bounded above**. Nothing requires them to be bounded below: monic δ needs only nᵢ > 0.
    - *Corroboration.* This matches the phrase "bounded above orthogonal sets" in Poinsot's abstract (unread).
    - *What does not enter.* No trace-class or Hilbert–Schmidt condition appears in the paper. Unbounded operators do not appear either: all maps are bounded by the choice of Hilb.
  - *Relation to CPV ([LIT-274](../literature.d/LIT-274.md)).* The orthonormal (special) form of CPV is recovered as a special case: Lemma 5 gives (U) + (F) ⇒ (H), and then Theorem 22 applies (p. 18). CPV's orthogonal Theorem 5.1 is recovered only in footnote 5's sketch. No GNS construction is used. There are no C*-algebras beyond the mention of CPV's route. The tool is Gelfand duality for *commutative Banach* algebras (characters = copyables, semisimple ⇔ Gelfand transform injective), plus Ambrose.
  - *Real versus complex.* The paper works over ℂ throughout and never discusses real Hilbert spaces. The only "real" item is its citation of Ingelstam's "Real algebras with a Hilbert space structure", used for automatic continuity (p. 12). The §5.4 remark that "group algebras over the rationals are isomorphism invariants of groups" also cites [Ing65], and that attribution looks misplaced (unverified).
    - *The equivalences fail over ℝ (my own check, numerical).* On ℝ², [THEORY-017](../theory.d/THEORY-017.md)'s example (ℂ as an ℝ-algebra, multiplication scaled by 1/√2) satisfies (A), (C), (M), (F) *and* (H), with a∗ = conjugate. It is semisimple, and has no nonzero copyable.
    - *A second, sharper example.* The real group algebra ℝ[ℤ/3] with weight 1/√3 is exactly the §5 nonnegative-matrix form of Proposition 37. It satisfies (A), (C), (M), (F) and (H), with a∗ = a⁻¹ on group elements. Yet over ℝ it has exactly one nonzero copyable, (1,1,1)/√3, in three dimensions. Over ℂ it has three, the Fourier characters.
    - *Consequence.* Over ℝ, Theorem 22's (c) and (d) and Proposition 40 do *not* imply (a). [THEORY-017](../theory.d/THEORY-017.md)'s real-scalar caveat therefore extends unchanged to infinite dimension. Nothing in this paper lifts it.
  - *Carroll's non-separable remark.* It is consistent with this paper and not contradicted. Theorem 22 needs no separability, apart from (f). So a *discrete* basis of a non-separable space is still captured algebraically, but only by supplying an algebra (an H*-algebra) on the space. That is precisely "extra data".
    - *What is still missing.* Continuous observables (position, momentum, PVMs) have no eigenbasis. The paper explicitly leaves them for later: "Beyond this lie continuous observables and projection-valued measures" (§6). That is the regime where Haag-type arguments and algebras of observables live. As my own gloss, R(A) is a commutative algebra of diagonal operators, whose weak closure is an *atomic* maximal abelian algebra. Continuous observables correspond to non-atomic ones, which this framework does not reach.
  - *Verdict for [THEORY-017](../theory.d/THEORY-017.md).* The bullet should be *narrowed, not kept as is*.
    - *What changes.* The basis-as-algebra identification, and so "a basis is extra structure supplied as an algebra", extends to discrete orthonormal bases in any dimension, separable or not, provided the algebra is taken nonunital and with (H). It has always been known that the unit (and the compact structure) fails beyond finite dimension. Whether (H) is automatic was open in this paper.
    - *What still falls outside.* Continuous observables, and Carroll's algebra-of-observables regime.
    - *The table.* It stays finite-dimensional, because its sources are.
    - *Proposed exact rewording of the bullet:*

      "- **Anything about continuous observables, or about infinite-dimensional spaces beyond discrete bases.** Abramsky & Heunen (the LIT for arXiv 1011.6123) show that a Frobenius algebra with a unit exists in Hilb only in finite dimension (Lemma 3). Dropping the unit, they prove that on a complex Hilbert space of any dimension, separable or not, a commutative special †-Frobenius algebra is induced by an orthonormal basis exactly when it satisfies Ambrose's H*-axiom, equivalently when it is semisimple (Thm 22). So a discrete basis is still extra structure supplied as an algebra on the space, in any dimension. Whether the H*-axiom is automatic was open there. Continuous observables, which have no eigenbasis, are outside that result (its §6), and there, Carroll notes, an algebra of observables must be supplied from the start (Haag, [LIT-123](../literature.d/LIT-123.md) p. 5). That is the setting of the GNS strand ([LIT-241](../literature.d/LIT-241.md), [THEORY-004](../theory.d/THEORY-004.md)). This document's table stays finite-dimensional, as its sources are, and the real-scalar caveat above holds in every dimension."
- **[THEORY-017](../theory.d/THEORY-017.md)'s two marked inferences.** The paper says nothing about probability distributions, contextuality or projection lattices. The only lattice remark is the proof of Theorem 16's necessity: the ideal lattice of ⊕ℂ is "a complete atomic boolean algebra". That is consistent with the Boolean-structure inference, now in arbitrary dimension, but it is not stated as such.
- **[NOTE-247](NOTE-247.md).** Its Connections entry for this paper ("the infinite-dimensional case, where Frobenius algebras must drop the unit") is accurate. It can now be made precise as above.
- **ML practice.** It carries nothing. This is operator algebra and category theory about bases, and it does not belong in the Anthology.
- **For filing.**
  - *Tags proposed.* `mathematics` first. Nearly all the content is algebra and functional analysis: Ambrose, Gelfand, Wedderburn, semigroups, quantales. `quantum-foundations` second, since the paper is framed as axiomatising observables in categorical quantum mechanics (abstract, §§1, 2.2, 6). This matches [LIT-274](../literature.d/LIT-274.md).
  - *Tags not proposed.* `logic`: there is no quantum logic here. `contextuality`: not addressed; complementarity is only listed as future work (§6).
  - *Candidate follow-up.* Poinsot 2020 (arXiv 2003.04149), which appears to close the main question.

## Limitations

- **The central question is open.** Theorem 22 characterises when a nonunital Frobenius algebra is a basis, not that it always is. As the paper stands, "nonunital Frobenius algebra = orthonormal basis" in infinite dimension is *not* established. The paper says so (§§4.5, 6).
- **The load-bearing steps rest on citations.** Ambrose's structure theorem and his semisimplicity result (Theorem 12, Proposition 17) are cited, not reproved. So are Kaplansky and Kock for Lemma 3, Carboni for Proposition 7, and Heunen [Heu10] for Proposition 23's splitting. Theorem 16's direct proof is complete for sufficiency, and its necessity is a one-sentence argument.
- **Complex, discrete and bounded only.** Real scalars are never considered, and the equivalences fail there (my examples above). Continuous spectra, PVMs and unbounded operators are out of scope (§6).
- **Orthogonal (non-special) bases get only a footnote.** Footnote 5 is a sketch with no norm condition, although boundedness of δ forces the norms to be bounded above.
- **The abstract says more than the body in two places.** "Always coincide in categories of generalized relations" needs Theorem 35's hypothesis q² = 1 ⇒ q = 1. "Arbitrary bases and observables" (the arXiv listing) means orthonormal bases and discrete observables.
- **Slips.**
  - *Proposition 11.* It omits (C) from its statement.
  - *Theorem 20's proof.* It cites "Lemma 13" for Proposition 13, and writes "m: X → X′" for A → A′.
  - *p. 18.* It says Lemma 5 "shows that the algebra is C*", when Lemma 5 gives (H).
  - *Hilb inside Mat_ℓ²(ℂ).* §2 calls Hilb equivalent to a "(nonfull) subcategory" of Mat_ℓ²(ℂ), and §5.4 calls it a "full subcategory".
  - *Theorem 35.* It has no separate proof. It rests on Proposition 34 and one sentence.

## Open questions

- **Does (F) imply (H) given (A), (C) and (M)?** Equivalently, is there a nonzero radical commutative special †-Frobenius algebra in Hilb (§4.5, Proposition 23)? Poinsot 2020's abstract claims a negative answer on radicals, which is a positive answer to the question. Reading it would close the gap and would license dropping "Whether the H*-axiom is automatic was open there" from the proposed [THEORY-017](../theory.d/THEORY-017.md) wording.
- **The general question** in arbitrary symmetric monoidal †-categories, and whether Frob(Hilb) ≃ HStar(Hilb) (§4.3).
- **Real Hilbert spaces.** What do these algebras classify there? My ℝ[ℤ/3] and ℂ-over-ℝ examples suggest Hilbert sums of ℝ and ℂ factors, the real H*-algebra picture of Ingelstam. That is unverified against the literature.
- **Continuous observables and PVMs, and complementary observables in infinite dimension (§6).** Is there a categorical notion of observable not tied to tensor-product copying? The paper itself warns against "concluding over-hastily that a particular approach is canonical" (p. 26).
- **The computational complexity** of finding the decomposition isomorphism of a finite abelian group algebra (footnote 7).

## Corrections to the seeded skim

- none (there was no seed or dossier)
- **Identification note for filing.** The journal-ref is "Clifford Lectures, AMS Proceedings of Symposia in Applied Mathematics 71:1--24, 2012". I verified via Crossref the DOI 10.1090/psapm/071/599. Crossref gives the container as *Proceedings of Symposia in Applied Mathematics*, volume title *Mathematical Foundations of Information Flow*, AMS 2012, pp. 1–24. The arXiv category is quant-ph. The affiliation on the PDF is Oxford University Computing Laboratory.
- **The arXiv listing's abstract and the v3 PDF's abstract differ.** The listing says the generalisation "will allow arbitrary bases and observables to be described". The PDF says "arbitrary bases, and therefore observables with discrete spectra". The body supports only the narrower reading. "Arbitrary" means orthonormal bases in arbitrary dimension (§§2.3, 4), not non-orthogonal ones. Observables are never defined separately from bases. Continuous observables are explicitly left for later (§6).
- **The abstract says H*-algebras and nonunital Frobenius algebras "always coincide in categories of generalized relations".** The body proves this for Rel and lbfRel (Theorems 31, 32) and for Mat_ℓ²(ℝ₊) (Theorem 38). For relations valued in a cancellative quantale Q, it proves it only when "q² = 1 implies q = 1 in Q" (Theorem 35). Otherwise the entries are square roots of unity ("we can choose square roots of unity for the entries", p. 24), and (H) is not shown. Theorem 24's summary statement ("in all these categories") omits that hypothesis.
- **The paper's "Theorem 1 [CPV09]" is the orthonormal/special version of [LIT-274](../literature.d/LIT-274.md), not its main theorem.** Here the definition of a Frobenius structure builds in (M), δ†∘δ = id, i.e. speciality (§2.1 and footnote 1). So "orthonormal bases … in one-to-one correspondence with dagger Frobenius structures" is CPV's §6 refinement. CPV's Theorem 5.1, orthogonal bases ↔ commutative †-Frobenius algebras without speciality, appears here only as footnote 5's infinite-dimensional sketch.
