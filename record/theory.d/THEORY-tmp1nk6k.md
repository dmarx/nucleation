---
status: Active
title: 'A chemostat is an emergent structure of a closed reaction network: when exchange reactions are fast and the reservoir species are abundant by a factor of order Omega, the closed network behaves to leading order as the open one, with its local detailed balance and dissipation, over a window that opens once exchange equilibrates and closes on a time of order Omega, after which a driven network relaxes to equilibrium; neither separation alone suffices'
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-10-31'
source:
- LIT-tmpgm18n
summary: >-
  Remlein, Esposito and Avanzini (2026), [LIT-tmpgm18n](../literature.d/LIT-tmpgm18n.md), read in
  [NOTE-tmp658wp](../notes.d/NOTE-tmp658wp.md): a multiscale expansion in the rate ratio ε and a WKB
  argument in the abundance ratio Ω, for arbitrary stoichiometry. The
  lifetime scaling was checked by integrating the paper's §IX network,
  T_δ = 0.00483 Ω against its fit 0.0048 Ω + 0.33. Active. It does not
  say that every driven closed network departs from open behaviour at
  T ~ Ω, only that it can from then on, nor anything about systems that
  are not chemical.
---
<!-- inactive-ok-file: CLAIM-478 THEORY-1052 — Proposed; the claim and the reading whose window this instance sharpens, cited as open -->

# THEORY-tmp1nk6k: A chemostat is an emergent structure of a closed reaction network: when exchange reactions are fast and the reservoir species are abundant by a factor of order Omega, the closed network behaves to leading order as the open one, with its local detailed balance and dissipation, over a window that opens once exchange equilibrates and closes on a time of order Omega, after which a driven network relaxes to equilibrium; neither separation alone suffices

## Source

Remlein, Esposito and Avanzini (2026), [LIT-tmpgm18n](../literature.d/LIT-tmpgm18n.md), §§V–IX and XI, eqs. 18,
31, 36–44, 49, 57 and Fig. 5, pp. 4–15 of arXiv 2604.14848v2; read in
[NOTE-tmp658wp](../notes.d/NOTE-tmp658wp.md).

## What was actually shown

**The regime.** Partition a closed network into internal species x,
would-be chemostatted species y, and reservoir species Y, with reactions
y ⇌ Y faster than the rest by 1/ε and Y more abundant than y by Ω. Taking
ε → 0 and then Ω → ∞, the master equation for the slow variables becomes
the open network's, with [y] fixed (eqs. 36–40). Its rates satisfy the
open network's local detailed balance (eq. 49), and its leading-order
dissipation equals the closed network's (eq. 57). With ε → 0 alone the slow
equation has the wrong rates and [y] still moves, so time-scale separation
is "necessary, but not sufficient" (p. 6). The two limits do not commute.

**The window.** The reservoir totals change by O(Ω) only after T = O(Ω) on
the slow clock (eq. 44). There are three time scales: exchange
equilibration, open-network dynamics, reservoir depletion. A network whose
emergent open form is detailed-balanced equilibrates within the window. A
driven one cannot, and on the ultra-slow scale the closed network
"eventually equilibrates" (p. 9).

**The check (mine).** For x ⇌ y₁, x ⇌ y₂ with fast y_i ⇌ Y_i, [Y₁] = 2Ω,
[Y₂] = Ω, a deterministic integration with ε = 10⁻⁴ gives the time at which
entropy production falls 1% below its open value as 0.00483 Ω − 0.27 over
Ω = 3 × 10³ to 10⁵. The paper's stochastic fit is 0.0048 Ω + 0.33. With x
slaved, the drive y₁ − y₂ decays as e^{−T/Ω} and a 1% fall in
(Δ/2) ln((3 + Δ)/(3 − Δ)) needs T/Ω = 0.00483.

**What could have failed.** The closed network's slow dynamics could have
converged to something other than the open network's, or its dissipation to
a different value. Or the departure time could have scaled otherwise than
linearly in Ω.

## What this does not say

- **That departure always happens at T ~ Ω.** It is the onset after which
  departure can happen; whether it does depends on topology (p. 9).
- **That the open description is wrong.** Within the window it is exact to
  leading order.
- **That maintenance is a property of the maintained system alone.** The
  window's upper end is set by the reservoir's capacity, which belongs to
  the environment. A maintained organization in the sense of [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md)
  is maintained relative to such a window.
- **That this is the only route to an effective constraint.** For
  [CLAIM-478](../claims.d/CLAIM-478.md) it is one mechanism among several, and it needs two
  separations, of rate and of abundance, rather than the one the claim
  names. Like the tracking result of [THEORY-1052](THEORY-1052.md), it has three time scales.
- **Anything outside dilute mass-action chemistry.** Buffers are the one
  laboratory instance the paper gives.
