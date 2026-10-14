---
status: Read
paper: LIT-237
title: 'Bra–ket notation (Wikipedia)'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the article's wikitext (en.wikipedia.org,
    action=raw, 43,401 bytes), every section, note and reference. The
    current revision is oldid 1377684197 of 2026-09-30 (from the page
    history on 2026-10-14; the MediaWiki API was rate-limited). It differs
    from the revision the seed skimmed (1376620925, 2026-09-25) in one
    sentence of the lead, checked by diffing the two raw texts. Replaces
    the seeded skim NOTE-215.
date: '2026-10-14'
summary: >-
  Dirac's notation writes vectors as kets and linear functionals as bras.
  On a Hilbert space the inner product, antilinear in its first slot,
  turns each ket into a bra, and the article cites the Riesz theorem for
  the reverse direction; on a Banach or untopologized space the bracket is
  only a functional applied to a vector, because Riesz does not apply. The
  article is a reference with internal inconsistencies, including an
  unsourced edit of 2026-09-30 to the date of the notation's origin.
---
<!-- inactive-ok-file: NOTE-215 — Superseded; the seeded skim this reading replaces -->

# NOTE-tmp5cyxp: Bra–ket notation (Wikipedia)

## Contribution

A reference article on Dirac's notation. It covers kets and bras, the
ket–bra identification on Hilbert space, row and column vectors,
non-normalizable kets, operators acting on either side, outer products
and projectors, Hermitian conjugation rules, tensor products, the
resolution of the identity, and a translation into mathematicians'
notation. It adds no result.

## Key insight

A bra is a functional and a ket is a vector. Writing ⟨φ|ψ⟩ as both "a bra
applied to a ket" and "an inner product" is legitimate only where every
continuous functional comes from a vector, which is a Hilbert space. The
article says so in two places: in the identification section, with a
pointer to the Riesz theorem, and in the Banach-space paragraph, where
"the bracket does not have the meaning of an inner product, because the
Riesz representation theorem does not apply".

## Assumptions

- **Physicists' convention.** The inner product (·, ·) is antilinear in
  its first argument, so (φ, ·) ≡ ⟨φ| is linear.
- **Complex spaces throughout,** finite- or infinite-dimensional, with the
  separable complex Hilbert space as the setting of quantum mechanics.

## Key results

The article states conventions and standard facts, not theorems:

- **Identification (§Inner product and bra–ket identification).** For a
  ket ψ and a vector φ, (φ, ψ) =: f_φ(ψ) =: ⟨φ|ψ⟩. Each ket thus gives a
  bra; that every bra comes from a ket is left to the cited Riesz
  theorem. The set of covectors ⟨φ| is called "a subspace of the dual
  vector space", which on a Hilbert space is the whole continuous dual.
- **Matrices.** On ℂⁿ with a fixed orthonormal basis, ⟨A|B⟩ = Σ A_i* B_i,
  bras are rows, kets are columns, and the bra of a ket is its conjugate
  transpose. If A is an N × N matrix, A† is its conjugate transpose.
- **Non-normalizable states.** Kets of infinite norm (delta functions,
  plane waves) are not in the Hilbert space; the article points to the
  GNS construction and to rigged Hilbert spaces as broadenings.
- **Outer product.** (|φ⟩⟨ψ|)(x) = ⟨ψ|x⟩|φ⟩ is rank one, and for a unit ψ,
  |ψ⟩⟨ψ| is the orthogonal projection onto span{ψ}.
- **Associativity** holds for expressions in numbers, bras, kets,
  operators and products, but not with antilinear operators such as time
  reversal.
- **Hermitian conjugation rules.** Reverse the order and conjugate each
  factor: ⟨φ|ψ⟩* = ⟨ψ|φ⟩, ⟨φ|A|ψ⟩† = ⟨ψ|A†|φ⟩.
- **Unit operator.** For a complete orthonormal system,
  |ψ⟩ = Σ_i ⟨e_i|ψ⟩|e_i⟩ and Σ_i |e_i⟩⟨e_i| = 𝕀, with the continuous
  forms ∫dx |x⟩⟨x| = ∫dp |p⟩⟨p| = 𝕀 and ⟨x|p⟩ = e^{ixp/ℏ}/√(2πℏ).
- **Mathematicians' notation.** Φ : H → H*, Φ(h) = φ_h with
  φ_h(g) = ⟨h, g⟩ = ⟨h|g⟩, "the embedding".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | On a Hilbert space the bracket is both a functional applied to a vector and an inner product, and the identification of bras with kets rests on the Riesz theorem | moderate | stated with a pointer to the Riesz article, not proved |
| C2 | On a Banach or untopologized space bras and kets can still be written, but the bracket is not an inner product | moderate | stated, one paragraph |
| C3 | Σ_i \|e_i⟩⟨e_i\| is the identity for a complete orthonormal system | moderate | stated as a consequence of the basis expansion; convergence in which topology is not said |

## Concepts

- **Ket |v⟩.** A vector of a complex vector space; physically a state.
- **Bra ⟨f|.** A linear form f : V → ℂ.
- **Covector to |φ⟩.** The bra ⟨φ| = (φ, ·) obtained from the inner
  product.
- **Generalized eigenvector.** A position or momentum "eigenket" such as
  |r⟩, which is not an element of the Hilbert space.

## Connections

The bra–ket section of the Riesz article ([LIT-230](../literature.d/LIT-230.md)) does the same
identification in the opposite convention (⟨y | x⟩ := ⟨x, y⟩, with the
representer in the antilinear slot) and proves it. The article names
Grassmann's [φ|ψ] (1862) as a precursor. Its pointer to GNS
([LIT-241](../literature.d/LIT-241.md)) for non-normalizable states is discussed below.

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cites this article.** [NOTE-239](NOTE-239.md) names it
  as the notation van Rijsbergen's book uses in its ch. 6.
- **The seed's summary needs one correction.** [LIT-237](../literature.d/LIT-237.md) says Dirac
  "introduced" the notation in 1939. The current lead says it was
  "created by Paul Dirac in his monograph, 'The Principles of Quantum
  Mechanics' published by Oxford University 1930", while its footnote
  still cites Dirac (1939), "A new notation for quantum mechanics", and
  a later paragraph still says the notation "was effectively established
  in 1939". The 1930 sentence came in an anonymous edit of 2026-09-30
  with the summary "When BRA KET notation was first created", replacing
  "created by Paul Dirac in his paper, 'A New Notation for Quantum
  Mechanics' from 1939". The record should keep 1939, from the reference
  the article actually gives, and not cite the lead.
- **The GNS pointer is weak.** The article says the definition of Hilbert
  space "can be broadened to accommodate" non-normalizable kets, citing
  the GNS construction or rigged Hilbert spaces. Rigged Hilbert spaces
  do that. GNS builds a Hilbert space from a state on a C*-algebra and
  does not house delta-function kets; the GNS article ([LIT-241](../literature.d/LIT-241.md)) says
  nothing about them. The record should not cite this article for a GNS
  treatment of improper states.
- **Two internal inconsistencies, worth knowing before citing it.**
  - The "Pitfalls" section says |ψ⟩† = ⟨ψ| is "not correct in a
    technical sense", while the "Hermitian conjugation" section uses
    exactly that as its first formal rule.
  - In "Notation used by mathematicians", φ_h(g) = ⟨h, g⟩ is linear in g
    only if the mathematicians' inner product is linear in its second
    slot, but the next paragraph says mathematicians put the conjugate
    on the second slot (⟨φ, ψ⟩ = ∫ φ conj ψ). Under that convention the
    embedding should be h ↦ ⟨·, h⟩, as in [LIT-230](../literature.d/LIT-230.md).
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Wikipedia, under a "Cleanup reorganize" banner dated February 2023, and
  revised as recently as 2026-09-30. Cite it for conventions at most.
- The resolution of the identity is stated without saying in what sense
  the infinite sum converges (strongly, not in operator norm), and the
  continuous forms are formal.
- Unbounded operators (position, momentum) appear without domains.

## Open questions

- None the article can settle. The rigged-Hilbert-space treatment of
  improper kets would need its own source if the record ever leans on it.
