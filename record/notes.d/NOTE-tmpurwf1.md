---
status: Read
paper: 'LIT-tmpzunec'
title: 'Rahaman et al. — On the Spectral Bias of Neural Networks'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from arXiv 1806.08734v3 (31 May 2019, the camera-ready
    ICML version with appendices, 23 pages), downloaded from arxiv.org and
    extracted with pdftotext. Read: §§1–6 and Appendices A (Experiments
    1–9, A.1–A.7), B (Lemma 3), C (Lemmas 1–2, Theorem 1, the Diaz et al.
    recursion, Propositions 1–3, the stationary-phase argument of C.7), D
    (Definition 1, Lemma 4, Remarks 1–2, the volume proposition) and E.
    Equations garbled by extraction were rebuilt from the surrounding text
    and checked against renders of pp. 4, 6, 7 and 16. Figures 1–3 and
    6–9, 19 and 20 were seen in renders at low resolution, so their
    heatmaps are read qualitatively; the rest were read from captions and
    text. The Fourier decay (Lemma 1, Lemma 2 for bounded polytopes), the
    sign of Lemma 1, and the flower-manifold mechanism were re-checked by
    hand and with a numpy script in the scratchpad.
date: '2026-10-20'
summary: >-
  A ReLU network is piecewise linear, so its Fourier transform falls as
  k^(−d−1) along almost every direction and as k^(−2) along the normals
  to the faces of its linear regions; that is proved for compactly
  supported networks only. Trained networks fit low frequencies first,
  even when high frequencies carry ten times the amplitude, and
  high-frequency components are the first to be destroyed by parameter
  noise; both are experiments. The tie from the decay to the order of
  learning is a heuristic bound, and the volume "proof" in Appendix D
  does not hold. On a curve embedded in the plane, high latent
  frequencies are fitted more easily as the curve gets more petals.
  The paper puts this down to the shape of the curve, but most of it
  comes from the curve getting longer.
---
<!-- inactive-ok-file: THEORY-186 THEORY-481 — Proposed; accounts this reading is set beside, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmpon8ox — Proposed; the empirical account filed from this reading -->

# NOTE-tmpurwf1: Rahaman et al. — On the Spectral Bias of Neural Networks

## Contribution

It named the "spectral bias" and gave the first combined case for it, in
three parts. (i) A closed form for the Fourier transform of a ReLU
network, built from the fact that it is continuous and piecewise linear.
(ii) Experiments showing that a deep ReLU network trained on a sum of
sinusoids fits the low frequencies first, whatever their amplitudes, and
that its high-frequency components are the least robust to random
perturbation of the trained parameters. (iii) Experiments and a
stationary-phase argument showing that on a low-dimensional manifold the
frequencies that are hard to learn are set by the embedding, not by the
target alone. Part (i) is proved, for compactly supported networks. Part
(ii) is experimental. The link from (i) to (ii) is an asymptotic bound on
the speed of each frequency, not a theorem about order. Part (iii) is a
heuristic with one controlled family of curves.

## Key insight

The frequency content of a ReLU network is limited by its geometry:
finitely many flat pieces, each with a bounded slope. Each integration
by parts across a face of a linear region gains a factor 1/k, so along a
generic direction the transform falls as k^(−d−1). Raising a high
frequency needs many regions and large slopes, which need large and
finely tuned weights. Gradient descent grows the weights slowly, so the
high frequencies come late. The same tuning makes them fragile. "Low
frequency" is in the coordinates of the input space. If the data lie on
a curve that the input space traverses quickly, a low frequency in the
input space is a high one along the curve.

## Assumptions

- **§2 and Appendix C, the analysis.** f(x) = T^(L+1) ∘ σ ∘ T^(L) ∘ … ∘
  σ ∘ T^(1)(x), with affine T^(k) and σ = ReLU, scalar output. The
  Fourier convention is f̃(k) = ∫ f(x)e^(−ik·x) dx. Lemma 2 is Diaz, Le
  and Robins's theorem for a **bounded** full-dimensional polytope. A
  general ReLU network is not compactly supported, and its outer linear
  regions are unbounded. The paper treats that case as a tempered
  distribution (Appendix C.1, Case 2) and says it generalises the polytope
  construction (footnote 4). Appendix C.2 only restates the bounded case.
- **Eq. 9 and Proposition 2 (C.5).** These assume gradient flow or full-batch
  gradient descent on squared error, with a fixed target. The experiments
  use full-batch **Adam** (A.1, A.2, A.5).
- **Experiments 1, 2, 5, 6 and 7.** Inputs are on a 1-D grid ([0, 1], 200
  points; or the latent grid of a curve, 1000 points). Spectra are the
  single-sided DFT on that grid. The network is 6 layers × 256 ReLU units,
  except in Experiment 7. Results are averaged over 10 runs, which differ
  in the sampled phases.
- **§4.** The data manifold is γ([0, 1]^m) for an injective γ, and the data
  distribution is the image of the uniform distribution on the latent cube.
  "Frequency on the manifold" is frequency in the latent coordinate z, not
  in arclength.

## Key results

Proved (re-derived here for the compact case; see [THEORY-tmpuaxgt](../theory.d/THEORY-tmpuaxgt.md)):

- **Lemma 1.** f̃(k) = i Σ_ε (W_ε k / k²) 1̃_(P_ε)(k), where P_ε are the
  linear regions, W_ε = W^(L+1)W_ε^(L)⋯W_ε^(1) is the gradient on P_ε,
  and k = ‖k‖. The proof applies the divergence theorem to f(x)e^(−ik·x)k.
  The prefactor should be −i: the divergence of f e^(−ik·x) k gives
  k·∇f − ik²f, so f̃ = (1/(ik²))∫k·∇f e^(−ik·x), and the paper's Eq. 26
  divides by −ik² instead. This affects only the phase.
- **Lemma 2 (Diaz et al.).** For a full-dimensional bounded polytope,
  1̃_P(k) = Σ_(n=0)^d D_n(k) 1_(G_n)(k)/k^n, where G_n is the union of the
  n-dimensional subspaces orthogonal to some codimension-n face. The paper
  says D_n is Θ(1) as k → ∞. It is O(1): D_n is a sum of phase terms
  e^(iΦ), which can cancel, as the transform of [a, b] vanishes at
  k = 2πj/(b − a). Its constant also depends on the direction k̂ and
  blows up as k̂ nears an exceptional subspace (the weight
  W_(F,G) = i Proj_F(k)·N_F(G)/‖Proj_F(k)‖² of Eq. 34 does).
- **Theorem 1.** f̃_θ(k) = Σ_(n=0)^d C_n(θ, k) 1_(H_n^θ)(k)/k^(n+1). "In
  almost all directions of R^d, we have a k^(−d−1) decay. However, the
  decay can be as slow as k^(−2) in specific directions orthogonal to the
  d − 1 dimensional faces bounding the linear regions." The exponent is
  fixed by d alone. Width, depth and the size of the weights enter only
  the numerator, which the paper bounds by N_f L_f: the number of linear
  regions times the Lipschitz constant.
- **Proposition 3 (C.6), the Lipschitz bound.**
  ‖W_ε‖ ≤ L_f ≤ Π_(k=1)^(L+1) ‖W^(k)‖ ≤ ‖θ‖_∞^(L+1) √d Π_(k=1)^L d_k. It
  uses ‖W‖ ≤ √(IJ)‖θ‖_∞ for an I × J matrix. This is correct, and loose.
- **Proposition 1 (C.4).** Along a fixed direction, ∂f̃/∂θ decays one
  power of k more slowly than f̃. The reason is that the phase
  e^(ik k̂·x₀) depends on θ through the vertices x₀.

Heuristic (stated as derivations, not proved):

- **Eq. 9.** If f̃ = O(k^(−Δ−1)) along k̂, with 1 ≤ Δ ≤ d, then
  |dh̃(k)/dt| = |∂f̃/∂θ · dθ/dt| = O(k^(−Δ)) for the residual h = f − λ,
  "where we use the fact that dθ/dt … is independent of k". This bounds
  the *speed* at frequency k at each instant. Its constant contains
  N_f L_f, which grows during training (Fig. 1, right). So it does not
  give an order of learning times. Proposition 2 is the single-frequency
  case, ∂h̃(k₀, t)/∂t = O(k₀^(−1)).
- **Appendix D.** Ξ_ε(k) = {θ ∈ Θ : ∃k′ > k, |f̃_θ(k′)| > ε}, with Θ an
  L∞ ball of radius K (the weight clip). The claim is
  vol(Ξ_ε(k))/vol(Θ) = O(k^(−Δ−1)). The proof does not hold (see
  Limitations).
- **Eq. 14–15, C.7.** The latent transform is
  (f∘γ)^(l) = ∫ dk f̃(k) P_γ(l, k), with
  P_γ(l, k) = ∫ dz e^(i(k·γ(z) − l·z)). By stationary phase, the
  important pairs satisfy l = J_γ(z̄)k. Expanding γ in a Fourier series,
  l_ν = −ik Σ_p p_ν k̂_μ γ̃_μ[p] e^(−ip·z). So "we can get arbitrarily large
  frequencies l_i if γ̃_i[p] is large enough for large p, even when k_i is
  fixed". This is the chain rule for instantaneous frequency, stated
  asymptotically.

Experimental:

- **Experiment 1 (Figs. 1, 2, 10).** Target λ(z) = Σ A_i sin(2πk_i z + φ_i),
  with κ = (5, 10, …, 50), 200 points, and 80 000 full-batch Adam steps.
  With A_i = 1, and also with A_i rising from 0.1 to 1, "lower frequencies
  (i.e. smaller k_i's) are regressed first, regardless of their
  amplitudes". The spectral norms of all layers grow throughout training.
- **Experiment 2 (Fig. 3).** After convergence on κ = (10, …, 50), the
  parameters are perturbed to θ* + δθ̂ with θ̂ a random unit vector. The
  perturbed spectrum, normalised by the trained one, collapses first at
  high frequency as δ grows.
- **Experiments 3–4 (Figs. 4, 5, 11, 13).** On MNIST (two classes, inputs
  in [0, 1]^784), a radial wave βsin(k‖x‖) is added to the target. Then
  the best validation loss is hurt by low-frequency noise and barely by
  high-frequency noise, and the validation loss dips early when the noise
  is of high frequency. With a "generalized frequency", the index of the
  Gaussian RBF kernel's eigenvectors on the samples, the dip occurs at
  about iteration 200. That is when the network has fitted τ₀ and not yet
  the high-index noise ψ_γ = Σ (n/N)² φ_n.
- **Experiment 7 (A.5, Figs. 14–18).** Networks are fitted to a sampled δ
  function (a flat spectrum). Depth helps fit high frequencies within
  60 000 steps, much more than width does. A weight clip of 0.1–0.2
  "prevents the network from learning higher frequencies".
- **Experiments 5–6 (Figs. 7–9).** The data lie on the flower curves
  γ_L(z) = (1 + ½sin(2πLz))(cos 2πz, sin 2πz). Regression on frequencies
  20–200 in z, and classification of the sign of sin(2πkz) for
  k = 50–400, both get easier as L grows. For (k, L) = (200, 20), two
  initialisations fit the samples almost perfectly and disagree off the
  curve (Fig. 7).
- **Experiment 8 (A.6, Fig. 19).** White-noise labels are regressed on
  MNIST reconstructions from a 64-feature denoising autoencoder, and on
  points of a 64-dimensional coordinate hyperplane in [0, 1]^784. Training
  loss falls faster on the MNIST reconstructions (blue below green in
  Fig. 19). The text's lead sentence, "harder to solve if the input
  samples lie on the same manifold", is garbled; the figure gives the
  direction.
- **Experiment 9 (A.7, Figs. 20–21).** AutoNEB finds paths between
  same-class CIFAR-10 training and adversarial images that a ResNet-20
  classifies the same all the way, "with an average length (3.0 ± 0.3)%
  longer than the linear connection".
- **Appendix E (Fig. 22).** The DNN's radial spectrum on the L = 20,
  k = 150 task decays faster than k-NN's for K = 5–20. k-NN's accuracy does
  not improve with L.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Fourier transform of a ReLU network falls as k^(−d−1) along almost every direction, and no slower than k^(−2) along any | strong for compactly supported networks; not shown for general ones | Lemmas 1–2 and Theorem 1. Re-derived for the bounded case in [THEORY-tmpuaxgt](../theory.d/THEORY-tmpuaxgt.md), with D_n = O(1) rather than Θ(1). For unbounded networks see Limitations |
| C2 | Networks learn lower frequencies first, regardless of amplitude | moderate, for the setting tested | Experiment 1, one architecture, 1-D, full-batch Adam, 10 runs; Experiment 7 and the MNIST experiments are consistent |
| C3 | The decay of the spectrum explains the order, because the speed at frequency k is O(k^(−Δ)) | weak | Eq. 9 is an instantaneous upper bound whose constant grows during training; it gives no comparison of fitting times |
| C4 | Higher frequencies are less robust to random parameter perturbation | moderate, empirically | Experiment 2 (Fig. 3) |
| C5 | Parameters expressing frequencies above k occupy a fraction O(k^(−Δ−1)) of the parameter ball | unsupported as proved | Appendix D. Remark 2 is false as stated, and the integral step needs a bound uniform in θ that Theorem 1 does not give |
| C6 | Spectral bias persists in high-dimensional real data | moderate | Experiments 3–4 on MNIST; the frequencies are proxies (a radial wave; RBF eigenvector index) |
| C7 | High latent frequencies get easier to learn as the manifold's shape gets more complex | weak as an explanation, strong as an observation | Experiments 5–6 show the effect; the curves' lengths grow with L, and that alone accounts for most of it (see Limitations) |
| C8 | The latent frequency reachable from input frequency k scales with the embedding's derivatives, l = J_γ(z̄)k | moderate | stationary phase (C.7); it is the chain rule, and holds asymptotically |
| C9 | Depth helps a network fit high frequencies far more than width, and a weight clip prevents it | moderate, qualitative | Experiment 7, one target, one run per setting shown |
| C10 | All same-class CIFAR-10 images, adversarial ones included, are joined by paths of constant prediction | moderate for the pairs tried | Experiment 9; 50 images per class and 50 adversarials; it does not test spectral bias directly |

## Concepts

- **Spectral bias.** "These networks prioritize learning the low frequency
  modes." It is defined by the order of learning, and "manifests itself
  not just in the process of learning, but also in the parameterization
  of the model itself" (robustness). It is not defined as a property of
  the minimum reached.
- **Frequency.** In §§2–3 this is the Fourier frequency in input
  coordinates. In Experiment 4 it is the index n of the Gaussian RBF
  kernel's eigenvectors on the samples, sorted by decreasing eigenvalue.
  In §4 it is frequency in the latent coordinate z. Three different
  things are called by the one word.
- **Linear region / activation pattern.** A maximal set on which every
  hidden unit keeps its sign. The network is affine on it, with gradient
  W_ε (Lemma 3).
- **Face poset.** Diaz et al.'s bookkeeping for the recursion. Each path
  P = F₀ → F₁ → … descends one dimension per step and contributes a
  factor O(1/k) per step until it reaches a face to which k is
  orthogonal.
- **P_γ(l, k).** The kernel carrying input frequency k to latent
  frequency l through the embedding γ.

## Connections

Contemporaneous with Xu, Zhang and Xiao's "frequency principle" (2018),
which the paper credits as concurrent and independent, and followed by
Xu's analysis of two-layer sigmoid networks. It builds on the
linear-region counts of Montúfar et al. and Raghu et al., the polytope
transform of Diaz, Le and Robins, and Arora et al.'s result that every
CPWL function is a ReLU network. It frames itself as a first step
towards formalising Arpit et al.'s observation that networks fit simple
patterns before memorising. In this record its kernel-regime successors
are already read: Cao et al. ([LIT-624](../literature.d/LIT-624.md), [NOTE-483](NOTE-483.md)), Basri et al.
([LIT-612](../literature.d/LIT-612.md), [NOTE-481](NOTE-481.md)) and Bietti and Bach ([LIT-608](../literature.d/LIT-608.md), [NOTE-475](NOTE-475.md)), assembled
in [THEORY-086](../theory.d/THEORY-086.md). [NOTE-777](NOTE-777.md) (Belrose et al., [LIT-952](../literature.d/LIT-952.md)) places itself
beside this paper.

## Bearing on the record

**What it adds beyond [THEORY-086](../theory.d/THEORY-086.md).**

- **A different object.** [THEORY-086](../theory.d/THEORY-086.md)'s k^(−d) is the decay of the NTK's
  *eigenvalues*, which are learning rates, on S^(d−1) with uniform data,
  in the kernel regime. This paper's k^(−d−1) is the decay of the Fourier
  transform *of the network function itself*, at any parameters, any
  width, in R^d. The two exponents are not the same statement: one is a
  rate of learning, the other a limit on what the function contains.
  They should not be cited as agreeing or as differing.
- **It holds outside the kernel regime, but says less.** The
  representational bound holds for every finite network. The only
  bridge to learning dynamics is Eq. 9, a bound on speed whose constant
  moves. [THEORY-086](../theory.d/THEORY-086.md) has a theorem about order where this paper has a
  heuristic; this paper has experiments outside the kernel regime where
  [THEORY-086](../theory.d/THEORY-086.md) has none, beyond Basri et al.'s residual networks.
- **Depth.** [THEORY-086](../theory.d/THEORY-086.md) says depth does not change the NTK's decay
  exponent. Theorem 1's exponent does not depend on depth either, and
  depth enters only through N_f L_f. Experiment 7 then finds that depth
  helps fit high frequencies in finite training. These are consistent.
  The empirical depth effect is a statement about constants and about
  training beyond the kernel regime, which [THEORY-086](../theory.d/THEORY-086.md) does not cover.
- **Robustness and manifolds.** [THEORY-086](../theory.d/THEORY-086.md) says nothing about
  either.

**What it adds beyond [THEORY-186](../theory.d/THEORY-186.md) (and [THEORY-740](../theory.d/THEORY-740.md)).** In the deep
linear network the order of acquisition is by the *data's* singular
values: a stronger mode is learned first, whatever it means. Experiment 1
with rising amplitudes is a case where the order is not by strength. A
tenfold weaker low frequency is fitted before a stronger high one. So
the order belongs to the learner's own spectrum, as in the kernel regime,
not to the target's. In a finite nonlinear network trained with Adam the
learner's preference beat a tenfold amplitude difference. That is filed
as [THEORY-tmpon8ox](../theory.d/THEORY-tmpon8ox.md), Proposed. It is one study.

**[QUESTION-tmp8qovh](../questions.d/QUESTION-tmp8qovh.md).** This reading gives the question a second
fact about acquisition and nothing about refinement or relevance:

- *Acquisition is ordered by the operator, not by the target's strength*,
  in this setting ([THEORY-tmpon8ox](../theory.d/THEORY-tmpon8ox.md)). Combined with [THEORY-186](../theory.d/THEORY-186.md), the
  "strength" that orders acquisition is a product of the learner's
  spectrum and the data's. In a deep linear network with white inputs the
  learner is flat and the data decide. In a ReLU network on a 1-D grid
  the learner's frequency preference dominated across a tenfold range.
  Neither the paper nor the record has a formula for the product outside
  the kernel regime.
- *Acquisition by frequency is not acquisition by refinement.* The
  Fourier bands of a sum of sinusoids are not a refinement chain in A2's
  sense: no band is a function of another. The paper's order is the
  "dynamical" order of A2 with no "structural" partner. To be a
  coarse-to-fine chain, the levels would have to be low-pass truncations,
  and then refinement holds by construction, as in [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md).
- *The order is coordinate-dependent.* §4 shows that "low frequency" is
  relative to the coordinates in which the network is smooth. The same
  latent signal is low or high frequency depending on the embedding. So
  an acquisition order by frequency is a property of the learner *and*
  the embedding, not of the target. This parallels [THEORY-tmp3xg7a](../theory.d/THEORY-tmp3xg7a.md)'s
  finding that the diffusion order depends on the normalisation α.
- *Relevance.* Experiments 3–4 show high-frequency label noise fitted
  last. This is a case where acquisition order and relevance to the
  *clean* target agree, but only because the noise was made high
  frequency by design. Low-frequency noise is fitted first, and there
  they disagree.

**Is it ML practice?** The paper gives no instruction for practice. It
describes a bias, mentions adversarial training and mixup as restricting
the solution space without recommending them, and compares DNNs, kernel
machines and k-NN (Appendix E) as an evaluation, not advice. So it is
not sent to the anthology on the instruction criterion. It is about how
deep networks train, which an anthology topic could hold, so the
`anthology-candidate` flag on [LIT-tmpzunec](../literature.d/LIT-tmpzunec.md) is right. It is held here for
this record's own question about orders of acquisition, as the LIT says.

## Limitations

- **Theorem 1 is proved only for compactly supported networks.** A
  general ReLU network grows linearly, and its outer regions are
  unbounded. Lemma 2 is a theorem about bounded polytopes. For unbounded
  regions the transform is a distribution, and it can be singular on
  lower-dimensional subspaces rather than decaying. A two-layer network
  Σ a_j max(0, w_j·x + b_j) on R^d has a transform supported on the lines
  spanned by the w_j (the paper cites Eldan and Shamir for this). Away
  from those lines it is zero, so "k^(−d−1) in almost all directions"
  holds vacuously, and on the lines it is a measure, not a k^(−2) decay.
  Restricting a network to a bounded input box does not rescue it either.
  f·1_B is discontinuous on ∂B, so its transform falls only as k^(−1)
  along the box's normals. What the experiments measure is a DFT on a
  grid, which is neither.
- **Θ(1) should be O(1).** The phase sums D_n and C_n can vanish, and
  their constants depend on direction without a uniform bound.
- **Eq. 9 does not give an order.** It bounds |dh̃(k)/dt| from above at
  each instant, with a constant that grows as N_f L_f grows. It does not
  compare the times at which frequencies are fitted, and it assumes
  gradient descent, while the experiments use Adam.
- **Appendix D's volume result does not follow.** Remark 2 says
  1_k(θ) ≤ |f̃_θ(k)| for large k. But 1_k(θ) = 1 only says that some
  k′ > k has |f̃_θ(k′)| > ε. The true inequality is
  1_k(θ) ≤ sup_(k′>k)|f̃_θ(k′)|/ε. The final step
  ∫_Θ|f̃_θ(k)| dθ = O(k^(−Δ−1)) vol(Θ) needs a constant uniform over θ ∈ Θ.
  Theorem 1's constant depends on θ, through the regions and through how
  near k̂ lies to their faces' normals, and Δ itself depends on θ. What
  does follow is weaker: for fixed k̂, vol(Ξ_ε(k)) → 0 as k → ∞, by
  dominated convergence from Lemma 4.
- **§4 confounds shape with length.** The flower γ_L gets longer as L
  grows. Its arclength is 6.3 at L = 0, 10.6 at L = 4, 21.5 at L = 10,
  33.1 at L = 16 and 40.9 at L = 20 (computed here). The latent target
  sin(2πkz) is uniform in z, so on a longer curve the same k has more
  arclength per cycle. A fixed input-space wave sin(2π·5·x₁), pulled back
  to z, has a latent band holding 99% of its power of 33, 71, 159, 255 and
  319 for those L. That is roughly proportional to arclength (5.3 to 7.8
  cycles per unit length). The paper's own mechanism, l = J_γk, says the
  same thing: what matters is the speed |γ′|. Curvature, number of
  petals or "complexity" enter only through it. No experiment holds
  length fixed while varying shape, so "manifold complexity" is not
  isolated from "a longer curve in a bounded box".
- **"Easier" means easier to fit.** Experiments 5, 6 and 8 report training
  loss and training accuracy. Fig. 7 shows that two initialisations fitted
  equally well disagree off the curve, which is the opposite of
  evidence for generalisation.
- **Experiment 8 is not controlled for scale.** The hyperplane points are
  uniform in [0, 1]^64 with the other 720 coordinates zero. The
  autoencoder reconstructions have a different norm, spread and
  pairwise distance distribution, and any of these changes how fast
  noise is fitted.
- **Single settings.** Experiments 1, 2, 5 and 6 use one architecture and
  one optimiser, on 1-D latent grids, with 10 runs. The MNIST
  experiments use proxy frequencies: a radial wave, and the RBF
  eigenvector index, whose link to Fourier frequency is shown only for 50
  uniform points on [0, 1] (Fig. 6).
- **Minor errors.** In Lemma 1 the sign of i is wrong (above). Appendix
  A.4 sorts the eigenvalues increasing (λ₁ ≤ … ≤ λ_N) and the text
  sorts them decreasing. It also refers to a "Figure ?". A.2 says the 10
  runs differ in "the sampled z_i's", which are a fixed uniform grid; the
  phases are what vary. Eq. 14 drops the (2π)^(−d/2) normalisation, and
  its kernel uses e^(+ik·γ) against §2's e^(−ik·x).

## Open questions

- Does the order by frequency survive when the target's amplitudes rise
  faster than tenfold? At what ratio, if any, does a strong high
  frequency get fitted before a weak low one? A per-frequency
  fitting-time curve against amplitude ratio would locate the crossover
  between [THEORY-186](../theory.d/THEORY-186.md)'s order by strength and this paper's order by
  frequency.
- Is there a theorem for finite ReLU networks outside the kernel regime
  that orders fitting times by frequency? Eq. 9 would need a lower bound
  on the speed at low frequency, not only an upper bound at high
  frequency.
- Does manifold shape matter once arclength is fixed? Curves of equal
  length and bounding box, with different curvature profiles, would
  separate the two. The paper's Experiments 5–6 cannot.
- How does Theorem 1 read for a network on a bounded domain with a
  smooth window? That is the version that would connect it to the DFT
  measurements.
