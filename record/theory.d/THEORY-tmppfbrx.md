---
status: Proposed
promote_when: >-
  The original (Halfin & Whitt 1981) is read and states the iff condition, the limiting delay probability and the diffusion limit for the M/M/s queue as the tutorial reports them.
title: 'Halfin and Whitt: in a many-server queue with Poisson arrivals and exponential service, the probability that an arrival waits tends to a value strictly between zero and one exactly when the number of servers exceeds the offered load by a multiple of its square root, and the scaled number in system then tends to a diffusion that is a negative-drift Brownian motion above full occupancy and an Ornstein–Uhlenbeck process below it'
version: 1
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-tmpf2bau
summary: >-
  Halfin and Whitt (1981), [LIT-tmpodkh1](../literature.d/LIT-tmpodkh1.md), unread, as reported by the tutorial of van Leeuwaarden, Mathijsen and Zwart (2019), [LIT-tmpf2bau](../literature.d/LIT-tmpf2bau.md), skimmed in [NOTE-tmpbp6yl](../notes.d/NOTE-tmpbp6yl.md) (§§1, 2.1, 3, 4). The tutorial states both results in formulas and attributes them to Halfin and Whitt, without their proofs. Proposed until the original is read. It does not say that capacity sized to mean demand is wrong in every regime, nor that the headroom is idle: utilization tends to one.
---
<!-- inactive-ok-file: LIT-tmpodkh1 NOTE-tmpbp6yl — Unavailable or Skimmed, and new; the unread original and the reading of the tutorial that stands in for it, cited as open -->

# THEORY-tmppfbrx: Halfin and Whitt: in a many-server queue with Poisson arrivals and exponential service, the probability that an arrival waits tends to a value strictly between zero and one exactly when the number of servers exceeds the offered load by a multiple of its square root, and the scaled number in system then tends to a diffusion that is a negative-drift Brownian motion above full occupancy and an Ornstein–Uhlenbeck process below it

## Source

Halfin and Whitt (1981), [LIT-tmpodkh1](../literature.d/LIT-tmpodkh1.md), the original, which was not read: no lawful copy was located, and Whitt's own site returned HTTP 403. Sourced to the tutorial of van Leeuwaarden, Mathijsen and Zwart (2019), [LIT-tmpf2bau](../literature.d/LIT-tmpf2bau.md), read in part in [NOTE-tmpbp6yl](../notes.d/NOTE-tmpbp6yl.md), which stands in for it at the owner's request.

## What was actually shown

- **The delay probability** (§2.1, Prop. 2.1, p. 7 of the arXiv PDF): with
  s servers and offered load λ, the Erlang-C delay probability tends to
  g(β) = [1 + βΦ(β)/φ(β)]⁻¹, strictly between 0 and 1, if and only if
  (1 − ρ)√s → β > 0, which is s ≈ λ + β√λ. The tutorial says Halfin and
  Whitt "showed that this is in fact the only scaling regime in which such
  a non-degenerate limit exists and identified" its value.
- **The diffusion** (§2.1, Thm 2.2, pp. 9–10): the centred, scaled number
  in system tends to a process with drift −β above zero and −β − x below,
  which "is a combination of a negative-drift Brownian motion" above zero
  and an Ornstein–Uhlenbeck process below; its stationary distribution and
  the steady-state interchange are credited to Halfin and Whitt.
- The tutorial gives no proof of either, saying the original's "relies on
  Stone's Theorem" (p. 16).

## What this does not say

- That the original states these results in this form: it was not read,
  beyond one sentence the tutorial quotes from it.
- That capacity sized to mean demand is wrong: the efficiency-driven and
  quality-driven regimes are legitimate choices, and the result is about
  when the delay probability is non-degenerate.
- That the headroom is reserve kept idle: utilization tends to one, and
  large pooled systems need proportionally less spare capacity.
- Anything about finite systems without care (§1, p. 6), or about arrival
  processes and models other than M/M/s, which the tutorial does not report
  from the original.
