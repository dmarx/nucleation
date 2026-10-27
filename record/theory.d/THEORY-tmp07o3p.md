---
status: Proposed
promote_when: >-
  A theorem for a class of nonlinear open systems that states when the
  system tracks, and when it tips from, a branch of quasi-static
  attractors under a time-varying parameter, as a comparison between the
  drift of the attractor in state space and the system's slowest
  relaxation, scaled by the distance to the threshold; or a nonlinear
  counterexample in which tracking fails although that drift is slow
  against every relaxation rate. Not settled by more linear or
  normal-form examples, which the paper already gives, nor by
  simulations that bracket a critical rate.
title: 'A quasi-static attractor describes an open system only while the drift of that attractor in state space is slow against the system''s slowest relaxation, scaled by the distance to the tipping threshold; rate-induced tipping is the failure of that time-scale separation, and it can occur while the parameter itself moves slowly, if the attractor is sensitive to it, and with no slowing of any mode'
version: 1
tags:
- complex-systems
- mathematics
date: '2026-10-27'
source:
- LIT-tmpj4ix1
summary: >-
  Ashwin, Wieczorek, Vitolo and Cox (2012), [LIT-tmpj4ix1](../literature.d/LIT-tmpj4ix1.md), read in
  [NOTE-tmp429c3](../notes.d/NOTE-tmp429c3.md). Shown for the linear tipping-radius model, where the
  sufficient condition for tracking is a rate comparison, and stated for
  a fast-slow example ("rate dependent tipping occurs when the slow and
  very slow timescales are no longer separable"). Proposed because for
  nonlinear systems the paper says "no exact analogy possible" and gives
  no general condition. It bears on [CLAIM-tmpmx2ql](../claims.d/CLAIM-tmpmx2ql.md), whose constraints hold
  over a window between time scales.
---
<!-- inactive-ok-file: CLAIM-tmpmx2ql CLAIM-157 — Proposed; neighbours cited as open -->

# THEORY-tmp07o3p: A quasi-static attractor describes an open system only while the drift of that attractor in state space is slow against the system's slowest relaxation, scaled by the distance to the tipping threshold; rate-induced tipping is the failure of that time-scale separation, and it can occur while the parameter itself moves slowly, if the attractor is sensitive to it, and with no slowing of any mode

## Source

Ashwin, Wieczorek, Vitolo and Cox (2012), [LIT-tmpj4ix1](../literature.d/LIT-tmpj4ix1.md), §1 (p. 2), §2.2
(p. 8), §3.3.2 (p. 16) and §5 (p. 19), arXiv v5; read in [NOTE-tmp429c3](../notes.d/NOTE-tmp429c3.md).

## What was actually shown

**In the linear model, tracking is a rate comparison.** With
‖e^{Mu}‖ ≤ c e^{−βu}, the system avoids tipping by time t if
(c/β)·r_max(t) < R, eq. (13), where r_max is the largest drift
|dx̃/dt| so far; for scalar M this is ‖M⁻¹‖·r_max(t) < R, eq. (14). The
paper reads it as time scales: the QSE's motion has a natural time R/|r(t)|,
and "For an R-tipping to occur, this natural timescale may be comparable to
the slowest timescale (e.g. the reciprocal of the leading eigenvalue of M) of
the parametrized system" (p. 8).

**The drift that counts is the attractor's, not the parameter's.**
r = (dx̃/dλ)(dλ/dt), eq. (8). "if |dx̃/dλ| ≈ 1/ε, then clearly we can have
R-tipping even when |dλ/dt| ≈ ε‖M‖" (p. 8). A parameter that moves slowly
against the system's own rates can still tip it if the attractor's position
is sensitive to the parameter.

**In the fast-slow example the separation is named.** "only when the
parameter variation is very slow with respect to the slow variable and there
are three timescales is tracking guaranteed. In this sense, the rate
dependent tipping occurs when the slow and very slow timescales are no longer
separable" (p. 16).

**No slowing is needed.** "neither N-tipping and R-tipping require any
change of stability" (p. 19). In the linear model M is fixed, so no mode
slows; the separation is lost because the input speeds up. This is set
against the separation κ_drift ≪ κ_crit ≪ κ_stab that time-series analysis
of bifurcation-induced tipping relies on, for which "there is no a priori
reason … to hold for a given system" (p. 2).

## What this does not say

- **That the comparison decides for nonlinear systems.** The tipping-radius
  model has "no exact analogy" there: an effective radius "may depend on
  the shape of the local basin of attraction, the nonlinearities present and
  the exact path taken in parameter space" (p. 8). The linear condition is
  sufficient for tracking, not necessary, and no sufficient condition for
  tipping under varying drift is given (p. 8).
- **That separation lost always means tipping.** Between the two steady-drift
  bounds the path decides (p. 7), and the starting state moves the critical
  rate (eqs. 17, 37).
- **That this is the only way separation fails.** Near a bifurcation the
  slowest relaxation goes to zero and the same comparison fails from the
  other side; that is B-tipping with slow passage effects, which the paper
  names (p. 2) and does not analyse.
- **Anything about constraints or individuation.** The reading of the
  quasi-static attractor as a constraint that holds over a window between
  time scales is [CLAIM-tmpmx2ql](../claims.d/CLAIM-tmpmx2ql.md)'s, not the paper's.
