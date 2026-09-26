---
status: Skimmed
paper: LIT-tmpy9oi9
title: 'Jorgensen & Tian, Noncommutative Analysis (GNS, RKHS)'
version: 1
date: '2026-09-26'
summary: >-
  The textbook puts the kernel construction and the GNS construction in one frame. It calls building a Hilbert space from a positive definite function "the GNS construction", and proves (Cor. 1.35) that the feature map realising a kernel as inner products is unique up to a unitary among minimal realisations. It also states that in the abelian case states are exactly probability measures, so that "the GNS construction is non-commutative measure theory".
---
<!-- inactive-ok-file: LIT-tmpy9oi9 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmp6923k: Jorgensen & Tian, Noncommutative Analysis (GNS, RKHS)

## Contribution

A graduate text in functional analysis motivated by quantum physics, probability and harmonic analysis. It runs from Hilbert-space tools and unbounded operators through the spectral theorem, operator algebras with an emphasis on the GNS correspondence between states and cyclic representations, dilation theory, Brownian motion, group representations and the Kadison–Singer problem, to self-adjoint extensions, graph Laplacians and reproducing kernel Hilbert spaces. The authors present it as unusual in organising these topics around the links between states, the representations they induce, and the operator algebras those generate.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Ch. 1, Remark 1.34 (p. 30): "An extremely useful method to build Hilbert spaces is the GNS construction". Start from a positive definite ϕ: X×X → C, form finite sums Σ c_x δ_x with ⟨Σc_xδ_x, Σd_yδ_y⟩ = Σ c̄_x d_y ϕ(x,y), quotient the null vectors and complete. This is the Moore–Aronszajn recipe, named GNS.
- Corollary 1.35 (p. 31): ϕ is positive definite iff ϕ(x,y) = ⟨Φ(x), Φ(y)⟩_H for some Φ: X → H. If H is minimal (the Φ(x) span a dense subspace), any two minimal solutions are related by a unitary U with UΦ₁(x) = Φ₂(x). The text prints "Φ₂(x)U", apparently a typo. Remark 1.36: H can be chosen as L²(Ω,F,P) for a probability space depending on ϕ.
- Ch. 4, Theorem 4.6 (p. 126): a bijection between states S(A) and cyclic representations up to unitary equivalence, built from the form (a,b) ↦ ϕ(a*b) with Ω = class(1) as the cyclic vector. Remark 4.8: pure states correspond to irreducible representations.
- §4.2, Example 4.28 (p. 131): for A = C(X), f ↦ ∫ f dμ is a state and "in the abelian case, all states are Borel probability measures. Because of this example, we say that the GNS construction is non-commutative measure theory."
- Ch. 11, Def. 11.1 and Claim 11.2 (pp. 333–334): point evaluation is continuous, so "by Riesz" there is K_s with h(s) = ⟨K_s, h⟩, and K_s = E_s*(1). This is the Riesz-makes-kernels link of the sibling strand, stated in the same book.

## Open questions

- It is the source found that states the kernel/GNS parallel explicitly, naming the kernel construction GNS, together with the uniqueness-up-to-unitary theorem for kernel realisations (Cor. 1.35) and the commutative reading (states = measures).
- The L²(P) identification of the commutative GNS space is not written out in the passages read, only states = measures. Check Ch. 3 (the spectral theorem via cyclic representations, "function algebra → measure μ → L²(μ)") for an explicit statement.
- Theorem 11.10 (Kolmogorov: positive definite functions on groups) and Ch. 5 (Stinespring dilation) are the group and operator-valued versions. Worth a look if kernels with symmetry matter.
