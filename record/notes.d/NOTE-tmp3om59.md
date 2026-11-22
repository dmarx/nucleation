---
status: Skimmed
paper: LIT-2266
title: 'Hancock and colleagues 2024, skimmed for what metastability is as a property of dynamics, how it differs from noise-driven switching among stable states, and how dwell times might tell them apart'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-094 from the authors' accepted
    manuscript in the University of Oxford's repository
    (ora.ox.ac.uk/objects/uuid:967c1662-3633-40ff-a524-dbd530e1078c/files/rjw827d81v,
    54 pp.), an institutional copy of the published review (Nature
    Reviews Neuroscience 26(2): 82–100), text extracted with pdftotext.
    Read: abstract, introduction, "What is metastability?", "The many
    routes to metastability and transient states", the dwell-time section,
    the concluding remarks, Box 2 and the opening of Box 3. Skipped: the
    history, the section on empirical signatures, the neurobiological
    drivers, the first two parts of the outlook, Box 1, the figures and
    the supplement. Quotations rechecked by script against the downloaded
    text. Read by the lead worker itself. No email address sent.
date: '2026-11-22'
summary: >-
  A review for neuroscientists. Metastability is a property of a
  dynamical system's landscape, not of data: regions that attract in some
  directions and repel in others (saddles, or the ghost of a fixed point
  after a bifurcation), so that trajectories dwell and escape "by design",
  without noise; multistability is switching among stable states driven
  by noise. Several routes lead to it, with symmetry breaking as the common
  enabler: a fixed point's ghost, cycles of saddles with delays or
  asymmetric stimuli, phase-lagged chimeras, chaotic itinerancy. Dwell
  times may tell the two apart: exponential for noise-driven multistability,
  gamma-like in metastable models. The reading is [THEORY-tmp31kx6](../theory.d/THEORY-tmp31kx6.md).
---
<!-- inactive-ok-file: THEORY-tmp31kx6 NOTE-tmpj6fck CLAIM-478 — Proposed or Skimmed; this reading's account, a reading set beside it, and a claim it bears on -->

# NOTE-tmp3om59: Hancock and colleagues 2024, skimmed for what metastability is as a property of dynamics, how it differs from noise-driven switching among stable states, and how dwell times might tell them apart

## Contribution

A definition of metastability against multistability, a catalogue of the
dynamical routes to it, and a proposed test. The reading is
[THEORY-tmp31kx6](../theory.d/THEORY-tmp31kx6.md).

## Key results

1. **Definition** (§ What is metastability?): a metastable system's
   "attractor landscape includes regions that attract in some directions
   but repel in others"; "while in multi-stable systems a trajectory can
   only escape from an attractor due to noise, trajectories in metastable
   systems transition between repelling and attracting regions ‘by
   design’". It "corresponds to a specific type of dynamic behaviour —
   that is, something certain systems do — and not to a single specific
   mechanism".
2. **Routes** (§ The many routes): "the identification of symmetry
   breaking as a key enabler of metastability"; the ghost of a fixed point
   after a saddle-node (Kelso's bimanual model), cycles of saddles from
   delays (Hansel; Kori and Kuramoto) or asymmetric stimuli (winnerless
   competition), phase-lagged chimeras in community-structured Kuramoto
   models, and chaotic itinerancy. Of the chimera model: "The existence of
   saddles in this specific generalisation of a Kuramoto model [...] has,
   to our knowledge, not been formally investigated."
3. **Not in the data** (Box 2): "metastability is a property of a
   dynamical system (that is, a mathematical or theoretical model aimed at
   capturing empirically observed phenomena), and not of data"; and
   switching with long dwells is "a necessary but not sufficient
   condition".
4. **A test** (§ Distribution of dwell times): with noise-driven
   multistability "the dwell time will (under standard assumptions on the
   noise distribution) display an exponential distribution"; metastable
   models give gamma-like distributions; a fit to the gamma distribution
   "could be a way to obtain an all-or-none test", if the rationale holds.
5. **Criticality is distinct** (Box 3; concluding remarks): metastability
   "should not be conflated" with complexity, criticality or
   multistability.

## Assumptions

Metastability defined within deterministic dynamical systems theory;
noise as the mechanism of multistable switching under standard
assumptions.

## Concepts

Metastability ("unstable attraction"); multistability; saddle; ghost or
memory of a fixed point; heteroclinic cycle (cycle of saddles); chaotic
itinerancy and Milnor attractors; signatures of metastability (variance of
the Kuramoto order parameter, among others); dwell-time distribution.

## Bearing on the record

- **[QUESTION-281](../questions.d/QUESTION-281.md)** (bears on). The review separates two of the question's
  transitions: escape across a barrier from a stable state by noise
  (multistability), and passage near saddles or a fixed point's ghost
  without noise (metastability), and proposes dwell-time statistics to
  tell them apart in data. A form that dwells near a saddle is
  transient by design; one held in a basin is stable until a fluctuation.
- **The other readings of this lead.** Caprioglio and Berthouze
  ([NOTE-tmp3gqv7](NOTE-tmp3gqv7.md)) and Augustsson and colleagues ([NOTE-tmp3oxzv](NOTE-tmp3oxzv.md)) report
  metastable chimeras in Kuramoto-type models, the class the review says
  has not been shown to contain saddles; Kaur and colleagues
  ([NOTE-tmpj6fck](NOTE-tmpj6fck.md)) find heavy-tailed, truncated power-law residences, which
  are neither the exponential nor the gamma of key result 4.
- **[CLAIM-478](../claims.d/CLAIM-478.md)** (note only). The slowing near a fixed point's ghost is
  slowing near a former bifurcation, the claim's second-half setting, but
  the review does not tie it to constraint.

## Limitations

- Skimmed; the section on empirical signatures, where most of the
  neuroscience lives, was not read.
- The dwell-time test is offered as promising, with computational support
  only, and the authors note a noise-driven model that gave a
  stretched-exponential distribution.
