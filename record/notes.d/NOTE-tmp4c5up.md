---
status: Read
paper: LIT-243
title: 'Adler — Hilbert spaces and the Riesz representation theorem'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the 15-page PDF on math.uchicago.edu (HTTP 200 on
    2026-10-14), text extracted with pdftotext -layout: abstract, §§1–5,
    the appendix, acknowledgments and references, every statement and
    proof. Pages 7 and 12 were rendered as images to read the complex
    conjugates in Thm 3.5's proof and Thm 4.9, which the text layer
    drops. Replaces the seeded skim NOTE-206.
date: '2026-10-14'
summary: >-
  An undergraduate expository proof, twice over, that every continuous
  linear functional on a Hilbert space is v ↦ ⟨u, v⟩ for a unique u with
  ‖u‖ = ‖φ‖: once from the projection theorem, once as
  u = Σ_k conj φ(e_k) e_k over any orthonormal basis, with
  ‖φ‖² = Σ_k |φ(e_k)|². It ends with von Neumann's proof of the
  Radon–Nikodym theorem for finite positive measures by applying Riesz to
  f ↦ ∫ f dν on L²(ν + μ).
---
<!-- inactive-ok-file: NOTE-206 — Superseded; the seeded skim this reading replaces -->

# NOTE-tmp4c5up: Adler — Hilbert spaces and the Riesz representation theorem

## Contribution

No new result; a careful from-scratch exposition by an REU student
(mentor Jake Fiedler), following Axler, Rudin and Stein–Shakarchi. It
builds inner products, norms, Hilbert spaces and orthogonal projection,
proves the Riesz representation theorem, proves it again constructively
through orthonormal bases, and derives the Radon–Nikodym theorem from it.

## Key insight

The first proof finds the representer as a multiple of a unit vector
normal to ker φ, and the author says it "seems to fall from the sky". The
second proof removes the mystery: expand in any orthonormal basis and the
representer's coefficients are the conjugated values of φ on the basis,
so Riesz is the infinite-dimensional version of the finite-dimensional
dual-basis computation of §3.

## Assumptions

- **Convention.** The inner product is linear in its second argument and
  conjugate-linear in its first (Def. 1.1), the opposite of [LIT-230](../literature.d/LIT-230.md). So
  the theorem reads φ(v) = ⟨u, v⟩.
- **Completeness.** Used once, in the Hilbert projection theorem (Thm
  2.2), where the minimizing sequence converges ("only here do we invoke
  the completeness of the space").
- **Choice.** Orthonormal bases exist by Zorn's lemma (§4); the
  construction is explicit only where a basis can be built (Gram–Schmidt
  in the separable case, footnote 11).
- **Radon–Nikodym** is proved for finite positive μ and ν with ν ≪ μ; the
  σ-finite, signed and complex cases are said to follow from monotone
  convergence and the Hahn decomposition, not proved.

## Key results

- **Thm 1.5 (Cauchy–Schwarz)**, with equality iff the vectors are
  dependent; **Thm 1.8 (parallelogram law).**
- **Thm 2.2 (Hilbert projection theorem).** In a Hilbert space the
  distance to a nonempty closed convex set is attained at a unique point.
  For a closed subspace U, v − v_U ⊥ U, the decomposition is unique, and
  (U^⊥)^⊥ = U. A subspace is dense iff its orthogonal complement is {0}.
- **§3, finite dimensions.** With the dual basis, φ ↦ φ′ = Σ conj(φ_i) e_i
  is conjugate-linear and isometric, and φ(v) = ⟨φ′, v⟩ for any
  orthonormal basis.
- **Thm 3.5 (Riesz).** For continuous linear φ on a Hilbert space V there
  is a unique u with φ(v) = ⟨u, v⟩ for all v, and ‖u‖ = ‖φ‖. Proof: take
  a unit w ⊥ ker φ and u = conj φ(w) w.
- **Thms 4.5–4.8.** An orthogonal family is summable iff the squared
  norms are (an "infinite Pythagorean theorem"); Bessel's inequality;
  the closed span of an orthonormal set is
  {Σ α_k e_k : Σ |α_k|² < ∞}, and v = Σ ⟨e_k, v⟩ e_k.
- **Thm 4.9 (Riesz again).** For bounded φ and any orthonormal basis
  {e_k}, u = Σ_k conj φ(e_k) e_k satisfies φ(v) = ⟨u, v⟩, and
  ‖φ‖ = ‖u‖ = (Σ_k |φ(e_k)|²)^{1/2}.
- **Thm 5.1 (Radon–Nikodym).** If μ, ν are finite positive measures on
  the same σ-algebra and ν(A) = 0 whenever μ(A) = 0, there is a
  measurable h with ν(A) = ∫_A h dμ. Proof: φ(f) = ∫ f dν is bounded on
  L²(σ), σ = ν + μ, so ∫ f dν = ∫ f g dσ for some g; hence
  ∫ f(1 − g) dν = ∫ f g dμ (eq. 5.2); indicators show 0 ≤ g < 1 almost
  everywhere; truncations f_k of 1/(1 − g) and monotone convergence give
  h = g/(1 − g).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every continuous linear functional on a Hilbert space is the inner product with a unique vector of equal norm | strong | Thm 3.5, full proof |
| C2 | The representer is Σ_k conj φ(e_k) e_k in any orthonormal basis, and ‖φ‖² = Σ_k \|φ(e_k)\|² | strong | Thm 4.9, full proof |
| C3 | The Radon–Nikodym theorem for finite positive measures follows from Riesz applied on L²(ν + μ) | strong | Thm 5.1, full proof |
| C4 | The extension to σ-finite, signed and complex measures is routine | weak | asserted in one sentence, not proved |

## Concepts

- **Unordered sum.** L is the sum of a family if every ε has a finite Ω
  with every finite Ω′ ⊇ Ω within ε of L (Def. 4.4).
- **Orthonormal basis.** A maximal orthonormal set; its span is dense,
  not all of the space (the ℓ² example with a_i = 2^{-i}).
- **Standard isomorphism.** The conjugate-linear isometry V′ → V of §3.

## Connections

The Wikipedia article ([LIT-230](../literature.d/LIT-230.md)) gives the same theorem, the same
orthonormal-basis formula and a different convention. The Radon–Nikodym
derivative proved here is the object MINE's Donsker–Varadhan dual is tight
at ([NOTE-828](NOTE-828.md), [LIT-256](../literature.d/LIT-256.md)); this paper's proof is von Neumann's.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cites this paper.** Readings name it as
  the record's secondary account of Riesz ([NOTE-289](NOTE-289.md), [NOTE-239](NOTE-239.md),
  [NOTE-828](NOTE-828.md)).
- **The seed's summary needs one correction.** [LIT-243](../literature.d/LIT-243.md) and the skim say
  the representer is "the sum of φ(e_k)e_k". The paper writes
  Σ_k conj φ(e_k) e_k (p. 12; the bar is lost in the text layer). The two
  agree on real spaces only.
- **Cite it for what [NOTE-289](NOTE-289.md) wants.** It proves uniqueness and the
  isometry for arbitrary Hilbert spaces, and gives the basis formula. It
  says nothing about kernels, RKHS or factorisation, as the skim noted.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Student expository work. Correct as read, but cite a textbook (Axler,
  Rudin, Stein–Shakarchi) for anything leaned on.
- Typographical slips:
  - Thm 4.8 writes "span(e_Ψ) = Σ α_k e_k" for the closure of the span.
  - In the projection-theorem proof one term lacks its factor 2
    ("2‖p − q_m‖² + ‖p − q_n‖²").
  - In the proof of Thm 4.9, "⟨u, e_k⟩ = φ(e_k)" is right under its
    convention only because u carries the conjugated coefficients.
- The Radon–Nikodym proof is for finite measures; the general case is
  only asserted.

## Open questions

- None the paper raises. Whether the record needs the σ-finite
  Radon–Nikodym theorem in full would decide whether a textbook source is
  wanted.
