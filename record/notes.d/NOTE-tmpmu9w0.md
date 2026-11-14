---
status: Read
paper: LIT-tmpruadv
title: 'Sun et al. — Phase transition in a dryland shrub–grass ecosystem'
version: 2
history:
- version: 1
  date: '2026-11-14'
  note: >-
    Read in full on 2026-11-14 from the publisher's PDF (10 pages, CC BY
    4.0), which the owner uploaded to the session after pnas.org's
    Cloudflare check stopped the fetch. Text extracted with pdftotext;
    figures read from their captions. Read: the abstract, significance
    statement, introduction, all four Results and Discussion sections,
    the conclusion, Materials and Methods with Table 1, and the reference
    list. Not read: the SI Appendix (Fig. S1, the comparison with the
    Ising model; Fig. S2, hysteresis from different initial
    configurations; Fig. S3), Dataset S1 and the Zenodo code
    (doi:10.5281/zenodo.23751909), none of which is in the PDF. Page
    numbers are the article's.
- version: 2
  date: '2026-11-14'
  note: >-
    At the owner's request the authors' archived code (Zenodo
    10.5281/zenodo.23751909, CC BY 4.0) was read and its update rules
    reimplemented and rerun the same day; see the section "The authors'
    code, rerun". The supposed inconsistency in the survival thresholds
    is withdrawn: the code computes the net effect as a competition load,
    so Table 1's H_g = 1.1 > H_s = 1.0 means grasses tolerate more
    competition, as the text says, and the text's "Hg < Hs" uses the
    opposite sign for NE. The Assumptions, Limitations and Open questions
    are corrected to match; nothing else in the reading changes.
date: '2026-11-14'
summary: >-
  A field survey along a rainfall gradient at the desert margin of
  northern China and a kernel-based probabilistic cellular automaton. In
  the model, shrubs deplete resources weakly over a wide radius and
  grasses strongly over a narrow one; along rising resource supply this
  gives shrub patterns, a bistable interval, then grass patterns, which
  the authors call a first-order phase transition and match to a shift
  they observe within 180–250 mm of annual rainfall. Fairy circles are
  produced by an imposed contraction of the shrub kernel and read as
  metastable; cover at the desert edge falls with disturbance along a
  fitted power law read as a continuous transition. The phase-transition
  vocabulary is applied by analogy; the model's bistability is shown, the
  field's is inferred from alternation between plots.
---

<!-- inactive-ok-file: LIT-720 — Unavailable; cited by the paper as its foil, named here only to place it -->

<!-- inactive-ok-file: CASE-tmpjrrhk — Proposed; the fairy-circle rerun, the assistant's study, cited in the section on the code -->

# NOTE-tmpmu9w0: Sun et al. — Phase transition in a dryland shrub–grass ecosystem

## Contribution

A minimal spatial model in which two plant types differ only in their
interaction kernels (the range and strength of the resource depletion
each causes around itself, plus a short-range facilitation) and in the
competition each can survive. Run along a resource-supply gradient, it
produces patterned shrubland, a bistable interval, and patterned
grassland. The authors pair it with a 30-site, 55-plot field survey and
trait data, and recast the whole as a phase-transition description:
precipitation as an external field, the shrub–grass shift as first
order, fairy circles as metastable states near it, and the
vegetation–desert edge as a continuous, disorder-driven transition.

## Key insight

A trade-off in *spatial scale* of foraging, wide and weak against narrow
and strong, is enough for two plant types to exclude each other locally
and so to switch abruptly, with hysteresis, as resource supply changes.
The authors call it the EI trade-off, extensive against intensive.
Nothing at the landscape scale needs to feed back on the drivers. The
switch is in the kernels.

## Assumptions

- **The landscape is homogeneous apart from rainfall.** The sites were
  chosen for sandy soil, flat terrain and little human disturbance, and a
  covariate analysis found that soil variables and elevation had mostly
  no significant partial effects once precipitation was controlled. The
  authors conclude more than this shows: "This indicates that the
  observed spatial patterns reflect a pure self-organization process,
  with environmental heterogeneity effectively ruled out" (p. 8).
- **Rival feedbacks are absent.** Fire is absent from the protected
  areas; there is "no clear gradient in wind or soil erosion" along the
  east–west transect; microclimate "struggle[s] to explain" the patterns
  (p. 4). These are asserted, not measured in the paper.
- **The model.** A 200 × 200 lattice, periodic boundaries, synchronous
  update, three states per cell (shrub, grass, bare). Global random
  dispersal with probability R = 0.5. The interaction field is the
  convolution of each type's distribution with its kernel. Competitive
  strength is K− = c/(n−·s), where c is the plant's resource demand, n−
  the number of cells within its depletion radius r−, and s the
  per-cell resource supply (Eq. 1). Facilitation has a constant
  strength K+. A plant whose net effect NE is below its threshold H
  survives with probability 1 − k(H − NE), truncated to [0, 1]. Table
  1: r_s− = 20, r_g− = 3; c_s = 5, c_g = 3; r_s+ = 4, r_g+ = 1; K+ =
  0.01; H_s = 1.0, H_g = 1.1; k = 0.5; s scanned from 0 to 2.0.
- **How the thresholds are signed.** The text says grasses "tolerate
  more severe resource competition, whereas shrubs require a higher
  resource threshold for survival" (p. 5) and that "Grasses have a lower
  threshold than shrubs (Hg < Hs)" (p. 8), while Table 1 gives H_g = 1.1
  and H_s = 1.0. The code settles it: there the net effect is a
  competition load and survival is 1 − k(NE − H), so the higher H_g
  means grasses tolerate more competition. The text's formula writes NE
  with the opposite sign, under which "Hg < Hs" says the same thing. The
  two agree; only the sign convention differs.

## Key results

- **The field shift** (p. 3, Fig. 2 B–H). Total cover rises linearly
  with rainfall, but composition shifts from shrub to grass "within a
  narrow precipitation window of 180 to 250 mm mean annual precipitation
  (MAP)", where plots alternate between shrub and grass dominance. Patch
  size and nearest-neighbour distance "decline sharply once grasses
  become dominant", and the skewness of both "increases rapidly" in the
  window. The authors read these together as "hallmarks of a first-order
  phase transition, analogous to magnetization reversal in the Ising
  model under an applied magnetic field" (p. 3). The window falls at an
  aridity index of about 0.8, which they align with global aridity
  thresholds (Berdugo et al. 2020).
- **The model's bistability** (p. 4, Fig. 3C). From random starts at
  density 0.01 each, after 1,000 iterations "Shrubs dominate in drier
  areas and grasses in wetter areas, whereas in the transition zone
  either can win by excluding the other." Hysteresis from different
  initial configurations is reported in SI Fig. S2, which was not read.
- **Patterns** (p. 5, Fig. 3 D–E). Each type forms its own stable
  pattern. Short-range positive and long-range negative effects in the
  kernels are the "scale-dependent feedbacks" of the pattern-formation
  literature. In the field, shrub patches are larger and more widely
  spaced than grass patches, and both grow with aridity.
- **The trait test** (p. 5, Fig. 2 I–J). Plots are projected onto a
  conservative-to-acquisitive trait axis, found by k-means (k = 2)
  anchored on SLA and leaf dry mass. Patch size and nearest-neighbour
  distance regress on the projection with R² = 0.35 and 0.42 in the
  PC1–PC2 plane, and 0.41 and 0.48 in the PC2–PC3 plane (all P <
  2 × 10⁻⁶). The PC2–PC3 plane is described as "having removed the
  variation associated with the precipitation gradient".
- **Fairy circles** (pp. 5–7, Fig. 4 A–C). In the field, hollow shrub
  rings in a grass matrix occur "exclusively within the shrub–grass
  transition zone". The simulation starts from "a critical shrub spot
  pattern", increases s, "halved the shrub negative interaction radius
  rs−, and disabled shrub dispersal" (p. 9). The resulting hollow rings
  are read as metastable, like supercooled water, and as a case of
  "evade tipping" through patterning (Rietkerk et al. 2021). Bare-soil
  circles around shrub patches before hollowing are reported as new.
- **The desert edge** (p. 7, Fig. 4 D–E). Boundary vegetation (nebkhas
  of *Nitraria*, *Artemisia ordosica*) has larger patches, modelled by
  adding clonal local recruitment (radius 4, probability 0.2) and a
  wider shrub kernel. Under random removal of intensity D, simulated
  cover follows C ∼ (Dc − D)^β, and "R2 > 0.9 was considered as
  evidence for power-law behavior" (p. 9). The authors call this "a
  disorder-driven continuous (second-order) phase transition" (p. 7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The kernel model has a bistable interval in resource supply where either type excludes the other depending on initial configuration | moderate | Fig. 3C; SI Fig. S2 (unread); code archived |
| C2 | The field shrub–grass shift is a first-order phase transition | weak | alternation between plots, nonlinear cover change and rising skewness; none is specific to first-order transitions, and no field hysteresis is shown |
| C3 | The EI trade-off is "empirically validated" | weak to moderate | regressions of patch size and spacing on a trait axis (R² 0.35–0.48); kernel radii and strengths are not measured |
| C4 | Fairy circles are metastable configurations near the first-order threshold | weak | a scenario imposed by hand (radius halved, dispersal off) reproduces the shape; no lifetime or escape from metastability is shown |
| C5 | Cover at the desert edge vanishes by a continuous transition | weak | a power-law fit with a free critical point, judged by R² > 0.9; no finite-size scaling |
| C6 | Conservative traits are a by-product of extending the foraging range, not an adaptive strategy | interpretive | argued in the discussion (p. 5), not tested |

## Method

The field survey covered 30 sites 50–100 km apart, with paired natural
and boundary plots, and 25 more natural plots 3–10 km apart within the
transition window. Rainfall comes from the CWEP-2P product at 0.25°
resolution, bilinearly interpolated. Drone orthomosaics were taken at
each site, and on each 50 random patches were fitted by hand as ellipses
in ImageJ by a single operator. Patch size is the minor axis, because
labyrinthine patches have no measurable major axis. Thirteen traits come
from quadrats. The model is described under Assumptions.

## Concepts

- **EI trade-off**: the trade-off between extensive resource foraging
  (wide range, weak per-unit depletion, perennial woody biomass) and
  intensive foraging (narrow range, strong depletion, high efficiency).
  The authors offer it as the "fundamental" trade-off behind the
  conservative–acquisitive spectrum.
- **Interaction kernel, interaction field**: a plant's signed influence
  as a function of distance, and the convolution of all plants with
  their kernels. Each cell's fate depends on its net value there.
- **Phase**: "a macroscopically uniform state" (p. 2). Desert,
  shrubland and grassland are the phases. A phase's "structure" is its
  stable spatial pattern.
- **External-field-driven first-order transition** against
  **disorder-driven continuous transition**: precipitation as the field
  that tilts between two ordered vegetated states, and disturbance as
  the disorder that destroys spatial order. These are the authors'
  mappings onto the Ising model; the mechanistic comparison is in SI
  Fig. S1, which was not read.
- **Spot-origin hypothesis**: fairy circles arise from shrub spots
  hollowed out when grass competition shrinks the shrubs' foraging
  range.

## Connections

The paper's foil is the macroscopic feedback framework of regime shifts
(Scheffer et al. 2001, [LIT-720](../literature.d/LIT-720.md); Dakos et al. 2019), which it calls
"effective for prediction" but not an explanation from individuals. Its
pattern mechanism is the scale-dependent feedback of Rietkerk et al.
(2002) and Pringle & Tarnita (2017). It uses depletion-range kernels
like those of Martinez-Garcia et al. (2023, their ref. 34) and Cabal et
al.'s root segregation (2020). Spatial skewness as a warning comes from
Guttal & Jayaprakash (2009), and the paper also cites Scheffer et al.
(2009), [LIT-1956](../literature.d/LIT-1956.md). The fairy-circle reading engages Guirado et al. (2023)
on their global distribution and Rietkerk et al. (2021) on evading
tipping. "Turing-like" names the morphology. The mechanism is not
diffusion-driven instability of a homogeneous state ([THEORY-543](../theory.d/THEORY-543.md)) but
kernel competition on a lattice.

## Bearing on the record

- **[QUESTION-281](../questions.d/QUESTION-281.md)** (by which transitions do forms come into being and
  pass away). The paper names, for one system, three different routes:
  a field-driven switch with bistability between two patterned states;
  a continuous loss of order under disturbance; and a metastable form
  (the hollow ring) held near a threshold. In the fairy circles it
  separates the making of the form (hollowing, when the foraging range
  contracts) from what keeps it ("shrubs utilize resources from the
  central hollow to counter the siege by surrounding grasses", p. 6).
  That bears on the question's creation-against-stabilization
  distinction. It does not answer it, because the contraction is
  imposed in the simulation rather than arising, and stability is
  asserted rather than tested. Filed as `bears_on`, with a dated note on
  the question.
- **[THEORY-1315](../theory.d/THEORY-1315.md)** (critical slowing and its warning signals). The paper
  uses rising spatial skewness as one of the hallmarks of a first-order
  transition. [THEORY-1315](../theory.d/THEORY-1315.md) holds that such signals mark nearness to a
  broad class of thresholds, "not which kind". On that account the
  skewness supports nearness to some threshold and not the first-order
  reading, which rests on the model's hysteresis. Dated note filed on
  [THEORY-1315](../theory.d/THEORY-1315.md).
- **[LIT-726](../literature.d/LIT-726.md), [LIT-2165](../literature.d/LIT-2165.md), [THEORY-1468](../theory.d/THEORY-1468.md)** (regime shifts and restoration).
  The paper offers a bottom-up alternative to the feedback account those
  hold. It does not test it against them: it argues the feedbacks are
  absent at its sites without measuring them. No note is filed on
  these; the contrast is recorded here.
- **[THEORY-543](../theory.d/THEORY-543.md), [LIT-527](../literature.d/LIT-527.md)** (Turing; Cross–Hohenberg). "Turing-like" is
  used for the pattern and not for the mechanism. No note filed.

## Limitations

- **"Phase transition" is applied by analogy.** In the model, bistability
  and hysteresis are shown, which supports a discontinuous transition.
  In the field, nothing distinguishes a first-order transition from a
  steep but smooth turnover across heterogeneous plots: there are no
  time series, no repeat visits, and no plots on both sides of the
  window under the same rainfall followed through time.
- **The covariate analysis is overread.** Finding no significant partial
  effects of mapped soil variables and elevation does not rule out
  environmental heterogeneity. The soil grid is coarse, and grazing
  history, groundwater and the rainfall product's own error are not
  examined.
- **The fairy-circle result is a scenario.** Halving the shrub kernel and
  switching off dispersal is the hypothesis put in by hand. The model
  does not produce the contraction from grass competition. "Metastable"
  is not tested: no lifetime, no escape rate, no perturbation.
- **The power law is weakly identified.** A three-parameter fit with a
  free critical point, judged by R² > 0.9, cannot tell a power law from
  other concave declines. There is no finite-size scaling or
  lattice-size check.
- **The trait test is correlational and indirect.** Kernel range and
  strength are not measured: there are no root data. The trait axis is
  built with SLA and LDM as anchors. Patch size and spacing are
  themselves the pattern the model is tuned to produce.
- **Undisclosed parameters and a boundary mismatch** (from the code). The
  fairy-circle scenario starts from a spot pattern grown with shrub
  radius 40, facilitation 0.05 and shrub mortality scaling 5, none of
  which the paper reports. The convolution pads mirror-symmetrically,
  where the Methods say periodic. The rerun found the second makes
  little difference.
- **"Minimal set of assumptions"** (p. 2) is asserted. The only ablation
  reported is that the facilitation asymmetry "is not essential for
  phase transition" (p. 8).
- Patch measurement is manual, with 50 patches per site and one
  operator.

## Open questions

- Is the interval robust to lattice size and to local rather than
  global dispersal? With global dispersal, the model has no spatial
  seeding to carry a front.
- Would repeat surveys of the transition-window plots show the
  alternation persisting (bistability) or drifting with rainfall
  (turnover)?

## The authors' code, rerun

On 2026-11-14 the authors' notebooks were read and the update rules of
`ShrubGrassTransition.ipynb` and `FariyCircle.ipynb` reimplemented and
checked against them line by line. The runs were made in the session's
scratchpad and are not committed, since this record holds no code. All
runs used a 200 × 200 lattice, Table 1's parameters and 1,000 steps,
unless stated.

- **From sparse random starts** (density 0.01 each, as in Fig. 3C; four
  seeds per s, s = 0.40–0.98 in steps of 0.02). Shrubs win at every s ≤
  0.68 and grasses at every s ≥ 0.76. Between them (s = 0.70–0.74) the
  seeds split: some end in shrubland, some in grassland, some still mixed.
  This reproduces Fig. 3C's "either can win". With periodic boundaries
  (two seeds) the split moves to s ≈ 0.66–0.68.
- **Against invasion** (an established shrubland grown at s = 0.5, or
  grassland at s = 0.95, seeded with 1% of the other type on empty cells;
  two seeds; s = 0.40–0.96 in steps of 0.04). Established shrubland
  excludes the invading grass at every s tested; grass survives only at
  0.1–0.3% at high s. Established grassland excludes invading shrubs at
  every s ≥ 0.48, and shrubs take over at s ≤ 0.44. **The model is
  bistable from s ≈ 0.48 to at least 0.96**, a far wider interval than
  the narrow split from random starts. That split is the point where a
  race from near-empty ground ties, not the edge of the bistable region.
  Without invaders, either established state persists at every s,
  because dispersal comes only from plants already present, so an extinct
  type never returns.
- **Facilitation removed** (K+ = 0, two seeds). Random starts still
  split near s ≈ 0.68–0.70, and established states still persist. Shrubs
  still form a regular pattern: the radial power spectrum peaks at a
  wavelength of about 25 cells, 273 times its median (570 times with
  facilitation; 1.5 for a shuffled control). Grass shows a weak
  periodicity of about 3.6 cells either way. Both wavelengths are about
  1.2 times the competition radius (20 and 3), the range Martinez-Garcia
  et al. give for competition-only patterns. **Competition alone makes
  the patterns and the switch**, so "scale-dependent feedback" is not
  needed to describe this model.
- **Fairy circles.** Run in [CASE-tmpjrrhk](../cases.d/CASE-tmpjrrhk.md). The rings are made by the
  kernel contraction imposed by hand, with or without grass, and grass
  erodes them. The notebook stops at 200–500 steps, before most of the
  decay.

What follows for the paper:

- The THEORY's `promote_when` is met. Bistability is shown, under the
  code's threshold convention, which is also the paper's.
- The match of the model's switch to the field's narrow 180–250 mm
  window rests on the random-start race point. By the model's own
  hysteresis, an established shrubland would persist far into wetter
  conditions than the window. If the field transition is the model's,
  the narrow window needs an account the paper does not give: an
  establishment history like the race, or immigration from outside.

