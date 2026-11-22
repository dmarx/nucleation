---
status: Proposed
promote_when: >-
  An independent derivation or measurement confirms what the title says:
  that for λ ≠ 0 in one dimension χ = ½ and z = 3/2 (growth exponent ⅓),
  against z = 2 for λ = 0; that λ is marginally relevant in two
  dimensions; and that above two dimensions a small λ is irrelevant. An
  open re-derivation of the RG or of the exact one-dimensional result,
  read and filed, would do, or a reading of the higher-dimensional
  literature beyond Le Doussal's summary; Takeuchi and Sano (LIT-2982)
  already confirm the one-dimensional exponents in experiment.
title: "Kardar, Parisi and Zhang propose ∂h/∂t = ν∇²h + (λ/2)(∇h)² + η, invariant under a shift of h and a small tilt, as the simplest local equation for a growing interface, and by a one-loop dynamic renormalization group find that any nonzero λ is relevant in one dimension and gives a class with χ = ½ and z = 3/2, exact by a fluctuation-dissipation theorem, that λ is marginally relevant in two dimensions, and that above two dimensions a small λ is irrelevant and the surface asymptotically smooth with z = 2"
version: 1
tags:
- complex-systems
- natural-sciences
date: '2026-11-22'
source:
- LIT-2978
corroborates:
- CLAIM-803
bears_on:
- QUESTION-508
summary: >-
  Kardar, Parisi and Zhang (1986), [LIT-2978](../literature.d/LIT-2978.md), read in full in
  [NOTE-tmpf6isj](../notes.d/NOTE-tmpf6isj.md). The equation is argued from locality and symmetry; the
  one-dimensional exponents are exact by a fluctuation-dissipation
  theorem the letter cites rather than shows; the two-dimensional
  conjecture of superuniversality later failed (Le Doussal,
  [THEORY-tmpdcfxq](THEORY-tmpdcfxq.md)). Grounds [CLAIM-841](../claims.d/CLAIM-841.md)'s KPZ row for d ≤ 2
  ([ARG-tmp2xbl4](../arguments.d/ARG-tmp2xbl4.md)) and is one of the three cases of [CLAIM-tmpvq33w](../claims.d/CLAIM-tmpvq33w.md).
  Proposed until confirmed by an independent derivation.
---
<!-- inactive-ok-file: THEORY-tmpmoyol — Proposed; the reading of Takeuchi and Sano -->
<!-- inactive-ok-file: THEORY-tmpdcfxq ARG-tmp2xbl4 CLAIM-tmpvq33w — new or Proposed; this reading, the retrospective read beside it, and the entries it grounds -->
<!-- inactive-ok-file: CLAIM-841 — Proposed; the claim whose KPZ row it grounds -->

# THEORY-tmpo3w5v: Kardar, Parisi and Zhang propose ∂h/∂t = ν∇²h + (λ/2)(∇h)² + η, invariant under a shift of h and a small tilt, as the simplest local equation for a growing interface, and by a one-loop dynamic renormalization group find that any nonzero λ is relevant in one dimension and gives a class with χ = ½ and z = 3/2, exact by a fluctuation-dissipation theorem, that λ is marginally relevant in two dimensions, and that above two dimensions a small λ is irrelevant and the surface asymptotically smooth with z = 2

## Source

Kardar, Parisi and Zhang (1986), "Dynamic Scaling of Growing Interfaces",
Physical Review Letters 56, 889–892, [LIT-2978](../literature.d/LIT-2978.md), read in full in
[NOTE-tmpf6isj](../notes.d/NOTE-tmpf6isj.md) from a course copy.

## The account

The (∇h)² term is "the lowest-order nonlinear term that can appear in
the interface growth equation" (p. 889). The equation "is invariant under
translations h → h + const", and under h → h + ε·x, x → x + λεt, "which
describes the tilting of the interface by a small angle"; the mean
velocity is removed by a moving frame (p. 889). The one-loop flow of
λ̄² = λ²D/ν³ is dλ̄/dl = ((2 − d)/2)λ̄ + K_d((2d − 3)/4d)λ̄³, and λ itself
is not renormalized at this order (p. 891). So:

- d = 1: λ̄ flows to a fixed point where z = 3/2 and χ = ½, which "are
  actually exact" by "a fluctuation-dissipation theorem that holds in
  d = 1 only" (p. 891); the width grows as t^(1/3).
- d = 2: λ "is marginally relevant, and grows under rescaling", to a
  fixed point "not accessible by perturbation theory" (pp. 891–892).
- d ≥ 3: a small λ "is irrelevant, and an asymptotically ideal smooth
  surface is expected with z = 2", with "the possibility of a phase
  transition to different scaling for strong enough couplings" (p. 892).

Three classes follow: random deposition, the linear ("ideal") interface
with χ = (2 − d)/2 and z = 2, and the KPZ class for λ ≠ 0 (p. 892).

## What would have come out otherwise

λ could have been irrelevant in one dimension, leaving the linear
interface; or the static exponent could have told the classes apart. It
does not: in d = 1 both have χ = ½, and only z separates them (p. 891).

## What it does not say

- That KPZ scaling is reached without a threshold in every dimension:
  above two dimensions a small λ flows to the smooth phase.
- That χ = ½, z = 3/2 hold in d = 2: conjectured here, later found false
  (Le Doussal, [THEORY-tmpdcfxq](THEORY-tmpdcfxq.md)).
- Anything about height distributions, which are Tracy-Widom
  ([THEORY-tmpmoyol](THEORY-tmpmoyol.md)), or about tails.
