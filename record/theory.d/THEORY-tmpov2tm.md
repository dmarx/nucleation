---
status: Proposed
promote_when: >-
  An independent experiment or analysis, in a second physical or
  biological system of near-identical units on a known graph, in which
  the synchronized clusters observed are the symmetry orbits computed in
  advance, and a cluster desynchronizes in isolation where its own
  transverse block, and only it, is predicted to lose stability. It is
  refuted, for the stated class, by a stable synchronized pattern that
  splits an orbit without breaking a symmetry, or by an isolated
  desynchronization that the IRR blocks do not predict. What cannot
  settle it: networks with nonidentical units, weighted or directed
  coupling, or clusters from input-equitable partitions without symmetry,
  which are outside the claim.
title: "In a network of identical units with identical couplings, the orbits of the graph's symmetry group are synchronization clusters, and a cluster moved only by its own factor of the group can lose synchrony while the others keep it"
version: 1
tags:
- network-science
- complex-systems
- mathematics
date: '2026-10-14'
source:
- LIT-960
summary: >-
  Pecora et al. (2014), [LIT-960](../literature.d/LIT-960.md), read in [NOTE-tmpagh2p](../notes.d/NOTE-tmpagh2p.md): eq. (1), the IRR
  block-diagonalization (eqs. 2–4, 7), the derivation of isolated
  desynchronization (eq. 6) and an 11-node electro-optic experiment. The
  pattern of clusters that can synchronize is read from the wiring;
  whether each does is set by the dynamics through its own transverse
  block. Symmetry is sufficient, not necessary, for clusters. The paper
  says nothing about external drive, so the use of these clusters as a
  sign of coupling rather than a shared cue is the record's inference.
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-157 — Proposed; the coupling and boundary claims this account bears on, open -->

# THEORY-tmpov2tm: In a network of identical units with identical couplings, the orbits of the graph's symmetry group are synchronization clusters, and a cluster moved only by its own factor of the group can lose synchrony while the others keep it

## Source

Pecora, Sorrentino, Hagerstrom, Murphy and Roy (2014), *Nature
Communications* 5:4079, [LIT-960](../literature.d/LIT-960.md), read in full in [NOTE-tmpagh2p](../notes.d/NOTE-tmpagh2p.md) (the
published article and the arXiv preprint; the Supplementary Information
was not obtained).

## What was actually shown

- **The class.** ẋᵢ = F(xᵢ) + σ Σⱼ Aᵢⱼ H(xⱼ), with identical F and H, and
  A a symmetric 0/1 adjacency matrix (eq. 1). The form is needed only
  near the synchronization manifold.
- **Clusters (a theorem).** Every symmetry R_g of the graph commutes with
  A, so the equations are unchanged when a symmetry permutes the nodes.
  The orbits of the symmetry group are therefore sets of nodes that can
  move identically. Each orbit's synchronous motion is a solution.
- **Stability (a theorem plus computation).**
  - The IRR transformation T makes TAT⁻¹ block-diagonal. One M × M block
    lies in the synchronization manifold, and the transverse blocks are
    one per IRR.
  - A cluster is stable where the maximum Lyapunov exponent of its
    transverse block is negative.
  - Clusters moved by one non-decomposable factor of the group share a
    block. They are "intertwined" and "will always either synchronize
    together or not at all".
- **Isolated desynchronization (a derivation, eq. 6).**
  - Suppose the group is a direct product of commuting factors. A node
    outside cluster C_m is then coupled to every node of C_m with the same
    weight.
  - So it receives the same summed input from C_m whether C_m is
    synchronized or not.
  - The other clusters' synchronous states stay invariant when C_m loses
    synchrony, and if they are also stable, that is isolated
    desynchronization.
- **What could have failed.**
  - In an 11-node electro-optic network with 32 symmetries, the clusters
    were computed before the experiment, and the bifurcations were
    predicted from the simulated transverse MLEs.
  - The experiment, with real heterogeneity and noise, showed the four
    nontrivial clusters synchronize at β = 0.72π. At β = 1.4π the
    four-node cluster split into two pairs while the others held. The two
    intertwined clusters desynchronized together.
  - The experiment could have shown clusters other than the orbits, or
    desynchronizations the blocks did not predict. It did not.
- **How common.**
  - In 10,000 random, Barabási–Albert and bipartite 100-node graphs of
    each kind, almost every graph had several nontrivial clusters and
    several factors.
  - Two power grids also had many symmetries.
  - This is a statement about topology. The authors say stability "will
    depend on the dynamical systems of the network nodes".

## What this does not say

- **It does not say that clusters require symmetry.** The published text
  notes that clusters also arise "where input and output couplings match
  in a cluster, but there is no symmetry". So a synchrony pattern that is
  not a symmetry orbit is not evidence against coupling.
- **It does not cover nonidentical units, weighted or directed
  coupling.** The authors say these "can all be handled in much the same
  way" but that "it is not clear that those more general cases will have
  as many symmetries". None is worked through.
- **It does not say which clusters will be seen.** The graph fixes what
  can synchronize. The node dynamics and parameters fix what does.
- **It says nothing about external drive.** The record registered [LIT-960](../literature.d/LIT-960.md)
  on [QUESTION-063](../questions.d/QUESTION-063.md) as a coupling signature that a shared drive does not
  predict.
  - That is an inference from this theorem, not a claim of the paper.
  - Within the class it is sound. Identical uncoupled units under one
    drive have no graph to give their synchrony a pattern of orbits. So
    synchrony that follows the orbits of a known coupling graph, and
    above all an isolated desynchronization of one orbit, is a mark of
    coupling.
  - It needs the graph known in advance and the units near-identical.
  - It is not the single-member intervention [QUESTION-063](../questions.d/QUESTION-063.md) asks for.
- **It does not say that a synchronized cluster is a unit of any kind.**
  Members of an orbit need not be linked to each other ("remote
  synchronization"). They are in step because they receive equal input,
  not because they entrain each other.

## Connections

No relations are declared.

- **[QUESTION-063](../questions.d/QUESTION-063.md).** It bears on the question as above. It is not an
  answer, because it neither distinguishes drive from coupling by
  measurement nor supplies an intervention design.
- **[CLAIM-172](../claims.d/CLAIM-172.md).** A mutually coupled network yields several synchronized
  sub-collectives, and members of one need not be coupled to each other.
  So synchrony does not mark the boundary of the coupled system, nor
  entrainment among the members in step.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** A cluster that stays synchronized through another's
  desynchronization is invariant because its input is equal, not because
  the coupling across its edge is weak. The near-decomposability test and
  the symmetry test pick out different objects.
