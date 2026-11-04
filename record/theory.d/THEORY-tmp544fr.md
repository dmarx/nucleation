---
status: Active
title: 'For a small-noise diffusion the Freidlin–Wentzell quasi-potential equals 2 inf ∫ |b| sin²(θ/2) ds over curves, θ the angle between curve and drift, and the minimizing curve is the path a noise-driven transition follows with probability tending to one; with gradient drift and identity noise that curve runs against the drift, the time-reversed relaxation path, while a far-from-gradient drift, as in the Maier–Stein model above β = 4, makes it depart from the heteroclinic orbit'
version: 1
tags:
- mathematics
- complex-systems
date: '2026-11-03'
source:
- LIT-tmpk8i57
summary: >-
  Heymann and Vanden-Eijnden (2008), [LIT-tmpk8i57](../literature.d/LIT-tmpk8i57.md), read in part in
  [NOTE-tmp6wm7j](../notes.d/NOTE-tmp6wm7j.md) (§§1, 2.1–2.2, 4.1, 5). Active: the geometric formula and
  the gradient case were re-derived for this reading; the path
  concentration is Proposition 2.3, whose proof was not read but whose
  statement is standard Freidlin–Wentzell theory; the Maier–Stein
  threshold is the paper's computation agreeing with Maier and Stein's.
  It does not say anything at finite noise, or for degenerate noise, which
  the paper's ellipticity assumption excludes.
---
<!-- inactive-ok-file: NOTE-tmp6wm7j — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->

# THEORY-tmp544fr: For a small-noise diffusion the Freidlin–Wentzell quasi-potential equals 2 inf ∫ |b| sin²(θ/2) ds over curves, θ the angle between curve and drift, and the minimizing curve is the path a noise-driven transition follows with probability tending to one; with gradient drift and identity noise that curve runs against the drift, the time-reversed relaxation path, while a far-from-gradient drift, as in the Maier–Stein model above β = 4, makes it depart from the heteroclinic orbit

## Source

Heymann and Vanden-Eijnden (2008), [LIT-tmpk8i57](../literature.d/LIT-tmpk8i57.md); read in [NOTE-tmp6wm7j](../notes.d/NOTE-tmp6wm7j.md).

## What was actually shown

- **The formula** (eqs. 1.16–1.18): from ½|ψ̇ − b|²_a ≥ |ψ̇|_a|b|_a −
  ⟨ψ̇, b⟩_a, with equality at |ψ̇| = |b|, V(x₁, x₂) = 2 inf_γ ∫ |b|_a
  sin²(θ/2) ds. Re-derived.
- **Concentration** (Proposition 2.3): given a transition, the process stays
  in any tube around the unique minimizing curve with probability → 1 as
  ε → 0.
- **Gradient case** (p. 1058): with b = −∇U and σ = I, "transition paths are
  always parallel to the drift". Re-derived: along an uphill curve
  ∫ |∇U|(1 − cos θ) ds ≥ ΔU, with equality only when the curve runs against
  the drift everywhere, so V to the saddle is 2ΔU and the path is the
  reversed relaxation path.
- **Maier–Stein** (§4.1): gradient only at β = 1, yet the minimum action path
  is the heteroclinic orbit for β ≤ 4; above 4 it is not.

## What this does not say

- That the path is distinguishable at finite noise from one sample.
- That any nongradient drift changes the path: in Maier–Stein it takes β > 4.
- That it applies to degenerate noise (Assumption 3 requires ellipticity).
