---
number: 168
status: Open
formerly:
- QUESTION-tmpnscuv
title: 'Does the ℓ₁ recovery transition of some non-Gaussian measurement ensemble provably converge to the Gaussian curve ρ(δ) as N → ∞, or do simulations an order of magnitude beyond N = 1600 keep the gap shrinking as N^(−1/2) for an ensemble not used to choose that exponent?'
version: 1
tags:
- mathematics
- mathematical-statistics
date: '2026-10-19'
line: formal-apparatus
refines:
- QUESTION-120
summary: >-
  Filed when the promotion audit (batch 025, [ADR-047](../decisions.d/ADR-047.md) v3) narrowed and
  promoted [THEORY-391](../theory.d/THEORY-391.md) to what Donoho and Tanner measured. In 2,948,000
  optimizations at N = 200, 400 and 1600, eight non-Gaussian ensembles
  approached the Gaussian curve, consistent with N^(−1/2) gaps. Whether
  that agreement is a limit theorem is [THEORY-391](../theory.d/THEORY-391.md)'s former promote_when,
  moved here unchanged.
answered_by:
- THEORY-tmpgv8ip
---

# QUESTION-168: Does the ℓ₁ recovery transition of some non-Gaussian measurement ensemble provably converge to the Gaussian curve ρ(δ) as N → ∞, or do simulations an order of magnitude beyond N = 1600 keep the gap shrinking as N^(−1/2) for an ensemble not used to choose that exponent?

## Why it is a question

[THEORY-391](../theory.d/THEORY-391.md) now states only what was observed, at three problem sizes,
with the exponent N^(−1/2) fitted on the same data. Random signs fit the
model out of sample, but that is one ensemble at the same sizes. The
authors say the result "goes far beyond current theory", and the
universality class is not delineated. The Gaussian curve itself comes
from the authors' earlier face-counting theorems, which the record does
not hold.

## What would answer it

Either of these would answer it yes:
- A proof, for some non-Gaussian ensemble in the paper's class such as
  random signs, that the ℓ₁ recovery transition converges to the Gaussian
  ρ(δ; C) as N → ∞.
- Simulations at problem sizes an order of magnitude beyond N = 1600, in
  which the gap to the Gaussian curve keeps shrinking as N^(−1/2) for an
  ensemble not used to choose that exponent.

An ensemble whose gap stops shrinking would answer it no. More
simulations at the same sizes do not settle it.
