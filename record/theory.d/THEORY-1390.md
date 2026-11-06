---
number: 1390
status: Active
formerly:
- THEORY-tmpeo94c
title: "Hopkins (2010) holds that all freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, that only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and that where linear actuators must act to drive the permitted motions without parasitic error is computed from a stiffness matrix that carries each flexure's location, orientation, geometry and material"
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    At the twenty-ninth status review, at the status review's ruling (the
    owner delegated these rulings; ADR-065), on NOTE-1596 v2: promoted
    Proposed → Active, and promote_when deleted. Narrowed (kind 3): the
    third clause said placement "is set by the flexures' stiffness and not
    by the freedom space alone"; the thesis states the dependence on
    stiffness (§4.2.1), and the contrast with the freedom space is the
    record's inference, held by CLAIM-589. The old title was "Hopkins (2010) holds that all freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, that only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and that where linear actuators must act to drive the permitted motions without parasitic error is set by the flexures' stiffness and not by the freedom space alone". The
    old promote_when asked for an independent screw-system classification
    and a second experiment, which the attribution does not need; it moves
    word for word to the new THEORY that extends this one and states the
    theses without attribution (ADR-047 kind 1). It read: "An independent
    screw-system classification confirms the 50 freedom/constraint space
    types and the boundary between those parallel flexures can realise and
    those that need modules stacked in series, and a second experiment or
    an independent model confirms that, for a fixed freedom space, where
    linear actuators must act to drive the permitted motions without
    parasitic error shifts with the flexures' stiffness as the
    twist–wrench stiffness matrix predicts."
tags:
- natural-sciences
- control-theory
- mathematics
date: '2026-11-05'
source:
- LIT-2042
summary: >-
  Hopkins (2010), [LIT-2042](../literature.d/LIT-2042.md), read in [NOTE-1596](../notes.d/NOTE-1596.md) (every argument chapter and
  every passage stating the title's clauses; the type-by-type catalogue of
  ch. 3 and most of Appendix A's case list not read). Active as a report of
  what the thesis holds. Whether the 50 types are complete and whether the
  actuation theory holds beyond the one experiment stay with the extending
  THEORY. It is quasi-static and small-motion, and says nothing about
  actuating serial systems. Not peer reviewed.
---
# THEORY-1390: Hopkins (2010) holds that all freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, that only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and that where linear actuators must act to drive the permitted motions without parasitic error is computed from a stiffness matrix that carries each flexure's location, orientation, geometry and material

## Source

Hopkins, *Design of Flexure-based Motion Stages for Mechatronic Systems
via Freedom, Actuation and Constraint Topologies (FACT)*, MIT Ph.D.
thesis (2010), [LIT-2042](../literature.d/LIT-2042.md); read in [NOTE-1596](../notes.d/NOTE-1596.md).

## What was actually shown

- **The count (§2.1, p. 29).** "There are only 50 freedom and constraint
  space pairs called types.", once twists and wrenches of every pitch are
  allowed; described in ch. 3 (1, 3, 10 and 22 in the 0–3 DOF columns) and
  by symmetry in §3.5 (10, 3, 1), derived in Appendix A.
- **The boundary (§2.1, p. 30).** "Parallel flexure systems may only
  possess freedom spaces that lie within the parallel pyramid." Three pure
  translations are "only possible for a serial flexure system" (§1.1.1,
  p. 18).
- **The actuation space is computed from stiffness (§4.2.1; eq. 4.11
  carries E, G, I₁, I₂, J, A, l).** It is computed from the
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
- That the 50-type enumeration is complete: Appendix A's case analysis
  defers to the master's thesis for the 2-DOF column and the symmetry, and
  was not checked here (see the THEORY that extends this one).
- That the freedom space alone does not fix actuator placement: the
  thesis implies it but does not say it; [CLAIM-589](../claims.d/CLAIM-589.md) does.
