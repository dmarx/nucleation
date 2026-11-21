---
status: Proposed
title: 'hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Edited in place, the term having been filed in this pull request, after
    the readings of LIT-tmpd3swn (NOTE-tmpamhd2), LIT-tmpzkxka
    (NOTE-tmpzxtnv) and LIT-tmpm1tji (NOTE-tmphbpab). The title and the
    definition's core stand. Corrected: the papers spell it "hyper-ribbon"
    (the 2015 review mostly "hyperribbon"); the widths are geodesic, measured
    from a central point along the metric's eigendirections; the tie of
    widths to the spectrum (width ≈ √λ) is the authors' empirical finding
    under conditions, not an identity; their argument for the geometric
    fall is a heuristic from interpolation in one independent variable;
    condition 2 is revised, since the manifold's boundaries are where the
    metric is singular; the caution against equating stiffness with RG
    relevance is A's, not the review's. The statements that the sources were
    unread are replaced.
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
- THEORY-tmpgsgka
- THEORY-tmpkoje5
- THEORY-tmpd7a4j
- THEORY-774
- THEORY-777
- THEORY-742
summary: >-
  The shape the exchange "Rich Get Richer Power Laws" gives, at A19 §4,
  to the set of predictions a sloppy model can make: long in a few
  directions and thinner along each further one, the widths falling
  roughly geometrically, so there is no sharp line between the parameter
  combinations that matter and those that do not. The record held the
  sloppy Fisher spectra that produce it ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)) but had
  no word for the shape, which the exchange returns to from A38 on, where
  the owner ties it to Watanabe's stratification (U24). The term is from
  Transtrum, Machta and Sethna (LIT-tmpd3swn, LIT-tmpzkxka, read on
  2026-11-21 as THEORY-tmpkoje5 and THEORY-tmpgsgka, which corrected the
  definition in version 2: geodesic widths from a central point, width ≈ √λ
  under conditions, a heuristic argument); the
  conditions in the definition, and the separation from a power law in
  event sizes, are the assistant's checks of A's wording. The wording is
  A's (the other assistant in the exchange "Rich Get Richer Power Laws",
  A19); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the record's evidence for the critical-Ising spectrum -->
<!-- inactive-ok-file: LIT-tmp0fpti LIT-tmpdz70v LIT-tmpsqbr9 — Deferred, registered 2026-11-21 from the exchange, unread -->
<!-- inactive-ok-file: CLAIM-tmpj0k4q — filed with this term from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-tmpb2gly TERM-tmptiim0 THEORY-tmpd7a4j THEORY-tmpgsgka THEORY-tmpkoje5 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# TERM-tmp5z2du: hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum

## Definition

Take a model whose parameters θ (N of them) map to a vector of
predictions y(θ) in the space of possible observations, each component
scaled by its measurement error. The **model manifold** is the image of
parameter space under that map: the set of all prediction vectors the
model can produce. It is a **hyperribbon** when, measured along a
sequence of mutually orthogonal directions, its widths fall roughly
geometrically, each width smaller than the last by a roughly constant
factor, over many decades. The papers spell it **hyper-ribbon**: "We
describe the shape of a model manifold with such a hierarchy as a
hyper-ribbon" ([LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), §III); the 2015 review writes "hyperribbon".
The **widths** are geodesic: the data-space length of a geodesic started
from a central point along an eigendirection of the metric, run until it
meets a boundary, or the length of a cross-section ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), Fig. 3:
"Geodesic cross-sectional widths ... along the eigendirections of the
metric from some central point"). In the papers' examples they span about
four decades.

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
squared stretch factors of the map along its principal directions. A spectrum spread geometrically over decades, a **sloppy** one
([TERM-tmptiim0](TERM-tmptiim0.md)), is the local form; the hyperribbon is the global form,
in which the manifold's extent, bounded by where parameters run to their
limits, follows a hierarchy of the same kind. That the two hierarchies
agree, width ≈ singular value of J ≈ √λ (not 1/√λ), is the authors'
finding under conditions, not an identity: observed in one
eight-parameter model in 2010; in 2011 exact for polynomial fitting on a
ball, within √(2/M) for exponentials in a continuum limit, and numerical for
a sum of exponentials and a 4-4-2 tanh network, all in natural or log
units from a central point; and failing in magnitude for the PC12 model,
whose widths are "smaller by several orders of magnitude" with the same
spacing ([THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md)). The local spectrum alone is not intrinsic: "one
can always reparametrize the manifold to make the metric at a point any
symmetric, positive definite matrix" ([LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), p. 6). Their reason
for the geometric fall is separate from the spectrum: fitting as
interpolation of an analytic function, each cross-section "thinner than
the last by a roughly constant factor" ∆, spacing over a radius of
convergence; a ratio-test heuristic, argued for one independent variable
and extended "in some multidimensional sense" ([THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md),
[THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md)). The stiff directions are usually combinations of parameters,
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
   ([THEORY-774](../theory.d/THEORY-774.md)), and the critical Ising model's irrelevant directions fall
   by up to six decades under decimation while the field and the
   T_c gradient stay ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-742](../theory.d/THEORY-742.md)).
2. *Regular in the interior, singular at the edges.* The local reading
   needs a Fisher matrix of full rank where it is evaluated. The sources
   make the boundaries singular: "Model boundaries correspond to points on
   the manifold where the metric is singular" ([LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), p. 10),
   usually where parameters run to 0 or ∞ (in log parameters, all at
   infinity), sometimes on finite fold lines such as two equal rates
   ([CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md)). So the widths are measured across a regular interior
   between singular edges. At a singular point, where it loses
   rank, the widths do not shrink smoothly to zero along a direction; the
   manifold folds or pinches, and the Bayesian count of effective
   parameters is set by the learning coefficient rather than by the
   spectrum ([THEORY-087](../theory.d/THEORY-087.md), [THEORY-1253](../theory.d/THEORY-1253.md)). How the two pictures meet is the
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
  coarse-graining are the relevant ones ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-742](../theory.d/THEORY-742.md)), but
  stiffness depends on the measurement and coordinates and relevance on a
  fixed point and a scale map (A19 §5). This caution is A's and the
  record's, not the review's: Transtrum and colleagues say the Ising
  model develops stiff directions "along precisely those parameter
  combinations deemed 'relevant' under the renormalization group"
  ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md), §V). A19 §5's table gives critical
  exponents as the rates at which perturbations "grow or shrink under
  rescaling"; for the Fisher eigenvalues the record's reading has the
  rate b^(2y−d) per step, with the dimension d in it, not b^y
  ([THEORY-777](../theory.d/THEORY-777.md)), and the exact transfer of the metric needs the
  renormalized Hamiltonian to stay in the family ([THEORY-742](../theory.d/THEORY-742.md)).
- **Not a count of parameters.** Neither a hyperribbon's dimension nor
  its number of "wide" directions is fixed: how many directions a data set
  resolves grows with the data ([CLAIM-tmpj0k4q](../claims.d/CLAIM-tmpj0k4q.md)), and which of several
  effective dimensions is meant is open ([QUESTION-tmpzlagu](../questions.d/QUESTION-tmpzlagu.md)).

## Sources

The term and the geometry: Transtrum, Machta and Sethna 2010 and 2011
([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md)), and the review by Transtrum and colleagues
2015 ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md)) and by Quinn and colleagues 2023 ([LIT-tmp0fpti](../literature.d/LIT-tmp0fpti.md)), the
work A19 links. The method of reducing a model along its thin directions
to the manifold's boundary, which A19 §4 names: Transtrum and Qiu 2014
([LIT-tmpdz70v](../literature.d/LIT-tmpdz70v.md)). The empirical base in systems biology: Gutenkunst and
colleagues 2007 ([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md)). The two papers and the 2015 review were
read on 2026-11-21 ([NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md), [NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md), [NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md)) and filed
as [THEORY-tmpkoje5](../theory.d/THEORY-tmpkoje5.md), [THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md) and [THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md); the 2023 review,
the reduction method and the survey are Deferred and unread. The
definition rests on those readings, on A's wording and on the record's
readings of [THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md) and [THEORY-742](../theory.d/THEORY-742.md).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

Read in [NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md), [NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md) and [NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md); the corrections are
made in place above (version 2). What the readings support and qualify:

- **Supported:** the shape, each width "thinner than the last by a roughly
  constant factor"; "no sharp line", the 2011 paper's "no clean separation
  between important (stiff) and irrelevant (sloppy) direction" and the
  review's "not a well-defined boundary between the stiff and sloppy
  combinations"; condition 1, since the 2011 paper scales residuals by
  their errors and its ratio ∆ "will depend on the model and the data being
  fit", and the review's hopping model is a "hyper-blob" after one step
  and a hyper-ribbon after many.
- **Qualified:** the tie of widths to the spectrum is empirical and
  conditional (natural or log units, a central point; it fails in magnitude
  for PC12); the widths argument is a heuristic for one independent
  variable; "over many decades" is about four decades of width in their
  examples (eight of eigenvalue).
- **Revised:** condition 2. The boundaries are where the metric is
  singular, mostly at infinite parameter values, sometimes on finite fold
  lines; the interior is regular.
- **Not the sources':** the caution against equating stiffness with RG
  relevance (A19 §5), and the separation from a power law in event sizes.
- **Their scope:** the 2010 letter excludes "Multiparameter models whose
  parameters are individually measured by the data" and models "with
  sensitive, chaotic dependence on parameters".
