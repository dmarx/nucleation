---
status: Proposed
promote_when: >-
  An independent re-derivation of the n-level updates from the paper's
  stated generative model (each level a Gaussian random walk with
  variance exp(κi x(i+1) + ωi) of the level above, the top one with
  constant variance ϑ) and approximations (Gaussian mean-field posteriors,
  each variational energy expanded to second order) reproduces Eqs 9–16:
  one update form at every level above the first, each mean update a
  prediction error weighted by the ratio of the precision of the
  prediction of the level below to the posterior precision, a value
  prediction error at the first level and a volatility prediction error
  above it. It is not met by fits to behaviour, by parameter-recovery
  results, or by agreement with exact inversion, none of which the title
  asserts.
title: 'Mathys and colleagues show that a hierarchy of any number of Gaussian random walks, each level setting the log-variance of the one below, inverts under a mean-field variational approximation to one-step updates of the same form at every level above the first; each mean update is a prediction error weighted by the ratio of the precision of the prediction below to the posterior precision, a value prediction error at the first level and a volatility prediction error above it'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-tmpnn27v, the reading of LIT-tmpkft30,
    registered from the owner's pasted synthesis of 2026-11-04. The
    wording is the reader's; adopting it is the owner's call. Not
    re-derived for this filing. The paper's parameter-recovery result is
    a separable claim, noted in NOTE-tmpnn27v and not filed here.
tags:
- probabilistic-modeling
- learning-and-conditioning
date: '2026-11-04'
source:
- LIT-tmpkft30
summary: >-
  Mathys et al. (2014), [LIT-tmpkft30](../literature.d/LIT-tmpkft30.md), read in [NOTE-tmpnn27v](../notes.d/NOTE-tmpnn27v.md). The
  Hierarchical Gaussian Filter's update equations for n levels: the same
  precision-weighted prediction-error form at every level above the
  first, a value prediction error at level 1 and a volatility prediction
  error above. Proposed until the updates are re-derived. It says nothing
  about how close the approximation is to exact inversion, whether the
  parameters can be recovered, or whether people learn this way. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpjlua4 — Proposed or new; cited from the reading of Mathys et al. (2014) as open -->

# THEORY-tmph6x8h: Mathys and colleagues show that a hierarchy of any number of Gaussian random walks, each level setting the log-variance of the one below, inverts under a mean-field variational approximation to one-step updates of the same form at every level above the first; each mean update is a prediction error weighted by the ratio of the precision of the prediction below to the posterior precision, a value prediction error at the first level and a volatility prediction error above it

## Source

Mathys, Lomakina, Daunizeau, Iglesias, Brodersen, Friston and Stephan
(2014), [LIT-tmpkft30](../literature.d/LIT-tmpkft30.md); read in [NOTE-tmpnn27v](../notes.d/NOTE-tmpnn27v.md). It generalizes the
three-level derivation of [THEORY-tmpjlua4](THEORY-tmpjlua4.md).

## What was actually shown

- **n levels** (Introduction): "here, we extend the HGF explicitly to any
  number of levels", with the coupling exp(κi x(i+1) + ωi) motivated as a
  first-order expansion of the log of any positive coupling (Appendix A),
  and variances scaled by the time between inputs.
- **The update form** (Eqs 9–16): "value prediction errors (VAPEs) at the
  first level, volatility (i.e., variance) prediction errors (VOPEs) at
  all higher levels"; "the updates of the means are precision-weighted
  prediction errors" (Discussion). The weight is the precision of the
  prediction of the level below over the posterior precision of the level
  updated.
- **Illustration**: two simulated agents differing in sensory
  uncertainty, one subject's data with two response models compared by
  free energy, and a simulation study of recovery. These show the
  machinery working; the derivation is what the title asserts.

## What this does not say

- That the approximation is accurate: it still needs nearly quadratic
  variational energies, and large ϑ can push the top-level precision below
  zero, the agent knowing "less than nothing". The paper bounds the
  priors instead.
- That the parameters are identifiable: "there is a fundamental ambiguity
  between individual differences in coupling (i.e., κ) and individual
  differences in priors for x3 (i.e., μ(0)3)" (Appendix F).
- That parameters are recovered in general: recovery was shown for κ and
  ζ only, on one model and input sequence, and degrades at high decision
  noise. That is a separate claim, not filed.
- That people learn this way: the evidence is cited (Iglesias et al.
  2013; Vossel et al. 2013), not shown.
- That the hierarchy is across participants: estimation is per subject,
  by MAP, with no group-level pooling, unlike HDDM ([LIT-563](../literature.d/LIT-563.md)).
