---
status: Proposed
title: 'In tolerance-bounded compatibility on a graph with disturbed offsets, one configuration serves every disturbance in a class the agent cannot tell apart exactly when, on each overlap, the class''s half-range of disturbance is within tolerance, and the cycle condition for compatibility holds for the class''s midpoint offsets with each tolerance reduced by that half-range; whether a compatible configuration exists depends on a disturbance only through its cohomology class, but whether one can be selected depends on its edgewise spread, so an agent that reads the cohomology class exactly need not be able to select one'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A counterexample within the scalar model: offsets, tolerances and a
  finite class of disturbances for which the half-range and reduced cycle
  conditions hold and no single configuration serves the class, or fail
  and one does. Or the triangle case failing: two disturbances in the
  same cohomology class, each with a compatible configuration, that one
  configuration serves. Not defeated by a dynamic agent that re-selects
  over time; the claim is about one-shot selection, as CLAIM-537 is.
tags:
- mathematics
- agency
date: '2026-11-07'
line:
- formal-apparatus
- will-organization
rests_on:
- CLAIM-537
- CLAIM-538
summary: >-
  A by-product of the synthesis review of 2026-11-07, where the reader
  of the formal-apparatus cluster found that the cluster did not
  integrate and that one inference from it is new. CLAIM-537's condition
  III says an agent can select a configuration from what it observes
  exactly when the static condition holds within each class of
  disturbances it cannot tell apart; this claim says what that condition
  is for a given class, using CLAIM-538's cycle condition, and draws the
  consequence for an agent that reads the disturbance's cohomology class.
  The coboundary observation is the reader's; the criterion for a class
  is the filer's, checked by linear programming on 1,480 random graphs
  with no mismatch (scratch/formal/class_selection_check.py). Both are
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

# CLAIM-tmpkvgmj: In tolerance-bounded compatibility on a graph with disturbed offsets, one configuration serves every disturbance in a class the agent cannot tell apart exactly when, on each overlap, the class's half-range of disturbance is within tolerance, and the cycle condition for compatibility holds for the class's midpoint offsets with each tolerance reduced by that half-range; whether a compatible configuration exists depends on a disturbance only through its cohomology class, but whether one can be selected depends on its edgewise spread, so an agent that reads the cohomology class exactly need not be able to select one

## The claim

Take CLAIM-537's model: overlaps e of a graph with nominal offsets a₀,
tolerances δ, disturbances w, and the requirement |Dx − a₀ − w| ≤ δ. An agent
that observes o = h(w) must choose one x for the whole class C = h⁻¹(o).

**For a class.** One x serves every w ∈ C exactly when, on each overlap,
(Dx)_e lies in [a₀_e + max_C w_e − δ_e, a₀_e + min_C w_e + δ_e]. With
m_e and r_e the midpoint and half-range of w_e over C, that interval is
centred at a₀_e + m_e with half-width δ_e − r_e. So the class is selectable
exactly when

- r_e ≤ δ_e on every overlap, and
- CLAIM-538's cycle condition holds for offsets a₀ + m and tolerances
  δ − r: on every cycle c, |cᵀ(a₀ + m)| ≤ Σ (δ_e − r_e)|c_e|.

This is CLAIM-537's condition II with the class's spread in place of the
disturbance bound η, and its midpoint in place of the nominal offset.

**Existence against selection.** By CLAIM-538, whether a world w has a
compatible configuration depends on a₀ + w only through its class in
H¹(G; ℝ), its holonomies. Selection depends on the edgewise spread of the
class, which the H¹ class does not fix. So an agent whose observation is
exactly the cohomology class of the disturbance, h(w) = [w], can be unable to
select a compatible configuration in a class where every world has one.

**The triangle.** CLAIM-537's own example shows it: a₀ = 0, δ_e = 0.3, and
the worlds w = (0.6, −0.6, 0) and (−0.6, 0.6, 0). Both are coboundaries, of
holonomy 0, so they lie in one H¹ class and each has an exact solution. Edge
12 would need x₂ − x₁ in both [0.3, 0.9] and [−0.9, −0.3]: the half-range
there is 0.6 > 0.3. No single configuration serves both.

## Check

scratch/formal/class_selection_check.py compares the criterion with a
direct linear program on 1,480 random connected graphs of three to five
nodes, with classes of one to four disturbances. There were no mismatches,
and 335 instances were selectable. It then reproduces the triangle.

## What it does not say

- **That reading the cohomology class is useless.** It fixes whether
  compatibility is possible world by world, which is CLAIM-537's condition I.
  It does not fix what the agent can do about it.
- **Which observation is the least that suffices.** Observing w exactly
  always does when condition I holds; the coarsest observation that makes
  every class selectable is not characterized here.
- **Anything about feedback over time, or beyond scalar overlaps**, the
  limits CLAIM-537 states.
