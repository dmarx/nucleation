---
number: 283
status: Active
formerly:
- THEORY-tmpsluko
title: 'For a hierarchical multi-index target with isotropic Gaussian inputs and even, separable links, direction k becomes weakly recoverable by the Bayes-optimal estimator at a sample count proportional to its squared weight to the power minus one, so features emerge one at a time through sharp spectral transitions in the number of samples; a target-agnostic spectral estimator attains the thresholds and the optimal weighted error, and a two-layer network whose first layer is that estimator, with a ridge readout, attains them in excess risk'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision for THEORY-283 (batch 024,
    ADR-047). The title began "for a two-layer network", which read as a
    trained network. The thresholds are proved for the Bayes-optimal and
    spectral estimators, and the network result for Algorithm 1 (spectral
    first layer, data split, ridge readout); the title now says so and
    names the target's conditions. The theorems were proved in a work the
    record has read in full (NOTE-805), so promotion rests on that reading.
    The promote_when asked for a gradient-descent proof or a second input
    law, both outside the narrowed title. It moves unchanged to
    QUESTION-158.
tags:
- learning-theory
- representation-learning
date: '2026-10-14'
source:
- LIT-940
summary: >-
  Defilippis, Krzakala, Loureiro and Maillard (2026), [LIT-940](../literature.d/LIT-940.md), read in
  [NOTE-805](../notes.d/NOTE-805.md). Take x ~ N(0, I/d), n = αd, and f⋆ = Σ a_k g_k(⟨w_k, x⟩)
  with even links of generative exponent two and a_k ~ k^(−γ). Direction
  k is weakly recoverable at α_k = Θ(a_k^(−2)) (Thm. 3.2). The optimal
  weighted error is Θ(α^(−1+1/(2γ))) until α ≍ m⋆^(2γ). The spectral
  estimator on Σ T(y_i)x_ix_iᵀ attains both (Thm. 3.6). The cascade is in
  the number of samples, not in training time. The network result is for
  a spectral first layer plus a ridge readout, not gradient descent.
answers:
- QUESTION-039
---
<!-- inactive-ok-file: THEORY-229 THEORY-187 THEORY-204 THEORY-201 THEORY-180 — Proposed; accounts this one is set beside, none of them rested on -->

# THEORY-283: For a hierarchical multi-index target with isotropic Gaussian inputs and even, separable links, direction k becomes weakly recoverable by the Bayes-optimal estimator at a sample count proportional to its squared weight to the power minus one, so features emerge one at a time through sharp spectral transitions in the number of samples; a target-agnostic spectral estimator attains the thresholds and the optimal weighted error, and a two-layer network whose first layer is that estimator, with a ridge readout, attains them in excess risk

## Source

Defilippis, Krzakala, Loureiro and Maillard (2026), [LIT-940](../literature.d/LIT-940.md), read in
[NOTE-805](../notes.d/NOTE-805.md). The account rests on Theorems 3.2, 3.6 and 3.8, Remark 3.5,
and Appendices A–C.

## What was actually shown

**The setting.**
- Inputs x ~ N(0, I_d/d), with labels y = Σ_(k≤m⋆) a_k g_k(⟨w_k, x⟩) + √Δ ξ.
- The w_k are orthogonal, and a_k = Θ(k^(−γ)).
- Each g_k is even, with E[g_k²] and |E[g_k″]| bounded away from zero
  and infinity uniformly in k, so each direction is detectable at
  n = Θ(d).
- The limit is n, d → ∞ at α = n/d fixed, then α, m⋆ ≫ 1.

**Thresholds (Thm. 3.2, Eq. 13).** The Bayes estimator first correlates
with w_k at α_k = Θ(k^(2γ) m⋆^((1−2γ)₊)), which is Θ(a_k^(−2)) in both
regimes of γ.
- **Lower bound.** An oracle that is told the other directions faces a
  single-index problem with SNR a_k². Its weak-recovery threshold is
  Θ(1/SNR) (Corollary C.4, from Barbier et al.'s free entropy expanded at
  small SNR).
- **Upper bound.** The spectral estimator below.

**Rates (Thm. 3.2, Eq. 12).**
- For γ > 1/2, MMSE_γ = Θ(α^(−1+1/(2γ))) while α ≪ m⋆^(2γ), and Θ(m⋆/α)
  after.
- For γ < 1/2, it is Θ(1) while α ≪ m⋆, and Θ(m⋆/α) after.
- The error splits into k_α·Θ(1/α), from the k_α ≍ α^(1/(2γ)) directions
  already out, plus Σ_(k>k_α) a_k², from the rest.

**Spectral estimator (Thm. 3.6).** Take the top eigenvectors of
T = Σ_i T(y_i)x_ix_iᵀ, for any bounded preprocessing T, cut at an eigengap
of C/√d. They attain the same rates and thresholds. Because the links are
even and separable, E[zzᵀ − I | y] is diagonal, so each spike correlates
with one direction only.

**Network (Thm. 3.8).** For polynomial links, a network whose first layer
is ZŴ^sp, with Z random, and whose readout is fitted by random-feature
ridge regression on a fresh half of the data, has excess risk
Θ(MMSE_γ) + O(n^(−1/2)).

**What could have come out otherwise.**
- The thresholds could have depended on the other directions, as they do
  for general multi-index models. The oracle bound shows they do not
  here.
- A target-agnostic method could have lost a factor against the Bayes
  rate. It does not.
- The simulations at d = 1000 (Figs. 1–3) show the predicted crossover
  near α ≈ m⋆^(2γ) ≈ 400, and spikes leaving the bulk in sequence.

## What this does not say

- **Not a training-time result.** The "cascade of phase transitions" is
  in the number of samples. No trajectory of training is analysed. The
  bridge to gradient descent is Remark 3.5: with a slightly modified
  loss, early first-layer gradient descent from a small sphere is a
  power iteration on T. That is cited from Bonnaire et al. (2025) and
  Zhang et al. (2025), not proved here.
- **Not that gradient descent attains the rates.** The network theorem
  is for Algorithm 1: spectral initialization, a data split, and a ridge
  readout. The authors leave open whether SGD without spectral
  initialization does (§5).
- **Not the Bayes risk.** The excess-risk rate equals the subspace rate.
  It is not shown to be the optimal risk (Remark 3.9).
- **Not beyond separable, even, Gaussian structure.** The one-by-one
  reading depends on the diagonal G(y). With interacting directions the
  paper says the picture "can be arbitrary complicated".
- **Not that it explains the heavy-tailed weight spectra of trained
  networks.** §5 says the spectra "resemble" those, and that is all.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md).** It answers in part. In this model class the order of
  acquisition is the order of the target's weights a_k, and the moment
  is a sample count n_k = Θ(a_k^(−2) d). Every acquisition is one kind of
  event: a spike leaving a random-matrix bulk, sharp in the limit.
- **[THEORY-229](THEORY-229.md).** Both accounts acquire top eigenvectors of a data matrix
  in order of strength. They differ in what they fix:
  - [THEORY-229](THEORY-229.md) fixes the data and gives a training time,
    τ_j ≈ −log(s_j(0)²γ_j)/(8γ_j).
  - This account gives the sample size at which a direction is
    recoverable at all.
  - Remark 3.5's power-iteration reading makes small-initialization
    gradient descent the common mechanism, but no paper held here joins
    the two clocks.
- **[THEORY-204](THEORY-204.md) and [THEORY-201](THEORY-201.md).** Their horizon has the same form: a
  signal of strength s is detectable once n·s² is of order one, so a
  power-law signal gives a power-law threshold with doubled exponent.
  There it is assumed for real text. Here it is proved for Gaussian
  inputs. That is an analogy of form only.
- **[THEORY-180](THEORY-180.md).** The attention-layer result from the same group has a
  matching picture: outliers are recovered directions, and the bulk is
  noise.
- **[THEORY-187](THEORY-187.md).** Its depth-dependent plateau is a training-time
  quantity, so it does not compete with this sample-size threshold.
