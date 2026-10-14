---
number: 759
status: Read
formerly:
- NOTE-tmp4idzz
paper: LIT-976
title: 'Bird — Emergence of Quantised Representations Isolated to Anisotropic Functions'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (arxiv.org/pdf/2507.12070, v4 of
    2026-01-26, 47 pp.; earlier versions are v1 2025-07-16, v2 2025-07-30
    and v3 2025-09-04), text extracted with pdftotext: §§1–5 and
    Appendices A (statistical artefacts of the method), B (width, depth,
    latent layer, Leaky-ReLU, hyperoctahedral Leaky-ReLU, MNIST), C
    (theory for other architectures, the first-order gradient analysis
    and the "affine divergence", speculated pathologies), D
    (reconstruction error), E (architectures and training) and F
    (notation). The results are density plots with no text layer, so what
    they show was read from captions and text. Fig. 16's caption did not
    extract. The Zenodo deposit was not compared with v4.
date: '2026-10-14'
summary: >-
  In small CIFAR and MNIST autoencoders built from orthogonally
  equivariant parts except the activation, elementwise tanh and
  Leaky-ReLU drive latent representations into narrow beams along or
  against the standard basis, arranged by each activation's symmetry
  group. Radial (O(n)-equivariant) versions of the same functions leave
  them spread. The beams appear even in the first latent layer, which no
  activation precedes. The evidence is visual, five seeds a condition,
  with no statistic.
---
<!-- inactive-ok-file: THEORY-184 THEORY-017 THEORY-022 THEORY-210 THEORY-083 THEORY-288 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-759: Bird — Emergence of Quantised Representations Isolated to Anisotropic Functions

## Contribution

The paper makes an ablation in which the activation function is the only
part of a network that singles out a basis. Encoder, decoder and hidden
maps are affine, initialised by rotation-invariant Xavier-normal weights
and zero biases, and trained by momentum SGD on mean-squared
reconstruction, all of which commute with rotations. Changing the
activation from an elementwise form to a radial one switches
basis-aligned clustering of the latent representations on and off. It
also introduces a visualisation, the privileged-plane projective (PPP)
method, to see that clustering.

## Key insight

An elementwise nonlinearity is equivariant only to a finite group, the
signed permutations B_n for tanh and the permutations S_n for Leaky-ReLU.
It gives the representation space a frame, and training moves
representations toward the frame's directions, even upstream of the
nonlinearity. An O(n)-equivariant nonlinearity must be radial,
f(x) = h(‖x‖)x̂, and gives no frame. So the axis-aligned, near-discrete
structure seen in such networks is put there by the primitive, not found
in the data.

## Assumptions

- **Setting.** Autoencoders on CIFAR-10 (3,072-d) or MNIST (784-d):
  - an affine encoder to width n ∈ {12, 18, 24, 32};
  - L ∈ {0, 1, 2, 3} hidden blocks, each an activation then an n → n
    affine map;
  - an activation and an affine decoder.
- **Training.** Batch 24, momentum 0.9, learning rate 0.08, MSE loss,
  float64, 125 epochs. Xavier-normal weights, zero biases.
- **Inputs.** Main-text results use raw [0, 1] pixels. Appendix results
  standardise each pixel over the training set.
- **The activation pairs.**
  - Elementwise tanh, Σᵢ tanh(x·êᵢ)êᵢ, B_n-equivariant, against
    isotropic tanh, tanh(‖x‖)x̂, O(n)-equivariant. The two agree on the
    basis directions.
  - Elementwise Leaky-ReLU (α = 10⁻²), S_n-equivariant, against an
    isotropic Leaky-ReLU, αx inside the ball ‖x‖ < ε = 1 and outside it
    printed as x − (1 − α)ε. That is dimensionally a vector minus a scalar,
    presumably x − (1 − α)εx̂.
  - Two B_n Leaky-ReLUs: an elementwise one with a dead zone (Eq. 9) and
    a max-norm one (Eq. 10).
- **The measurement.** For a chosen basis, all pairs of basis vectors span
  planes. A representation is plotted in a plane if
  ‖v_∥‖/‖v‖ > ε = 0.75. Densities are summed over all planes. The basis
  measured is the standard one unless stated.
- **The latent layer studied** is usually layer 0, after the encoder and
  before any activation.

## Key results

- **Tanh, raw CIFAR, width 18 (Fig. 1).**
  - Over 125 epochs the five elementwise-tanh networks form "distinct,
    highly dense, approximately discrete" beams along (horizontal and
    vertical) or against (diagonal) the basis directions.
  - The five isotropic-tanh networks stay "circularly symmetric,
    continuous", becoming less clustered with training.
  - The only number given: about 2,000 representations pass the PPP
    threshold early in training and in all isotropic networks, against
    about 200,000 late in anisotropic training, two orders of magnitude.
- **Deeper networks (Fig. 2, three hidden blocks).**
  - Anisotropic beams drift and merge onto the axes during training.
  - Isotropic networks form some clusters, but not along the basis (rows
    6, 8 and 9). The author reads these as task-driven.
- **Leaky-ReLU (Fig. 3, Figs. 18–21).** The same contrast holds.
  - Elementwise Leaky-ReLU at layer 0 "always" gives two antipodal beams
    on one diagonal, the ±1 direction.
  - The author ties this to S_n lacking sign flips. Only the orthant of
    1 is mapped by the identity, and its share of the domain is 2⁻ⁿ.
- **Hyperoctahedral Leaky-ReLU (Figs. 22–27).** Basis-aligned beams like
  hyperoctahedral tanh's, and unlike S_n Leaky-ReLU's. This is the
  paper's best evidence that the group, not the function's other
  properties, predicts the arrangement. Fig. 25 is the cleanest instance.
- **Width (Figs. 8–10).** With width, isotropic densities thin out, as a
  spread distribution over a growing sphere should. Anisotropic ones
  concentrate more about the axes. At width 12 some anisotropic networks
  instead avoid the axes.
- **Later layers (App. B.3).** Anisotropic structure usually sharpens with
  layer and isotropic structure smooths, with exceptions (Fig. 17).
- **MNIST (App. B.5).** Same contrast, fainter (Figs. 28–30).
- **Controls on the method (App. A).**
  - PPP of Gaussian samples with random orthogonal bases shows small
    spurious over- and under-densities along the basis, because planes
    overlap there.
  - Uniform [0, 1] data under a random linear map gives spurious
    antipodal clusters. Per-pixel standardisation removes most of it.
  - Neither artefact produces the late-training beams, and both apply to
    the two arms alike.
- **First-order mechanism (App. C.2).** One step on a single affine layer
  moves the pre-activation by Δz = −η(‖x‖² + 1)J_fᵀg.
  - Elementwise: J_f = diag(ψ′), so the step is ψ′ ⊙ g, each component
    rescaled separately according to the orthant.
  - Radial: J_f = (ϕ′(r) − ϕ(r)/r)x̂x̂ᵀ + (ϕ(r)/r)I, so the step is a
    multiple of g plus a radial term, the same in every direction.
  - The author offers this as a description of how symmetry enters, not a
    derivation of beams.
- **"Affine divergence" (App. C.2.1).** The factor (‖x‖² + 1) makes the
  realised step on z differ from −η∂L/∂z per sample. The author proposes
  z = (Wx + b)/√(1 + ‖x‖²) as a correction. Speculative and untested.
- **Reconstruction (App. D).** With standardised inputs, isotropic networks
  reach lower test error than elementwise ones in every tanh
  configuration shown (Fig. 31), and in all Leaky-ReLU cases (Fig. 36).
  Without standardisation the result is mixed (Figs. 32–33). Five seeds
  each. The author calls this preliminary.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In these autoencoders, elementwise activations produce basis-aligned near-discrete latent clusters that radial ones do not | moderate | paired ablations, five seeds each, many widths, depths, layers and two datasets; visual only, one threshold count |
| C2 | The effect reaches layers that no activation precedes | moderate | layer-0 measurements throughout |
| C3 | The arrangement follows the activation's symmetry group (B_n against S_n) more than its functional form | weak to moderate | two function families and two B_n Leaky-ReLUs; qualitative comparison of plots |
| C4 | The discrete clusters are a prerequisite for grandmother neurons, superposition and possibly neural collapse | weak | argued by connection to the author's earlier SRM paper, not tested |
| C5 | Isotropic activations reconstruct better | weak | preliminary error curves, mixed without standardisation |
| C6 | The component-wise Jacobian deflects updates per orthant and so creates attractors | weak | first-order single-layer calculation, App. C.2 |

## Method

The PPP method:

1. For a set of unit vectors b̂ᵢ (usually the standard basis), take each
   pair and orthonormalise it, ê₁ = b̂₁ and ê₂ ∝ b̂₂ − (b̂₂·b̂₁)b̂₁.
2. Project each representation onto the plane by the pseudo-inverse.
3. Keep it if ‖v_∥‖/‖v‖ > ε.
4. Place a narrow Gaussian at its in-plane coordinates and sum over all
   planes and all representations.

The colour scale is fixed per row, so early-training density can be
invisible next to late-training beams. A random subset of size N^0.9 was
plotted where N was large.

## Concepts

- **Anisotropic / isotropic function.** One whose maximal algebraic
  equivariance group is discrete (S_n, B_n) or the orthogonal group O(n).
  It is a property of the map's form, not of any distribution.
- **Distinguished directions / privileged basis.** The directions an
  anisotropic form singles out.
- **Quantisation.** Representations collapsing from a continuous spread
  into a few narrow beams.
- **Task-agnostic structure.** Structure that recurs across seeds and
  datasets in the arrangement fixed by the primitive's group. The author
  distinguishes it from clustering the task calls for.

## Connections

The paper continues the author's Spotlight Resonance Method (ICLR 2025
workshop), which found alignment to the activation's basis and that it
moves when the basis is rotated, and his "Isotropic Deep Learning"
(Zenodo 2025), which proposed the radial primitives and predicted this
result. It cites Elhage et al.'s toy models of superposition for the
privileged basis, Godfrey et al. on network symmetries, and Papyan et al.
on neural collapse.

## Bearing on the record

- **[QUESTION-058](../questions.d/QUESTION-058.md)** lists the architecture as a possible source of a
  group in a representation. This paper isolates the activation as such a
  source. The beams are arranged by B_n or S_n, groups with no counterpart
  in reconstructing CIFAR or MNIST, and they vanish when the activation is
  made O(n)-equivariant. So a discrete group read off a trained network can
  be the network's own. [LIT-976](../literature.d/LIT-976.md)'s filing note said the paper finds
  that "the algebraic symmetry of network primitives predicts
  task-agnostic representational structure". That is a fair summary of
  the claim. The support is visual, from small autoencoders, with the
  B_n/S_n distinction resting on one family's comparison.
- **[THEORY-184](../theory.d/THEORY-184.md)** shows that a permutation-equivariant update preserves
  the symmetry it starts with. Bird's elementwise networks have the same
  permutation symmetry, yet their representations move from spread to
  concentrated. [THEORY-184](../theory.d/THEORY-184.md) constrains distances between neurons, while
  Bird reports the distribution of examples in the neuron basis, so the
  two do not conflict. Together they say that the update keeps the group
  and the primitive imprints it on the data's representation.
- **[THEORY-017](../theory.d/THEORY-017.md)** holds that a basis is extra data supplied from outside
  the space. Bird gives a learned case in which the basis is supplied by
  the activation: with only rotation-equivariant parts, no direction is
  privileged, and the training procedure is rotation-equivariant in
  distribution. That last step is the record's inference from the setup,
  not the paper's statement.
- **[THEORY-022](../theory.d/THEORY-022.md)** says the group in the grokking network "comes from the
  task, not the network". Bird shows the opposite source for a different
  kind of structure: discrete axis alignment, not characters. The two are
  compatible, but [THEORY-022](../theory.d/THEORY-022.md)'s "not the network" should not be read as
  general.
- **[THEORY-210](../theory.d/THEORY-210.md).** In the isotropic networks every hidden layer has an
  O(n) gauge, a continuous symmetry, and the paper's conjecture that they
  depend less on initialisation is the kind of claim [THEORY-210](../theory.d/THEORY-210.md) bears on.
  Bird does not test it.
- **[THEORY-083](../theory.d/THEORY-083.md)** (neural collapse). Bird uses autoencoders to avoid the
  permutation symmetry of one-hot heads, and speculates that collapse
  is related. It is not tested.
- **Filed from this reading:** [THEORY-288](../theory.d/THEORY-288.md).
- The recommendations to re-evaluate activation functions, to prefer
  isotropic primitives for generative models, and to correct the affine
  map are machine-learning practice and belong to the anthology.

## Limitations

- **No statistic.** The comparisons are density plots. The author says
  quantitative measures "may further strengthen the certainty" and leaves
  them to future work. The only count is the about-100× rise in
  above-threshold samples.
- **Small models.** Widths up to 32 and depths up to 3 hidden blocks, on
  CIFAR and MNIST only. Transformers, convolutions and residual networks
  are discussed (App. C.1) but not run.
- **The isolation is of a pair, not of symmetry alone.** Every
  O(n)-equivariant map is radial, so each pair also contrasts
  coordinate-wise against radial nonlinearity. The hyperoctahedral
  Leaky-ReLU results are the evidence that the group matters beyond that.
  They are qualitative.
- **Artefacts.** The method has known biases along the basis it measures
  in, discussed and partly controlled in App. A.
- **Single author, unrefereed.** The paper was revised three times; v4
  was read.
- The downstream claims (grandmother neurons, superposition, neural
  collapse) and the pathologies (adversarial fragility, capacity) are
  conjectures here.

## Open questions

- A statistic for beam formation, with seeds and a null from random
  orthogonal bases, so that the contrast has an effect size.
- Whether a network with the even-sign-flip group D_n, between S_n and
  B_n, shows an intermediate arrangement. The author's attempt failed to
  train.
- Whether the effect persists in classifiers and in large models, where
  residual connections, normalisation and attention each bring their own
  symmetry.
