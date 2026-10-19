---
status: Open
title: 'Do the hyperbolic Betti-curve matches in odour space and in CA1 separate a hyperbolic metric from a flat sphere or a flat multiscale code, and do they replicate on other data?'
version: 1
tags:
- neuroscience
- natural-sciences
- mathematics
date: '2026-10-19'
line: learned-structure
summary: >-
  The former promote_when clauses of [THEORY-191](../theory.d/THEORY-191.md) and [THEORY-192](../theory.d/THEORY-192.md), moved here
  unchanged when both were narrowed to what was measured and promoted
  under [ADR-047](../decisions.d/ADR-047.md) v3. Each Betti-curve test rejected only uniform Euclidean
  cubes. On a thin shell, hyperbolic distance is nearly a monotone
  function of angle, and uniform hyperbolic sampling is nearly an
  exponential spread of scales, so flat rivals remain. Neither study has
  been repeated on other data or by another group.
---
<!-- inactive-ok-file: THEORY-618 — Proposed; named as the general hypothesis an answer would bear on, not leaned on -->

# QUESTION-tmpq3pd7: Do the hyperbolic Betti-curve matches in odour space and in CA1 separate a hyperbolic metric from a flat sphere or a flat multiscale code, and do they replicate on other data?

## Why it is a question

[THEORY-191](../theory.d/THEORY-191.md) (four natural odour sources and one perceptual data set,
[LIT-872](../literature.d/LIT-872.md)) and [THEORY-192](../theory.d/THEORY-192.md) (twelve CA1 sessions, [LIT-876](../literature.d/LIT-876.md)) report that rank
orders of correlations have the Betti-curve signature of a 3D hyperbolic
ball and not of a uniform Euclidean cube. On 2026-10-19 both were
narrowed to the data measured and promoted, at the owner's direction,
carrying out the promotion audit's batch 018
(record/promotion-audit/decisions/[THEORY-191](../theory.d/THEORY-191.md).yaml and [THEORY-192](../theory.d/THEORY-192.md).yaml,
[ADR-047](../decisions.d/ADR-047.md) v3). Their promote_when clauses moved here unchanged.

It is open for two reasons.

- **The nulls.** The only flat null in each paper is a uniform cube. For
  the odour data, the fitted model is a thin shell, and there hyperbolic
  distance rises strictly with angle, so a sphere or near-sphere in
  Euclidean space would give nearly the same rank order ([NOTE-672](../notes.d/NOTE-672.md): a
  Spearman correlation of about 0.91 in a simulation of the fitted shell).
  For CA1, uniform sampling in a hyperbolic ball is close to an
  exponential distribution of a scale coordinate in flat space, which is
  the paper's own half-space picture ([NOTE-668](../notes.d/NOTE-668.md), [NOTE-670](../notes.d/NOTE-670.md)).
- **Replication.** Each result is one study by one group.

## What would answer it

From [THEORY-191](../theory.d/THEORY-191.md)'s former promote_when: an independent analysis of
natural odour co-occurrence data, from other odour sources or by another
group, that finds the same Betti-curve match to a hyperbolic geometry
AND rejects flat models that share the shell's low-dimensional,
near-spherical arrangement: points on or near a 2-sphere in Euclidean
space, or a flat space with an exponentially distributed scale
coordinate. A replication that again compares the hyperbolic shell only
against uniform Euclidean cubes does not count, because on a thin shell
that comparison cannot separate a hyperbolic metric from a sphere.

From [THEORY-192](../theory.d/THEORY-192.md)'s former promote_when: an independent analysis, on CA1
recordings other than the CRCNS hc-3 and 48-m-track sessions, or by
another group on the same data, that finds the same Betti-curve match to
a 3D hyperbolic ball AND rejects Euclidean models with an exponentially
distributed size coordinate (multiscale fields in a flat space). A
replication that again compares hyperbolic against uniform Euclidean
sampling alone does not count, because that comparison cannot separate a
hyperbolic metric from an exponential distribution of field scales.

A positive answer bears on [THEORY-618](../theory.d/THEORY-618.md), the general hyperbolic-geometry
hypothesis that extends both. [QUESTION-025](QUESTION-025.md) notes the same limit for
co-occurrence geometries.
