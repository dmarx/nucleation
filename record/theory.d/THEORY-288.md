---
number: 288
status: Proposed
formerly:
- THEORY-tmpv0dw8
promote_when: >-
  A replication with a stated statistic: for paired networks differing
  only in the activation, a measure of concentration along the measured
  basis (with a null from random orthogonal bases, as in App. A), with
  effect sizes across seeds, in a second laboratory or at larger scale.
  Refuted if radial activations in an otherwise rotation-equivariant
  network give the same basis-aligned concentration, or if elementwise
  ones give none once the method's own artefacts are controlled. What
  cannot settle it: more density plots of the same kind, or the
  reconstruction-error comparisons, which bear on whether the effect
  matters, not on whether it occurs.
title: "In small CIFAR and MNIST autoencoders whose only basis-privileging primitive is the activation function, elementwise tanh and Leaky-ReLU concentrate latent representations into narrow beams arranged by the activation's discrete symmetry group, even in layers no activation precedes, while their orthogonally equivariant radial counterparts leave them spread, so axis-aligned discreteness there comes from the primitive, not the task"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-288.yaml, batch 013, ADR-047),
    the symmetry argument behind the ablation, the record's own, is filed
    apart as CLAIM-382, demonstrated and Active, with its proof and
    the optimiser condition it needs. This THEORY cites it and keeps its
    empirical title, whose promote_when is unchanged. The status stays
    Proposed.
tags:
- representation-learning
- mathematics
date: '2026-10-14'
source:
- LIT-976
summary: >-
  Bird (2025, v4 2026), [LIT-976](../literature.d/LIT-976.md), read in [NOTE-759](../notes.d/NOTE-759.md). Autoencoders of
  width 12–32 and up to three hidden blocks on CIFAR and MNIST, with
  rotation-equivariant affine maps, initialisation and optimiser.
  Elementwise tanh (B_n) and Leaky-ReLU (S_n) give beams along or against
  the basis, or on the ±1 diagonal, and radial tanh and Leaky-ReLU (O(n))
  do not. The evidence is density plots, five seeds a condition, with no
  statistic. The downstream claims, that this causes grandmother neurons,
  superposition and neural collapse, are untested.
answers:
- QUESTION-058
---
<!-- inactive-ok-file: THEORY-017 THEORY-022 — Proposed; accounts this one bears on -->

# THEORY-288: In small CIFAR and MNIST autoencoders whose only basis-privileging primitive is the activation function, elementwise tanh and Leaky-ReLU concentrate latent representations into narrow beams arranged by the activation's discrete symmetry group, even in layers no activation precedes, while their orthogonally equivariant radial counterparts leave them spread, so axis-aligned discreteness there comes from the primitive, not the task

## Source

George Bird (2025; v4 of 2026-01-26), [LIT-976](../literature.d/LIT-976.md), read in [NOTE-759](../notes.d/NOTE-759.md):
§§1–5 and Appendices A–E.

## What was actually shown

**The ablation.** These are autoencoders with:
- an affine encoder from the image to width n ∈ {12, 18, 24, 32};
- L ≤ 3 hidden blocks, each an activation then an affine n → n map;
- an activation and an affine decoder.

Weights are Xavier-normal, biases zero, training is momentum SGD on MSE.
All of these commute with rotations of the hidden spaces. Only the
activation varies:
- elementwise tanh, Σᵢ tanh(x·êᵢ)êᵢ, equivariant to the signed
  permutations B_n, against isotropic tanh, tanh(‖x‖)x̂, equivariant to
  O(n);
- elementwise Leaky-ReLU, equivariant to S_n, against a radial
  Leaky-ReLU;
- two B_n Leaky-ReLUs.

**The observation.** Latent representations were projected onto all
planes spanned by pairs of standard basis vectors and kept within an
angular threshold. The plots show:
- Elementwise tanh: narrow beams along and against the axes, growing
  through training (Figs. 1–2, 8–17). The count above threshold rises
  from about 2,000 to about 200,000.
- Elementwise Leaky-ReLU: two antipodal beams on one diagonal at layer 0
  (Figs. 3, 18–21). The ±1 orthant is the only one S_n treats specially.
- B_n Leaky-ReLU: beams along the axes, like tanh and unlike S_n
  Leaky-ReLU (Figs. 22–27).
- Radial versions: spread, continuous distributions. Deeper isotropic
  networks form some clusters, not aligned with the basis.
- Layer 0, which no activation precedes, shows the effect. So it reaches
  backward through training, not only through the forward map's
  geometry.
- MNIST shows the same contrast (Figs. 28–30).

What could have come out the other way: elementwise networks could have
given spread representations, with the basis showing only in parameters.
Or radial networks could have formed the same beams through the data's
own pixel axes, which the encoder mixes at random.

**A symmetry argument behind it.** This is the record's, from the setup,
and since 2026-10-19 it is [CLAIM-382](../claims.d/CLAIM-382.md), demonstrated and Active, with its
proof. With a radial activation, every part of the network and its training
is equivariant to rotations of each hidden space, and the initialisation is
invariant in distribution. So the law of the learned representation is
rotation-invariant, and no beam can prefer the standard axes. The argument
needs an orthogonally equivariant optimiser. Bird's momentum SGD is one,
and Adam would not be. The
non-trivial findings are three:
- elementwise activations produce strong concentration, not a mild
  basis-dependence;
- the concentration is on the directions the activation's group singles
  out;
- the radial networks stay spread, not clustered in random directions.

## What this does not say

- **Not a measured effect size.** There is no statistic, and the method
  has artefacts along the measured basis (App. A). The contrast is large
  in the plots, but it is visual.
- **Not "symmetry alone".** Every O(n)-equivariant map is radial, so each
  pair also contrasts coordinate-wise against radial nonlinearity. The
  B_n against S_n Leaky-ReLU comparison is the evidence for the group
  over the form, and it is qualitative.
- **Not large models.** Widths up to 32 and depths up to 3, reconstruction
  only. Classifiers, convolutions, residual streams and attention are
  discussed, not run.
- **Not the downstream phenomena.** That this is the origin of grandmother
  neurons, discrete superposition or neural collapse is the author's
  conjecture.
- **Not that isotropic networks are better.** The reconstruction results
  (App. D) are preliminary, and mixed without input standardisation.

## Connections

- **[QUESTION-058](../questions.d/QUESTION-058.md).** Isolates the activation as a source of group structure
  in a representation: B_n or S_n, from the network, with no counterpart
  in the task. A discrete arrangement read off a trained network can
  belong to its primitive.
- **[THEORY-184](THEORY-184.md).** The permutation-equivariant update preserves the symmetry
  it starts with. This adds that the primitive imprints its group on how
  examples are distributed.
- **[THEORY-017](THEORY-017.md).** A basis is supplied from outside the space. Here the
  activation supplies it, and removing that removes the axes.
- **[THEORY-022](THEORY-022.md).** There the group of the characters came from the task.
  Here a group comes from the network. "Not the network" does not
  generalise beyond that case.
- **[THEORY-021](THEORY-021.md).** The packed geometries of superposition are found in toy
  models with ReLU, an S_n primitive. Bird conjectures that such
  geometries depend on the activation's group. That is untested, and
  [THEORY-021](THEORY-021.md) does not depend on it.
