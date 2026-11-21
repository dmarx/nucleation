---
number: 769
status: Proposed
formerly:
- CLAIM-tmp6q7ma
title: 'Seen from one of its states, a tree of rate differences relaxes as a power of time, not exponentially, because the escape it sees is an average of exponentials over a spread of rates; hyperbolic discounting is the same kind of average, so a hierarchy of time scales is one origin of hyperbolic-like discounting, though the exact hyperbola needs a particular spread: per-level rates falling by the square of the branching on a uniform tree, or an exponential spread of hazards'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) A uniform rate tree, infinite or deep enough,
  whose return probability from one leaf does not decay as a power of
  time with exponent ln b/(ln(1/g) − ln b) over the window before the
  root's time, contrary to Bachas and Huberman and to the assistant's
  check. (b) A showing that the discounting an agent exhibits is not an
  average of exponentials over hazard or time-scale rates in the cases the
  claim names, so that the shared form is a coincidence of functional
  shape and not a shared mechanism.
tags:
- complex-systems
- motivation
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
- will-organization
rests_on:
- CLAIM-780
grounds:
- THEORY-2141
- THEORY-2131
- THEORY-1117
summary: >-
  The result of [LEAD-200](../leads.d/LEAD-200.md). The assistant's check of 2026-11-21 found the
  return probability on designed rate trees decaying as a power of time
  with exponent ln b/ln(1/(bg)); Bachas and Huberman, read as a stand-in
  for Ogielski and Stein, give the same exponent, ln b/(ln(1/g) − ln b),
  with its conditions. Sozou, read through Fedus and colleagues, gives
  hyperbolic discounting as exponentials averaged over an exponential
  spread of hazards. Both are averages of exponentials over a spread of
  rates. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2141 THEORY-2131 LIT-2954 CLAIM-777 LEAD-200 CLAIM-781 — Proposed, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->
<!-- inactive-ok-file: LIT-tmp1b7mm CLAIM-tmp1dlyp CLAIM-tmpr9au6 CLAIM-tmplb1ow — Deferred or new; cited in the note of 2026-11-21 on the exchange "Rich Get Richer Power Laws" -->

# CLAIM-769: Seen from one of its states, a tree of rate differences relaxes as a power of time, not exponentially, because the escape it sees is an average of exponentials over a spread of rates; hyperbolic discounting is the same kind of average, so a hierarchy of time scales is one origin of hyperbolic-like discounting, though the exact hyperbola needs a particular spread: per-level rates falling by the square of the branching on a uniform tree, or an exponential spread of hazards

## The claim

**From one state, a rate tree decays as a power law.** On a uniform tree with
b branches per node and per-pair rates falling by a factor g per level, the
probability of still being where one started is a sum over levels of
b^(−k) times an exponential with rate of order (bg)^k. Bachas and Huberman
([THEORY-2141](../theory.d/THEORY-2141.md)), read as the stand-in for Ogielski and Stein ([LIT-2954](../literature.d/LIT-2954.md),
Unfetched), solve it: on an infinite tree it decays as t^(−v),
v = ln b/(ln(1/g) − ln b), when gb < 1; on any finite tree it ends
exponentially. The assistant's check of 2026-11-21, on designed trees of 729 to
1,024 leaves, fitted exponents within about 5% of the same value (b = 2,
g = 0.1: −0.447 against −0.431; b = 3, g = 0.1: −0.953 against −0.912;
script in the curation entry of 2026-11-21).

**Hyperbolic discounting is the same kind of average.** Sozou, read through
Fedus and colleagues ([THEORY-2131](../theory.d/THEORY-2131.md)), shows that an agent discounting by
survival under a constant but unknown hazard discounts by the prior-weighted
average of exponentials: an exponential spread of hazards gives exactly
1/(1 + kt), a gamma spread 1/(1 + bt)^c.

**So.** In both, an exponential at each rate, averaged over a spread of rates,
gives slower-than-exponential decay. A hierarchy of time scales, seen from one
of its levels, is one such spread. Ainslie's hyperbolic discounting
([THEORY-1117](../theory.d/THEORY-1117.md)) is then what an agent whose relevant hazards or time scales form
a hierarchy would show, with the caveat that the exact hyperbola, asymptotic
exponent one, needs a particular spread: v = 1 on a uniform tree requires
g = 1/b², and Sozou's exact form requires an exponential prior.

[CLAIM-777](CLAIM-777.md)'s E[a^W] = r/(r + ln(1/a)) is the same integral with the roles
of rate and time swapped: the wait is random there, the rate in Sozou.

## What it does not say

- Not that Ainslie's account is explained. It concerns the shape of
  discounting, not his interests, bargaining or personal rules.
- Not that every hierarchy gives a hyperbola. Only particular spreads give
  exponent one; other trees give other powers, and a finite tree ends
  exponentially.
- Not that the two works were read in the original. Ogielski and Stein and
  Sozou are Unfetched; the claim rests on their neighbours.
- [CLAIM-781](CLAIM-781.md)'s qualification applies: in Bachas and Huberman's model a
  level stays a level only while gb < 1, so the branching counts as well as
  the rates.

## Note of 2026-11-21: the exchange "Rich Get Richer Power Laws"

A5 §4 of that exchange gives the same average as a route to power laws:
exponential waiting times whose rates are gamma-distributed give
P(T > t) = (b/(b + t))^a, which is THEORY-2131's gamma case read as a
survival function. The assistant checked it by two million draws (a = 1.5,
b = 2: 0.0680 against 0.0680 at t = 10). The exchange adds two things this
claim does not state. The first is the name superstatistics (Beck,
LIT-tmp1b7mm, registered and unread). The second is a caution: "If a
dataset displays a power law, that does not necessarily mean any
individual entity follows power-law dynamics." The caution applies here
too. A power law in the population's escape does not show a power law in
any one state's dynamics, only a spread of exponential rates. The
exchange's catalogue is CLAIM-tmp1dlyp (item 4). The same mechanism is
also why a bulk with a long tail does not by itself mark a system near a
transition, which bears on the owner's conjecture CLAIM-tmpr9au6 and its
reading CLAIM-tmplb1ow. The claim is unchanged.
