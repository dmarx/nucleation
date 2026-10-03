---
number: 528
status: Read
formerly:
- NOTE-tmpi1dor
paper: LIT-655
title: 'Understanding Mode Connectivity via Parameter Space Symmetry'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v1 (20 pages). Main text in full; proofs in Appendices
    C and D followed for Proposition 4.1, Proposition 4.3 (in outline),
    Lemma 5.1, Proposition 5.2 and Proposition 5.3; Appendix A and E read
    for statements only. Theorem 6.2's displayed formula is garbled in the
    text layer and is given here in the form its first-order approximation
    (κ‖w₂ − w₁‖²/8) implies.
date: '2026-10-03'
summary: >-
  Minimum of full-rank ‖Y − W_l…W₁X‖² ≅ GL_h(ℝ)^{l−1}: 2^{l−1} components,
  independent of width. 1-D three-layer: 4 components, 3 with a skip. h ≥ 2:
  permutations connect all components. Homogeneous last layers: rescaled
  minima in one component with unbounded midpoint loss, even under
  last-layer permutations (Props. 5.3–5.4). Symmetry curves
  γ(t) = exp(t log g)·w have constant loss; curvature ≤ κ bounds the chord's
  distance from the level set by (1/κ)(1 − √(1 − (κ‖Δw‖/2)²)) ≈ κ‖Δw‖²/8.
---


# NOTE-528: Understanding Mode Connectivity via Parameter Space Symmetry

## Contribution

It brings a tool from topology to the question of whether minima are
connected: find the group of parameter transformations that leave the loss
unchanged, and read the components of the minimum off the components of the
group. With it the paper counts components exactly for full-rank linear
networks, shows a skip connection reducing the count, shows permutations
connecting the rest, and constructs explicit failures of linear mode
connectivity and explicit constant-loss curves.

## Key insight

A minimum is not a point but an orbit: apply any symmetry to a minimum and
you get another. If the symmetry group is in one piece, so is the orbit; if
the group is in two pieces (GL_h has positive- and negative-determinant
halves), the orbit can be too. A permutation with negative determinant
hops between the halves, which is one reason permuting helps connectivity.
A continuous symmetry like rescaling also gives a curve along which loss is
exactly constant, and the curve can be far from straight. When it is very
curved, its chord leaves the minimum and the straight-line barrier is large.

## Assumptions

- **Section 4.1**: square full-rank X, Y ∈ ℝ^{h×h}, all W_i ∈ ℝ^{h×h}, no
  activation, zero minimum. The homeomorphism needs every W_i invertible on
  the minimum, which full rank of X and Y forces.
- **Proposition 4.3**: n = 1 (scalar weights), X, Y ≠ 0, residual
  W₃(W₂W₁X + εX).
- **Propositions 5.3–5.4**: L(W) = ‖Y − W_l σ(W_{l−1} f(…))‖² with σ(cz) =
  c^k σ(z); ‖Y‖ ≠ 0; a zero-loss minimum exists. The proof uses c = m > 0
  only, so positive homogeneity (leaky ReLU, linear) is what is needed.
- **Theorem 6.2**: a smooth constant-loss curve between the two points, with
  curvature bounded by κ_max, and a Lipschitz loss for the loss bound.
- **Experiments**: synthetic two-layer and five-layer regressions with
  Gaussian X, Y and sizes up to 100 (Figs. 3–4).

## Key results

- **Corollary 4.2**: 2^{l−1} components, independent of width, because
  GL_h(ℝ) has two components for every h.
- **Proposition 4.3**: with ε ≠ 0 the minimum is S₁ ∪ S₀, with S₁ ≅ GL₁ × GL₁
  (4 components) and S₀ the line {W₁ = 0, W₃ = Y(εX)⁻¹}; S₀ meets two
  components of S₁, giving 3.
- **Lemma 5.1, Proposition 5.2**: for l = 2, any g with det g < 0 moves a
  minimum to the other component; for h ≥ 2 a layerwise choice of
  permutations makes any two minima connected.
- **Proposition 5.3 (proof, Appendix D)**: with W′ = (W_l m^{−k}, mW_{l−1},
  …), the midpoint loss is (1 − 2^{−(k+1)}(1 + m^{−k})(1 + m)^k)²‖Y‖², which
  exceeds b for m chosen large; Fig. 4 shows it growing on a five-layer
  leaky-ReLU network.
- **Proposition 5.5**: on {(W₁, W₂) : W₁W₂ = A}, chord points can be
  arbitrarily far from the set. The paper notes attention's W_Q W_Kᵀ has this
  GL_h structure.
- **Proposition 6.1**: under the approximate action (U, V) ↦ (Uσ(VX)σ(gVX)†,
  gV), ‖Uσ(VX) − U′σ(V′X)‖ ≤ ‖Uσ(VX)‖. Checked on 100 random sigmoid networks
  (Fig. 3a).
- **Theorem 6.2**: dist(w, L⁻¹(c)) ≤ d_max for every chord point, with
  d_max ≈ κ_max‖w₂ − w₁‖²/8 when κ_max‖w₂ − w₁‖ is small, and
  |L(w) − c| ≤ C_L d_max.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The minimum of a full-rank linear network has 2^{l−1} components | strong (proof) | Prop. 4.1, Cor. 4.2 |
| C2 | Skip connections reduce the number of components | strong for the 1-D three-layer case only; generalisation suggested, not proved | Prop. 4.3, Fig. 1 |
| C3 | Permutations connect all minima of full-rank linear networks with h ≥ 2 | strong (proof) | Lemma 5.1, Prop. 5.2 |
| C4 | Linear interpolation between minima in one component can have unbounded loss, even after last-layer permutation | strong as a construction; the constructed minima are rescalings that SGD's implicit bias may never produce, as the authors concede | Props. 5.3–5.4, §5.2 |
| C5 | Symmetry-induced curves have constant loss, and approximate ones have bounded loss change | strong for exact symmetries; for the approximate action the bound is loose (it allows the output to change by its own norm) | Eq. 5, Prop. 6.1, Fig. 3 |
| C6 | Bounded curvature of a connecting curve implies approximate LMC | strong (elementary geometry) as a sufficient condition; no estimate of κ for real networks | Thm. 6.2 |

## Concepts

- **symmetry group of L**: a topological group G with L(g·x) = L(x).
- **orbit**: all g·x for g ∈ G; a subset of a level set.
- **connected component, π₀**: maximal connected subsets; |π₀| counts them.
- **symmetry-induced curve**: γ(t) = exp(t log g)·w, constant loss when g
  acts as a symmetry.

## Connections

- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md)), Git Re-Basin ([LIT-661](../literature.d/LIT-661.md))**: the
  permutation conjecture and its algorithms. This paper shows permutations
  doing a topological job (joining GL components) in linear networks, and
  shows that continuous symmetries can defeat linear interpolation where
  permutations of one layer cannot repair it.
- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: their empirically fitted curves are
  what Section 6 replaces with derived ones.
- **Kuditipudi et al. ([LIT-671](../literature.d/LIT-671.md)), Ferbach et al. ([LIT-680](../literature.d/LIT-680.md))**: cited
  as the dropout-stability and optimal-transport routes to connectivity.
- **Lubana et al. ([LIT-669](../literature.d/LIT-669.md)), Zhou et al. ([LIT-674](../literature.d/LIT-674.md))**: cited for
  what failure and success of LMC mean about the models.
- **Theus et al. ([LIT-664](../literature.d/LIT-664.md))** exploit the same GL_h symmetry of attention
  products that Proposition 5.5 points to, for alignment.

## Bearing on the record

- It widens the anthology's [ANTH-THEORY-010](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-010.md) from permutations to continuous
  symmetries: the account "barrier = mislabelled units" is the discrete
  special case. It also qualifies that theory: continuous symmetries can
  make the barrier between two equivalent minima unbounded.
- A THEORY candidate: *the connectedness of a network's minimum is bounded
  by the connectedness of its symmetry group, and permutations matter
  because they join group components that continuous symmetries cannot*.
  Proven only for linear networks.
- Its §7 cautions against averaging minima without checking connectivity, a
  practice instruction for the anthology.

## Limitations

- **Linear networks** for the component counts, and scalar weights for the
  skip-connection result. The authors call extension to nonlinear networks
  an open problem that needs the full symmetry group, which is unknown for
  most architectures.
- **Reachability.** The unbounded-barrier constructions are not minima SGD
  is shown to find; the paper offers implicit bias as the likely reason LMC
  is observed anyway.
- **Approximate symmetries** (Section 6.1) are not loss-preserving when the
  batch exceeds the hidden width, and the only bound is the output's own
  norm.
- **Experiments** are synthetic regressions with tens of units; nothing on
  trained image or language models.

## Open questions

- What are the components of the minimum for ReLU networks, once the full
  symmetry group is known?
- How curved are the symmetry-induced curves between real SGD minima?
  Theorem 6.2 needs that number.

## Corrections

- none to a seeded skim (there was no seed)
- **Homogeneity.** Proposition 5.3 states σ(cz) = c^k σ(z) "for all c ∈ ℝ",
  which leaky ReLU does not satisfy for c < 0. The proof only uses c > 0, so
  the result stands for positively homogeneous activations.
- **"First two layers."** The text after Proposition 5.4 says the
  permutation is "restricted to the first two layers", but the proposition
  permutes between W_{l−1} and W_l, the last two.
