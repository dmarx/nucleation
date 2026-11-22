---
number: 904
status: Proposed
formerly:
- CLAIM-tmpjwc0h
title: 'Compensation under a sustained load does not need a block: in a phi4 lattice kink and in the locked cluster of a uniformly coupled Kuramoto population the other members undo nearly all of a load''s damage to the form, as in a two-block control, while the block test on members gives the kink a ratio that falls as the square of the lattice spacing and gives the cluster, on its coupling constants, the score of every set of its size'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A correct rerun of the computation that finds, in either mode, the other
  members undoing less than half of a sustained load's damage to the
  form's task variable at the core of the kink or across the locked
  cluster; or a block test on member groupings, of the kind CLAIM-157
  states, that singles out the kink's sites as the lattice spacing goes to
  zero, or that singles out the locked cluster on the coupling constants
  alone. A different Occam threshold does not count for the cluster, since
  every set of its size scores the same.
tags:
- individuation
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-334
bears_on:
- QUESTION-218
- QUESTION-035
summary: >-
  From [LEAD-083](../leads.d/LEAD-083.md)'s study. With κ the share of a sustained load's damage
  to the form that the other members undo (others free against others
  frozen), κ is 1.00 on the kink's core at every spacing, 0.97 for the
  locked cluster and 1.00 in a two-block control. The cluster's members
  also entrain: detuned members are held, and the rest follow them by
  0.91 of their shift. The kink's compensating sites move with it, so no
  grouping of sites is the unit over time. The block test on segments
  holding the kink falls from 1.57 to 0.11 as the spacing halves twice,
  and entrywise coupling is uniform. On coupling constants the cluster
  scores √(156/44), as every subset of 156 does. On realized interaction
  it stands out (0.81 against 0.19 to 0.28) without clearing τ = 1. Two
  cases of the kind [CLAIM-157](CLAIM-157.md)'s `defeated_if` names, partly: the kink has
  no timing to entrain. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; the criterion the study tests -->
<!-- inactive-ok-file: CASE-334 — new; the study this claim states -->

# CLAIM-904: Compensation under a sustained load does not need a block: in a phi4 lattice kink and in the locked cluster of a uniformly coupled Kuramoto population the other members undo nearly all of a load's damage to the form, as in a two-block control, while the block test on members gives the kink a ratio that falls as the square of the lattice spacing and gives the cluster, on its coupling constants, the score of every set of its size

## The claim

In [CASE-334](../cases.d/CASE-334.md)'s three arms:

1. **Compensation without a block.** Hold a few members displaced and
   read the form's task variable with the other members free and frozen.
   The others undo all of the damage at the kink's core (κ = 1.00 at
   h = 0.5 and 0.25), 0.97 of it in the Kuramoto cluster, and 1.00 of it
   in a block of the control. Compensation, as a mark of unity, does not
   distinguish a block from these two modes.
2. **The kink's compensating members are not fixed.** The sites with
   κ > 0.5 at t = 50 are those within 1.5 to 2.25 units of the kink's centre, and
   moving the kink by 6 moves them by 6. The unit is a function of the
   whole field, as [QUESTION-218](../questions.d/QUESTION-218.md) puts the alternative, and not a subset
   of sites.
3. **The block test on members misses the kink in the continuum limit.**
   Neighbouring sites are coupled equally everywhere. The best ratio of a
   segment holding the kink is its shape-mode gap over 1/h², about 1.5h²:
   1.57, 0.43 and 0.11 at h = 1, 0.5 and 0.25. At h = 1 it clears τ = 1
   and beats the vacuum; at h ≤ 0.5 only segments of at most four sites
   clear τ = 1, and vacuum segments of their size score within 7% of
   them. Compensation does not change with h.
4. **The cluster's members compensate and entrain, and the coupling
   constants cannot pick them out.** Five detuned members move 5% of their
   detuning and the rest of the cluster follows them by 0.91 of that.
   Detuned drifting oscillators move the cluster by nothing measurable. On
   the coupling constants every set of 156 oscillators scores
   ρ = √(156/44) = 1.88, the cluster included. On the realized Jacobian it
   scores 0.81 against 0.19 to 0.28 for random sets of its size.

## What it does not say

- **That either mode is one system.** It says that two marks of unity the
  record names, measured, come apart from the block test on members.
- **That [CLAIM-157](CLAIM-157.md) is defeated.** Its `defeated_if` asks for systematic
  failures, and these are two models at one setting each. The kink meets
  only the compensation half, since an overdamped kink has no timing. The
  cluster meets both halves, but whether the test misses it depends on
  reading interaction as coupling constants or as realized, and on τ.
- **That compensation is more than restoring a declared form.** κ is read
  against a declared task variable. In the kink's vacuum it is negative,
  since local healing takes the field away from every kink.
- **That the kink's closure was measured as dynamical independence.** Its
  closure is the gap in its linearization (translation mode near 0,
  shape mode 1.5, continuum from 2).

## Why it bears on the block test

[CLAIM-157](CLAIM-157.md)'s point 3 already names a mode, the projector onto the
block's joint mode, as the unit. This claim shows where finding that mode
by grouping members fails while the marks of unity hold. In the kink the
gap that sets the mode off is in the eigenbasis of the whole field, which
is [CLAIM-164](CLAIM-164.md)'s object, and no grouping of sites carries it.
