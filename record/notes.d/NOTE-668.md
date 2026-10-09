---
number: 668
status: Read
formerly:
- NOTE-tmp1swq3
paper: 'LIT-876'
title: 'Hippocampal spatial representations exhibit a hyperbolic geometry'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the PubMed Central open-access copy (PMC9829541,
    CC BY 4.0), fetched as JATS XML through Europe PMC and read as plain
    text: abstract, Main, all four Results sections, Discussion, every
    Methods section (data, place-field and spatial-information
    computation, decoder, correlation matrices, clique topology, radius
    and dimension fitting, the Bayesian curvature estimator, the
    undersampling simulation, the Fisher-information model, statistics),
    the captions of Figs. 1–7 and Extended Data Figs. 1–10, the data and
    code statements, and the reference list. The figures themselves, the
    Supplementary Information (Tables 1–2, Figs. 1–2) and the source data
    were not seen; the per-session statistics in Supplementary Table 1 are
    known here only through the text's summary. The equations were
    followed, not re-derived.
date: '2026-10-09'
summary: >-
  In rat dorsal CA1, the rank order of pairwise spike correlations
  matches points drawn uniformly from a 3D hyperbolic ball, not from a
  low-dimensional Euclidean cube, and the ball's radius grows with the
  logarithm of exploration time. Place-field sizes are near exponential,
  which a Poisson model shows is more informative than uniform or
  log-normal sizes. The evidence separates "hyperbolic ball, uniform" from
  "Euclidean cube, uniform"; it does not separate a hyperbolic metric from
  an exponential distribution of field sizes, and the hierarchy it
  describes is nesting of field scales, not a recovered tree.
---

<!-- inactive-ok-file: THEORY-185 THEORY-192 — Proposed; cited as the account QUESTION-025 builds on and as the THEORY this reading sources -->

# NOTE-668: Hippocampal spatial representations exhibit a hyperbolic geometry

## Contribution

Hyperbolic geometry had been proposed for neural circuits (Sharpee 2019)
and found in olfactory stimuli and human odour perception (Zhou, Smith &
Sharpee 2018), but not in recorded neural activity. This paper applies
Giusti et al.'s clique topology to CA1 place-cell correlations and finds
their Betti curves consistent with a 3D hyperbolic geometry and not with
low-dimensional Euclidean ones. It adds a dynamic finding, the radius
growing with log exploration time, and an efficiency argument: the
exponential field-size distribution that a hyperbolic representation
implies carries more positional information, and the optimal radius for
CA1's cell count matches the one measured.

## Key insight

A population of place cells whose field sizes span scales, with
exponentially more small fields than large ones, is a discretised tree:
large fields contain smaller ones, and a tree embeds with low distortion
in hyperbolic space. Read as points, the neurons sit in a ball whose
radius is the log of the ratio between the largest and smallest scales
represented. Adding small fields as the animal learns pushes the boundary
out, and since their number grows as e^R, the radius grows only as the
log of the time spent.

## Assumptions

- **Correlation is similarity.** C_ij is the peak-normalised
  cross-correlogram integrated over ±1 s, read as degree of place-field
  overlap (after Hampson et al. 1996). Only its rank order is used.
- **Uniform sampling.** Model points are drawn uniformly in each
  geometry: uniform in the unit cube for Euclidean; uniform angle and
  radial density ∝ sinh^(d−1)(r) for the native hyperbolic ball of
  curvature −1 and radius R_max. Neurons are assumed to be a uniform
  sample of the representation.
- **Noise.** 5% multiplicative Gaussian noise on model distances, none on
  data.
- **Cell selection.** Putative pyramidal cells firing 0.1–7 Hz;
  inhibitory and unidentified units excluded; cells silent over 30 min
  excluded; for CRCNS sessions only the last two thirds of each session.
- **One field per neuron** for the field-size estimator (Eq. 1, Bayesian
  estimate of ζ with fields below 25 cm excluded); the topological method
  does not assume it.
- **Fisher model.** Independent Poisson neurons, 2D Gaussian fields with
  random orientation, widths i.i.d. exponential (or uniform, log-normal
  matched in mean, and variance for log-normal).

## Key results

- **Geometry (Fig. 2; Extended Data Figs. 1–5).** On three animals on the
  novel 48-m track (34–41 active cells), two 2.5-m-track sessions and seven
  box sessions (CRCNS hc-3), experimental Betti curves fall within the
  spread of 3D hyperbolic samples on integrated Betti value and L1
  distance, and outside that of Euclidean cubes; time-shifted spike trains
  fall outside the hyperbolic spread. 3D fits better than the three other
  hyperbolic dimensions compared (χ² statistic, ANOVA, Tukey). Restricting to the most spatially
  informative 75% of cells does not change this. Radii 10.5–15.5.
- **Not anatomical.** Field size on the 48-m track is not correlated with
  septotemporal or proximodistal position within dorsal CA1, so this is
  not the known dorsoventral gradient of field size.
- **Growth with experience (Fig. 3; Extended Data Figs. 7–10).** Box
  radius rises with log exploration time over days (r = 0.85, P = 3·10⁻⁶),
  fitted by I = log(1 + T/t₀) + (T/t₀) log(1 + t₀/T). On the 48-m track the
  radius of each 1-m segment, from field sizes, rises with time per metre
  (r = 0.50), and with entropy of the track's turns, but the entropy effect
  vanishes once speed is controlled (partial r = 0.18, P = 0.24). After 4 h
  of sleep the radius is below the extrapolated value: the growth is with
  experience, not elapsed time.
- **Decoding (Fig. 4a–c).** Median decoding error falls exponentially with
  spikes used; the exponent rises over days and correlates with radius
  (r = 0.70).
- **Efficiency (Figs. 4d–g, 5).** Exponential widths beat uniform and
  log-normal ones on Fisher information at every N simulated; the optimal
  R grows as log N; extrapolated to the number of active CA1 neurons it
  matches the most-familiar-box radius. Same with gamma-distributed field
  counts per cell.
- **Log-normal reconciliation (Fig. 6).** Truncating small fields and
  pooling exponentials of different rates make exponential samples
  fit a log-normal (simulation only).
- **Undersampling (Extended Data Fig. 9).** Under about a minute of data
  the topological radius estimate is biased upward; this is why the
  seconds-scale analysis uses field sizes instead.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | CA1 correlation rank-orders match uniform 3D hyperbolic samples and not uniform low-dimensional Euclidean ones | moderate (12 sessions, 3 data sets, shuffle control) | Fig. 2; ED Figs. 1–5 |
| C2 | The hyperbolic radius grows with log exploration time, as maximal acquirable information does | moderate (correlational; log fit and Eq. 2 fit both shown) | Fig. 3; ED Figs. 7, 8, 10 |
| C3 | The growth tracks experience, not speed, area or elapsed time | moderate | ED Fig. 8 |
| C4 | Exponentially distributed field sizes maximise positional Fisher information among the three families tried | strong within the model; three families only | Figs. 4e, 5 |
| C5 | The measured radius is the optimum for CA1's neuron count | weak (extrapolation of a simulated log N curve over four orders of magnitude) | Fig. 4g, 5b |
| C6 | The representation is hierarchical in a tree-like way | illustrative; no tree is inferred from data | Fig. 1a–b |
| C7 | Spikes from different neurons should be order-dependent because hyperbolic addition is non-commutative | conjecture, untested | Discussion |

## Method

The geometric inference is Giusti et al.'s: Betti curves of the order
complex of a similarity matrix, compared with the curves of matrices
built from points sampled in candidate geometries, 300 samples per
candidate, with P values from where the data fall in the sampled
distribution. Radius is chosen by maximising the product of four such P
values over R in {5, 5.5, …, 24}, with 75% subsampling of cells repeated
100 times. The second estimator fits an exponential to place-field sizes
and reads the rate as curvature. Efficiency is argued by simulated Fisher
information.

## Concepts

- **hyperbolic radius R_max**: the radius of the ball at curvature −1;
  equivalently the inverse curvature at fixed radius. The paper calls it
  the "size" of the representation.
- **Betti curve β_m(ρ)**: number of m-dimensional cycles (not bounded by
  cliques) in the graph keeping the top fraction ρ of pairs.
- **integrated Betti value**: ∫ β_m(ρ) dρ.
- **temporal familiarity**: time spent per metre of track, the inverse of
  mean speed over the fields in a segment.

## Connections

- **Krioukov et al. (2010)**, *Hyperbolic Geometry of Complex Networks*,
  filed and read in the same batch ([LIT-865](../literature.d/LIT-865.md), [NOTE-680](NOTE-680.md)): cited
  here (ref. 13, with Gromov) for a tree-like network being a mesh over a
  hidden hyperbolic geometry, and Boguñá, Papadopoulos & Krioukov (2010)
  for greedy routing. The node-radius ↔ log-degree map there corresponds
  to the field-size ↔ radius map here: in both, radial position is a
  log-scale variable and uniform sampling in the ball gives an exponential
  tail. That is my connection; the paper draws only the routing one.
- **Sala et al. (2018)**, filed in the same batch ([LIT-874](../literature.d/LIT-874.md)): its
  subject is the precision cost of embedding trees in hyperbolic space;
  this paper embeds no tree, so the tradeoffs there are not engaged.
- In the record's neuroscience holdings nothing else measures the
  geometry of a population code; [LIT-633](../literature.d/LIT-633.md) (ripple-mediated co-firing) is
  the nearest by method, using pairwise co-firing, and does not ask about
  geometry.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Little. The question asks whether attributes that
  imply or exclude one another in co-occurrence statistics still give
  linear attribute directions and a non-Boolean concept lattice. This
  paper is about a spatial code, and its hierarchy is containment of
  place fields by scale, not implication among attributes. It offers one
  analogy and no answer: nested fields are nested extents, a partial
  order by inclusion, and here such an order is said to be represented
  with a hyperbolic metric rather than by linear directions in a flat
  space. If that carried over, a hierarchical attribute structure would
  show up as radial depth plus angle rather than as a sum of attribute
  vectors, which is the opposite of [THEORY-185](../theory.d/THEORY-185.md)'s premise. The paper does
  not test anything of the kind, and it does not satisfy either kind of
  answer [QUESTION-025](../questions.d/QUESTION-025.md) names.
- It is the source of [THEORY-192](../theory.d/THEORY-192.md).
- No CLAIM in the record rests on biological representation geometry, so
  it grounds none; no instruction for ML practice, nothing for the
  anthology.

## Limitations

- **Metric and distribution are confounded.** The paper says so itself:
  model Betti curves differ "through (1) different distribution of points
  … and (2) different distance metrics". The Euclidean null is a uniform
  cube; no Euclidean null with an exponential (multiscale) distribution of
  a size coordinate was tried, nor any other non-uniform Euclidean or
  spherical model. So C1 shows "uniform hyperbolic, not uniform
  Euclidean", and the step to "the code's metric is hyperbolic" is not
  isolated from "field sizes are exponential". The paper's own Fig. 1b
  construction (centre in the plane, size as height) is the half-space
  picture in which those two coincide.
- **Few cells.** 34–56 cells per session for a 3D geometry with one free
  radius; the radius estimate is biased under about a minute of data.
- **No tree recovered.** "Hierarchical" rests on the construction in Fig.
  1b and on the exponential field-size distribution, not on any inferred
  branching structure in the data.
- **Correlational dynamics.** Radius growth versus time is a regression on
  sorted sessions; the log fit and the information formula are both
  fitted, with t₀ free.
- **Efficiency is model-bound.** The Fisher comparison is against two
  alternative families, under independent Poisson neurons, and the match
  to CA1's cell count extrapolates a simulated curve far beyond the
  simulated range.
- **Dorsal CA1 only**, rats only, a few environments.

## Open questions

- Does a Euclidean model with exponentially distributed field sizes, or a
  model with field centres and scales sampled independently, produce the
  same Betti curves? If so, C1 is a finding about scale distribution
  rather than about metric.
- Does the order-dependence of spike integration predicted from
  non-commutative hyperbolic addition (C7) appear in downstream readout?
- Does the same signature hold in ventral CA1, entorhinal cortex, or
  non-spatial hippocampal codes, where the authors expect a broader
  hierarchy?
