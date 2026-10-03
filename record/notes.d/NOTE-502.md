---
number: 502
status: Read
formerly:
- NOTE-tmphy0l9
paper: LIT-638
title: 'Interacting spiral wave patterns underlie complex brain dynamics'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the typeset PDF on co-author Feng's Warwick page:
    main text, Figs. 1–8, Methods (data, scale selection, phase and
    vorticity fields, spiral detection and boundary, null model,
    classifiers, streamlines, phase-oscillator model) and Extended Data
    captions. Supplementary Videos and Supplementary Information were not
    seen. Figure values are taken from the text and captions only.
date: '2026-10-03'
summary: >-
  Phase fields of 0.01–0.1 Hz HCP fMRI on the flattened cortex hold about
  16 spirals per hemisphere at rest (radius 10.5 ± 4.8 mm), centred on
  phase singularities that move at 2.2 mm/s with superdiffusive exponent
  β ≈ 1.5 and sit on functional boundaries. Opposite spirals annihilate
  (51% fully, 46% partly), like ones repel (2.6%). Spiral centres and
  charges decode four language conditions at 48.3% (chance 25%,
  raw-amplitude decoder 30.2%), and spiral pairs act as gates and walls
  that route task activity flow.
---

<!-- inactive-ok-file: NOTE-418 — Skimmed; the reading of Cross & Hohenberg, cited only for its statement that defects of broken phase symmetry are established in laboratory systems -->
<!-- inactive-ok-file: LIT-647 — Deferred, paywalled; named as the companion review, not leaned on -->

# NOTE-502: Interacting spiral wave patterns underlie complex brain dynamics

## Contribution

Rotating waves had been seen locally in cortex (spindles, turtle and
marmoset LFP, monkey prefrontal cortex, rodent slices) and one global
rotation in arousal-averaged fMRI. This paper finds many small, mobile
spirals coexisting across the whole human cortex in moment-to-moment fMRI,
characterises their motion and pairwise interactions as defect dynamics,
and links their configuration to tasks: it decodes task condition from
them, and reads task-specific routing of activity flow from their
arrangement.

## Key insight

Treat the phase of slow cortical fluctuations as a field on a sheet and
look for its topological defects. A defect is a spiral, and its rotation
sense is a charge of ±1. Charges move, collide and annihilate as defects
do in excitable and turbulent media. Because a spiral sets the direction
of flow around it, flipping the sense of a few spirals at region
boundaries reverses the flow through a whole region without building a new
pattern. On this picture the brain switches the direction of large-scale
traffic, bottom-up or top-down, by re-signing its defects.

## Assumptions

- **Data**: HCP minimally pre-processed fMRI, 2 mm CIFTI grayordinates
  (about 32,000 vertices per hemisphere) on the HCP flat map. Three random
  cohorts of 100 (rest, language, language replication) and 100 subjects
  doing the working-memory task.
- **Filtering**: 4th-order zero-phase Butterworth, 0.01–0.1 Hz;
  difference-of-Gaussian spatial band-pass at scales from geometric
  eigenmode wavelengths. The analysis scale, 70–138 mm, is the band where
  spiral-based **task classification is highest** (Methods).
- **Phase field**: Hilbert phase per voxel; phase vector field V = ∇φ by
  circular central differences; vorticity ω = ∇ × V; spiral cores where
  |curl| > 1 and clusters of at least 3 × 3 voxels; boundaries grown while
  phase vectors stay within 45° of the circle's tangent; boundaries then
  manually inspected.
- **Null model**: 3-D (x, y, t) Fourier phase randomisation, preserving
  spatial and temporal autocorrelation. Spatial filtering makes spirals
  appear in the null too, so a spiral time step counts only if its
  filtered–unfiltered phase similarity (share of voxels within 30°)
  exceeds the null's 95th percentile.
- **Flattening**: the authors concede that the flat map does not preserve
  distances and that a wave reverberating round a sulcus could appear as a
  spiral; they test spiral density against sulcal depth and find no bias.
- **Model**: a 30 × 30 lattice of Kuramoto-type phase oscillators with
  nearest-neighbour sine coupling and random initial phases; spirals are
  reversed by φ → π − φ inside their boundaries.

## Key results

- **Prevalence and size** (Fig. 2). 16.33 ± 2.22 spirals per time step in
  the left hemisphere at rest (18.8 ± 2.6 during the task); radius
  10.46 ± 4.77 mm; 62% span more than one of 22 regions; amplitude falls
  towards the singularity; density highest on region and network
  boundaries, not dependent on gyri, sulci or inflections (Extended Data
  Fig. 2).
- **Motion** (Fig. 3). Angular speed 0.36 ± 0.31 rad/s, heavy-tailed;
  propagation 2.19 ± 1.80 mm/s; MSD ∝ τ^β with β between 1 and 1.9 (mean
  1.5) for 96% of trajectories; centres travel up to about 10 cm.
- **Interactions** (Fig. 4). Full annihilation 51.04%, partial
  annihilation 46.40%, repulsion 2.55%. Full annihilation leaves a plane
  wave travelling opposite to the pre-collision flow. Cross-scale
  intersection ratios exceed the null for all scale pairs (P < 0.001) and
  peak late in a spiral's life.
- **Task specificity** (Figs. 5–6). Story versus math listening reverses
  dominant rotation at the PCC/dorsal-stream/superior-parietal border, with
  the opposite sense in the homologous right-hemisphere region. Contrast
  maps are hemispherically symmetric (r = 0.63 listening, 0.66
  answering) and strongest in frontoparietal, dorsal-attention and
  default-mode networks (auditory too when answering).
- **Decoding**. Four conditions at 48.33 ± 0.31% (replication 50.35%),
  null 24.32%, raw-amplitude decoder with matched input 30.2%. Working
  memory: stimulus type 43.72% (chance 25%), 0-back versus 2-back 66.72%,
  correct versus incorrect 58.96% (chance 50%).
- **Unfiltered signals** (Fig. 7). Trial-averaged, unfiltered task-evoked
  fMRI shows spirals at the same places and senses as the filtered data;
  PCA of the signal round a spiral traces a rotation in the first two
  components, which explain over 80% of variance.
- **Activity flow** (Fig. 8). Opposite pairs make S-shaped "gates",
  like pairs saddle-shaped "walls". During math listening four spiral
  clusters route flow from primary auditory to lateral temporal cortex;
  during answering seven route it the other way, through DMN, FPN and
  DAN back to primary auditory cortex. A local phase-vector classifier
  separates the two sessions best inside this "region of coordination".
  In the lattice model, annihilation is again the commonest interaction,
  and reversing selected spirals reverses the flow between them
  (Extended Data Fig. 9).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Slow cortical fMRI phase fields contain many coexisting spirals around phase singularities, beyond what filtering of autocorrelated noise produces | moderate to strong: a phase-randomised null with a filtered–unfiltered similarity test, replicated in unfiltered task averages; flat-map distortion argued against, not excluded | Figs. 2, 7; Extended Data Figs. 1–2 |
| C2 | Spiral centres move superdiffusively and interact as topological defects (annihilation of opposite charges, repulsion of like ones) | moderate: descriptive statistics over 100 subjects; interaction categories defined by the authors | Figs. 3–4 |
| C3 | Spiral locations and rotation senses carry task information beyond raw fMRI amplitude | moderate: above chance and above a matched amplitude decoder, replicated in a second cohort, but the analysis scale was chosen to maximise this decoding | Fig. 6; Methods |
| C4 | Interacting spirals coordinate correlated activation and deactivation and route task activity bottom-up or top-down | weak to moderate: read from trial-averaged streamlines and a phenomenological model; no perturbation of spirals in the brain | Fig. 8; Extended Data Figs. 7–9 |
| C5 | Transitions between functional network states are continuous, not discrete switches between metastable states | weak: an interpretation of C4, not tested against a state-switching model | Discussion |
| C6 | Brain spirals are "essential" to brain function and computation | speculative: stated as "might be" | Discussion |

## Concepts

- **brain spiral**: a localised rotational wave in the phase field, with
  high vorticity at its centre and a phase singularity there.
- **phase singularity / topological charge**: a point round which the
  phase winds by ±2π; charge +1 or −1 by rotation sense (the paper calls
  anticlockwise positive vorticity).
- **phase vector field**: the spatial gradient of the phase map, read as
  the local direction of activity flow.
- **full annihilation / partial annihilation / repulsion**: the three
  pairwise interaction types (Methods).
- **region of coordination (ROC)**: a region whose task-specific flow is
  set by the spirals that encircle it.
- **superdiffusion**: mean-squared displacement growing as τ^β with β > 1.

## Connections

- **Belousov–Zhabotinsky ([LIT-531](../literature.d/LIT-531.md), [NOTE-414](NOTE-414.md))** and **Cross & Hohenberg
  ([LIT-527](../literature.d/LIT-527.md), [NOTE-418](NOTE-418.md)).** Annihilating waves and spirals at broken fronts in
  BZ, and defects of broken phase symmetry in non-equilibrium patterns, are
  the physics these objects belong to. The paper cites Kuramoto and Coullet
  et al., not these.
- **Turing 1952 ([LIT-535](../literature.d/LIT-535.md), [NOTE-427](NOTE-427.md)).** Travelling waves are Turing's case
  (e) and need at least three morphogens; the analogy to cortex is only
  that propagating patterns come from a reaction–diffusion-type medium,
  which this paper does not model.
- **Vohryzek et al. 2022 ([LIT-080](../literature.d/LIT-080.md), [NOTE-054](NOTE-054.md)).** Rival description of
  non-stationarity (C5): discrete substates with dwell times versus
  continuous spiral-organised flow.
- **Kelso 2021 ([LIT-601](../literature.d/LIT-601.md)).** Phase-oscillator coordination; its
  metastability is relative coordination, compatible with C5.
- **Verzhbinsky et al. 2026 ([LIT-633](../literature.d/LIT-633.md)).** Coordination by synchronous
  bursts rather than propagation, at a timescale three orders faster.
- **Muller et al. 2026 ([LIT-647](../literature.d/LIT-647.md)).** The companion review on
  travelling waves, unread.

## Bearing on the record

- First reading in the record to claim that defect dynamics of the kind
  documented in BZ and in pattern-formation theory organise brain
  activity. A THEORY on large-scale cortical dynamics as an excitable
  medium could cite it, with a second source from electrophysiology.
- Bears on [LIT-080](../literature.d/LIT-080.md)'s landscape picture as a rival (C5); no THEORY in the
  record yet states either side.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Scale chosen on the outcome.** The spatial band was fixed where
  spiral decoding is maximal; decoding accuracy is therefore an
  optimistic estimate, though the replication cohort used the same band.
- **Flat-map and filtering artefacts.** The null controls filtering; the
  flat map's distortion is argued against with a sulcal-depth test only.
- **Haemodynamic signal.** Spirals are in BOLD at 0.01–0.1 Hz; the paper
  cites, but does not show, that infra-slow fMRI reflects infra-slow LFP.
- **Flow is phase gradient.** "Activity flow" is the phase-vector field,
  not measured transfer of activity or information.
- **No perturbation.** Reversing spirals is done only in a 30 × 30
  lattice of phase oscillators.
- **Uncorrected contrast maps.** Task-contrast maps threshold P < 0.05
  "no adjustment is made for multiple comparisons" (Fig. 5 caption).
- **Manual steps.** Spiral boundaries are inspected by hand; network
  boundaries were annotated manually from a published figure.

## Open questions

- Do spirals of the same kind appear in electrophysiology at the scale of
  the whole cortex, and are they the same events?
- Does a discrete-state model of the same scans (for example, phase-locking
  states) lose its explanatory power once spiral positions and charges are
  regressed out, or the reverse?
- What mechanism makes cortical defects superdiffusive where fluid defects
  diffuse normally?

## Corrections

- none to a seeded skim (there was no seed)
- **Sign convention.** Results (p. 2) assign topological charge "+1 and
  –1" to clockwise and anticlockwise spirals respectively; Methods
  (spiral density map) assign −1 to clockwise and +1 to anticlockwise,
  matching positive vorticity for anticlockwise. The Methods convention
  is the one the maps use; nothing downstream depends on which.
