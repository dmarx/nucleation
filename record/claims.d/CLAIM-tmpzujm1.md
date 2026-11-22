---
status: Proposed
title: 'On data whose inputs and targets are each written in a tree''s levels with a strength per level, every kernel of inner products and norms commutes exactly with the level projectors, so kernel gradient flow acquires the levels in the order of input strength alone, while a decoupled deep linear network acquires them in the order of input strength times target strength; the two learners'' phase boundaries therefore differ, and neither is fixed by tree depth'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-052: the
    sufficient conditions QUESTION-217 asks for, for two model classes,
    with the study that checks them.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation in scratch/studies/lead-052/README.md: a
  kernel that is a function of inner product and norms whose Gram matrix
  on such tree-symmetric items fails to commute with a level projector, or
  a kernel flow from zero output whose level risk is not exp(−2μ_ℓt/N); or
  a decoupled, balanced deep linear network on such data whose acquisition
  times do not approach the ratio of the levels' products c_ℓ g_ℓ as the
  initial scale goes to zero. Not defeated by learners outside these two
  classes, or by data without the tree symmetry, which lie outside the
  claim.
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-217
- QUESTION-039
grounds:
- CASE-tmp7n58t
- THEORY-186
- THEORY-086
summary: >-
  A partial answer to [QUESTION-217](../questions.d/QUESTION-217.md)'s request for sufficient conditions,
  for two learners. Write inputs X = √N H diag(c) R and targets
  Y = √N H diag(g) R′ in the Haar basis H of a binary tree, with level
  strengths c and g. Items then have equal norms and inner products that
  depend only on the depth of their common ancestor, so any kernel of
  inner products and norms is a sum of block matrices that act as a scalar
  μ_ℓ on each level: [K, P_ℓ] = 0 exactly, A2's Conjecture A condition
  holding by symmetry. Kernel flow from zero output then gives each level's
  risk as exp(−2μ_ℓt/N), and μ_ℓ depends on c alone: target strengths
  never enter the order. For a decoupled, balanced deep linear network the
  same data give T_ℓ/T_m → c_m g_m / c_ℓ g_ℓ as the initial scale goes to
  zero (the [THEORY-186](../theory.d/THEORY-186.md) solution with diagonal input covariance). So the
  same data can be coarse-first for one learner and simultaneous or
  fine-first for the other, and in neither does the tree's depth set the
  order. Checked in [CASE-tmp7n58t](../cases.d/CASE-tmp7n58t.md): the exact kernels and a width-2048
  network were simultaneous in 79 to 81 of 81 cells with flat inputs,
  and the two-layer linear network matched the product order in all 81.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmp7n58t CLAIM-tmp0h57p — new; the study and the empirical claim of LEAD-052, filed 2026-11-22 -->
<!-- inactive-ok-file: THEORY-186 — Proposed; the deep linear solution this claim applies under its own assumptions -->

# CLAIM-tmpzujm1: On data whose inputs and targets are each written in a tree's levels with a strength per level, every kernel of inner products and norms commutes exactly with the level projectors, so kernel gradient flow acquires the levels in the order of input strength alone, while a decoupled deep linear network acquires them in the order of input strength times target strength; the two learners' phase boundaries therefore differ, and neither is fixed by tree depth

## The claim

Let N = 2^L items be the leaves of a binary tree, H the Haar basis of R^N
with its columns grouped by level (level ℓ holds the distinctions the tree
draws at depth ℓ), and P_ℓ the projector onto level ℓ. Take inputs
X = √N H diag(c) R_in and targets Y = √N H diag(g) R_out, with any
per-level strengths and any rotations.

1. **Commutation.** Every item has the same norm, and the inner product of
   two items depends only on the depth of their lowest common ancestor. So
   a kernel that is a function of the inner product and the two norms has
   a Gram matrix K = Σ_d a_d B_d, with B_d the block matrix of ones on the
   depth-d subtrees. B_d multiplies a level-ℓ Haar vector by N/2^d when
   ℓ ≤ d (the vector is constant on depth-d blocks) and annihilates it when
   ℓ > d (it sums to zero on them). Hence [K, P_ℓ] = 0 for every ℓ.
2. **Kernel flow.** Under dF/dt = −(1/N)K(F − Y) from F = 0, level ℓ's
   relative risk is exp(−2μ_ℓt/N), so T_ℓ(δ) = N ln(1/δ)/(2μ_ℓ). Acquisition
   is coarse-first exactly when μ_ℓ falls with ℓ, which depends on c and
   the kernel, never on g. For the linear kernel μ_ℓ ∝ c_ℓ².
3. **Deep linear flow.** For a two-layer linear network started decoupled
   and balanced at a common small strength ε, level ℓ's strength a obeys
   ȧ = 2a(c_ℓg_ℓ − c_ℓ²a). Its acquisition time is
   (1/2s_ℓ)[ln(b₁/(1 − b₁)) − ln(b₀/(1 − b₀))], with s_ℓ = c_ℓg_ℓ,
   b₁ = 1 − √δ and b₀ = c_ℓ²ε/s_ℓ, so T_ℓ/T_m → s_m/s_ℓ as ε → 0.

So the two learners divide the same space of strengths differently: the
kernel's coarse-first region is where the input strengths fall with depth,
the deep linear network's where the products do. Tree depth enters neither
order except through the strengths placed on it.

## What it rests on

The derivation is in scratch/studies/lead-052/README.md, and its pieces
are tested there (commutator below 10⁻¹⁰; exponential level risks to
machine precision). Step 3 is [THEORY-186](../theory.d/THEORY-186.md)'s solution, extended to a
diagonal input covariance; [THEORY-086](../theory.d/THEORY-086.md) is the kernel-regime account whose
"eigenspace by eigenspace" step 2 instantiates. The study
([CASE-tmp7n58t](../cases.d/CASE-tmp7n58t.md)) checks both against trained networks.

## What it does not say

- Nothing about data without the tree symmetry, where [K, P_ℓ] need not
  vanish and levels can mix.
- Nothing about a deep linear network from random rather than decoupled
  starts beyond what the study observed (agreement in all 81 cells of its
  first grid), nor about depth three or more, where the study found target
  strength weighed more than input strength.
- Nothing about finite-width or feature-learning networks; that is
  [CLAIM-tmp0h57p](CLAIM-tmp0h57p.md)'s empirical question.
- It concerns acquisition measured by the network's own output, not by a
  probe on its hidden units.
