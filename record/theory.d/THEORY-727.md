---
number: 727
status: Active
formerly:
- THEORY-tmpr7w9h
title: 'For a fixed linear operator in an inner-product norm, growth over time t is the top singular value of the propagator, which the eigenvalues bound only from below; it starts at the numerical abscissa, which can be positive when every mode decays; and the forced response is bounded by the condition number of the eigenvectors over the distance to the spectrum'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-323 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-323.yaml, batch 007, ADR-047).
    THEORY-323's promote_when asked for a standard reference proving the
    general statements, which the record does not hold. The owner ruled on
    2026-10-19 that a checked step-by-step re-derivation recorded in the
    decision file meets such a clause. Each statement here was checked by
    its textbook proof, given below, and both sources were read in full.
    The forced-variance clause, which LIT-931 cites and does not prove,
    stays in THEORY-323, which extends this one.
tags:
- mathematics
- complex-systems
date: '2026-10-19'
source:
- LIT-931
- LIT-932
summary: >-
  Farrell & Ioannou (1996), [LIT-931](../literature.d/LIT-931.md), read in [NOTE-831](../notes.d/NOTE-831.md), with Trefethen et al.
  (1993), [LIT-932](../literature.d/LIT-932.md), read in [NOTE-839](../notes.d/NOTE-839.md). For du/dt = Au with A fixed: a normal A
  grows as its spectral abscissa; in general the growth over t is
  σ_max(e^(At)), with the eigenvalues as a floor; the initial growth rate is
  the top eigenvalue of (A + A†)/2; and harmonic forcing is bounded by
  κ(E)/dist(iω, Λ(A)), with the ε-pseudospectrum marking where eigenvalues
  of A + Δ, ‖Δ‖ < ε, can go. All in a chosen norm. The white-noise variance
  result is [THEORY-323](THEORY-323.md)'s, still Proposed.
extended_by:
- THEORY-323
---
<!-- inactive-ok-file: THEORY-323 THEORY-325 — Proposed; the account this was split from and its companions, cited as open -->

# THEORY-727: For a fixed linear operator in an inner-product norm, growth over time t is the top singular value of the propagator, which the eigenvalues bound only from below; it starts at the numerical abscissa, which can be positive when every mode decays; and the forced response is bounded by the condition number of the eigenvectors over the distance to the spectrum

## Source

Farrell & Ioannou (1996), [LIT-931](../literature.d/LIT-931.md), read in full in [NOTE-831](../notes.d/NOTE-831.md): §2 (eqs.
1–10) and §3 (eqs. 11–19). Trefethen, Trefethen, Reddy & Driscoll (1993),
[LIT-932](../literature.d/LIT-932.md), read in full in [NOTE-839](../notes.d/NOTE-839.md): eqs. 5–13.

## What was actually shown

For du/dt = Au, with A fixed in time and growth measured in an
inner-product norm. Each statement is the source's, and each was checked by
its standard proof for the promotion audit.

1. **Normal operators follow their eigenvalues.** A normal A is unitarily
   diagonalizable, A = UΛU†, so ‖e^(At)‖ = ‖e^(Λt)‖ = e^(α(A)t), with α the
   spectral abscissa ([LIT-931](../literature.d/LIT-931.md), §2).
2. **Growth is a singular value.** The largest growth over time t is the
   operator norm ‖e^(At)‖ = σ_max(e^(At)), and the optimal perturbation is
   the top right singular vector, by the SVD ([LIT-931](../literature.d/LIT-931.md), eqs. 4–5).
3. **The eigenvalues are a floor.** σ_max(e^(At)) ≥ ρ(e^(At)) =
   max_i |e^(λ_i t)|, since the spectral radius never exceeds the norm
   (eq. 6).
4. **Initial growth is the numerical abscissa.** d/dt ‖e^(At)x‖² at t = 0
   is ⟨(A + A†)x, x⟩, so the initial growth rate of ‖e^(At)‖ is
   λ_max((A + A†)/2) (eq. 10). It can be positive when every eigenvalue is
   in the left half-plane. For A = [[−1, M], [0, −2]], the symmetric part
   [[−1, M/2], [M/2, −2]] has trace −3 and determinant 2 − M²/4, so its top
   eigenvalue is (−3 + √(1 + M²))/2, positive exactly when M > 2√2.
5. **Forced response and pseudospectra.** If A = EΛE⁻¹, then
   (iωI − A)⁻¹ = E(iωI − Λ)⁻¹E⁻¹, so ‖(iωI − A)⁻¹‖ ≤
   κ(E)/dist(iω, Λ(A)) ([LIT-931](../literature.d/LIT-931.md), eq. 19). The ε-pseudospectrum, the set of
   z with ‖(zI − A)⁻¹‖ > 1/ε, is exactly the set of eigenvalues of A + Δ
   with ‖Δ‖ < ε ([LIT-932](../literature.d/LIT-932.md), eq. 13). For a non-normal A it can reach far
   past the ε-neighbourhood of the spectrum, so large resonance can occur
   far from any eigenvalue ([LIT-932](../literature.d/LIT-932.md), eqs. 5–7).

The sources' examples show the sizes involved. A 2 × 2 operator with
eigenvalues −1 and −2 grows about eightfold before decaying. A damped Eady
model, stable in every mode, grows a hundredfold in energy over four days
([LIT-931](../literature.d/LIT-931.md), Figs. 4 and 8).

## What this does not say

- **Anything about white-noise variance.** That a non-normal stable system
  holds more forced variance than the sum of its pole contributions, with
  equality only when A is normal, is [THEORY-323](THEORY-323.md). The source cites it and
  does not prove it.
- **That non-normality belongs to the system.** It is relative to the norm,
  and a norm can always be found that makes A normal ([LIT-931](../literature.d/LIT-931.md), §2). The
  statements have content only once the norm is fixed on independent
  grounds, such as energy.
- **That the growth persists.** A stable autonomous system still decays at
  the rate of its spectral abscissa in the end.
- **Anything for time-varying or nonlinear systems.** Those are [THEORY-325](THEORY-325.md)
  and [THEORY-304](THEORY-304.md).
