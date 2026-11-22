---
status: Proposed
promote_when: >-
  An independent simulation or analysis of phase-frustrated identical
  oscillators on hierarchically modular networks reproduces what the title
  says: chimera and metastable states from mesoscale structure alone; the
  population-level states following the Laplacian's slow modes, with a
  reduction to the two-population model that holds when the gap to the
  fast modes is large and fails when it is small; and module coherence
  lost once the gap between the lowest two layers falls below a threshold.
  The threshold's value near 2 is not required.
title: 'Caprioglio and Berthouze report that in simulations of identical phase-frustrated oscillators on three-layer hierarchically modular networks, mesoscale structure alone yields chimera and metastable states; the states of the upper layers follow the network Laplacian''s slow modes, which reduce the network to the two-population model only when their gap to the fast modes is large, and the lowest-layer modules stay coherent, each acting as a single macro-oscillator, only while the spectral gap between the lowest two layers exceeds a threshold, below which they desynchronize and resynchronize metastably'
version: 1
tags:
- network-science
- complex-systems
- neuroscience
date: '2026-11-22'
source:
- LIT-2241
corroborates:
- CLAIM-478
- CLAIM-157
- CLAIM-tmpa694z
bears_on:
- QUESTION-391
summary: >-
  Caprioglio and Berthouze (2024), [LIT-2241](../literature.d/LIT-2241.md), read in [NOTE-tmp3gqv7](../notes.d/NOTE-tmp3gqv7.md)
  (appendices skipped). Numerical, one network family, N = 512. It
  corroborates [CLAIM-478](../claims.d/CLAIM-478.md)'s first half with its version-5 condition, a gap
  between levels large against the spread within, and [CLAIM-157](../claims.d/CLAIM-157.md)'s
  gap-isolated block as the unit; and it bears on [QUESTION-391](../questions.d/QUESTION-391.md), since the
  coarse-grained description fails as the gap closes. It also shows an
  Ott–Antonsen-based reduction of a network holding only with a large gap,
  which supports [CLAIM-tmpa694z](../claims.d/CLAIM-tmpa694z.md). Proposed until reproduced independently.
---
<!-- inactive-ok-file: CLAIM-tmpa694z — Proposed; the verdict of LEAD-094 this reading supports -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-157 — Proposed; the claims this reading corroborates -->

# THEORY-tmpgdriu: Caprioglio and Berthouze report that in simulations of identical phase-frustrated oscillators on three-layer hierarchically modular networks, mesoscale structure alone yields chimera and metastable states; the states of the upper layers follow the network Laplacian's slow modes, which reduce the network to the two-population model only when their gap to the fast modes is large, and the lowest-layer modules stay coherent, each acting as a single macro-oscillator, only while the spectral gap between the lowest two layers exceeds a threshold, below which they desynchronize and resynchronize metastably

## Source

Caprioglio and Berthouze (2024), "Emergence of metastability in frustrated
oscillatory networks: the key role of hierarchical modularity", *Frontiers
in Network Physiology* 4: 1436046, [LIT-2241](../literature.d/LIT-2241.md), read from the arXiv preprint
in [NOTE-tmp3gqv7](../notes.d/NOTE-tmp3gqv7.md).

## The account

A nested stochastic block model with one structural parameter H fixes the
mean degree while moving connections between and within the two
populations. Identical Kuramoto–Sakaguchi oscillators, lagged only between
modules, show coherence at low H, stable and breathing chimeras at
intermediate H, metastable and alternating chimeras near H = 0.5, and
decoupled populations above about 0.7. The graph Laplacian has two gaps,
one between the slowest mode and the population modes, one between the
population modes and the module modes. Keeping the slow modes reproduces
the two-population model's chimeras when the second gap is large; the
modules stay fully synchronized, acting as single macro-oscillators, when
that gap exceeds about 2, and below it they desynchronize and
resynchronize under the slow modes' influence.

## Bearing

Evidence for [CLAIM-478](../claims.d/CLAIM-478.md)'s first half (a gap between levels makes the
module a unit that constrains its members) and for [CLAIM-157](../claims.d/CLAIM-157.md)'s
gap-isolated block; on [QUESTION-391](../questions.d/QUESTION-391.md), the slow description fails when the
fast modes come back as the gap closes. Its reduction to an Ott–Antonsen
model held only with a large gap, which bears on the verdict of [LEAD-094](../leads.d/LEAD-094.md)
([CLAIM-tmpa694z](../claims.d/CLAIM-tmpa694z.md)).
