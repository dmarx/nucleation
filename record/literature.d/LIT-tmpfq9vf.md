---
status: Active
status_note: >-
  read 2026-10-31 ([NOTE-tmp3di1n](../notes.d/NOTE-tmp3di1n.md); appendices skimmed); worth reading
  for the bounds a fixed driving places on every stationary state of
  any reaction network ([THEORY-tmph5hkv](../theory.d/THEORY-tmph5hkv.md)). The exchange's A13 also cited
  it for organizations that end when their driving is exhausted; the
  paper's chemostats are fixed, and that point is [LIT-tmpgm18n](LIT-tmpgm18n.md)'s.
title: 'Thermodynamic Space of Chemical Reaction Networks'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A13 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2024-07-16; journal_ref PRX 16, 041026 (2026), doi
    10.1103/g875-ldn5). The summary follows the abstract and the
    exchange's description; a reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read from the arXiv preprint 2407.11498v4, 25 pp., main text in full
    and appendices skimmed, in NOTE-tmp3di1n; status Deferred → Active.
    The citation stands. The summary is rewritten from the text. The
    registration's "Why this is here" attributed to it, after A13, a
    point about finite lifetimes that it does not make; corrected
    below. The reading produced THEORY-tmph5hkv.
tags:
- thermodynamics
date: '2026-10-31'
published: '2024-07-16'
arxiv: '2407.11498'
doi: '10.1103/g875-ldn5'
first_author: 'Liang'
keywords:
- 'chemical reaction networks'
- 'thermodynamic bounds'
- 'affinity'
implementations: []
summary: >-
  Liang, De Los Rios & Busiello (2024; PRX 2026). For any open
  mass-action reaction network at stationarity, each reaction's affinity
  is bounded by the extremal cycle affinities, per use, over the
  elementary flux modes containing it, and each product of
  concentrations by the effective equilibrium constants of the extremal
  pathways; a virtual, infinitely slow probe reaction extends the bounds
  to species no reaction connects. This thermodynamic space has zero
  width at equilibrium. Bistability, chiral symmetry breaking,
  self-assembly yield and pattern contrast lie inside it; a measured
  state outside it falsifies a proposed topology. Fixed chemostats and
  stationary states only.
---

# LIT-tmpfq9vf: Thermodynamic Space of Chemical Reaction Networks

Liang, S., De Los Rios, P., & Busiello, D. M. (2026). Thermodynamic space of chemical reaction networks. *Physical Review X*, 16, 041026.

Read in [NOTE-tmp3di1n](../notes.d/NOTE-tmp3di1n.md).

## Why this is here

A13 used it for the intersection of the dynamically viable region with what thermodynamic driving permits, and the paper supplies exactly that ([THEORY-tmph5hkv](../theory.d/THEORY-tmph5hkv.md)): no stationary state, for any kinetics, lies outside a region set by topology and driving, and the region is a point at equilibrium. A13 also used it for "an organization endogenously maintained relative to its own organization can still have a finite lifetime because its driving is exhausted". The paper does not show that: its chemostats are fixed and it treats only stationary states. The finite-lifetime point is Remlein, Esposito and Avanzini's ([LIT-tmpgm18n](LIT-tmpgm18n.md)). For [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) rewritten as chemistry, every fixed point lies between the floor set by the waste and the ceiling set by the fuel ([NOTE-tmp3di1n](../notes.d/NOTE-tmp3di1n.md)).
