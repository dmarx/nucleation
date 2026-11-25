---
number: 339
status: Proposed
formerly:
- CASE-tmpg9x2o
title: 'Holonomy across three evaluative contexts'
statement: >-
  Three simulated evaluative contexts with transport derived by fit on
  shared commitments give holonomy indistinguishable from the identity in
  3000 draws of the null, a holonomy angle equal to the sum of the contexts'
  internal comparison angles in the planar case, and the spherical excess
  for local charts of a curved space of profiles; noise gives a measurable
  null, and few anchors per overlap let it flip orientation
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-067 by delegation.
    Code, tests and results are under scratch/studies/lead-067/.
standing: documented
kind: executed-study
tags:
- mathematics
- ethics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
illustrates:
- CLAIM-907
bears_on:
- QUESTION-130
summary: >-
  The numerical side of [LEAD-067](../leads.d/LEAD-067.md): the construction of [CLAIM-907](../claims.d/CLAIM-907.md) run in
  numpy (seed 20261122). In the null (one configuration, three random O(d)
  frames, 1000 draws at each of three sizes), the largest ‖H − I‖ is
  2.2e-14. In the planar case, the holonomy angle equals the sum of the
  internal angles in 12 of 12 draws. Local log-map charts of the sphere
  give a holonomy within 0.3% of the triangle's spherical excess. With
  representation noise σ, the null's holonomy has median about 1.3σ at ten
  anchors per overlap, but with three anchors up to 23% of draws flip
  orientation. With an underdetermined overlap, the holonomy runs from
  0.006 to 2.83 under exact fits. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-907 — Proposed; the claim filed with this study -->

# CASE-339: Holonomy across three evaluative contexts

## The case

[LEAD-067](../leads.d/LEAD-067.md) asks for A19 §8's finite construction for [QUESTION-130](../questions.d/QUESTION-130.md): three overlapping contexts, the comparisons each overlap shares, transport derived from them, and the loop's holonomy, starting with the null. [CLAIM-907](../claims.d/CLAIM-907.md) states and proves the construction. This case is its numerical run (scratch/studies/lead-067/: `transport.py`, `test_transport.py` with 18 passing tests, `run_study.py`, `results.json`, and a README saying how to rerun).

Context c holds vectors in ℝᵈ for the commitments it holds. The transport between two contexts is the orthogonal Procrustes fit on the commitments they share, and it is flagged undetermined when the fit is not unique. The holonomy is H = T_AC T_CB T_BA. Five runs, seed 20261122:

- **The null.** One configuration of commitments, with each context in its own random O(d) frame. At (d, k) = (2, 2), (3, 3) and (5, 6), with k commitments per overlap, 1000 draws each, the largest ‖H − I‖_F is 2.2e-14. The median frame differences ‖g_a − g_b‖ are 1.6 to 2.9, so the contexts' coordinates differ widely. One draw at (3, 3) had a near-coplanar overlap flagged undetermined.
- **The planar case.** Each context holds two pairs of commitments, and the pairs sit at an internal angle θ_c drawn from U(−1.2, 1.2). In 12 draws the holonomy's angle equals |θ_A + θ_B + θ_C| mod 2π to printing precision. Every overlap fits exactly (residual < 1e-15), and gluing into one configuration fails by 0.03 to 2.0.
- **Curved charts.** Commitments are normalized profiles, that is, unit vectors in ℝ³. Each context is the log-map chart at its own reference profile, in a frame of its own, and the fits are made on centred anchors. For geodesic triangles with sides 0.2 to 1.2 rad, the mean |holonomy angle| over 20 draws at anchor spread 0.0025 is within 0.3% of the spherical excess: 0.0201 against 0.0201, 0.0822 against 0.0821, 0.3537 against 0.3538, and 0.8758 against 0.8755. The same chart construction on a plane gives H = I (a test).
- **The noisy null** (d = 3, 500 draws per cell). Each representation is perturbed by N(0, σ²).
  - With ten commitments per overlap, the median ‖H − I‖ is about 1.3σ and the 95th percentile about 2.4σ, at every σ from 0.001 to 0.1, with no orientation flips.
  - With three commitments per overlap, 0.2%, 2.6%, 8.8% and 23% of draws at σ = 0.001, 0.01, 0.03 and 0.1 have det H = −1. In those draws ‖H − I‖ ≥ 2: a gross holonomy produced by noise on a near-degenerate overlap.
- **Underdetermination.** If A and B share one commitment in ℝ³, every transport in a one-parameter family fits it exactly. Over the free angle, ‖H − I‖ runs from 0.006 to 2.83.

## What it can show

It is documented as a computation. It shows that the constructions of [CLAIM-907](../claims.d/CLAIM-907.md) behave as the proof says, and it supplies two things the proof does not.

- **A noise null.** A measured holonomy is evidence against the null only beyond the null's spread, which is about 2.4σ at ten anchors per overlap. With few anchors, orientation flips have to be checked separately, by det H and by whether each fit is determined.
- **A nontrivial holonomy that is derived and not chosen, of the kind [QUESTION-130](../questions.d/QUESTION-130.md)'s note of 2026-10-29 sets aside.** In the curved-chart run the holonomy is forced by the charts and equals the area the loop encloses. But the curvature belongs to the representation, linear charts of a space of normalized profiles, and not to anything evaluated. It is the Sengupta reading's lesson ([NOTE-1350](../notes.d/NOTE-1350.md)) again, now between contexts.

It cannot show that any real evaluative contexts carry representations like these. The planar case's nonzero angle sum is constructed, not measured. Whether real contexts' comparisons ever fail to close, and whether they do so beyond the noise null, is the open part of [QUESTION-130](../questions.d/QUESTION-130.md).
