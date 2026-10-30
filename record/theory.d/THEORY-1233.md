---
number: 1233
status: Proposed
formerly:
- THEORY-tmp9386m
title: 'For the replicator flow of a finite game, every asymptotically stable sink chain component contains at least one sink strongly connected component of the weakly-better-response graph, a Markov-Conley chain'
version: 1
tags:
- game-theory
- complex-systems
date: '2026-10-30'
source:
- LIT-1516
extends:
- THEORY-942
promote_when: >-
  A checked re-derivation recorded in this file of Theorems 2.1.2 and
  2.5.1, which the reading made (NOTE-1156), together with a complete
  proof of Theorem 2.4.24's conjugation step (the volume-preserving
  transformation of the interior replicator flow), from the paper's
  sources or another, read and checked. It is refuted by a finite game in
  which some asymptotically stable sink chain component of the replicator
  flow contains no sink strongly connected component of the weakly
  better-response graph, or by one MCC meeting two chain components. The
  title says nothing about the limit of the stationary distribution as α
  grows, nor about invariance to copies. Results on those neither promote
  nor refute it.
summary: >-
  The half of Omidshafiei et al.'s Theorem 2.4.24 that [THEORY-942](THEORY-942.md) does not
  assert, kept here when the twenty-fourth status review promoted
  [THEORY-942](THEORY-942.md) on the other half ([ADR-047](../decisions.d/ADR-047.md), kind 1). The paper's proof
  conjugates the interior flow to a volume-preserving one, and then
  argues inductively that an attractor reaches a vertex. [NOTE-1156](../notes.d/NOTE-1156.md) found
  that step asserted, not carried out.
---

# THEORY-1233: For the replicator flow of a finite game, every asymptotically stable sink chain component contains at least one sink strongly connected component of the weakly-better-response graph, a Markov-Conley chain

## Source

Omidshafiei et al., [LIT-1516](../literature.d/LIT-1516.md), read in [NOTE-1156](../notes.d/NOTE-1156.md) from arXiv v4: Theorem
2.4.24 (p. 14, proof p. 44).

## What is shown and what is not

The paper argues this. The interior replicator flow preserves volume
after a change of coordinates, so an asymptotically stable set must meet
the boundary. Inductively it contains a vertex, and then the set of
profiles reachable from that vertex by weakly better replies, which is an
MCC. The change of coordinates is easy. In log-ratio coordinates the
interior field has divergence 0, since no population's payoff
differences depend on its own mix, and a script at the status review of
2026-10-30 confirmed it. What is not carried out is the induction: that
the trace of an attractor on a face is again an attractor there, and that
the vertex's weakly-better closure is pulled in. [THEORY-942](THEORY-942.md) holds the
other half, that each MCC lies inside one chain component, re-derived. The
converse of this entry, that every MCC lies in an asymptotically stable
component, is false: in matching pennies the whole square is one
component ([NOTE-1156](../notes.d/NOTE-1156.md)).
