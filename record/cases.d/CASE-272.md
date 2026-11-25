---
number: 272
status: Proposed
formerly:
- CASE-tmp71zhd
title: 'Modular-addition transformers over checkpoints'
statement: >-
  A proposed study: small transformers trained on modular addition, saved at
  many checkpoints, with the training kernel's eigenspaces and each layer's
  coupling among Fourier modes measured over training, to see whether
  changes in modal coupling forecast the Fourier circuit's formation better
  than training loss, Fourier energy and the known progress measures
version: 1
standing: stipulated
kind: proposed-study
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-15'
line:
- learned-structure
bears_on:
- QUESTION-275
- QUESTION-217
draws_on:
- THEORY-022
summary: >-
  A's "Experiment I", from A14 of the continuation of the exchange
  "Explain String Theory" (2026-11-15), as the first test of the owner's
  hypothesis that wave mathematics applies to learning ([CLAIM-698](../claims.d/CLAIM-698.md)).
  It uses the task where the record already holds a Fourier mechanism
  ([THEORY-022](../theory.d/THEORY-022.md), from [LIT-345](../literature.d/LIT-345.md)), so the modes are justified by the task's
  group, not chosen to fit. Not run. Proposed because the design is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-022 CLAIM-698 — Proposed or new; the held mechanism and the claim the study tests -->

# CASE-272: Modular-addition transformers over checkpoints

## The design

At each checkpoint τ and layer ℓ, measure
M_{ℓ,τ}(x) = U_{ℓ+1}ᵀ DΦ_{ℓ,τ}(h_ℓ(x)) U_ℓ in the Fourier basis of ℤ/p,
together with the empirical tangent kernel's eigenspaces and the moving-
basis term Ω_τ = U_τᵀU̇_τ ([QUESTION-217](../questions.d/QUESTION-217.md)'s note of 2026-11-15). The
selection rule χ_k χ_m = χ_{k+m} says which couplings the algorithm needs.
The question is whether they rise before the network generalizes.

## The comparison that decides it

Modal-coupling measures, taken at early checkpoints, are scored against
the progress measures of [LIT-345](../literature.d/LIT-345.md), against Fourier energy alone and against
training loss as forecasts of when the circuit forms and of held-out
Fourier ablations. If the established measures forecast as well, the
coupling description adds nothing here.

## Its limits

The Fourier basis is given by the task. A positive result would not show
that modes can be found where no symmetry supplies them. That is the next
step, and the harder one.
