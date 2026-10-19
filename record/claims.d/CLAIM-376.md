---
number: 376
status: Active
formerly:
- CLAIM-tmp007ve
title: 'A linear system that is stable at every instant can have a positive Lyapunov exponent: shifting any operator with exponent λ > 0 by −δI lowers its exponent by exactly δ and makes every instantaneous operator stable, so for 0 < δ < λ the shifted system is stable at every instant and unstable'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Filed Active at the owner's direction, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/THEORY-325.yaml,
    batch 006, ADR-047). Farrell & Ioannou state that destabilization
    persists when the operator is stable at each instant without showing
    it (NOTE-842). This is the record's own construction that shows it, so
    it is a CLAIM (ADR-032), applied to the paper's switched oscillator
    with the Floquet multipliers computed in closed form.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below or in the computed monodromy: an operator
  A(t) with exponent λ for which A(t) − δI does not have exponent λ − δ,
  or a different trace or largest multiplier for the switched oscillator at
  T = 1.
tags:
- mathematics
- complex-systems
date: '2026-10-19'
line: formal-apparatus
grounds:
- LIT-929
summary: >-
  The case [THEORY-724](../theory.d/THEORY-724.md)'s source asserts and does not show. If A(t)
  has first Lyapunov exponent λ > 0, the propagator of A(t) − δI is
  e^(−δt)Φ(t), so its exponent is exactly λ − δ, while every eigenvalue of
  every A(t) moves left by δ. Applied to the undamped oscillator switching
  ω between 0.5 and 3 every unit of time: λ = 0.1955, and with δ = 0.1 the
  system is stable at every instant, with eigenvalues −0.1 ± 3i and
  −0.1 ± 0.5i, and has exponent 0.0955.
---
<!-- inactive-ok-file: THEORY-325 — Proposed; the stochastic account, named as what this does not cover -->

# CLAIM-376: A linear system that is stable at every instant can have a positive Lyapunov exponent: shifting any operator with exponent λ > 0 by −δI lowers its exponent by exactly δ and makes every instantaneous operator stable, so for 0 < δ < λ the shifted system is stable at every instant and unstable

## The claim

Let du/dt = A(t)u have propagator Φ(t) and first Lyapunov exponent
λ = lim sup ln‖Φ(t)‖/t > 0, and suppose every A(t) has spectral abscissa
at most 0. For δ in (0, λ), the system du/dt = (A(t) − δI)u:

1. has exponent exactly λ − δ > 0, and
2. is stable at every instant, with spectral abscissa at most −δ.

## Proof

δI commutes with every A(t), so the propagator of A(t) − δI is
Φ_δ(t) = e^(−δt)Φ(t). Then ln‖Φ_δ(t)‖/t = ln‖Φ(t)‖/t − δ, and the lim sup
is λ − δ. The eigenvalues of A(t) − δI are those of A(t) shifted by −δ,
which proves (2).

## The switched oscillator

Take Farrell & Ioannou's oscillator ([LIT-929](../literature.d/LIT-929.md), eqs. 13–17) with γ = 0:
A_ω = [[0, 1], [−ω², 0]], ω switching between 0.5 and 3 every T = 1. Each
block integrates in closed form:

R_ω(T) = exp(A_ω T) = [[cos ωT, sin(ωT)/ω], [−ω sin ωT, cos ωT]].

The monodromy over one period, of length 2, is M = R_3(1)R_0.5(1). Its
determinant is 1 and its trace is −2.1548. Since |tr M| > 2, the multipliers
are real, with the largest equal to 1.4784, so λ = ln(1.4784)/2 = 0.1955.
Every A_ω is neutral, with eigenvalues ±iω. With δ = 0.1, the instantaneous
eigenvalues are −0.1 ± 3i and −0.1 ± 0.5i, and the exponent is 0.0955. The
numbers were computed from the closed form, and checked against a matrix
exponential of the shifted operators.

## What it does not say

- **That −δI is the paper's damping.** Farrell & Ioannou damp the velocity,
  with −2γ in the lower-right entry. The shift damps both coordinates. It
  is enough for the existence claim, and says nothing about the paper's
  damped curves.
- **Anything about random variation.** That is [THEORY-325](../theory.d/THEORY-325.md)'s, still Proposed.
- **That such a shifted operator is normal.** It inherits A(t)'s
  non-normality, as [THEORY-724](../theory.d/THEORY-724.md)'s bound requires.
