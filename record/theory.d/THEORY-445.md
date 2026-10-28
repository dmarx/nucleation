---
number: 445
status: Active
formerly:
- THEORY-tmp5lcx6
title: "A network built from group correlations over a discrete split group of plane symmetries, pointwise nonlinearities and coset pooling is equivariant to that group by construction, through the regular representation alone: the group is fixed before training and built into the weight sharing, not found in the data"
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-16'
source:
- LIT-314
summary: >-
  Cohen & Welling (2016), [LIT-314](../literature.d/LIT-314.md), read in [NOTE-288](../notes.d/NOTE-288.md). G-correlation
  commutes with the left action of G by the change of variables h → uh
  (eq. 12), and so do pointwise nonlinearities and pooling over cosets, up
  to edge effects and for rotations that are symmetries of the grid.
  Matched-parameter p4 and p4m layers lowered rotated-MNIST error from
  5.03% to 2.28% and plain-CIFAR10 error from 9.45% to 6.46%. The paper
  uses no irreducible representations, characters or Fourier analysis,
  learns nothing about which symmetry the data have, and does not separate
  the effect of equivariance from the changed channel structure.
bears_on:
- QUESTION-058
---
<!-- inactive-ok-file: THEORY-019 — Proposed; accounts of symmetry in spectra and in updates, named in Connections, not leaned on -->

# THEORY-445: A network built from group correlations over a discrete split group of plane symmetries, pointwise nonlinearities and coset pooling is equivariant to that group by construction, through the regular representation alone: the group is fixed before training and built into the weight sharing, not found in the data

## Source

Cohen & Welling (2016), [LIT-314](../literature.d/LIT-314.md) (ICML 2016), read in full in [NOTE-288](../notes.d/NOTE-288.md).

## What was actually shown

**The construction.** The first layer correlates the image with
g-transformed filters, (f ⋆ ψ)(g) = Σ_y Σ_k f_k(y) ψ_k(g⁻¹y), so its output
is a function on G. Later layers correlate functions on G with filters on
G (eq. 11). The group G is p4 (translations and 90° rotations) or p4m
(adding reflections), and must be split, g = ts with t a translation and s
in the stabiliser of the origin (§7).

**The proofs.** Planar correlation is not rotation-equivariant:
[L_r f] ⋆ ψ = L_r[f ⋆ L_{r⁻¹}ψ] (eq. 9). G-correlation is:
[L_u f] ⋆ ψ = L_u[f ⋆ ψ] (eq. 12). Pointwise nonlinearities commute with
L_h (eq. 15), max-pooling over gU commutes with L_h (eqs. 17, 20), and
pooling over cosets gH gives an H-invariant map, a function on G/H (§6.3).
Exact equivariance needs one bias and one batch-norm scale per G-feature
map (§6.1). The backward pass is again a G-correlation (App. C).

**The experiments.** At roughly matched parameter counts, rotated-MNIST
test error falls from 5.03% (planar) to 2.28% (P4CNN), against a previous
best of 3.98%. Pooling over rotations in intermediate layers gives 3.21%,
worse than keeping the rotation axis to the last layer (Table 1, seed
standard deviations reported). On un-augmented CIFAR10, ResNet44 error
falls from 9.45% to 6.46% with p4m; on augmented CIFAR10+ from 5.61% to
4.94% (Table 2, single runs).

**What could have come out otherwise.** The proofs could not. The
experiments could have shown no gain from the group. They showed one,
including on CIFAR, whose objects are upright and so not symmetric under
the group (§9).

## What this does not say

- **That the network learns its symmetry.** G is chosen before training
  and stipulated, with its action on the grid and the transformation law
  of the feature maps. Nothing is learned about which symmetry the data
  have.
- **That it uses representation theory.** Feature maps are functions on
  G and G acts by permuting and transforming them: the regular
  representation. The words "irreducible", "character" and "Fourier" do
  not occur in the body ([NOTE-288](../notes.d/NOTE-288.md), Corrections).
- **That equivariance is what helps.** Matching parameters changes width
  and channel structure, and no ablation separates the two. "Increases the
  expressive capacity" is asserted, not measured.
- **That equivariance holds exactly for rotations in general.** It holds
  for rotations that are symmetries of the sampling grid (90°), and up to
  edge effects.
- **That the converse holds.** Only sufficiency is proved: these layers
  are equivariant. That equivariance forces generalised convolution is
  Kondor & Trivedi's result for compact groups ([LIT-305](../literature.d/LIT-305.md)).
- **State of the art on CIFAR10.** It holds for plain CIFAR10 only; on
  CIFAR10+ the best result is "comparable" to the prior 4.17%.

## Connections

- **[QUESTION-058](../questions.d/QUESTION-058.md)** asks how much of a group's structure in a trained
  network comes from the task, the architecture, the training set and the
  update. Here all of it comes from the architecture, by construction,
  and the analyst supplies the group. This is the limiting case the
  question contrasts with recovery from the weights.
- **[THEORY-019](THEORY-019.md).** Symmetry forces spectral degeneracy, and degeneracy does
  not identify a symmetry. A G-CNN's equivariance is imposed, so it says
  nothing about detecting a group from a spectrum.
- **[THEORY-184](THEORY-184.md).** A permutation-equivariant update preserves the symmetry
  it starts with. A G-CNN's weight sharing is a symmetry built in, which
  the backward pass, again a G-correlation, preserves.
- **Lenc & Vedaldi ([LIT-363](../literature.d/LIT-363.md), [NOTE-309](../notes.d/NOTE-309.md))** measured equivariance a trained CNN
  acquired without being built for it. This paper's relay of that work
  overstates it ([NOTE-288](../notes.d/NOTE-288.md), correction of 2026-09-29).
