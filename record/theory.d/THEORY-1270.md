---
number: 1270
status: Active
formerly:
- THEORY-tmpshz26
title: 'Entropy production does not select which of several maintained steady states is the stable one: in the bistable Schlögl model the state the system occupies in the long run can carry either the higher or the lower deterministic entropy production rate, and the mean stochastic entropy production follows whichever state is more probable; in general the most dissipative attractor is the longest-lived only under special conditions, and lifetime tracks relaxation entropy only near detailed balance'
version: 1
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
source:
- LIT-1890
- LIT-1892
summary: >-
  Vellela & Qian (2009), [LIT-1890](../literature.d/LIT-1890.md) (§3.3, Fig. 6), read in
  [NOTE-1474](../notes.d/NOTE-1474.md), show the counterexample; Falasco & Esposito (2025),
  [LIT-1892](../literature.d/LIT-1892.md) (§§III.F, IV.H, VIII.B.6), read in [NOTE-1472](../notes.d/NOTE-1472.md), give the
  general account: minimum entropy production holds only near detailed
  balance with linear dynamics, and the two maximum principles hold only
  where relaxation and escape dissipations nearly coincide. Active as a
  negative result. It does not refute every extremum principle, only
  those that rank steady states by dissipation alone.
---
<!-- inactive-ok-file: THEORY-671 — Proposed; the account this one counts against, named as open -->

# THEORY-1270: Entropy production does not select which of several maintained steady states is the stable one: in the bistable Schlögl model the state the system occupies in the long run can carry either the higher or the lower deterministic entropy production rate, and the mean stochastic entropy production follows whichever state is more probable; in general the most dissipative attractor is the longest-lived only under special conditions, and lifetime tracks relaxation entropy only near detailed balance

## Source

Vellela & Qian (2009), [LIT-1890](../literature.d/LIT-1890.md), §3.3 (eqs. 3.12–3.27, Figs. 6–7) and
§5, read in [NOTE-1474](../notes.d/NOTE-1474.md). Falasco & Esposito (2025), [LIT-1892](../literature.d/LIT-1892.md), §III.F
(eqs. 101–102), §IV.H (eq. 160) and §VIII.B.6 (eqs. 290–292), read in
[NOTE-1472](../notes.d/NOTE-1472.md).

## What was actually shown

**The counterexample.** Each deterministic steady state xᵢ* of the
Schlögl model dissipates at ξᵢ = ΔG·J^ss_i ≥ 0 (eqs. 3.12–3.14). The
master equation has one mean entropy production rate,
ξ_CME = ΔG × (stationary cycle flux) (eq. 3.23), approximately V times the
ξᵢ of the two stable states weighted by their probabilities (eq. 3.27).
Sweeping b at a = 1 (Fig. 6), ξ_CME/V jumps from the lower branch ξ₋ to the
upper ξ₊ where the dominant state changes. So the state the system
occupies is sometimes the more and sometimes the less dissipative of the
two: "the more stable of the two stable equilibria can have either a high
or a low entropy production rate" (§3.3); "the entropy production rate
alone is unable to fully describe stability in the steady state" (§5).
The middle state's rate, always between the other two, is never
represented, so ξ_CME is always the maximum or the minimum of the three.

**The general account.** Minimum entropy production is recovered for
states close to detailed balance under linearized dynamics (Falasco &
Esposito eqs. 101–102), "only" there. Read as a statement about
lifetimes, eq. (160) is a maximum principle, "the attractor with the
largest life-time is the one with the largest relaxation (or smallest
instantonic) entropy production". It is exact at linear order and tight
only where the two path entropies nearly coincide, which in general
requires ⟨σ̇_γ⟩ → 0. The usual statement, that the attractor with the
largest steady dissipation lives longest, needs that dissipation to be
concentrated near the fixed points and the relaxation and instanton time
scales to match. "Some fine tuning or peculiar symmetries" (eqs.
290–292).

**What could have failed.** The stochastic rate might have been pinned
to one branch, or the more probable branch might always have been the
higher (or lower) one. In the sweep it is not.

## What this does not say

- **That dissipation is irrelevant to stability.** The escape rate is
  bracketed by path entropies ([THEORY-1264](THEORY-1264.md)); dissipation along
  trajectories constrains lifetimes. What fails is ranking states by
  their steady dissipation rate alone.
- **That Fig. 7's trend is a principle.** Vellela & Qian's observation
  that entropy production falls as the dominant state's barrier rises,
  offered as support for least dissipation as robustness, is one sweep of
  one parameter in one model.
- **That every maximum-entropy-production claim is refuted.** [THEORY-671](THEORY-671.md)
  states a selection principle for systems with many internal degrees of
  freedom. This is a one-variable counterexample plus a general argument
  that the principle needs special conditions; it does not show that the
  conditions never hold in the systems [THEORY-671](THEORY-671.md) is about.
