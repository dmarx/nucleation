---
number: 1453
status: Proposed
formerly:
- THEORY-tmpyfhtk
promote_when: >-
  An experiment shows the predicted design dependence: origami that differ
  only in staples per crossover column or in breakpoint stacking strength
  (for example three-domain against two-domain maximum-crossover designs,
  or monodisperse against disparate staple energies) show a nucleation
  signature, such as a lag in isothermal folding just below the melting
  temperature or ramp hysteresis, only in the high-stacking design, and the
  signature disappears a few degrees below the melting temperature; or an
  independent model, such as oxDNA or a kinetic domain-level model,
  reproduces the same presence and absence of the barrier and its control
  by stacking rather than hybridization strength.
title: 'Cumberworth, Frenkel and Reinhardt show, in Monte Carlo free-energy calculations of a domain-level lattice model of small planar DNA origami, that typical designs with two-domain staples and edge or single-domain staples assemble downhill with no nucleation barrier, that a maximum-crossover design with three-domain staples has a barrier of about 10 kBT, about 20 kBT at domain resolution, at its melting temperature which vanishes a few degrees below it, and that the presence and height of the barrier are set mainly by coaxial stacking between adjacent staples, not by hybridization strength'
version: 1
tags:
- natural-sciences
- complex-systems
- thermodynamics
date: '2026-11-05'
source:
- LIT-2134
summary: >-
  Cumberworth, Frenkel and Reinhardt (2022), [LIT-2134](../literature.d/LIT-2134.md), read in
  [NOTE-1638](../notes.d/NOTE-1638.md). Equilibrium simulation of four designs of at most 27
  domains with averaged energies. It does not say that a barrier changes
  folding times or yields, which are not simulated, nor that it causes the
  hysteresis seen in temperature ramps, which the authors explain but do not
  reproduce, nor that larger designs have no other barriers.
---

# THEORY-1453: Cumberworth, Frenkel and Reinhardt show, in Monte Carlo free-energy calculations of a domain-level lattice model of small planar DNA origami, that typical designs with two-domain staples and edge or single-domain staples assemble downhill with no nucleation barrier, that a maximum-crossover design with three-domain staples has a barrier of about 10 kBT, about 20 kBT at domain resolution, at its melting temperature which vanishes a few degrees below it, and that the presence and height of the barrier are set mainly by coaxial stacking between adjacent staples, not by hybridization strength

## Source

Cumberworth, Frenkel and Reinhardt (2022), [LIT-2134](../literature.d/LIT-2134.md); read in
[NOTE-1638](../notes.d/NOTE-1638.md).

## What was actually shown

- **Downhill designs** (Fig. 2a, b): systems S and D and the two-row
  design have no barrier along either order parameter at Tm.
- **A barrier** (Fig. 2b): three-row peaks at four of nine fully bound
  staples, about 10 kBT, and about 20 kBT with the domain-level peaks.
- **Temperature** (Fig. 3a): the barrier along fully bound staples
  "disappears after a few degrees" below the melting point.
- **Stacking, not hybridization** (Fig. 2c; SI Figs. S10–S12): halving
  stacking removes the three-row barrier; scaling it by 1.5 creates one in
  two-row; S and D stay downhill even with doubled stacking; hybridization
  energies 50% weaker or stronger have "almost no effect on the barrier
  height".
- **Could have come out otherwise**: every design could have had a barrier,
  or the barrier could have tracked hybridization strength or size; the
  calculations found neither.

## What this does not say

- That a barrier improves yield or speed: no kinetics are simulated, and
  the jamming argument is a conjecture.
- That ramp hysteresis comes from a nucleation barrier: it is explained,
  not reproduced, and Dannenberg et al.'s kinetic model accounts for it
  without one.
- That large, heterogeneous designs are barrier-free: the authors concede
  other kinds of barrier there.
- Anything about misbinding beyond averaged energies, or about free staples
  and aggregation, which the model excludes.
