---
number: 112
status: Active
formerly:
- CASE-tmpiyvbk
title: 'Bistable authority with a tilt: in ẇ = μw − w³ + h, with w the balance of authority between two regimes and h a higher-order volition favouring one, for μ > 0 the operative regime changes only when |h| passes 2μ^{3/2}/(3√3), so a sincere and efficacious higher-order volition can move the balance without moving the regime, and which regime operates depends on the path of h'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A19 used this case's equation at h =
    0 with μ = α − κ for the authority balance between two organizations
    (CLAIM-tmpptl3y); there the pitchfork is supercritical and restoring the
    constraint restores equality, and this case's hysteresis is in the tilt
    h at fixed μ > 0. Extended the same day: Arthur's planner who tilts at the outset matches the tilt before symmetry breaks. The case is unchanged.
standing: fictional
kind: construction
tags:
- self-governance
- complex-systems
date: '2026-10-18'
line: will-organization
illustrates:
- CLAIM-122
- CLAIM-025
summary: >-
  A8 §4 of the exchange of 2026-10-17, restated as A12's Proposition 3
  and kept in A15. The saddle-node threshold and the hysteresis are
  derived and rechecked here. A8: "It's a countermodel showing why
  endorsement strength, effective governance, and behavioral transition
  can come apart." A8's "endorsement" is the reflective attitude, not the
  record's [TERM-053](../terms.d/TERM-053.md) sense, so h is called a higher-order volition. It
  models authority between regimes; it does not revive will as an
  attractor ([TERM-003](../terms.d/TERM-003.md), Superseded). Fictional by construction.
supports:
- CLAIM-tmpptl3y
---

# CASE-112: Bistable authority with a tilt: in ẇ = μw − w³ + h, with w the balance of authority between two regimes and h a higher-order volition favouring one, for μ > 0 the operative regime changes only when |h| passes 2μ^{3/2}/(3√3), so a sincere and efficacious higher-order volition can move the balance without moving the regime, and which regime operates depends on the path of h

## The construction

A8 §4: "Suppose w represents the balance of authority between two
action-generating regimes. Let h represent an endorsement favoring one of
them. A minimal nonlinear model is

  ẇ = μw − w³ + h.

Here μ controls the stability structure, and h tilts the competition
toward the endorsed regime." A12's Proposition 3 is the same equation in z.
Here h is a higher-order volition in Frankfurt's sense, an attitude that
one regime should be effective. The record's endorsement ([TERM-053](../terms.d/TERM-053.md)) is a
different thing, an effect of one process on another's share of
influence.

Equilibria satisfy h = φ(w) = w³ − μw, and f′(w) = μ − 3w².

- **μ ≤ 0.** φ is monotone, so there is one equilibrium for each h, and it
  is stable.
- **μ > 0.** φ has a local maximum at w = −√(μ/3) and a local minimum at
  w = +√(μ/3), of value ±(2μ/3)√(μ/3), so

    h_c = 2(μ/3)^{3/2} = 2μ^{3/2}/(3√3).

  For |h| < h_c there are three equilibria. The outer two have
  |w| > √(μ/3), so f′ < 0, and they are stable. The middle one is
  unstable. At |h| = h_c an outer equilibrium meets the middle one and
  both vanish, a saddle-node.
- **Hysteresis.** Start in the competing regime, w < 0, and raise h. For
  0 < h < h_c the state moves continuously along the lower branch and
  stays there. Past h_c the branch is gone and w jumps to the upper one.
  Lower h back to 0 and w stays positive. Returning to the first regime
  needs h < −h_c.
- **Structure against strength.** h_c falls to 0 as μ → 0. A change in μ,
  the structure of the competition, can make a small h decisive. A8: "With
  stronger endorsement, or with structural changes that alter μ, the
  competing attractor may disappear".

The threshold was checked by hand and numerically for this filing.

## What it can show

- **Efficacy without transition.** A8: "An endorsement can be sincere and
  causally efficacious while remaining too weak to shift the system out of
  its current attractor basin. It may change the local balance without
  producing a behavioral transition." For 0 < h < h_c the volition moves
  w, and the regime is unchanged.
- **Changing the conditions, not the attitude.** Lowering μ with h fixed
  can switch the regime. That is [CLAIM-122](../claims.d/CLAIM-122.md)'s form: changing the
  conditions of efficacy changes behaviour while the competing attitudes
  stay fixed. It is [CASE-013](CASE-013.md)'s writer blocking the websites.
- **Persistence against revision.** A12, Proposition 3: "An enduring
  commitment can coexist with high costs of revision." Once in the upper
  regime the agent stays there for every h > −h_c. That is [CLAIM-025](../claims.d/CLAIM-025.md)'s
  separation, and the revisability dimension of [CLAIM-354](../claims.d/CLAIM-354.md).

## What it cannot show

- **That motivation follows this equation.** A8: "This is not a claim that
  human motivation literally follows a quartic potential." A12: "application
  to human commitments remains interpretive."
- **Will as an attractor.** [TERM-003](../terms.d/TERM-003.md) defined will as a higher-order
  attractor and was superseded by will-organization ([TERM-023](../terms.d/TERM-023.md)). Here the
  attractor is a state of the balance of authority, and the will-organization
  is what sets μ and passes h into w. The case does not restore the old
  definition.
- **That h is the agent's own.** A8 §3: "we could accidentally redefine
  endorsement as whichever signal successfully changes behavior. That
  would collapse a normative notion into a causal one." The model says
  what an input does, not what makes it authoritative ([THEORY-029](../theory.d/THEORY-029.md)).

## Note of 2026-10-21: the normal form at zero tilt, read as a rule

A19 of the exchange of 2026-10-20 used ḋ = (α − κ)d − βd³ for the
authority balance between two organizations, with κ a stabilizing
institutional constraint. That is this case's equation at h = 0 with
μ = α − κ: weakening the constraint past κ = α makes the equal allocation
unstable (checked). It is a second appearance of the normal form, and a
new reading of μ as the strength of a rule. It is filed as [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md),
which this case supports.

At h = 0 the pitchfork is supercritical, so in κ there is no hysteresis:
restoring κ > α makes the equal allocation again the only equilibrium,
and a tipped allocation decays back to it. This case's hysteresis is in
the tilt h at fixed μ > 0, and it is what A19 did not draw: an allocation
tipped by a tilt past h_c is not restored by removing the tilt. This
case's h is what A19 called "explicit symmetry breaking". [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md)'s
check also ran this case's form with a small tilt through a weakening,
restoring and re-weakening of the constraint: restoring it brought w near
zero, and weakening it again selected the side the tilt favours, not the
side the state had held before.

Arthur's model, read the same day through its 1983 working paper
(NOTE-tmpyyaar), has the same shape in another setting: a planner can
tilt the adoption process at the outset, and once one technology has
locked in, small changes in returns have no effect and only large ones
swing the market (THEORY-tmpxzls4). That matches this case's tilt h before
symmetry breaks and its hysteresis in h after; Arthur's lock-in is
absorption in accumulated adoptions, not a pitchfork, so the match is of
shape only.
