---
number: 2141
status: Proposed
formerly:
- THEORY-tmppuotc
promote_when: >-
  A re-derivation of the uniform-tree exponent from the paper's general
  solution, or an independent derivation, and a numerical check on a
  finite uniform tree showing a power-law window with that exponent ending
  in exponential decay.
title: 'Bachas and Huberman show that a random walk among the leaves of an ultrametric tree, with rates set by the height of the common ancestor, relaxes by one exponential mode per branch point, so that on an infinite uniform tree with b offspring per node and per-pair rates falling by a factor g per level the autocorrelation decays as a power of time with exponent ln b/(ln(1/g) − ln b) when gb < 1, while on any finite tree it ends in exponential decay'
version: 1
tags:
- complex-systems
- probabilistic-modeling
- mathematics
date: '2026-11-21'
source:
- LIT-2950
summary: >-
  Ultradiffusion, read as the stand-in for Ogielski and Stein. It is what
  a tree of rate differences ([CLAIM-780](../claims.d/CLAIM-780.md)'s limit) looks like from one
  state over time: a power law, not an exponential. Proposed until its
  promote_when is met.
---
<!-- inactive-ok-file: LIT-2954 CLAIM-780 THEORY-2137 CLAIM-769 — Proposed, Deferred, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2141: Bachas and Huberman show that a random walk among the leaves of an ultrametric tree, with rates set by the height of the common ancestor, relaxes by one exponential mode per branch point, so that on an infinite uniform tree with b offspring per node and per-pair rates falling by a factor g per level the autocorrelation decays as a power of time with exponent ln b/(ln(1/g) − ln b) when gb < 1, while on any finite tree it ends in exponential decay

## Source

Bachas and Huberman, [LIT-2950](../literature.d/LIT-2950.md), read in [NOTE-2218](../notes.d/NOTE-2218.md) from the SLAC preprint, as a stand-in for Ogielski and Stein ([LIT-2954](../literature.d/LIT-2954.md), Unfetched).

## What was actually shown

The general solution on any ultrametric tree (§2), and on uniform trees the exponent v = s/(1 − s), s = ln b/Δh, for s < 1 (§3), with instability for s ≥ 1 and exponential decay on finite trees (§2).

## What this does not say

Nothing about trees whose levels are not uniform beyond §3's remarks, and nothing about Ogielski and Stein's exact exponent.

## Connections

[CLAIM-780](../claims.d/CLAIM-780.md) (the tree in the limit); [THEORY-2137](THEORY-2137.md) (Bovier and colleagues: the hierarchy of metastable sets); [CLAIM-769](../claims.d/CLAIM-769.md) (hyperbolic-like discounting from a tree of rates); the assistant's check of 2026-11-21 (curation entry of that date), which fitted the same exponent on finite trees.
