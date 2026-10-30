---
number: 1232
status: Proposed
formerly:
- THEORY-tmp771g4
promote_when: >-
  An analysis of the Friedkin–Johnsen reflected-appraisal map (Eqs. 6, 9
  and 10 of LIT-1404) that finds its fixed points and their stability for
  strongly connected relative weights, showing that the autocratic fixed
  points attract almost every start, or a published simulation by others
  that reproduces the contrast with the DeGroot–Friedkin map on the same
  networks. A larger simulation by this record would not settle it.
title: 'Under reflected appraisal across issues, whether power concentrates in one member depends on the single-issue step: with Friedkin–Johnsen anchoring on initial positions almost every random strongly connected group evolves to a single leader, and with DeGroot consensus the same random complete networks keep power spread'
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-30'
source:
- LIT-1404
- LIT-1146
extends:
- THEORY-1161
summary: >-
  The general contrast, filed beside [THEORY-1161](THEORY-1161.md) by the twenty-fourth
  status review ([ADR-065](../decisions.d/ADR-065.md) §3; [ADR-047](../decisions.d/ADR-047.md) kind 1). [THEORY-1161](THEORY-1161.md), Active, holds
  what Friedkin's simulations showed; whether the anchored step's
  autocratic fixed points attract almost every start, and the DeGroot
  step's do not, is this entry's question. Re-runs on sparse networks of
  density 0.4 gave 93% and 96% single leaders; the DeGroot side rests on
  [THEORY-916](THEORY-916.md), Proposed.
---
<!-- inactive-ok-file: THEORY-916 — Proposed; the DeGroot–Friedkin account the comparison rests on, cited as open -->

# THEORY-1232: Under reflected appraisal across issues, whether power concentrates in one member depends on the single-issue step: with Friedkin–Johnsen anchoring on initial positions almost every random strongly connected group evolves to a single leader, and with DeGroot consensus the same random complete networks keep power spread

## Source

Friedkin (2011/2012), [LIT-1404](../literature.d/LIT-1404.md), read in full in [NOTE-1374](../notes.d/NOTE-1374.md); and Jia,
MirTabatabaei, Friedkin and Bullo (2015), [LIT-1146](../literature.d/LIT-1146.md), read in [NOTE-1135](../notes.d/NOTE-1135.md), whose
result is [THEORY-916](THEORY-916.md).

## Where the evidence stands

What Friedkin's simulations showed is [THEORY-1161](THEORY-1161.md), Active, which this entry
extends. Neither paper compares the two single-issue steps; the comparison is
the record's re-run, set out with its script in [THEORY-1161](THEORY-1161.md)'s note of
2026-10-30. On random complete networks the anchored step gave a single leader
every time and the DeGroot step a median largest self-weight of about 0.27 and
0.13; on strongly connected networks of density 0.4 the anchored step gave a
single leader in 93% and 96% of runs, which sits against "almost every". Jia
et al.'s theorem for the DeGroot step is [THEORY-916](THEORY-916.md), Proposed, its proofs not
yet checked. The `promote_when` above is [THEORY-1161](THEORY-1161.md)'s condition before the twenty-fourth status review promoted it, carried here unchanged, because it asks what would make the thesis true and not what the source says.
