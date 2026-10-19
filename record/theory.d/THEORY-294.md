---
number: 294
status: Proposed
formerly:
- THEORY-tmpye6gw
promote_when: >-
  A result beyond the one-dimensional case where the NTK and the NNGP
  differ by more than a within-class rescaling. That could be a derivation
  for multi-dimensional or multi-class data, or a measurement of NC1, with
  a stated metric, on networks trained in a verified lazy regime (the
  tangent kernel measured to stay fixed) on real data. The measurement
  should show NC1 staying at its initial value while the same
  architecture, trained out of the lazy regime, collapses. The account is
  refuted by a lazy-regime network, kernel verified static, whose hidden
  features' NC1 falls substantially below its value at initialization.
  More Gaussian-mixture simulations of NNGP against NTK cannot settle it,
  and neither can finite networks whose regime is not checked.
title: 'Lazy-regime training of a wide shallow network does not collapse its features: on two-class Gaussian data the expected within-class variability of the NTK features is that of the NNGP features at initialization'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-985
answers:
- QUESTION-051
summary: >-
  Kothapalli & Tirer (2024), [LIT-985](../literature.d/LIT-985.md), read in [NOTE-774](../notes.d/NOTE-774.md). NC1 =
  tr Σ_W / tr Σ_B of kernel-defined features is a closed function of the
  kernel matrix (Theorem 4.1). For one-dimensional data, two classes on
  opposite sides of the origin and zero bias, the ReLU NTK of a wide
  two-layer net is a within-class rescaling of the NNGP kernel. So the
  expected NC1 is the same (Theorem 5.1). In higher dimensions it is
  measured no lower, and for ReLU higher. A narrow theorem with a
  suggestive generalization. The inference that collapse requires feature
  learning is the reading's, not proved.
---
<!-- inactive-ok-file: THEORY-083 THEORY-212 THEORY-286 — Proposed; the record's statement of collapse, its lazy-versus-rich regime and NTK-spectrum accounts, and the two UFM accounts filed today -->

# THEORY-294: Lazy-regime training of a wide shallow network does not collapse its features: on two-class Gaussian data the expected within-class variability of the NTK features is that of the NNGP features at initialization

## Source

Kothapalli & Tirer (2024, TMLR 2025), [LIT-985](../literature.d/LIT-985.md), read in [NOTE-774](../notes.d/NOTE-774.md):
Theorem 4.1, Theorem 5.1 with its proof (Appendix D, Eqs. 49–57),
Figures 2–3, and Appendices E–G.

## What was actually shown

**The formula.** For features with inner products Q(x, x′) = hᵀh′, the
traces of the within-class and between-class covariances are explicit sums
over the class blocks of the kernel matrix (Theorem 4.1). So
NC1 = tr Σ_W / tr Σ_B can be computed for the features of any kernel
without the features themselves.

**The theorem.** Take a two-layer net in the infinite-width limit with
ReLU activation and zero bias variance. Take one-dimensional data, two
classes N(μ₁, σ₁²) and N(μ₂, σ₂²) with μ₁ < 0 < μ₂ and |μ_c| ≫ σ_c, so every
cross-class product x x′ is negative. Then:

- the NNGP post-activation kernel is (σ_w²/2)xx′ within a class and 0
  across (Eq. 54);
- the NTK is (σ_w⁴/2 + σ_w²/2)xx′ within a class and 0 across (Eq. 56);
- so E[NC1(H_NTK)] = E[NC1(H_GP)] =
  Σ_c[(n_cμ_c² + n_cσ_c²)/N − μ_c²/2] / Σ_c[μ_c²/2 − n_c²μ_c²/N²] +
  Δ_h.o.t. (Theorem 5.1, Eq. 57).

The NTK describes the features a wide net keeps throughout gradient
descent with a small learning rate. The NNGP describes them at
initialization. So in this setting lazy training leaves within-class
variability exactly where initialization put it. For Erf the same
comparison holds approximately, by expansion (Appendix E).

**The measurements.** On two-class Gaussian mixtures in d₀ up to 128, the
NTK's NC1 tracks the NNGP's with Erf and exceeds it with ReLU (Figures
2–3). So the NTK is not more collapsed anywhere tested. A data-aware kernel
(Seroussi et al.'s equations of state) does fall below the NNGP at width
500, where finite networks also fall (Figure 4). The measurement could
have gone the other way: the NTK could have shown lower NC1 with
dimension, as the finite nets sometimes do.

## What this does not say

- **It does not prove the result beyond its setting.** The theorem has
  one input dimension, two classes split by the origin, and zero bias.
  There the NTK is a within-class rescaling of the NNGP, so the equality
  is nearly structural. Everything else is simulation on Gaussian
  mixtures.
- **It does not show that feature learning produces collapse.** The paper
  shows the lazy regime does not. Its candidate for the alternative, the
  data-aware kernel, tracks finite networks on separable data. It fails
  under class overlap in high dimension and under imbalance, where the two
  move in opposite directions (Figures 5, 12, 13).
- **It does not use [LIT-618](../literature.d/LIT-618.md)'s metric or regime.** NC1 here is
  tr Σ_W / tr Σ_B, and the networks are two-layer, binary and MSE-trained
  for 1000 steps. That is not the terminal phase of deep cross-entropy
  training that [THEORY-083](THEORY-083.md) describes.
- **It does not say features become more collapsed than the data.** In
  Appendix F the kernel features are about half as collapsed as the raw
  inputs, by the relative metric, when the classes are symmetric.

## Connections

- **[THEORY-212](THEORY-212.md)** says that with strongly unbalanced layers a two-layer
  linear net learns with a static kernel and leaves the larger layer
  task-agnostic. This account is the collapse-side counterpart: a static
  kernel leaves within-class variability unchanged.
- **[THEORY-086](THEORY-086.md)** describes what kernel-regime gradient descent *does* fit:
  the target, eigenspace by eigenspace. Fitting the target in the lazy
  regime does not reorganize the features. This account adds that in
  particular it does not collapse them.
- **[THEORY-278](THEORY-278.md) and [THEORY-286](THEORY-286.md)** derive collapse in
  unconstrained-features models, where nothing but the labels shapes the
  features. This account is the record's only one where the data enter,
  and what it finds is a negative.
- **[THEORY-083](THEORY-083.md).** If this account holds generally, the terminal-phase
  collapse [THEORY-083](THEORY-083.md) measures is a signature of training outside the lazy
  regime.
