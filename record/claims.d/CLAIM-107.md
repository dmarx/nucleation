---
number: 107
status: Proposed
formerly:
- CLAIM-tmpuwwjx
title: 'A pragmatic observable is conserved under a Markov reconstruction process when it is harmonic for the kernel, which gives a Noether-type conservation criterion'
version: 1
role: thesis
defeated_if: >-
  A Markov reconstruction model in which an observable satisfies the
  manuscript's criterion yet its distribution, not only its mean, drifts
  in a way the manuscript counts as non-conservation.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-09'
line: pragmatic-transport
works:
- what-survives-translation
grounds:
- THEORY-158
summary: >-
  The manuscript's §4, citing Baez and Fong. [CLAIM-094](CLAIM-094.md) says what
  the cited theorem needs that the discrete-time criterion leaves out.
objected_by:
- CLAIM-094
complements:
- CLAIM-093
---
<!-- inactive-ok-file: THEORY-158 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-107: A pragmatic observable is conserved under a Markov reconstruction process when it is harmonic for the kernel, which gives a Noether-type conservation criterion

## The claim

§4 cites Baez and Fong ([LIT-773](../literature.d/LIT-773.md)) correctly: for finite continuous-time Markov
processes, a diagonal observable commutes with the generator exactly when its
expectation and second moment are conserved for every initial distribution
([THEORY-158](../theory.d/THEORY-158.md)). It then states its own discrete-time criterion, Kf = f, under
which f(S_n) is a martingale and E f(S_n) is invariant, and bounds the drift
of the mean by Σε_i when ‖K_i f − f‖ ≤ ε_i.

## What it does not say

The manuscript says plainly that Noether's hypotheses do not hold
automatically in communicative systems, and that its bounds are
expectation-preservation estimates only.

## Where it came from

The owner's U37 objection: "symmetry is a kind of invariance, no? isn't that part
of the point of Noether Theory?" ([CLAIM-040](CLAIM-040.md)). A105 conceded and found Baez
and Fong's Noether theorem for Markov processes: "a genuine
conservation-theoretic connection for the continuous-time Markov special case".
It also gave the discrete harmonic condition Kf = f, its approximate form
(‖Kf − f‖∞ ≤ ε gives drift at most nε, or Σε_i), and a candidate conserved
quantity: "Whether the speaker and audience occupy positions of solidarity or
normative asymmetry". A105's stronger condition, K(h∘f) = h∘f for all bounded h,
which conserves the whole distribution, became the manuscript's "stronger
conditions" without the formula. The limit on borrowing Noether is
[CLAIM-093](CLAIM-093.md).
