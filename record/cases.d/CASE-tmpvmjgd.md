---
status: Active
title: 'Interacting accumulators on an influence network: if each perspective''s continuous support for one of two interpretations follows dxᵢ = [dᵢ − λxᵢ + κ Σⱼ Wᵢⱼxⱼ]dτ + noise, with W irreducible and row-stochastic and ℓ its left eigenvector, then ℓᵀ(κW − λI) = (κ − λ)ℓᵀ, so the ℓ-weighted support L = ℓ·x is exactly an Ornstein–Uhlenbeck process with drift ℓ·d, rate κ − λ and variance ℓᵀΣℓ, and a drift-diffusion process at κ = λ; with tanh coupling and member noise the transition is at κ_c = λ/E[sech² ε], not at κ = λ'
version: 1
standing: stipulated
kind: construction
tags:
- complex-systems
- network-science
- probabilistic-modeling
date: '2026-10-25'
line: distributed-agency
variant_of:
- CASE-074
illustrates:
- CLAIM-262
summary: >-
  From the continuation of the exchange of 2026-10-24 (U28–U47). A36
  derived it as the answer to the owner's U34 hypothesis, and A37, A42,
  A43 and A44 restated it as the population simulator's unit test. The
  case formalizes [CASE-074](CASE-074.md)'s crowd as a linear network of accumulators: the
  hidden tally is the balanced case, the visible tally positive feedback.
  The closure is [THEORY-733](../theory.d/THEORY-733.md)'s, the variance [THEORY-321](../theory.d/THEORY-321.md)'s influence
  concentration and the balance [THEORY-068](../theory.d/THEORY-068.md)'s, a combination no source
  makes. Checked when filed, and the reply's nonlinear transition
  corrected.
supports:
- CLAIM-tmpfd9lk
---
<!-- inactive-ok-file: THEORY-tmphmdtd — Proposed; the reflected-appraisal reading named as where endogenous influence enters, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-262 — Proposed; the owner's claim this construction illustrates, nothing here rests on it -->

# CASE-tmpvmjgd: Interacting accumulators on an influence network: if each perspective's continuous support for one of two interpretations follows dxᵢ = [dᵢ − λxᵢ + κ Σⱼ Wᵢⱼxⱼ]dτ + noise, with W irreducible and row-stochastic and ℓ its left eigenvector, then ℓᵀ(κW − λI) = (κ − λ)ℓᵀ, so the ℓ-weighted support L = ℓ·x is exactly an Ornstein–Uhlenbeck process with drift ℓ·d, rate κ − λ and variance ℓᵀΣℓ, and a drift-diffusion process at κ = λ; with tanh coupling and member noise the transition is at κ_c = λ/E[sech² ε], not at κ = λ

## The case

M perspectives and two interpretations, H₊ and H₋. xᵢ is perspective i's
support for H₊ over H₋, "a continuous-valued opinion or decision variable;
it need not be a calibrated log likelihood" (A36):

    dxᵢ = [dᵢ − λxᵢ + κ Σⱼ Wᵢⱼ xⱼ] dτ + noiseᵢ,   Σⱼ Wᵢⱼ = 1,
    ℓᵀW = ℓᵀ,  Σᵢ ℓᵢ = 1,   L = Σᵢ ℓᵢ xᵢ.

dᵢ is the evidence drift perspective i receives, λ its leak, κ the
strength with which it takes up its neighbours' support, and W the
influence network. Σ is the covariance of the members' noise.

## What follows

1. **Exact closure.** Since ℓᵀ(κW − λI) = (κ − λ)ℓᵀ,
   dL = [ℓ·d + (κ − λ)L]dτ + ℓ·noise. The same identity holds step by step
   for an Euler scheme, so a simulated L is exactly a Gaussian AR(1)
   whatever the step size. A36: "**This reduction is exact for the
   specified linear system.**" It is [THEORY-733](../theory.d/THEORY-733.md)'s condition for exact
   dynamical independence: the coarse-graining's row space is invariant
   under the transpose of the drift. [CLAIM-388](../claims.d/CLAIM-388.md)'s uniform sum is the case
   ℓ = 1/M.
2. **Drift diffusion at balance.** At κ = λ, dL = ℓ·d dτ + σ_eff dB, the
   standard drift-diffusion model. With κ < λ, L is a leaky
   Ornstein–Uhlenbeck process. With κ > λ it is unstable, and early
   evidence is amplified. That is [THEORY-068](../theory.d/THEORY-068.md)'s net leak, carried from two
   competing units to a network. The other modes of κW − λI decay at rates
   λ − κ Re μ_k > 0 at balance, since Re μ_k < 1 for every other
   eigenvalue of an irreducible W. So the members settle around L with a
   stationary spread of order σ/√λ.
3. **Variance from influence concentration.** σ_eff² = ℓᵀΣℓ. Only for
   independent noises is this Σℓᵢ²σᵢ², and with equal σ it is σ²/M_eff,
   M_eff = 1/Σℓᵢ². A36's example, one perspective with weight ½ and 23
   sharing the rest, gives M_eff = 3.83. Since max ℓᵢ² ≤ Σℓᵢ² ≤ max ℓᵢ,
   the collective noise vanishes exactly when the largest influence weight
   does, which is [THEORY-321](../theory.d/THEORY-321.md)'s condition (Golub and Jackson) in variance
   form. A36: "a small effective population doesn't necessarily mean poor
   decisions. A highly weighted specialist might be more accurate than
   everyone else." Under correlated evidence, as in A43's typed workspace
   with its `correlation_group`, the diagonal formula understates the
   noise: by a factor of about 12 in a check with pairwise correlation ½.
4. **The hidden and the visible tally.** In [CASE-074](CASE-074.md)'s terms, voters
   who cannot see the tally integrate independently, the balanced case. A
   visible tally that draws votes to the leader adds κ above λ. At a fixed
   bound on L, raising κ − λ above 0 shortens decisions and lowers
   accuracy. That is the direction of A37's reported public-tally run
   (85.4% correct in 49.5 steps balanced, 67.1% in 18.5 with feedback;
   reported from a sandbox, parameters not given).

## The nonlinear version, corrected

A36 §6 replaced κ Σⱼ Wᵢⱼxⱼ by κ Σⱼ Wᵢⱼ tanh(xⱼ) and wrote the mean field as
dL = [d̄ − λL + κ tanh L]dτ + …, with a pitchfork at κ = λ. It called this
"a plausible mean-field equation". But Σⱼ ℓⱼ tanh(xⱼ) ≠ tanh(L) when the
members disagree. With member noise the members spread about L by ε, the
slope of the coupling at the origin is κ E[sech² ε], and the symmetric
state loses stability at κ_c = λ/E[sech² ε] > λ. For uniform W and
λ = σ = 1, ε has variance ½ and κ_c ≈ 1.38. A36's κ = λ is the limit of no
member noise.

## Checked when filed

By script (numpy), M = 24 and a random row-stochastic W:
- the identity ℓᵀ(κW − λI) = (κ − λ)ℓᵀ holds exactly at (κ, λ) = (1, 1),
  (0.3, 0.9) and (1.5, 0.5);
- at κ = λ = 0.5, 400 runs of 2,000 steps at dτ = 0.01: variance rate
  0.0448 predicted and 0.0448 observed; drift −0.0089 predicted and
  −0.0118 observed, drift being the noisier estimate;
- the regression slope of the increment on L was −0.008, −0.48 and 0.50
  against κ − λ = 0, −0.5 and 0.5;
- with pairwise noise correlation ½, the observed variance rate was 0.997
  of ℓᵀΣℓ, which was 12.4 times Σℓᵢ²;
- M_eff = 3.833 for A36's example;
- with drift 0.5, σ = 1 and bounds at ±1 on L, 20,000 runs each:

  | κ − λ | 0 | 0.5 | 1 | 2 |
  |---|---|---|---|---|
  | P(correct) | 0.732 | 0.717 | 0.708 | 0.677 |
  | mean decision time | 0.96 | 0.82 | 0.72 | 0.56 |

  against the analytic drift-diffusion value 0.731 at κ = λ;
- for the tanh version, E[sech² ε] = 0.726 for ε ∼ N(0, ½), so κ_c = 1.377.
  A simulation (M = 50, 200 runs, d = 0) gave a mean |L| of 0.12, 0.16,
  0.20, 0.37, 0.99 and 1.77 at κ = 0.8, 1.0, 1.2, 1.4, 1.6 and 2.0.

A37's own check, "residual variance 1.003 against 1" over 24 perspectives
and 200 trials, tests an identity that holds at every Euler step by
construction. It verifies the code, not the theory, as A37 itself said:
"That verifies the implementation of this benchmark; it does not yet
establish the broader organizational hypothesis."

## What it can show

That a collective can be an exact drift-diffusion decider when none of its
members is one. That its noise is set by how concentrated influence is.
That the condition is a balanced linear mode, and that a public tally is a
dial on it.

## What it cannot show

- Emergence. A35's self-audit of its own app applies here too: "we obtain
  the result because Gaussian additive evidence is built into the update
  rule". A36: "a unit test for the population simulator, not an empirical
  test of our philosophical theory."
- A decision. The result is the marginal law of L. The collective decision
  is a drift-diffusion decision only if commitment is a bound on L. A bound
  on one member's support, or on a majority count, is not.
- Anything for a readout not weighted by ℓ, such as a uniform average or
  one member's support. Those carry a stationary transverse term.
- Anything for a reducible W. Several closed groups give several balanced
  modes, and L is then one neutral coordinate among several.
- Anything for binary positions. A37 called xᵢ "each perspective's binary
  support variable". If the members broadcast sign(xⱼ) in place of xⱼ, the
  closure fails: the drift of L then depends on the members' positions,
  not on L alone, and a check at κ = λ gave a nonzero slope.
- Endogenous influence. With W(τ), dL gains (dℓ)ᵀx (A36). That term is
  where governance enters, reflected appraisal among others
  ([THEORY-tmphmdtd](../theory.d/THEORY-tmphmdtd.md)), and it is not covered here.
