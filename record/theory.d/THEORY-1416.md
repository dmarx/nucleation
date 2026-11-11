---
number: 1416
status: Active
formerly:
- THEORY-tmppfbrx
title: 'van Leeuwaarden, Mathijsen and Zwart report that Halfin and Whitt showed that in a many-server queue with Poisson arrivals and exponential service the probability that an arrival waits tends to a value strictly between zero and one exactly when the number of servers exceeds the offered load by a multiple of its square root, and that the scaled number in system then tends to a diffusion that is a negative-drift Brownian motion above full occupancy and an Ornstein–Uhlenbeck process below it; they prove the limit of the waiting probability under that scaling'
version: 3
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1577, the reading in part of the tutorial of
    van Leeuwaarden, Mathijsen and Zwart (LIT-2059), standing in for the
    unread Halfin and Whitt (1981), LIT-2085.
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted by the twenty-ninth status review, at the status
    review's ruling (the owner delegated these rulings); ADR-065; ADR-047,
    kind 3. NOTE-1577 v2 reads in full the parts of the tutorial the title
    rests on (§§1, 2.1, 3, 4, 5.1). The title now reports what the tutorial
    states and attributes, and adds the one result it proves (§2.1,
    pp. 7–8). The old title asserted Halfin and Whitt's results directly,
    on the strength of a neighbour's report; the attribution is recorded
    in LIT-2085's status note, and the original stays unread. The old
    title: Halfin and Whitt: in a many-server queue with Poisson arrivals
    and exponential service, the probability that an arrival waits tends to
    a value strictly between zero and one exactly when the number of
    servers exceeds the offered load by a multiple of its square root, and
    the scaled number in system then tends to a diffusion that is a
    negative-drift Brownian motion above full occupancy and an
    Ornstein–Uhlenbeck process below it. The old promote_when: "The
    original (Halfin & Whitt 1981) is read and states the iff condition,
    the limiting delay probability and the diffusion limit for the M/M/s
    queue as the tutorial reports them." The body's "The tutorial gives no
    proof of either" was wrong for the delay limit and is corrected.
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-093. corroborates CLAIM-520 added. The claim's
    note of 2026-11-04 (NOTE-1577): "It supports the claim in kind: in §4,
    headroom over mean load is set by trading a cost of capacity against a
    cost of delay". No other change.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2059
summary: >-
  van Leeuwaarden, Mathijsen and Zwart (2019), [LIT-2059](../literature.d/LIT-2059.md), read in [NOTE-1577](../notes.d/NOTE-1577.md)
  (§§1, 2.1, 3, 4, 5.1). They state Halfin and Whitt's M/M/s results in
  formulas and attribute them to Halfin and Whitt (1981), [LIT-2085](../literature.d/LIT-2085.md), which
  is unread. They prove the delay limit under the square-root scaling, but
  not its converse or the diffusion limit. Active as a report of the
  tutorial. It does not say that capacity sized to mean demand is wrong in
  every regime, nor that the headroom is idle: utilization tends to one.
corroborates:
- CLAIM-520
---
<!-- inactive-ok-file: LIT-2085 — Unavailable; the unread original the tutorial reports, cited as open -->

# THEORY-1416: van Leeuwaarden, Mathijsen and Zwart report that Halfin and Whitt showed that in a many-server queue with Poisson arrivals and exponential service the probability that an arrival waits tends to a value strictly between zero and one exactly when the number of servers exceeds the offered load by a multiple of its square root, and that the scaled number in system then tends to a diffusion that is a negative-drift Brownian motion above full occupancy and an Ornstein–Uhlenbeck process below it; they prove the limit of the waiting probability under that scaling

## Source

Halfin and Whitt (1981), [LIT-2085](../literature.d/LIT-2085.md), the original, which was not read: no
lawful copy was located, and Whitt's own site returned HTTP 403. Sourced to
the tutorial of van Leeuwaarden, Mathijsen and Zwart (2019), [LIT-2059](../literature.d/LIT-2059.md),
read in [NOTE-1577](../notes.d/NOTE-1577.md), which stands in for it at the owner's request.

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
- **What the tutorial proves** (§2.1, pp. 7–8): the delay limit under the
  scaling, by the Central Limit Theorem for the Poisson distribution and
  Stirling's formula, substituted into the relation between the Erlang B
  and C formulae. §5.1 gives bounds that provide "an alternative proof and
  confirmation of Proposition 2.1" (p. 20). The "only if" is attributed,
  not proved. For the diffusion it gives "a heuristic explanation" (p. 9)
  and says the original's proof "relies on Stone's Theorem" (p. 16). A
  numerical check of the delay limit, with controls, is
  scratch/formal/readiness_erlangc_check.py.

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
