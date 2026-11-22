---
number: 822
status: Proposed
formerly:
- CLAIM-tmpfwwfy
title: "Concentration of measure, such as a Gaussian vector's concentration on a thin annulus, is an important consideration in modelling a deep network's representational manifold as an active-matter system in high dimension"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that, for deep networks' representations at the widths used in
  practice, the statistics an active-matter reading would take as order
  (concentrated norms, near-orthogonal directions, nearly equal pairwise
  distances, alignment, cone occupancy) depart so far from a concentration
  null matched to the representation's covariance that the null changes no
  conclusion; or an active-matter model of representations whose
  predictions are the same whether or not the high-dimensional baseline is
  subtracted. A demonstration that real representations are anisotropic
  does not meet it: the claim is about the baseline, not about isotropy.
tags:
- representation-learning
- mathematics
- complex-systems
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-515
summary: >-
  The owner's, at U19 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21), on the active-matter model of [QUESTION-515](../questions.d/QUESTION-515.md): "I think an important
  consideration here is concentration of measure, e.g. to a gaussian
  annulus". The other assistant took it as "a crucial correction to the
  model we've been developing" (A30); its development is filed as
  [CLAIM-797](CLAIM-797.md), [CLAIM-838](CLAIM-838.md), [CLAIM-847](CLAIM-847.md) and [CLAIM-799](CLAIM-799.md).
---
<!-- inactive-ok-file: CLAIM-797 CLAIM-838 CLAIM-847 CLAIM-799 CLAIM-848 CLAIM-827 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-tmpvwv5n — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-822: Concentration of measure, such as a Gaussian vector's concentration on a thin annulus, is an important consideration in modelling a deep network's representational manifold as an active-matter system in high dimension

## The claim

The owner, at U19, answering A29's model of a network's representations as
interacting particles: "I think an important consideration here is
concentration of measure, e.g. to a gaussian annulus".

In high dimension, probability concentrates whatever the particles do. An
isotropic Gaussian vector in ℝ^D lies near radius √D in a shell of constant
width; two independent random directions are nearly orthogonal; pairwise
distances are nearly equal. A model that reads structure off a population of
embeddings has to read it against that baseline, or it will take geometry
for organization.

## What it changes

The other assistant's development (A30–A35), filed as A's:

- the baseline itself, and what it rules out as evidence ([CLAIM-797](CLAIM-797.md));
- the scales at which a directional bias overcomes it ([CLAIM-838](CLAIM-838.md));
- concentration set by effective, not ambient, dimension, and its tie to
  power-law spectra ([CLAIM-847](CLAIM-847.md), with the assistant's finite-width correction
  [CLAIM-848](CLAIM-848.md));
- learned structure emerging from the random bulk as a detectability
  threshold ([CLAIM-799](CLAIM-799.md));
- the assistant's comparison of the thresholds this produces ([CLAIM-827](CLAIM-827.md)).

## What it does not say

- Not that trained representations are isotropic or Gaussian. The baseline
  is a null to measure against, and the interesting structure is the
  departure from it.
- Not that concentration is the only consideration, or that it settles
  whether the active-matter model holds ([QUESTION-515](../questions.d/QUESTION-515.md)).

## Note of 2026-11-22: Cai and colleagues, read

Cai, Zhang, Liu and Shi (LIT-2975, NOTE-tmpll97d, THEORY-tmpvwv5n): **background.**
A population energy for contrastive representations on a compact manifold,
with experiments in two and three dimensions; it does not treat
concentration of measure in high dimension. No relation.
