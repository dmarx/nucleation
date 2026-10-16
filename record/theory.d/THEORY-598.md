---
number: 598
status: Active
formerly:
- THEORY-tmpodgn4
title: "Group interactions that enter a dynamical model linearly, as in diffusion on simplices or random walks on hypergraphs with edge-independent vertex weights, reduce to pairwise dynamics on a reweighted graph; the abrupt transitions, bistability and stabilised coexistence reported for higher-order systems come from group terms that enter nonlinearly, and whether the representation is a hypergraph or a simplicial complex is itself a modelling claim that changes the outcome"
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-16'
source:
- LIT-091
summary: >-
  Battiston et al. (2020), [LIT-091](../literature.d/LIT-091.md), read in full in [NOTE-057](../notes.d/NOTE-057.md). A review: the
  reduction results are its own §V algebra (three-body linear diffusion
  becomes a weighted graph Laplacian, Eq. 35) and reported results it
  cites (Chitra and Raphael on hypergraph walks); the nonlinear effects are
  one-paper summaries, mostly mean-field or all-to-all. The review never
  states the condition as a result, and its introduction and conclusion
  claim more ("no doubts", "profoundly change"), citing linear cases among
  the examples. The condition is the record's reading of what its body
  shows; edge-dependent vertex weights also escape the reduction.
---

# THEORY-598: Group interactions that enter a dynamical model linearly, as in diffusion on simplices or random walks on hypergraphs with edge-independent vertex weights, reduce to pairwise dynamics on a reweighted graph; the abrupt transitions, bistability and stabilised coexistence reported for higher-order systems come from group terms that enter nonlinearly, and whether the representation is a hypergraph or a simplicial complex is itself a modelling claim that changes the outcome

## Source

Federico Battiston, Giulia Cencetti, Iacopo Iacopini, Vito Latora, Maxime
Lucas, Alice Patania, Jean-Gabriel Young and Giovanni Petri (2020),
"Networks beyond pairwise interactions: Structure and dynamics", *Physics
Reports* 874, 1–92, [LIT-091](../literature.d/LIT-091.md), read in full in [NOTE-057](../notes.d/NOTE-057.md).

## What was actually shown

**Linear group terms reduce.**
- §V (p. 37): "traditional diffusion is a linear process and consequently
  the simplest generalization to higher-order structures can always be
  reduced to equations involving only pairwise couplings". Three-body
  linear diffusion becomes a weighted Laplacian L^△ with
  ℓ^△_ij = δ_ij Σ_k a^△_ijk − Σ_k a^△_ijk (Eq. 35).
- §V B (p. 41): random walks on hypergraphs with edge-independent vertex
  weights are equivalent to walks on a weighted projected graph (Chitra
  and Raphael, reported).
- Near synchrony, identical oscillators with higher-order coupling are
  governed by a weighted pairwise multi-order Laplacian (Lucas et al.,
  Eqs. 49–51).

**Nonlinear group terms do not.** The reported effects all come from
coupling functions in which the group enters nonlinearly:
- triadic Kuramoto, sin(θ_j + θ_k − 2θ_i) (Eq. 43): abrupt
  desynchronisation and an incoherent state stable for all coupling;
- simplicial SIS, where a 2-simplex transmits only when both other members
  are infected (Eq. 58): a discontinuous, bistable transition. [NOTE-057](../notes.d/NOTE-057.md)'s
  mean-field check finds an endemic branch below λ = 1 exactly when
  λ_Δ > 1;
- three-body consensus with an influence function s(|x_j − x_k|)
  (Eq. 61): the mean is conserved only when s is constant;
- replicator dynamics with b_ijk x_j x_k terms, and Grilli et al.'s
  three-seedling competition, where the coexistence point that pairwise
  competition leaves neutral becomes globally stable (Eqs. 67–70).

**The representation matters.** A simplicial complex assumes every
sub-group of an interacting group also interacts; a hypergraph assumes
nothing. The graph projection loses group identity and the clique complex
invents groups (Fig. 1). Simplicial contagion (Eq. 58) and contagion on
d-uniform hypergraphs (Eq. 59) behave differently.

**What could have come out otherwise.** Linear diffusion with group terms
could have had dynamics no weighted graph reproduces. It does not: the
reduction is direct algebra.

## What this does not say

- **That linearity is the only escape.** Walks with edge-dependent vertex
  weights are not time-reversible and cannot be reduced to weighted-graph
  walks, though the walk is still linear.
- **That higher-order structure as such changes dynamics.** That is the
  introduction's and §X's framing (C10, C11). §X's list of "profoundly
  changed" critical behaviour cites an edge-independent hypergraph walk and
  linear simplex diffusion, which §V itself reduces.
- **That the nonlinear effects are general.** Most are mean-field,
  all-to-all or for identical oscillators, and the review says the effect of
  symmetric against asymmetric coupling functions has "not been
  investigated systematically" (p. 47).
- **That group interactions can be detected in data.** The review says no
  inference scheme yet distinguishes a genuine k-body coupling from
  pairwise coupling plus correlations at scale (§X).
- **That the brain is shown to be higher-order.** The review reports the
  neuroscience evidence as mixed.
- **That a pairwise description is more fundamental.** Phase reduction of
  pairwise-coupled nonlinear oscillators produces three- and four-body
  phase terms at second order (C9), so the arrow can run the other way.

## Connections

- **Forman curvature** ([THEORY-502](THEORY-502.md), from [LIT-020](../literature.d/LIT-020.md)). Forman's curvature
  lives on cell complexes and decomposes the Hodge Laplacian this review
  defines; the network version keeps only the 1-skeleton.
- **Spectral and Fiedler dimensions** ([THEORY-576](THEORY-576.md), from [LIT-028](../literature.d/LIT-028.md)). The
  review's spectral dimension is the density-of-states one, which that
  account separates from the gap exponent.
- **Information decomposition** ([LIT-025](../literature.d/LIT-025.md), [LIT-042](../literature.d/LIT-042.md)). The review's O-information
  pointers belong to the same programme of measuring high-order dependence,
  used here only in passing.
