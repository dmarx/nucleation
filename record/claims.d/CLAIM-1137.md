---
number: 1137
status: Proposed
formerly:
- CLAIM-tmpm9sp7
title: 'Adaptation speed times passed noise is constant'
statement: >-
  For a reference adapting as ż = k(d + n − z), the time to come within δ of
  a unit step in demand, ln(1/δ)/k, times the stationary variance it takes
  from white noise of intensity σ², kσ²/2, is σ² ln(1/δ)/2 whatever k is, so
  a deadline H for the step sets a floor σ² ln(1/δ)/(2H) on the noise the
  reference passes
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the derivation or the check; or a reference following
  this first-order rule whose product of step-response time and stationary noise
  variance depends on k.
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
- readiness
rests_on:
- CLAIM-1152
complements:
- CLAIM-1010
uses:
- TERM-115
summary: 'A gap fill: a gap of the manuscript governance-of-possibility, §4 (GB4),
  which finds no combined result for how fast a reference should be revisable
  given both a deadline and a noise spectrum. For [CLAIM-1152](CLAIM-1152.md)''s first-order
  reference the two pictures meet in a conserved product. Checked with python3
  -I. The wording is the assistant''s (Claude, in this session); adopting it is
  the owner''s call.'
---

# CLAIM-1137: Adaptation speed times passed noise is constant

## The derivation

[CLAIM-1152](CLAIM-1152.md)'s reference: ż = k(d + n − z), H_k(s) = k/(s + k).

- **The deadline picture.** With no noise and a unit step in d at t = 0,
  z(t) = 1 − e^{−kt}, so |1 − z| ≤ δ from t_δ = ln(1/δ)/k on.
- **The frequency picture.** With d = 0 and n white of intensity σ²
  (E n(t)n(s) = σ²δ(t − s)), z is an Ornstein–Uhlenbeck process,
  dz = −kz dt + kσ dW, with stationary variance
  ∫₀^∞ (k e^{−ku})² σ² du = kσ²/2. In [CLAIM-1152](CLAIM-1152.md)'s terms it is the
  noise passed, σ² ∫ k²/(k² + ω²) dω/2π.

So t_δ · Var z = σ² ln(1/δ)/2, independent of k. Speeding the reference
up shortens the time to meet a changed demand and raises the noise it
passes in exact proportion; no k improves both. A deadline H for meeting
the step to within δ needs k ≥ ln(1/δ)/H, hence
Var z ≥ σ² ln(1/δ)/(2H): the shorter the deadline, the more noise the
reference must pass.

This sets [CLAIM-1152](CLAIM-1152.md)'s noise cost beside a deadline, as [TERM-115](../terms.d/TERM-115.md) poses
deadlines. [CLAIM-1010](CLAIM-1010.md) gives the speed floor vH ≥ 1 − δ − ε for a
reference revisable at a bounded rate; that is a different model, a rate
limit rather than a first-order rule, and the two answer different parts
of the manuscript's question.

## The check

With python3 -I, σ = 0.7 and δ = 0.05: integrating the step response
numerically gives t_δ = 14.979, 2.996 and 0.599 at k = 0.2, 1 and 5,
against ln(20)/k = 14.979, 2.996 and 0.599. The variance by quadrature
of the impulse response is 0.049, 0.245, 1.225 and 4.9 at k = 0.2, 1, 5
and 20, equal to kσ²/2. The product is 0.7340 at every k, equal to
σ² ln(20)/2. Simulated processes (exact discretization, 4 × 10⁵ steps)
gave variances of 0.0491, 0.2276 and 1.267 against 0.049, 0.245 and
1.225, within sampling error.

## What it does not say

- Not the best k: that needs the two errors weighed, as [CLAIM-1152](CLAIM-1152.md)'s
  λ does.
- Nothing for other filters. The product is for the first-order rule; a
  higher-order filter, or one shaped to the spectra ([CLAIM-1152](CLAIM-1152.md)'s
  T*), can trade differently.
- Nothing for coloured noise or demands other than a step. With noise,
  being within δ by H is a probability, as [TERM-115](../terms.d/TERM-115.md)'s readiness is; the
  claim gives the time of the mean response only.

## Gap filled

A gap of the manuscript governance-of-possibility, §4 (GB4): "The record
holds no combined result that says how fast a reference should be
revisable given both a deadline and a noise spectrum."
