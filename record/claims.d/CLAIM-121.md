---
number: 121
status: Active
formerly:
- CLAIM-tmpze62b
title: 'A transport whose local kernels commute with restriction maps overlap-consistent source models to overlap-consistent target models'
version: 1
role: thesis
defeated_if: >-
  A family of local kernels that commutes with restriction carries an
  overlap-consistent source model to a target model whose marginals
  disagree on some mapped overlap.
tags:
- mathematics
- contextuality
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
answers:
- QUESTION-022
uses:
- TERM-008
summary: >-
  Proposition I of A84, Proposition B1 of C6, the manuscript's
  Proposition 1. It concerns marginal consistency, not global
  noncontextuality.
supports:
- CLAIM-100
---
<!-- inactive-ok-file: CLAIM-100 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-121: A transport whose local kernels commute with restriction maps overlap-consistent source models to overlap-consistent target models

## The claim

A84 proposed three anchoring propositions; this is the first. C6 Proposition
B1: "For finite scenarios with a compatible stochastic transport K_C, if the
source empirical laws are overlap-consistent, then the transported family is
overlap-consistent. Proof: restrict a transported context distribution; use
kernel restriction-compatibility to exchange pushforward and restriction; then
use source overlap consistency; repeat from the second context." Manuscript §6,
Proposition 1, with the same sketch.

## What it does not say

C6: "This proposition concerns overlap consistency, not preservation of
noncontextuality under all imaginable maps." The manuscript: "not automatically
global noncontextuality".

## What was checked

C7 Appendix A's proof, read on 2026-10-09: "For any two contexts C,F with overlap
D, the target marginal from K_C#e_C on τ(D) equals K_D#(ρ^C_D#e_C). Source
consistency makes the latter K_D#e_D, which also equals the corresponding target
marginal from F." Each step holds: the first is the naturality assumption
(marginalizing after K_C equals K_D after marginalizing), the second is source
overlap consistency, and the third is the same argument from F. Two conditions
are needed and both are stated in C7. Kernels K_D must exist for each overlap D,
which "for every inclusion D⊆C" supplies if the family is closed under overlaps.
The conclusion is consistency on τ(D), which is the mapped overlap only when
τ(C) ∩ τ(F) = τ(C ∩ F). Appendix A says so itself: "If mapped overlaps are
larger than images of source overlaps, the stated conditions must cover those
extra target variables too; this is why the geometric assumptions on τ matter."
The manuscript's "consistent on the mapped overlaps" is right under that reading.
Active.

## Prior art

This proposition is a special case of Karvonen's "Categories of Empirical
Models" ([LIT-tmpes6yu](../literature.d/LIT-tmpes6yu.md)). His natural transformation σ is exactly the family of local kernels commuting with restriction, and his
Lemma 3.12 states the limit that local kernels need not glue. The record's
reader drew this mapping; Karvonen does not mention translation. The
manuscript should cite it.
