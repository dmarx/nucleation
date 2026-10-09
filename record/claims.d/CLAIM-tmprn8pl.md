---
status: Active
title: 'A harmonic observable conserves only its mean, and Baez and Fong show that mean conservation for every initial state does not make an observable a symmetry'
version: 1
role: granted
tags:
- mathematics
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- THEORY-158
- LIT-773
- THEORY-tmp3dh4x
objects_to:
- CLAIM-tmpuwwjx
summary: >-
  From the reading of Baez and Fong ([NOTE-598](../notes.d/NOTE-598.md)). The manuscript's Kf = f
  is the mean-only condition, which the cited theorem's counterexample
  shows is weaker than commuting with the generator.
---
<!-- inactive-ok-file: THEORY-tmp3dh4x — Proposed; Baez's account of Noether, cited for why the Markov case differs, not as settled -->

# CLAIM-tmprn8pl: A harmonic observable conserves only its mean, and Baez and Fong show that mean conservation for every initial state does not make an observable a symmetry

## The claim

Baez and Fong's theorem needs the second moment conserved as well as the mean;
their three-state counterexample conserves the mean for every initial state
while the second moment moves, and the observable does not commute with the
generator ([NOTE-598](../notes.d/NOTE-598.md) checked it by hand). The manuscript's discrete-time
criterion Kf = f is a mean condition, so it is a conservation criterion but
not the Noether-type one its section heading claims.

## What it does not say

It does not say Kf = f is useless: a harmonic observable is a martingale, and
the manuscript's drift bound is correct. Whether Kf = f together with K(f²) =
f² gives the discrete-time analogue of the theorem is the record's
extrapolation; Baez and Fong treat continuous time only, and only diagonal
observables, so symmetries that permute states are out of scope.

## Why the Markov theorem is the one that applies

Baez's account of Noether's theorem (LIT-tmpionqf, NOTE-tmpjlwej,
THEORY-tmp3dh4x) puts the equivalence of symmetry and conservation in an
antisymmetric bracket between observables, with reversible one-parameter
groups. A Markov kernel has neither. The manuscript's setting is therefore
the Baez–Fong case, where the mean alone is not enough, and not the
Hamiltonian case where it would be. This is the record's connection; neither
paper draws it.
