---
number: 486
status: Read
formerly:
- NOTE-tmpxfj4e
paper: 'LIT-622'
title: 'Optimizing Neural Networks with Kronecker-factored Approximate Curvature'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v7 (58 pages, text layer). Sections 1–13 and Appendices
    A (cumulant derivation and Lemma 4), B (inverting A⊗B ± C⊗D) and C
    (cheap v⊤Fv) read; the proof of Theorem 1 and Corollaries 2–3 in the
    final appendix followed in outline. Figures 2–3 and 5–11 are read from
    their captions and the text, since the extracted text does not carry
    the plotted values.
date: '2026-10-03'
summary: >-
  Fisher blocks E[āāᵀ ⊗ ggᵀ] ≈ E[āāᵀ] ⊗ E[ggᵀ], with error a sum of third-
  and fourth-order cumulants; the inverse is approximated as block-diagonal
  or block-tridiagonal over layers. Factored Tikhonov damping (π chosen by
  trace norms), re-scaling by the exact Fisher, and a two-parameter momentum
  solved on the quadratic model. On three deep autoencoders it beats tuned
  NAG-SGD by orders of magnitude in iterations; block-tridiagonal gains
  25–40% per iteration over block-diagonal.
---

# NOTE-486: Optimizing Neural Networks with Kronecker-factored Approximate Curvature

## Contribution

An approximation to the neural-network Fisher that is neither diagonal nor
low-rank, can be inverted cheaply, and can be estimated online from as much
data as one likes without raising the cost of inversion. Around it, a full
optimizer with damping, momentum and cost controls that makes approximate
natural gradient competitive with SGD in the stochastic regime, plus a proof
that it is invariant to a broad class of per-layer affine reparameterizations.

## Key insight

The gradient of a layer's weight matrix is an outer product of what flows in
(activations ā) and what flows back (derivatives g). If the two are treated
as independent, each layer's Fisher block becomes a Kronecker product of an
input-side covariance and an output-side covariance, and Kronecker products
invert factor by factor. The cross-layer structure is then put in the
*inverse* Fisher, where it is approximately sparse, rather than in the
Fisher, where it is not.

## Assumptions

- **Loss is a negative log-likelihood** L(y, z) = −log r(y | z) of a
  simple predictive distribution (Gaussian for squared error, multinomial
  for cross-entropy), so the Fisher equals the generalized Gauss–Newton
  matrix when z are natural parameters (Section 2.2).
- **The model's Fisher**: expectations over y are under the network's
  predictive distribution, estimated by sampling targets and running an
  extra backward pass (Section 5). Lemma 4, E[u Dv] = 0, holds only for this
  distribution, not for training labels.
- **Independence of activity products and derivative products** (Eq. 2),
  for the Kronecker factorization; it is exact when third- and fourth-order
  cumulants vanish, e.g. jointly Gaussian quantities.
- **Fully connected feed-forward layers** with elementwise nonlinearities
  and biases folded in by a homogeneous coordinate. Convolutional and
  recurrent layers are listed as future work.
- **Damping negligible** for the invariance results (Corollary 2).

## Key results

- **Eq. 1.** F̃ᵢ,ⱼ = Āᵢ₋₁,ⱼ₋₁ ⊗ Gᵢ,ⱼ, with Āᵢ,ⱼ = E[āᵢāⱼᵀ] and
  Gᵢ,ⱼ = E[gᵢgⱼᵀ].
- **Eq. 3.** The per-entry error is κ(ā⁽¹⁾, ā⁽²⁾, g⁽¹⁾, g⁽²⁾) +
  E[ā⁽¹⁾]κ(ā⁽²⁾, g⁽¹⁾, g⁽²⁾) + E[ā⁽²⁾]κ(ā⁽¹⁾, g⁽¹⁾, g⁽²⁾). On the Figure 2
  network the total error over the middle four layers is 2894.4 against an
  upper bound of 4134.6.
- **Block-diagonal inverse (Section 4.2).** F̆⁻¹ = diag(Ā⁻¹ᵢ₋₁,ᵢ₋₁ ⊗ G⁻¹ᵢ,ᵢ),
  applied as Uᵢ = G⁻¹ᵢ,ᵢVᵢĀ⁻¹ᵢ₋₁,ᵢ₋₁.
- **Block-tridiagonal inverse (Section 4.3).** F̂⁻¹ = ΞᵀΛΞ, the block
  Cholesky form of a chain-structured directed Gaussian model, with
  Ψᵢ,ᵢ₊₁ = Ψ^Āᵢ₋₁,ᵢ ⊗ Ψ^Gᵢ,ᵢ₊₁. The conditional covariances are differences
  of Kronecker products, inverted by the eigen-decomposition method of
  Appendix B.
- **Factored Tikhonov damping (Eq. 7).** (Ā + π√(λ+η) I) ⊗ (G + (1/π)√(λ+η) I),
  with π = √[(tr Ā/(d+1)) / (tr G/d)], the ratio of average eigenvalues.
  The authors report it often works better than exact Tikhonov damping and
  call the reason "somewhat mysterious".
- **Re-scaling (Section 6.4).** α* = −∇hᵀΔ / (Δᵀ F Δ + (λ+η)‖Δ‖²), using
  the exact Fisher on the mini-batch; with it, K-FAC is HF preconditioned by
  the approximate Fisher with one CG step.
- **Momentum (Section 7).** δ = αΔ + μδ₀ with α, μ minimizing the quadratic
  model; on a deterministic quadratic this is preconditioned linear CG.
- **Theorem 1, Corollaries 2–3.** Without damping, K-FAC's path in
  distribution space is invariant to s†ᵢ = W†ᵢā†ᵢ₋₁, ā†ᵢ = Ωᵢφ̄ᵢ(Φᵢs†ᵢ) for
  invertible Ωᵢ, Φᵢ: e.g. logistic versus tanh, and affine input
  preprocessing. The block-diagonal update equals gradient descent in a
  network whose activities and derivatives are centered and whitened.
- **Experiments (Section 13).** MNIST, CURVES and FACES deep autoencoders.
  K-FAC's per-iteration progress grows superlinearly in mini-batch size m;
  with an exponentially increasing m and momentum it is much faster per
  second than the NAG baseline; without its momentum it is not
  significantly faster. Block-tridiagonal makes 25–40% more progress per
  iteration than block-diagonal at moderately higher cost.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A layer's Fisher block is well approximated by a Kronecker product of activation and derivative covariances | moderate: exact error formula, but checked visually on one small tanh network; the authors expect it never to be exact | Eq. 3, Figure 2 |
| C2 | The inverse Fisher is approximately block-tridiagonal over layers while the Fisher is not | moderate: graphical-model argument plus one example network | Section 4.1, Figure 3 |
| C3 | K-FAC with momentum and growing batches is much faster than tuned SGD with momentum | moderate: three autoencoder benchmarks, single GPU, no classifiers | Figures 10–11 |
| C4 | K-FAC is invariant to per-layer affine reparameterizations when damping is negligible | strong (proof) | Theorem 1, Corollary 2 |
| C5 | Re-scaling by the exact Fisher is needed for good updates | moderate: one network at one iteration | Figure 7 |
| C6 | The model Fisher should be used, not the empirical Fisher | weak here: argued, and attributed to Martens (2010, 2014) | Section 5, footnote 3 |

## Concepts

- **Khatri–Rao product**: the block-wise Kronecker structure F̃ takes across
  layers.
- **generalized Gauss–Newton (GGN)**: the PSD curvature matrix obtained by
  linearizing the network up to the loss; equal to the Fisher in the
  exponential-family case.
- **empirical Fisher**: the second moment of gradients at the training
  labels; contrasted with the true Fisher, which samples y from the model.
- **factored Tikhonov damping**: adding multiples of I to each Kronecker
  factor instead of to their product.

## Connections

- **Amari (1998, [LIT-607](../literature.d/LIT-607.md))** gives the definition approximated,
  F⁻¹∇h, and the information-geometric reading of it.
- **Heskes (2000)** had a similar block-diagonal Kronecker approximation;
  K-FAC differs by adaptive damping with exact-Fisher re-scaling, the
  block-tridiagonal inverse, momentum and stochastic estimation of Gᵢ,ᵢ.
  **Povey et al. (2015)**, concurrent, used the empirical Fisher.
- **TONGA (Le Roux et al. 2008)** and **Ollivier (2013)** use per-unit
  blocks; K-FAC's blocks are whole layers.
- **Papyan (2020, [LIT-613](../literature.d/LIT-613.md))** later tested the per-layer Kronecker
  approximation on classifiers and proposed a class-wise correction.

## Bearing on the record

- It is the record's statement of *imposed* Kronecker structure in the
  Fisher. The question the owner's line asks, what structure the true Fisher
  has, is answered for classifiers by Papyan, and his answer is that a
  single Kronecker product per layer misplaces the class-driven outliers.
- **THEORY candidate (not filed):** "Per-layer Fisher blocks of a
  classifier are sums of class-indexed Kronecker products, not one
  Kronecker product." Sources would be Papyan 2020 with this paper as the
  approximation it corrects.
- Carries an instruction for practice, hence `anthology-candidate`; the
  anthology reads its successors ([ANTH-LIT-768](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-768.md), [ANTH-LIT-746](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-746.md)).

## Limitations

- All optimization experiments are deep autoencoders with squared or
  cross-entropy reconstruction loss; nothing on classifiers, convolutional
  or recurrent networks.
- The approximation-quality evidence is one small network, partially
  trained.
- Many hyperparameters of the damping scheme (λ start 150, ω₁, T₁ = 5,
  T₂ = 20, T₃ = 20, τ₁ = 1/8, τ₂ = 1/4) were set by the authors' experience;
  the paper says some are application dependent.

## Open questions

- When does the independence of activities and derivatives fail badly? The
  paper bounds the error by cumulants but does not characterise networks
  where they are large. Papyan's class structure is one answer.
- Extensions to convolutional and recurrent layers, listed by the authors.

## Corrections

- none (there was no seed)
