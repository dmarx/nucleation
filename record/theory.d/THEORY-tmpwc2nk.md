---
status: Proposed
promote_when: >-
  A checked re-derivation recorded in this file of Theorems 2.1.2 and 2.5.1,
  which the reading made (NOTE-tmpxufhw), together with a complete proof of
  Theorem 2.4.24's conjugation step (the volume-preserving transformation
  of the interior replicator flow), from the paper's sources or another,
  read and checked. It is refuted by a finite game in which some
  asymptotically stable sink chain component of the replicator flow
  contains no sink strongly connected component of the weakly
  better-response graph, or by one MCC meeting two chain components. The
  title says nothing about the limit of the stationary distribution as α
  grows, nor about invariance to copies. Results on those neither promote
  nor refute it.
title: "The α-Rank chain over pure strategy profiles, built from Fermi-imitation fixation probabilities in finite populations with rare mutation, has a unique stationary distribution at every finite ranking intensity; as the intensity grows without bound its transitions become those of Markov chains confined to the sink strongly connected components of the game's weakly-better-response graph, each of which lies inside a single chain component of the replicator flow"
version: 1
tags:
- game-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-tmpkx8qe
summary: >-
  Omidshafiei et al. (2019), LIT-tmpkx8qe, Theorems 2.1.2, 2.4.24 and 2.5.1,
  read from arXiv v4 in NOTE-tmpxufhw, proofs followed. Irreducibility is
  immediate, and the α → ∞ limit is of transition matrices. The link to
  the replicator flow rests on a volume-preservation step that is asserted,
  not carried out. Not shown: what the stationary distribution tends to,
  how it splits among several sinks, or invariance to duplicated
  strategies, which the reader found it lacks.
---
<!-- inactive-ok-file: NOTE-tmpxufhw — the reading this is filed from -->
<!-- inactive-ok-file: CLAIM-tmpuxcp6 THEORY-896 — Proposed; named in prose, nothing here rests on them -->

# THEORY-tmpwc2nk: The α-Rank chain over pure strategy profiles, built from Fermi-imitation fixation probabilities in finite populations with rare mutation, has a unique stationary distribution at every finite ranking intensity; as the intensity grows without bound its transitions become those of Markov chains confined to the sink strongly connected components of the game's weakly-better-response graph, each of which lies inside a single chain component of the replicator flow

## Source

Omidshafiei, Papadimitriou, Piliouras, Tuyls, Rowland, Lespiau, Czarnecki,
Lanctot, Pérolat & Munos, LIT-tmpkx8qe, read in NOTE-tmpxufhw from
arXiv:1903.01373v4: eqs. 2–10 (pp. 6–7), Theorem 2.1.2 (p. 8, proof
pp. 42–43), Definition 2.4.23 and Theorem 2.4.24 (p. 14, proof p. 44),
Theorem 2.5.1 (p. 15, proof p. 45).

## What was actually shown

- **Uniqueness.** Every fixation probability under Fermi imitation with
  finite payoffs is positive. Any profile reaches any other by changing one
  population at a time, so the chain is irreducible, with a unique
  stationary distribution.
- **The limit of the transitions.** For payoff advantage Δ > 0, the
  fixation probability (1 − e^{−αΔ})/(1 − e^{−mαΔ}) tends to 1. For Δ < 0
  it tends to 0, and for Δ = 0 it is 1/m. So at α = ∞ the chain moves only
  along weakly better deviations, and its closed classes are the sink
  strongly connected components of the response graph, the MCCs. The
  reader re-derived the limits.
- **The link to dynamics.** For the replicator flow, an asymptotically
  stable set must meet the boundary, since the interior flow preserves
  volume after a conjugation. Inductively it contains a vertex, and so the
  whole set reachable from it by weakly better replies, an MCC. Each MCC
  is chain transitive, so it lies in one chain component.

What could have come out otherwise: a sink of the better-response graph
could have straddled two chain components, or an attracting component
could have avoided the pure profiles altogether.

## What this does not say

- **That α-Rank's ranking has a limit, or which.** At α = ∞ the chain is
  reducible whenever there are several MCCs, as the authors say. At large
  finite α the split among sinks depends on payoff differences and m, and
  no result characterizes it.
- **That every MCC is in an asymptotically stable component.** Only the
  converse is proved.
- **That the ranking resists padding.** In the symmetric
  single-population model, duplicating scissors in rock-paper-scissors
  moves rock to first place at every α tried (NOTE-tmpxufhw).
- **That its masses are evolutionary strength in a population-dependent
  sense.** The single-population fitness is local: payoff against the one
  opponent met, regardless of the population's composition.

## Connections

The discrete form of its Conley reading is the condensation of a win
digraph, acyclic and so always carrying an ordinal potential, with MCCs as
its sinks. That bears on how TERM-077 and CLAIM-tmpuxcp6 treat cyclic
records. In a game with THEORY-896's finite improvement property and no payoff
ties, every MCC is a single profile, a pure equilibrium (NOTE-tmpxufhw).
