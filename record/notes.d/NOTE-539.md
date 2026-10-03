---
number: 539
status: 'Read'
formerly:
- NOTE-tmptw1ml
paper: 'LIT-656'
title: 'Loss Surface Simplexes for Mode Connecting Volumes and Fast Ensembling'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv PDF (v2, 26 pages) through PyMuPDF text
    extraction: §§1–7 and Appendix A in full; Appendices B and C from
    captions and text. Ensemble error rates are quoted where the text states
    them; values in Figs. 8–9 and 11 were not read off the plots.
date: '2026-10-03'
summary: >-
  SPRO: train connecting vertices to minimize mean loss at 5 uniform
  samples in a simplicial complex minus λ log volume. It joins up to 7
  modes in one complex and finds a low-loss region of at least 10
  dimensions for VGG-16 on CIFAR-10 (volume collapses at the 11th vertex).
  ESPRO, simplexes grown from single modes at about 10 epochs per vertex,
  beats deep ensembles in error, calibration and corruption robustness.
---

# NOTE-539: Loss Surface Simplexes for Mode Connecting Volumes and Fast Ensembling

## Contribution

A method, SPRO, for finding simplexes and simplicial complexes of low loss in
weight space, with evidence that independently trained networks lie in a
single multi-dimensional low-loss region rather than at the ends of thin
tunnels. From it, a practical ensembling method, ESPRO.

## Key insight

If a one-bend curve connects two modes, the bend is not special: a whole
simplex of bends does it too. Low loss in deep networks occupies volumes that
can be sampled uniformly once their vertices are known, and points spread
across such a volume disagree enough to ensemble well.

## Assumptions

- **Modes**: independently trained networks; VGG-16 trained 300 epochs with
  SGD (momentum 0.9, cosine schedule, learning rate 0.05, weight decay 5e−4);
  connectors trained 20 epochs at learning rate 0.01 (App. A).
- **Objective** (Eq. 1): for connector θ_j, minimize (1/H) Σ_h L(D, φ_h) −
  λ_j log V(K), φ_h ∼ U(K), H = 5. λ_j is normalized by the volume of a
  random complex of the same structure, with λ* = 10⁻⁸; results are reported
  insensitive to it (Fig. A.3).
- **Initialization**: a new vertex starts at the mean of the existing ones.
- **Sampling** (App. A.1): barycentric weights from a flat Dirichlet. The
  authors worry this may not be uniform on a non-standard simplex and check
  it visually (Fig. A.2).
- **BatchNorm** statistics recomputed for each sampled model, after Garipov
  et al.; LayerNorm needs nothing.

## Key results

- **SWAG over curves** (§4.1, Fig. 2): a Gaussian posterior over the bend of a
  Garipov et al. curve; every sampled curve stays in low loss.
- **Complexes** (§4.2): K(S(w₀,θ₀,θ₁,θ₂), S(w₁,θ₀,θ₁,θ₂)) for VGG-16 on
  CIFAR-10 (Fig. 3); 4 modes and 3 connectors on CIFAR-100; 7 modes, 9
  connectors and 12 simplexes on CIFAR-10 (Fig. 4).
- **Dimension** (§4.3, Fig. 5): volume between two modes grows with
  connectors to a maximum of about 10⁵ and collapses to about 10⁻⁴ at k = 11;
  all 25 samples per complex exceed 98% train accuracy. The low-loss manifold
  has at least 10 dimensions here.
- **ESPRO** (§5): simplexes grown from each of several modes. Vertex cost
  about 10 epochs (CIFAR-10) and 20 (CIFAR-100), against 200 and 300 for a
  model. 25 samples. VGG-16 CIFAR-10: 3-member deep ensemble about 6.2% error,
  ESPRO with 2-simplexes about 5.7%. At any fixed number of members or
  training budget ESPRO beats deep ensembles, on CIFAR-10 and CIFAR-100
  (Fig. 8), and for ResNet-56 (Fig. 9).
- **Functional diversity** (§5.3, Fig. 7): samples from one 3-simplex of an
  8-layer classifier on two spirals fit the data with visibly different
  decision boundaries.
- **Uncertainty** (§6): better in-between and extrapolation bands on a toy
  regression than deep ensembles and curve-subspace inference (Fig. 10); most
  accurate under Gaussian-noise corruption at all levels, and lowest NLL after
  temperature scaling (Fig. 11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Independently trained networks are connected through multi-dimensional simplicial complexes of low loss | moderate: VGG-16 on CIFAR-10/100, up to 7 modes | §4.2, Figs. 3–4 |
| C2 | The connecting low-loss region has at least 10 dimensions for VGG-16 on CIFAR-10 | moderate as a lower bound; one setting | §4.3, Fig. 5 |
| C3 | All SGD solutions lie on one connected multi-dimensional volume | weak: an extrapolation from the complexes found | §1, Fig. 1, §7 |
| C4 | ESPRO beats deep ensembles in accuracy at equal size and budget | moderate: VGG-16 and ResNet-56 on CIFAR | Figs. 8–9 |
| C5 | ESPRO gives better calibration and robustness under shift | moderate: CIFAR-10 corruptions, after temperature scaling | Fig. 11, App. C |

## Method

SPRO adds connectors one at a time, each trained with the others fixed.
ESPRO grows a simplex S(w_j, θ_{j,0}, …, θ_{j,k}) at each mode separately and
predicts with the average over the union of the simplexes, read as a Bayesian
model average under a posterior uniform on the complex (Eqs. 4–5).

## Concepts

- **mode connecting volume**: a set of positive volume in weight space, of low
  loss, containing several independently trained modes.
- **simplicial complex K**: a union of simplexes sharing vertices; its volume
  is the sum of theirs.
- **SPRO / ESPRO**: Simplicial Pointwise Random Optimization, and ensembling
  over its simplexes.

## Connections

- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md)).** The procedure generalized; their
  connecting curve is the 1-simplex case.
- **Draxler et al. ([LIT-653](../literature.d/LIT-653.md)).** Credited jointly with discovering low-loss
  curves.
- **Fort & Jastrzębski (2019)**, not held: low-loss "wedges" and connectors
  joining several modes at a point (m-tunnels), which SPRO also recovers.
- **Wortsman et al. (2021)**, not held: concurrent work learning lines and
  simplexes of networks from scratch.
- **Izmailov et al. (SWA, [ANTH-LIT-673](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-673.md)), Maddox et al. (SWAG)**: the flat-region
  and posterior tools this paper builds on.

## Bearing on the record

- Supports the THEORY candidate that SGD optima lie in one connected low-loss
  set, and widens it from paths to volumes of measurable dimension.
- Relevant to the star-domain readings in this batch: it shows the set has
  volume, but says nothing on whether it is convex or star-shaped.
- An anthology candidate for its ensembling method.

## Limitations

- **One architecture carries the geometry**: all volume and dimension
  results are VGG-16 on CIFAR.
- **Dimension is a lower bound** for SPRO's construction; §4's opening calls
  it "an empirical upper bound", while §4.3 rightly calls it a lower bound.
- **"All modes on one volume"** is the framing (Fig. 1, §7), supported by
  complexes of at most 7 modes.
- **The sampling worry is unneeded** (my observation, not the paper's): a flat
  Dirichlet over barycentric coordinates, mapped affinely onto any simplex,
  is uniform on that simplex, because an affine map has constant Jacobian.
  The loss estimate in Eq. 1 is therefore unbiased.
- **Ensemble gains depend on temperature scaling** for NLL comparisons.

## Open questions

- What is the true dimension of the low-loss region, and how does it scale
  with width?
- Are the complexes convex after permutation alignment? This paper does not
  align.
- Can MCMC be designed to move within these subspaces, as the authors propose?

## Corrections

- none to a seeded skim (there was no seed)
