---
number: 672
status: Read
formerly:
- NOTE-tmpaosen
paper: 'LIT-872'
title: 'Hyperbolic geometry of the olfactory space'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the PubMed Central open-access copy (PMC6114987,
    CC BY-NC), fetched as JATS XML through Europe PMC and read as plain
    text: abstract, Introduction, Results, Discussion, both Materials and
    Methods sections (clique topology with the hyperbolic and Euclidean
    models, the perceptual distance, the P-value procedure, the hyperbolic
    nonmetric MDS), the captions of Figs. 1–5, the acknowledgements and
    data statement, and the reference list. The figures themselves and the
    Supplementary Materials (figs. S1–S7, tables S1–S5) were not seen; the
    per-dataset P values in tables S1–S5 are known here only through the
    text. The equations were followed, not re-derived. One check of my
    own: a simulation of the fitted shell (70 points, 6.3 ≤ r ≤ 7, radial
    density ∝ sinh 2r) gives a Spearman correlation of about 0.91 between
    its hyperbolic distances and the angular distances of the same points
    on a 2-sphere.
date: '2026-10-09'
summary: >-
  In four natural odour sources, rank-ordered concentration correlations
  match points near the surface of a 3D hyperbolic ball and not uniform
  Euclidean cubes; human odour-descriptor profiles match a full 3D
  hyperbolic ball. The evidence separates "hyperbolic shell" from "uniform
  Euclidean cube" only. On a thin shell, hyperbolic distance is nearly a
  monotone function of angle, so a sphere in flat space, which was not
  tested, would be a close rival, and the hierarchy that motivates the
  model is not recovered from the data.
---

<!-- inactive-ok-file: THEORY-191 THEORY-192 THEORY-196 THEORY-188 THEORY-185 — Proposed; cited as the THEORY this reading sources, as sibling findings in the batch, and as the account QUESTION-025 builds on -->

# NOTE-672: Hyperbolic geometry of the olfactory space

## Contribution

Before this paper, clique topology (Giusti et al. 2015) had been used to
detect geometric structure in neural correlations, and odour perception
had been described as low-dimensional and qualitatively curved (Koulakov
et al.'s "potato-chip"). This paper applies the Betti-curve test to the
co-occurrence statistics of natural odours and to human perceptual
ratings. It reports that both fit a 3D hyperbolic geometry and neither
fits a uniform Euclidean cube. It also proposes that the matching
geometry and dimension of stimulus and percept avoid the distortion a
mismatch would force.

## Key insight

If odours are produced together by branching biochemical pathways, their
co-occurrence should be organised like the leaves of a tree. A tree
embeds with low distortion in hyperbolic space, its leaves near the
boundary. So the paper asks whether the rank order of odour correlations
looks like a sample from near the boundary of a hyperbolic ball. Because
Betti curves are invariant to any monotone transform of the correlations,
the question is posed about geometry alone, without fixing how
correlation maps to distance.

## Assumptions

- **Correlation is proximity.** D_ij = −|C_ij|, the absolute Pearson
  correlation of two compounds' concentrations across samples. Only the
  rank order is used, so any decreasing function of |C| gives the same
  result. The sign of a correlation is discarded.
- **Uniform sampling in the candidate geometry.** Euclidean: uniform in
  the d-cube. Hyperbolic: native ball of curvature ζ = 1, uniform angle,
  radial density ρ(r) ∝ sinh((d − 1)r) on [R_min, R_max], with distance by
  the hyperbolic law of cosines,
  cosh x = cosh r cosh r′ − sinh r sinh r′ cos Δθ.
- **Multiplicative noise** on model distances, D = D_geo (1 + ε N(0,1)),
  ε fitted per dataset (0.040–0.050 hyperbolic; 0.05–0.09 Euclidean). No
  noise for the perceptual set.
- **Fitting.** Parameters (R_max, R_min, ε, or d and ε) are tuned to the
  first integrated Betti value; the second and third are then the test.
- **Perceptual distance** is the Euclidean distance between 146-vectors
  of descriptor ratings (Dravnieks), not a correlation.
- Compounds whose concentrations were mostly zero were dropped.

## Key results

- **Natural odours (Fig. 2; tables S1–S4).** All four datasets are
  consistent with a 3D hyperbolic shell, R_max = 7 and R_min = 0.9 R_max
  for all four: P > 0.25 (blueberry), > 0.21 (tomato), > 0.45 (mouse),
  > 0.19 (strawberry), the minimum over Betti 2 and 3. The best Euclidean
  models (d = 8 or 10) are rejected: P < 0.03 (blueberry), < 0.003 (the
  rest). Shuffled concentrations fit random matrices (P = 0.4, 0.7, 0.9)
  and are rejected by the hyperbolic model (P < 0.01). The same holds
  with L1 distances between curves and with log concentrations.
  Hyperbolic dimension above 3 is not excluded, but 3 fits best (fig. S3).
- **Embedding (Fig. 3).** A nonmetric MDS modified for hyperbolic
  distance, with radii fixed and angles optimised, places the compounds
  approximately uniformly over the sphere. They do not cluster by
  functional group (fig. S5).
- **Axes (Fig. 4).** In the joint strawberry–tomato embedding (Procrustes
  aligned), directions for pleasantness, boiling point and acidity are
  fitted on two thirds of the compounds and tested on the rest.
  Pleasantness of single compounds, R = 0.66, P = 3 × 10⁻⁷; liking of
  tomato samples from a strawberry-trained axis, R = 0.34, P = 0.01;
  boiling point and acidity, P < 0.04. Pleasantness is predictable from
  the other two axes, since the shell is effectively 2D.
- **Perception (Fig. 5; table S5).** Euclidean spaces of every dimension
  fail the first integrated Betti value (P < 0.003). Hyperbolic balls of
  several dimensions match Betti 1, but only low dimensions also match
  Betti 2. 3D is best, and d ≥ 9 is rejected (P < 0.034). Betti 3 is about
  zero. The biphasic curves are reproduced by resampling the hyperbolic
  MDS embedding, whose points fill half the ball (L1 P = 0.32 and 0.20
  hyperbolic, P = 0 and 0.06 Euclidean). Hyperbolic MDS distances
  correlate better with perceptual distances than Euclidean ones (fig. S6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Rank-ordered concentration correlations in four natural odour sources match a 3D hyperbolic shell and not a uniform Euclidean cube | moderate (four datasets, shuffle control, two scoring rules; the only flat null is a uniform cube) | Fig. 2; tables S1–S4 |
| C2 | All four sources share one hyperbolic radius | weak (a single grid-fitted shell, R_max = 7, R_min = 0.9 R_max, reported identical; how finely R was searched is not stated) | Methods |
| C3 | Human odour-descriptor profiles match a full 3D hyperbolic ball and no Euclidean space | moderate (one dataset of 127 odorants) | Fig. 5; table S5 |
| C4 | Pleasantness, boiling point and acidity are linear axes of the fitted fruit-odour space, with held-out validation | moderate for pleasantness of single compounds; weak for mixtures (R = 0.34) | Fig. 4 |
| C5 | Natural odour space is hierarchical, a tree whose leaves are the compounds | argued, not tested; no tree is inferred and compounds do not cluster by chemistry | Fig. 1; Discussion |
| C6 | Matching stimulus and perceptual geometry minimises perceptual distortion | conjecture | Discussion |
| C7 | Perceptual spaces in general are hyperbolic, because of hierarchical networks and saturating neurons | conjecture, supported only by citations to visual, haptic and auditory work | Discussion |

## Method

Betti curves of the order complex of a similarity matrix (Giusti et al.)
are compared with those of matrices built from points sampled in each
candidate geometry: 300 samples per candidate, P values as two-tailed
percentiles of the data's integrated Betti value, or of its L1 distance
to the model's mean curve. Model parameters are tuned on Betti 1 and
tested on Betti 2 and 3. Visualisation is by MATLAB's nonmetric MDS with
the distance replaced by the hyperbolic one, initialised from the fitted
shell, radii held fixed.

## Concepts

- **olfactory space**: here, the space whose points are monomolecular
  compounds (or odour mixtures) and whose distances are set by
  co-occurrence across natural samples. The perceptual space is the same
  for descriptor profiles.
- **integrated Betti value**: the area under a Betti curve, the number of
  m-dimensional cycles plotted against edge density.
- **hyperbolic shell**: the ball model sampled only between R_min and
  R_max, standing for the leaves of a tree.
- **Venn-to-half-space map**: a disc of centre (x, y) and radius ρ becomes
  the point (x, y, ρ) of the upper half-space, so larger, more inclusive
  sets sit higher. Cited to Krioukov et al. (ref. 7), not proved here.

## Connections

- **Krioukov et al. (2010)**, filed in the same batch ([LIT-865](../literature.d/LIT-865.md),
  [NOTE-680](NOTE-680.md), [THEORY-188](../theory.d/THEORY-188.md)), is ref. 7: the ball model, the radial
  density sinh((d − 1)r), the law of cosines, and the reading of a
  boundary shell as the leaves of a tree all come from there. Ref. 21 is
  Boguñá, Papadopoulos & Krioukov on Internet routing.
- **Zhang, Rich, Lee & Sharpee (2022)** ([LIT-876](../literature.d/LIT-876.md), [NOTE-668](NOTE-668.md),
  [THEORY-192](../theory.d/THEORY-192.md)) is the same lab applying the same test to CA1 place
  cells, with a full ball rather than a shell. Its reading names this paper
  as prior art. The confound named there, that the metric is not
  separated from the distribution of points, holds here too, and here in
  a sharper form.
- **Sala et al. (2018)** ([LIT-874](../literature.d/LIT-874.md), [THEORY-196](../theory.d/THEORY-196.md)): its subject is
  the precision cost of embedding a known tree. This paper embeds no tree,
  so those tradeoffs are not engaged.
- In the record's holdings nothing else concerns olfaction, odour
  statistics or perceptual geometry.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Indirect, but closer than the hippocampal paper, for
  two reasons.
  - The data here are co-occurrence statistics: the correlation of
    components across natural samples, the analogue of word co-occurrence.
    They are reported to be non-Euclidean in a rank-invariant sense.
  - Linear attribute directions are nevertheless read out of the fitted
    curved space.

  Neither result answers the question. The attributes (pleasantness,
  boiling point, acidity) are continuous and not hierarchical. No
  implication structure among binary attributes is posited or measured.
  The axes are fitted in the angular coordinates of a shell that is close
  to a sphere, not in the hyperbolic metric. The paper's Fig. 1 argument
  does bear on the lattice side of the question: a family of sets (a
  formal context's extents) maps to points of a hyperbolic half-space with
  inclusion as height. That suggests implication among attributes would
  appear as radial depth rather than as a sum of attribute vectors,
  against [THEORY-185](../theory.d/THEORY-185.md)'s premise. The argument is cited from Krioukov et
  al., not shown here, and it is not tested.
- It is the source of [THEORY-191](../theory.d/THEORY-191.md).
- No CLAIM in the record rests on odour or perceptual geometry, so it
  grounds none. It gives no instruction for ML practice, so nothing goes to
  the anthology.

## Limitations

- **The only flat null is a uniform cube.** On a shell of fixed radius,
  hyperbolic distance is a strictly increasing function of the angle
  between points, so its rank order is that of points on a 2-sphere. The
  fitted shell is thin (6.3 ≤ r ≤ 7, with most mass near 7 under the
  sinh 2r density). In my simulation of it, hyperbolic and spherical
  angular distances have a Spearman correlation of about 0.91. The radial
  spread and the noise carry what difference remains. Points on a sphere,
  or a sphere with a per-point offset, in Euclidean 3-space were not
  tested, and the "essentially 2D" space of the Results says as much. The
  natural-odour result therefore does not cleanly separate a hyperbolic
  metric from a spherical arrangement in flat space. This is my
  observation; the paper does not discuss it. The perceptual result
  (full ball, R_max = 1.6) is not subject to it in this form.
- **No hierarchy is recovered.** The tree is the motivation. Compounds
  are spread uniformly over the shell and do not cluster by chemistry, so
  the data show no branching structure.
- **Small samples.** 45–78 compounds over 50–101 samples per source; one
  perceptual dataset of 127 odorants, which the authors say samples
  perceptual space non-uniformly.
- **Fitting freedom.** The hyperbolic model has R_max, R_min and ε; the
  Euclidean, d and ε. Both are tuned on Betti 1 before testing on Betti 2
  and 3. The grid over R and the per-dataset P values are in the
  supplement, which was not read.
- **Sign discarded.** |C| treats anticorrelated compounds as close, which
  fits co-production only if anticorrelation also means a shared pathway.
- **Separate spaces.** Fruit and mouse sets share no compounds, so their
  common radius is a fitted coincidence of parameters, not one embedding.
- The perceptual-distortion and cross-modal claims (C6, C7) are
  discussion only.

## Open questions

- Does a flat model with points on or near a 2-sphere, or a flat space
  with an exponentially distributed scale coordinate, fit the odour Betti
  curves as well? Rejecting both would make the hyperbolic metric
  necessary rather than sufficient.
- Can a tree be inferred from odour co-occurrence, by hierarchical
  clustering or an ultrametric fit, and does it match known biosynthetic
  pathways? That would test C5 directly.
- Does a larger, pooled odour set fill the interior of the ball, as the
  Discussion suggests, and is the dimension still 3?
