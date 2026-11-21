---
status: Read
title: 'Transtrum, Machta & Sethna 2011 — the geometry of nonlinear least squares: widths, boundaries and curvature of sloppy model manifolds'
paper: LIT-tmpzkxka
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the arXiv preprint 1010.1449v1 (7 October 2010, the only version),
    41 pp., fetched 2026-11-21 from arxiv.org (HTTP 200), the authors'
    manuscript of the paper published as Phys. Rev. E 83, 036701 (2011),
    doi:10.1103/PhysRevE.83.036701 (metadata from the arXiv API, no email
    address sent); the journal text was not sought and may differ. Text
    extracted with pdftotext. Read in full: §§I–IX, every figure and table
    caption, Appendices A–B and footnotes [70]–[72]; the reference list
    skimmed. Page numbers are the preprint's. Read by a reader subagent;
    filed by a second one, which rechecked every quote used here against
    the extraction.
date: '2026-11-21'
summary: >-
  The long treatment: a sloppy model's manifold is a bounded hyper-ribbon
  whose widths fall by a roughly constant factor, argued from polynomial
  interpolation; in natural or log units, from a central point, the
  geodesic widths match the Jacobian's singular values (≈ √λ) for a sum of
  exponentials and a 4-4-2 tanh network, but not in magnitude for PC12.
  Boundaries are where the metric JᵀJ is singular, usually at parameters 0
  or ∞, also on finite fold lines (equal rates); with fewer data than twice
  the parameters, finite singular points are generic. Fitting fails at
  boundaries; geodesic acceleration and delayed gratification help.
---
<!-- inactive-ok-file: ARG-tmp97cwb ARG-tmpddtmr ARG-tmpj0r42 ARG-tmpjx3ww ARG-tmpmvc5e ARG-tmpv3nqz CASE-tmpb2gly CLAIM-tmpa8hb2 CLAIM-tmpcg4uu CLAIM-tmpcgvcp CLAIM-tmpficzj CLAIM-tmpj0k4q CLAIM-tmpnu4ar CLAIM-tmppkdjz LIT-tmp0z602 TERM-tmp5z2du TERM-tmptiim0 THEORY-777 THEORY-tmpgsgka — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# NOTE-tmpzxtnv: Transtrum, Machta & Sethna 2011 — the geometry of nonlinear least squares: widths, boundaries and curvature of sloppy model manifolds

## Contribution

The global, parametrization-independent geometry of sloppiness: widths
and curvatures of the model manifold, argued from interpolation theory and
checked numerically; boundaries identified with singularities of the
metric; parameter-effects curvature shown to dominate extrinsic curvature;
Gauss–Newton and Levenberg–Marquardt read as Euler steps of geodesic flow;
geodesic acceleration and "delayed gratification" as cheap improvements
to Levenberg–Marquardt. It continues LIT-tmpd3swn.

## Key insight

The local spectrum of JᵀJ is not intrinsic, but the widths of the model
manifold are, and for sloppy models they form a geometric series that the
spectrum happens to estimate when parameters are in natural units. The
manifold's edges are where the metric degenerates, mostly at parameters
running to 0 or ∞, sometimes at finite folds.

## Assumptions

- Gaussian independent residuals scaled by their errors (§I, Eq. 1); then
  JᵀJ is the Fisher information (App. A). M data points, N parameters,
  M > N.
- Widths argument: an analytic model whose higher derivatives "do not grow
  too fast" (a radius of convergence R), sampling points "not too widely
  spaced", n "sufficiently large".
- Width–singular-value agreement: parameters in natural or log units, and
  the measuring point central, not near a boundary (§III, §VII D).
- Geodesic = Gauss–Newton path: extrinsic flatness.

## Key results

- **Sloppiness defined** (§I p. 2): "Sloppiness is the property that the
  behavior of the model responds very strongly to only a few combinations
  of parameters", stiff and sloppy. At the best fit the Hessian's
  eigenvalues span many orders of magnitude, "whose logarithms tend to be
  evenly spaced" (p. 3); Fig. 2: "there is no clean separation between
  important (stiff) and irrelevant (sloppy) direction in parameter
  space." Linear polynomial fitting, with its Hilbert-matrix Hessian, is
  listed as sloppy (Fig. 2b).
- **The spectrum is not intrinsic** (§II p. 6): "one can always
  reparametrize the manifold to make the metric at a point any symmetric,
  positive definite matrix."
- **The widths argument** (§III pp. 7–8, Eq. 13): the range left after
  fixing n points shrinks by δfₙ₊₁/δfₙ ≈ (t − tₙ₊₁)/R: "Each cross section is
  thinner than the last by a roughly constant factor ∆ = δt/R ... We
  describe the shape of a model manifold with such a hierarchy as a
  hyper-ribbon." §VII D (p. 25): Wₙ ∼ W₀∆ⁿ, ∆ from 0.1 to 0.9 across
  seventeen systems-biology models.
- **Widths ≈ singular values** (§III pp. 8–9, Fig. 6). Exact for
  polynomial fitting with Σθ² ≤ 1 (a hyper-ellipse with the Vandermonde
  singular values as axes); for exponentials in a continuum limit,
  "within the relatively small factor" √(2/M); numerically, for an
  eight-parameter sum of exponentials in log parameters and a 4-4-2 tanh
  network with the weights as parameters, the widths "nicely track the
  singular values" over about four decades. Widths are geodesic lengths
  from a central point along a metric eigendirection to a boundary. For
  PC12 the geodesic widths are "smaller by several orders of magnitude",
  although "the spacing between geodesic widths is the same as the
  spacing between the singular values"; the authors blame a start near a
  hyper-corner. "This depends on the choice of parameters and the
  placement of the best fit" (p. 25). So widths ≈ √λ, not 1/√λ.
- **Why models are sloppy** (§III p. 10): "Whenever there are more
  parameters than effective degrees of freedom among the data points";
  "We view most multiparameter fits as a type of multidimensional
  interpolation."
- **Boundaries** (§II pp. 6–7, §III p. 10, §IV p. 11). Of the two
  exponentials on 0 ≤ θ₁, θ₂ ≤ ∞: three boundaries come from parameters at
  their bounds; "The one exception to this is the fold line, which
  corresponds to when the parameters are equal". "Model boundaries
  correspond to points on the manifold where the metric is singular.
  Typical boundaries occur when parameters are near their extreme values
  (such as ±∞ or zero), where the model becomes unresponsive". Of the
  fold: "No parameters were at extreme values, but the model behavior was
  nonetheless singular." By counting the linear dependence of the M-vectors
  ∂μr (Eq. 16), "if M < 2N there will exist nontrivial singular points of
  the metric at non-extreme values of the parameters"; for M > 2N not
  generically, except near-singular "to machine precision". "The
  parameter space picture has the advantage that boundaries typically do
  not exist (i.e. they lie at parameter values equal to ∞)"; in log
  parameters all of them do. Network metric singularities are equated
  with boundaries, citing Amari, Park and Ozeki (LIT-tmp0z602).
- **Evaporation and noise** (§III, §VII G): parameters drift to extreme
  values; "for a given model, the errors must be smaller than the
  narrowest width for there to be no evaporated parameters" (pp. 29–30);
  the expected number of unevaporated parameters grows as log(W₀/σ)/|log ∆|
  (Eq. 37).
- **Curvature** (§VII D): parameter-effects curvature far exceeds
  extrinsic, by a factor of about 10⁵ in Fig. 20; "the entire structure of
  the manifold can be summarized by three numbers", W₀, ∆ and N.
- **Algorithms** (§VIII): "The Levenberg algorithm is simply the
  Gauss-Newton method on the model graph instead of the model manifold";
  geodesic acceleration costs one extra residual evaluation; on the
  four-exponential test, success 33% → 65%, mean Jacobian evaluations
  2002 → 258. "The results presented in this section do not constitute a
  rigorous comparison" (p. 36).

## Concepts

- **Model manifold, model graph, data space** — as in LIT-tmpd3swn.
- **Hyper-ribbon** — a bounded manifold whose widths form a geometric
  series with ratio ∆, spacing over radius of convergence.
- **Boundary** — a point of the manifold where the metric is singular.
- **Fold line** — a boundary at finite parameter values, where two
  parameters are equal.
- **Parameter evaporation** — parameters drifting to extreme values
  during a fit or at a noisy best fit.
- **Extrinsic and parameter-effects curvature** — after Bates and Watts.

## Connections

A continuation of LIT-tmpd3swn (NOTE-tmpamhd2); reviewed in LIT-tmpm1tji
(NOTE-tmphbpab). Cites Amari, Park and Ozeki 2006 (LIT-tmp0z602,
Deferred) for metric singularities in network training, and states that
Amari's natural-gradient flow reduces to the geodesic equation when all
nonlinearity is parameter-effects curvature (THEORY-082 holds Amari's
account).

## Bearing on the record

Filed as THEORY-tmpgsgka. Dated notes of 2026-11-21 on each entry below.

- **TERM-tmptiim0**, **TERM-tmp5z2du**: the corrections made in place
  (invariance in the widths; √λ under conditions; boundaries singular;
  "evenly spaced"; spelling).
- **CLAIM-tmpcg4uu**: its "What it does not say" inverted the paper's
  relation (widths ≈ √λ, not 1/√λ), corrected there; the fold line
  corroborates its edge half.
- **CLAIM-tmpcgvcp**: polynomial fitting, its separating example, is the
  paper's own sloppy example; the paper ties sloppiness to singularity at
  the boundaries. ARG-tmpddtmr.
- **CLAIM-tmpa8hb2**, **ARG-tmpj0r42**: boundaries are where the metric is
  singular; widths come from interpolation, not strata. ARG-tmp97cwb.
- **CASE-tmpb2gly**: the paper's toy model is the case's; θ₁ = θ₂ is its
  "fold line", singular at finite parameters.
- **CLAIM-tmpficzj**, **ARG-tmpmvc5e**: the paper applies the hyper-ribbon
  to a 4-4-2 tanh network (Fig. 6b), and its counting makes finite
  singular points generic when M < 2N. ARG-tmpv3nqz.
- **CLAIM-tmpnu4ar**: its gap (boundaries at infinity becoming strata) is
  the paper's log-coordinate and model-graph picture, not resolved by it.
- **ARG-tmpjx3ww**, **CLAIM-tmppkdjz**: widths are data-space distances in
  units of σ, and the spectrum depends on parametrization.
- **CLAIM-tmpj0k4q**, **QUESTION-tmpzlagu**: Eq. 37's count of unevaporated
  parameters, logarithmic in W₀/σ for a geometric series, is one more
  effective dimension.
- **THEORY-082**: parallel, as under Connections.
- **THEORY-774**, **THEORY-777**, **THEORY-742**: background; the general
  geometry their cases instantiate, with no coarse-graining here.

Nothing here is an instruction for machine-learning practice.

## Limitations

- The widths argument is a ratio-test heuristic ("roughly", "in some
  multidimensional sense"); universality rests on a few models
  (exponentials, polynomials, one 4-4-2 network, PC12).
- The width–singular-value match is conditional on units and on the
  starting point, and fails in magnitude for PC12. The paper does not
  derive it from the widths argument: one explains the geometric fall,
  the other the agreement with √λ, and what makes them coincide beyond the
  polynomial and continuum-exponential cases is left a conjecture
  (§VII D). This is the gap in the paper's own argument that matters to
  the record.
- The algorithm comparisons are admitted non-rigorous.
- A slip: Appendix B's prose says a rejected step reduces the
  Levenberg–Marquardt term, while Algorithm 2 and §VIII raise it.
