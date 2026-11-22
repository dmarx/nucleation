---
number: 2014
status: Proposed
formerly:
- THEORY-tmp8my3p
title: 'Gili and colleagues infer, for a literature-based eleven-region language connectome, the subnetworks whose coarsest balanced colourings equal the group-average fMRI synchrony clusters at rest (four fibres) and in two speech tasks (five, one partition for both); the inferred networks have only the identity automorphism and their rest and task partitions cross, so the reported fibration symmetry breaking is a change of balanced partition imposed by the observed clusters, not predicted from structure'
version: 1
source:
- LIT-2804
tags:
- neuroscience
- network-science
date: '2026-11-19'
bears_on:
- QUESTION-218
- QUESTION-125
- QUESTION-063
corroborates:
- CLAIM-405
promote_when: >-
  A replication from the released code and data showing that the resting
  and task partitions are reachable by edge removals alone while most
  random partitions with the same block sizes are not, or an independent
  cohort in which the clusters are predicted from a structural network
  fixed before the fMRI is analysed.
summary: >-
  Gili, Avila, Pasquini, Holodny, Phillips, Boldi, Gabrielli, Caldarelli,
  Zimmer and Makse ([LIT-2804](../literature.d/LIT-2804.md)), read in [NOTE-2111](../notes.d/NOTE-2111.md). A
  mixed-integer program deletes the fewest tracts from a baseline
  connectome (five fibres, each an orbit) until each state's observed
  synchrony clusters are its coarsest balanced colouring. Rest gives four
  fibres, both tasks five, all with only the identity automorphism, and
  the rest and task partitions are not ordered by refinement. The account
  applies [THEORY-1065](THEORY-1065.md): synchrony classes without symmetry. It goes past
  that theorem in calling an invariant partition "proven to be
  synchronous", and it predicts no partition.
---

# THEORY-2014: Gili and colleagues infer, for a literature-based eleven-region language connectome, the subnetworks whose coarsest balanced colourings equal the group-average fMRI synchrony clusters at rest (four fibres) and in two speech tasks (five, one partition for both); the inferred networks have only the identity automorphism and their rest and task partitions cross, so the reported fibration symmetry breaking is a change of balanced partition imposed by the observed clusters, not predicted from structure

## The account

Gili and colleagues ([LIT-2804](../literature.d/LIT-2804.md)) take an eleven-region dorsal-stream
language network and a baseline connectome assembled from the tract
literature. Its five fibres coincide with its five orbits. For each brain
state they find the group-average phase-locking clusters, then delete the
fewest edges so that those clusters become the coarsest balanced
colouring of what is left. At rest that gives four fibres; in verb
generation and phonemic fluency, the same five. Both inferred networks
have only the identity automorphism. The authors call baseline-to-rest
group symmetry breaking with more fibration symmetry, and rest-to-task
fibration symmetry breaking, "analogous to symmetry breaking in
ferromagnets".

## What it rests on

The balanced-colouring theorem the record holds as [THEORY-1065](THEORY-1065.md), applied
in reverse: the theorem says which partitions any admissible dynamics
leaves invariant, and the paper asks which network would make an observed
partition one of them.

## What it does not show

- That the inferred networks are anatomical: the paper itself says they
  are idealized.
- That the clusters were predicted: they are the program's input. The
  genuine outputs are that a removal-only solution exists and that the
  automorphisms are lost.
- That any fibre attracts. [THEORY-1065](THEORY-1065.md) gives invariance only, and no
  stability test is run.
- That the transitions are moves within one lattice of balanced
  equivalence relations ([LIT-2249](../literature.d/LIT-2249.md)): each state's partition belongs to a
  different inferred graph.

## Bearing

It corroborates [CLAIM-405](../claims.d/CLAIM-405.md)'s crossing boundaries: one system's partitions
under two conditions cross, Broca's area splitting between them. The
criterion is the same in both states, so it does not show two criteria
picking crossing units. It bears on [QUESTION-218](../questions.d/QUESTION-218.md), since structural fibres
are units without internal coupling, though the pipeline assumes that the
functional block and the fibre coincide. It bears on [QUESTION-125](../questions.d/QUESTION-125.md) and
[QUESTION-063](../questions.d/QUESTION-063.md) as a natural case in which a partition changes with state
under a shared task drive.
