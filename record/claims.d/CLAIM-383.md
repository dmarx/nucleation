---
number: 383
status: Active
formerly:
- CLAIM-tmpyj9zk
title: "In plane Couette and plane Poiseuille flow, measured in the energy norm, the linearized operator about the laminar profile has transient growth at least cR and resolvent norm at least cR² with c independent of R, so wherever it is eigenvalue-stable a perturbation of norm at most CR⁻² makes it eigenvalue-unstable"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-304 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-304.yaml, batch 013, ADR-047).
    The lower bounds follow from the streamwise-independent (lift-up)
    scaling, the record's own derivation, so this is a CLAIM (ADR-032).
    THEORY-304 keeps the leading-order scalings and their constants, from
    the source's computation, Proposed, and cites this claim for the lower
    bounds.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a cross-stream field (v, w) at
  streamwise wavenumber zero whose evolution depends on the streamwise
  velocity or on the base profile, or a rescaling under which the
  streamwise response is not R times an R-independent field.
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-10-19'
line:
- formal-apparatus
summary: >-
  [THEORY-304](../theory.d/THEORY-304.md)'s scalings as lower bounds, derived. At streamwise wavenumber
  zero, the cross-stream velocities obey an R-independent Stokes problem
  in the time t/R. They force the streamwise velocity through −U′v, so
  the streamwise response is R times an R-independent field. In the energy
  norm this gives transient growth at least cR, and in the steady forced
  problem a resolvent norm at least cR². Through pseudospectra, a
  perturbation of norm O(R⁻²) then moves an eigenvalue into the unstable
  half-plane wherever the flow is eigenvalue-stable. The sharp constants,
  and that the growth is no more than order R, come from the computation
  and are not here.
---
<!-- inactive-ok-file: THEORY-323 — Proposed; the account this bound was split from and that cites it, and the general non-normality account, cited as open -->

# CLAIM-383: In plane Couette and plane Poiseuille flow, measured in the energy norm, the linearized operator about the laminar profile has transient growth at least cR and resolvent norm at least cR² with c independent of R, so wherever it is eigenvalue-stable a perturbation of norm at most CR⁻² makes it eigenvalue-unstable

## The claim

Let U(y) be the laminar profile between no-slip walls, U′ = 1 for plane
Couette and U′ = −2y for plane Poiseuille flow, and let L be the
linearized Navier–Stokes operator about it, with perturbations measured
in the kinetic-energy norm. There are constants c, C > 0, independent of
the Reynolds number R, such that:

1. sup_t ‖e^{tL}‖ ≥ cR;
2. ‖L⁻¹‖ ≥ cR², so the maximum resonance over real frequencies is at
   least cR²;
3. at any R where L is eigenvalue-stable, some perturbation E with
   ‖E‖ ≤ CR⁻² gives L + E an eigenvalue with positive real part.

## Derivation

1. **Decoupling.** At streamwise wavenumber zero the linearized equations
   are ∂_t u + U′v = R⁻¹∇²u for the streamwise velocity, and
   ∂_t(v, w) = −∇p + R⁻¹∇²(v, w) with ∂_y v + ∂_z w = 0 for the
   cross-stream velocities. The (v, w) problem involves neither u nor U.
2. **Rescaling.** Put t = Rτ and p = p̂/R. Then (v, w) as a function of τ
   solves a Stokes problem with no R in it. The streamwise velocity solves
   ∂_τ u = ∇²u − RU′v, so with u(0) = 0, u = Rû(τ) with û independent of R.
3. **Growth.** In the energy norm, ‖q(Rτ)‖² = R²‖û(τ)‖² + ‖(v, w)(τ)‖².
   Take ‖(v, w)(0)‖ = 1, with v(0) nonzero where U′ ≠ 0. Then
   ∂_τ û(0) = −U′v(0) ≠ 0, so ‖û(τ*)‖ = c > 0 for some τ*, and
   ‖e^{tL}‖ ≥ cR at t = Rτ*.
4. **Resonance.** Take steady forcing f = (0, f_v, f_w). Then (v, w) = RSf,
   with S the R-independent steady Stokes solve, and
   u = RΔ⁻¹(U′v) = R²Δ⁻¹U′Sf. For an f with Δ⁻¹U′Sf ≠ 0, ‖L⁻¹f‖ ≥ cR²‖f‖.
5. **Destabilization.** For a closed operator, z is an eigenvalue of L + E
   for some E with ‖E‖ ≤ 1/‖(z − L)⁻¹‖. This is the pseudospectral
   characterization, used here, as in [LIT-932](../literature.d/LIT-932.md), for the discretized
   operator. The resolvent is continuous in z, so ‖(δ − L)⁻¹‖ ≥ cR²/2 for
   small δ > 0. Some ‖E‖ ≤ 2/(cR²) then puts an eigenvalue at δ.

## What it does not say

- **That the growth is of order R and no more, or what the constants
  are.** Table 1 of [LIT-932](../literature.d/LIT-932.md), R/29.1, R/71.5, (R/8.12)² and (R/17.4)²,
  comes from computation. That is [THEORY-304](../theory.d/THEORY-304.md)'s, Proposed.
- **Where the flows are eigenvalue-stable.** All R for Couette flow and
  R < 5772 for Poiseuille flow is the source's statement. The third bound
  is stated conditionally on it.
- **Anything about transition.** That transition happens through this
  growth plus nonlinear mixing is [LIT-932](../literature.d/LIT-932.md)'s conjecture, and is not filed.
- **Anything in other norms.** Non-normality is norm-relative
  ([THEORY-323](../theory.d/THEORY-323.md)).
