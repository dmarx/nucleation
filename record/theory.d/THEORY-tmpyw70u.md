---
status: Active
title: "Near equilibrium, steady states minimise entropy production and every fluctuation decays; far from it, the excess entropy production has no fixed sign, so a fluctuation can grow past an instability of the thermodynamic branch into a structure held up only by flows across the boundary, and thermodynamics supplies only a sufficient condition for such a state's stability, not a principle selecting which structure appears"
version: 1
tags:
- complex-systems
- thermodynamics
date: '2026-10-16'
source:
- LIT-516
- LIT-527
summary: >-
  Prigogine (1977), [LIT-516](../literature.d/LIT-516.md), read in full in [NOTE-424](../notes.d/NOTE-424.md), with Cross &
  Hohenberg (1993), [LIT-527](../literature.d/LIT-527.md), skimmed in [NOTE-418](../notes.d/NOTE-418.md). Minimum entropy
  production holds only for steady states in the strictly linear regime
  with constant coefficients. Beyond it, non-negative excess entropy
  production suffices for stability; its failure is not shown to give
  instability. Which structure appears is left to kinetics, boundaries and
  fluctuations. Cross and Hohenberg find no global minimisation principle
  beyond a perturbative one near threshold, and quote Glansdorff and
  Prigogine conceding that "the search for a universal kinetic potential
  has proved to be unsuccessful".
---
<!-- inactive-ok-file: NOTE-418 — Skimmed; the second source is a skim, and the account is stated from the sections it read -->
<!-- inactive-ok-file: THEORY-072 THEORY-tmp1lcfx THEORY-tmph2xbv THEORY-tmpxjvy1 — Proposed; candidate selection principles and a neighbouring account named for context, nothing here rests on their being settled -->

# THEORY-tmpyw70u: Near equilibrium, steady states minimise entropy production and every fluctuation decays; far from it, the excess entropy production has no fixed sign, so a fluctuation can grow past an instability of the thermodynamic branch into a structure held up only by flows across the boundary, and thermodynamics supplies only a sufficient condition for such a state's stability, not a principle selecting which structure appears

## Source

Prigogine (1977), [LIT-516](../literature.d/LIT-516.md), Nobel lecture "Time, Structure and
Fluctuations", read in full in [NOTE-424](../notes.d/NOTE-424.md). Cross & Hohenberg (1993),
[LIT-527](../literature.d/LIT-527.md), *Reviews of Modern Physics* 65:851–1112, skimmed in [NOTE-418](../notes.d/NOTE-418.md)
(about 30 of 262 pages, chosen for this question). The lecture states the
theorems and cites their proofs; it does not prove them.

## What was actually shown

**Near equilibrium (§§2–3 of the lecture).** With local equilibrium and
linear laws J = LX with Onsager symmetry, "for steady states sufficiently
close to equilibrium entropy production reaches its minimum" (p. 266).
That needs "even more restrictive conditions" than linearity: constant
coefficients. The second-order excess entropy δ²S is negative and its time
derivative is the entropy production, so δ²S is a Lyapounov function and
"ensures the damping of all fluctuations".

**Far from equilibrium (p. 269).** Around a non-equilibrium steady state
½ ∂δ²S/∂t = Σ δJ_ρ δX_ρ, the excess entropy production, which "has
generally not a well-defined sign". If it stays non-negative, the state is
stable. That is sufficient; its violation is not shown to imply
instability.

**Dissipative structures.** Beyond an instability of the branch continuous
with equilibrium, a new state can appear: in Bénard convection, "a giant
fluctuation stabilized by exchanges of energy with the outside world"
(p. 267). The Brusselator, with its inputs held constant, has steady state
X₀ = A, Y₀ = B/A, unstable for B > 1 + A² (4.4), beyond which there is a
limit cycle; with diffusion, stationary patterns (the "Turing
bifurcation"). Autocatalytic steps are necessary but not sufficient for
the chemical case (p. 271). Which branch is taken at a bifurcation depends
on which fluctuation happened.

**The review's verdict ([LIT-527](../literature.d/LIT-527.md), §XIII).** In general "no such free energy
(or other so-called Lyapunov potential) can be defined for nonequilibrium
systems, though there are notable exceptions" (p. 857). "There is no
evidence for the existence of any global minimization principles
controlling the structure, except as a perturbative statement near
threshold" (p. 1080). A closed chemical system "ultimately must come to
equilibrium", so non-equilibrium structure is a transient or a response to
"external chemical pumping" (p. 865).

**What could have come out otherwise.** A general extremum principle for
non-equilibrium steady states could have been found. As of 1993 none had
produced physical results on pattern formation, the maximum-entropy
formalism included.

## What this does not say

- **That minimum entropy production governs dissipative structures.** The
  lecture restricts it to the strictly linear regime, where there are no
  such structures. Far from equilibrium behaviour can be "even opposite to
  that indicated by the theorem" (pp. 266–267).
- **That no selection principle can exist.** Only that none is established.
  The maximum-entropy-production proposal ([THEORY-tmpxjvy1](THEORY-tmpxjvy1.md)) is a later
  candidate, and its derivation is contested ([THEORY-tmpy0c02](THEORY-tmpy0c02.md)).
- **That dissipative structure is a mark of life.** Convection rolls and
  chemical clocks meet the criterion and are not alive. [NOTE-424](../notes.d/NOTE-424.md) and
  [NOTE-418](../notes.d/NOTE-418.md) both read the physics as a necessary condition at most.
- **That irreversibility comes from dynamics.** The lecture's §§6–7
  programme assumes an entropy operator exists, says that "is certainly not
  always possible" (p. 279), and links it to macroscopic thermodynamics only
  "at least in the linear region".
- **That Bénard's cells were buoyancy-driven.** The lecture's "Bénard
  instability" is Rayleigh's problem. Bénard's open-dish hexagons were
  surface-tension driven (Pearson 1958; [LIT-527](../literature.d/LIT-527.md) §II.B.3).

## Connections

- **Turing's instability ([THEORY-tmphslyk](THEORY-tmphslyk.md))** is the stationary diffusive
  case the lecture names after him, with a purely kinetic criterion.
- **The BZ reaction ([THEORY-tmpe57v7](THEORY-tmpe57v7.md))**: a closed batch oscillates only as
  a transient, and a fed reactor sustains it, which is this account's open
  system in the laboratory.
- **Maximum entropy production ([THEORY-tmpxjvy1](THEORY-tmpxjvy1.md))** proposes the selection
  principle this account says thermodynamics lacks. It does not contradict
  Prigogine's theorem, which answers another question in another regime.
  No `rivals` edge is declared: this account says no principle is
  established, not that none holds.
- **Gradient degradation ([THEORY-tmph2xbv](THEORY-tmph2xbv.md))** and **driven matter
  ([THEORY-tmp1lcfx](THEORY-tmp1lcfx.md))** are further candidates for what selects among
  far-from-equilibrium states.
- **Organisms against flames ([THEORY-072](THEORY-072.md))** cites the lecture for the
  structures themselves and draws the line by closure of constraints, which
  this physics does not supply.
