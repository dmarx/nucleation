---
number: 387
status: Proposed
formerly:
- CASE-tmp17zl1
title: 'Remote clock frequency differences estimated over satellite links and checked against a simultaneous optical-fibre comparison and a second, independent satellite technique'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-164 as a delegated
    lead worker, from Riedel et al. (LIT-3144, NOTE-2371).
standing: documented
kind: reported-study
tags:
- natural-sciences
- philosophy-of-science
date: '2026-11-22'
line:
- distributed-agency
reported_in:
- LIT-3144
- NOTE-2371
illustrates:
- CLAIM-510
summary: >-
  From Riedel et al. (2020): four European institutes compare their
  clocks for 26 days through local masers and two satellite links at
  once, TWSTFT (signal exchange over a geostationary satellite) and GPS
  PPP. Each link estimates the frequency difference of each remote clock
  pair. The two estimates agree within their uncertainties, and for
  LNE-SYRTE and PTB both agree with an optical-fibre comparison of the
  same clocks, one run at the same time. A measured correspondence between
  remote local standards is checked against evidence that the measurement
  producing it did not produce: [CLAIM-510](../claims.d/CLAIM-510.md)'s own clock example, in practice.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-510 — Proposed; the claim this case illustrates and whose condition it is offered to meet -->
<!-- inactive-ok-file: NOTE-2371 THEORY-2281 — new; the reading this case is taken from -->

# CASE-387: Remote clock frequency differences estimated over satellite links and checked against a simultaneous optical-fibre comparison and a second, independent satellite technique

## The case

Riedel et al. ([LIT-3144](../literature.d/LIT-3144.md), [NOTE-2371](../notes.d/NOTE-2371.md), [THEORY-2281](../theory.d/THEORY-2281.md)) ran
a 26-day campaign of five optical clocks and six fountains at INRIM,
LNE-SYRTE, NPL and PTB.

- **The local descriptions.** Each institute's clocks, read against its
  own hydrogen maser.
- **The correspondence.** The relative frequency difference between two
  remote clocks, after each clock's gravitational redshift is corrected.
- **The measurement.** A satellite link between the masers. TWSTFT
  exchanges coded signals both ways over a satellite, which cancels the
  transit times (p. 4); GPS PPP uses the navigation signals. Each gives
  its own estimate of every pair's difference.
- **The checks.** The two techniques against each other ("compatible
  within a confidence level of 68 %", p. 11); and, for LNE-SYRTE and PTB,
  both against an optical-fibre comparison of the same clocks, the
  strontium one "carried out simultaneously with our measurement campaign"
  (p. 12), the fountain one from a fibre comparison reported separately
  (their ref. [16], p. 13).

The estimate from one channel is held against channels with other paths,
other hardware and other error models, which took no part in producing it.

## What it can show

- That a measured correspondence can be checked against evidence the
  measurement did not produce, in a working practice where the
  independence is the practitioners' and not a modeller's stipulation.
  This is [CLAIM-510](../claims.d/CLAIM-510.md)'s example of clock offsets estimated by signal
  exchange and checked against a reference that took no part, with the
  reference a second channel to the same remote clock rather than a
  co-located clock.
- That such a check can locate a fault. The NPL strontium pairs were
  offset "independent of the link technique" (p. 12), which pointed to the
  clock and not the links; NPL later found a systematic shift in it.

## What it cannot show

- That the check presupposes no correspondence. Each channel has its own
  calibrated delays, and all share the clocks and one geodetic redshift
  correction; the check tests the links against each other, not the
  shared terms.
- That agreement certifies more than the stated uncertainty budgets allow;
  the budgets were not read.
- Anything for adaptive apparatuses: no correspondence is revised here.
