---
status: Read
paper: LIT-tmpijst5
title: 'Zelnik, Meron & Bel — Gradual regime shifts in fairy circles'
version: 1
history:
- version: 1
  date: '2026-11-14'
  note: >-
    Read in full on 2026-11-14 by a delegated reader from
    https://arxiv.org/pdf/1703.00732 (v1, 2017-03-02, 23 pp., the authors'
    manuscript; its abstract page gives the PNAS DOI). Read: the abstract,
    introduction, §§I–VI and Appendices A–C; the references as a list. Not
    read: the figure panels themselves, so the width of the hybrid range
    in rainfall is not quoted. Table I did not extract cleanly. Whether
    Appendices A–C match the PNAS SI is unchecked, and the arXiv wording,
    posted after publication, may differ from the version of record. Page
    numbers are the arXiv PDF's. Every quotation below was string-matched
    against the text by the filer.
date: '2026-11-14'
summary: >-
  A two-field model (biomass and soil water) fitted to the Namibian
  fairy-circle grassland has, inside its uniform/gap-pattern bistable
  range, many stable hybrid states. Brief droughts or wet spells move it
  between them, which the authors match to a fairy-circle birth and death
  seen in 2004–2013 images; periodic pulses give a gradual shift that the
  same pulses do not produce from a uniform or periodic start. The gradual
  cascade is a simulation result; the field evidence is correlations over
  eight images.
---

<!-- inactive-ok-file: LIT-720 LIT-1642 — Unavailable or Unfetched; named as the paper's foil and as the theory it cites -->

# NOTE-tmppk4i4: Zelnik, Meron & Bel — Gradual regime shifts in fairy circles

## Contribution

The paper is the first test, in a model fitted to a particular ecosystem,
of the pattern-formation prediction that hybrid states make regime shifts
gradual. That prediction "has never been tested either in a real ecosystem
or in a model describing the dynamics of a specific ecosystem" (p. 2). It
also adds evidence from dynamics, alongside earlier static statistics,
that fairy circles are a self-organized water–vegetation pattern.

## Key insight

Bistability does not imply a jump. Where the fronts between two states
are pinned, a whole family of mosaics is stable, and forcing that leaves
the pinning range only briefly moves the system one domain at a time. The
shift is then gradual in the aggregate, though every local step is
discontinuous.

## Assumptions

- Smooth rainfall and uniform terrain. The authors say this inflates the
  simulated correlations (p. 6).
- Sandy soil, so infiltration is the same on bare and vegetated ground
  (f = 1). The surface-water feedback therefore drops out.
- The root kernel is treated as a point, since roots of about 0.5 m are
  small against a pattern scale of about 10 m (pp. 14–15).
- Parameters come from the literature. The authors give no source for E
  in grasses. Soil-water diffusion is set to 150 m²/yr, above their own
  estimated range, "to account for" termite channels (p. 12).
- Gradual shifts need repeated brief excursions outside the hybrid range.
  A slow ramp in rainfall is not studied. Real rainfall variability would
  push the simplified model "towards one of the uniform states" (p. 9).

## Key results

- **Foil** (p. 1): catastrophic shifts are "abrupt transitions between two
  alternative stable states that occur uniformly across the ecosystem".
- **Hybrid states** (p. 4, Fig. 1): "a subrange with many stable hybrid
  states", with gaps added "as the branch snakes down".
- **Birth and death** (p. 5, Fig. 2): these "correspond to transitions
  between hybrid states". They are reproduced from the 2004 images by one
  year at 84 mm/yr (drought) or 143 mm/yr (wet spell), then 102 mm/yr.
- **Time scales** (pp. 6, 9): "the timescale for changes in the fairy
  circle size is much shorter than the time scale for changes in the fairy
  circle number". Size is "convergence to a steady state"; number follows
  "the dynamics of fronts that separate domains". In the images, size
  correlates with rainfall accumulated over a short time and number with
  rainfall over a long time (Fig. 3).
- **The cascade** (p. 6, Fig. 4): periodic droughts (one year at 81 mm/yr,
  then 15 years at 102) drive the system "by successive shifts to hybrid
  states of larger gap numbers". Wet spells at 138 mm/yr drive it back.
- **Dependence on the start** (p. 7; Fig. 10): uniform or periodic starts
  "remain practically unchanged"; "No regime shift takes place even though
  the system is subjected to the same rainfall regime".
- **Mechanism** (p. 10): "a finite wavenumber (Turing) instability",
  needing strong water uptake and soil-water diffusion faster than biomass
  spread.
- **Robustness** (p. 18): with each dimensionless parameter moved by ±10%,
  "in all cases, the hybrid states exist".
- **The authors' weighing**: the evidence is "compelling evidence" (p. 8)
  but "does not rule out alternative hypotheses" (p. 9), and the "exact
  biological origin of hybrid states" is unclear.

## Concepts

- **Hybrid (localized) state**: a stable mosaic of uniform vegetation and
  periodic gap pattern, on a snaking solution branch (homoclinic snaking;
  Knobloch, LIT-1642).
- **Front pinning**: the front between the two states stays put over a
  range of the control parameter. Outside that range it moves.
- **Gradual vs abrupt regime shift**: in the aggregate, a cascade of
  spatially confined transitions against one uniform jump.

## Connections

The foil is Scheffer et al. 2001 (LIT-720). The pattern mechanism is
Turing's (THEORY-543). The hybrid states are the localized structures of
Knobloch's theory (LIT-1642), which this paper cites as its ref. [7]. The
excursions driven by fluctuations are close to the noise-induced routes of
Ashwin et al. (LIT-1654).

## Bearing on the record

- **QUESTION-281.** A worked case of the localized-structures route.
  - A form (a gap) comes into being and passes away by a spatially
    confined transition between coexisting stable states.
  - Pinning on the snaking branch stabilizes it.
  - Brief excursions outside the pinning range make and unmake it.
  - The instability supplies the pattern and the pinning holds a given
    mosaic: creation and stabilization are different mechanisms, shown by
    continuation in a model.

  Dated note filed.
- **THEORY-136** (abrupt change is not evidence of alternative stable
  states). The field evidence here, correlations over eight images, falls
  short of that entry's bar. The model meets it: dependence on the initial
  state (Fig. 10) and a lasting shift after brief forcing (Fig. 4). The
  paper adds that the converse also holds: alternative stable states do
  not imply an abrupt change. Dated note filed.
- **Sun et al. (2026)**, filed in dmarx/nucleation#494 and named by
  citation, since its codes are not on the default branch.
  - Different objects share one name. Here fairy circles are bare gaps in
    single-species grass; in Sun et al. they are hollow shrub rings in
    grass.
  - The two agree that fairy circles are self-organized, and that they sit
    in a range of rainfall where two states are both stable.
  - They differ on stability: stable hybrid states here, metastable rings
    there.
  - This paper qualifies Sun et al.'s "abrupt". Plots in different states
    at the same rainfall are a mosaic, and with fronts pinned the regional
    shift would be gradual even though each plot jumps. Sun et al.'s
    single survey cannot tell the two apart.
  - Both can be right at their own scales.
- **LIT-1642** (Knobloch). This paper is an applied instance of that
  theory and stands in for it only as far as hybrid states and snaking
  go.

## Limitations

- The gradual cascade is shown only in simulation, under an idealized
  periodic schedule of pulses.
- The field data are eight images of four 180 × 180 m regions. No
  significance test is reported, the lag was chosen for the strongest
  correlation, and one birth and one death are illustrated without a
  count.
- E and D_W are unmeasured, and D_W is set above the authors' own
  estimated range.
- Termite hypotheses are not excluded.

## Open questions

- Are the shared fronts between Sun et al.'s two patterned phases pinned
  in their lattice model? If not, the model predicts a front moving toward
  the more stable phase, and so an abrupt regional shift, except near one
  coexistence point.
