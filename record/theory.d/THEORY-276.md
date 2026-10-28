---
number: 276
status: Active
formerly:
- THEORY-tmpov2tm
title: "In a network of identical units with identical couplings, the orbits of the graph's symmetry group are synchronization clusters, and a cluster moved only by its own factor of the group can lose synchrony while the others keep it"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-276.yaml,
    batch 013, ADR-047). The title is a statement about invariant sets, and
    is re-derived below by the fixed-point-subspace argument, which makes
    the hypothesis for isolated desynchronization explicit: the factor that
    moves the cluster moves nothing else. The promote_when asked for a
    second experiment testing which clusters are seen and when, which is
    the stability question the title leaves to the dynamics. It moves
    unchanged to QUESTION-147. The claim is unchanged.
tags:
- network-science
- complex-systems
- mathematics
date: '2026-10-14'
source:
- LIT-960
summary: >-
  Pecora et al. (2014), [LIT-960](../literature.d/LIT-960.md), read in [NOTE-775](../notes.d/NOTE-775.md): eq. (1), the IRR
  block-diagonalization (eqs. 2–4, 7), the derivation of isolated
  desynchronization (eq. 6) and an 11-node electro-optic experiment. The
  pattern of clusters that can synchronize is read from the wiring;
  whether each does is set by the dynamics through its own transverse
  block. Symmetry is sufficient, not necessary, for clusters. The paper
  says nothing about external drive, so the use of these clusters as a
  sign of coupling rather than a shared cue is the record's inference.
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-157 — Proposed; the coupling and boundary claims this account bears on, open -->
<!-- inactive-ok-file: QUESTION-147 — Open; the second-system test moved out of this account's promote_when, named as open -->

# THEORY-276: In a network of identical units with identical couplings, the orbits of the graph's symmetry group are synchronization clusters, and a cluster moved only by its own factor of the group can lose synchrony while the others keep it

## Source

Pecora, Sorrentino, Hagerstrom, Murphy and Roy (2014), *Nature
Communications* 5:4079, [LIT-960](../literature.d/LIT-960.md), read in full in [NOTE-775](../notes.d/NOTE-775.md) (the
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
- **[QUESTION-147](../questions.d/QUESTION-147.md).** Whether the stability predictions hold in a
  second system of near-identical units: the condition this account's
  promote_when carried until 2026-10-19.

## Note of 2026-10-19: the invariance, derived directly

Let π be a graph automorphism, so A_{π(i)π(j)} = Aᵢⱼ, and let P permute
node states, (Px)ᵢ = x_{π(i)}. Write f for the right-hand side of eq. (1).

- **Equivariance.** f(Px)ᵢ = F(x_{π(i)}) + σ Σⱼ Aᵢⱼ H(x_{π(j)}) =
  F(x_{π(i)}) + σ Σⱼ A_{π(i)π(j)} H(x_{π(j)}) = (Pf(x))ᵢ.
- **Fixed-point subspaces are invariant.** For any subgroup Σ of the
  automorphism group, let Fix(Σ) be the states with Px = x for every
  π ∈ Σ. If x ∈ Fix(Σ), then f(x) = f(Px) = Pf(x), so the vector field is
  tangent to Fix(Σ), and by uniqueness a trajectory that starts there
  stays there.
- **Clusters.** Fix(G), for the whole group G, is the set of states equal
  on every orbit. So orbit-wise synchrony is invariant.
- **Isolated desynchronization.** Let G = H_m × K, where H_m moves only the
  nodes of C_m and K, the product of the other factors, fixes C_m
  pointwise. For a node i outside C_m, H_m fixes i, so G·i = K·i. The
  K-orbits are the G-orbits outside C_m and singletons inside it. Fix(K) is
  then the set of states synchronized on every other cluster with C_m
  free, and it is invariant. If H_m also moved another cluster, the two
  would be intertwined, and they lose synchrony together, as the paper
  says.

Whether these states are stable is the separate question the transverse
IRR blocks answer. The title claims only possibility, and the 11-node
experiment exhibits the stable case.

## Note of 2026-10-27 (evening): the readings of the U15–U23 works

Stewart, Golubitsky and Pivato ([NOTE-1217](../notes.d/NOTE-1217.md); [THEORY-1065](THEORY-1065.md)) generalize this
reading's result. The orbit partitions of a symmetry group are balanced, so
orbit clusters are a special case of their Thm 6.5. That theorem covers
non-additive coupling, several cell and arrow types, and clusters with "input
and output couplings match … but there is no symmetry" (Figures 3 and 19).
Necessity holds only over the whole class of admissible dynamics, and
stability, the other half of this reading, is not treated. Torres-Hugas et
al. ([NOTE-1218](../notes.d/NOTE-1218.md)) give a further instance. In a seven-node motif with two
commuting reflections, the pentagonal block loses transverse stability first
while the triangular mode stays stable.
