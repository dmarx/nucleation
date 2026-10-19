---
number: 294
status: Active
formerly:
- THEORY-tmpye6gw
title: "For a wide two-layer ReLU network with zero bias on one-dimensional data whose two classes lie on opposite sides of the origin, the tangent kernel is a constant multiple of the initialization kernel, so lazy training leaves the within-class variability of its features, NC1, where initialization put it"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-294 (batch 045, ADR-047 v2). The dated note below re-derives
    Theorem 5.1: both kernels are a constant times x·x′ within a class and
    zero across, and NC1 is a ratio of linear functionals of the kernel, so
    it is unchanged. The title is held to that setting; "does not collapse
    its features" in general and "on two-class Gaussian data" are dropped.
    The promote_when moves to QUESTION-tmpx46z2.
tags:
- learning-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-985
answers:
- QUESTION-051
summary: >-
  Kothapalli & Tirer (2024), [LIT-985](../literature.d/LIT-985.md), read in [NOTE-774](../notes.d/NOTE-774.md). NC1 = tr Σ_W / tr
  Σ_B of kernel-defined features is a ratio of linear functionals of the
  kernel matrix (Theorem 4.1). For one-dimensional data, two classes on
  opposite sides of the origin and zero bias, the ReLU tangent kernel of a
  wide two-layer net is a constant multiple of the NNGP kernel, so NC1 is
  the same (Theorem 5.1, re-derived). In higher dimensions it is measured
  no lower, and for ReLU higher; whether lazy training leaves NC1 in place
  there is [QUESTION-tmpx46z2](../questions.d/QUESTION-tmpx46z2.md). The inference that collapse requires feature
  learning is the reading's, not proved.
---
<!-- inactive-ok-file: THEORY-083 THEORY-212 THEORY-286 — Proposed; the record's statement of collapse, its lazy-versus-rich regime and NTK-spectrum accounts, and the two UFM accounts filed today -->

# THEORY-294: For a wide two-layer ReLU network with zero bias on one-dimensional data whose two classes lie on opposite sides of the origin, the tangent kernel is a constant multiple of the initialization kernel, so lazy training leaves the within-class variability of its features, NC1, where initialization put it

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

## Note of 2026-10-19: Theorem 5.1, re-derived

Re-derived for the promotion audit (batch 045, [ADR-047](../decisions.d/ADR-047.md) v2), in the
theorem's setting. The network is two-layer ReLU in the infinite-width
limit with zero bias. The inputs are one-dimensional, in two classes, and
every product x·x′ of inputs from different classes is negative.

1. **Both kernels are homogeneous.** For scalar inputs and
   w ~ N(0, σ_w²), relu(wx)·relu(wx′) is zero whenever x and x′ have
   opposite signs. When they share a sign it is w²·xx′·1{wx > 0}. So the
   NNGP post-activation kernel is c₁·xx′ within a class and 0 across. The
   weight-gradient term of the tangent kernel is
   E[a²]·P(wx > 0, wx′ > 0)·xx′, which is likewise c₂·xx′ within a class
   and 0 across. So the tangent kernel is κ times the NNGP kernel,
   entry by entry, for a constant κ > 0. In the paper's parametrisation
   κ = σ_w² + 1 (Eqs. 54 and 56).
2. **NC1 does not see the constant.** By Theorem 4.1, tr Σ_W and
   tr Σ_B of kernel features are linear functionals of the kernel matrix.
   Multiplying the kernel by κ multiplies both by κ and leaves their ratio
   unchanged.

So NC1 of the tangent-kernel features equals NC1 of the
initialization-kernel features for every sample that meets the sign
condition, not only in expectation. Eq. 57's closed form follows, with
its correction for samples where some cross-class product is not
negative. Nothing in the argument survives once the kernels stop being
proportional, as they do beyond one dimension. That wider case, which the
promote_when asked for, is [QUESTION-tmpx46z2](../questions.d/QUESTION-tmpx46z2.md).
