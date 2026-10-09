---
number: 192
status: Proposed
formerly:
- THEORY-tmpae88o
promote_when: >-
  An independent analysis, on CA1 recordings other than the CRCNS hc-3 and
  48-m-track sessions used here or by another group on the same data,
  finds the same Betti-curve match to a 3D hyperbolic ball AND rejects
  Euclidean models in which a size coordinate is exponentially distributed
  (multiscale fields in a flat space), not only uniform Euclidean cubes.
  A replication that again compares hyperbolic against uniform Euclidean
  sampling alone does not count, because that comparison cannot separate
  a hyperbolic metric from an exponential distribution of field scales.
title: 'Pairwise correlations among rat CA1 place cells have the Betti-curve signature of points sampled uniformly from a three-dimensional hyperbolic ball, not of a low-dimensional Euclidean cube, and the fitted radius grows with the logarithm of exploration time'
version: 1
tags:
- neuroscience
- mathematics
date: '2026-10-09'
source:
- LIT-876
summary: >-
  Zhang, Rich, Lee & Sharpee (2022), [LIT-876](../literature.d/LIT-876.md): in twelve sessions
  from three data sets, the rank order of CA1 spike correlations matched
  uniform samples from a 3D hyperbolic ball and not uniform samples from
  low-dimensional Euclidean cubes or shuffled data, and the ball's radius
  rose with log exploration time from seconds to days. It does not show
  that the metric, as opposed to the distribution of field scales, is
  hyperbolic, nor that a tree is represented.
---

# THEORY-192: Pairwise correlations among rat CA1 place cells have the Betti-curve signature of points sampled uniformly from a three-dimensional hyperbolic ball, not of a low-dimensional Euclidean cube, and the fitted radius grows with the logarithm of exploration time

## Source

Zhang, Rich, Lee & Sharpee (2022 online; *Nature Neuroscience* 26, 2023),
[LIT-876](../literature.d/LIT-876.md), Figs. 2–3 and Extended Data Figs. 1–10, as read in
[NOTE-668](../notes.d/NOTE-668.md).

## What was actually shown

Each neuron's distance to another is its negated spike correlation over
±1 s. Clique topology turns the matrix into Betti curves, the counts of
1-, 2- and 3-cycles as the edge threshold sweeps from sparse to complete;
the curves depend only on the rank order of the correlations. For each
candidate geometry, as many points as recorded cells are sampled
uniformly, their distances (with 5% noise) give model Betti curves, and
300 such samples give a distribution.

In three rats on a novel 48-m track, two 2.5-m track sessions and seven
1.8-m box sessions (34–56 active cells in the sessions shown), the data
fell inside the 3D hyperbolic distribution and outside the Euclidean
cube distributions on integrated Betti values and L1 distances; shuffled
spike trains fell outside the hyperbolic one. The test could reject: it
rejected the Euclidean cubes and the shuffled data, and it rejects
hyperbolic balls of the wrong radius or dimension.
3D fitted better than the other hyperbolic dimensions compared.

The radius grew with log exploration time across days (box, r = 0.85),
and within seconds on the long track when estimated from the exponential
rate of place-field sizes (r = 0.50). Behavioural covariates did not
account for it, and four hours away from the track did not advance it.

## What this does not say

- **Not that the metric is hyperbolic as against flat.** The nulls are
  uniform cubes. Uniform sampling in a hyperbolic ball and an exponential
  distribution of a scale coordinate are close to the same thing, and the
  paper's own construction (field centre in the plane, field size as
  height) is the half-space picture of it. A flat model with
  exponentially distributed field sizes was not tested.
- **Not that the code is a tree.** No branching structure is inferred.
  "Hierarchical" means fields of many sizes, with smaller ones more
  numerous, and larger ones containing smaller ones.
- **Not that the radius is optimal.** The match between the measured
  radius and the Fisher-optimal one for CA1's cell count is an
  extrapolation of a simulated curve under independent Poisson neurons.
- **Not general.** Dorsal CA1 of rats, spatial tasks, a few environments.
  Nothing here says that non-spatial or cortical codes are hyperbolic, or
  that semantic or categorical hierarchies are represented this way.
