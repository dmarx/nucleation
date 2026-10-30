---
number: 304
status: Active
formerly:
- THEORY-tmp62hye
title: 'In plane Couette and Poiseuille flow, measured in the energy norm, the linearized operator is so far from normal that perturbations can grow transiently by O(R) and resonate by O(R²), and operator perturbations of size O(R⁻²) make it eigenvalue-unstable, at Reynolds numbers where eigenvalue analysis predicts stability'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-304.yaml, batch 013, ADR-047),
    the lower bounds behind the scalings (growth at least cR, resonance at
    least cR², a destabilizing perturbation of norm at most CR⁻²) are
    derived from the streamwise-independent scaling and filed apart as
    CLAIM-383, demonstrated and Active. That rules out the refuter the promote_when
    names, growth bounded independently of R. The leading-order
    scalings and their constants still rest on the source's computation
    alone, so this THEORY keeps its promote_when unchanged. The status stays
    Proposed.
- version: 3
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active under ADR-065, at the status review's
    ruling (the owner delegated these rulings). The old title read: "In
    plane Couette and Poiseuille flow the linearized operator is so far from
    normal that perturbations can grow transiently by O(R) and resonate by
    O(R²), and operator perturbations of size O(R⁻²) make it
    eigenvalue-unstable, at Reynolds numbers where eigenvalue analysis
    predicts stability". Non-normality is norm-relative and every figure is
    in the energy norm, so the norm is now in the title; the norm-free
    reading is asserted by no one (ADR-047 kind 3, this note only). The
    title claims no more than the computation read in full in NOTE-839
    measured, its lower bounds are CLAIM-383, and nothing in the record
    contradicts it. The old promote_when read: "An independent computation
    or review of the linearized plane Couette and Poiseuille operators, such
    as Reddy & Henningson (1993) or Schmid & Henningson's monograph, read
    here and reproducing the O(R) transient growth, O(R²) resonance and
    O(R⁻²) minimal destabilizing perturbation with constants near those of
    Table 1. It is refuted by a correct computation in the energy norm
    showing growth bounded independently of R. What cannot settle it:
    experiments on transition, which bear on the conjecture this account
    excludes, not on the linear scalings." Its demand for an independent
    computation of the same scalings moves to QUESTION-tmpiwx25; the
    decision of 2026-10-19 to keep this entry Proposed predates ADR-065.
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-10-14'
source:
- LIT-932
summary: >-
  Trefethen, Trefethen, Reddy & Driscoll (1993), [LIT-932](../literature.d/LIT-932.md), read in
  [NOTE-839](../notes.d/NOTE-839.md): computed scalings for the linearized shear flows,
  mostly credited to earlier work and unified through pseudospectra. That
  transition to turbulence happens by this linear growth plus nonlinear
  mixing is the paper's conjecture from a 2 × 2 model, and is not part of
  this account.
---
<!-- inactive-ok-file: CLAIM-186 — Proposed; the claim that cites this paper, open -->
<!-- inactive-ok-file: THEORY-323 — Proposed; the general account this case falls under -->

# THEORY-304: In plane Couette and Poiseuille flow, measured in the energy norm, the linearized operator is so far from normal that perturbations can grow transiently by O(R) and resonate by O(R²), and operator perturbations of size O(R⁻²) make it eigenvalue-unstable, at Reynolds numbers where eigenvalue analysis predicts stability

## Source

Trefethen, Trefethen, Reddy & Driscoll, "Hydrodynamic Stability Without
Eigenvalues", *Science* 261 (1993), [LIT-932](../literature.d/LIT-932.md), read in full in
[NOTE-839](../notes.d/NOTE-839.md): eqs. 5–13, Table 1, Figs. 2 and 4–9.

## What was actually shown

Computation on the linearized Navier–Stokes operator L about laminar
plane Couette and plane Poiseuille flow, Fourier-transformed in x and z
and discretized in y, with amplification measured in the energy norm.

- **The anomaly.** Eigenvalue analysis gives instability only above R =
  5772 for Poiseuille flow and never for Couette flow. Transition is
  observed near R = 1000 and R = 350.
- **Leading-order scalings as R → ∞ (Table 1).**
  - Transient growth sup_t ‖exp(−itL)‖: R/29.1 (Couette), R/71.5
    (Poiseuille), reached at t = O(R).
  - Maximum resonance over real frequencies: (R/8.12)² and (R/17.4)².
  - Minimal destabilizing operator perturbation ε_min, the inverse of the
    maximum resonance: O(R⁻²) (Fig. 8). At R = 5000 a perturbation of
    norm 1.2 × 10⁻⁵ makes Poiseuille flow eigenvalue-unstable.
  For a normal operator with the same spectrum the growth would be at
  most 1 and the resonance O(R).
- **The amplified structures are three-dimensional.** The maxima occur
  at streamwise wavenumber α = 0, or nearly, and spanwise β between 1.18
  and 2.04: streamwise vortices that become streaks. For two-dimensional
  perturbations, the traditional focus under Squire's theorem, "some
  amplification can still occur, but it is far weaker".
- **The three quantities are linked.** ‖L⁻¹‖ ≤ ∫‖exp(−itL)‖dt, within a
  factor of about 2 here, so the O(R²) resonance is O(R) growth over an
  O(R) time. The pseudospectra give a lower bound on transient growth
  that falls short by a factor of about 1.4.

The scalings could have come out bounded in R; they did not. Their lower
bounds, transient growth at least cR, resonance at least cR², and a
destabilizing perturbation of norm at most CR⁻², follow from the
streamwise-independent scaling alone. That derivation is [CLAIM-383](../claims.d/CLAIM-383.md),
demonstrated and Active since 2026-10-19. The constants, and the fact
that growth is no more than order R, are the computation's. The paper
credits the discovery of large transient growth to Gustavsson, Henningson
et al. and Butler & Farrell, and its foundation to Butler & Farrell and
Reddy & Henningson.

## What this does not say

- **It does not say this is how transition to turbulence happens.** The
  paper's last section opens "we speculate". From a 2 × 2 model with
  energy-neutral quadratic mixing, whose threshold amplitude scales as
  R⁻³, it conjectures that transition in eigenvalue-stable shear flows
  is "essentially linear" with threshold O(R^γ), γ < −1. It lists how
  the Navier–Stokes equations differ from the model. The conjecture is
  not filed here.
- **It does not say which mechanism operates in a given experiment.**
  Resonance to vibration, growth from inlet disturbances, and
  destabilization by imperfect geometry are offered as possible triggers
  for distinct experiments, as speculation.
- **It does not give operator perturbations a physical meaning.** The
  authors leave open whether they describe transition or are "a symptom
  of the nonnormality of the unperturbed problem".
- **It is not about other flows.** Pipe flow and boundary layers are
  named as cases where eigenvalue analysis fails, but are not computed.
- **The figures are in the energy norm.** Non-normality is
  norm-relative ([THEORY-323](THEORY-323.md)).

## Connections

No relations are declared.

- **[THEORY-323](THEORY-323.md).** The general account; this is its best-measured
  physical case.
- **[CLAIM-186](../claims.d/CLAIM-186.md).** Its note says shear flows "turn turbulent because a
  transient amplification hands the disturbance to nonlinear dynamics".
  This account holds the first half. The "because" is the conjecture this
  account excludes, and the claim should cite it as conjecture.
