---
status: Active
title: 'An open system can tip away from an attractor that exists, keeps its stability and keeps its basin at every frozen value of its parameter, when the attractor moves faster than the system can track it; with steady drift what bifurcates is the ability to track, in a co-moving frame, not the attractor, and the critical rate depends on the relaxation rate, the distance to the tipping threshold and the starting state'
version: 1
tags:
- complex-systems
- mathematics
date: '2026-10-27'
source:
- LIT-tmpj4ix1
summary: >-
  Ashwin, Wieczorek, Vitolo and Cox (2012), [LIT-tmpj4ix1](../literature.d/LIT-tmpj4ix1.md), read in
  [NOTE-tmp429c3](../notes.d/NOTE-tmp429c3.md) from the corrected arXiv v5. Active as mathematics: shown
  in a linear model with a fixed stable matrix (so no bifurcation and no
  noise), in normal-form examples worked exactly, and in a fast-slow
  system whose equilibrium is unique and globally stable. It does not say
  that a system that tips is lost for good, that the threshold is a
  basin boundary, or that any real system has tipped this way.
---
<!-- inactive-ok-file: QUESTION-tmpl1yih CLAIM-157 THEORY-tmp07o3p — Open or Proposed; neighbours cited as open -->

# THEORY-tmpksbqt: An open system can tip away from an attractor that exists, keeps its stability and keeps its basin at every frozen value of its parameter, when the attractor moves faster than the system can track it; with steady drift what bifurcates is the ability to track, in a co-moving frame, not the attractor, and the critical rate depends on the relaxation rate, the distance to the tipping threshold and the starting state

## Source

Ashwin, Wieczorek, Vitolo and Cox (2012), [LIT-tmpj4ix1](../literature.d/LIT-tmpj4ix1.md), §§1–3 (pp. 3–16 of
arXiv v5, whose §§2.1–2.2 are the corrected text); read in [NOTE-tmp429c3](../notes.d/NOTE-tmp429c3.md).

## What was actually shown

**The definition.** For an open system dx/dt = f(x, λ(t)), "'R-tipping'
where the system fails to track a continuously changing quasi-static
attractor" (p. 3), set beside B-tipping (a bifurcation of that attractor)
and N-tipping (noise carries the system out of its neighbourhood).

**The linear model** (§2). dx/dt = M(x − x̃(λ)) inside a tipping radius R,
with M "a fixed stable linear operator". "because M is fixed there is no
bifurcation in the system and no noise is present" (p. 5). The state lags
the moving equilibrium by x − x̃ = −∫₀^∞ e^{Mu}(dx̃/dt) du, eq. (6), whose
leading term is M⁻¹r with r = (dx̃/dλ)(dλ/dt). With steady drift the lag is
exactly M⁻¹r: tipping is avoided if ‖M⁻¹‖·|r| < R, eq. (11), and occurs if
‖M‖⁻¹·|r| > R (p. 7). So the outcome compares how fast the equilibrium moves
with how fast the system relaxes, scaled by how far the threshold is.

**The examples** (§3), each of which could have failed to tip:

- Subcritical Hopf with a smooth shift of the equilibrium: "there is no
  change in stability or basin size of the QSE as t changes", yet for ∆ = 8
  the system tracks at ρ = 4.76 and tips at ρ = 4.8 (p. 12, Fig. 5).
- A fast-slow system whose equilibrium is unique and "globally
  asymptotically stable if N ≥ 5", where the fold of the slow manifold "defines
  a tipping threshold that is not associated with any basin boundary"
  (p. 13); r_c = Σ 2⁻ⁿ with steady drift, eq. (33).
- The critical rate depends on where the system starts: eq. (17) for the
  saddle-node normal form, eq. (37) for the fast-slow system with unsteady
  drift; in the linear model, between the two bounds "the path of
  parameter variation will determine whether or not there is any
  R-tipping" (p. 7).

**What bifurcates.** With steady drift, a change to co-moving coordinates
turns R-tipping into a bifurcation problem: a saddle-node at r = µ in
y = x + λ (§3.1), a saddle-node or subcritical Hopf of the co-moving
equilibrium of dw/dt = F(w) − r (§3.2.1). "observe that the bifurcation
parameter r does not vary in time, and it is 'the ability to track the QSE',
rather than the QSE itself, that bifurcates" (p. 11). With unsteady drift
there is no such reduction (§3.2.2).

**Rate cuts both ways.** "B-tipping may be suppressed for fast enough
variation of parameters" (p. 19, Fig. 8a): fast change can carry a system
past a bifurcation it would have tipped at under slow change.

## What this does not say

- **That a system that tips is lost for good.** Tipping is reaching the
  radius R, past which the linear model is "unphysical" (p. 5). In the
  climate model just below ρ_c "the system returns to the QSE after a
  transient" (Fig. 7a), and in the globally stable fast-slow system the
  paper does not say what follows the divergence. Loss is permanent only
  if the region past the threshold leads elsewhere, as in §3.1 and
  Fig. 7b, where solutions are unbounded.
- **That the threshold is a basin boundary.** It may be one (§§3.1–3.2)
  or not (§3.3); in the linear model it is a modelling choice.
- **That the rate alone decides.** The critical rate depends on the
  relaxation rate, the distance to the threshold, the starting state and,
  away from steady drift, the path.
- **A general nonlinear theory.** For nonlinear systems "There is however
  no exact analogy possible" with the tipping-radius model (p. 8), and no
  sufficient condition for tipping under varying drift is given.
- **That any real system has R-tipped.** The climate example is a
  zero-dimensional energy balance model; applications beyond climate are
  suggested, not shown (p. 19).
