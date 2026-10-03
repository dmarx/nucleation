---
status: 'Read'
paper: 'LIT-tmpyiw0q'
title: 'Proving Linear Mode Connectivity of Neural Networks via Optimal Transport'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from the arXiv PDF (v2, 40 pages) through PyMuPDF text extraction.
    §§1–7, the related-work appendix and Appendix B.14 (dropout stability)
    in full. Appendices B (OT lemmas, propagation Lemma 4.1, Theorems
    5.2–5.4 and B.21), C (mean-field proof) and D (matching experiments,
    Theorem D.2) read for statements and the structure of the arguments; the
    concentration and packing-number calculations were not checked line by
    line. Figure 2 read from its caption and text.
date: '2026-10-03'
summary: >-
  Layerwise neuron alignment equals a Wasserstein distance between
  empirical weight distributions (Birkhoff), so LMC modulo permutation
  follows when neuron weights are i.i.d. and layers are wide: for
  mean-field two-layer SGD (Theorem 3.1), and for deep Gaussian or
  sub-Gaussian nets with m̃_ℓ = Õ((T_ℓ/ε)^{m̃_{ℓ−1}}) (Theorem 5.2), tight
  by Theorem 5.3. Low-dimensional weights relax this (Theorem 5.4).
---

# NOTE-tmpxf5zl: Proving Linear Mode Connectivity of Neural Networks via Optimal Transport

## Contribution

A general framework that turns linear mode connectivity modulo permutation
into a question about the convergence of empirical measures in Wasserstein
distance. With it come proofs for trained two-layer networks and for deep
networks with independent weights, a lower bound showing the width rate is
tight, and a weight-matching method motivated by the dimension of the weight
distribution.

## Key insight

Two wide layers whose neurons are independent samples from one
distribution are two samples of the same cloud of points. Matching each
neuron of one to its nearest counterpart in the other is optimal transport,
and the matched pairs get closer as the clouds get denser, at a rate set by
the cloud's dimension. Match every layer, and the two networks compute nearly
the same activations, as does every network on the line between them. The
number of samples needed grows exponentially in dimension, which is why the
width needed explodes with depth unless weights live near a low-dimensional
subspace.

## Assumptions

- **LMC** is understood modulo permutation of hidden units throughout; the
  barrier follows Frankle et al. and Entezari et al. (sup over t of the error
  on the line minus the interpolated endpoint errors).
- **Theorem 3.1** (mean field; Mei et al. 2019): two-layer net f_N(x; θ) =
  (1/N) Σ σ*(x; θ_i); SGD with step size of order ε and slowly varying
  (Assumption 1); bounded, Lipschitz σ (excludes ReLU; the appendix relaxes
  this to small on a large compact set); bounded data support; initial weights
  i.i.d. with bounded support; Assumption 2 (smoothness of V, U) only for
  noisy regularized SGD. Width N ≥ N_min and step ε ≤ ε_max(N).
- **Multilayer results**: Assumption 6, the neurons' weight vectors within a
  layer are i.i.d. from µ_ℓ, which holds at initialization. Assumption 5: σ
  pointwise, 1-Lipschitz, σ(0) = 0 (ReLU qualifies). Assumption 7: loss
  convex in the prediction. Input with bounded second moment; m₀ ≥ 5 for
  technical reasons. Assumptions 3–4: each layer's weight distribution is
  approximable by fewer points, and errors sum with a central-limit
  behaviour.
- **Networks A and B** are independent draws from one distribution over
  parameters, independent of the test data.

## Key results

- **Lemma B.3** (Birkhoff): between two empirical measures with m atoms, the
  optimal-transport cost equals the minimum over permutations, so permutation
  matching is exactly a Wasserstein problem.
- **Theorem 3.1**: for any δ and error tolerance there is N_min such that, for
  N ≥ N_min and ε small enough, with probability ≥ 1 − δ there is a
  permutation of B's hidden layer with |t f(x; θ_A) + (1 − t) f(x; θ_B) −
  f(x; tθ_A + (1 − t)θ̃_B)| ≤ err for almost every x and every t, and a
  corresponding bound on the squared loss.
- **Lemma 4.1**: the closeness property propagates from layer ℓ to ℓ + 1
  with constants E_{ℓ+1} = 2C₂E_ℓ + 2C₁ m̃_ℓ Ē_ℓ.
- **Lemma 5.1 / Theorem 5.2** (Gaussian init): widths m_ℓ ≥ m̃_ℓ with
  m̃_ℓ = Õ((T_ℓ/ε)^{m̃_{ℓ−1}}), m̃₀ = m₀, give LMC with Q-probability
  1 − δ_Q. The two-layer case needs ε^{−m₀} hidden units, against Entezari et
  al.'s ε^{−(2m₀+4)}.
- **Theorem 5.3** (lower bound): for rows i.i.d. from a density bounded by F₁
  and full-rank data covariance, the expected best-permutation matching error
  is bounded below at the rate set by the dimension, so the recursive
  exponential growth is tight.
- **Theorem 5.4**: if weights are approximately supported in dimension
  k_ℓ = e·m̃_ℓ (Assumption 8, accuracy η), the needed width shrinks for widths
  up to about η^{−k}; asymptotically the rate of Theorem 5.2 returns.
- **Sub-Gaussian extension** (§5.5, App. B.13): independent coordinates with
  sub-Gaussian tails (for example uniform) give the same results with changed
  constants.
- **Dropout stability** (App. B.14): in a one-hidden-layer setting with
  sub-Gaussian weights, the dropout error scales with width at the same rate
  as the LMC error.
- **Experiment** (§6, Fig. 2): 3-hidden-layer, 512-wide MLP on MNIST, SGD at
  learning rates from 10⁻⁴ to 10⁻¹, 4 runs. Approximate dimension
  Dim(S) = tr(S)²/tr(S²) of the matched matrices correlates with the barrier;
  covariance-weighted weight matching (norm ‖·‖_{2,Σ_{ℓ−1}}) beats plain
  weight matching at every learning rate. Theorem D.2 supports it in a
  simplified case. Adam results were less clear and not reported.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Wide two-layer nets trained by mean-field SGD are LMC modulo permutation w.h.p. | strong (proof), mean-field regime with bounded activations | Theorem 3.1, App. C |
| C2 | Deep nets with i.i.d. neuron weights are LMC modulo permutation once widths exceed m̃_ℓ = Õ((T_ℓ/ε)^{m̃_{ℓ−1}}) | strong (proof) | Lemma 5.1, Theorem 5.2 |
| C3 | That recursive exponential rate is tight | strong (proof) | Theorem 5.3 |
| C4 | Low-dimensional weight distributions lower the width needed | strong (proof) under Assumption 8 | Theorem 5.4 |
| C5 | Approximate dimension of the weights predicts LMC in trained nets | weak: one MLP on MNIST, 4 runs, correlation less clear at learning rate 10⁻¹ | Fig. 2 |
| C6 | Covariance-weighted weight matching outperforms plain weight matching | moderate: same setting | Fig. 2, Theorem D.2 |

## Concepts

- **effective width m̃_ℓ**: a width smaller than the real one, defined through
  an equi-partition of the layer's neurons, that bounds the function space
  available at the layer and avoids requiring each real width to grow.
- **approximate dimension**: tr(S)²/tr(S²) of a covariance matrix.
- **Property 1**: a closeness condition on the activations of A, permuted B
  and the line between them at layer ℓ, propagated layer by layer.

## Connections

- **Entezari et al. ([LIT-tmp2uwzo](../literature.d/LIT-tmp2uwzo.md)).** Generalized: from one hidden layer at
  uniform initialization to deep nets and trained two-layer nets, with a
  better rate.
- **Git Re-Basin ([LIT-tmpd6bma](../literature.d/LIT-tmpd6bma.md)).** Its matching objectives are the
  baselines in §6. Its finding of no LMC at initialization is read here as a
  width effect.
- **Kuditipudi et al. ([LIT-tmplpsy5](../literature.d/LIT-tmplpsy5.md))** and **Shevchenko & Mondelli (2020)**,
  not held: dropout stability and non-linear connectivity for mean-field
  two-layer nets. This paper proves the stronger, linear statement in the same
  regime.
- **Singh & Jaggi (2020)**, not held: optimal transport used for soft
  alignment and fusion.
- **Frankle et al. ([LIT-tmp3owu9](../literature.d/LIT-tmp3owu9.md)).** Credited with coining LMC.

## Bearing on the record

- Theoretical support for the THEORY candidate that barriers are mostly
  permutation artefacts, under independence of neurons. It also explains the
  candidate's dependence on width.
- Bears on the candidate that linear connectivity emerges in training: it
  proves connectivity *at initialization* for wide enough nets. The two are
  consistent only because practical widths are far below the bound.

## Limitations

- **Independence of neurons** within a layer is the central assumption. It
  is exact at initialization and holds for mean-field two-layer SGD; for deep
  trained networks it is assumed. The authors name approximate independence
  as future work.
- **Mean-field Theorem 3.1 excludes ReLU** and needs vanishing step sizes.
- **The deep bounds are far from practical widths**, which the authors say
  outright.
- **The experiment** is one MLP on MNIST with SGD; Adam was inconclusive.

## Open questions

- How independent are the neurons of a trained deep layer, and does
  approximate independence suffice?
- Can a formal equivalence between dropout stability and LMC be proved? The
  appendix sketches it.
- Does the optimizer change the weight distribution's dimension, and with it
  LMC?

## Corrections

- none to a seeded skim (there was no seed)
