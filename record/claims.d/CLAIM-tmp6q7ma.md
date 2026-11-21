---
status: Proposed
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
- CLAIM-tmpxi826
grounds:
- THEORY-tmppuotc
- THEORY-tmp2kqhd
- THEORY-1117
summary: >-
  The result of [LEAD-tmp7rohc](../leads.d/LEAD-tmp7rohc.md). The assistant's check of 2026-11-21 found the
  return probability on designed rate trees decaying as a power of time
  with exponent ln b/ln(1/(bg)); Bachas and Huberman, read as a stand-in
  for Ogielski and Stein, give the same exponent, ln b/(ln(1/g) − ln b),
  with its conditions. Sozou, read through Fedus and colleagues, gives
  hyperbolic discounting as exponentials averaged over an exponential
  spread of hazards. Both are averages of exponentials over a spread of
  rates. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmppuotc THEORY-tmp2kqhd LIT-tmpslg57 CLAIM-tmpve51e LEAD-tmp7rohc CLAIM-tmpy75jv — Proposed, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# CLAIM-tmp6q7ma: Seen from one of its states, a tree of rate differences relaxes as a power of time, not exponentially, because the escape it sees is an average of exponentials over a spread of rates; hyperbolic discounting is the same kind of average, so a hierarchy of time scales is one origin of hyperbolic-like discounting, though the exact hyperbola needs a particular spread: per-level rates falling by the square of the branching on a uniform tree, or an exponential spread of hazards

## The claim

**From one state, a rate tree decays as a power law.** On a uniform tree with
b branches per node and per-pair rates falling by a factor g per level, the
probability of still being where one started is a sum over levels of
b^(−k) times an exponential with rate of order (bg)^k. Bachas and Huberman
([THEORY-tmppuotc](../theory.d/THEORY-tmppuotc.md)), read as the stand-in for Ogielski and Stein ([LIT-tmpslg57](../literature.d/LIT-tmpslg57.md),
Unfetched), solve it: on an infinite tree it decays as t^(−v),
v = ln b/(ln(1/g) − ln b), when gb < 1; on any finite tree it ends
exponentially. The assistant's check of 2026-11-21, on designed trees of 729 to
1,024 leaves, fitted exponents within about 5% of the same value (b = 2,
g = 0.1: −0.447 against −0.431; b = 3, g = 0.1: −0.953 against −0.912;
script in the curation entry of 2026-11-21).

**Hyperbolic discounting is the same kind of average.** Sozou, read through
Fedus and colleagues ([THEORY-tmp2kqhd](../theory.d/THEORY-tmp2kqhd.md)), shows that an agent discounting by
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

[CLAIM-tmpve51e](CLAIM-tmpve51e.md)'s E[a^W] = r/(r + ln(1/a)) is the same integral with the roles
of rate and time swapped: the wait is random there, the rate in Sozou.

## What it does not say

- Not that Ainslie's account is explained. It concerns the shape of
  discounting, not his interests, bargaining or personal rules.
- Not that every hierarchy gives a hyperbola. Only particular spreads give
  exponent one; other trees give other powers, and a finite tree ends
  exponentially.
- Not that the two works were read in the original. Ogielski and Stein and
  Sozou are Unfetched; the claim rests on their neighbours.
- [CLAIM-tmpy75jv](CLAIM-tmpy75jv.md)'s qualification applies: in Bachas and Huberman's model a
  level stays a level only while gb < 1, so the branching counts as well as
  the rates.
