---
number: 2197
status: Proposed
formerly:
- THEORY-tmpaojie
promote_when: >-
  The derivation is checked against Kosterlitz (1974), LIT-3059, or
  José, Kadanoff, Kirkpatrick and Nelson (1977), read and filed,
  confirming what the title says: spin-wave correlations r^(−k_BT/2πJ) at
  every low temperature, a flow to a line of fixed points with the vortex
  fugacity irrelevant below T_KT, and an essential singularity of the
  correlation length at T_KT.
title: '2D XY low-T phase is critical throughout'
statement: >-
  Drouin-Touchette's notes derive that the two-dimensional XY model's spin
  waves give correlations falling as r^(−k_BT/2πJ) at every low temperature,
  that below the Kosterlitz–Thouless temperature the vortex fugacity flows
  to zero on a line of fixed points, so the whole low-temperature phase has
  an infinite correlation length with nothing tuned, and that at the
  transition the correlation length diverges as an essential singularity,
  not a power
version: 1
tags:
- natural-sciences
- thermodynamics
date: '2026-11-22'
source:
- LIT-3055
bears_on:
- QUESTION-508
summary: >-
  Drouin-Touchette (2022), [LIT-3055](../literature.d/LIT-3055.md), skimmed in [NOTE-2295](../notes.d/NOTE-2295.md) as a
  stand-in for Kosterlitz and Thouless (1973), [LIT-2969](../literature.d/LIT-2969.md). Standard results,
  derived at a student level and credited to Kosterlitz (1974) and José et
  al. (1977). Grounds [CLAIM-841](../claims.d/CLAIM-841.md)'s XY row with Kosterlitz's lecture
  ([THEORY-2206](THEORY-2206.md)) ([ARG-198](../arguments.d/ARG-198.md)), and the BKT case of [CLAIM-862](../claims.d/CLAIM-862.md).
  Proposed until checked against the primary papers.
---
<!-- inactive-ok-file: NOTE-2295 THEORY-2206 ARG-198 CLAIM-862 — new or Skimmed; this reading, its companion and the entries it grounds -->
<!-- inactive-ok-file: LIT-2969 LIT-3059 — Unfetched or Deferred -->
<!-- inactive-ok-file: CLAIM-841 — Proposed -->

# THEORY-2197: 2D XY low-T phase is critical throughout

## Source

Drouin-Touchette (2022), "The Kosterlitz-Thouless phase transition: an
introduction for the intrepid student", arXiv 2207.13748, [LIT-3055](../literature.d/LIT-3055.md),
§§2–3, skimmed in [NOTE-2295](../notes.d/NOTE-2295.md).

## The account

Spin waves give g(r) ≈ (πr/a)^(−η(T)), η = k_BT/2πJ, so "at all
low-temperatures, the system is critical" (§2.2). A free vortex costs
∆F = (πJn² − 2k_BT) ln(L/a) (§2.3). The RG flows "terminate on a line of
fixed points at which y0 = 0", where "the fugacity becomes irrelevant"
(§3.3). Above T_KT, ξ ≈ a exp((π²/8b)√(T_KT/(T − T_KT))): the free energy
"only has an essential singularity" (§3.4).

## What it does not say

- That "critical" here means a tuned transition: it means ξ = ∞ through
  the phase.
- Which of these results the 1973 paper itself contains.
