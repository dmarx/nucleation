---
status: Proposed
promote_when: >-
  An independent analysis of natural odour co-occurrence data, from other
  odour sources or by another group, finds the same Betti-curve match to a
  hyperbolic geometry AND rejects flat models that share the shell's
  low-dimensional, near-spherical arrangement: points on or near a 2-sphere
  in Euclidean space, or a flat space with an exponentially distributed
  scale coordinate. A replication that again compares the hyperbolic shell
  against uniform Euclidean cubes alone does not count, because on a thin
  shell hyperbolic distance is nearly a monotone function of angle and
  that comparison cannot separate a hyperbolic metric from a sphere.
title: 'In natural odour sources, the rank order of correlations between compound concentrations has the Betti-curve signature of points near the boundary of a three-dimensional hyperbolic ball, not of a uniform Euclidean cube, and human odour-descriptor profiles have that of a full three-dimensional hyperbolic ball'
version: 1
tags:
- neuroscience
- natural-sciences
- mathematics
date: '2026-10-09'
source:
- LIT-tmpp74b9
summary: >-
  Zhou, Smith & Sharpee (2018), [LIT-tmpp74b9](../literature.d/LIT-tmpp74b9.md): for strawberry, tomato,
  blueberry and mouse-urine volatiles, and for Dravnieks' perceptual
  ratings of 127 odorants, clique-topology Betti curves match a 3D
  hyperbolic model and reject uniform Euclidean cubes of every dimension
  tried. It does not show a tree in the data, and because the fitted
  odour model is a thin shell, it does not separate a hyperbolic metric
  from a sphere in flat space.
---


# THEORY-tmp7qz7l: In natural odour sources, the rank order of correlations between compound concentrations has the Betti-curve signature of points near the boundary of a three-dimensional hyperbolic ball, not of a uniform Euclidean cube, and human odour-descriptor profiles have that of a full three-dimensional hyperbolic ball

## Source

Zhou, Smith & Sharpee (2018), *Science Advances* 4(8):eaaq1458,
[LIT-tmpp74b9](../literature.d/LIT-tmpp74b9.md), Figs. 2 and 5 and Materials and Methods, as read in
[NOTE-tmpaosen](../notes.d/NOTE-tmpaosen.md).

## What was actually shown

Each pair of compounds gets the distance −|corr| of their concentrations
across natural samples. Clique topology turns the matrix into Betti
curves, the counts of 1-, 2- and 3-cycles as the edge threshold sweeps.
The curves depend only on the rank order of the correlations. For each
candidate geometry, as many points as compounds are sampled, their
distances get 4–5% multiplicative noise, and 300 such samples give a
distribution against which the data's integrated Betti values are scored.
Parameters are tuned on the first curve and tested on the second and
third.

For four sources (45–78 compounds over 50–101 samples each), a 3D
hyperbolic ball sampled in the shell 6.3 ≤ r ≤ 7 fits all three curves
(P > 0.19 throughout), with one radius for all four. The best uniform
Euclidean cubes (d = 8 or 10) are rejected (P < 0.03, and < 0.003 for
three of the four). Shuffled data look like random matrices and are
rejected by the hyperbolic model. For Dravnieks' 146-descriptor profiles of
127 odorants, a full 3D hyperbolic ball fits the first two curves, and no
Euclidean dimension matches the first (P < 0.003). Hyperbolic dimension 9
and above is rejected there. The test could reject: it rejected the cubes,
the shuffles and high-dimensional hyperbolic balls.

## What this does not say

- **Not that the odour metric is hyperbolic as against a flat sphere.**
  On a shell of fixed radius, hyperbolic distance increases strictly with
  the angle between points, so the rank order of distances is that of
  points on a 2-sphere. The fitted shell is thin. In a simulation of it
  made for this record, hyperbolic and angular distances have a Spearman
  correlation of about 0.91. A sphere, or a near-sphere, in Euclidean
  space was not among the nulls; only uniform cubes were. The perceptual
  result, on a full ball, is not open to this objection in this form, but
  it shares the general one: a uniform cube is the only flat null, so the
  hyperbolic metric is not separated from a non-uniform distribution of
  points.
- **Not that odour space is a tree.** The hierarchy of biochemical
  pathways motivates the model and is not recovered: compounds spread
  uniformly over the shell and do not cluster by chemical class.
- **Not that the perceptual and stimulus spaces are the same space.** They
  share a dimension and a curvature sign, but with different radii and a
  shell against a full ball, and no mapping between them is fitted.
- **Not general.** Four odour sources, one perceptual dataset. Nothing
  here says other sensory or conceptual spaces are hyperbolic, or that a
  co-occurrence embedding of words would be.
