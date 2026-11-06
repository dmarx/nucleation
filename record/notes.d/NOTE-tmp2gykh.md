---
status: Read
paper: 'LIT-tmpfpeor'
title: 'Grimshaw, Smyth and Stepanyants — Decay of Benjamin–Ono solitons under dissipation'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Read in full on 2026-11-06 from arXiv:1801.09088v1 (27 January 2018),
    the preprint "submitted to Elsevier", from arxiv.org, text by
    pdftotext. Read: §§1–8, the summary table and the appendix deriving the
    extended NLS equation. Not compared with the published version in
    Wave Motion 78. Equations are taken from the extracted text; roots and
    fractions are partly garbled there and were restored from the layout
    where noted. Read as a stand-in for Kivshar & Malomed (1989),
    LIT-tmpzah9i.
date: '2026-11-06'
summary: >-
  A weakly damped Benjamin–Ono soliton stays a soliton whose amplitude
  slides down its one-parameter family at a rate set by an energy balance:
  exponentially under linear damping, twice as fast as a linear wave;
  algebraically under viscous, Landau, boundary-layer and Chezy losses; and
  to zero in a finite time under radiative loss, after which it becomes an
  envelope soliton. Where mass is not conserved a trailing shelf forms and
  the adiabatic theory eventually fails. Asymptotics checked against
  numerics; KdV laws quoted, not derived.
---
<!-- inactive-ok-file: LIT-tmpzah9i LIT-tmpfx0lb LIT-1642 THEORY-tmpu2r6o CLAIM-597 CLAIM-600 CLAIM-604 TERM-088 THEORY-072 — Unavailable, Unfetched or Proposed; cited from the reading of Grimshaw, Smyth & Stepanyants (2018) as open -->

# NOTE-tmp2gykh: Grimshaw, Smyth and Stepanyants — Decay of Benjamin–Ono solitons under dissipation

## Contribution

The Benjamin–Ono (BO) equation is integrable, like KdV; its algebraic
soliton u = A/(1 + (x − Vt)²/Δ²), with V = αA/4 and Δ = 4β/αA, is a
one-parameter family. The paper adds a weak loss δD[u] of six kinds and
gives, for each, how the soliton decays, with the time over which the
first-order theory holds and a check by direct numerical solution.

## Key insight

A soliton under weak loss does not break up. It stays on its family and
only its parameter A drifts, at a rate set by the energy the loss removes;
what the loss does to mass decides whether anything else is left behind.

## Assumptions

- Weak loss, δ or γ small; one soliton as the initial condition; one space
  dimension.
- The loss is a linear spectral operator (−ik)^m with m = 0 (Rayleigh),
  1/2 (laminar boundary layer), 1 (Landau, as |k|) or 2 (Reynolds); or a
  nonlinear |u|u friction (Chezy); or a large-scale dispersion term γ
  (§7).
- First-order adiabatic theory: energy lost to the shelf is neglected at
  that order.
- Numerics at α = 2, β = 1, δ from 10⁻⁴ to 0.1, γ from 10⁻⁶ to 10⁻⁴.

## Key results

- **Identity without loss** (§1): solitary waves "restore their parameters
  (amplitude, shape etc.) after collisions with each other, so that they
  are termed solitons [33], the only relic of the interaction being a phase
  shift. They are also stable under arbitrary localised perturbations."
- **The adiabatic picture** (§1): "the basic structure of the solitary wave
  remains the same, but its primary parameter A, which determines its
  amplitude, speed and width, is no longer a constant, but is a slowly
  varying function of time". The theory "in essence reduces to an energy
  balance equation", dE/dt = −δF (eq. 9), which in multiple scales is "the
  condition for the elimination of secular terms". The soliton's energy is
  E_s = πβA/α (eq. 14, garbled in extraction, restored from the layout).
- **Mass** (§1): for m > 0 solutions conserve mass, for m = 0 not; since the
  soliton's mass "does not depend on its amplitude", under Rayleigh damping
  "the solution u(x, t) cannot be just a BO soliton, but must contain a
  non-solitonic part (a trailing wave)."
- **Rayleigh** (§2, eq. 15): A0 e^(−t/τ), τ = 1/2δ; the linear wave "decays
  two times slower", with τ = 1/δ, because the width grows as the amplitude
  falls. Validity to t/τ ≈ 3.1 (δ = 10⁻³) and 4.3 (δ = 10⁻⁴) (eq. 16); then
  "the tail generated behind the soliton gradually accumulates" energy and
  eq. 15 "ceases to be valid" (Fig. 2).
- **Reynolds** (§3, eq. 25): A0/√(1 + t/τ), τ = 8β²/(δα²A0²); agreement "very
  good, even for a relatively large dissipation coefficient", δ = 0.1.
- **Landau** (§4, eq. 30): A0/(1 + t/τ), τ = 4β/(δαA0); the decaying soliton
  "can be an exact solution", "a nice example of an exact non-stationary
  solution in the form of a decaying soliton"; with mass conserved "no
  trailing shelf can be formed at leading order" and the theory "is valid
  for all time in the case of Landau damping". For KdV, by citation of Ott
  and Sudan, "the amplitude decay due to Landau damping is more rapid",
  A0(1 + t/τ)^−2.
- **Laminar boundary layer** (§5, eq. 33): A0/(1 + t/τ)²; for KdV, by
  citation, A0(1 + t/τ)^−4.
- **Chezy friction** (§6, eq. 35): A0/(1 + t/τ), τ = 2/(3δA0); a constant
  shelf, "independent of the solitary wave amplitude" (eq. 37).
- **Radiative loss** (§7, eq. 43): A0(1 − t/τ), a "terminal decay" in which
  the soliton "completely vanishes in the extinction time" τ; for KdV, by
  citation, the soliton vanishes "in accordance with the quadratic law"
  A0(1 − t/τ)². "The soliton is accompanied by the radiation of a large
  scale trailing wave." But "in reality it does not completely disappear,
  but transforms into an envelope soliton" (eq. 61). With γ of the other
  sign, "the initial BO soliton does not decay, but gradually evolves into
  another soliton of a higher amplitude and zero mean value."
- **Summary** (§8, Table): "Good agreement between the theory and
  numerical solutions was found when the dissipative coefficients were
  sufficiently small."

## Concepts

Adiabatic soliton decay; energy balance as the secularity condition; mass
balance and the trailing shelf; the validity window of first-order theory;
terminal (finite-time) radiative decay; transformation into a different
localized structure.

## Connections

- **For Kivshar & Malomed (1989)**, [LIT-tmpzah9i](../literature.d/LIT-tmpzah9i.md), unread: it restates the
  review's central method, adiabatic perturbation theory by energy balance,
  and its central qualitative result for damping, that a weakly damped
  soliton shrinks along its family rather than breaking up, for BO and,
  by citation, KdV. It does not restate the review's NLS results under
  damping or gain, kink dynamics, perturbed collisions or radiation
  calculations, and does not cite the review.
- **Zabusky & Kruskal (1965)**, [LIT-tmpfx0lb](../literature.d/LIT-tmpfx0lb.md), unread: the collision property
  quoted in §1 is the one they named.
- **Dissipative solitons**: nothing here on gain or supply. For that route,
  Herr et al. (2014) and Grelu & Akhmediev (2012), filed in the same batch,
  and [LIT-1642](../literature.d/LIT-1642.md) (Knobloch 2015, Unfetched).
- Filed from it: [THEORY-tmpu2r6o](../theory.d/THEORY-tmpu2r6o.md).

## Bearing on the record

- **[TERM-088](../terms.d/TERM-088.md) (individuation)**: supports the dynamical sense with a sharp
  case. Under loss the individual persists as one member of its family
  with drifting parameters; its identity is the family, not a fixed shape.
- **[CLAIM-604](../claims.d/CLAIM-604.md)**: a contrast case. Damped solitons show no collapse threshold
  and no hysteresis; amplitude falls smoothly, and even the finite-time
  radiative extinction is continuous. Consistent with the claim's scope,
  which is upkeep drawn in proportion to the intact state.
- **[CLAIM-597](../claims.d/CLAIM-597.md)**: a parallel only for linear damping, A0 e^(−t/τ); under the
  other losses decay is algebraic, slower than exponential. A soliton's
  parts are not replaced, so the claim's model does not apply directly.
- **[CLAIM-600](../claims.d/CLAIM-600.md)**: supports its warning that slow reversion can mimic
  persistence. Under viscosity the amplitude falls only as
  (1 + t/τ)^(−1/2), and under Landau damping the shape is kept exactly
  while the soliton runs down: intact shape is not evidence of permanence.
- **[CLAIM-516](../claims.d/CLAIM-516.md)**: no conflict. A lossless soliton has no turnover and falls
  outside the claim's hypothesis; with loss and nothing produced, it
  decays, as the claim would predict.
- **[THEORY-072](../theory.d/THEORY-072.md), [QUESTION-085](../questions.d/QUESTION-085.md)**: a lossless soliton is neither flame nor
  organism; it is held by an internal balance, not a flow, and decays when
  any loss is added. A candidate rung below "dissipative, externally held".
- **[QUESTION-399](../questions.d/QUESTION-399.md)**: a structure persists here without ever being
  self-maintaining; persistence and self-maintenance come apart.

## Limitations

One integrable equation, BO; the KdV laws are quoted from the literature,
not re-derived; no NLS; no gain, pump or supply; one dimension; long-time,
non-adiabatic fate studied only for the radiative case. Theory and
numerics, no experiment.
