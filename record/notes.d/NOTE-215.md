---
number: 215
status: Skimmed
formerly:
- NOTE-tmpm9f7j
paper: LIT-237
title: 'Bra–ket notation (Wikipedia)'
version: 1
date: '2026-09-26'
summary: >-
  Dirac's bra–ket notation writes vectors as kets and continuous linear functionals as bras, and on a Hilbert space the Riesz representation theorem is what licenses treating every bra as the conjugate of a ket, so that ⟨φ|ψ⟩ is at once a functional applied to a vector and an inner product.
---
<!-- inactive-ok-file: LIT-237 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-215: Bra–ket notation (Wikipedia)

## Contribution

The article describes the notation Paul Dirac introduced in 1939 for vectors, dual vectors and linear operators on complex vector spaces, now standard in quantum mechanics. Kets |ψ⟩ are vectors, bras ⟨φ| are linear functionals, and their juxtaposition is the bracket ⟨φ|ψ⟩. It covers operators acting on either side, outer products |ψ⟩⟨φ|, Hermitian conjugation, resolution of the identity over an orthonormal basis, common pitfalls, and the mathematicians' translation of the notation.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §"Inner product and bra–ket identification on Hilbert space": identifying a ket with a bra relies explicitly on the Riesz representation theorem; the bracket is defined as the functional f_φ applied to ψ.
- §"Non-normalizable states and non-Hilbert spaces": physicists routinely write kets with infinite norm (delta functions, plane waves) that are not in the Hilbert space; the article points to rigged Hilbert spaces and the GNS construction, and says that on a Banach or untopologized space the bracket is not an inner product "because the Riesz representation theorem does not apply".
- §"Outer products" and §"The unit operator": Σ_i |e_i⟩⟨e_i| = I over a complete orthonormal system — the notation's compact form of basis expansion and projection.
- §"Pitfalls and ambiguous uses": reuse of symbols and operations inside bras/kets are flagged as sources of error.
- §"Notation used by mathematicians": the embedding Φ: H → H*, h ↦ ⟨h,·⟩ (antilinear), i.e. the Riesz map under another name.

## Open questions

- For representation learning its contribution is notational, not substantive: ⟨x|y⟩ as a similarity, |ψ⟩⟨ψ| as a rank-one projector, and Σ|e_i⟩⟨e_i| as a resolution of identity are a clean vocabulary for kernels, Gram matrices and spectral truncations (a rank-k spectral embedding is Σ_{i≤k} λ_i |e_i⟩⟨e_i|).
- It makes the owner's question sharp: bra–ket notation is only honest where Riesz holds, so if the readings use it, Riesz is being used implicitly.
- Wikipedia with a reorganisation banner; do not cite it for anything beyond definitions.
