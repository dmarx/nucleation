---
number: 57
status: Skimmed
formerly:
- NOTE-tmphmt18
paper: LIT-091
title: 'Networks beyond pairwise interactions (review)'
version: 1
date: '2026-09-25'
summary: >-
  Many systems' interactions happen in groups rather than pairs. Representing them explicitly, as hypergraphs or simplicial complexes, changes both the measured structure and the dynamics, and in particular adds new non-linearities and abrupt (explosive) transitions that pairwise models miss.
---

<!-- inactive-ok-file: LIT-091 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-057: Networks beyond pairwise interactions (review)

## Contribution

The review argues that in social contact, chemical reactions, ecology and elsewhere, interactions involve three or more units and cannot be reduced to dyads. It surveys the new field of networks with higher-order interactions. It first relates the frameworks used to represent them, then covers structural measures and generative models (random and growing simplicial complexes, bipartite graphs, hypergraphs). It then turns to dynamics: diffusion, synchronization, spreading, opinion dynamics and evolutionary games on higher-order structures, followed by applications and open problems.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Representations (§II): low- vs. high-order and graph-based vs. explicit representations (hypergraphs, simplicial complexes, bipartite graphs, motifs), and the relations among them.
- Measures and models (§III–IV): incidence and adjacency tensors, higher-order centralities and clustering, simplicial homology and persistent homology, hypergraph and combinatorial Laplacians. Equilibrium and out-of-equilibrium models (bipartite, stochastic set, hypergraph, simplicial).
- Dynamics (§V–VIII): higher-order random walks; higher-order Kuramoto and phase-reduction models, where group interactions produce abrupt or explosive (de)synchronization; spreading and opinion models on simplicial complexes and hypergraphs; multiplayer games.
- Applications (§IX): social systems, neuroscience and brain networks, ecology, other biology.
- Outlook (§X): higher-order interactions add non-linearities absent from pairwise models. Open problems include genuinely higher-order measures (e.g. simplicial closure), temporal and multilayer extensions, and localizing homological features.

## Open questions

- This is the standard reference for higher-order networks, and the natural anchor citation for a network-science note on hypergraphs and simplicial complexes. It is also relevant background for hypergraph and simplicial neural networks, which the review predates.
- Being a 92-page review, it is best read by section on demand rather than end to end.
