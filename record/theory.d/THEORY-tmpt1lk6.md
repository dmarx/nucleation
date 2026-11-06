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
title: "All freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and where linear actuators must act to drive the permitted motions without parasitic error is set by the flexures' stiffness and not by the freedom space alone"
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Filed at the twenty-ninth status review, at the status review's ruling
    (the owner delegated these rulings; ADR-047 kind 1, ADR-065): the wider
    thesis THEORY-1390 reported, split off when THEORY-1390 was narrowed to
    what Hopkins (2010) holds and promoted. It keeps THEORY-1390 v1's
    wording, without the attribution, and its promote_when word for word.
tags:
- natural-sciences
- control-theory
- mathematics
date: '2026-11-06'
source:
- LIT-2042
extends:
- THEORY-1390
summary: >-
  What Hopkins (2010) holds ([THEORY-1390](THEORY-1390.md)), stated as true. The thesis
  offers its chart as "a comprehensive classification of screw systems"
  (§2.1), derives it by a case analysis (Appendix A) that defers to the
  master's thesis for the 2-DOF column and the column symmetry, and does
  not compare it type by type with Gibson and Hunt's or Rico and Duffy's
  classifications. The actuation theory has one bench experiment, whose
  measured errors were much larger than predicted, and the thesis states
  that placement is computed from stiffness without saying that the
  freedom space alone leaves it open. Proposed until an independent
  classification and a second test exist.
---

# THEORY-tmpt1lk6: All freedom–constraint space pairs of a flexure-guided rigid body fall into 50 types, only those whose constraint space holds enough pure-force lines can be realised by parallel flexures while the rest need modules stacked in series, and where linear actuators must act to drive the permitted motions without parasitic error is set by the flexures' stiffness and not by the freedom space alone

## Source

Hopkins, *Design of Flexure-based Motion Stages for Mechatronic Systems
via Freedom, Actuation and Constraint Topologies (FACT)*, MIT Ph.D.
thesis (2010), [LIT-2042](../literature.d/LIT-2042.md); read in [NOTE-1596](../notes.d/NOTE-1596.md). The attributed report is
[THEORY-1390](THEORY-1390.md).

## What would settle it

An independent classification of screw systems for flexures that recovers
the 50 types and the parallel pyramid's boundary, and a second experiment
or independent model in which, for one freedom space, the least-error
actuator line moves with the flexures' stiffness as the twist–wrench
stiffness matrix predicts.

## Where it stands

- **The count** rests on chapter 3 (the 0–3 DOF columns), §3.5 (the 4–6 DOF
  columns by symmetry, proved in the master's thesis, [LIT-2031](../literature.d/LIT-2031.md)) and
  Appendix A, which gives "the logic ... that was used to consider every
  way twists could be combined to generate all possible freedom spaces".
- **The boundary** is the thesis's usefulness criterion: a freedom space of
  n DOFs needs 6 − n independent pure-force wrenches in its constraint
  space (§2.1).
- **Actuation**: one stage, one actuator line varied; the least error came
  about 17.5 cm below the probe tip against 20 cm predicted, with errors
  much larger than predicted (§4.7).
