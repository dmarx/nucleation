---
number: 1830
status: Active
formerly:
- THEORY-tmper33k
title: 'On Tu, a biochemical network at equilibrium has a steady state fixed by its free-energy landscape, so changing its rates cannot change where it sits; dissipation lets kinetics set the steady state, and functions such as proofreading, adaptation and synchronization need it, adaptation and synchronization only above a threshold; in a four-state model of adaptation the dissipation rate, speed and accuracy obey Ẇ = c₁V_a ln(c₂A_a) to leading order, and the author proposes, as a law for living systems, that dissipation is bounded below by a function of performance'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed Active, not Proposed, because the filer checked what the title
    asserts beyond the author's report. The four-state adaptation model
    was reimplemented and its exact steady state computed (NOTE-1904,
    "A check of the ESA relation"). At equilibrium the activity tracks the
    input; under strong driving it adapts. Dissipation and speed match the
    leading-order expressions within 5%, and the ESA ratio is 0.72–0.94
    for γ from 10² to 10⁴. The proposed law is reported as the author's
    proposal, not asserted.
tags:
- natural-sciences
- thermodynamics
- complex-systems
date: '2026-11-15'
source:
- LIT-2547
bears_on:
- QUESTION-452
summary: >-
  Tu (2026), [LIT-2547](../literature.d/LIT-2547.md), read in [NOTE-1904](../notes.d/NOTE-1904.md). The derivations are in
  small Markov networks: a three-state proofreading model, a four-state
  "magic square", and a mean-field model of coupled Poisson clocks. The
  sharp edges: the ESA relation is leading-order, and in the filer's
  check accuracy saturates at a residual set by the network's own
  parameters, past which more dissipation buys speed and no accuracy; and
  the proposed law, Ẇ ≥ F(P₁, P₂, …) with F unspecified, is a schema whose
  content lies only in its instances.
---
<!-- inactive-ok-file: THEORY-tmp9t69m — Proposed; the reading of Gingrich and colleagues, 2026-11-22 -->

# THEORY-1830: On Tu, a biochemical network at equilibrium has a steady state fixed by its free-energy landscape, so changing its rates cannot change where it sits; dissipation lets kinetics set the steady state, and functions such as proofreading, adaptation and synchronization need it, adaptation and synchronization only above a threshold; in a four-state model of adaptation the dissipation rate, speed and accuracy obey Ẇ = c₁V_a ln(c₂A_a) to leading order, and the author proposes, as a law for living systems, that dissipation is bounded below by a function of performance

## Source

Tu (2026), [LIT-2547](../literature.d/LIT-2547.md), read in full in [NOTE-1904](../notes.d/NOTE-1904.md).

## What was actually shown

- **Proofreading.** In a three-state model, error reduction below the
  equilibrium rate is bounded by the driving free energy,
  ηmin/η0 ≥ e^(−G0), and is impossible without it.
- **Adaptation.** In the four-state model, adaptation is impossible at
  equilibrium. It appears only for driving γ above a threshold
  γc ≈ ra/c. In its adaptive regime the ESA relation holds to leading
  order, which the filer reproduced numerically.
- **Synchronization.** In the coupled-clock model (from the author's
  2020 paper), synchronization needs exchange reactions that dissipate
  beyond what drives each clock, above a critical exchange frequency.
- **Dwell times.** An equilibrium system's dwell-time distributions are
  monotonically decreasing, so a peaked distribution implies driving.

Each result is a derivation in a model, any of which could have failed:
an equilibrium network might have adapted, or the price might have grown
in proportion to accuracy.

## What this does not say

- **That the proposed law has content as stated.** Ẇ ≥ F(P₁, P₂, …) with F
  unspecified holds trivially for F = 0. The review offers it as a
  proposal generalizing its instances.
- **That the ESA relation holds outside its regime,** or for adaptive
  networks other than this motif. In the filer's check it fails once
  accuracy reaches the residual left at infinite driving.
- **That any particular cell operates at the bound.** The review suggests
  living systems sit "near—though not exactly on" it, without data.
- **That this is the same bound as the thermodynamic uncertainty
  relation** ([THEORY-1268](THEORY-1268.md)), which prices the precision of a counted
  current as 1/ε², where the ESA relation prices adaptation accuracy as
  ln(1/ε).

## Note of 2026-11-22: Gingrich, Horowitz, Perunov and England, read

**A contrast**, no edge (LIT-2981, NOTE-tmpri2np, THEORY-tmp9t69m). The
uncertainty relation is now proved for every current of a Markov jump
network, pricing current precision as 1/ε²; Tu's relation prices
adaptation accuracy logarithmically. Different observables, so the proof
leaves the difference noted above as it was. Status unchanged.
