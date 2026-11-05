---
number: 1398
status: Proposed
formerly:
- THEORY-tmpivh27
promote_when: >-
  An experiment (time-resolved SAXS, fluorescence or arrested AFM) or an
  independent simulation shows, in an accessible origami design, a collapse
  into a locally ordered, globally disordered precursor before global
  ordering, and, in a large interior-heavy design, trapped products with
  defective interiors whose early folding progress does not predict the
  final outcome.
title: 'In mesoscopic simulation, DNA origami folds hierarchically: accessible structures collapse into a locally ordered precursor that then crystallizes, while larger structures with interior geometry are often caught in global topological traps that early progress does not predict'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
source:
- LIT-2081
summary: >-
  DeLuca, Duke, Ye, Poirier, Ke, Castro and Arya (2024), [LIT-2081](../literature.d/LIT-2081.md),
  read in [NOTE-1561](../notes.d/NOTE-1561.md). A simulation result, ten runs per design, in a
  model without misbinding, helical topology, base stacking or annealing.
  It does not say that real origami traps this way, nor that the
  precursor is a nucleus: the paper does not use the word for its
  mechanism.
---
<!-- inactive-ok-file: NOTE-tmpwxm2p — Proposed, new or Skimmed; cited from the assistant's reading across the DNA origami readings -->

# THEORY-1398: In mesoscopic simulation, DNA origami folds hierarchically: accessible structures collapse into a locally ordered precursor that then crystallizes, while larger structures with interior geometry are often caught in global topological traps that early progress does not predict

## Source

DeLuca, Duke, Ye, Poirier, Ke, Castro and Arya (2024), [LIT-2081](../literature.d/LIT-2081.md); read
in [NOTE-1561](../notes.d/NOTE-1561.md).

## What was actually shown

- **Four-helix bundle**: averaged over ten runs, two first-order regimes;
  staples bridge the scaffold, a cooperative zipping collapses it into a
  proto rod, and crystallinity grows afterwards, so local order comes
  before global.
- **Design dependence**: routing with many crossovers gives one rate and
  no zipping; early-binding long staples collapse the structure regardless
  of progress.
- **32-helix bundle**: progressively slower kinetics, a spread of over 150
  unrealized contacts at 5 s across runs, unfolded interiors in some, and a
  run best folded at 1 s that ends second worst in a global topological
  trap.

## What this does not say

- That experiments show this pathway: they are proposed, not done.
- That trapping is general: it is found in the large interior-heavy design;
  the small ones fold virtually defect-free.
- That folding proceeds by nucleation: the model omits the base-stacking
  barrier the authors associate with nucleation under annealing.
- Anything about defects from misbinding or helical topology, which the
  model cannot represent.

## Note of 2026-11-05: the DNA origami readings, read across

The assistant's reading across the eight DNA origami readings filed on the owner's request to connect the record's inquiry to DNA origami. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

Two experimental and modelling readings bear on the theory. Dunn and colleagues ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md)), in experiment and a kinetic model, find that early long-range seams decide the fold and can trap it "effectively, irreversibly", which corroborates DeLuca et al.'s finding that early global contacts set the outcome. Sobczak's dissertation ([NOTE-tmpwxm2p](../notes.d/NOTE-tmpwxm2p.md), read in part) attributes slow folding at low temperature to a system that "gets lost in a sea of easily accessible incorrect states", spurious short bindings rather than global topological traps; the two accounts can both hold in different designs, so this is a note, not a rivalry. Schneider, Möritz and Dietz ([NOTE-tmpqi66a](../notes.d/NOTE-tmpqi66a.md)) see a compacted intermediate before the folded state, consistent with the theory's precursor, by gel only.

No status changes.
