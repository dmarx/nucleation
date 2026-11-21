---
status: Read
paper: LIT-2999
title: 'Gutenkunst, Waterfall, Casey, Brown, Myers & Sethna 2007 — sloppy spectra across seventeen systems-biology models'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    From the open-access full text, JATS XML from Europe PMC's documented
    REST interface (PMC2000971, ADR-101), fetched 2026-11-21 (HTTP 200);
    equations 1–3 from the MathML in the publisher's article XML
    (journals.plos.org, CC-BY); Fig. 1 and inline formulas as images from
    the publisher; Dataset S1 (the supplementary zip) from the publisher,
    of which only the Hessian files and two plotting scripts were read as
    text and nothing was executed. Read in full: abstract, author summary,
    Introduction, Results, Discussion, Methods, captions of Figs. 1–4,
    references. Skipped: Texts S1–S5; Figs. 2–4 read from their captions.
    The eigenvalues of the Dataset S1 Hessians were computed with
    python3 -I by the reader and recomputed by the filer (scratchpad
    filerA/eig.py), with the same results. Read by a reader subagent; filed
    by a second one, which rechecked every quote used here against the
    Europe PMC text.
date: '2026-11-21'
summary: >-
  Seventeen ODE models from the systems-biology literature, 9 to 234
  parameters each: the Hessian of a least-squares deviation of all time
  courses, in log parameters at the published values, has eigenvalues that
  "span many decades", "approximately evenly spaced in their logarithm",
  with "no well-defined cutoff", along eigenvectors skewed from the bare
  parameter axes. Read as the Fisher information of an idealized fit, it
  leaves many parameters more than 100% uncertain; in one model a
  collective fit constrains a prediction that direct measurement would
  match only with all 24 relevant parameters known to ±25%. Focus on
  predictions, not parameters.
---
<!-- inactive-ok-file: TERM-140 TERM-135 CLAIM-820 THEORY-tmpks8pd ARG-tmpddl7x — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws", or from this reading -->
<!-- inactive-ok-file: LIT-tmprn2qw LIT-tmpgafot LIT-tmpmgyty — Deferred, registered 2026-11-21 from this reading, unread -->

# NOTE-tmp1feoo: Gutenkunst, Waterfall, Casey, Brown, Myers & Sethna 2007 — sloppy spectra across seventeen systems-biology models

## Contribution

The empirical generalization of sloppiness from one model (Brown et al.
2004, LIT-tmpmgyty) to a collection of seventeen, and the converse
argument that measuring parameters one by one is an inefficient route to
a predictive model. The two-part criterion it states, spread and skew, is
the one the record's term (TERM-140) had only half of.

## Key insight

In models of this kind no parameter combination can be singled out as the
last one that matters: the eigenvalues fall over many decades with no
gap, so a fit pins predictions while leaving parameters loose, and
measuring parameters directly would have to be precise for almost every
one of them to do as well.

## Assumptions

- A local quadratic approximation at the published parameters θ*.
- Idealized data: every species observed continuously under every
  condition of the original paper, simulated from θ* (Eq. 1, "a kind of
  continuous least-squares fit of parameters θ to data simulated from
  published parameters θ*"), each species normalized by its maximum.
- Log parameters: "We took derivatives with respect to log θ to consider
  relative changes in parameter values, because biochemical parameters can
  have different units and widely varying scales" (Eq. 2).
- The model structure taken as correct.

## Key results

- **The collection** (Results, Fig. 1): 17 models, "about ten to more than
  200 parameters"; "In most cases, these parameters were not
  systematically fit or measured in the original publication."
- **The span** (Results): "In every case, the eigenvalues span many
  decades. All but one span more than 10⁶ ... In each spectrum the
  eigenvalues are also approximately evenly spaced in their logarithm;
  there is no well-defined cutoff between 'important' and 'unimportant'
  parameter combinations." Fig. 1B is clipped at 5×10⁻⁷ ("Not all values
  are visible for all models"). The text does not name the exception.
- **The criterion** (Results): "These characteristic parameter
  sensitivities that evenly span many decades and are skewed from bare
  parameter axes define a 'sloppy' model", citing Brown & Sethna 2003
  (LIT-tmprn2qw). Skew is measured per parameter by I/P, the ratio of the
  ellipsoid's intersection with an axis to its projection on it: "very
  few axes have I/P ≈ 1". No threshold is given for either part.
- **Fisher information** (Results): H is "the corresponding Fisher
  information matrix" of the idealized fit; second-derivative terms vanish
  at θ*, so H = JᵀJ (Methods, Eq. 3).
- **Eigenvectors** (Results) "may not be useful in guiding model
  reduction", since they mix many parameters.
- **Collective fits** (Fig. 3): with 100 data points per parameter at 10%
  error, "such fitting leaves many parameters with greater than 100%
  uncertainty"; sloppiness predicts this "even for fitting to complete
  data that the model can fit perfectly."
- **Fit against measurement** (Fig. 4, the PC12 model): after Brown et
  al.'s fit "Not a single parameter was constrained to better than a
  factor of 50", yet the ERK prediction is tight. To match it by
  measurement "all 24 involved parameters must be measured to within a
  factor of plus or minus 25%"; with one of them known only within a range
  of 1,000, the prediction "would likely be useless". "Uncertainty for
  this prediction is large if any one of about 18 of the 24 involved
  parameters is unmeasured."
- **Causes** (Discussion): the bare-to-eigenparameter transformation is
  "fundamental to the system, not an artifact of the modeling process";
  and sloppiness depends on the data: "exhaustive experiments designed to
  decouple the system and separately measure each parameter will
  naturally not yield sloppy parameter sensitivities." The PC12 model
  with every rate and concentration rescaled to 1 "remains sloppy, with
  eigenvalues roughly uniformly spanning five decades".
- **"Universal"** (Introduction): "Universality in this sense does not
  imply that all models must necessarily share the property", citing
  Waterfall et al. 2006 (LIT-tmpgafot).

**From Dataset S1** (the reader's computation, recomputed by the filer;
not the paper's statements). Eigenvalues normalized by the largest; several
Hessians have small negative eigenvalues, which mark a numerical floor of
relative 10⁻¹⁸ to 4×10⁻⁷, and only eigenvalues above it are counted. One
model (von Dassow, 49 parameters) has 957 non-finite entries and is left
out.

- The exception to "more than 10⁶" is the Kholodenko kinase cascade
  (21 parameters, 5.2 decades, all eigenvalues positive); the Lee Wnt
  model resolves 5.7 decades plus one eigenvalue at numerical zero.
- The resolved span stays at 5 to 10 decades from 9 to 234 parameters,
  while the number of eigenvalues per decade grows from about 1 (Tyson,
  9 parameters; Zwolak, 11) to 15 and 22 (Chen, 131; Sasagawa, 234). The
  large models' spans are lower bounds, their tails lying under the floor.
- So "evenly spaced in their logarithm" here means roughly uniform density
  over the log range, not a fixed step per rank: median successive gaps
  run from 0.8 decades in the smallest model to 0.03 in the largest.
- The rescaled PC12 model resolves 23 eigenvalues over 4.4 decades; the
  paper says five.

## Concepts

- **Sloppy** — spectra that "evenly span many decades and are skewed from
  bare parameter axes".
- **Stiff and sloppy directions**; **I/P**, alignment of the ellipsoid with
  a bare axis.
- **Collective fit** against **direct measurement**.
- **Universal** in the statistical-physics sense: a shared property with a
  deep cause, not one every model has.

## Connections

The empirical base the 2010, 2011 and 2015 papers cite (NOTE-2240,
NOTE-2247, NOTE-2242); their characterizations of it are accurate, and
"seventeen" is right. The PC12 model is Brown et al. 2004 (LIT-tmpmgyty),
the same model the 2011 paper studies. The word and the definition come
from Brown & Sethna 2003 (LIT-tmprn2qw); the sense of "universal" and a
proposed cause from Waterfall et al. 2006 (LIT-tmpgafot), named without a
code in NOTE-1018. All three are registered Deferred from this reading.

## Bearing on the record

Filed as THEORY-tmpks8pd. Dated notes of 2026-11-21 on each entry below.

- **TERM-140** — corrects it in three places, made in place there: the
  criterion has a second part (skew from the bare axes); "a decade or more
  below the last" is wrong for most of the collection; and the claim that
  a sloppy spectrum covers decades in proportion to the number of
  parameters is not what these spectra show. Supports "relative to a
  design" verbatim. On "relative to a chart" it argues the other way: the
  bare parametrization is "fundamental to the system".
- **TERM-135** — background: no model manifold and no widths here; the
  ellipsoids are in parameter space, axes ∝ 1/√λ.
- **CLAIM-820** — supports its consequence in one model, and its
  relativity to the observables fitted; the rescaled model tells against
  the spread being an artefact of scales. ARG-tmpddl7x.
- **NOTE-2240**, **NOTE-2242** — parallel: what they cite this paper for
  holds.
- **NOTE-1018** — names "Gutenkunst et al. 2007" without a code; the
  code is now LIT-2999.

Nothing here is an instruction for machine-learning practice.

## Limitations

- The spectra are of an idealized design, every species observed
  continuously, not of the experiments the models were fitted to.
- Local (Hessian) analysis only; no threshold for "many decades" or
  "evenly"; "evenly" is judged by eye from a clipped figure.
- The fit-against-measurement comparison is one prediction in one model;
  others are in Text S3, unread.
- The skew criterion is stated relative to the bare parameters in log
  units, the chart the paper also calls fundamental; it says nothing on
  how the spectrum scales with the number of parameters.
