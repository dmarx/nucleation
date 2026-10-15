---
status: Active
title: 'The monograph''s castle topic, persistent across refinement by construction,
  persists as no eigenmode: in its rank-2 and rank-3 co-occurrence matrices the
  eigenvector nearest the castle topic changes rank and turns through about 51°,
  and every eigenvector mixes signs'
version: 1
standing: fictional
kind: construction
tags:
- probabilistic-modeling
- mathematics
date: '2026-10-15'
line: formal-apparatus
illustrates:
- CLAIM-148
summary: >-
  Appendix H of Part III of the owner's LEGO monograph builds two co-occurrence
  matrices from nonnegative topics. One has topics for spaceship and castle; the
  other splits spaceship into wings and engines and keeps castle unchanged. The
  monograph reads castle's survival as a stable eigenmode and calls that archetype
  persistence. Computed here: the topics overlap (ship·castle = 0.21), so no eigenvector
  is the castle topic. The eigenvector closest to it is the second mode at rank
  2 (cosine 0.873) and the first at rank 3 (0.926), about 51° apart. Persistence
  of a generating factor does not show as persistence of an eigenvector, which is
  what [CLAIM-148](../claims.d/CLAIM-148.md)'s identifiability limits predict.
---
<!-- inactive-ok-file: QUESTION-tmpjnf86 — new; the question this bears on -->

# CASE-tmpliavq: The monograph's castle topic, persistent across refinement by construction, persists as no eigenmode: in its rank-2 and rank-3 co-occurrence matrices the eigenvector nearest the castle topic changes rank and turns through about 51°, and every eigenvector mixes signs

## The case

Appendix H ("Spectral Toy Example — Stable Core Topics Across Refinement"),
over four parts: wing, engine, window, door.

- **Rank 2.** M² = 3·φ_ship φ_shipᵀ + 2·φ_castle φ_castleᵀ, with
  φ_ship = (0.7, 0.7, 0.1, 0.1) and φ_castle = (0.05, 0.05, 0.7, 0.7).
- **Rank 3.** M³ = 1.5·φ_wing φ_wingᵀ + 1.2·φ_engine φ_engineᵀ +
  2·φ_castle φ_castleᵀ, with φ_wing = (0.9, 0.1, 0.1, 0.1),
  φ_engine = (0.1, 0.9, 0.1, 0.1), and castle unchanged.

The appendix's entries were checked here and are right. It concludes:
"**Stable core:** 'castle' is preserved exactly across refinement", and
the surrounding chapters read archetypes as "strong eigenmodes" that
"persist under refinement (blowup)".

**Computed here** with numpy.

| | eigenvalues | cosine of castle topic with modes 1, 2, 3 |
|---|---|---|
| M² | 3.213, 1.757, 0, 0 | 0.488, 0.873, 0.000 |
| M³ | 2.215, 1.191, 0.831, 0 | 0.926, 0.372, 0.057 |

M²'s second eigenvector is (−0.30, −0.30, 0.64, 0.64), a contrast of castle
against ship, not castle. M³'s first is (−0.35, −0.27, −0.64, −0.64). The
two are about 51° apart (|cosine| 0.63).

## What it can show

That "castle persists" is true of the factor the matrices were built from
and false of their eigenvectors. The topics overlap, and eigenvectors are
orthogonal, so the spectrum cannot return them. [CLAIM-148](../claims.d/CLAIM-148.md) gives the
general form. A factorization is identified only up to a change of latent
coordinates, and nonnegativity narrows that only under further conditions
(anchors). [CASE-042](CASE-042.md) is the same point for collaborative filtering and topic
models. A persistence criterion for naming a category ([QUESTION-tmpjnf86](../questions.d/QUESTION-tmpjnf86.md))
has to be stated for factors recovered under such conditions, not for
eigenvectors.

## What it cannot show

That spectral methods cannot recover topics. They can, given anchor
words or higher moments. The monograph's other worked example
(Part III, 2b) uses orthogonal directions by construction, and there the
eigenvectors are the directions it built.
