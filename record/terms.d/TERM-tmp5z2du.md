---
status: Proposed
title: 'hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum'
version: 1
tags:
- information-geometry
- mathematical-statistics
- complex-systems
- model-comparison
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
draws_on:
- THEORY-774
- THEORY-777
- THEORY-742
summary: >-
  The shape the exchange "Rich Get Richer Power Laws" gives, at A19 §4,
  to the set of predictions a sloppy model can make: long in a few
  directions and thinner along each further one, the widths falling
  roughly geometrically, so there is no sharp line between the parameter
  combinations that matter and those that do not. The record held the
  sloppy Fisher spectra that produce it (THEORY-774, THEORY-777) but had
  no word for the shape, which the exchange returns to from A38 on, where
  the owner ties it to Watanabe's stratification (U24). The term is from
  Transtrum, Machta and Sethna (LIT-tmpd3swn, LIT-tmpzkxka, unread); the
  conditions in the definition, and the separation from a power law in
  event sizes, are the assistant's checks of A's wording. The wording is
  A's (the other assistant in the exchange "Rich Get Richer Power Laws",
  A19); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the record's evidence for the critical-Ising spectrum -->
<!-- inactive-ok-file: LIT-tmpd3swn LIT-tmpzkxka LIT-tmpm1tji LIT-tmp0fpti LIT-tmpdz70v LIT-tmpsqbr9 — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: CLAIM-tmpficzj CLAIM-tmpj0k4q QUESTION-tmpzlagu — filed with this term from the same exchange, Proposed -->

# TERM-tmp5z2du: hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum

## Definition

Take a model whose parameters θ (N of them) map to a vector of
predictions y(θ) in the space of possible observations, each component
scaled by its measurement error. The **model manifold** is the image of
parameter space under that map: the set of all prediction vectors the
model can produce. It is a **hyperribbon** when, measured along a
sequence of mutually orthogonal directions, its widths fall roughly
geometrically, each width smaller than the last by a roughly constant
factor, over many decades.

A19 §4 puts it so: the manifold "is extended in a few directions but
becomes progressively thinner along others. Researchers call this
geometry a *hyperribbon*", and "a hyperribbon has many dimensions, with a
hierarchy of successively smaller widths". The point A draws from it:
"In a sloppy model, there may be no abrupt distinction between important
and unimportant parameter directions. Instead, their importance can
decrease steadily across many orders of magnitude."

**What ties it to a Fisher spectrum.** Locally, with Gaussian errors, the
Fisher information is the metric the map pulls back,
I = JᵀJ/σ² with J = ∂y/∂θ, and its eigenvalues λ₁ ≥ λ₂ ≥ … are the
squared stretch factors of the map along its principal directions. A
spectrum spread geometrically over decades, a **sloppy** one, is the local
form; the hyperribbon is the global form, in which the manifold's
extent, bounded by where parameters run to their limits, follows the same
hierarchy. The stiff directions are usually combinations of parameters,
not single ones: A19 §2's two-parameter model,
y = (θ₁+θ₂)x + ε(θ₁−θ₂)z with x and z orthonormal, has Fisher eigenvalues
2/σ² along θ₁+θ₂ and 2ε²/σ² along θ₁−θ₂, a ratio of 1/ε², 400 at
ε = 0.05. The assistant checked those values by computing JᵀJ in numpy
(eigenvalues 2 and 0.005 at σ = 1, ratio 400.0).

**Two conditions the definition carries** (the assistant's, not A's):

1. *Relative to an experiment.* Widths are measured in units of
   measurement error, so the same model is a hyperribbon for one design
   and not another. A19 §2 says as much: "Fisher sensitivity is local and
   depends on what we measure, measurement noise, and parameter
   coordinates." In the record's two worked cases the spread appears only
   through coarse observation: the hopping model's eigenvalues separate by
   a factor of order t when the density is seen after t steps
   (THEORY-774), and the critical Ising model's irrelevant directions fall
   by up to six decades under decimation while the field and the
   T_c gradient stay (THEORY-777, THEORY-742).
2. *Regular, not singular.* The local reading needs a Fisher matrix of
   full rank where it is evaluated. At a singular point, where it loses
   rank, the widths do not shrink smoothly to zero along a direction; the
   manifold folds or pinches, and the Bayesian count of effective
   parameters is set by the learning coefficient rather than by the
   spectrum (THEORY-087, THEORY-1253). How the two pictures meet is the
   owner's question at U24, left to the filing of that turn.

## What it is not

- **Not a power law in event sizes, and not evidence of criticality.**
  A19 §5 marks this itself: "a geometric hierarchy of parameter
  sensitivities is not itself evidence that event sizes follow a power
  law or that the system is critical. The common feature is scaling. The
  quantities being scaled, and the mechanisms producing the scaling, are
  different." A hyperribbon is a statement about parameter
  distinguishability under one experiment; a power-law tail is a
  statement about the distribution of one observable.
- **Not RG relevance.** In suitable settings the stiff directions after
  coarse-graining are the relevant ones (THEORY-777, THEORY-742), but
  stiffness depends on the measurement and coordinates and relevance on a
  fixed point and a scale map (A19 §5). A19 §5's table gives critical
  exponents as the rates at which perturbations "grow or shrink under
  rescaling"; for the Fisher eigenvalues the record's reading has the
  rate b^(2y−d) per step, with the dimension d in it, not b^y
  (THEORY-777), and the exact transfer of the metric needs the
  renormalized Hamiltonian to stay in the family (THEORY-742).
- **Not a count of parameters.** Neither a hyperribbon's dimension nor
  its number of "wide" directions is fixed: how many directions a data set
  resolves grows with the data (CLAIM-tmpj0k4q), and which of several
  effective dimensions is meant is open (QUESTION-tmpzlagu).

## Sources

The term and the geometry: Transtrum, Machta and Sethna 2010 and 2011
(LIT-tmpd3swn, LIT-tmpzkxka), and the review by Transtrum and colleagues
2015 (LIT-tmpm1tji) and by Quinn and colleagues 2023 (LIT-tmp0fpti), the
work A19 links. The method of reducing a model along its thin directions
to the manifold's boundary, which A19 §4 names: Transtrum and Qiu 2014
(LIT-tmpdz70v). The empirical base in systems biology: Gutenkunst and
colleagues 2007 (LIT-tmpsqbr9). All are Deferred and unread; the
definition rests on A's wording and on the record's readings of
THEORY-774, THEORY-777 and THEORY-742.
