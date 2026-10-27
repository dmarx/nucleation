---
number: 234
status: Open
formerly:
- QUESTION-tmpszev1
title: 'Do interchange interventions leave the mediating direction underdetermined in trained networks: do two basis-related alignments in a trained model tie on every interchange drawn from the data, and for which networks are alignments that agree on all such interventions unique up to a stated symmetry?'
version: 3
history:
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: two works read on 2026-10-26 for the exchange
    "Experimental Infrastructure Review" bear on the choice of units: a
    theory that fixes them by the data's symmetries in an idealized
    transformer, and a benchmark whose scoring cannot see ties. Neither
    answers the question, which is unchanged.
- version: 3
  date: '2026-10-27'
  note: >-
    A dated note added: four facts about instruments from the
    circuits works read on 2026-10-26, none a trained-network tie of
    the kind asked for, and a neighbouring question about
    dictionaries filed as QUESTION-tmpidxeb. The question is
    unchanged.
tags:
- causality
- philosophy-of-science
- representation-learning
date: '2026-10-20'
line: learned-structure
summary: >-
  Filed when the promotion audit (batch 062, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-243](../theory.d/THEORY-243.md) to what the constructed three-unit network proves:
  two basis-related alignments tie on every interchange intervention on
  the input. Whether such ties occur in trained networks, or are ruled
  out for some class up to a symmetry, was the old promote_when, and it
  moves here.
answered_by:
- THEORY-802
---
<!-- inactive-ok-file: THEORY-802 — Proposed; the answer this question is set beside, cited for its dated note, not leaned on -->

# QUESTION-234: Do interchange interventions leave the mediating direction underdetermined in trained networks: do two basis-related alignments in a trained model tie on every interchange drawn from the data, and for which networks are alignments that agree on all such interventions unique up to a stated symmetry?

## Why it is a question

[THEORY-243](../theory.d/THEORY-243.md) now states an existence result. In the identity network
x ↦ x(1, 0, 1) ↦ (0, 2, 1)·h, aligning the input with the third unit and
aligning it with (h₁ + h₂)/√2 pass every interchange intervention on the
input equally (Makelov et al., [LIT-968](../literature.d/LIT-968.md); Wu et al., [LIT-961](../literature.d/LIT-961.md)). So
interventions on that variable alone do not fix which direction mediates
it. The general reading, that the mediating direction is fixed only
relative to a chosen decomposition into units, needs more than one
constructed case.

An answer is one of the following:

- **A trained-network tie.** In a trained network, two alignments of
  the same high-level variable that differ by a change of basis crossing
  component boundaries and agree on every interchange intervention drawn
  from the data distribution. Then a showing of what, if anything,
  separates them.
- **A uniqueness bound.** A proof that, for a stated class of networks
  and high-level models, alignments that agree on all such interventions
  for every aligned variable are unique up to a stated symmetry.

Further cases where one alignment scores higher than another cannot
settle it, since the question is about ties under a fixed set of
interventions.

## Note of 2026-10-26: units fixed by symmetry, and a benchmark that cannot see ties

Two works read on 2026-10-26 for T24 of the exchange "Experimental
Infrastructure Review" ([QUESTION-tmpivbso](QUESTION-tmpivbso.md)) bear on which decomposition
into units fixes a mediating direction.

- **Units fixed by the data's symmetries** ([THEORY-tmpdxhxm](../theory.d/THEORY-tmpdxhxm.md)). Musat,
  Pimentel, Zucchet and Hofmann compute, for attention-only transformers
  on block-list inductive tasks with fixed orthogonal write maps, the
  subspace of weights the data's symmetry group fixes, and gradient
  descent never leaves it. Its basis of elementary token and position
  actions is a decomposition chosen neither by convention (Wu et al.'s
  reading, [THEORY-802](../theory.d/THEORY-802.md)) nor by privileging the network's components
  (Makelov et al.'s), but by the task's symmetry group. It is not an
  answer of either kind this question names: it says nothing about
  interchange interventions, and it holds only inside the idealization.
  It suggests where a uniqueness bound might be sought, for networks
  whose training the data's symmetries confine.
- **A benchmark that scores one alignment at a time** ([THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)).
  MIB's causal-variable track ranks localization methods by mean
  interchange-intervention accuracy, alignment by alignment. A tie
  between two basis-related alignments would show as two equal scores
  and is never looked for. Its winning method, distributed alignment
  search, is trained against the causal model it is scored on.

The question is unchanged.

## Note of 2026-10-27: ties by construction, not ties found

The core circuits works, read on 2026-10-26 at the owner's request, add
four facts about the instruments. None is a trained-network tie of the
kind the question asks for.

- **DAS fixes subspaces, not directions.** In Geiger et al.'s Definition
  3 (LIT-tmpsavwt) the rotation enters an intervention only through the
  projector onto the learned subspace, so rotations that select the same
  subspaces give identical interventions. DAS alignments are therefore
  unique at most up to rotations within the learned subspaces: a stated
  symmetry, but of the instrument, not of networks. The observation is
  the record's (NOTE-tmpzb21n), not the paper's.
- **Causal scrubbing ties by construction** basis-related hypotheses
  that induce the same partitions of the data (THEORY-tmpblgxz). So does
  any method that scores nodes by their effect on one metric under one
  family of contrasts, sparse feature circuits among them
  (NOTE-tmpr0gdc).
- **The basis changes the verdict.** DAS's toy and its trained-network
  results (THEORY-tmpgqlal) are THEORY-243's converse: a learned rotation
  passes where the neuron basis fails.
- **A wide search can manufacture alignment.** On frozen random networks
  DAS's IIA rises above chance once the layer is wide (THEORY-tmpqhbjf),
  so a tie found by a supervised search in a wide layer would need that
  control.

The source of the basis freedom in transformers, the residual stream's
lack of a privileged basis, is stated in Elhage et al.'s framework
(LIT-tmp9dono; THEORY-802's note of 2026-10-27). The neighbouring
question, whether two dictionaries of equal fidelity give the same
validated circuit, is filed as QUESTION-tmpidxeb. The question is
unchanged.
