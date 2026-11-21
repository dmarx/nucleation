---
status: Proposed
title: 'Two mechanisms that merge: in F(a, b) = (a + b, ab), and in a sum of two exponentials with rates u ± v, the predictions depend on the difference v only through v², so the smaller Fisher eigenvalue falls as v² and is zero on the stratum a = b, where the model image has a smooth fold edge, the learning coefficient at a true point on the edge is 3/4 against 1 inside, and a smooth prior pushed into prediction space diverges at the edge as the inverse square root of the distance'
version: 1
standing: stipulated
kind: construction
tags:
- information-geometry
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
variant_of:
- CASE-152
draws_on:
- THEORY-087
- THEORY-1253
summary: >-
  A39 §§2–4 of the exchange "Rich Get Richer Power Laws" (2026-11-21),
  answering the owner's U24, with the assistant's checks and two
  additions: the same edge in the textbook sloppy model, a sum of
  exponentials, and the learning coefficient at a true point on the edge
  away from the origin and inside the image. A smallest case in which a
  thin direction turns into a degenerate one. The construction is A's (the
  other assistant in the exchange "Rich Get Richer Power Laws", A39); the
  additions are the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmpcgvcp LIT-tmpd3swn LIT-tmpzkxka — a Proposed claim filed with this case, and Deferred works registered from the exchange and not yet read -->

# CASE-tmpb2gly: Two mechanisms that merge: in F(a, b) = (a + b, ab), and in a sum of two exponentials with rates u ± v, the predictions depend on the difference v only through v², so the smaller Fisher eigenvalue falls as v² and is zero on the stratum a = b, where the model image has a smooth fold edge, the learning coefficient at a true point on the edge is 3/4 against 1 inside, and a smooth prior pushed into prediction space diverges at the edge as the inverse square root of the distance

## The construction

A39 §2: "Consider a two-parameter model with predictions F(a,b)=(a+b, ab)",
observed with isotropic Gaussian noise, so the Fisher matrix is JᵀJ/σ². Put
u = (a + b)/2 and v = (a − b)/2. Then F = (2u, u² − v²): the predictions
depend on the difference v only through v². The swap a ↔ b is a discrete
redundancy; the merge a = b (v = 0) is a continuous one.

Everything below was checked by the assistant with `python3 -I`
(scripts in the session scratchpad, `t5/check1.py` to `check3.py`).

- **Fisher spectrum.** J = [[2, 0], [2u, −2v]], so JᵀJ has determinant 16v²
  and trace 4 + 4u² + 4v². The smaller eigenvalue is 4v²/(1 + u²) to
  leading order (3.199 × v² at u = ½, v = 0.01) and the larger stays near
  4(1 + u²). At v = 0 the rank drops to 1. A thin direction becomes, as v
  shrinks, an exactly degenerate one: A's "a precise mathematical
  realization of the transition from a thin direction to a degenerate one".
- **The image.** Since (a − b)² = s² − 4p ≥ 0, the image is p ≤ s²/4. Its
  edge is a smooth parabola; the singular thing is the map, which folds
  the plane onto the region along a = b. A39: "The boundary itself is a
  smooth curve. The singularity is that the two-parameter map loses rank
  when it reaches that curve."
- **Learning coefficient.** With the truth at a = b = 0, the squared error
  is K = 4u² + (u² − v²)² ≍ u² + v⁴, and the local evidence falls as
  n^(−3/4): the slope −d log Z/d log n over [−1, 1]² is 0.754, 0.751,
  0.750, 0.750 at n = 10², 10³, 10⁴, 10⁶. A regular two-parameter point
  gives 1.
- **The same away from the origin** (the assistant's check, answering the
  ledger's question whether the 3/4 is local to the origin). With the
  truth at a = b = ½, a point on the edge, the slope is 0.750 at n = 10⁴,
  10⁵ and 10⁶: K = 4δu² + (2c·δu + δu² − v²)² is again ≍ δu² + v⁴ for any
  c. With the truth inside the image, at (0.2, 0.8), the true set is the
  two points (0.2, 0.8) and (0.8, 0.2), each regular, and the slope is
  1.003, 1.000, 1.000. The swap doubles the evidence and leaves the
  exponent alone. So λ = 3/4 holds along the whole stratum a = b, and λ = 1
  off it.
- **Pushed-forward prior.** |∂(s, p)/∂(u, v)| = 4|v| and v² = s²/4 − p, so
  a smooth prior on (u, v) gives a density ∝ (s²/4 − p)^(−1/2) near the
  edge: divergent and integrable. Checked by Monte Carlo (4 × 10⁶ uniform
  draws, the slab |s| < 0.05): density × √(depth) stays within 3.7–4.7 ×
  10⁴ while depth runs from 2 × 10⁻⁴ to 1.3 × 10⁻².

## The same edge in the textbook sloppy model

The assistant's addition. The model behind the hyperribbon picture
(LIT-tmpd3swn, LIT-tmpzkxka) is a sum of exponentials. Take two,
y(t) = e^(−k₁t) + e^(−k₂t), with k₁,₂ = u ± v. Then y = 2e^(−ut)cosh(vt),
which also depends on v only through v². Sampled at 40 times in
[0.1, 5] with u = 1, the smaller Fisher eigenvalue divided by v² is
3.21, 4.88, 5.43, 5.57 at v = 0.4, 0.2, 0.1, 0.05, settling to a constant,
and it is exactly 0 at v = 0. With four distinct rates (0.5, 1, 2, 4) the
Fisher eigenvalues run from 2.5 × 10⁻³ to 15.7, a spread of 6 × 10³ with
none zero: sloppy and regular. Equal rates are a fold edge of this
model's image, and the edge is a singular stratum of exactly this case's
kind.

## What it shows, and what it cannot

It shows that a sloppy eigenvalue can be the shadow of a nearby stratum:
near a = b the thin direction is thin *because* the stratum is near, and
its eigenvalue measures the squared distance to it. It also shows the
point Fisher spectrum missing what decides the learning coefficient: at
v = 0 it reports one zero eigenvalue and nothing about the quartic.

It cannot show that every thin direction ends at a stratum. A linear
model with an ill-conditioned design is sloppy everywhere and singular
nowhere (CLAIM-tmpcgvcp). Nor does the pushed-forward density say where a
trained network's probability goes. In a Bayesian model the likelihood
depends on the parameters only through (s, p), so the posterior's image
in prediction space keeps the same factor (s²/4 − p)^(−1/2): the
concentration at the edge survives conditioning on data. Gradient
training samples no posterior, so nothing here transfers to it. The
case is stipulated: its numbers are facts of the definition, not
observations of any network.
