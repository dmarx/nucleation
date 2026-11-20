---
status: Proposed
title: 'In a linear Gaussian restatement step with per-step noise, the information a feature keeps about its start falls geometrically, as a to the power 2n, where the step contracts the feature, and only as 1/n where the step copies it with error: a feature copied with any error drifts slowly instead of settling, and only a feature copied exactly keeps its start'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the variance of the n-step noise,
  σ²(1 − a²ⁿ)/(1 − a²) for |a| < 1 and nσ² for a = 1, in the Gaussian
  mutual information ½ ln(1 + a²ⁿ s² / Vₙ), or in the two asymptotic
  rates; or a linear Gaussian step meeting the hypotheses in which a
  feature with a = 1 and σ > 0 keeps information about its start bounded
  away from zero.
tags:
- information-theory
- probabilistic-modeling
- design-rationale
date: '2026-11-20'
line:
- formal-apparatus
- nucleating-argument
rests_on:
- CLAIM-635
- CLAIM-270
summary: >-
  The rate that sets apart the three kinds of feature in CLAIM-tmpdx6l8.
  CLAIM-635 holds the exact case (a feature conserved exactly keeps its
  start for ever) and shows that a bounded defect allows forgetting, with
  a two-state flip chain as witness. That witness is itself contracting.
  This adds the neutral case on an unbounded state: a feature copied with
  error forgets, but only as 1/n, against the geometric rate of a
  contracting one. Derived and checked by simulation (2026-11-20). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-635 CLAIM-tmpdx6l8 — Proposed; the exact case this extends, and the claims filed with it -->

# CLAIM-tmpw6wkt: In a linear Gaussian restatement step with per-step noise, the information a feature keeps about its start falls geometrically, as a to the power 2n, where the step contracts the feature, and only as 1/n where the step copies it with error: a feature copied with any error drifts slowly instead of settling, and only a feature copied exactly keeps its start

## The claim

Take one feature of an entry, x, restated at each step by

  xₙ₊₁ = a·xₙ + (1 − a)·c + σ·ξₙ,  ξₙ i.i.d. N(0, 1),  x₀ ~ N(0, s²),

with c the step's own fixed point (the convention) and σ > 0 the per-step
error. Then

  xₙ = aⁿx₀ + (1 − aⁿ)c + noise of variance Vₙ,
  Vₙ = σ²(1 − a²ⁿ)/(1 − a²) for |a| < 1, and Vₙ = nσ² for a = 1,

and, the pair being jointly Gaussian,

  I(x₀; xₙ) = ½ ln(1 + a²ⁿ s² / Vₙ).

- **Contracting (|a| < 1).** Vₙ → σ²/(1 − a²), so I ≈ ½ a²ⁿ s²(1 − a²)/σ²:
  the start is forgotten geometrically, and xₙ settles near c, within a
  spread fixed by σ and a.
- **Copied with error (a = 1, σ > 0).** I = ½ ln(1 + s²/(nσ²)) ≈ s²/(2nσ²):
  the start is forgotten, but only as 1/n, and the feature does not settle;
  it random-walks with spread √n·σ.
- **Copied exactly (a = 1, σ = 0).** xₙ = x₀: the start is kept whole. This
  is CLAIM-635's case.

**Check.** Simulated with 200,000 chains (s = 1, σ = 0.1, c = 3) for
a = 1, 0.9 and 0.5, at n = 10, 100 and 400: the closed form matched the
empirical Gaussian information (from the sample correlation) wherever it is
above the sampling floor of about 10⁻⁵ nats; at a = 1, n·I rose toward
s²/(2σ²) = 50 (12.0, 34.7, 44.6). Script in the curation entry of
2026-11-20, 230350.

## What it adds to CLAIM-635

CLAIM-635 shows that exact conservation keeps a lower bound on retention
for ever, and that a bounded defect allows forgetting. Its witness, a
two-state chain flipping with probability p, is contracting (its
nonconstant eigenvalue is 1 − 2p), so it forgets geometrically. This claim
gives the case between: a feature the step leaves neutral but copies with
error. It forgets too, but at a rate slower by an exponential. The three
rates are what CLAIM-tmpdx6l8's three kinds of feature are distinguished by.

## What it does not say

- Not that noiseless contraction forgets in the information sense. With
  σ = 0 and |a| < 1, x₀ is recoverable in principle from xₙ; the step only
  shrinks its trace below any fixed resolution. Forgetting in information
  needs noise.
- Not that restatement is linear or Gaussian. The rates are for this
  model; CLAIM-635 holds the exact case for any Markov kernels. That the
  neutral case forgets polynomially and not geometrically beyond this
  model is not shown.
