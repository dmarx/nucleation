---
status: Read
paper: LIT-tmp5mwek
title: 'Martinez-Garcia et al. — Integrating theory and experiments for dryland vegetation patterns'
version: 1
history:
- version: 1
  date: '2026-11-14'
  note: >-
    Read in full on 2026-11-14 by a delegated reader from
    https://arxiv.org/pdf/2101.07049v4 (24 pp., the authors' preprint for
    Chaos, Solitons & Fractals, dated 19 Oct 2022); text extracted with
    pdftotext. Read: the abstract, §§1–6, the captions of Figs. 1–6, and
    Tables 1–2. Not read: the figure images, and the reference list beyond
    refs. [16], [21], [28], [41], [43], [58], [91], [110] and [111]. Page
    numbers are the preprint's. Every quotation below was string-matched
    against the text by the filer.
date: '2026-11-14'
summary: >-
  A review sorting dryland vegetation models by the net plant interaction
  they assume as a function of distance, from scale-dependent feedback
  (SDF) to purely competitive feedback (PCF). Both give the same pattern
  sequence; SDF models collapse abruptly with hysteresis, PCF models
  smoothly. It proposes a transplant experiment to read the sign of the
  net interaction, and notes that kernels are seldom fitted to measured
  roots or crowns. No new model or data; its numbers rerun published
  models.
---

# NOTE-tmpbqaec: Martinez-Garcia et al. — Integrating theory and experiments for dryland vegetation patterns

## Contribution

The review separates two questions that the pattern literature had run
together: which mechanism makes the pattern, and which transition the
system will undergo. Two families of models answer the first question the
same way and the second differently. The authors organize reaction–diffusion
models (Klausmeier, Rietkerk) and kernel models (Lefever–Lejeune, nonlocal
coupling, PCF) on one axis, and give a field design that could tell the
mechanisms apart.

## Key insight

Long-range inhibition is enough for a periodic pattern. Short-range
facilitation is not needed for it, but it changes how the vegetation is
lost: with facilitation the loss is abrupt and hysteretic, without it the
loss is smooth. So a spotted landscape says the system is dry, not how it
will fail.

## Assumptions

- **Aggregated patterns only**: patches of many individuals, so that
  continuous fields apply. Segregated patterns, with one plant per patch,
  are set aside (p. 5).
- **One net interaction as a function of distance** summarizes all the
  feedbacks.
- **Homogeneous soil and rainfall** in the base models.
- **One plant type**, set against water or bare soil. No model with two
  competing plant types is treated.
- **A stationary pattern** for the field test (p. 13).

## Key results

- **Same patterns, different collapses** (abstract): "although these
  alternative hypotheses lead to visually indistinguishable patterns, they
  predict contrasting desertification dynamics".
- **A continuum of models** (§2, p. 3): the two categories are "the
  extremes of a continuum of models characterized by the ratio between
  the intensity of short-range positive and negative interactions".
- **Parsimony** (§2, p. 5): "PCF is the most parsimonious feedback type
  that generates vegetation patterns."
- **How competition alone aggregates plants** (§3.3, p. 10): "competition
  is more intense in the regions between patches than inside each patch,
  which stabilizes an aggregated pattern". The Fig. 4 caption: patchy
  distributions "in which the distance between patches is between one and
  two times the range of the nonlocal interactions are stable".
- **What facilitation does** (§3.3, p. 9): "short-range positive feedbacks
  might be secondary actors that sharpen the boundaries of clusters rather
  than being key for the instabilities".
- **SDF collapse** (§4, p. 11): in the Rietkerk model the threshold "is
  located at R ≈ 0.55 mm day−1", and recovery needs more rain, which
  closes a hysteresis loop. Termites break it in two: "termite-induced
  heterogeneity breaks the large hysteresis loop of the original model
  into two smaller ones". Multistable models give patterns that "only
  contain partial information about the ecosystem state since they will
  be very strongly determined by the system history".
- **PCF collapse** (§4, p. 11): such transitions "do not show bistability
  and do not feature hysteresis loops". Whether this comes from "the
  absence of a positive feedback or the lack of diffusion" is left open.
- **What is unmeasured** (§3.2.2, p. 9; §5, p. 13; §6, p. 15): kernel
  scales "are rarely parameterized using field measurements of root extent
  and crown size"; "To our knowledge, the net-interaction approach is
  conspicuous by being absent"; and "kernel-based models still do not
  incorporate realistic functional forms for the kernels".
- **The test** (Table 2, p. 14): transplants under canopy, in bare soil and
  behind root barriers. A neutral or negative effect under canopy, with a
  strongly negative one in bare soil, reads as PCF. A positive effect under
  canopy, with a negative one in bare soil, reads as SDF.

## Concepts

- **SDF / PCF**: scale-dependent feedback (net interaction positive near a
  plant, negative farther off) against purely competitive feedback
  (negative at every distance, weakening with it).
- **Net interaction**: a focal plant's effect on a neighbour's fitness, as
  a function of distance.
- **Exclusion region**: the zone between patches where competition from
  more than one patch overlaps.
- **Observational, net-interaction and selective-mechanistic** approaches
  to identifying a mechanism.

## Connections

The review places Klausmeier's and Rietkerk's reaction–diffusion models
under Turing's activator–inhibitor principle ([THEORY-543](../theory.d/THEORY-543.md)). In the PCF
models the instability comes from the kernel, not from diffusion. It cites
the early-warning literature ([LIT-1956](../literature.d/LIT-1956.md), its ref. [16]). It is Sun et al.'s
(2026, dmarx/nucleation#494) ref. 34, cited there for the claim that "the
spatial extent of negative feedback generated by plant resource
exploitation governs both patch size and the wavelength of regular
patterns".

## Bearing on the record

- **Sun et al. (2026)**, filed in dmarx/nucleation#494; named here by
  citation, since its codes are not yet on the default branch.
  - Their ref.-34 citation is half supported. Spacing is set by the
    competition range, for PCF (the Fig. 4 caption). Patch size is not
    stated in this review.
  - Their kernels combine competition with a weak facilitation, which
    puts their model near the competitive end of this continuum. That
    their facilitation asymmetry "is not essential" is not the same as a
    test with facilitation removed, so calling their mechanism a
    scale-dependent feedback is unsupported until that test is run.
  - Their unmeasured radii (r− = 20 and 3) are the unmeasured kernel
    scales this review names.
  - By this review's argument, regressing patch geometry on traits cannot
    identify the mechanism.
  - The review does not treat bistability between two plant types, so it
    neither supports nor undercuts their bistable interval.
- **[THEORY-543](../theory.d/THEORY-543.md)** (Turing's diffusion-driven instability). The review
  holds a pattern-forming instability that needs no diffusion: nonlocal
  competition alone. Dated note filed.
- **[QUESTION-281](../questions.d/QUESTION-281.md).** The review shows, for one family of systems, that the
  mechanism which makes a form (the instability) does not fix how the form
  is lost (abruptly, in two steps or smoothly). That bears on the
  question's separation of creation from stabilization and loss. It is
  written as `bears_on` on the THEORY, with no dated note, since it is
  model-only and secondary.

## Limitations

- A review. Its PCF spacing claim rests on the authors' earlier refs.
  [21, 28], which were not read.
- The field protocol has not been run. The authors concede infiltration
  "might be very hard to measure" (p. 14).
- One plant type only.
- The authors wrote the PCF models. They flag their own no-bistability
  result as possibly an artefact of the lack of diffusion.

## Open questions

- Does a PCF kernel model with two plant types that differ in range and
  strength, Sun et al.'s set-up with facilitation removed, keep a
  bistable interval?
