---
number: 1445
status: Active
formerly:
- THEORY-tmpa4har
title: 'Aksel, Navarro, Fong and Douglas report that choosing DNA origami staple breakpoints by a shortest-path search over a weighted graph, scored by an equilibrium free energy summing staple binding, scaffold loop closure and hybridization at 50 °C, raised the gel-measured yield of accurately folded multilayer blocks from 2-6% to 48-61% in four published designs, three of them with unchanged scaffold route and helix layout, with yields correlating with the model''s score'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings), under ADR-065: the title reports what Aksel and colleagues
    measured by gel, and NOTE-1642 reads the version of record and its
    SI Appendix in full. The condition asked for an independent
    reproduction, and it moves unchanged to QUESTION-tmpdtizm, which
    lists it under this entry's code; this entry bears_on it: 'An
    independent group, on DNA origami designs whose scaffold route and
    helix layout are held fixed, reproduces a yield gain of comparable
    size from score-optimized staple breakpoints alone, measured by a
    quantified method beyond gel mobility (counted TEM or AFM particles)
    with replicates, and finds yields ordered by the equilibrium score.'
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2125
bears_on:
- QUESTION-tmpdtizm
summary: >-
  Aksel, Navarro, Fong and Douglas (2024), [LIT-2125](../literature.d/LIT-2125.md), read in
  [NOTE-1642](../notes.d/NOTE-1642.md). The yields are integrated gel intensity in a
  hand-bounded window after one 21 h anneal, with no stated replicates and
  TEM only of the redesigns; the correlation is R² = 0.86 over 8 designs
  from the same four structures. The largest gain (10×10, 2 to 61%) also
  changed the scaffold seam and paired fraction. The score is equilibrium
  and ignores folding kinetics and inter-staple cooperativity, so the
  account is one of more stable parts, not of a chosen pathway.
---

# THEORY-1445: Aksel, Navarro, Fong and Douglas report that choosing DNA origami staple breakpoints by a shortest-path search over a weighted graph, scored by an equilibrium free energy summing staple binding, scaffold loop closure and hybridization at 50 °C, raised the gel-measured yield of accurately folded multilayer blocks from 2-6% to 48-61% in four published designs, three of them with unchanged scaffold route and helix layout, with yields correlating with the model's score

## Source

Aksel, Navarro, Fong and Douglas (2024), [LIT-2125](../literature.d/LIT-2125.md); read in
[NOTE-1642](../notes.d/NOTE-1642.md).

## What was actually shown

- **The method**: staple-precursor phosphates as nodes, candidate staples
  of 21-60 nt as edges, weights −ln P_staple from binding, loop-closure and
  hybridization free energies at 50 °C; k = 10 shortest paths per
  precursor, assembled at random into global solutions.
- **Yields** (Fig. 3): 10×10 block from 2 to 61%; 4×16, 8×8 and 16×4
  blocks from 4 to 48%, 3.6 to 56% and 6 to 48%, after one stepped anneal,
  by integrated gel intensity in the redesign's leading window.
- **Held fixed** (SI Figs. S3-S5): for the three 64-helix blocks the
  redesigns "used identical scaffold routes and staple-passivation
  strategies", so only breakpoints differ.
- **Correlation**: yields against the model's score Q_origami, R² = 0.86
  over the 8 designs.
- **Could have come out otherwise**: the redesigns could have folded no
  better than the originals, or yield could have failed to track the
  score.

## What this does not say

- That the gain comes from a different folding pathway: the model ignores
  kinetics, and the authors explain the gain by more stable staples.
- That the 10×10 gain is due to breakpoints alone: its seam, insertion and
  paired fraction also changed.
- That the yields are counts of correct particles: they are gel
  intensities in a window set by hand, with no replicates stated.
- That the gain is 6- to 30-fold as the abstract says: the reported
  numbers give 8 to about 30.
- That raising staple excess above 10:1 would help, or that tuning subset
  concentrations would: both are modelled or proposed, not tested.
