---
status: Proposed
promote_when: >-
  A first-hand reading of an experiment, by the same or another
  laboratory, in which the founding cell's intracellular iron (or a second,
  chromosomal reporter of Fur activity) is measured directly in single
  E. coli cells and its lineages are sampled at every generation, showing
  that descendants share the founder's swarming class for a few
  generations and then relax to the population distribution, with the
  relaxation following the iron variable. Refuted if, with iron measured
  directly, swarming potential is shown to be inherited independently of
  it, or if sibling homogeneity at four generations does not replicate.
  What would not settle it: further correlations with the same plasmid
  reporter; refits of the switching model to the same two time points;
  and demonstrations of bistable switches, which are a different mechanism.
title: 'In genetically identical E. coli, a cell''s swarming potential is a transient inherited state: its descendants share it for about four generations and lose it by about seven, and it tracks the cell''s iron status rather than a bistable switch'
version: 1
tags:
- natural-sciences
- complex-systems
date: '2026-10-09'
source:
- LIT-tmpns8pq
summary: >-
  Bhattacharyya et al. (2023), [LIT-tmpns8pq](../literature.d/LIT-tmpns8pq.md). Single-cell swarm assays show
  sibling homogeneity in swarming at four generations and its loss by
  seven, a correlation (Spearman r = 0.71) between a Fur-repressed reporter
  and swarming, and longer persistence when iron is clamped. The iron link
  is read through a promoter reporter and is correlational, the
  inheritance rests on few founders and three time points, and the
  paper's "memory", "conditioning" and "decision-making" are functional
  labels, not evidence of learning.
---

# THEORY-tmpq45k7: In genetically identical E. coli, a cell's swarming potential is a transient inherited state: its descendants share it for about four generations and lose it by about seven, and it tracks the cell's iron status rather than a bistable switch

## Source

Bhattacharyya, Bhattarai, Pfannenstiel, Wilkins, Singh and Harshey (2023),
[LIT-tmpns8pq](../literature.d/LIT-tmpns8pq.md), read in [NOTE-tmpwvklq](../notes.d/NOTE-tmpwvklq.md).

## What was actually shown

- **Inheritance.** Single planktonic E. coli MG1655 cells, isolated by
  dilution to extinction, give swarms whose diameters vary more than those
  from 100- or 10,000-cell inocula. The single-cell daughters of one
  mother, harvested at a calibrated fourth generation, swarm alike; at the
  seventh, sibling variability returns. Cells taken from a swarm's edge are
  uniform good swarmers and keep it to the fourth generation. This could
  have come out otherwise: siblings could have been as variable as
  unrelated cells at G4.
- **Iron.** Among environmental perturbations and ten plasmid-expressed
  swarming genes, only fepA and fur change the variability. An iron
  chelator makes cells better swarmers and holds that to G7; added iron
  or fepA overexpression makes them worse and holds that to G12. A
  fepA-promoter sfGFP reporter, bright when Fur is derepressed by low iron,
  correlates with sorted single cells' swarm diameter (Spearman
  r = 0.7067, p = 8.66 × 10⁻¹⁶), not in a constitutive-promoter control
  (r = 0.15) or in ΔfepA (r = 0.05). In five sorted mothers, G4 daughters
  follow the mother's reporter level.
- **Not a constant-rate switch.** A three-class switching model (XS, M, L)
  reproduces the lineage fractions when each founding cell keeps its class
  for a fixed delay (τ ≈ 3 generations for XS and M, ≈ 4 for L) and then
  switches at constant rates toward a 52/35/13% steady state. The authors
  rule out bistable and toggle switches and epigenetic inheritance because
  the state lasts only a few generations.

## What this does not say

- **Not that iron has been shown to be the carrier.** Iron is never
  measured. The reporter reads Fur-repressed transcription from a
  multicopy plasmid; the evidence is correlation plus perturbation of the
  iron pathway. "Iron status, as the Fur regulon reports it" is the most
  the evidence supports.
- **Not that bacteria learn, decide or are conditioned.** The paper's
  "memory", "conditioning" and "decision-making" name the persistence of a
  physiological state across divisions. No association between stimulus
  and response is tested, and nothing here supports a claim of cognition
  in bacteria beyond that persistence.
- **Not that the state is an alternative stable state.** It relaxes back to
  the population distribution; persistence for a few generations is what a
  slow variable produces (compare [THEORY-136](THEORY-136.md)).
- **Not a precise timescale.** Only G0, G4, G7 and G12 were sampled, with
  generations inferred from timing, so "four" and "seven" are the time
  points tested. The fixed-delay model has five parameters fitted to two
  time points, and no delay-free fit is reported, so the claim that
  switching is not memoryless is weak.
- **Not that the same state governs biofilm and antibiotic survival across
  generations.** Those correlations were measured in the founding cells
  only. The bet-hedging reading and the generality of the mechanism are the
  authors' conjectures.
