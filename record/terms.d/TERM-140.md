---
number: 140
status: Proposed
formerly:
- TERM-tmptiim0
title: 'sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads evenly over many decades with no gap that separates the parameter combinations that matter from those that do not, along eigenvectors skewed from the bare parameter axes; a graded property, distinct from ill-conditioning and from singularity'
version: 4
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Edited in place, the term having been filed in this pull request, after
    the readings of its sources: LIT-2977 (NOTE-2240), LIT-3009
    (NOTE-2247) and LIT-2994 (NOTE-2242). The title and the
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
- version: 3
  date: '2026-11-21'
  note: >-
    Edited in place after the readings of LIT-2999 (Gutenkunst et al.
    2007, NOTE-tmp1feoo) and LIT-2960 (Amari, Park & Ozeki 2006,
    NOTE-tmptlwkf). Retitled. Added: the survey's second criterion,
    eigenvectors "skewed from bare parameter axes", measured by I/P; that
    "evenly spaced in their logarithm" means an even density over the log
    range; the survey's "All but one span more than 10⁶" in place of the
    unread mark; and, from Amari, Park & Ozeki, that in networks the
    singular sets are interior cone apices at finite parameters, so
    "regular inside, singular at the edges" holds for the sloppy-model
    literature's models and not for networks. Removed: "each typically a
    decade or more below the last", and the separation from a power-law
    spectrum with its table, which assumed a fixed ratio per rank and so a
    span growing with the number of parameters. Across the survey's
    models the resolved span stays at 5–10 decades while the density per
    decade grows from about 1 to 15–22 (the reader's computation from the
    paper's Dataset S1, recomputed by the filer; a lower bound, because of
    the numerical floor). The separations from ill-conditioning and from
    singularity, and the relativity to chart and design, stand.
- version: 4
  date: '2026-11-22'
  note: >-
    Edited in place after the reading of LIT-2958 (Quinn, Abbott,
    Transtrum, Machta & Sethna 2023, NOTE-tmp3keyy, THEORY-tmpx26x7). The
    title stands (its change awaits the owner) and so does the definition.
    Added: that the review's "sloppy" requires the prediction-space widths
    as well as the eigenvalues to be hierarchical, while this term takes
    the local, eigenvalue half; the review's "roughly equally spaced in
    log" recorded as a rival, fixed-step reading beside the term's density
    reading, both kept as alternatives; and that the review calls the
    geometric bound ρ^(−j) "a power law", a loose usage.
tags:
- information-geometry
- mathematical-statistics
- model-comparison
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
draws_on:
- THEORY-2155
- THEORY-2154
- THEORY-2156
- THEORY-774
- THEORY-777
- THEORY-742
- THEORY-tmpks8pd
- THEORY-tmpbobud
- THEORY-tmpx26x7
summary: >-
  At the owner's suggestion of 2026-11-21, after the filing of the
  exchange "Rich Get Richer Power Laws": "a TERM for the mathematical
  (information geometric?) sense of 'sloppy' might be merited". The record
  used the word in that sense in several entries ([TERM-135](TERM-135.md),
  [TERM-137](TERM-137.md), [CLAIM-813](../claims.d/CLAIM-813.md), [CLAIM-820](../claims.d/CLAIM-820.md), [CLAIM-812](../claims.d/CLAIM-812.md)) and in
  its readings of sloppy spectra ([THEORY-774](../theory.d/THEORY-774.md), [THEORY-777](../theory.d/THEORY-777.md)), without
  defining it. A model is sloppy, at a parameter point and for a given
  observation design, when the eigenvalues of its Fisher information,
  in a declared chart (conventionally the logarithms of its bare
  parameters), spread evenly over many decades, no gap among them marks off
  the combinations that matter from those that do not, and the
  eigenvectors are skewed from the bare parameter axes. The term separates
  this from three neighbours: ill-conditioning (one ratio, which a single
  gap can produce), singularity (a zero eigenvalue on a stratum), and the
  hyperribbon (the chart-free shape of the predictions, [TERM-135](TERM-135.md)).
  It says nothing of the law by which the spectrum falls. Its job is to let the record's entries on sloppiness,
  singular learning and effective dimension say which of these they mean.
  The source of the concept is Sethna and colleagues: LIT-2977,
  LIT-3009 and LIT-2994, read on 2026-11-21 (THEORY-2156,
  THEORY-2155, THEORY-2154), and the survey LIT-2999, read the same day
  (THEORY-tmpks8pd). They define sloppiness by example, by an eigenvalue
  spread "evenly spaced in their logarithm" and by skew from the bare
  axes, and put its chart-free content in the widths of the model
  manifold; versions 2 and 3 record what they say. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-135 TERM-137 CLAIM-813 CLAIM-820 CLAIM-812 CLAIM-825 CLAIM-848 THEORY-777 TERM-142 — Proposed, Deferred or new; the entries this term defines a word for, and the unread works it comes from -->
<!-- inactive-ok-file: ARG-133 CASE-302 THEORY-2154 THEORY-2155 THEORY-2156 THEORY-tmpks8pd THEORY-tmpbobud ARG-tmpewh6z — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

<!-- inactive-ok-file: THEORY-tmpx26x7 — Proposed or new; the 2023 review's reading, filed 2026-11-22 -->

# TERM-140: sloppy, of a parametric model at a point and for an observation design: its Fisher information spectrum, in a declared chart, spreads evenly over many decades with no gap that separates the parameter combinations that matter from those that do not, along eigenvectors skewed from the bare parameter axes; a graded property, distinct from ill-conditioning and from singularity

## Definition

Let a model map parameters θ ∈ ℝᵏ to predictions, observed with noise under a fixed design (which quantities, at which times or conditions, with what error). Its Fisher information at θ is g(θ); for least squares with unit noise, g = JᵀJ, with J the Jacobian of the predictions.

- **Sloppy.** The model is *sloppy* at θ, for that design, when the eigenvalues λ₁ ≥ … ≥ λₖ > 0 of g span many decades and are spread roughly evenly across them, in the sense of a roughly uniform density over the log range rather than a fixed step from one to the next, with no single gap that splits them into a few that matter and a remainder that does not.
- **Skewed.** The stiff and sloppy directions are combinations of parameters, not the bare parameters: few eigenvectors lie near a bare axis. Gutenkunst and colleagues make this half of their definition, "sensitivities that evenly span many decades and are skewed from bare parameter axes define a 'sloppy' model" ([LIT-2999](../literature.d/LIT-2999.md), Results), and measure it per parameter by I/P, the ratio of the ellipsoid of good fits' intersection with an axis to its projection on it ("very few axes have I/P ≈ 1"). Skew is relative to the chart too: it is measured against the bare axes in log units.
- **Stiff and sloppy directions.** The eigenvectors of the large eigenvalues are *stiff* directions; those of the small ones are *sloppy* directions. The adjective on the model refers to the whole graded spectrum, not to having some sloppy directions.
- **Graded.** There is no threshold in the concept. How many decades, and how even, are said when it matters. The sources give none either: the review's only cut is practical, eigenvalues below 1 in units of the measurement error ([NOTE-2242](../notes.d/NOTE-2242.md)). Their examples span six to ten decades: in the survey of seventeen systems-biology models, "All but one span more than 10⁶" ([LIT-2999](../literature.d/LIT-2999.md), Results), the exception being the Kholodenko kinase cascade at about 5.2 decades (the reader's computation from the paper's Dataset S1); eight in the 2010 letter's one eight-parameter model ([NOTE-2240](../notes.d/NOTE-2240.md)); six to seven in the review's five spectra. Across the survey the resolved span stays at 5 to 10 decades from 9 to 234 parameters, while the number of eigenvalues per decade grows from about 1 to 15–22 ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md); a lower bound for the large models, whose tails lie under a numerical floor near 10⁻⁷).
- **Relative to a chart.** Fisher eigenvalues are not invariant under reparametrization: under θ = Aφ the metric becomes Aᵀ g A. The convention is the logarithms of the bare parameters, so that the eigenvalues compare relative changes. A claim that a model is sloppy names its chart, or uses that convention.
- **Relative to a design.** More data or a different design can stiffen a direction. Sloppiness is of a model as observed, not of a model alone ([CLAIM-825](../claims.d/CLAIM-825.md): the number of resolved directions grows with data).

**Checked** with `python3 -I`, scratchpad script `sloppy_check.py`. A sum of k exponentials, with log-rate parameters, observed at 40 times with unit noise:
- k = 3: the eigenvalues span 1.9 decades;
- k = 5: 5.0 decades;
- k = 7: 8.8 decades.

The successive gaps are 0.6 to 2.3 decades and widen down the spectrum, so "spread" does not mean equally spaced. The sources say otherwise of their models: eigenvalues "whose logarithms tend to be evenly spaced" ([LIT-3009](../literature.d/LIT-3009.md), p. 3), each combination "less important than the previous by a fixed factor" ([LIT-2994](../literature.d/LIT-2994.md), §I). Both are kept: "roughly" is theirs, and a sum of exponentials sampled at 40 times, in this check, falls faster than geometrically down the spectrum. Gutenkunst and colleagues' "approximately evenly spaced in their logarithm" is, in their own spectra, an even density: median successive gaps run from 0.8 decades in a 9-parameter model to 0.03 in a 234-parameter one ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)). The definition asks for spread with no gap, not for a fixed step.

**Two readings of "evenly spaced", kept as alternatives.** (a) *Density*,
this term's: the eigenvalues fill the log range with roughly uniform
density, the successive gaps free to vary, as in the survey's spectra and
in the check above. (b) *Fixed step*, the reading the 2023 review's words
invite: "hierarchical: roughly equally spaced in log, spanning several
decades" ([LIT-2958](../literature.d/LIT-2958.md), §2), with widths that "follow a geometric decay" (§3),
each eigenvalue a roughly constant factor below the last. They part where
the number of parameters grows: under (b) the span grows in proportion,
under (a) it need not, and the survey's spans stay at 5 to 10 decades
([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)). The term is stated in (a), which (b) satisfies;
which one the sources mean is not settled by their wording, and the owner
may prefer (b). The review also calls its bound ρ^(−j) on the j-th axis
"a power law"; ρ^(−j) is geometric in j, and a power law in rank would be
j^(−α). The usage is loose and the term does not follow it. The same five-exponential model spans 6.1 decades in the chart of the bare rates, and 8.4 after rescaling three of them by 1, 10 and 100. So the count of decades depends on the chart.

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011) and Transtrum et al. (2015), read

What the sources say, and what version 2 changed because of it.

- **Defined by example and by spectrum.** The 2010 letter does not define
  sloppiness; it names as "sloppiness" the eigenvalues of g = JᵀJ forming
  "a hierarchy, spanning eight orders of magnitude" in one model
  ([NOTE-2240](../notes.d/NOTE-2240.md)). The 2011 paper: "Sloppiness is the property that the
  behavior of the model responds very strongly to only a few combinations
  of parameters", with "no clean separation between important (stiff) and
  irrelevant (sloppy)" directions ([NOTE-2247](../notes.d/NOTE-2247.md)). The 2015 review: "Sloppy
  is the term used to describe a class of complex models exhibiting large
  parameter uncertainty when fit to data" ([NOTE-2242](../notes.d/NOTE-2242.md)).
- **The spectrum is not intrinsic; the widths are.** "one can always
  reparametrize the manifold to make the metric at a point any symmetric,
  positive definite matrix" (2011, p. 6); "the eigenvalues of the FIM are
  not sufficient to make this conclusion" (2015, §III). The sources put
  the chart-free content of sloppiness in the model manifold: bounded, its
  geodesic widths falling roughly geometrically, the hyperribbon
  ([TERM-135](TERM-135.md)). In their usage sloppiness proper is that global shape,
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
- **Singular.** A sloppy model has g invertible at the point where it is evaluated, so near that point every direction is identified given enough data. A singular model has a zero eigenvalue on a stratum, and its learning coefficient differs from d/2 ([TERM-137](TERM-137.md), senses 4 and 5; [CLAIM-813](../claims.d/CLAIM-813.md)). But the sources tie the two at the edges: "Model boundaries correspond to points on the manifold where the metric is singular" (2011, p. 10). Usually the boundaries lie where parameters run to 0 or ∞, and in log parameters all of them lie at infinity; some lie at finite parameters, on fold lines such as θ₁ = θ₂ in a sum of two exponentials, where "No parameters were at extreme values, but the model behavior was nonetheless singular" (2011, p. 7; generic when the data number fewer than twice the parameters). So in these models the sloppy interior is regular and its edges are singular: "regular, not singular" is a property of the point in the interior, not of the whole model, and a parameter pushed toward an edge can run to infinity rather than be identified (the sources' "evaporation"). The two meet near a finite stratum, where a sloppy eigenvalue goes to zero with the squared distance ([CASE-302](../cases.d/CASE-302.md)), and at finite n, where an unresolved sloppy direction counts like a flat one ([CLAIM-812](../claims.d/CLAIM-812.md); [ARG-133](../arguments.d/ARG-133.md) weighs what the edges do to [CLAIM-813](../claims.d/CLAIM-813.md)). That picture is the sloppy-model literature's, for its own models, and does not hold for networks: there the singular sets lie inside parameter space at finite values, where a hidden unit is switched off or two units coincide, and collapse in the space of distributions to a cone apex or a point joining two components, not to an edge ([LIT-2960](../literature.d/LIT-2960.md); [THEORY-tmpbobud](../theory.d/THEORY-tmpbobud.md)). The 2011 paper's "metric singularities (i.e. model boundaries)" for network training stretches the source it cites ([ARG-tmpewh6z](../arguments.d/ARG-tmpewh6z.md)).
- **A hyperribbon.** The 2023 review joins the two in one definition: "We call a model sloppy, and the model manifold a hyperribbon, if the parameter-space eigenvalues and prediction-space widths are hierarchical" ([LIT-2958](../literature.d/LIT-2958.md), §2; [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)). In its usage "sloppy" requires both halves. This term takes the local, eigenvalue half only, what a computation at a point gives, and leaves the widths to [TERM-135](TERM-135.md). The hyperribbon is the shape of the set of predictions, whose widths fall roughly geometrically in the sources' own models, a statement about widths that this version does not carry over to a fixed eigenvalue ratio per rank ([TERM-135](TERM-135.md)). That shape does not depend on the chart; the Fisher spectrum does. Sloppiness is the parameter-space face, the hyperribbon the prediction-space face. Their connection, that the widths follow √λ, is Transtrum, Machta and Sethna's: observed in one model in 2010, shown exactly for polynomials and numerically for a few models in 2011, and conditional on units and on the point measured from ([THEORY-2155](../theory.d/THEORY-2155.md)).
- **Not a claim about the law of decay.** Version 2 separated sloppiness from a power-law spectrum by assuming that a sloppy spectrum falls by a constant factor per rank, and so spans decades in proportion to the number of parameters. The survey's spectra do not bear that out: from 9 to 234 parameters the span stays at 5 to 10 decades while the density per decade grows ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md), a lower bound). A spectrum that is evenly dense over a fixed log range, a geometric one and a power law in rank can each be spread with no gap, so the definition does not tell them apart and does not try to. Which law a given spectrum follows is said separately when it matters; the participation ratio under a power law is [CLAIM-848](../claims.d/CLAIM-848.md)'s, and neither law is "scale-free" in the sense of [TERM-142](TERM-142.md) without further conditions.
- **Unimportant.** A sloppy direction is one along which the predictions, as observed, change little. It says nothing of whether a task depends on it ([TERM-137](TERM-137.md)).

## Sources

- The concept and the word are Sethna and colleagues'. The systems-biology survey is Gutenkunst and colleagues ([LIT-2999](../literature.d/LIT-2999.md); [THEORY-tmpks8pd](../theory.d/THEORY-tmpks8pd.md)), the source of the skew criterion and of "evenly spaced in their logarithm". The geometry is Transtrum, Machta and Sethna 2010 and 2011 ([LIT-2977](../literature.d/LIT-2977.md), [LIT-3009](../literature.d/LIT-3009.md); [THEORY-2156](../theory.d/THEORY-2156.md), [THEORY-2155](../theory.d/THEORY-2155.md)), and the review is Transtrum and colleagues 2015 ([LIT-2994](../literature.d/LIT-2994.md); [THEORY-2154](../theory.d/THEORY-2154.md)). All four were read on 2026-11-21 ([NOTE-2240](../notes.d/NOTE-2240.md), [NOTE-2247](../notes.d/NOTE-2247.md), [NOTE-2242](../notes.d/NOTE-2242.md), [NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)); versions 2 and 3 record what they change. Where the singular sets of networks lie is Amari, Park and Ozeki's ([LIT-2960](../literature.d/LIT-2960.md), [NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md)).
- The record's readings of sloppy spectra are [THEORY-774](../theory.d/THEORY-774.md) (the hopping model, whose Fisher metric is given exactly), [THEORY-777](../theory.d/THEORY-777.md) (decimated critical Ising) and [THEORY-742](../theory.d/THEORY-742.md) (the Fisher information a coarse-graining loses).
- The separations from ill-conditioning and from the chart are the assistant's, checked as above.

## Note of 2026-11-21: Gutenkunst et al. (2007) and Amari, Park & Ozeki (2006), read

What the two readings changed, made in place above (version 3).

- **Gutenkunst et al. ([NOTE-tmp1feoo](../notes.d/NOTE-tmp1feoo.md)) correct the term in three places.**
  The criterion has two parts, spread and skew, and the term had only the
  first; "a decade or more below the last" holds only for the smallest
  models (about one eigenvalue per decade at 9–11 parameters); and the
  contrast with a power law rested on a fixed ratio per rank that the
  survey's spectra do not show. The paper itself says nothing on how the
  span scales with the number of parameters; the 5–10 decades and the
  growing density are the reader's computation from its Dataset S1,
  recomputed by the filer (scratchpad script filerA/eig.py).
- **Supported:** "relative to a design", in the paper's own words: "exhaustive experiments
  designed to decouple the system and separately measure each parameter
  will naturally not yield sloppy parameter sensitivities" (Discussion).
- **Qualified:** "relative to a chart". The paper takes log parameters and
  argues that the bare parametrization "is fundamental to the system, not
  an artifact of the modeling process". It predates the 2011 observation
  that the metric at a point can be reparametrized to any positive
  definite matrix; the term keeps the chart relativity and the convention.
- **Amari, Park and Ozeki ([NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md)) limit "What it is not:
  singular".** In multilayer perceptrons and mixtures the Fisher matrix
  degenerates on continua at finite parameters, cone apices in the space
  of distributions, and the paper never says "boundary". So the sloppy
  literature's "regular inside and singular at its edges" holds for its
  own models, not for networks ([ARG-tmpewh6z](../arguments.d/ARG-tmpewh6z.md)). The separation of sloppy
  from singular stands, and sharpens there: near a network's critical set
  the model is not a regular interior with a spread spectrum but a
  neighbourhood of rank loss.

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

Read in [NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md) ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)); the additions are made in place
above (version 4).

- **Supported:** "relative to a design": "a systems biology model is not
  sloppy if one designs experiments to measure one parameter at a time"
  (§8.2); "relative to a chart": rescaling parameters changes "the FIM and
  hence the spectrum of eigenvalues", while geodesic length "is
  independent of the way we define the coordinate system" (§2); "graded":
  "several decades", no threshold.
- **Supported: distinct from singularity.** The review separates
  sloppiness, "practical identifiability", from structural
  non-identifiability, which "would give eigenvalues of the metric exactly
  equal to zero" (§3), as this term separates sloppy from singular.
- **Parallel: distinct from ill-conditioning.** A separation of scales
  "certainly will generate a large range of eigenvalues, but do[es] not
  explain why eigenvalues span many decades uniformly" (§3): a large range
  is not yet sloppiness, close to this term's separation of one ratio from
  an even spread.
- **Qualified: the definition is half the review's.** Its "sloppy" needs
  widths too; this term keeps the eigenvalue half, as its "A hyperribbon"
  bullet now says.
- **Left open: which "evenly spaced".** The review's "roughly equally
  spaced in log" reads as a fixed step; it is recorded beside the term's
  density reading, both kept (Definition, above).
- **Skew:** the review's only form of the second criterion is "The most
  important eigendirections need not align with our parameter directions"
  (§1), weaker than "skewed".
- **Precision:** a sloppy model "will have an effective low-dimensional
  description if many of its widths are small compared to the precision
  of the predictions demanded" (§2). Sloppiness, as this term defines it,
  is not yet low effective dimension.

The note is the assistant's (Claude, in this session).
