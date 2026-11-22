---
status: Proposed
promote_when: >-
  The published text (Physica A 322, 2003), or a second source, confirms
  eq. 2 (B(E) as the Laplace transform of f(β) for a parameter that
  fluctuates slowly against local equilibration), eq. 13 (a gamma f gives
  (1 + bE)^(−c), with c = 1/(q − 1)), eq. 21 (the shared small-variance
  correction e^(−β₀E)(1 + σ²E²/2)) and the p. 7 remark that the large-E
  behaviour depends on f. Not met by a check of which densities give power
  laws, which the title does not assert.
title: "Beck and Cohen define superstatistics as the Laplace transform of a slowly fluctuating inverse temperature's density, show that a gamma density gives Tsallis's q-exponential and that every superstatistics shares the same first correction at small variance, and leave the large-energy behaviour to the density"
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 from the delegated reading in NOTE-tmpj8ro5; quotations
    rechecked by the filer against the text.
tags:
- thermodynamics
- probabilistic-modeling
date: '2026-11-22'
source:
- LIT-2962
corroborates:
- CLAIM-769
bears_on:
- QUESTION-505
summary: >-
  Beck and Cohen (2003), [LIT-2962](../literature.d/LIT-2962.md), read in [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md). A letter:
  the mixture-of-exponentials construction in physics, with a gamma density
  giving the Tsallis form exactly and a universality result at small
  variance. It never says "power law"; which densities give one is the
  assistant's [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md). Proposed until the published text or a second
  source confirms it.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-769 CLAIM-tmpf9qt9 THEORY-2131 — Proposed or new; this account's reading and the entries it bears on -->

# THEORY-tmpczldx: Beck and Cohen define superstatistics as the Laplace transform of a slowly fluctuating inverse temperature's density, show that a gamma density gives Tsallis's q-exponential and that every superstatistics shares the same first correction at small variance, and leave the large-energy behaviour to the density

## Source

Beck and Cohen (2003), [LIT-2962](../literature.d/LIT-2962.md), read in [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md) from arXiv v2.

## What was actually shown

A system of cells, each in local equilibrium at an inverse temperature β
that fluctuates on a time scale "much larger than the relaxation time that
the single cells need to reach local equilibrium" (p. 2), has the long-run
Boltzmann factor B(E) = ∫ f(β) e^(−βE) dβ, "the Laplace transform of the
probability density f(β)" (p. 3). Closed forms: gamma f gives
(1 + bE)^(−c), Tsallis's q-exponential, with 2c "the effective number of
degrees of freedom contributing to the fluctuating β" (p. 5); uniform and
two-level f give sums or differences of exponentials. A general expansion
shows that "one always obtains the same result for small σ",
e^(−β₀E)(1 + ½σ²E²), so q = ⟨β²⟩/⟨β⟩² for any f (pp. 7–8). The
third-order coefficient g(q) tells the densities apart (p. 9). "In general
the large-E behavior is different for all superstatistics (it strongly
depends on the function f(β))" (p. 7).

## What this does not say

- Not that a spread of rates gives a power law: only the gamma case does
  among the closed forms, and a uniform f bounded away from zero keeps an
  exponential tail (eq. 5). The general condition is [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md)'s, the
  assistant's.
- Not what f(β) is for any system: it is "a priori unknown" (p. 3); the
  applications are cited, not shown.
- Not a population of entities: one system whose parameter fluctuates in
  space and time, seen over long times. The mathematics is the same
  mixture.

## Connections

[THEORY-2131](THEORY-2131.md) has the same integral as discounting under an unknown hazard,
with the same gamma and uniform results; [CLAIM-769](../claims.d/CLAIM-769.md) and [CLAIM-795](../claims.d/CLAIM-795.md) (item 4)
use it. It `corroborates` [CLAIM-769](../claims.d/CLAIM-769.md); [CLAIM-795](../claims.d/CLAIM-795.md)'s item 4 grounds on it.
