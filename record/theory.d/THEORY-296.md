---
number: 296
status: Active
formerly:
- THEORY-tmpztbz7
title: 'In a preregistered multimodal test with clearly seen images, category-selective posterior cortex showed no sustained content-specific synchronization with early visual cortex, which iEEG sampled with 12 electrodes: the preregistered phase coupling was brief, low-frequency and mostly stimulus-evoked, and exploratory amplitude coupling, gamma included, was also brief'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active under ADR-065 and ADR-047's routing, at
    the status review's ruling (the owner delegated these rulings). The old
    title read: "In a preregistered multimodal test with clearly seen
    images, category-selective posterior cortex showed no sustained
    content-specific synchronization with early visual cortex: the coupling
    was brief, low-frequency and mostly stimulus-evoked". Its last clause
    held for the preregistered phase coupling only; the exploratory
    amplitude coupling, with the evoked response removed, was mainly gamma
    and also brief, so the clause is restated (ADR-047 kind 3, this note
    only). The authors' own hedge, sparse V1/V2 sampling, is now in the
    title. The narrowed title reports what one preregistered study, read in
    full in NOTE-812, measured, and nothing in the record contradicts it.
    The old promote_when read: "A recording with dense sampling of V1/V2 and
    of category-selective cortex in the same subjects (the iEEG here had 12
    V1/V2 electrodes), during clearly seen images held for over a second,
    that tests content-specific phase or amplitude coupling in the gamma
    band over the whole stimulus with the evoked response removed. It is
    supported if such coupling is again brief or absent at a sensitivity
    that detects it elsewhere, and refuted if it is sustained for the
    duration of the image. Results from other metrics or bands, or from
    coupling with prefrontal cortex, cannot settle it." Its demand for a
    denser recording is an independent test of the same null, and moves to
    QUESTION-350.
tags:
- consciousness
- neuroscience
date: '2026-10-14'
source:
- LIT-973
summary: >-
  Cogitate Consortium, Ferrante et al. (2025), [LIT-973](../literature.d/LIT-973.md), read in
  [NOTE-812](../notes.d/NOTE-812.md). IIT's proponents predicted sustained gamma-band
  synchronization between category-selective cortex and V1/V2 throughout
  a conscious percept. iEEG and MEG phase consistency found only early,
  brief, 2–25 Hz coupling, mostly evoked, with Bayesian support for the
  null; exploratory amplitude coupling was also brief. V1/V2 was sparsely
  sampled in iEEG. It tests IIT's proposed implementation, not
  integrated information.
---
<!-- inactive-ok-file: THEORY-098 — Proposed; the sensory-recurrence account this bears on -->

# THEORY-296: In a preregistered multimodal test with clearly seen images, category-selective posterior cortex showed no sustained content-specific synchronization with early visual cortex, which iEEG sampled with 12 electrodes: the preregistered phase coupling was brief, low-frequency and mostly stimulus-evoked, and exploratory amplitude coupling, gamma included, was also brief

## Source

Cogitate Consortium, Ferrante, Gorska-Klimowska, Henin et al. (2025),
*Nature* 642:133–142, [LIT-973](../literature.d/LIT-973.md), read in [NOTE-812](../notes.d/NOTE-812.md): "Interareal
connectivity", Discussion, Methods ("Functional connectivity analysis"),
Extended Data Figs. 5–7.

## What was actually shown

**The prediction.** Preregistered with IIT's proponents: "sustained
gamma-band connectivity within the posterior cortex, that is, between
high-level and low-level sensory areas (V1/V2), throughout any conscious
visual experience". IIT "would be challenged in the absence of sustained
content-specific synchronization between face–object selective areas and
V1/V2". It was a critical prediction.

**The test.** Pairwise phase consistency between face- or
object-selective sites and V1/V2, on 1.0-s and 1.5-s task-irrelevant
trials. In iEEG it was computed electrode to electrode within patients,
and in MEG with GED-filtered fusiform sources.

**The result.**
- iEEG: content-selective synchrony with V1/V2 was "early and brief (for
  example, less than 0.75 s), and restricted to low frequencies
  (2–25 Hz)", and "mostly explained by the stimulus-evoked response". It
  disappeared when the evoked response was removed. Bayes factors favoured
  the null (BF01 = 1.15–4.9).
- MEG: the same pattern, with gamma-band BF01 > 3.
- Exploratory DFC (amplitude co-modulation, evoked response removed):
  object-selective coupling with V1/V2 that included gamma but "was
  brief". Face-selective coupling was "scarce" (BF01 = 1.3).
- fMRI gPPI: FFA coupled face-selectively with V1/V2, a result of the
  kind both theories allow, with no time course.

**Beside it.** The same study found sustained category information and
duration-tracking activity in posterior cortex ([THEORY-102](THEORY-102.md)'s pattern). So
content was held over time while content-specific coupling to early
visual cortex was not. The consortium calls the coupling result "the most
direct challenge" to IIT, being "incompatible with IIT's claim that the
state of the neural network, including its activity and connectivity,
specifies the degree and content of consciousness".

What could have come out otherwise: gamma phase consistency could have
stayed above its across-category baseline for the whole image, as
predicted.

## What this does not say

- **It does not test integrated information.** Nothing computed Φ. The
  prediction belongs to IIT's proposed implementation in posterior cortex,
  which the authors say a theory may revise while keeping its core.
- **It does not exclude sustained coupling under denser sampling.** Only
  12 iEEG electrodes were in V1/V2, against 472 in prefrontal cortex. The
  authors grant the null "could stem from methodological limitations (for
  example, limited iEEG sampling of V1/V2 areas)".
- **It does not say posterior cortex does not sustain content.** It did,
  for category and object identity. The finding is about coupling between
  areas, not about content within one.
- **It does not favour the workspace by default.** The preregistered PPC
  found no content-selective coupling with prefrontal cortex either.
  Exploratory DFC found brief prefrontal gamma coupling, and that is not
  the preregistered test.
- **It is about clearly seen, unchanging images** over at most 1.5 s.

## Connections

- **[THEORY-098](THEORY-098.md)** puts the basis of perceptual consciousness in recurrent
  activity in sensory cortex. This result does not refute it, since
  recurrence need not show as sustained gamma phase-locking with V1/V2.
  But it removes one measurable form that sustained posterior recurrence
  was predicted to take.
- **[THEORY-102](THEORY-102.md)** and [THEORY-245](THEORY-245.md) hold what the same paradigm showed
  about content: sustained posterior category coding, and prefrontal
  content at onset only and without identity or orientation. Read
  together, sustained content in posterior cortex came without sustained
  content-specific coupling to early visual cortex.
- **[QUESTION-048](../questions.d/QUESTION-048.md).** As a theory test, it shows how a design aimed at a
  theory reaches only its implementation. That is the paper's own point,
  and it is why no `answers:` is declared.
