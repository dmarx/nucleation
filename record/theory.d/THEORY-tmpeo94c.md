---
status: Proposed
promote_when: >-
  An independent screw-system classification confirms the 50
  freedom/constraint space types and the boundary between those parallel
  flexures can realise and those that need modules stacked in series, and
  a second experiment or an independent model confirms that, for a fixed
  freedom space, where linear actuators must act to drive the permitted
  motions without parasitic error shifts with the flexures' stiffness as
  the twist–wrench stiffness matrix predicts.
title: 'Hopkins (2010) holds that all freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, that only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and that where linear actuators must act to drive the permitted motions without parasitic error is set by the flexures'' stiffness and not by the freedom space alone'
version: 1
tags:
- natural-sciences
- control-theory
- mathematics
date: '2026-11-05'
source:
- LIT-tmp9cusv
summary: >-
  Hopkins (2010), LIT-tmp9cusv, read in part in NOTE-tmpnscd2 (chs. 1, 2.1–2.2,
  4.1–4.4, 4.7 and 5; the type catalogue, ch. 3, and the stiffness-matrix
  derivation, §§4.5–4.6, were not read). Proposed: the 50-type count rests
  on a catalogue and appendix not read, the thesis is not peer reviewed,
  and the actuation result has one experiment behind it, which located
  the least-error actuator line near the prediction while measuring
  errors much larger than predicted. It is quasi-static and small-motion,
  and says nothing about actuating serial systems.
---
<!-- inactive-ok-file: NOTE-tmpnscd2 — Skimmed and new; the reading this account comes from, cited as open -->

# THEORY-tmpeo94c: Hopkins (2010) holds that all freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, that only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and that where linear actuators must act to drive the permitted motions without parasitic error is set by the flexures' stiffness and not by the freedom space alone

## Source

Hopkins, *Design of Flexure-based Motion Stages for Mechatronic Systems
via Freedom, Actuation and Constraint Topologies (FACT)*, MIT Ph.D.
thesis (2010), LIT-tmp9cusv; read in NOTE-tmpnscd2.

## What was actually shown

- **The count (§2.1, p. 29).** "There are only 50 freedom and constraint
  space pairs called types.", once twists and wrenches of every pitch are
  allowed.
- **The boundary (§2.1, p. 30).** "Parallel flexure systems may only
  possess freedom spaces that lie within the parallel pyramid." Three pure
  translations are "only possible for a serial flexure system" (§1.1.1,
  p. 18).
- **Stiffness sets the actuation space (§4.2).** It is computed from the
  twist–wrench stiffness matrix, which holds "the orientation, location,
  geometry and material properties of each flexible constraint"; a system
  whose actuation space is not among the 26 "cannot be actuated with
  linear actuators alone" (§4.3.2, p. 122).
- **One test (§4.7, p. 134).** The least parasitic error came with the
  actuator about 17.5 cm below the probe tip, against 20 cm predicted.

## What this does not say

- That kinematically equivalent designs perform alike. The thesis says the
  opposite: their "elastomechanics, dynamics, and manufacturability may be
  altered" (§2.2.4, p. 36).
- Anything about large motions, dynamic actuation, or actuating serial
  systems, all left as future work.
- That constraints create freedom. Freedoms a parallel system cannot have
  come from stacking bodies in series.
- Anything about control effort in the optimal-control sense; the thesis
  is quasi-static.
- That the 50-type enumeration was checked here.
