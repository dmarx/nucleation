---
number: 750
status: Active
formerly:
- THEORY-tmpe0x90
title: 'For a stationary Gaussian signal the lag-τ entropy rate with one-point embedding is h_τ = H(X) + ½ log(1 − c(τ)²), so where the normalized second-order structure function 1 − c(τ) is small and scales as τ^ζ₂, h_τ = (ζ₂/2) log τ + constant; the "scaling of information" that Granero-Belinchón, Roux and Garnier measure in near-Gaussian wind-tunnel turbulence, slope 1/3 in the inertial range and 1 in the dissipative range, is the scaling of the second-order structure function written in nats'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-970. The formula is the paper's (3) and the
    slopes its reading of the Batchelor model (4). Every step is re-derived
    below and checked numerically, which meets ADR-047 v2. The application
    to the turbulence data rests on one measurement, the paper's report
    that its k-nearest-neighbour estimate agrees with (3) at all but the
    smallest scales; the title claims no more than that study measured, so
    ADR-047 v3 applies. The reading of the result as "nothing beyond S₂"
    is the paper's own Discussion, stated here as a theorem with its
    conditions.
tags:
- information-theory
- natural-sciences
date: '2026-10-20'
source:
- LIT-1243
answers:
- QUESTION-219
summary: >-
  Granero-Belinchón, Roux and Garnier (2016), [LIT-1243](../literature.d/LIT-1243.md), read in full in
  [NOTE-970](../notes.d/NOTE-970.md). A Gaussian identity and its small-lag asymptotics: the
  conditional entropy of x(t) given x(t − τ) is a monotone function of the
  autocorrelation, so its scaling exponent is half the structure-function
  exponent. In the Modane data the estimated entropy rate matches the
  Gaussian formula, so the measured "information spectrum" is S₂ again. It
  is not a distribution of a conserved quantity over scales, and it carries
  nothing about the direction or size of energy transfer. It answers
  [QUESTION-219](../questions.d/QUESTION-219.md) only in the narrow sense of supporting A3's caution.
---

# THEORY-750: For a stationary Gaussian signal the lag-τ entropy rate with one-point embedding is h_τ = H(X) + ½ log(1 − c(τ)²), so where the normalized second-order structure function 1 − c(τ) is small and scales as τ^ζ₂, h_τ = (ζ₂/2) log τ + constant; the "scaling of information" that Granero-Belinchón, Roux and Garnier measure in near-Gaussian wind-tunnel turbulence, slope 1/3 in the inertial range and 1 in the dissipative range, is the scaling of the second-order structure function written in nats

## Source

Granero-Belinchón, Roux and Garnier (2016), *EPL* 115, 58003, [LIT-1243](../literature.d/LIT-1243.md),
read in full in [NOTE-970](../notes.d/NOTE-970.md) from arXiv:1607.05511v2. The formula is the
paper's (3). The slopes −1/3 and −1 (against log of inverse scale) are its
reading of the Batchelor model (4) through (3). The derivation below is the
record's.

## What was actually shown

**Setting.** x(t) is a stationary, centred Gaussian signal with variance σ²
and normalized autocorrelation c(τ), |c| < 1. The paper's entropy rate with
embedding m = 1 is the conditional differential entropy of one sample given
the sample a lag τ away, h_τ^(1) = H(x(t) | x(t − τ)), in nats.

**Step 1. The identity.** Given x(t − τ) = y, x(t) is Gaussian with mean
c(τ)y and variance σ²(1 − c(τ)²), which does not depend on y. The entropy of
a Gaussian of variance v is ½ log(2πe v). So

  h_τ^(1) = ½ log(2πe σ²(1 − c²)) = H(X) + ½ log(1 − c(τ)²),

with H(X) = ½ log(2πe σ²). This is the paper's (3).

**Step 2. Small-lag asymptotics.** Write s(τ) = 1 − c(τ) = S₂(τ)/(2σ²),
the normalized second-order structure function. Then 1 − c² = s(2 − s), and

  h_τ^(1) − H(X) = ½ log s + ½ log 2 + ½ log(1 − s/2).

If s ∝ τ^ζ₂ and s ≪ 1, the last term is O(s) and h_τ^(1) = (ζ₂/2) log τ +
constant. With K41's ζ₂ = 2/3 the slope is 1/3; for a smooth signal, ζ₂ = 2
and the slope is 1. Against log(f_s/τ), the paper's axis, the slopes are
−1/3 and −1. As τ grows past the correlation time, c → 0 and h_τ^(1) → H(X),
the flat integral-range value the paper reports.

**Step 3. fBm.** For fractional Brownian motion of Hurst exponent H, at
times t ≫ τ the conditional variance of B(t) given B(t − τ) tends to the
increment variance σ₀²τ^(2H), so h_τ^(1) ≈ H log τ + ½ log(2πe σ₀²). This
is the paper's (6). For H = 1/3 the slope is 1/3; the paper measures
0.32 ± 0.01 on a synthetic signal.

**Checked numerically** (script in the session scratchpad, not in the
repository). With s(τ) taken from the Batchelor form (τ/L)^(2/3)/(1 +
(η/τ)²)^(2/3), L = 1, η = 10⁻³, the fitted slope of ½ log(1 − c²) against
log τ is 0.337 for 3 × 10⁻³ < τ < 3 × 10⁻² and 1.000 for 10⁻⁶ < τ < 10⁻⁵.

**The empirical step.** The paper estimates h_τ^(1) from the Modane
wind-tunnel signal with k-nearest-neighbour estimators ([THEORY-709](THEORY-709.md)), and
reports that the result is "almost identical" to (3) computed from the
measured autocorrelation, and that (3) "holds at all scales" for m = 1.
Embeddings m = 2, 3 change nothing outside the dissipative range. So in
these data the measured information scaling is the S₂ scaling, as the
paper's Discussion says: it "contains the same physics as the one given
by the second order structure function".

**What could have come out otherwise.** A strongly non-Gaussian two-point
distribution would have pulled the estimate below (3). The Gaussian value
is the maximum conditional entropy for a given covariance, so any
non-Gaussian dependence can only lower it. The paper reports no
measurable gap outside the dissipative range.

## What this does not say

- **That the entropy rate sees nothing beyond S₂ in any signal.** Steps 1–3
  are about Gaussian signals. For a non-Gaussian signal h_τ depends on the
  whole two-point law. The claim about turbulence is the paper's empirical
  report for one velocity record, estimated with a resolution of 0.03 to
  0.08 nats.
- **That information is distributed over scales.** h_τ at different τ are
  not parts of a total. They do not sum to an entropy, no balance law
  links them, and nothing is transferred between them. Choosing a lag τ is
  down-sampling without low-pass filtering, so every smaller scale stays
  in the signal. "Information spectrum" and "distribution of information
  amongst scales" are the paper's words for a lag-dependent conditional
  entropy, not a band decomposition like [THEORY-754](THEORY-754.md)'s.
- **Anything about energy transfer.** S₂ is even in the increments. The
  third-order structure function, which the 4/5 law ties to the energy
  flux, does not enter. [THEORY-748](THEORY-748.md) shows that the entropy rate is
  blind to that asymmetry by symmetry, not just weakly sensitive to it.
- **That increasing m measures higher-order statistics.** For a Gaussian
  process the m-point entropy rate depends only on c(τ) at multiples of τ.
  For fBm with H = 1/3, conditioning on one more past point shifts h by
  ½ log(1 − ρ²) ≈ −0.022 nats, where ρ = 2^(2H−1) − 1 ≈ −0.206 is the
  correlation of consecutive increments. That is below the paper's
  standard deviation of 0.03. So "no measurable evolution" with m is
  expected even for a Gaussian non-Markov signal, and says little about
  non-Gaussian correlations.

## Connections

- **[THEORY-754](THEORY-754.md).** Eyink and Aluie's band decomposition is exact, with
  a flux that telescopes between bands. The entropy rate at lag τ has no
  such budget. The two use "scale" for different things: a filter band
  there, a sampling lag here.
- **[QUESTION-219](../questions.d/QUESTION-219.md).** It supports A3's caution that energy transfer and
  information transfer "should not be identified merely because both can
  be assigned a direction across scales". This paper's information
  quantity is not even assigned a direction. It is a monotone function of
  S₂, an even, two-point statistic.
- **[THEORY-709](THEORY-709.md).** The estimator behind the empirical step.
