---
status: Read
paper: 'LIT-tmpzhtw7'
title: 'Di Volo and Férézou — Nonlinear collision between propagating waves in mouse S1'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from the Europe PMC full-text XML of the published
    article (PMC8490437,
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8490437/fullTextXML).
    Read in full: abstract, Introduction, all Results, Discussion and the
    experimental Methods. Skipped: the computational Methods (network model,
    2-D mean field, spatial coupling, inversion), the equations and the
    references. A side reading, so kept compact. The filer rechecked every
    quote below against that copy.
date: '2026-11-15'
summary: >-
  The main result: in anaesthetised mouse barrel cortex, two whisker-evoked
  waves launched 10 ms apart sum sub-linearly, about 30% below the linear
  sum at peak, as a heterogeneous E/I mean-field model predicted from the
  lower gain of already-active populations. The waves are excitable fronts
  at about 0.1 mm/ms, anisotropic in intensity, not speed.
---
<!-- inactive-ok-file: THEORY-088 CLAIM-606 — Proposed; cited from a side reading as contrast and as the claim it is set against -->

# NOTE-tmpm4s2r: Di Volo and Férézou — Nonlinear collision between propagating waves in mouse S1

## Contribution

An inversion from mesoscale imaging to a map of excitatory coupling. With
it, anisotropic propagation is explained by heterogeneous coupling, and a
sub-linear wave collision is predicted by the model and then measured.

## Key insight

A cortical wave here is a chain of jumps in a bistable excitable medium,
not a linear oscillation. Where two fronts meet, populations already
active respond less, so the waves do not superpose.

## Assumptions

Isoflurane anaesthesia; six mice. Only excitatory coupling is inferred,
with inhibition uniform. Exponential decay of coupling with distance. A
late input from S2 (about 26 ms) is excluded.

## Key results

- **Sub-linear collision, the main result** ("Suppressive interaction"):
  "the activity evoked by the two stimuli presented sequentially is lower
  than the linear summation of the responses to the two stimuli presented
  separately", with "a mean peak at around -30%" across all six mice,
  strongest near C2. The deficit travels as a "suppressive wave".
- **Its cause in the model**: a sub-linear population gain, which needs
  conductance-based synapses and a higher inhibitory gain (Discussion).
- **Mechanism of spread** ("A computational model"): a local input "can
  potentially trigger a chain of jumps to high activity states that
  spreads in space"; with uniform coupling it "spreads uniformly in space
  with a speed equal to the axon conduction velocity".
- **Anisotropy** ("Anisotropic structure"): speed "is approximately the
  same in all directions", while the linescans are "not symmetric with
  respect to the initial activation site".
- **Inversion**: on synthetic data it "converges to a K(x,y) very similar to
  the real one"; on real data it gives "a heterogeneous and non-symmetric
  distribution of couplings".

## Concepts

Propagating wave; bistable excitable medium; adaptation; mean-field E/I
model; model inversion; sub-linear summation; suppressive wave.

## Bearing on the record

- **Linear-interference readings**: qualifies them. Two colliding cortical
  waves sum to about 30% less than their sum. The linear interference of
  Gepshtein et al. ([LIT-tmphayso](../literature.d/LIT-tmphayso.md)) holds for that model's stationary,
  low-contrast regime, not for cortical wave interaction in general.
- **[THEORY-088](../theory.d/THEORY-088.md)**: no bearing. Fronts meet and sum sub-linearly, with no
  defects, phase singularities or annihilation.
- **[CLAIM-606](../claims.d/CLAIM-606.md)**: an excitable, adaptation-terminated front sits at most on
  the supplied route. The paper does not withdraw supply, which is the
  test the claim asks for.

## Limitations

Computational Methods unread, so identifiability of the inversion beyond
the synthetic test rests on the authors' word. One delay and one whisker
pair for the collision.
