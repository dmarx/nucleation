---
number: 214
status: Skimmed
formerly:
- NOTE-tmpm09fm
paper: LIT-230
title: 'Riesz representation theorem (Wikipedia)'
version: 1
date: '2026-09-26'
summary: >-
  A Hilbert space is isometrically (anti-)isomorphic to its continuous dual — every continuous linear functional φ is x ↦ ⟨x, f_φ⟩ for a unique f_φ with ‖f_φ‖ = ‖φ‖ — and this identification is what defines adjoints and the bra–ket correspondence.
---
<!-- inactive-ok-file: LIT-230 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-214: Riesz representation theorem (Wikipedia)

## Contribution

The article states the Riesz (Riesz–Fréchet, 1907) representation theorem: on a real Hilbert space the continuous dual is isometrically isomorphic to the space itself, and on a complex one it is isometrically anti-isomorphic. It sets up the linear/antilinear conventions carefully for both mathematicians and physicists, proves existence and uniqueness, gives several explicit constructions of the representing vector, and uses the theorem to define the canonical inner product on the dual, the extension of bra–ket notation, and the adjoint of an operator. It is distinguished at the top from the Riesz–Markov–Kakutani theorem about functionals and measures.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §"Statement": for φ ∈ H* there is a unique f_φ with φ(x)=⟨x,f_φ⟩, ‖f_φ‖=‖φ‖; f_φ lies in (ker φ)^⊥ and is the minimum-norm element of φ^{-1}(‖φ‖²) — the proof runs through the Hilbert projection theorem.
- Historical note in the statement section: attributed simultaneously to Riesz and Fréchet in 1907.
- §"Observations": a functional is pictured as the hyperplane φ^{-1}(1) with ker φ parallel to it; the Riesz vector is the normal direction.
- §"Constructions of the representing vector": from any nonzero u ⊥ ker φ, from the orthogonal projection onto ker φ, and in finite dimensions as a matrix computation.
- §"Adjoints and transposes": the adjoint A* is defined by composing A's transpose with the Riesz isometries Φ_H, Φ_Z; self-adjoint, normal and unitary operators are characterised this way.
- §"See also" includes "Covariance operator"; the article does not mention reproducing kernel Hilbert spaces (0 occurrences of "reproducing").

## Open questions

- Kernels and RKHS: an RKHS is a Hilbert space of functions on which every evaluation map f ↦ f(x) is continuous; Riesz then gives the representer k_x with f(x)=⟨f,k_x⟩, and k(x,y)=⟨k_x,k_y⟩ is the kernel. Everything in kernel methods, the representer theorem and neural-tangent-kernel analyses sits on this step, even though this article does not say so.
- Functionals as vectors: a linear probe, a readout head or a "concept direction" in an embedding space is a functional; Riesz is why it can be treated as a vector in the same space (normal to its level sets, per §Observations), and why cosine-similarity arithmetic on representations is meaningful only relative to a chosen inner product.
- Spectral approximation: the adjoint (and hence self-adjointness, which gives real spectra and orthogonal eigenfunctions) is defined via Riesz; spectral-embedding and spectral-contrastive analyses that approximate the top eigenfunctions of an operator on L²(data) presuppose it. The "Covariance operator" see-also is the bridge to cross-covariance / HSIC-style dependence measures.
- A deeper reading should check whether the anthology's representation readings ever need the complex case; if not, only the real-Hilbert-space statement (an honest isomorphism) matters and the antilinear bookkeeping can be skipped.
