---
number: 69
status: Proposed
formerly:
- THEORY-tmpjmrqg
promote_when: >-
  A first-hand reading of the data, which this record holds only as one
  of the model's authors reports it. Reading Haken, Kelso & Bunz (1985,
  LIT-588, Deferred) and Schöner, Haken & Kelso (1986, not filed),
  or a later independent replication, and finding in them: anti-phase
  bimanual coordination switching to in-phase at a critical movement
  frequency, and not the reverse; the variance of relative phase and its
  relaxation time after a perturbation both rising as that frequency is
  approached, before the switch; and hysteresis, the system staying
  in-phase when the frequency is lowered again through the bistable
  range. The account is refuted if the fluctuations and relaxation time
  do not grow before the switch, so that the change is a jump with no
  loss of stability (as a motor programme switching on a cue would give),
  or if the transition can be made to run from in-phase to anti-phase by
  raising frequency alone. What cannot settle it: the breadth of systems
  in which HKB-like dynamics has been reported (between people, with
  virtual partners, in brain activity), which the retrospective lists
  and which shows reach, not that the bimanual transition is what the
  model says.
title: 'Rhythmic bimanual coordination switches from anti-phase to in-phase through a nonequilibrium phase transition in relative phase, captured by the HKB equation, with critical fluctuations and critical slowing as early warning'
version: 1
tags:
- behavioral-integration
- complex-systems
- embodied-cognition
date: '2026-10-03'
source:
- LIT-601
summary: >-
  Kelso's 2021 retrospective ([LIT-601](../literature.d/LIT-601.md)) states the
  Haken–Kelso–Bunz model: relative phase φ between the hands obeys
  dφ/dt = −a sin φ − 2b sin 2φ, so in-phase and anti-phase are both stable
  for b/a > 1/4 and anti-phase loses stability below it as movement
  speeds up. With noise the switch is a nonequilibrium phase transition,
  and the reported data show enhanced fluctuations and critical slowing
  before it. Many effectors act as one through a collective variable,
  with no controller choosing the pattern. Proposed, because the 1985
  paper and the 1986 stochastic analysis are unread and the data are
  held as their author reports them.
supports:
- CLAIM-045
- CLAIM-110
- CLAIM-tmpigdl0
- CLAIM-tmptsdgt
---
<!-- inactive-ok-file: LIT-588 LIT-578 — Deferred; HKB 1985 and Dynamic Patterns, named as the unread originals, not leaned on -->
<!-- inactive-ok-file: THEORY-058 THEORY-056 — Proposed; the record's account of disorder as an alternative stable state, and its account of control without a regulator, named for their bearing -->

# THEORY-069: Rhythmic bimanual coordination switches from anti-phase to in-phase through a nonequilibrium phase transition in relative phase, captured by the HKB equation, with critical fluctuations and critical slowing as early warning

## Source

Kelso (2021), "The Haken–Kelso–Bunz (HKB) model: from matter to movement
to mind", [LIT-601](../literature.d/LIT-601.md), read in [NOTE-467](../notes.d/NOTE-467.md): §§2–4, Box 1 and the
Appendix. It stands in for the paywalled 1985 paper ([LIT-588](../literature.d/LIT-588.md)) and the
book *Dynamic Patterns* ([LIT-578](../literature.d/LIT-578.md)), both Deferred.

## What was actually shown

**The model, as Kelso states it.** Kelso ([LIT-601](../literature.d/LIT-601.md)) takes the relative
phase φ of the two index fingers as the order parameter. Its dynamics is
dφ/dt = −a sin φ − 2b sin 2φ, with potential V(φ) = −a cos φ − b cos 2φ.
Both φ = 0 (in-phase) and φ = π (anti-phase) are stable when b/a > 1/4, at
slow movement. Below 1/4, at fast movement, anti-phase is unstable and only
in-phase remains: a pitchfork bifurcation, with movement frequency as the
control parameter. The φ equation is derived from two coupled nonlinear
oscillators, one per limb (Eqs. 4–6), so the collective variable is
obtained from the level below and not only fitted to it.

**Hysteresis follows from the layout.** Because both patterns are stable
in the slow range, a system that has switched to in-phase at high frequency
has no reason to return to anti-phase when the frequency is lowered again.
That is a consequence of Eq. (1), stated here by the record; the read text
does not report the hysteresis data.

**The phase transition and its warning signs, as reported.** With noise
(Eq. 3, Schöner et al. 1986), the switch is a nonequilibrium phase
transition. Kelso reports that "the hallmark features of nonequilibrium
phase transitions including a strong enhancement of fluctuations and
critical slowing down—'anticipatory signatures' of upcoming pattern
change" were observed, and that the stochastic model fitted means,
variances, relaxation times and switching times with a single free
parameter. He quotes Haken that such fluctuations are hard to understand on
a motor-programme account, which "does not allow any fluctuations". This is
the result that could have come out otherwise: a stored programme switching
on a cue predicts an abrupt change with no growth of variability before
it. The record has not seen the data.

**Brain, as reported.** Transcranial stimulation over premotor and
supplementary motor cortex switched anti-phase to in-phase and not the
reverse, as the model's stability asymmetry predicts, and activity in
several motor regions scaled with the instability of anti-phase. Cited, not
read.

## What this does not say

- **Not that the mind is HKB.** Kelso's later sections extend the dynamics
  to coordination between people, with machines, and to "mind". The claim
  here is about rhythmic bimanual coordination. The breadth is reported,
  and the retrospective's inference that coupling is "informational" is
  the author's (C4 in [NOTE-467](../notes.d/NOTE-467.md)).
- **Not that the dynamical model settles the mechanism.** Kelso's claim that
  deriving HKB from neural populations puts the mechanism-versus-description
  objection "to bed" is asserted, not argued.
- **Not a global minimum principle.** The potential V(φ) is a property of a
  one-dimensional flow, which always has one. It is no evidence of the
  kind of variational principle Cross and Hohenberg ([LIT-527](../literature.d/LIT-527.md)) find absent
  in pattern formation away from equilibrium, except near threshold.

## Connections

- **The unity it is about.** `behavioral-integration`: Bernstein's problem
  of many degrees of freedom acting as one, answered by a collective
  variable and not by a controller. The record's other accounts of
  integration work by competition ([THEORY-068](THEORY-068.md)), arbitration or
  bargaining; this is the dynamical alternative. It is not about a self or
  a subject ([ADR-024](../decisions.d/ADR-024.md)).
- **Complex systems.** Rizi ([LIT-150](../literature.d/LIT-150.md)) locates the onset of emergence by order
  parameters, diverging susceptibility and correlation length, and
  asserts that weak emergence is all science needs. HKB is a case in
  the record where an order parameter and a control parameter were
  identified in human behaviour and critical fluctuations reported. Cross
  and Hohenberg ([LIT-527](../literature.d/LIT-527.md)) describe patterns near onset by low-dimensional
  amplitude and phase equations; HKB's reduction to one phase variable near
  an instability is that strategy applied to limbs.
- **[THEORY-058](THEORY-058.md)** (mental disorders as alternative stable states of
  self-reinforcing loops). That account borrows hysteresis and critical
  slowing from the physics of phase transitions, and the record notes it
  does so without an order parameter or a measured transition. HKB is the
  record's case of the same signatures with both, in human behaviour, so it
  shows the kind of evidence [THEORY-058](THEORY-058.md)'s `promote_when` asks for can be
  obtained from people. It is no evidence that disorders behave this way,
  and no relation is declared.
- **[THEORY-056](THEORY-056.md)** (control without a distinct regulator). HKB's pattern
  changes are not chosen by any controller. It is a neighbour in
  architecture, about movement and not motive, and no relation is declared.
- **Participatory sense-making ([LIT-571](../literature.d/LIT-571.md))** and **Raja et al.
  ([LIT-598](../literature.d/LIT-598.md))** take Kelso's coordination dynamics as given: the first
  for relative coordination between people, the second as a system already
  explained by its own collective variable, which a Markov-blanket
  partition does not improve on.
