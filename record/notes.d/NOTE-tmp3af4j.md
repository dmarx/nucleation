---
status: Read
paper: 'LIT-tmplwjyi'
title: 'DeLuca et al. — Mechanism of DNA origami folding by mesoscopic simulation'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the publisher's PDF
    (https://www.nature.com/articles/s41467-024-46998-y.pdf), 13 pages,
    CC BY 4.0; text extracted by pdftotext. Read in full: the abstract,
    introduction, all of Results (model, validation, four-helix bundle,
    hybridization enthalpy, scaffold routing, staple design, 32-helix
    bundle), the Discussion, and Methods through the crossover potential.
    Skimmed or skipped: the rest of Methods (integrator, order parameters),
    the Supplementary Information and the Supplementary Movies.
date: '2026-11-05'
summary: >-
  A mesoscopic bead model of DNA, its bending and backbone potentials
  switching with hybridization, simulates whole isothermal folding of DNA
  origami. Small four-helix bundles fold hierarchically, collapsing by a
  cooperative zipping into a locally ordered, globally disordered precursor
  that then crystallizes; a large 32-helix bundle folds slowly and
  variably and is sometimes caught in global topological traps, and early
  coalescence does not predict the final outcome. Simulation only, with no
  misbinding or helical topology.
---
<!-- inactive-ok-file: THEORY-tmpivh27 CLAIM-185 CLAIM-184 CLAIM-478 CLAIM-523 CLAIM-545 LIT-926 LIT-917 — Proposed, Unavailable or new; cited from the reading of DeLuca et al. (2024) as open -->

# NOTE-tmp3af4j: DeLuca et al. — Mechanism of DNA origami folding by mesoscopic simulation

## Contribution

A coarse-grained model that reaches the full folding timescale of DNA
origami while keeping configurational information, not only which
staples are bound; a mechanism for small structures, local order before
global order through collapse into a precursor; and an argument that
kinetic models over hybridization states can mis-predict yield.

## Key insight

Within one hybridization state lie many configurations, and some have no
viable route to the folded structure on experimental timescales. Folding
success depends on the path through configuration space, which the
hybridization count does not record, and an early, persistent intermediate
can be the wrong one.

## Assumptions

- **Resolution**: 8 nucleotides per bead, square lattice only, no
  torsional potentials (so no global twist).
- **Binding**: only designed complements bind, all with one enthalpy
  (default −10 kcal/mol); "for simplicity, we do not allow misbinding to
  occur"; no base stacking between adjacent staples.
- **Conditions**: isothermal at 300 K, no annealing; "Our simulations were
  conducted at a high staple/scaffold concentration (1.6 µM) and at a 1:1
  staple-to-scaffold ratio."
- **Statistics**: ten runs per design.

## Key results

- **Hierarchy (abstract).** The simulations "reveal a hierarchical folding
  process involving zipping into a partially folded precursor followed by
  crystallization into the final structure".
- **Local before global (Results, four-helix bundle).** "This indicates
  that this structure establishes local order before it establishes global
  order"; the zipping may be "a critical event that is required to
  overcome the penalty of constraining the partially assembled scaffold to
  itself".
- **Routing (Discussion).** "routings with many crossovers exhibited linear
  kinetics while the straight-across routing exhibited multiple kinetic
  regimes".
- **Staples (Results).** Long centre staples that bind early collapse the
  structure into a proto rod "irrespective of the folding progress",
  suppressing the two-phase behaviour.
- **Large design (Results, 32-helix bundle).** "faster coalescence into a
  proto form early on is not a perfect predictor of overall folding
  performance"; one run, best folded at 1 s, becomes second worst at 3.6 s,
  "caught in a global topological trap".
- **Contrast (abstract).** "Larger structures are found to exhibit
  heterogeneous staple incorporation kinetics and frequent trapping in
  metastable states", against accessible structures with first-order
  kinetics and "virtually defect-free folding".
- **Yield (Discussion).** Within a hybridization state, some sub-ensembles
  "do not have a viable path to correct folding or have escape times which
  may be very slow"; "kinetic models may thus significantly overpredict
  yield".

## Concepts

- **Switchable force field**: bending and backbone potentials that change
  with local hybridization, so one bead behaves as single strand, double
  strand or crossover.
- **Proto rod**: the collapsed precursor, roughly the final shape but
  swollen, shorter and without global order.
- **Crystallinity**: an order parameter of backbone-tangent alignment;
  local order is the count of unrealized scaffold contacts.
- **Global topological trap**: a configuration, such as scaffold outside
  the core, that severely slows or halts folding.

## Connections

It cites lattice Monte Carlo studies of origami nucleation (Cumberworth,
Frenkel and Reinhardt 2022) and a base-stacking nucleation barrier under
annealing, which its model omits. Its collapse-then-order pathway is
structurally like the two-step nucleation of LIT-926, a link the paper
does not make. LIT-917 is about the same theme of kinetic access deciding
which structure forms.

## Bearing on the record

- **The synthesis's description.** The pasted synthesis on constraint
  architectures cites it as S5 for hierarchical folding and "frequent
  trapping in metastable states" in some designs. Both are the abstract's
  words. Two qualifications.
  - **The trapping is a simulation result, found in the large design.** It
    is reported for the 32-helix bundle over ten runs; the four-helix
    bundles fold virtually defect-free. Nothing here is an experiment.
  - **No nucleation claim.** The paper does not call its mechanism
    nucleation; it uses the word only for others' lattice simulations and
    for a base-stacking barrier its model leaves out. The synthesis's
    "organizational nucleus" is A's notion, and this paper should not be
    cited as a nucleation case.
- **CLAIM-185 (persistent structures as anchors).** Qualifies the anchor
  idea by analogy, not as nucleation: the proto rod is a persistent
  intermediate on which later order grows, but an early, persistent
  structure can be the wrong anchor (the trapped run).
- **CLAIM-184 (anchors entrench).** Supports by physical analogy: early
  coalescence that sets the scaffold wrongly locks the structure out of the
  folded state.
- **CLAIM-079 (stability does not entail viability).** Supports by
  analogy: a trapped 32-helix bundle is long-lived with no viable path to
  the target within the time simulated.
- **CLAIM-478 (scale separation makes constraints).** Loosely supports:
  fast local contact formation then slow global ordering, with local order
  constraining the global.
- **TERM-064, CLAIM-523, CLAIM-545, QUESTION-090, CLAIM-025**: no bearing.
- Filed: THEORY-tmpivh27. No instruction for machine-learning practice.

## Limitations

- **Simulation only**; the authors offer predictions for SAXS,
  fluorescence and AFM.
- **No misbinding, helical topology, base stacking or global twist**: "Since
  our model does not contain the helical nature of hybridization, these
  types of folding defects cannot be captured with this model."
- **Isothermal**, at high concentration and 1:1 stoichiometry; ten runs per
  design; simplified designs.
- **Deterministic proximity criterion** for hybridization, which the
  authors say a probabilistic one would improve.
