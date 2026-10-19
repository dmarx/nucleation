---
number: 185
status: Open
formerly:
- QUESTION-tmpbc3nl
title: "When does the information bottleneck's first global transition between a lattice block and its far environment coincide with the point where the uninformative encoder loses stability, and is the first feature the leading excited transfer-matrix mode beyond the Ising check?"
version: 1
tags:
- information-theory
- natural-sciences
date: '2026-10-19'
line: 'formal-apparatus'
summary: >-
  The promotion condition formerly on [THEORY-205](../theory.d/THEORY-205.md), widened. [THEORY-205](../theory.d/THEORY-205.md) was
  narrowed to the point where the uninformative IB encoder loses
  stability, β = (λ0/λ1)^(2L_B), and promoted on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v2).
  The global threshold, where the uninformative encoder stops being
  optimal, is 1/s*. It can come earlier, as it does on a skewed 3-state
  chain. In the circumference-3 Ising check the two agree.
---

# QUESTION-185: When does the information bottleneck's first global transition between a lattice block and its far environment coincide with the point where the uninformative encoder loses stability, and is the first feature the leading excited transfer-matrix mode beyond the Ising check?

## Why it is a question

[THEORY-205](../theory.d/THEORY-205.md) holds, exactly, that in the slab geometry on a cylinder the
uninformative information-bottleneck encoder loses local stability at
β = (λ0/λ1)^(2L_B), and that the unstable direction is the boundary weak
value of the leading excited transfer-matrix eigenvector. That point is
β = 1/ρ_m², with ρ_m the maximal correlation between block and
environment. The uninformative encoder stops being globally optimal
earlier, at β = 1/s*. Here s* = sup I(U;E)/I(U;V) over encoders U, and
s* ≥ ρ_m².

In the circumference-3 critical Ising check the two thresholds agree to
six figures. In a nearest-neighbour chain of 3-state units, they differ
27-fold at a buffer of two transfer steps. There an encoder that flags a
rare state beats the uninformative one well below the bifurcation.

So the IB's first transition in a lattice model is the bifurcation only
under some further condition, perhaps a symmetry. Whether the first
feature the global optimum keeps is still the leading excited mode is
open. Until 2026-10-19 the second-model half of this was [THEORY-205](../theory.d/THEORY-205.md)'s
promote_when.

## What would answer it

- A proof that s*(V;E) = ρ_m²(V;E) for a stated class of transfer
  matrices, such as those whose leading excited mode is odd under an
  involutive symmetry. Or a characterisation of when it fails.
- An exact transfer-matrix computation on a model other than Ising, such
  as a Potts or non-integrable chain on a cylinder wide enough to
  separate ∆₁ from ∆₂, that finds the global IB optimum just past 1/s*
  and says which feature it keeps.

Against [THEORY-205](../theory.d/THEORY-205.md)'s feature claim: a short-range model with a symmetric
transfer matrix whose unstable direction at the bifurcation, in the slab
geometry, is not that eigenvector.

What would not answer it: results for planar blocks inside a buffer shell,
or for RSMI at a fixed alphabet. They bear on the wider claim
[THEORY-205](../theory.d/THEORY-205.md) does not make.
