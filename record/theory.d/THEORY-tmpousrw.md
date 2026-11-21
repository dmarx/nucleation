---
status: Proposed
title: 'Lau and colleagues define the local learning coefficient of a local minimum as the volume-scaling exponent of its low-loss set and estimate it as nβ*(E[Lₙ] − Lₙ(w*)) under a posterior tempered at β* = 1/log n and tied to w* by a Gaussian of precision γ, sampled by SGLD; that the estimate converges to the coefficient is conjectured, with the conditions on γ left open, and it is calibrated only in noiseless deep linear networks of 10² to 10⁸ parameters, where it tracks the exact values with relative errors mostly between 0 and 0.8, underestimates; elsewhere the authors claim only relative comparisons at fixed sampler settings'
promote_when: >-
  The relative errors read off Fig. J.2 confirmed against the authors'
  released data or a reproduction of the deep-linear-network calibration
  at one scale or more, with γ and β* as stated; and the App. D conjecture
  confirmed as still unproved in the paper's latest version (a proof would
  change the title).
version: 1
tags:
- learning-theory
- loss-landscapes
- mathematical-statistics
date: '2026-11-21'
source:
- LIT-tmpnbl2d
bears_on:
- QUESTION-tmp7d1ws
summary: >-
  Lau, Furman, Wang, Murfet and Wei, [LIT-tmpnbl2d](../literature.d/LIT-tmpnbl2d.md), read in [NOTE-tmp92pjh](../notes.d/NOTE-tmp92pjh.md).
  The estimator behind the record's learning-coefficient entries
  ([THEORY-1275](THEORY-1275.md), [THEORY-975](THEORY-975.md)). The estimate is a free-energy slope at
  effective sample size n/log n, cut off also by the localizer's γ; the
  paper fixes β*, sets γ per experiment, and calibrates only in noiseless
  deep linear networks.
---

# THEORY-tmpousrw: Lau and colleagues define the local learning coefficient of a local minimum as the volume-scaling exponent of its low-loss set and estimate it as nβ*(E[Lₙ] − Lₙ(w*)) under a posterior tempered at β* = 1/log n and tied to w* by a Gaussian of precision γ, sampled by SGLD; that the estimate converges to the coefficient is conjectured, with the conditions on γ left open, and it is calibrated only in noiseless deep linear networks of 10² to 10⁸ parameters, where it tracks the exact values with relative errors mostly between 0 and 0.8, underestimates; elsewhere the authors claim only relative comparisons at fixed sampler settings

## Source

Lau, Furman, Wang, Murfet and Wei, "The Local Learning Coefficient: A
Singularity-Aware Complexity Measure", [LIT-tmpnbl2d](../literature.d/LIT-tmpnbl2d.md), read from arXiv
2308.12108v2 in [NOTE-tmp92pjh](../notes.d/NOTE-tmp92pjh.md).

## What was actually shown

- **Definition** (Def. 1): the ε-sublevel volume near w* scales as
  cε^λ(−log ε)^(m−1); λ(w*) is the local learning coefficient.
- **Estimator** (Def. 2): λ̂(w*) = nβ*[E Lₙ(w) − Lₙ(w*)] under a posterior
  tempered at β* = 1/log n and localized by a Gaussian of precision γ;
  "λ̂(w∗) depends on γ but we have suppressed this in the notation."
- **Consistency** (App. D): conjectured, "given certain conditions on γ".
- **Calibration** (§5.1, App. J): against exact coefficients in realizable,
  noiseless deep linear networks of 10² to 10⁸ parameters, γ = 1, the
  relative error (λ − λ̂)/λ lies mostly between 0 and +0.8 (Fig. J.2, read
  from the rendered page): the estimate mostly underestimates.
- **Elsewhere** (§5.2, Apps. K–O): relative comparisons only, at fixed
  sampler settings.

What could have failed: the estimates could have missed the exact values
by orders of magnitude, or failed to rise with them across scales; they
did not.

## What this does not say

- **That the estimator is consistent.** A conjecture.
- **What it measures at other temperatures or localizations.** One β* per
  experiment; γ = 1 or 100 without a study of dependence. On a quadratic
  loss the estimate is Σ ½ te_i/(te_i + γ) with t = n/log n ([NOTE-tmp92pjh](../notes.d/NOTE-tmp92pjh.md)),
  so a direction with curvature below about γ log n/n counts as flat.
- **That an underestimate is a smaller coefficient.** The authors
  attribute underestimation to a sampler that has not settled (App. H).
- **That calibration transfers.** Outside deep linear networks the values
  are uncalibrated; [LIT-1894](../literature.d/LIT-1894.md)'s Table K.1 ([NOTE-1462](../notes.d/NOTE-1462.md)) shows errors of about
  15% and a wrong order between phases of equal coefficient in a model
  with known values.
