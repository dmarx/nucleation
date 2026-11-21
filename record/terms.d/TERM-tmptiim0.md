---
status: Proposed
title: 'sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads over many decades with no gap that separates the parameter combinations that matter from those that do not; a graded property, distinct from ill-conditioning, from singularity and from a power-law spectrum'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Edited in place, the term having been filed in this pull request, after
    the readings of its sources: LIT-tmpd3swn (NOTE-tmpamhd2), LIT-tmpzkxka
    (NOTE-tmpzxtnv) and LIT-tmpm1tji (NOTE-tmphbpab). The title and the
    definition stand. Added: what the sources say sloppiness is, that they
    put its invariant content in the model manifold's widths, that widths
    match √λ only in natural or log units, from a central point and under
    conditions, and that their "evenly spaced" / "fixed factor" differs from
    the widening gaps this term's own check found (both kept). Revised:
    "What it is not: singular", since the sources make the manifold's
    boundaries the points where the metric is singular, so the sloppy
    interior is regular and its edges singular. The separations from
    ill-conditioning and from a power-law spectrum are marked as the
    record's, and the statements that the sources were unread are replaced.
tags:
- information-geometry
- mathematical-statistics
- model-comparison
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
draws_on:
- THEORY-tmpgsgka
- THEORY-tmpd7a4j
- THEORY-tmpkoje5
- THEORY-774
- THEORY-777
- THEORY-742
summary: >-
  At the owner's suggestion of 2026-11-21, after the filing of the
  exchange "Rich Get Richer Power Laws": "a TERM for the mathematical
  (information geometric?) sense of 'sloppy' might be merited". The record
  used the word in that sense in several entries ([TERM-tmp5z2du](TERM-tmp5z2du.md),
  [TERM-tmpnxjq4](TERM-tmpnxjq4.md), [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md), [CLAIM-tmpficzj](../claims.d/CLAIM-tmpficzj.md), [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)) and in
  its readings of sloppy spectra ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)), without
  defining it. A model is sloppy, at a parameter point and for a given
  observation design, when the eigenvalues of its Fisher information,
  in a declared chart (conventionally the logarithms of its bare
  parameters), spread over many decades, and no gap among them marks off
  the combinations that matter from those that do not. The term separates
  this from four neighbours: ill-conditioning (one ratio, which a single
  gap can produce), singularity (a zero eigenvalue on a stratum), the
  hyperribbon (the chart-free shape of the predictions, [TERM-tmp5z2du](TERM-tmp5z2du.md)),
  and a power-law spectrum (a sloppy spectrum falls by roughly a constant
  factor per rank, so it covers decades in proportion to the number of
  parameters). Its job is to let the record's entries on sloppiness,
  singular learning and effective dimension say which of these they mean.
  The source of the concept is Sethna and colleagues: LIT-tmpd3swn,
  LIT-tmpzkxka and LIT-tmpm1tji, read on 2026-11-21 (THEORY-tmpkoje5,
  THEORY-tmpgsgka, THEORY-tmpd7a4j), and LIT-tmpsqbr9, unread. They define
  sloppiness by example and by an eigenvalue spread "roughly evenly spaced"
  in log, and put its chart-free content in the widths of the model
  manifold; version 2 records what they say. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmp5z2du TERM-tmpnxjq4 CLAIM-tmpcgvcp CLAIM-tmpficzj CLAIM-tmpcg4uu CLAIM-tmpj0k4q CLAIM-tmpym2vz THEORY-777 LIT-tmpsqbr9 TERM-tmpyi882 — Proposed, Deferred or new; the entries this term defines a word for, and the unread works it comes from -->
<!-- inactive-ok-file: ARG-tmpddtmr CASE-tmpb2gly THEORY-tmpd7a4j THEORY-tmpgsgka THEORY-tmpkoje5 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# TERM-tmptiim0: sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads over many decades with no gap that separates the parameter combinations that matter from those that do not; a graded property, distinct from ill-conditioning, from singularity and from a power-law spectrum

## Definition

Let a model map parameters θ ∈ ℝᵏ to predictions, observed with noise under a fixed design (which quantities, at which times or conditions, with what error). Its Fisher information at θ is g(θ); for least squares with unit noise, g = JᵀJ, with J the Jacobian of the predictions.

- **Sloppy.** The model is *sloppy* at θ, for that design, when the eigenvalues λ₁ ≥ … ≥ λₖ > 0 of g span many decades and are spread across them, each typically a decade or more below the last, with no single gap that splits them into a few that matter and a remainder that does not.
- **Stiff and sloppy directions.** The eigenvectors of the large eigenvalues are *stiff* directions; those of the small ones are *sloppy* directions. The adjective on the model refers to the whole graded spectrum, not to having some sloppy directions.
- **Graded.** There is no threshold in the concept. How many decades, and how even, are said when it matters. The sources give none either: the review's only cut is practical, eigenvalues below 1 in units of the measurement error ([NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md)). Their examples span six to eight decades: eight in the letter's one eight-parameter model ([NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md)), six to seven in the review's five spectra; [LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md) (unread) is the systems-biology survey behind them.
- **Relative to a chart.** Fisher eigenvalues are not invariant under reparametrization: under θ = Aφ the metric becomes Aᵀ g A. The convention is the logarithms of the bare parameters, so that the eigenvalues compare relative changes. A claim that a model is sloppy names its chart, or uses that convention.
- **Relative to a design.** More data or a different design can stiffen a direction. Sloppiness is of a model as observed, not of a model alone ([CLAIM-tmpj0k4q](../claims.d/CLAIM-tmpj0k4q.md): the number of resolved directions grows with data).

**Checked** with `python3 -I`, scratchpad script `sloppy_check.py`. A sum of k exponentials, with log-rate parameters, observed at 40 times with unit noise:
- k = 3: the eigenvalues span 1.9 decades;
- k = 5: 5.0 decades;
- k = 7: 8.8 decades.

The successive gaps are 0.6 to 2.3 decades and widen down the spectrum, so "spread" does not mean equally spaced. The sources say otherwise of their models: eigenvalues "whose logarithms tend to be evenly spaced" ([LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md), p. 3), each combination "less important than the previous by a fixed factor" ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md), §I). Both are kept: "roughly" is theirs, and a sum of exponentials sampled at 40 times, in this check, falls faster than geometrically down the spectrum. The definition asks for spread with no gap, not for even spacing. The same five-exponential model spans 6.1 decades in the chart of the bare rates, and 8.4 after rescaling three of them by 1, 10 and 100. So the count of decades depends on the chart.

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

What the sources say, and what version 2 changed because of it.

- **Defined by example and by spectrum.** The 2010 letter does not define
  sloppiness; it names as "sloppiness" the eigenvalues of g = JᵀJ forming
  "a hierarchy, spanning eight orders of magnitude" in one model
  ([NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md)). The 2011 paper: "Sloppiness is the property that the
  behavior of the model responds very strongly to only a few combinations
  of parameters", with "no clean separation between important (stiff) and
  irrelevant (sloppy)" directions ([NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md)). The 2015 review: "Sloppy
  is the term used to describe a class of complex models exhibiting large
  parameter uncertainty when fit to data" ([NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md)).
- **The spectrum is not intrinsic; the widths are.** "one can always
  reparametrize the manifold to make the metric at a point any symmetric,
  positive definite matrix" (2011, p. 6); "the eigenvalues of the FIM are
  not sufficient to make this conclusion" (2015, §III). The sources put
  the chart-free content of sloppiness in the model manifold: bounded, its
  geodesic widths falling roughly geometrically, the hyperribbon
  ([TERM-tmp5z2du](TERM-tmp5z2du.md)). In their usage sloppiness proper is that global shape,
  and the eigenvalue spread in log parameters is its local symptom. This
  term keeps the local, chart-relative definition, which is what a
  computation at a point gives, and marks the chart; the hyperribbon is the
  invariant face.
- **Widths ≈ √λ, under conditions.** The widths are geodesic lengths from a
  central point along the metric's eigendirections. They approximate the
  Jacobian's singular values, √λ, in natural or log units: exactly for
  polynomial fitting on a ball, within √(2/M) for exponentials in a
  continuum limit, numerically for a sum of exponentials and a 4-4-2 tanh
  network; not in magnitude for the PC12 model, started near a corner
  (2011, §III). The review: "when we use dimensionless model parameters
  (e.g. log-parameters), the square roots of the FIM eigenvalues are a
  reliable approximation to the widths". The 2010 letter observes the
  match in one model. It is √λ, not 1/√λ: 1/√λ is the width of the ellipse
  of good fits in parameter space (2015, parameter-space figure).
- **Ill-conditioning.** The review says the FIM of a typical sloppy model
  "is extremely ill-conditioned" (§VII) and draws no line between the two.
  The separation below is the record's.

## What it is not

- **Ill-conditioned.** The condition number λ₁/λₖ is one ratio. A spectrum (1, 0.9, 0.8, 0.7, 10⁻⁸) is badly conditioned but not sloppy: four eigenvalues sit within 0.15 decades and one gap of 7.9 decades does all the work (checked). It has a clean split into what matters and what does not, which is what sloppiness lacks.
- **Singular.** A sloppy model has g invertible at the point where it is evaluated, so near that point every direction is identified given enough data. A singular model has a zero eigenvalue on a stratum, and its learning coefficient differs from d/2 ([TERM-tmpnxjq4](TERM-tmpnxjq4.md), senses 4 and 5; [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md)). But the sources tie the two at the edges: "Model boundaries correspond to points on the manifold where the metric is singular" (2011, p. 10). Usually the boundaries lie where parameters run to 0 or ∞, and in log parameters all of them lie at infinity; some lie at finite parameters, on fold lines such as θ₁ = θ₂ in a sum of two exponentials, where "No parameters were at extreme values, but the model behavior was nonetheless singular" (2011, p. 7; generic when the data number fewer than twice the parameters). So the sloppy interior is regular and its edges are singular: "regular, not singular" is a property of the point in the interior, not of the whole model, and a parameter pushed toward an edge can run to infinity rather than be identified (the sources' "evaporation"). The two meet near a finite stratum, where a sloppy eigenvalue goes to zero with the squared distance ([CASE-tmpb2gly](../cases.d/CASE-tmpb2gly.md)), and at finite n, where an unresolved sloppy direction counts like a flat one ([CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md); [ARG-tmpddtmr](../arguments.d/ARG-tmpddtmr.md) weighs what the edges do to [CLAIM-tmpcgvcp](../claims.d/CLAIM-tmpcgvcp.md)).
- **A hyperribbon.** The hyperribbon is the shape of the set of predictions, whose widths fall roughly geometrically ([TERM-tmp5z2du](TERM-tmp5z2du.md)). That shape does not depend on the chart; the Fisher spectrum does. Sloppiness is the parameter-space face, the hyperribbon the prediction-space face. Their connection, that the widths follow √λ, is Transtrum, Machta and Sethna's: observed in one model in 2010, shown exactly for polynomials and numerically for a few models in 2011, and conditional on units and on the point measured from ([THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md)).
- **A power-law spectrum** (a separation the record makes; the sources do not discuss it). A sloppy spectrum falls by roughly a constant factor per rank: geometric in the index. A power law in rank, λₙ ∝ n^(−α), falls ever more slowly. The checked contrast:

  | Eigenvalues | Geometric (ratio ½) covers | Power law (α = 2) covers |
  |---|---|---|
  | 10 | 2.7 decades | 2.0 decades |
  | 50 | 14.8 decades | 3.4 decades |
  | 200 | 59.9 decades | 4.6 decades |

  So a sloppy model with many parameters spans decades in proportion to the number of parameters, and a power-law spectrum spans them in proportion to the log of that number. The participation ratio behaves differently under each ([CLAIM-tmpym2vz](../claims.d/CLAIM-tmpym2vz.md) for the power-law case). Neither is "scale-free" in the sense of [TERM-tmpyi882](TERM-tmpyi882.md) without further conditions.
- **Unimportant.** A sloppy direction is one along which the predictions, as observed, change little. It says nothing of whether a task depends on it ([TERM-tmpnxjq4](TERM-tmpnxjq4.md)).

## Sources

- The concept and the word are Sethna and colleagues'. The systems-biology survey is Gutenkunst and colleagues ([LIT-tmpsqbr9](../literature.d/LIT-tmpsqbr9.md), unread). The geometry is Transtrum, Machta and Sethna 2010 and 2011 ([LIT-tmpd3swn](../literature.d/LIT-tmpd3swn.md), [LIT-tmpzkxka](../literature.d/LIT-tmpzkxka.md); [THEORY-tmpkoje5](../theory.d/THEORY-tmpkoje5.md), [THEORY-tmpgsgka](../theory.d/THEORY-tmpgsgka.md)), and the review is Transtrum and colleagues 2015 ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md); [THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md)). The three were read on 2026-11-21 ([NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md), [NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md), [NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md)); version 2 records what they change.
- The record's readings of sloppy spectra are [THEORY-774](../theory.d/THEORY-774.md) (the hopping model, whose Fisher metric is given exactly), [THEORY-777](../theory.d/THEORY-777.md) (decimated critical Ising) and [THEORY-742](../theory.d/THEORY-742.md) (the Fisher information a coarse-graining loses).
- The separations from ill-conditioning, from a power-law spectrum and from the chart are the assistant's, checked as above.
