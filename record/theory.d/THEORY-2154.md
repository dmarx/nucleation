---
number: 2154
status: Proposed
formerly:
- THEORY-tmpd7a4j
title: 'Transtrum and colleagues (2015) characterize a sloppy model by Fisher eigenvalues roughly evenly spaced in log over many decades with no boundary between stiff and sloppy combinations, and, since those eigenvalues change under reparametrization, locate the invariant content in a bounded model manifold whose geodesic widths fall exponentially, the hyperribbon, approximated by the square roots of the eigenvalues in dimensionless parameters, argued from interpolation for one independent variable, and read through parameter-space compression as why coarse-grained theories predict well'
promote_when: >-
  A check of the review's statements as quoted against the published
  Perspective (J. Chem. Phys. 143, 010901), since arXiv v1 was read; and an
  independent computation, by authors outside the Sethna group, on a model
  outside systems biology, finding Fisher eigenvalues in log parameters
  roughly evenly spaced in log with no gap, and geodesic widths
  approximated by their square roots. The readings of LIT-2977 and
  LIT-3009 confirm that the review restates its sources; they are the
  same group's work and do not meet this.
version: 1
tags:
- information-geometry
- model-comparison
- complex-systems
date: '2026-11-21'
source:
- LIT-2994
corroborates:
- CLAIM-825
- CLAIM-833
summary: >-
  Transtrum, Machta, Brown, Daniels, Myers and Sethna (2015), [LIT-2994](../literature.d/LIT-2994.md),
  read in [NOTE-2242](../notes.d/NOTE-2242.md). The programme's own statement of what sloppiness
  is: a spectrum as symptom, the hyperribbon as substance. It gives no
  quantitative criterion and draws no line from ill-conditioning or from
  singularity; its neural-network passage is about an autoencoder's code,
  not its weights.
---

# THEORY-2154: Transtrum and colleagues (2015) characterize a sloppy model by Fisher eigenvalues roughly evenly spaced in log over many decades with no boundary between stiff and sloppy combinations, and, since those eigenvalues change under reparametrization, locate the invariant content in a bounded model manifold whose geodesic widths fall exponentially, the hyperribbon, approximated by the square roots of the eigenvalues in dimensionless parameters, argued from interpolation for one independent variable, and read through parameter-space compression as why coarse-grained theories predict well

## Source

Transtrum, Machta, Brown, Daniels, Myers and Sethna, "Perspective:
Sloppiness and emergent theories in physics, biology, and beyond", J.
Chem. Phys. 143, 010901 (2015), [LIT-2994](../literature.d/LIT-2994.md), read from arXiv 1501.07668v1
in [NOTE-2242](../notes.d/NOTE-2242.md).

## What was actually shown

A review; what it reports, with its sources:

- **The symptom.** FIM eigenvalues "decay roughly log-linearly, with each
  parameter combination being less important than the previous by a fixed
  factor ... Consequently there is not a well-defined boundary between the
  stiff and sloppy combinations" (§I; Fig. 1, five spectra).
- **Why the symptom is not enough.** "the eigenvalues of the FIM are not
  sufficient to make this conclusion"; "the FIM can be transformed into any
  positive definite matrix by a simple linear transformation of
  parameters" (§III).
- **The substance.** Geodesic widths are "exponentially distributed", and
  "when we use dimensionless model parameters (e.g. log-parameters), the
  square roots of the FIM eigenvalues are a reliable approximation to the
  widths" (§III, citing [LIT-2977](../literature.d/LIT-2977.md) and [LIT-3009](../literature.d/LIT-3009.md)). "The exponential
  distribution of manifold widths has been described as a hyperribbon".
- **Why.** Interpolation, "for the case of a single independent variable".
- **Emergence.** The hopping model's manifold "contracts onto a
  hyper-ribbon" as time proceeds; the Ising model develops stiff
  directions "along precisely those parameter combinations deemed
  'relevant' under the renormalization group" (§V, restating [LIT-1299](../literature.d/LIT-1299.md)).
- **Reduction.** MBAM reduces EGFR from 48 parameters to 12 (§IV).

## What this does not say

- **A criterion.** No threshold in decades, no spacing test, no count.
- **A line from ill-conditioning.** "extremely ill-conditioned" is said of
  the FIM of a sloppy model; what more sloppiness is, beyond shape, is the
  move to the widths.
- **Anything about singular models,** rank loss or learning coefficients;
  the FIM is called "positive semi-definite" and no more.
- **That the stiff directions are always the RG-relevant ones in
  general.** "precisely those" is said of one Ising computation; the
  caution against equating the two in the record is A19 §5's.
- **That neural networks are sloppy in their weights.** The autoencoder's
  "parameters" are its code, and the evidence is unpublished.
