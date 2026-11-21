# Reader notes: LIT-tmpd3swn, Transtrum, Machta & Sethna, "Why are nonlinear fits so challenging?"

Reader key lit-tmpd3swn. Read 2026-11-21.

## Provenance

- Read: arXiv:0909.3884v2 (16 Dec 2009), PDF, https://arxiv.org/pdf/0909.3884,
  fetched 2026-11-21, HTTP 200, application/pdf. Kind: arXiv preprint (the
  authors' own manuscript). Text extracted with pdftotext; the extraction drops
  the "fi", "ff", "ffi" and "c" glyphs of the font, so the quotes below restore
  them by sense (e.g. "fits", "effects", "curvature"); nothing else altered.
- Abstract page https://arxiv.org/abs/0909.3884, HTTP 200, 2026-11-21:
  v1 22 Sep 2009, v2 16 Dec 2009; journal DOI 10.1103/PhysRevLett.104.060201
  (Phys. Rev. Lett. 104, 060201, 2010). No email address sent anywhere.
- What was read: all of it, 4 pages: abstract, text, Figs. 1–4 captions (the
  figures themselves only as their captions and the text that cites them),
  Table I, footnotes [23], [24], references. Nothing skipped.
- Copies located: the arXiv abs and PDF above (read). The PRL version at the
  DOI was not sought, since the arXiv v2 is dated after acceptance-era
  revision and was read in full. No obstacle met.

## Summary

A four-page PRL. Least-squares fitting is cast as geometry: the model
manifold M is the N-dimensional surface of predictions Y(θ) in data space
R^M; the cost is half the squared Euclidean distance to the data; the
induced metric is g = JᵀJ, "known as the Fisher Information matrix". The
authors find M typically bounded, with cross-sections forming a hierarchy of
widths, "a long, thin ribbon" ("hyper-ribbon"); explain the hierarchy by
treating fitting as interpolation of an analytic function sampled inside its
radius of convergence; observe that the widths track the square roots of the
metric's eigenvalues in one eight-dimensional model; find the extrinsic
curvature small, so geodesics are nearly straight; attribute fitting failures
to algorithms running into the manifold's boundaries; and add geodesic
acceleration to Levenberg–Marquardt, which raises its success rate on a test
problem.

## Contribution

The geometric picture (bounded, thin, nearly flat model manifold) as the
explanation of why fits fail, the interpolation argument for the width
hierarchy, and the geodesic-acceleration correction to Levenberg–Marquardt.
The term "hyper-ribbon" (hyphenated here) appears in this paper.

## Key results (with places and quotes)

1. Metric (p. 1): "The Euclidean metric of data space ... induces a metric on
   the manifold, gµν = ∂µY · ∂νY = (JᵀJ)µν ... gµν is known as the Fisher
   Information matrix." No noise σ appears: distances are raw residuals, so
   unit measurement error is implicit; the paper never says the components are
   scaled by their errors.
2. Two-exponential manifold (Fig. 1 caption, p. 1), model e^(−θ1 t)+e^(−θ2 t)
   at t = 1/3, 1, 3: "Boundaries exist when θµ = 0, ∞ and when θ1 = θ2. (The
   ribbon-like structure of Fig. 2 emerges only in higher dimensions.)"
3. Hyper-ribbon (p. 1): "this model manifold can take the form of a
   hyper-ribbon, with thinnest direction four orders of magnitude smaller than
   the long axes." Abstract: "cross sections have a hierarchy of widths and are
   typically very narrow."
4. Interpolation argument (pp. 1–2, Eq. 1): for an analytic f(t) with Taylor
   terms ≲ R^(−n), the range Δf_n left at t0 after constraining n nearby
   points obeys Δf_{n+1}/Δf_n ≈ (t − t_{n+1})/R < 1: "Each cross section is
   thinner than the last by a roughly constant factor, yielding the observed
   hierarchy." Heuristic ("If n is sufficiently large").
5. Widths and spectrum (p. 2, Fig. 3): Fig. 3 plots "Geodesic cross-sectional
   widths of an eight dimensional model manifold along the eigendirections of
   the metric from some central point, together with the square root of the
   eigenvalues (singular values of the Jacobian)"; "the widths and singular
   values each spanning around four orders of magnitude and the curvatures
   covering eight." Text: "the eigenvalues of the metric tensor gµν in Fig. 3
   also form a hierarchy, spanning eight orders of magnitude — this
   'sloppiness' has been documented in a number of other models"; "the widths
   of the model manifold track nicely with these eigenvalues in Fig. 3 (taking
   the square root to match units): moving parameter combinations along
   eigendirections of the metric by an order of magnitude (fixed shift in log
   parameters) exhausts the range of behavior (width). This tracking suggests
   that the ubiquity of sloppy eigenvalue spectra at best fits implies a
   ubiquitous hyper-ribbon structure for the model manifold." Conclusion
   (p. 4): "These boundaries form a hierarchy of widths dual to the hierarchy
   of Hessian eigenvalues characteristic of nonlinear model fits."
6. Scope (p. 2): "(Multiparameter models whose parameters are individually
   measured by the data, and on the other extreme models with sensitive,
   chaotic dependence on parameters, will likely not fall into this family.)"
   And: "Most parameters in these models have bounded effects — they can be
   set to limiting values (zero, infinity, etc.) and still have finite model
   predictions."
7. Few effective degrees of freedom (p. 2): "near degenerate Hessians result
   whenever multiple data points reside within some generalized radius of
   convergence ... the model has few effective degrees of freedom. Whenever
   there are many model parameters for each effective degree of freedom there
   will be a hierarchy of widths and the model will be sloppy." And: "only a
   few stiff parameter combinations need to be tuned to fit most of the data
   ... The remaining unconstrained parameter combinations control the
   interpolated values, which are already restricted by the analyticity of the
   model."
8. Curvature (p. 2, fn. 24): extrinsic and parameter-effects curvatures span
   twice the decades of the widths ("their formulas include a factor of 1/λ");
   extrinsic curvature three orders smaller than parameter-effects curvature:
   "The ribbon is nearly flat, but very thin; the geodesics hit the edges long
   before finding a good fit" (p. 3).
9. Boundaries and algorithms (p. 3): "Since most boundaries occur at infinite
   parameter values, the model graph G 'stretches' these boundaries to
   infinity"; LM is read as Gauss–Newton on the model graph with metric
   g0 + λI. Geodesic acceleration aµ = −g^µν ∂ν y · ∂α∂β y v^α v^β, step
   δθ = v + a/2.
10. Table I (p. 3), sum of four exponentials in log-parameters, starts near a
   boundary: success LM+accel 65%, traditional LM 33%, trust-region LM 12%,
   BFGS 8%; one test problem, number of trials not stated.

## Assumptions

Least squares with a Euclidean data metric (unit, equal errors implicit);
analytic models of one variable sampled within a radius of convergence (for
the width argument); positive parameters in log coordinates (Table I; the
"fixed shift in log parameters" remark); widths measured from "some central
point" along the metric's eigendirections.

## Concepts

model manifold; model graph; hyper-ribbon; cross-sectional width (geodesic);
sloppiness (eigenvalue hierarchy of g = JᵀJ); stiff / sloppy combinations;
extrinsic vs parameter-effects curvature; geodesic acceleration;
Levenberg–Marquardt as Gauss–Newton on the model graph; manifold boundaries.

## What "sloppy" means here (the brief's question)

The paper gives no formal definition. It names as "sloppiness" the
eigenvalues of g = JᵀJ forming "a hierarchy, spanning eight orders of
magnitude" (Fig. 3's one model) and cites Gutenkunst et al. 2007 [5] and
others for its ubiquity. It says nothing about even spacing in log scale; that
characterization is not in this paper. The ranges are: eigenvalues ~8 decades,
singular values and widths ~4 decades, curvatures ~8 decades, thinnest/longest
axis ~4 decades (p. 1). On whether the widths are set by the same spectrum: the
paper observes it in one model (Fig. 3), calls the two hierarchies "dual"
(p. 4), offers the log-parameter-shift mechanism, and "suggests" generality.
Its own explanation of the geometric fall (result 4) bounds the widths
directly, without going through the spectrum.

## Verdict on the exchange's characterization (A19, A39; as quoted in the codes)

Accurate on the core: a hierarchy of widths, each smaller than the last by a
roughly constant factor; a ribbon shape; the metric JᵀJ called the Fisher
information; the link between sloppy spectra and the ribbon. Three things the
exchange's wording goes beyond: (a) "over many decades" — the paper shows ~4
decades of width in one eight-parameter model; (b) the tie of widths to the
spectrum is an observation in one model plus a suggestion, not a derivation;
(c) "no abrupt distinction between important and unimportant parameter
directions" and talk of "importance" are A's, not this paper's; the paper
speaks of what the data constrain and of fitting. The exchange omits the
paper's purpose (why fits fail; geodesic acceleration).

## Bearing on the named codes

- TERM-tmp5z2du (hyperribbon): supports, with qualifications. The definition's
  "each width smaller than the last by a roughly constant factor" is the
  paper's (result 4). Qualify: the paper's term is "hyper-ribbon"; widths are
  "geodesic cross-sectional widths ... along the eigendirections of the metric
  from some central point" (Fig. 3), worth adding to the definition; the
  measurement-error scaling is not in this paper (it uses raw Euclidean
  distance); "over many decades" is ~4 decades in the one example; "the
  hyperribbon is the global form ... follows the same hierarchy" is the paper's
  observation and suggestion (result 5), not a theorem. Condition 1 (relative
  to an experiment) is supported by the interpolation argument: the hierarchy
  arises when data points lie within the radius of convergence R, a design
  fact. Condition 2 (regular, not singular): the paper is silent. The paper's
  scope exclusions (result 6) could be added under "What it is not".
- CLAIM-tmpcgvcp: background, consistent. The paper speaks of "near
  degenerate Hessians" (regular, small eigenvalues), as the claim's
  "sloppiness" does. It does not discuss singularity or learning coefficients.
  Its Fig. 1 caption names θ1 = θ2 as a boundary of the two-exponential
  manifold, which supports the claim's remark that "the textbook sloppy model
  has such strata at its edges" as to location (it does not call it a fold or
  a rank-loss stratum).
- CLAIM-tmpa8hb2: leaves open; qualifies. Nothing on Watanabe. "Since most
  boundaries occur at infinite parameter values" (p. 3) means most of the
  hyper-ribbon's edges are limits, not finite-point folds; the claim's "Not yet
  shown" about widths stays true, though Fig. 3 measures widths along the
  metric's eigendirections, so in the paper's own measurement the two
  hierarchies are aligned by construction of the directions.
- CASE-tmpb2gly: supports its identification. The case's textbook model is
  exactly the paper's Fig. 1 model, and the paper lists θ1 = θ2 among its
  boundaries. The v² scaling, the learning coefficient and the pushed-forward
  density are not in the paper.
- ARG-tmpj0r42: supports both its "measure" critical question and its
  caveat. Widths are geodesic, measured from a central point (Fig. 3), not
  point eigenvalues; "most boundaries occur at infinite parameter values"
  (p. 3) is the paper's own statement, backing the ARG's "Many lie at infinite
  parameter values".
- ARG-tmpjx3ww: supports. The hyper-ribbon is defined by distances in data
  space under g = JᵀJ, and the paper frames the hierarchy as what the data
  constrain (result 7), not as importance. Qualify "under its stated noise":
  this paper states no noise model.
- THEORY-774: parallel. Same metric (JᵀJ with unit error); 774 derives a
  hierarchy exactly for a hopping model observed after t steps; this paper
  gives a heuristic for analytic models sampled within R. Both make the
  hierarchy come from observing at a scale coarse relative to the system's own.
- THEORY-777, THEORY-742: background only; no coarse-graining or RG here.

## Limitations

Heuristic width argument (analytic, single-variable models; "roughly";
"sufficiently large n"). Widths-vs-spectrum shown for one unnamed
eight-dimensional model from "some central point"; no statement of which
model or which point. Table I is one test problem, trial counts not given.
Noise is not modelled; "Fisher information" is used for JᵀJ under unit error.
The fuller treatment is deferred to refs [10], [18] (LIT-tmpzkxka is likely
[10]'s published form).

## Candidate THEORY

Sentence: Transtrum, Machta and Sethna argue that the manifold of a nonlinear
least-squares model's predictions in data space is typically bounded and
ribbon-like, its cross-sectional widths each smaller than the last by a
roughly constant factor, which they explain for analytic models of one
variable sampled within their radius of convergence by the error bound of
polynomial interpolation; they observe in one eight-parameter model that the
geodesic widths along the eigendirections of g = JᵀJ track the square roots of
its eigenvalues, both spanning about four decades, and suggest that sloppy
spectra imply this "hyper-ribbon" generally; fits fail where algorithms reach
the manifold's boundaries, and adding geodesic acceleration to
Levenberg–Marquardt raised its success rate on one four-exponential test from
33% to 65%.

promote_when: Width-and-spectrum computations on models beyond the paper's
one, giving geodesic cross-sectional widths along the eigendirections of JᵀJ
beside the square roots of its eigenvalues, that find the widths falling by a
roughly constant factor and tracking the singular values within a stated
factor; or a proof that the interpolation bound fixes the width ratio for a
stated class of analytic models.

## Recheck (grep of record/ after reading)

Searched: Levenberg, geodesic acceleration, extrinsic curvature,
parameter-effects curvature, model manifold, hyper-?ribbon, sloppy,
Gauss-Newton, radius of convergence, model graph, sum of exponentials,
Transtrum, effective degrees of freedom/dimension. Entries the first search
(the brief's list) missed:
- CLAIM-tmpcg4uu (Proposed): its "textbook sloppy model ... at equal rates" is
  the paper's Fig. 1 boundary θ1 = θ2: supports the location.
- CLAIM-tmpnu4ar (Proposed), reduction toward manifold boundaries "where
  parameters stop mattering": supports; the paper's "unresponsive" boundaries
  and "bounded effects ... set to limiting values (zero, infinity)" (p. 2).
  Qualifies the duality it proposes: most boundaries are at infinite parameter
  values (p. 3).
- CLAIM-tmpficzj (Proposed), parameter vs behavioural complexity: supports;
  "although parameters cannot be reliably extracted by fitting degenerate
  models, it is still possible to constrain the outcome of new experiments"
  (p. 2).
- CLAIM-tmpj0k4q (Proposed), resolved directions grow with data: parallel and
  partly contrasting. The paper says added points within the radius of
  convergence "are interpolations that supply little new information" (p. 3),
  each further cross-section a constant factor thinner — a geometric fall,
  which on that claim's own terms gives logarithmic growth.
- QUESTION-tmpzlagu (Open), effective dimensions: bears; the paper's "few
  effective degrees of freedom" is one more such count, undefined.
- ARG-tmpmvc5e (Rejected), sloppy behaviour carrying to networks: background;
  the paper's own scope excludes models with chaotic parameter dependence and
  models whose parameters are individually measured.
- TERM-tmpnxjq4 (Proposed), "weak direction" in six senses: the paper's sense
  is small singular value of J / thin width in data space.
- LIT-1299 / NOTE-1018 / THEORY-774 / THEORY-777 already cite the same group.
- Hits for "model graph" (THEORY-675, THEORY-887), "extrinsic curvature"
  (THEORY-2031) and "Levenberg" (NOTE-1554) are other senses; no bearing.

## Neighbours

None needed; the work itself was read.
