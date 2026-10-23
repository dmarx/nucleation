---
status: Answered
title: 'In two optically trapped beads with a symmetric hydrodynamic coupling and a recorded noise drive on one trap, do directional information measures between the beads follow the symmetry of the coupling?'
version: 1
tags:
- information-theory
- causality
- natural-sciences
date: '2026-10-23'
line: distributed-agency
refines:
- QUESTION-063
answered_by:
- THEORY-275
summary: >-
  The negative part of [QUESTION-063](QUESTION-063.md), split off under [ADR-049](../decisions.d/ADR-049.md) at the
  owner's request in the exchange of 2026-10-23, "Framework Overview
  Request", and answered by [THEORY-275](../theory.d/THEORY-275.md). No: in the one system [LIT-947](../literature.d/LIT-947.md)
  studied, time-delayed mutual information and transfer entropy follow the
  path of the recorded drive, not the symmetry of the coupling. Whether
  any measurement or intervention tells shared drive from coupling, and
  what happens under an unrecorded drive shared by both units, stay with
  [QUESTION-063](QUESTION-063.md).
---

# QUESTION-tmpasghi: In two optically trapped beads with a symmetric hydrodynamic coupling and a recorded noise drive on one trap, do directional information measures between the beads follow the symmetry of the coupling?

## Answer

No, for this system. [THEORY-275](../theory.d/THEORY-275.md) (Active), from Das, Manikandan and
Banerjee ([LIT-947](../literature.d/LIT-947.md), read in [NOTE-788](../notes.d/NOTE-788.md)): two colloids coupled through a
symmetric hydrodynamic tensor, with recorded noise moving one trap.
Time-delayed mutual information and transfer entropy run drive → driven →
other, with backflow at moderate drive, in experiment and in numerics. In
numerics of the fitted model only, the flow reads one-way under strong
drive. So a directional measure can report a hierarchy where the coupling
is reciprocal.

The answer is a counterexample, which [ADR-049](../decisions.d/ADR-049.md) counts as an answer to a
question of the form "must X?". It is not a theorem about directional
measures in general; that generalization is the record's own claim,
[CLAIM-396](../claims.d/CLAIM-396.md) (Proposed), and its test in a second system is [QUESTION-186](QUESTION-186.md).

## What stays with [QUESTION-063](QUESTION-063.md)

[QUESTION-063](QUESTION-063.md) asks what measurement or intervention tells shared drive,
coupling among members and distinct internal routes apart. [THEORY-275](../theory.d/THEORY-275.md)
removes one candidate for the observational case and says nothing of the
rest: the drive here is recorded and on one unit, while [QUESTION-063](QUESTION-063.md)'s
case is an unrecorded drive that may be shared. [THEORY-129](../theory.d/THEORY-129.md) and [THEORY-130](../theory.d/THEORY-130.md)
keep their partial answers to the parent.

## Why it is a split

[THEORY-275](../theory.d/THEORY-275.md) answered [QUESTION-063](QUESTION-063.md) "in part, negatively", as the parent's
body already said. Under [ADR-049](../decisions.d/ADR-049.md) a partly answered question is split: the
answered part is filed as a child worded to exactly what the Active entry
settles, and the answering entry's `answers` link moves to it. The owner
asked for the splits in the exchange of 2026-10-23 (U9: "can we split any
QUESTIONs into an answered part and an unanswered refinement?").
