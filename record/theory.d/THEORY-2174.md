---
number: 2174
status: Proposed
formerly:
- THEORY-tmpwtoad
title: 'V1 eigenspectrum follows a 1/n power law'
statement: >-
  Stringer, Pachitariu, Steinmetz, Carandini and Harris find that the
  stimulus-related responses of about 10,000 mouse V1 neurons to natural
  images have a cross-validated eigenspectrum close to a power law with
  exponent 1.04, fitted over ranks 11 to 500, and prove that in the
  many-neuron limit a code with finite expected derivative on a
  d-dimensional stimulus manifold has eigenvalues o(n^(−1−2/d)), a bound on
  the tail that lower-dimensional stimulus ensembles approach from above
promote_when: >-
  An independent recording, or a reanalysis of the released data with
  cross-validated PCA, finds an exponent near 1 for natural images in V1
  and exponents above 1 + 2/d for stimulus ensembles of lower dimension d;
  and a second reading checks Theorems 3 to 5 of the Supplementary
  Discussion as stated.
version: 1
tags:
- neuroscience
- representation-learning
- mathematics
date: '2026-11-22'
source:
- LIT-2972
summary: >-
  Stringer and colleagues, [LIT-2972](../literature.d/LIT-2972.md), read in [NOTE-2257](../notes.d/NOTE-2257.md). V1's code of
  natural images sits just on the smooth side of the critical exponent
  1 + 2/d: a spectrum decaying more slowly would put so much variance in
  fine directions that the code would stop being differentiable. The
  bound is strict and asymptotic in rank. It grounds [CLAIM-848](../claims.d/CLAIM-848.md)'s premise
  in that corrected form ([ARG-169](../arguments.d/ARG-169.md)).
---
<!-- inactive-ok-file: CLAIM-848 ARG-169 — Proposed or new; the claims this reading bears on and the argument for its support -->

# THEORY-2174: V1 eigenspectrum follows a 1/n power law

## Source

Stringer, Pachitariu, Steinmetz, Carandini and Harris, "High-dimensional
geometry of population responses in visual cortex", Nature 571 (2019),
[LIT-2972](../literature.d/LIT-2972.md), read from the PMC author manuscript and Nature's Supplementary
Information in [NOTE-2257](../notes.d/NOTE-2257.md).

## What was actually shown

- "The scaling exponent of the power law had a peak just above 1
  (1.04±0.02 SE, n = 7 recordings, Fig. 2e)", fitted "over the range
  11-500 dimensions". It survives whitening the images: "the power law in
  the neural responses remained".
- Supplementary Theorem 5: "If the expected derivative magnitude of φ is
  finite ... then λn = o(n−1−2/d)". Theorem 4 gives the weaker fractal
  bound O(n^(−1−2/d′)) for every d′ > d; Corollary 3.1 gives o(n^(−1)) for
  any code with finite variance and a continuous kernel.
- Stimulus ensembles of dimension 8, 4 and 1 gave exponents "1.49, 1.65,
  and 3.43, near but above the lower bounds of 1.25, 1.50, and 3.00".

What could have failed: the exponent could have tracked the images'
spectrum, fallen below 1 + 2/d for a low-dimensional ensemble, or not
risen as d fell. None did.

## What this does not say

- Not that a spectrum exactly at α = 1 + 2/d is smooth: it is the limit of
  smooth codes. In the circle example, at α = 3 "the dimension is still 1,
  even though" the code is not differentiable.
- Nothing about the head of the spectrum or any finite range of ranks: the
  theorems are about the tail as n → ∞, and the fit itself skips ranks 1
  to 10.
- Not why V1 sits near the bound; the bound is one-sided.
- Nothing about artificial networks; the record's use of it for learned
  representations ([CLAIM-848](../claims.d/CLAIM-848.md)) is an application.
