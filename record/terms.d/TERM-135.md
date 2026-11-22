---
number: 135
status: Proposed
formerly:
- TERM-tmp5z2du
title: 'hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum'
version: 4
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Edited in place, the term having been filed in this pull request, after
    the readings of LIT-2977 (NOTE-2240), LIT-3009
    (NOTE-2247) and LIT-2994 (NOTE-2242). The title and the
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
- version: 3
  date: '2026-11-21'
  note: >-
    Edited in place after the readings of LIT-2979 (Transtrum & Qiu 2014,
    NOTE-tmphbnqd), LIT-2999 (Gutenkunst et al. 2007, NOTE-tmp1feoo) and
    LIT-2960 (Amari, Park & Ozeki 2006, NOTE-tmptlwkf). The title and the
    definition stand. Added: the manifold boundary approximation needs a
    hierarchy of edges and corners as well as of widths, so a hyperribbon
    without corners, which the definition admits, is a case the method
    cannot use (the paper's ellipsoid); and condition 2 is limited to the
    sloppy-model literature's models, since in networks the singular sets
    are interior. The statements that the reduction method and the survey
    are unread are replaced.
- version: 4
  date: '2026-11-22'
  note: >-
    Edited in place after the reading of LIT-2958 (Quinn, Abbott,
    Transtrum, Machta & Sethna 2023, NOTE-tmp3keyy, THEORY-tmpx26x7). The
    title and the definition stand. Added: the rigorous bound for
    least-squares models smooth in their experimental control, which the
    review restates from Quinn, Wilber, Townsend & Sethna 2019
    (LIT-tmpmksrk, Deferred), beside the 2011 ratio-test heuristic; the
    review's joint definition, eigenvalues and widths both hierarchical;
    and, under condition 2, the review's own singular models "that are not
    strictly boundaries, such as a the tip of a cone". The Sources line
    calling the 2023 review unread is replaced.
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
- THEORY-2155
- THEORY-2156
- THEORY-2154
- THEORY-774
- THEORY-777
- THEORY-742
- THEORY-tmpt1tw7
- THEORY-tmpx26x7
summary: >-
  The shape the exchange "Rich Get Richer Power Laws" gives, at A19 §4,
  to the set of predictions a sloppy model can make: long in a few
  directions and thinner along each further one, the widths falling
  roughly geometrically, so there is no sharp line between the parameter
  combinations that matter and those that do not. The record held the
  sloppy Fisher spectra that produce it ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)) but had
  no word for the shape, which the exchange returns to from A38 on, where
  the owner ties it to Watanabe's stratification (U24). The term is from
  Transtrum, Machta and Sethna (LIT-2977, LIT-3009, read on
  2026-11-21 as THEORY-2156 and THEORY-2155, which corrected the
  definition in version 2: geodesic widths from a central point, width ≈ √λ
  under conditions, a heuristic argument); the
  conditions in the definition, and the separation from a power law in
  event sizes, are the assistant's checks of A's wording. The wording is
  A's (the other assistant in the exchange "Rich Get Richer Power Laws",
  A19); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the record's evidence for the critical-Ising spectrum -->
<!-- inactive-ok-file: THEORY-tmpx26x7 LIT-tmpmksrk — Proposed, Deferred or new; the 2023 review's reading and the 2019 paper it restates, filed 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-825 — filed with this term from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-302 TERM-140 THEORY-2154 THEORY-2155 THEORY-2156 THEORY-tmpt1tw7 THEORY-tmpks8pd THEORY-tmpbobud — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# TERM-135: hyperribbon: a model manifold whose widths across successive orthogonal directions fall roughly geometrically, the prediction-space face of a sloppy Fisher spectrum

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
hyper-ribbon" ([LIT-3009](../literature.d/LIT-3009.md), §III); the 2015 review writes "hyperribbon".
The **widths** are geodesic: the data-space length of a geodesic started
from a central point along an eigendirection of the metric, run until it
meets a boundary, or the length of a cross-section ([LIT-2977](../literature.d/LIT-2977.md), Fig. 3:
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
([TERM-140](TERM-140.md)), is the local form; the hyperribbon is the global form,
in which the manifold's extent, bounded by where parameters run to their
limits, follows a hierarchy of the same kind. That the two hierarchies
agree, width ≈ singular value of J ≈ √λ (not 1/√λ), is the authors'
finding under conditions, not an identity: observed in one
eight-parameter model in 2010; in 2011 exact for polynomial fitting on a
ball, within √(2/M) for exponentials in a continuum limit, and numerical for
a sum of exponentials and a 4-4-2 tanh network, all in natural or log
units from a central point; and failing in magnitude for the PC12 model,
whose widths are "smaller by several orders of magnitude" with the same
spacing ([THEORY-2155](../theory.d/THEORY-2155.md)). The local spectrum alone is not intrinsic: "one
can always reparametrize the manifold to make the metric at a point any
symmetric, positive definite matrix" ([LIT-3009](../literature.d/LIT-3009.md), p. 6). Their reason
for the geometric fall is separate from the spectrum: fitting as
interpolation of an analytic function, each cross-section "thinner than
the last by a roughly constant factor" ∆, spacing over a radius of
convergence; a ratio-test heuristic, argued for one independent variable
and extended "in some multidimensional sense" ([THEORY-2155](../theory.d/THEORY-2155.md),
[THEORY-2154](../theory.d/THEORY-2154.md)). For least-squares models smooth in their experimental
control there is now a rigorous bound, restated in the 2023 review from
Quinn, Wilber, Townsend and Sethna 2019 ([LIT-tmpmksrk](../literature.d/LIT-tmpmksrk.md), Deferred, unread):
"The proof relies on the smoothness of the predictions as the
experimental controls ... are varied"; with Taylor coefficients bounded by
one, the manifold lies within ε_N = T^N/(1−T) of a hyper-parallelepiped
skewed by the Vandermonde matrix, and in the Chebyshev form it "is
constrained by a hyper-ellipsoid whose j-th largest principal axis length
is bounded by" ρ^(−j) ([LIT-2958](../literature.d/LIT-2958.md), §3; [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)). The review calls
ρ^(−j) "a power law"; it is geometric in j, as the same paragraph's
"geometric decay" says. The review also makes the definition joint:
"We call a model sloppy, and the model manifold a hyperribbon, if the
parameter-space eigenvalues and prediction-space widths are hierarchical"
(§2). The stiff directions are usually combinations of parameters,
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
   the manifold where the metric is singular" ([LIT-3009](../literature.d/LIT-3009.md), p. 10),
   usually where parameters run to 0 or ∞ (in log parameters, all at
   infinity), sometimes on finite fold lines such as two equal rates
   ([CASE-302](../cases.d/CASE-302.md)). So the widths are measured across a regular interior
   between singular edges. At a singular point, where it loses
   rank, the widths do not shrink smoothly to zero along a direction; the
   manifold folds or pinches, and the Bayesian count of effective
   parameters is set by the learning coefficient rather than by the
   spectrum ([THEORY-087](../theory.d/THEORY-087.md), [THEORY-1253](../theory.d/THEORY-1253.md)). How the two pictures meet is the
   owner's question at U24, left to the filing of that turn. The
   condition is the sloppy-model literature's, for its own models. In
   neural networks the points of rank loss lie inside parameter space at
   finite values, a unit switched off or two units coinciding, and in the
   space of distributions at a cone apex, not at an edge ([LIT-2960](../literature.d/LIT-2960.md),
   [THEORY-tmpbobud](../theory.d/THEORY-tmpbobud.md)), so a network near such a set is not a regular
   interior between singular edges. The 2023 review loosens the condition
   itself: "model manifolds may have singular models that are not
   strictly boundaries, such as a the tip of a cone. These singularities
   often correspond to useful reduced models" ([LIT-2958](../literature.d/LIT-2958.md), §4,
   [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)), so even in the sloppy-model literature a singular
   point can lie inside the manifold, as Amari's cone apex does.

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
  ([LIT-2994](../literature.d/LIT-2994.md), §V). A19 §5's table gives critical
  exponents as the rates at which perturbations "grow or shrink under
  rescaling"; for the Fisher eigenvalues the record's reading has the
  rate b^(2y−d) per step, with the dimension d in it, not b^y
  ([THEORY-777](../theory.d/THEORY-777.md)), and the exact transfer of the metric needs the
  renormalized Hamiltonian to stay in the family ([THEORY-742](../theory.d/THEORY-742.md)).
- **Not enough for boundary reduction.** A hierarchy of widths is not a
  hierarchy of edges. Transtrum and Qiu's reduction method needs "the
  model manifold be bounded with a hierarchy of boundaries", and gives the
  counter-example: polynomial fitting with a bounded coefficient vector is
  "an ellipsoid with a hierarchy of widths but without a hierarchy of
  edges; i.e., there are no corners" ([LIT-2979](../literature.d/LIT-2979.md), para. 21). Such a manifold
  is a hyperribbon by this definition, and the method cannot use it
  ([THEORY-tmpt1tw7](../theory.d/THEORY-tmpt1tw7.md)).
- **Not a count of parameters.** Neither a hyperribbon's dimension nor
  its number of "wide" directions is fixed: how many directions a data set
  resolves grows with the data ([CLAIM-825](../claims.d/CLAIM-825.md)), and which of several
  effective dimensions is meant is open ([QUESTION-517](../questions.d/QUESTION-517.md)).

## Sources

The term and the geometry: Transtrum, Machta and Sethna 2010 and 2011
([LIT-2977](../literature.d/LIT-2977.md), [LIT-3009](../literature.d/LIT-3009.md)), and the review by Transtrum and colleagues
2015 ([LIT-2994](../literature.d/LIT-2994.md)) and by Quinn and colleagues 2023 ([LIT-2958](../literature.d/LIT-2958.md)), the
work A19 links. The method of reducing a model along its thin directions
to the manifold's boundary, which A19 §4 names: Transtrum and Qiu 2014
([LIT-2979](../literature.d/LIT-2979.md)). The empirical base in systems biology: Gutenkunst and
colleagues 2007 ([LIT-2999](../literature.d/LIT-2999.md)). The two papers and the 2015 review were
read on 2026-11-21 ([NOTE-2240](../notes.d/NOTE-2240.md), [NOTE-2247](../notes.d/NOTE-2247.md), [NOTE-2242](../notes.d/NOTE-2242.md)) and filed
as [THEORY-2156](../theory.d/THEORY-2156.md), [THEORY-2155](../theory.d/THEORY-2155.md) and [THEORY-2154](../theory.d/THEORY-2154.md); the reduction
method and the survey were read the same day ([NOTE-tmphbnqd](../notes.d/NOTE-tmphbnqd.md),
[NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)) and filed as [THEORY-tmpt1tw7](../theory.d/THEORY-tmpt1tw7.md) and [THEORY-tmpks8pd](../theory.d/THEORY-tmpks8pd.md); the
2023 review was read on 2026-11-22 ([NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md)) and filed as
[THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md), and the 2019 paper whose bound it restates is Deferred
and unread ([LIT-tmpmksrk](../literature.d/LIT-tmpmksrk.md)). The
definition rests on those readings, on A's wording and on the record's
readings of [THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md) and [THEORY-742](../theory.d/THEORY-742.md).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

Read in [NOTE-2240](../notes.d/NOTE-2240.md), [NOTE-2247](../notes.d/NOTE-2247.md) and [NOTE-2242](../notes.d/NOTE-2242.md); the corrections are
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

## Note of 2026-11-21: Transtrum & Qiu (2014), Gutenkunst et al. (2007) and Amari, Park & Ozeki (2006), read

- **Transtrum and Qiu ([NOTE-tmphbnqd](../notes.d/NOTE-tmphbnqd.md)) support the definition**: "the
  manifold is bounded with a hierarchy of widths, qualitatively described
  as a hyper-ribbon" (para. 8), spelt with the hyphen. **They add** that
  widths are not enough for their method, which needs nested edges and
  corners; an ellipsoid has the widths and "no corners" (para. 21). Made
  in place above, under "What it is not" (version 3). The reduced model
  sits at a "hypercorner", and after reduction "the lack of small
  eigenvalues" shows the reduced model is no longer sloppy.
- **Gutenkunst and colleagues ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)): background.** The survey
  has no model manifold and no widths; its ellipsoids are in parameter
  space, axes ∝ 1/√λ (Fig. 1A). It is the empirical base the definition's
  sources cite, and accurately.
- **Amari, Park and Ozeki ([NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md)) limit condition 2** to the
  sloppy-model literature's models: network singularities are interior,
  at finite parameters (made in place above).

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

Read in [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md) ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)); the additions are made in place
above (version 4).

- **Supported:** the definition, "a ribbon is much longer than it is
  wide, and much wider than it is thick" (§2); widths measured from a
  central point; condition 1, in the review's own words: "sloppiness is a
  property both of the scientific model and the predictions of interest"
  (§8.2), and the hopping model after one step "is not a hyper-ribbon"
  (§6.2).
- **Added: a rigorous bound**, for least-squares models smooth in their
  control variable, restated from the 2019 paper ([LIT-tmpmksrk](../literature.d/LIT-tmpmksrk.md), which
  would meet the review THEORY's promote_when once read). The 2011
  argument remains the heuristic for other models; for general
  probabilistic models the review says "we do not yet have an explanation
  for this in general, except for ... exponential families" (§8.2).
- **Added: interior singularities** in the sloppy-model literature itself
  ("the tip of a cone"), a point the term had credited only to Amari, Park
  and Ozeki ([LIT-2960](../literature.d/LIT-2960.md)).
- **Qualified, for the "Not a count of parameters" bullet:** a hyperribbon
  gives a low-dimensional description only "if many of its widths are
  small compared to the precision of the predictions demanded"; ΛCDM is
  sloppy and fully determined (§2).
- **On "Not RG relevance":** the review again connects "stiff and sloppy
  directions ... with relevant and irrelevant eigendirections" (abstract);
  its flow d log(ds²)/db = −D + 2y_i for irrelevant directions matches
  [THEORY-777](../theory.d/THEORY-777.md)'s b^(2y−d). The caution stays the record's.
