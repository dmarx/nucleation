---
number: 861
status: Read
formerly:
- NOTE-tmprvqbi
paper: LIT-230
title: 'Riesz representation theorem (Wikipedia)'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the article's wikitext (en.wikipedia.org,
    action=raw, 76,482 bytes), every section including the collapsed
    proofs, the notes and the proof footnotes. The revision is oldid
    1345571927 of 2026-03-26T20:59:01Z, confirmed through the MediaWiki
    API as the latest on 2026-10-14, so it is the same revision the seed
    skimmed. Replaces the seeded skim NOTE-214.
date: '2026-10-14'
summary: >-
  On a real or complex Hilbert space every continuous linear functional φ
  is x ↦ ⟨x, f_φ⟩ for a unique f_φ, with ‖f_φ‖ = ‖φ‖; the map y ↦ ⟨·, y⟩
  is an antilinear isometric bijection H → H*. Completeness is used only
  to split H = ker φ ⊕ (ker φ)^⊥. The article then defines the adjoint of
  a bounded operator between Hilbert spaces through this bijection, and
  shows it is the transpose read through the two Riesz maps.
---
<!-- inactive-ok-file: NOTE-214 — Superseded; the seeded skim this reading replaces -->
<!-- inactive-ok-file: THEORY-009 — Proposed; the account that cites this article, named for what the article does and does not support -->

# NOTE-861: Riesz representation theorem (Wikipedia)

## Contribution

A reference article, not a research contribution. It states and proves
the Riesz (Riesz–Fréchet, 1907) representation theorem for real and
complex Hilbert spaces with careful linear/antilinear bookkeeping. It
gives four constructions of the representing vector and uses the theorem
to define the canonical inner product on H*, the bra and ket of a
functional, and the adjoint of a bounded operator, and to restate
self-adjoint, normal and unitary operators in terms of functionals.

## Key insight

On a Hilbert space a continuous linear functional is the same thing as a
vector: the one normal to its level sets, of length equal to the
functional's norm. Everything that needs to move a functional back into
the space, which includes defining the adjoint of a bounded operator,
goes through this identification.

## Assumptions

- **Convention.** ⟨x, y⟩ is linear in the first argument and antilinear
  in the second; the physics bracket is ⟨y | x⟩ := ⟨x, y⟩. The
  representer always sits in the antilinear slot (note
  "ImportanceOfLocationOfRieszRep").
- **Completeness and continuity.** The existence proof uses them only to
  get a nonzero vector in (ker φ)^⊥, through H = K ⊕ K^⊥. The norm
  formula ‖⟨·, y⟩‖ = ‖y‖ holds in any inner-product space.
- **Bounded operators only.** The adjoint section takes A : H → Z to be a
  continuous linear operator between Hilbert spaces. Unbounded operators
  are not treated.

## Key results

- **Statement (§Statement).** For every φ ∈ H* there is a unique
  f_φ ∈ H with φ(x) = ⟨x, f_φ⟩ = ⟨f_φ | x⟩ for all x, and
  ‖f_φ‖_H = ‖φ‖_{H*}. Also f_φ is the unique vector in (ker φ)^⊥ with
  φ(f_φ) = ‖φ‖², and the unique minimum-norm element of
  C = φ^{-1}(‖φ‖²). Any nonzero q ∈ (ker φ)^⊥ is
  q = (‖q‖² / conj φ(q)) f_φ. *Holds when:* H is a real or complex
  Hilbert space.
- **Corollary.** Φ : H → H*, y ↦ ⟨·, y⟩ = ⟨y | ·⟩, is an injective
  antilinear isometry, and the theorem says it is surjective when H is
  complete. ⟨Φh, Φk⟩_{H*} = conj⟨h, k⟩_H = ⟨k, h⟩_H. Over ℝ, Φ is an
  ordinary linear isometric isomorphism.
- **Proof (collapsed, after Rudin 1991 pp. 307–309).** For nonzero p ⊥ ker φ,
  (φh)p − (φp)h ∈ ker φ for every h, which gives
  f_φ = (conj φ(p) / ‖p‖²) p. Uniqueness follows from the norm formula.
  It follows that (ker φ)^⊥ is one-dimensional when φ ≠ 0.
- **Observations.** ‖φ‖ = 1 / inf_{a ∈ φ^{-1}(1)} ‖a‖: the norm of a
  functional is read off its affine hyperplane φ^{-1}(1), whose nearest
  point to the origin is f_φ / ‖φ‖².
- **Constructions of f_φ.**
  - From any nonzero u ⊥ ker φ: f_φ = conj φ(u) u / ‖u‖².
  - From the projection x_K of any x with φ(x) ≠ 0 onto ker φ:
    f_φ = (‖φ‖² / φ(x)) (x − x_K).
  - From any orthonormal basis: f_φ = Σ_i conj φ(e_i) e_i, independent of
    the basis, with ‖f_φ‖² = Σ_i |φ(e_i)|².
  - On ℂⁿ with the standard inner product: Φ and Φ^{-1} are conjugate
    transposition between columns and rows. With ⟨z | w⟩_M = z̄ᵀ M w
    for a Hermitian positive-definite M the formulas change.
- **Real part.** On the underlying real space H_ℝ with
  ⟨x, y⟩_ℝ = Re⟨x, y⟩, the Riesz vector of Re φ equals f_φ.
- **Adjoint (§Definition of the adjoint).** For bounded A : H → Z and
  z ∈ Z, h ↦ ⟨z | Ah⟩_Z is a continuous linear functional on H, "and so
  by the Riesz representation theorem" there is a unique A*z with
  ⟨z | Ah⟩_Z = ⟨A*z | h⟩_H. A* is bounded. In finite dimensions with the
  standard inner product its matrix is the conjugate transpose.
- **Adjoints are transposes.** With ᵗA(ψ) := ψ ∘ A on Z* → H*,
  ᵗA ∘ Φ_Z = Φ_H ∘ A*, so A* = Φ_H^{-1} ∘ ᵗA ∘ Φ_Z.
- **Self-adjoint, normal, unitary.** A = A* iff ⟨z | A(·)⟩ = ⟨Az | ·⟩ for
  all z. A is normal iff the inner products in H* of the functionals
  ⟨Ah | ·⟩ and ⟨h | A(·)⟩ agree pairwise. An invertible A is unitary iff
  ⟨Az | A(·)⟩ = ⟨z | ·⟩ for all z.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every continuous linear functional on a Hilbert space is the inner product with a unique vector of equal norm | strong | standard theorem, proof given (after Rudin) |
| C2 | Completeness enters the existence proof only through H = ker φ ⊕ (ker φ)^⊥ | strong | the proof and its first note |
| C3 | The adjoint of a bounded operator between Hilbert spaces is defined through the Riesz bijection and equals the transpose read through it | strong | §Adjoints and transposes, with proof |
| C4 | In finite dimensions with the standard inner product the adjoint's matrix is the conjugate transpose | strong | stated, standard |

## Concepts

- **Riesz representation (representative) f_φ.** The unique vector with
  φ = ⟨·, f_φ⟩.
- **Anti-dual H̄*.** The continuous antilinear functionals; H → H̄*,
  y ↦ ⟨y, ·⟩, is a linear isometric bijection (the "fundamental theorem
  of Hilbert spaces").
- **Transpose ᵗA.** The algebraic adjoint ψ ↦ ψ ∘ A, defined on any
  normed spaces, with ‖ᵗA‖ = ‖A‖.

## Connections

The theorem is due to Riesz and Fréchet (1907), and the article's proofs
follow Rudin's *Functional Analysis* and Trèves. Its main-article links
send the bra–ket material to the bra–ket article ([LIT-237](../literature.d/LIT-237.md)). Adler's
REU paper ([LIT-243](../literature.d/LIT-243.md)) proves the same theorem twice, the second time by
the orthonormal-basis construction given here. The article separates
itself at the top from the Riesz–Markov–Kakutani theorem about
functionals and measures.

## Bearing on the record

- **[THEORY-009](../theory.d/THEORY-009.md)** cites this article for one sentence: "Riesz is what
  defines the adjoint of a general bounded operator". The article
  supports that exactly (§Definition of the adjoint). Its other clause,
  that for finite matrices and integral operators "the adjoint is the
  transpose, written down directly", is supported for matrices only, as
  the conjugate transpose under the standard inner product. The article
  says nothing about integral operators. That half is the theory's own,
  and true for real square-integrable kernels.
- The article also says why that sentence is weaker than it may look:
  A* = Φ_H^{-1} ∘ ᵗA ∘ Φ_Z. The transpose exists on any normed spaces,
  and Riesz only carries it back into H. So "the adjoint needs Riesz"
  means "turning the transpose into an operator on the same space needs
  Riesz". For a real finite-dimensional inner product the map Φ is the
  identification given by the inner product, which supports
  [THEORY-009](../theory.d/THEORY-009.md)'s reading that nothing beyond the inner product is used
  there.
- The skim's notes on RKHS and kernel methods are the skim's, not the
  article's. The word "reproducing" does not occur, and nothing is said
  about spectra; that self-adjointness gives real spectra and orthogonal
  eigenvectors is not in the article.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- A Wikipedia article: anonymous, revisable, and sourced to textbooks.
  Cite a textbook (Rudin, Trèves, Roman) for anything leaned on.
- Bounded operators only. The adjoint of an unbounded operator, which is
  what quantum observables such as position and momentum need, is not
  covered.
- The real-part section has small typographic slips ("⟨, ·, ·⟩" for
  ⟨·, ·⟩; "is be a proper subspace").

## Open questions

- Whether any reading in the record uses a complex Hilbert space where the
  antilinear bookkeeping matters. If none does, the real statement, an
  honest isometric isomorphism, is all the record needs.
