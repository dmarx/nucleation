---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp1swq3](../notes.d/NOTE-tmp1swq3.md)); worth reading as, on its own account, the first evidence that neural responses, not stimuli, carry a hyperbolic geometry. Pairwise spike-train correlations of a few dozen active dorsal CA1 cells per session (34 to 56 in the sessions shown), in rats on a novel 48-m track, a 2.5-m track and a 1.8-m box, give Betti curves (clique topology, invariant to any monotone transform of the correlations) that match points sampled uniformly from a 3D hyperbolic ball and fail to match uniform samples from Euclidean cubes of low dimension or shuffled spikes. The fitted radius (10.5–15.5 in units of inverse curvature) grows with the logarithm of exploration time, on scales from seconds to days, as the maximal information acquirable does. Place-field sizes are close to exponential, as the model requires, and in simulation exponentially distributed field sizes give more Fisher information than uniform or log-normal ones, with an optimal radius growing as log N that extrapolates to the radius measured. The "hierarchy" is one of nested place-field sizes; no tree is recovered from the data, and the only null geometry tested is Euclidean with uniform sampling.'
title: 'Hippocampal spatial representations exhibit a hyperbolic geometry that expands with experience'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 from the description
    "Zhang et al. (2023) — biological evidence for hyperbolically
    organized neural representations". Identification: Crossref, Europe
    PMC and the Salk lab's publication list give one match, Zhang, Rich,
    Lee & Sharpee, Nature Neuroscience 26(1):131–139, DOI
    10.1038/s41593-022-01212-4 (PMID 36581729, PMC9829541). A Europe PMC
    search for hyperbolic-geometry papers with an author Zhang in
    2022–2024 found no other neural candidate (the rest are a speech-BCI
    decoder, a path-planning optimiser and a cheminformatics model), and
    the lab's other first-author Zhang item (2025, auditory coding) does
    not concern hyperbolic geometry. No preprint was found: none on
    bioRxiv by Crossref posted-content search on the authors and title,
    none on arXiv, none listed by the lab, and the article itself names
    none. `published:` is 29 December 2022, the online date that
    Crossref (published-online, issued) and PMC (epub) agree on; the
    print issue is January 2023, hence "2023" in citations; ADR-002 takes
    the earlier. Received 21 April 2021, accepted 24 October 2022. Read in
    full from the PMC open-access copy (CC BY 4.0). Not held in the
    Anthology of the SOTA: a grep of its record/ (clone at commit d8b5ba5,
    which may be stale) for the authors, DOI, PMC id and title found
    nothing.
tags:
- neuroscience
- mathematics
- information-theory
date: '2026-10-09'
published: '2022-12-29'
doi: '10.1038/s41593-022-01212-4'
first_author: 'Zhang'
keywords:
- 'hippocampus'
- 'CA1'
- 'place cells'
- 'hyperbolic geometry'
- 'clique topology'
- 'Betti curves'
- 'neural encoding'
- 'learning and memory'
implementations:
- 'https://github.com/HuanqiuZhang/Fisher_info_codes'
summary: >-
  Zhang, Rich, Lee & Sharpee (2022 online, Nat. Neurosci. 26, 2023).
  The pairwise correlations of rat dorsal CA1 place cells have the
  topological signature of points sampled uniformly from a
  three-dimensional hyperbolic ball, not of a low-dimensional Euclidean
  cube, and the ball's radius grows with the logarithm of exploration
  time. Place-field sizes are near exponential, and in a Poisson model
  exponential sizes carry more positional Fisher information than uniform
  or log-normal ones, with an optimal radius that matches the measured
  one for the number of CA1 neurons.
---

<!-- inactive-ok-file: THEORY-tmpae88o — Proposed; cited as the THEORY this reading sources -->

# LIT-tmpvydv3: Hippocampal spatial representations exhibit a hyperbolic geometry that expands with experience

Huanqiu Zhang, P. Dylan Rich, Albert K. Lee and Tatyana O. Sharpee (2022
online; 2023 issue), *Nature Neuroscience* 26(1):131–139 —
DOI-10.1038/s41593-022-01212-4, open access at PubMed Central (PMC9829541)

## Key takeaways

- **The geometry test.** Distances between neurons are their negated
  pairwise spike correlations. Clique topology (Giusti et al. 2015)
  thresholds the matrix at every edge density and counts 1-, 2- and 3-cycles,
  so the Betti curves depend only on the rank order of the correlations.
  The experimental curves match uniform samples (300 per model) from a 3D
  hyperbolic ball, are rejected for uniform samples from Euclidean cubes of
  low dimension (up to 10 in the robustness check), and are rejected for
  the same cells after time-shifting each spike train. 3D fits better than other
  hyperbolic dimensions in the six sessions compared (two-way ANOVA).
- **The hierarchy is one of scale.** The paper's tree is built by
  putting neurons with larger place fields higher and linking a field to
  the larger fields that contain it. With one field per neuron, field sizes
  in a hyperbolic representation are near exponential,
  p(s) ≈ ζ e^(−ζs), and the measured sizes on the 48-m track fit an
  exponential (χ² P = 0.85). The tree is an illustration; no tree is
  inferred from the data.
- **The radius grows with experience.** Across days in a 1.8-m box the
  radius rises with log exploration time (r = 0.85), and the paper fits
  the formula for the maximal information acquirable in time T. On the
  48-m track, within seconds, radius estimated from field sizes rises with
  time spent per metre. Running speed, area covered and time away from the
  environment do not account for it. A mechanistic reading: if a small
  field forms after a fixed dwell t₀ and small fields lie at the edge,
  whose count grows as e^R, then R ≈ log(T/t₀).
- **Why it would be efficient.** In a model of independent Poisson
  neurons with 2D Gaussian fields, exponentially distributed field widths
  give more positional Fisher information than uniform or log-normal ones
  of the same mean, and for N neurons there is an optimal radius growing as
  log N. Extrapolated to 30–40% of the 320,000–490,000 CA1 pyramidal cells,
  it lands on the radius measured in the most familiar box sessions. A
  gamma-Poisson model of multiple fields per cell gives the same.
- **Log-normal field sizes are not counter-evidence**, the paper argues:
  discarding small fields, and pooling exponentials of different rates,
  turns exponential samples into near log-normal histograms (simulation).

## Standing in the record

Filed at the owner's request on 2026-10-09, in a batch of six works on
hierarchy and hyperbolic geometry asked for after the record opened
[QUESTION-025](../questions.d/QUESTION-025.md): Cagnetta et al.'s random hierarchy model, Krioukov et al.
(2010), Sala et al. (2018), Lin et al. (2023), this paper, and Yang et al.
(2023). The owner named it as "biological evidence for hyperbolically
organized neural representations".

Read on 2026-10-09 ([NOTE-tmp1swq3](../notes.d/NOTE-tmp1swq3.md)). The reading is the source of
[THEORY-tmpae88o](../theory.d/THEORY-tmpae88o.md), the record's statement of the finding and its limits.
It cites Krioukov et al. (2010), filed in the same batch, for the claim
that a tree-like network is a mesh over a hidden hyperbolic geometry.

It is not a reading for the anthology: no machine-learning practice is
involved, and its subject is a biological measurement.
