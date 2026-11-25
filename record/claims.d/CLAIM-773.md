---
number: 773
status: Proposed
formerly:
- CLAIM-tmphedau
title: 'Drift splits by how each feature is copied'
statement: >-
  In a linear Gaussian restatement step, an idea's drift from its source
  splits by the part of the step each feature lies in: a contracted feature
  drifts toward the convention and stops there, a feature copied with random
  error drifts undirected as the square root of the number of steps, a
  feature copied with a bias drifts directed and without bound, and a
  conserved one does not drift; a constant bias costs no retention, so drift
  and retention vary independently; and a feature passes a distance δ after
  about δ²/σ² restatements by random error, after ln(D/(D − δ))/ln(1/a) by
  contraction toward a convention at distance D > δ, and by contraction
  toward a convention nearer than δ only through noise
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in the bias (1 − aⁿ)(c − x₀) or nμ, in the
  variance σ²(1 − a²ⁿ)/(1 − a²) or nσ², in the Gaussian information
  ½ ln(1 + a²ⁿ s²/Vₙ) and its independence of μ, in the leading-order exit
  time δ²/σ² of a Gaussian walk from (−δ, δ), or in the deterministic
  crossing time; or a linear Gaussian step meeting the hypotheses whose
  drift falls outside the four kinds.
tags:
- probabilistic-modeling
- information-theory
- design-rationale
date: '2026-11-20'
line:
- formal-apparatus
- nucleating-argument
rests_on:
- CLAIM-779
- CLAIM-635
- CLAIM-270
uses:
- TERM-132
summary: >-
  A formal account of drift, at the owner's request of 2026-11-20
  ("connect to drift (which I think we can account for formally now if we
  haven't already)"). The record held drift as a phenomenon ([CLAIM-177](CLAIM-177.md)),
  three explanations of it ([CLAIM-180](CLAIM-180.md), [CLAIM-186](CLAIM-186.md), [CLAIM-191](CLAIM-191.md)) and bounds
  ([CLAIM-056](CLAIM-056.md), [CLAIM-107](CLAIM-107.md)), but no model that gives its kinds. This splits
  drift, by the parts of a restatement step ([CLAIM-772](CLAIM-772.md)), into four
  kinds with their rates, builds [CLAIM-081](CLAIM-081.md)'s independence of drift and
  retention, and gives the number of restatements before an idea passes a
  critical distance. Derived and checked by simulation (2026-11-20). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-779 CLAIM-772 TERM-132 CLAIM-180 CLAIM-186 CLAIM-191 CLAIM-189 CLAIM-114 — Proposed; the results this extends, and the claims it bears on -->

# CLAIM-773: Drift splits by how each feature is copied

## The model

One feature of an idea, restated once per step:

  xₙ₊₁ = a·xₙ + (1 − a)·c + μ + σ·ξₙ,  ξₙ i.i.d. N(0, 1),  x₀ ~ N(m, s²),

with c the step's fixed point (the convention), μ a systematic bias (taken
only with a = 1, where it is not absorbed into c), and σ the random error.
This is [CLAIM-779](CLAIM-779.md)'s model with a bias added. **Drift** is the
displacement dₙ = xₙ − x₀. Its mean square is bias squared plus variance.

## The four kinds

| Part ([TERM-132](../terms.d/TERM-132.md)) | E[dₙ \| x₀] | Var(dₙ \| x₀) | Kind |
|---|---|---|---|
| contracting, a < 1 | (1 − aⁿ)(c − x₀) | σ²(1 − a²ⁿ)/(1 − a²) | directed, saturating at the convention |
| copied with error, a = 1, μ = 0 | 0 | nσ² | undirected, diffusive, RMS √n·σ |
| copied with bias, a = 1, μ ≠ 0 | nμ | nσ² | directed, unbounded, linear in n |
| conserved, a = 1, μ = σ = 0 | 0 | 0 | none |

Directed drift therefore comes in two shapes, saturating (a fixed point) and
linear (a bias with none). Undirected drift grows as √n.

## Drift and retention vary independently

I(x₀; xₙ) = ½ ln(1 + a²ⁿ s²/Vₙ), with Vₙ the variance above, does not
depend on μ: a constant shift is invertible and loses nothing. So:

- copied with bias and no error (μ ≠ 0, σ = 0): drift nμ, retention whole;
- contracting: drift bounded by |c − x₀| plus noise, retention lost
  geometrically ([CLAIM-779](CLAIM-779.md));
- copied with error: drift √n·σ, retention lost as 1/n.

Every combination of large or small drift with high or low retention occurs.
[CLAIM-081](CLAIM-081.md) and [CLAIM-270](CLAIM-270.md) hold that the two are different profiles; this
constructs each pairing in one model.

## Passing a critical distance

Let an idea be lost, in [CLAIM-180](CLAIM-180.md)'s sense, when its displacement first
reaches δ.

- **Copied with error.** The expected exit time of a Gaussian walk from
  (−δ, δ) is δ²/σ² to leading order. Discrete steps overshoot the boundary;
  with the standard overshoot of about 0.583σ (−ζ(½)/√(2π), cited from
  memory and not on the record) the estimate is (δ + 0.583σ)²/σ².
- **Contracting, convention at distance D = |c − x₀| > δ.** Ignoring noise,
  the displacement D(1 − aⁿ) reaches δ at n* = ln(D/(D − δ))/ln(1/a):
  fast and deterministic.
- **Contracting, D < δ.** The mean never reaches δ; only noise carries the
  feature out, a rare event when the stationary spread σ/√(1 − a²) is small
  beside δ − D.

## Checks

Simulated on 2026-11-20 (scripts in the curation entry of 2026-11-20,
231623):

- Exit time, σ = 0.1, 20,000 walks: 31.7 steps for δ = 0.5 against
  δ²/σ² = 25 and (δ + 0.583σ)²/σ² = 31.2; 112.5 for δ = 1 against 100 and
  112.0.
- Crossing, a = 0.9, D = 2: n* = 2.73 for δ = 0.5 and 13.16 for δ = 1.5; none
  for δ = 2.5.
- Retention and bias, s = 1, σ = 0.1, n = 50, 200,000 chains: information
  0.5492 nats with μ = 0 and 0.5487 with μ = 0.5 (mean drift 25.0), against
  0.5493 from the formula.

## What it does not say

- Not that restatement is linear, Gaussian or one feature at a time. The
  conserved case holds for any Markov steps ([CLAIM-635](CLAIM-635.md)); the rest is this
  model's.
- Not that distance is the only drift that matters. A change of identity
  with every distance small ([CLAIM-031](CLAIM-031.md), [CLAIM-114](CLAIM-114.md)) is outside it.
- Not that drift is loss. The biased, noiseless case drifts without bound
  and loses nothing; [CLAIM-189](CLAIM-189.md)'s legitimate change can be drift of that kind.
- Nothing about distortion that breaks the triangle inequality
  ([QUESTION-017](../questions.d/QUESTION-017.md)): the model is metric.
