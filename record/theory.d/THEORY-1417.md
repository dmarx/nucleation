---
number: 1417
status: Active
formerly:
- THEORY-tmppn4nt
title: 'Zang, Zhao, Misseroni and Paulino show that prestressing Kresling origami cells with controllable springs tunes each cell''s energy barrier and stability continuously, so that reordering the barriers of cells in an assembly makes folding sequences feasible that the unprestressed assembly cannot follow'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-065: the title reports what one study showed, read
    in NOTE-1569 (the main text in full; the SI, which the title does not
    rest on, unread), and nothing in the record contradicts it. The
    promote_when asked for independent reproduction, which the title does
    not assert, and moves unchanged to QUESTION-405. The old condition:
    An independent experiment or simulation on prestressed multistable
    origami cells reproduces continuous tuning of the energy barrier, and of
    bistability, by prestress, and shows that reordering the barriers of the
    cells in an assembly makes feasible folding sequences that the
    unprestressed assembly cannot follow.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2091
summary: >-
  Zang, Zhao, Misseroni & Paulino (2025), [LIT-2091](../literature.d/LIT-2091.md), read in
  [NOTE-1569](../notes.d/NOTE-1569.md) (the main text; the SI was not read). Held as what one group's
  model and prototypes showed, with three-cell assemblies and a theory that misses
  the panel buckling seen in experiment. The "frustration" is prestress
  applied from outside, stored elastic energy, not an incompatibility
  inside the crease pattern. Of 56 ordered transitions in the three-cell
  stack, prestress opens the 8 blocked by the ordering of the barriers;
  the 16 that need intermediate states stay unachievable.
bears_on:
- QUESTION-405
---

# THEORY-1417: Zang, Zhao, Misseroni and Paulino show that prestressing Kresling origami cells with controllable springs tunes each cell's energy barrier and stability continuously, so that reordering the barriers of cells in an assembly makes folding sequences feasible that the unprestressed assembly cannot follow

## Source

Zang, Zhao, Misseroni & Paulino, "Origami frustration and its influence on
energy landscapes of origami assemblies", PNAS (2025), [LIT-2091](../literature.d/LIT-2091.md); read
in [NOTE-1569](../notes.d/NOTE-1569.md).

## What was actually shown

- **Cells.** Three kinds of spring (axial, torsional, along the mountain
  creases) prestress the cell. In the model and in prototypes the barrier
  moves continuously with the prestress, and "by controlling the level of
  prestress in the negative mode, we can switch the instability behavior
  from bistable to monostable" (Results, Parametric study).
- **Assemblies.** In a three-cell stack, "only thirty-two out of fifty-six
  folding paths are feasible": 16 need intermediate states and 8 are
  blocked by the ordering of the barriers. Prestress "enables the eight
  previously infeasible folding paths of Fig. 4C to be achieved as feasible
  folding paths in Fig. 5B." Four of these were shown experimentally.
- **In place.** Building different cells could open the same paths but
  "inevitably introduces new infeasible folding paths and does not support
  in-situ reconfiguration."

## What this does not say

- That every transition can be opened. The 16 that need intermediate
  states are not opened.
- That the structure frustrates itself. The prestress is supplied and
  adjusted from outside, by springs and a handle.
- That this frustration is incompatibility among demands. It is stored
  elastic energy, the energetic sense the record's term [TERM-060](../terms.d/TERM-060.md) sets
  apart from its own.
- That it scales. The assemblies have three cells, and the theory omits
  the panel buckling seen on loading.
