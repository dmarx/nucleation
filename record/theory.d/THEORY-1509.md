---
number: 1509
status: Proposed
formerly:
- THEORY-tmpu2r6o
promote_when: >-
  The decay laws of eqs. 15, 25, 30, 33 and 35 rederived from the energy
  balance dE/dt = −δF with the Benjamin–Ono soliton's energy
  E_s = πβA/α, or reproduced in a direct simulation of the damped
  Benjamin–Ono equation for one loss type over the stated validity window;
  the trailing shelf shown to appear under a loss that does not conserve
  mass and not under one that does; and, for "integrable wave equation"
  beyond Benjamin–Ono, the corresponding KdV laws found in a read source
  (such as Ott and Sudan 1970) rather than only cited.
title: 'A soliton of an integrable wave equation under weak loss does not break up but shrinks along its family of shapes at a rate set by energy balance, exponentially under linear damping and algebraically under viscous, Landau, boundary-layer and friction losses, while a shelf of non-soliton wave forms behind it wherever the loss does not conserve mass'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    CLAIM-600 moved into the SYNTHESIS scheme as SYNTHESIS-010 (ADR-077),
    so `corroborates` names the synthesis. No other change.
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-06'
source:
- LIT-2198
corroborates:
- SYNTHESIS-010
summary: >-
  Grimshaw, Smyth & Stepanyants (2018), [LIT-2198](../literature.d/LIT-2198.md), read in full in
  [NOTE-1687](../notes.d/NOTE-1687.md), for the Benjamin–Ono equation with six kinds of weak loss,
  by first-order adiabatic theory checked against direct numerics. Filed as
  the read neighbour of Kivshar & Malomed (1989), whose central method for
  damped solitons it carries in one equation. The KdV laws, which make the
  title's "integrable wave equation" more than one case, are quoted in the
  paper from earlier work, not derived, and so are not shown here. It says
  nothing of NLS, of gain or supply, or of strong loss. The wording is the
  reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-2210 — Unavailable or Proposed; cited from the reading of Grimshaw, Smyth & Stepanyants (2018) as open -->

# THEORY-1509: A soliton of an integrable wave equation under weak loss does not break up but shrinks along its family of shapes at a rate set by energy balance, exponentially under linear damping and algebraically under viscous, Landau, boundary-layer and friction losses, while a shelf of non-soliton wave forms behind it wherever the loss does not conserve mass

## Source

Grimshaw, Smyth & Stepanyants (2018), [LIT-2198](../literature.d/LIT-2198.md); read in [NOTE-1687](../notes.d/NOTE-1687.md).
The read neighbour of Kivshar & Malomed (1989), [LIT-2210](../literature.d/LIT-2210.md), unread.

## What was actually shown

For the Benjamin–Ono equation u_t + αuu_x + (β/π)∂²/∂x² P∫u(ξ, t)/(ξ − x) dξ + δD[u] = 0 (eq. 4), with its
soliton A/(1 + (x − Vt)²/Δ²), by first-order adiabatic theory (an energy
balance, the condition for removing secular terms) checked against direct
numerical solution (§8, Table):

| Loss | Decay law | τ | Eq. |
|---|---|---|---|
| Rayleigh (linear damping) | A0 e^(−t/τ) | 1/2δ | 15 |
| Reynolds (viscous) | A0/√(1 + t/τ) | 8β²/(δα²A0²) | 25 |
| Landau damping | A0/(1 + t/τ) | 4β/(δαA0) | 30 |
| Laminar boundary layer | A0/(1 + t/τ)² | (from the Table; garbled in extraction) | 33 |
| Chezy friction | A0/(1 + t/τ) | 2/(3δA0) | 35 |
| Radiative (large-scale dispersion) | A0(1 − t/τ) | αA0/(8πβγ) | 43 |

- Under linear damping the soliton's amplitude falls twice as fast as a
  linear wave's, which "decays two times slower" (§2).
- Under Landau damping the decaying soliton is an exact solution, and with
  mass conserved the adiabatic theory "is valid for all time" (§4).
- Under Rayleigh damping, with mass not conserved, a trailing wave is
  required, and the first-order theory fails near t/τ ≈ 3.1 (δ = 10⁻³) or
  4.3 (δ = 10⁻⁴) (§2); Chezy friction leaves a constant shelf (§6).
- The radiative law ends in finite time, but numerically the soliton
  "transforms into an envelope soliton" (§7).
- **KdV, quoted, not derived** (§§4, 5, 7): Landau A0(1 + t/τ)^−2, boundary
  layer A0(1 + t/τ)^−4, radiative A0(1 − t/τ)², each cited to earlier
  work.

## What this does not say

- That the laws hold for any integrable equation beyond BO: KdV is by
  citation only, and NLS is not treated.
- That the soliton never breaks up under strong loss: the theory is first
  order in a small loss.
- Anything about gain, pumping or a supplied balance, so nothing about the
  thresholds or hysteresis of [CLAIM-604](../claims.d/CLAIM-604.md).
- That the shrinking soliton persists: in every case but the sign-reversed
  radiative one it runs down. Its long life under algebraic loss is slow
  decay, which is what makes it bear on [CLAIM-600](../claims.d/CLAIM-600.md)'s warning that slow
  reversion can mimic persistence.

## Note of 2026-11-06: what holds it back

The laws are derived here for the Benjamin–Ono equation alone; the KdV laws
that make "integrable wave equation" more than one case are quoted from
earlier work (Ott and Sudan 1970 among them) that the record has not read,
and no step-by-step re-derivation of eqs. 15–35 from the energy balance,
checked by a second reader, is recorded.
