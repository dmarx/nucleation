---
status: Proposed
promote_when: >-
  A controlled sweep, for one architecture and objective and without a
  shared stable start, in which only a measured property of the data
  varies (graph density, feature separability or homophily; or client
  heterogeneity under federated averaging with an IID control), with
  barriers reported as numbers over several seeds. The account is
  supported if the linear barrier moves monotonically with the measured
  property, and refuted if barriers stay flat as it varies or move with
  the architecture instead. Correlations read off plots, and bounds whose
  proofs are missing or whose assumptions conflict, cannot settle it.
title: "Without a shared stable start, the linear barrier between solutions of one objective depends on the structure of the training data: between GCNs it falls with graph density and feature separability and is highest at middling homophily, and between federated-averaging models it grows with client heterogeneity and falls with width"
version: 1
tags:
- loss-landscapes
- network-science
- anthology-candidate
date: '2026-10-16'
source:
- LIT-676
- LIT-666
answers:
- QUESTION-069
summary: >-
  Li et al. (2025), [LIT-676](../literature.d/LIT-676.md), read in [NOTE-529](../notes.d/NOTE-529.md): on synthetic CSBM graphs the
  barrier between GCNs from different seeds falls with density and feature
  separability and peaks at middling homophily; GCN, GraphSAGE and GAT
  barriers are similar, an MLP's differ. Zhou, Zhang & Tsang (2023),
  [LIT-666](../literature.d/LIT-666.md), read in [NOTE-517](../notes.d/NOTE-517.md): FedAvg global models from one random start
  under more heterogeneous clients are separated by a larger line barrier,
  joined by a one-bend chain, and the barrier falls with width. Both
  readings named this account and held it back. The GNN proofs are
  missing and its barriers are plots; the federated bound treats
  heterogeneity as isotropic noise, and its lemma and theorem conditions
  conflict as written.
---
<!-- inactive-ok-file: LIT-676 — Proposed; one of the two readings this account rests on, which is why it is Proposed -->
<!-- inactive-ok-file: THEORY-109 THEORY-115 THEORY-tmpjgtxb — Proposed; neighbouring connectivity accounts named in Connections, not leaned on -->

# THEORY-tmpxxllh: Without a shared stable start, the linear barrier between solutions of one objective depends on the structure of the training data: between GCNs it falls with graph density and feature separability and is highest at middling homophily, and between federated-averaging models it grows with client heterogeneity and falls with width

## Source

- Li, Chen, Han, Zeng, Liu & Tang (2025), [LIT-676](../literature.d/LIT-676.md), read in full in
  [NOTE-529](../notes.d/NOTE-529.md): Observations 3–4, Figs. 4–5.
- Zhou, Zhang & Tsang (2023), [LIT-666](../literature.d/LIT-666.md), read in full in [NOTE-517](../notes.d/NOTE-517.md): §§IV–VII,
  Figs. 5–9, Theorems 1–2.

Both readings name this as a candidate account and hold it back as not
yet filed ([NOTE-529](../notes.d/NOTE-529.md) and [NOTE-517](../notes.d/NOTE-517.md), Bearing on the record).

## What was actually shown

**Graphs ([LIT-676](../literature.d/LIT-676.md)).** On contextual stochastic block model graphs, with two
Gaussian feature classes and in-class and out-class edge probabilities,
the linear barrier between GCNs trained from different seeds falls as
density and feature separability rise, and is highest at middling
homophily, with strongly homophilous and strongly heterophilous graphs
better connected (Observation 4, Fig. 5). On a given graph, GCN, GraphSAGE
and GAT give similar barriers while an MLP on the same features differs
markedly (Observation 3, Fig. 4). Graphs from similar domains give similar
interpolation curves (Observation 2).

**Federated averaging ([LIT-666](../literature.d/LIT-666.md)).** Ten clients, Dirichlet label skew with
α ∈ {0.1, 0.2, 0.5}. FedAvg global models from one initialisation, trained
under different heterogeneity, disagree on more than 20% of inputs, show a
line barrier with an accuracy drop of about 10% that is larger for
(0.1, 0.2) than for (0.1, 0.5) and grows over rounds, and are joined by a
one-bend polygonal chain without barrier (Figs. 5–7). In a two-layer
mean-field model with heterogeneity as Gaussian noise of variance βh(α) on
each neuron's update, two global models are ε_C-connected by a 7-segment
path with ε_C ∝ √h(α)((√log N + z)/√N + …) (Theorem 2). In MNIST runs the
line barrier falls with width from N = 200 to N = 6400 (Fig. 9).

**What could have come out otherwise.** Barriers could have tracked the
architecture rather than the data, or stayed flat as heterogeneity rose.
In both settings they moved with the data.

## What this does not say

- **That data structure is the only thing that sets the barrier.** The
  federated models also differ in random start and training history; no
  IID control is reported.
- **That the bounds hold.** [LIT-676](../literature.d/LIT-676.md)'s barrier bound (through the spectral
  gap), its generalisation bound and its graph distance cite an appendix
  that holds no proofs, and use undefined constants. [LIT-666](../literature.d/LIT-666.md)'s Lemma 1
  requires h(α) ≤ C₅ and Theorem 1, which uses it, states h(α) ≥ C₅; its
  theory is for two-layer networks, squared loss and one-pass data, its
  experiments for VGG11 and cross-entropy.
- **That the CSBM results cover heterophily as defined.** The paper's
  homophily definition requires p_in > p_out, so h > ½, yet heterophilous
  results are reported ([NOTE-529](../notes.d/NOTE-529.md)).
- **That the real graphs match the synthetic trend.** The "match" is
  asserted, and the real-graph barriers are given only as plots.

## Connections

- **[THEORY-115](THEORY-115.md)** holds that from a shared, already-stable start, linear
  connectivity holds only when the objectives share structure. This
  account is the other side: one objective, no shared stable start, and
  the data's structure moving the barrier. [THEORY-115](THEORY-115.md) already cites both
  papers as limits on its own scope.
- **[THEORY-tmpjgtxb](THEORY-tmpjgtxb.md)** takes [LIT-676](../literature.d/LIT-676.md)'s result that the curved path removes
  the barrier.
- **[THEORY-109](THEORY-109.md).** [LIT-666](../literature.d/LIT-666.md)'s Theorem 2 applies Kuditipudi et al.'s route,
  dropout stability implies a short low-loss path ([LIT-671](../literature.d/LIT-671.md)), with
  heterogeneity worsening the stability.
- **[QUESTION-069](../questions.d/QUESTION-069.md)** asks whether connectedness is a property of the
  solutions or of the regime they were trained in. On this account the
  data are part of the regime.
