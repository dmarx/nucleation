---
number: 1506
status: Proposed
formerly:
- THEORY-tmplxt7t
promote_when: >-
  An independent simulation of the same spherically symmetric double-well
  model reproduces the four things the title asserts: an existence window in
  initial radius with its lower end near the inflection-point and plateau
  conditions; a plateau energy and radius that do not depend on the initial
  radius; plateau lifetimes of order 10^3 m^-1 against order 10 m^-1 in the
  linear theory; and an abrupt end once the core amplitude has fallen below
  a minimum. Fodor's review (LIT-2197, §2.6.4) reports an independent
  code reproducing the Gaussian case (a lifetime near t ≈ 5800 for one
  initial radius, ending in about 25 oscillations); whether that, which
  covers one radius rather than the window, suffices is the owner's call.
  Nothing about nonspherical perturbations, the upper radius bound or
  permanence is asked.
title: 'In a spherically symmetric real scalar field with a double-well potential in 3+1 dimensions, subcritical bubbles with energy above a plateau value, core field beyond the inflection point and initial radius in a window shed part of their energy and settle into oscillons of nearly constant energy and radius whatever their initial radius, which radiate almost nothing for 10^3 to 10^4 m^-1, against about 5 to 10 m^-1 in the linear theory, and then decay quickly once slow radiation has lowered the core amplitude below the value at which its fluctuations stop being unstable; no topological invariant or conserved charge protects them'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-06'
source:
- LIT-2200
summary: >-
  Copeland, Gleiser & Müller (1995), [LIT-2200](../literature.d/LIT-2200.md), read in full in
  [NOTE-1699](../notes.d/NOTE-1699.md). Shown by numerical simulation, with a one-degree-of-freedom
  Gaussian ansatz explaining the lower radius bound and the end; spherical
  symmetry throughout, stability tested only against radial perturbations.
  It does not explain the upper radius bound, give an analytic lifetime, or
  define the plateau's endpoints formally. The wording of the title is the
  reader's condensation of the paper's §§III–IV and VII.
---

# THEORY-1506: In a spherically symmetric real scalar field with a double-well potential in 3+1 dimensions, subcritical bubbles with energy above a plateau value, core field beyond the inflection point and initial radius in a window shed part of their energy and settle into oscillons of nearly constant energy and radius whatever their initial radius, which radiate almost nothing for 10^3 to 10^4 m^-1, against about 5 to 10 m^-1 in the linear theory, and then decay quickly once slow radiation has lowered the core amplitude below the value at which its fluctuations stop being unstable; no topological invariant or conserved charge protects them

## Source

Copeland, Gleiser & Müller (1995), [LIT-2200](../literature.d/LIT-2200.md); read in [NOTE-1699](../notes.d/NOTE-1699.md).

## What was actually shown

- **Simulation (§III, §V).** Gaussian and tanh bubbles at rest, evolved with
  an outgoing grid edge so radiation does not return, energy conserved to
  one part in 10^3 or better. For a symmetric potential, Gaussian bubbles
  with R0 between about 2.4 and 4.5 enter an oscillon stage with energy near
  43 m/λ "regardless of their initial radius" and effective radius 2.8–3.0;
  peak lifetime about 7.4 × 10^3 m^-1. In asymmetric potentials lifetimes
  grow as the oscillon nears the critical bubble. These could have come out
  otherwise: the bubbles outside the window do disperse quickly, as in the
  linear theory.
- **Conditions (§III).** No oscillon below the plateau energy, and none if
  the core value lies short of the inflection point; stated as
  "sufficient conditions".
- **Ansatz (§IV).** The curvature of the effective potential for the core
  amplitude is negative only for R > 2.42, matching the simulated lower
  bound "independent of the initial amplitude"; below a radius-dependent
  core amplitude the oscillon "slips into the linear regime and quickly
  decays", compared with the last-oscillation amplitudes in Table 1.
- **No protection (§I).** The model is one real scalar, with neither the
  topological conservation laws of defects nor the conserved charge of
  nontopological solitons.

## What this does not say

- That oscillons are stable to nonspherical perturbations: "we only
  investigated stability to radial perturbations" (§VII).
- Why there is an upper bound on the initial radius; that is open
  ("Work on the fourth question is in progress").
- How long an oscillon lives in closed form: there is no analytic lifetime,
  and the lifetimes are read off an energy plateau in the figures without a
  stated rule for its start and end.
- That oscillons are permanent, or that fine-tuned ones are; that is a later
  and unresolved question (Fodor 2019; Gleiser & Krackow 2019).
- Anything about coupled fields, plasma or noise, which §VI names as open,
  or about cosmology beyond the order-of-magnitude speculation of §VI.
