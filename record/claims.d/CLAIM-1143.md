---
number: 1143
status: Proposed
formerly:
- CLAIM-tmpnl4xk
title: 'A witness never certifies the common mode'
statement: >-
  An independent physical witness certifies every difference among the
  channels that read it and never their common mode: if k channels each read
  the same placed points with an offset of their own, their reports identify
  every difference between offsets and leave one shift of all offsets and
  points together unidentified, however many channels there are; so the
  regress of anchors ends at a witness only together with a standard fixed
  by definition, which is how measurement ends it, and an error every
  channel shares stays invisible
version: 1
role: counter
warrant: demonstrated
defeated_if: An error in the rank computation; or a channel to a physical
  phenomenon that reports an absolute value without any convention fixing
  its zero or unit. As a reading of measurement, defeated by a calibration
  chain that ends at no defined standard.
tags:
- philosophy-of-science
- mathematics
- epistemology
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
objects_to:
- CLAIM-1146
rests_on:
- CLAIM-1125
complements:
- CLAIM-510
- CLAIM-011
summary: 'The assistant''s qualification of the owner''s point that mechanics
  has an independent witness ([CLAIM-1146](CLAIM-1146.md)). Checked in scratch/formal/beacon_gauge_check.py:
  with 1, 2, 3 or 5 channels, exactly the two dimensions of a common shift
  stay unidentified. The metrology is cited from standard knowledge, not from
  a reading the record holds. The wording is the assistant''s (Claude, in
  this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CASE-387 CLAIM-510 — Proposed; cited in this filing of 2026-11-23 -->

# CLAIM-1143: A witness never certifies the common mode

## The computation

Let k channels each read points z_t placed by the world, reporting
r_kt = z_t + d_k. The unknowns are the points and the offsets, and the
reports are linear in them. The common shift (z_t + u, d_k − u) leaves
every report unchanged, so it is unidentified. Everything else is
identified: in `scratch/formal/beacon_gauge_check.py` the rank deficiency
is exactly 2, the plane's two directions, for 1, 2, 3 and 5 channels. More
channels identify more differences d_i − d_j, but never the common mode.
The same holds with a different gain A_k on each channel, since
(z + u, d_k − A_k u) is again a symmetry ([CLAIM-1125](CLAIM-1125.md)).

## What it means for the owner's point

The owner is right that the world is a witness no revision can rewrite.
What the witness gives through comparison is agreement and disagreement
among channels, which is a great deal. Independent techniques that agree
are strong evidence. The record's own case is [LEAD-164](../leads.d/LEAD-164.md)'s clocks:
frequency differences estimated by satellite, checked against a
simultaneous optical fibre and a second, independent satellite technique
([CASE-387](../cases.d/CASE-387.md), [CLAIM-510](CLAIM-510.md)). But no amount of agreement fixes the frame.

Measurement ends the regress in two steps:
- **A standard fixed by definition against an invariant phenomenon.**
  Units are defined by fixing the numerical values of physical constants.
- **Traceability.** An unbroken chain of calibrations runs to a
  realization of that standard.

(Cited from standard knowledge of metrology, not from a reading the record
holds.) The definition plays the survey's part in [CLAIM-1185](CLAIM-1185.md). It is
chosen to be stable because the phenomenon is invariant, and it is not
revised by what it calibrates.

## What stays invisible

An error every channel shares is the common mode. Agreement among
channels cannot expose it, for example an assumption of the theory each
instrument's reading relies on. Exposing it takes a channel that does not
share it. Independence of technique lowers the chance of a shared error,
but it does not make one observable.

## Note of 2026-11-23: what holds it back

The rank computation is reproduced (scratch/formal/beacon_gauge_check.py),
but the title's clause that a standard fixed by definition 'is how
measurement ends' the regress rests on no reading the record holds; a read
source on the SI's defined constants and traceability, or a narrowing that
drops the clause to a Proposed interpretive claim, would free it.
