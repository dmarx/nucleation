---
number: 549
status: Read
formerly:
- NOTE-tmp25fhs
paper: LIT-708
title: 'Rarely categorical, highly separable representations along the cortical hierarchy'
version: 1
history:
- version: 1
  date: '2026-10-04'
  note: >-
    Read in full from the publisher's open-access PDF (35 pages): main
    text, Discussion, the complete Methods and every Extended Data legend,
    with Figs 3, 5 and 6 and Extended Data Fig. 11 inspected as rendered
    pages; other figures read from legends and recovered panel text. The
    displayed equations of the Gaussian-cluster PR derivation are only
    partly recoverable from the text layer, so the derivation is taken at
    its stated limits. The Peer Review File (34 pages, two rounds and the
    rebuttals) read in full; the Reporting Summary is image-only and was
    not read. A second reading under ADR-013: the anthology's reading of
    the same paper (ANTH-LIT-696) was read first and is compared below.
date: '2026-10-04'
summary: >-
  Within single regions of mouse cortex during the IBL task, neurons'
  8-variable selectivity profiles are more clustered than a covariance-
  matched Gaussian only in VISp, AUDp and SSp-ul, while pooled modules and
  the whole cortex cluster along anatomical lines. Over the conditions
  each region distinguishes (M_IC 5–16), ≥ 95% of random balanced
  dichotomies are decodable above a shuffle null in 15 of 16 regions (GU
  0.82). Clustered neurons provably cap the condition geometry's
  participation ratio near min(k, M).
---

<!-- inactive-ok-file: THEORY-083 — Proposed; compared in Bearing on the record as a different sense of "categorical", not supported or contradicted -->
<!-- inactive-ok-file: THEORY-102 — Proposed; its decoding evidence is one this paper's warning bears on, not tested -->
<!-- inactive-ok-file: THEORY-008 — Proposed; named for why rotation-invariant readout measures cannot see neuron types -->
<!-- inactive-ok-file: THEORY-017 — Proposed; named for the point that a basis is extra structure, which the neuron basis supplies physically -->

# NOTE-549: Rarely categorical, highly separable representations along the cortical hierarchy

## Contribution

A long-running dispute asks whether neurons in an area fall into
functional types ("categorical", as in Hirokawa et al. 2019 for rodent
orbitofrontal cortex) or are diverse and "category-free" (Raposo et al.
2014 for posterior parietal cortex). The studies disagreed on area,
species, task and method. This paper puts one test on every region of a
single brain-wide dataset, the International Brain Laboratory's Brainwide
Map. It then ties what it finds about neurons to the geometry of what the
population represents, through a shared-spectrum argument and an analytic
bound. The answer depends on scale: cortex as a whole is organised into
anatomical types, and most single areas are not.

## Key insight

The same neurons × conditions activity matrix can be read two ways
(Fig. 1a). Its rows, neurons in conditions space, either cluster into
types or do not. Its columns, conditions in neural space, form the
representational geometry. The two clouds have the same spectrum, so
structure in one constrains the other: k tight clusters of neurons act as
k neurons and cap the geometry's dimension near k. Diverse, unclustered
selectivity leaves room for a geometry in which the conditions are in
general position, and then a linear readout can split them in nearly any
way. Within cortical areas the paper finds the second case almost
everywhere.

## Assumptions

- **Data.** IBL Brainwide Map: about 14,000 cortical units from about 180
  Neuropixels sessions across 43 regions; at most 30 sessions per region;
  firing rate between 0.5 and 50 Hz. Only trials from the 80/20 biased
  blocks; trials with first movement later than 0.8 s dropped. Mice,
  trained (the authors say "often over-trained") on one task.
- **Selectivity model.** A reduced-rank regression predicts each neuron's
  z-scored activity from −0.2 to 0.8 s after stimulus onset (10 ms bins)
  from eight z-scored variables: block prior, stimulus side, contrast,
  choice, outcome, wheel velocity, whisker motion energy and licks.
  Coefficients over time are combinations of d = 5 temporal bases shared
  across all neurons and variables; a neuron's selectivity profile α is
  the coefficients summed over time, a point in ℝ⁸. Cross-validated mean
  R² is 0.16 against 0.09 for condition PSTHs (Fig. 2b).
- **Selective neurons only.** ΔR² of the regression over a trial-average
  model ≥ 0.015, which 4,617 neurons pass. The Methods explain why the
  threshold matters: with every neuron included, a peak of unselective
  "junk" neurons at zero makes a single Gaussian null fail and inflates
  the number of categorical areas; with too few, the centre of the
  distribution empties. Results are shown for several thresholds (Extended
  Data Fig. 6b).
- **Categorical.** k-means on α (k = 3–20, 100 initialisations), the k with
  the highest silhouette, clusters dominated (> 90% of silhouette mass) by
  one session removed; then a z-score of that silhouette against 100 draws
  of the same number of points from a Gaussian with the data's mean and
  covariance. Only regions with ≥ 50 selective neurons; Bonferroni P <
  0.05. "Categorical" here means types of *neurons* by response profile,
  not neurons selective for stimulus *categories* in Freedman's sense,
  which the paper and the rebuttal separate explicitly: a strongly
  category-selective neuron may sit on the tail of a Gaussian.
- **Conditions for geometry.** Four binarised variables (whisking above or
  below the session median, block, side, low or high contrast) give 16
  conditions, from 0 to 1,000 ms after onset. Choice and outcome are left
  out because the mice make too few errors when block and stimulus agree.
  Sessions need ≥ 5 trials per condition.
- **Decoding.** Linear SVM (Decodanda), each region resampled to a
  pseudopopulation of N = 4,000 neurons with T = 100 patterns per
  condition, simultaneously recorded neurons kept together; 80% training,
  100 cross-validations.
- **Hierarchy.** The anatomical ordering of Harris et al. (2019) from the
  Allen connectivity atlas, taken as given.

## Key results

- **Region is written into single neurons** (Fig. 2c–f). Region decoded
  from one neuron's time-varying profile at 0.233 accuracy against a null
  of 0.033 ± 0.003 (time-summed: 0.123); module at 0.422 against 0.203 ±
  0.010. Similarity of regions' mean profiles correlates with their
  anatomical connectivity (ρ = 0.40, P = 1.8 × 10⁻¹⁰); pairwise
  decodability anti-correlates with it (ρ = −0.49, P = 3.7 × 10⁻¹⁴).
- **Independent conditions** (Fig. 2i). M_IC runs from 5 (SSp-n) to 16
  (MOs) and rises with hierarchy (ρ = 0.77, P = 0.0005).
- **Within-region categoricality is rare** (Fig. 3d). VISp, AUDp and
  SSp-ul pass, SSp-ll and GU are near the line; silhouette z falls with
  hierarchy (ρ = −0.62, P = 0.004) over about 20 regions. Even VISp's
  clusters are weak in absolute terms (silhouette about 0.23 against a
  null near 0.14–0.18, Fig. 3b). The falling trend survives other ΔR²
  thresholds, the Leiden clusterer and time-resolved profiles (Extended
  Data Fig. 6b–d). Clustering raw rates in conditions space finds VISp and
  AUDp with no hierarchy trend; ePAIRS finds VISp and MOs (Extended Data
  Fig. 6f–i). The rebuttal adds that clustering quality does not
  correlate with a region's neuron count (its Reviewer Fig. 12).
- **Pooling produces types** (Fig. 3e,f; Extended Data Fig. 7). With the
  three categorical regions removed and the 100 best-encoded neurons per
  area: somatomotor z = 8.56, medial 7.84, lateral 2.32 (P = 0.04),
  prefrontal 0.54 (n.s.); whole cortex z = 8.0. Clusters align with area
  or module labels (z-scored Rand index); for example, a whisking-and-
  licking cluster is mostly SSp-n and SSp-m neurons.
- **Diversity and dimension** (Figs 4, 5). α-diversity (participation
  ratio of the neurons × 8 coefficient matrix, subsampled to 120 neurons)
  is about 4.0 in SSp-n and 5.8 in MOs; it tracks M_IC (ρ = 0.73) and
  anti-tracks α-space silhouette (ρ = −0.76). Representation
  dimensionality, the PR of the M_IC condition centroids, rises with
  α-diversity (ρ = 0.67, P = 0.005) and with hierarchy (ρ = 0.79, P =
  0.0003), from 2.0 (SSp-n) to 5.3 (MOs). Computed on single trials the
  PR is 10 to 350, correlated 0.86 with the centroid PR (Methods).
- **Clusters cap dimension** (Methods; Extended Data Fig. 9). The PR of
  the rows of a matrix equals that of its columns. For k Gaussian clusters
  of neurons over M conditions with N → ∞, PR → min(k, M) as within-cluster
  spread vanishes, and PR falls with silhouette at fixed k and M. Across
  regions, conditions-space silhouette predicts lower PR (ρ = −0.77, P =
  0.0004), and the formula predicts measured PR from k, δ and M_IC.
- **Separability** (Fig. 6; Extended Data Fig. 11). Over all 16
  conditions it rises with α-diversity (ρ = 0.69, P = 0.003): SSp-n 0.80,
  GU about 0.67, MOs 0.99. Over independent conditions it is ≥ 0.95 in 15
  of the 16 regions analysed, GU 0.82, and uncorrelated with α-diversity
  (ρ = 0.27, n.s.). Average decodability over independent conditions runs
  from 0.65 (GU) to 0.90 (SSp-n), against a 99th-percentile shuffle
  threshold near 0.53.
- **Synthetic checks** (Extended Data Fig. 8). With P = 16 conditions,
  separability saturates once the latent dimension L reaches about M/2,
  at every noise level, while average decodability keeps rising.
  Stretching one axis of a high-dimensional geometry lowers PR and leaves
  separability intact, so a low PR does not mean low separability.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Within most single regions of mouse cortex, neurons' selectivity to the eight IBL variables is no more clustered than a covariance-matched Gaussian; only VISp, AUDp and SSp-ul are | strong for this task and variable space | Fig. 3d; robust to threshold, clusterer and time resolution (Extended Data Fig. 6b–d); two other pipelines also find few categorical regions |
| C2 | Categoricality falls along the anatomical hierarchy | moderate | ρ = −0.62 over about 20 regions in α space; not reproduced in conditions space, and ePAIRS flags MOs (Extended Data Fig. 6f,g) |
| C3 | Pooled across modules or the whole cortex, selectivity is categorical and aligned with anatomy | moderate | Fig. 3e,f, Extended Data Fig. 7; a pool of regions with different mean profiles is a mixture, so rejecting a single-Gaussian null is close to expected; the Rand index shows the clusters partly are the regions |
| C4 | A neuron's region is decodable from its selectivity, and functional similarity tracks anatomical connectivity | strong | Fig. 2d–f, shuffle nulls |
| C5 | The number of conditions a region distinguishes rises along the hierarchy | moderate | ρ = 0.77 over 16 regions; threshold robustness (0.6, 0.666, 0.7) shown only in the rebuttal (Reviewer Figs 8, 9) |
| C6 | Tightly clustered neurons cap the condition geometry's PR near the number of clusters | strong as mathematics in its limit; moderate as a fit | shared spectrum of XXᵀ and XᵀX; large-N Gaussian-cluster derivation; Extended Data Fig. 9c–e |
| C7 | Response diversity predicts representation dimensionality and separability over all conditions | moderate | ρ = 0.67 and 0.69 over 16 regions; synthetic support (Extended Data Fig. 8e) |
| C8 | Over the conditions each region distinguishes, nearly every balanced dichotomy is linearly separable in every region | moderate as worded | 15 of 16 regions ≥ 0.95, GU 0.82; "separable" means above a shuffle null, on 4,000 resampled neurons; pairwise decodability was imposed by the merging step, so failure needs near-degenerate geometry |
| C9 | So decodability of a chosen variable "often lacks significance" | moderate | a generalisation from C8; the paper's own collinear example (Fig. 6a, middle) shows where it fails |
| C10 | Cortex "prioritize[s] diversity over categorical structure" | weak (interpretive) | inferred from C1 and C8 in one overtrained task; the Limitations name alternatives |

## Method

1. Fit the reduced-rank regression; take α as the time-summed
   coefficients.
2. Test clustering of α, region by region and in pools, against the
   matched Gaussian null; repeat in conditions space against a log-normal
   null and with ePAIRS (median nearest-neighbour angle against 5,000 null
   draws).
3. For each region, decode every pair of the 16 conditions, call pairs
   below 0.666 dependent, merge the largest clique of mutually
   undecodable conditions (Bron–Kerbosch), and repeat until all pairs are
   decodable; the count left is M_IC.
4. Compute α-diversity and the PR of the condition centroids.
5. Draw 200 random balanced dichotomies of the M or M_IC conditions, each
   condition balanced within its side; decode each with a cross-validated
   linear SVM; separability is the fraction above the 99th percentile of
   200 label-shuffled runs, average decodability the mean accuracy.

## Concepts

- **Categorical representation**: neurons whose response profiles cluster
  into types (the usage of Raposo et al. 2014, Hirokawa et al. 2019),
  tested against a single Gaussian with matched mean and covariance.
- **Uneven selectivity**: some variables are encoded much more strongly
  than others, so the cloud of profiles is elongated. The dominant
  structure in most regions.
- **Explicit and implicit modularity**: segregated neuron types versus the
  same activity-space geometry rotated, with no types. The paper says the
  two have the same computational properties.
- **M_IC**: the number of condition groups left after merging conditions
  the region cannot tell apart.
- **Representation dimensionality**: (Σλ)²/Σλ² of the centroid covariance;
  an embedding dimension, not an intrinsic one.
- **Separability**: the fraction of balanced dichotomies decodable above a
  shuffle null. Called "shattering dimensionality" in the submitted
  version; renamed in review because Bernardi et al. (2020) used that name
  for **average decodability**, the mean accuracy over dichotomies.

## Connections

The paper continues Fusi's mixed-selectivity programme: Rigotti et al.
(2013) and Fusi, Miller and Rigotti (2016) argued that diverse, mixed
selectivity gives high-dimensional representations that a linear readout
can use flexibly, and Bernardi et al. (2020) introduced the dichotomy
measures it reuses. Its categoricality test descends from PAIRS and ePAIRS
(Raposo et al. 2014; Hirokawa et al. 2019). Referee 5 calls it a
correction of Hirokawa et al.'s orbitofrontal result; the paper itself
notes the disagreement without saying so. Its Discussion finds agreement
with Khosla et al. on privileged axes at mesoscale and not locally, and
with Dahmen et al. on dimension rising up the visual hierarchy. It cites
RNN work in which simple tasks need no clusters and complex multi-task
training produces them (Yang et al. 2019; Dubreuil et al. 2022; Driscoll
et al. 2024; Johnston and Fusi). None of these is held in this record.

## Bearing on the record

- **A THEORY, filed with this reading.** Within single areas of mouse
  cortex during one decision task, neurons do not form discrete types
  beyond a few primary sensory areas, yet the conditions each area tells
  apart are separable in nearly every way. Single source.
- **[THEORY-083](../theory.d/THEORY-083.md) (neural collapse) is not contradicted.** It describes
  *conditions* collapsing to class means arranged as a simplex
  equiangular tight frame in feature space: in this paper's terms, maximal
  M_IC with maximal dimension, the arrangement that is separable in every
  way (Fig. 6a, right). This paper's "categorical" is about *neurons*
  forming types. Neural collapse is invariant to rotating the units, so
  it says nothing about types. By C6, a collapsed C-class layer whose
  units formed k tight types would need k ≥ C − 1. A referee listed neural
  collapse among work on "categorical representations" in the stimulus-
  category sense; the published reference list does not cite it.
- **[THEORY-102](../theory.d/THEORY-102.md) and its source, [LIT-644](../literature.d/LIT-644.md).** C9 is a caution for any
  account resting on decoding a chosen variable. Vishne et al.'s evidence
  is near-ceiling, time-generalising decoding plus exemplar geometry, not
  above-chance decoding of one label, so the caution qualifies rather than
  undercuts it.
- **[THEORY-008](../theory.d/THEORY-008.md)** (decodable information is a function of the
  kernel) explains why separability cannot distinguish explicit from
  implicit modularity: rotating the units leaves the kernel, and every
  readout measure, unchanged. **[THEORY-017](../theory.d/THEORY-017.md)** says a basis is structure
  supplied from outside the space. In a brain the neuron basis is
  physically given, which is what makes "are there neuron types?" a
  question with an answer.
- **No ML instruction.** Nothing here belongs in the anthology beyond what
  it already holds.

**The anthology's reading, compared** (per [ADR-013](../decisions.d/ADR-013.md); reported here, not
fixed across the boundary). The anthology's close reading (`NOTE-353` in
that record) agrees with this one on every number checked, and its
critique of C3 and C8 is adopted above. Three differences:

1. [ANTH-LIT-696](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-696.md)'s standing paragraph says the paper measures "whether
   concepts sit in categorical clusters or in separable, mixed-selective
   codes". That runs the two spaces together. The paper's "categorical"
   is about neurons clustering by response profile, not conditions or
   concepts clustering in activity space; conditions that clustered
   tightly in activity space would show up as a low M_IC. The anthology's
   note itself defines the term correctly.
2. Its `published: '2024-11-01'` is the preprint's month. Crossref gives
   the preprint a full posting date, 17 November 2024, and the scheme's
   date rule takes the first of the month only when no source gives a
   day.
3. Its LIT body still carries the seed's takeaway, "every area is
   maximally linearly separable", which its own reading corrects to 15 of
   16 analysed areas.

## Limitations

- **One task, eight variables.** "Rarely categorical" means no types
  within the IBL variable space; tuning to anything the task does not vary
  is invisible (Referee 3, now in the Limitations). Overtrained mice and a
  simple task; the authors expect more clustering in multi-task settings.
- **Coverage.** Clustering covers the regions with ≥ 50 selective neurons
  (about 20) and geometry the 16 with enough trials per condition, of 43
  in the dataset. The geometry set includes only three prefrontal regions
  (ACAd, PL, ORBl).
- **Lenient separability.** Above a shuffle null at about 0.53, on 4,000
  resampled neurons and 100 pseudo-trials; the rebuttal shows separability
  rising with T/N before converging, tested only in VISp. Merging to
  pairwise-decodable conditions removes the main route to failure, and the
  synthetic results show separability is blind to anisotropy.
- **"High-dimensional" is relative.** PR over independent conditions is at
  most 5.3, for 16 conditions in MOs; "high" means not near-degenerate.
- **The mesoscale result is partly expected from pooling** (C3).
- **Correlations over 16–20 regions**, with bootstrap intervals on the
  regression lines and no models of session or animal effects.
- **Only response profiles.** Spontaneous activity and transcriptomic cell
  types are not analysed; the authors raise both as places where types
  might show.

## Open questions

- Does "rarely categorical" survive a multi-task or less-trained
  recording analysed with the same pipeline?
- Is there structure within a module beyond the differences between
  region means, for example after subtracting each region's mean profile?
- Do transcriptomic types map onto response-profile clusters anywhere
  beyond primary sensory cortex?
- How do separability and cross-condition generalisation (abstraction)
  trade off in the same regions? This paper measures only the first.
