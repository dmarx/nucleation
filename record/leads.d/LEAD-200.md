---
number: 200
status: Done
formerly:
- LEAD-tmp7rohc
title: 'Check whether a hierarchy of time scales, seen from one level, decays hyperbolically rather than exponentially: whether relaxation summed over the levels of an ultrametric tree gives a power law, and whether hyperbolic discounting is exponential discounting averaged over a spread of hazard rates, which would tie Ainslie''s account of will to the time geometry of a hierarchy'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Done on 2026-11-21: the formal step run, both works sought and read
    through neighbours, and the claim filed.
stage: underway
priority: low
method:
- reading
- formal
tags:
- complex-systems
- motivation
- mathematics
date: '2026-11-20'
line:
- formal-apparatus
- will-organization
advances:
- CLAIM-781
- THEORY-1117
summary: >-
  The third sense of hyperbolicity the assistant named on 2026-11-20, kept
  apart because it rests on memory. Two classical results are recalled,
  not read: power-law relaxation on ultrametric spaces ([LIT-2954](../literature.d/LIT-2954.md)) and
  hyperbolic discounting from uncertain hazard rates ([LIT-2949](../literature.d/LIT-2949.md)). If
  both hold, hyperbolic discounting ([THEORY-1117](../theory.d/THEORY-1117.md)) is what a hierarchy of
  time scales looks like from one of its levels. Low priority: speculative
  until read.
---
<!-- inactive-ok-file: THEORY-2141 THEORY-2131 CLAIM-769 — Proposed, Unfetched or new; filed in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-780 CLAIM-777 LIT-2954 LIT-2949 — Proposed or Deferred; filed in this contribution or the ones it builds on -->

# LEAD-200: Check whether a hierarchy of time scales, seen from one level, decays hyperbolically rather than exponentially: whether relaxation summed over the levels of an ultrametric tree gives a power law, and whether hyperbolic discounting is exponential discounting averaged over a spread of hazard rates, which would tie Ainslie's account of will to the time geometry of a hierarchy

## Steps

1. **Formal.** On [CLAIM-780](../claims.d/CLAIM-780.md)'s designed hierarchy (rates g^level,
   branching b), compute the probability of still being in the starting
   block at time t. Check whether it falls as a power of t, with exponent
   set by log b / log(1/g), rather than exponentially. Cheap: a script.
2. **Reading.** Ogielski and Stein ([LIT-2954](../literature.d/LIT-2954.md)) for the ultrametric
   result; Sozou ([LIT-2949](../literature.d/LIT-2949.md)) for the discounting one.
3. **Then.** If both hold, a dated note on [THEORY-1117](../theory.d/THEORY-1117.md) (Ainslie) and a claim
   that hyperbolic discounting is what an agent whose relevant hazards span
   a hierarchy of time scales would show. [CLAIM-777](../claims.d/CLAIM-777.md)'s queue already
   gives a hyperbola-shaped mean, E[a^W] = r/(r + ln(1/a)), from an
   exponential averaged over an exponential wait; that is the same
   mechanism in one level.

## Note of 2026-11-21: done

Step 1: the assistant's check (curation entry of 2026-11-21) found the return probability on designed rate trees decaying as a power of time with exponent ln b/ln(1/(bg)), not the ln b/ln(1/g) this lead first guessed. Step 2: Ogielski and Stein and Sozou were Unfetched; their neighbours were read. Bachas and Huberman ([THEORY-2141](../theory.d/THEORY-2141.md)) give the same exponent, ln b/(ln(1/g) − ln b), with conditions (gb < 1; finite trees end exponentially); Fedus and colleagues ([THEORY-2131](../theory.d/THEORY-2131.md)) restate Sozou, an exponential prior over hazards giving exactly 1/(1 + kt). Step 3: [CLAIM-769](../claims.d/CLAIM-769.md), and a dated note on [THEORY-1117](../theory.d/THEORY-1117.md).
