---
number: 40
status: Skimmed
formerly:
- NOTE-tmp87h10
paper: LIT-075
title: 'Dreyer et al. 2024, ants vs humans on a piano-movers puzzle'
version: 1
date: '2026-09-25'
summary: >-
  On the same T-shaped load "piano-movers" puzzle, ant groups do better as they get larger, because collective alignment gives them an emergent short-term memory (persistent wall-sliding). Human groups do no better than individuals when they can talk, and worse when communication is restricted, because they fall back on greedy one-shot majority moves.
---

<!-- inactive-ok-file: LIT-075 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-040: Dreyer et al. 2024, ants vs humans on a piano-movers puzzle

## Contribution

Whether collective cognition beats individual cognition is hard to test, because groups and individuals usually face different problems. Carrying a large load through a cluttered space is an exception that both people and ants handle alone and in groups. The authors gave the same scaled piano-movers puzzle to single ants, small and large ant groups (longhorn crazy ants), and to single people and groups of people with and without communication. Larger ant groups outperform smaller ones through emergent memory stored in their ordered collective state. Individual humans plan in a reduced state space and beat ants on average, but restricted-communication human groups choose greedy moves and perform worse.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Setup ("One Puzzle, a Variety of Solvers", Fig. 1): a T-shaped load has to cross three chambers joined by narrow slits. Configuration space is (x, y, r_av·θ), normalized by slit width. The states a to h form a graph with a known optimal path.
- Performance (Fig. 2): humans beat ants on average in normalized path length, though the best ant solvers beat the worst humans. Large ant groups beat small groups.
- Ants (Fig. 3): large carried loads keep speed and direction when they hit a wall and slide along it persistently, while small groups lose speed and re-orient. The authors read this as short-term memory held in the collective ordered state, "analogous to ordered spins". Agent-based simulations with informed pullers, uninformed pullers and lifters reproduce the behaviour.
- Humans ("Human Solvers", Fig. 4): individuals treat the states as a mental graph, take shortest paths between nodes, and prune dead edges using long-term memory. Restricted-communication groups start moving within about 1 s and are fitted by a one-shot majority-vote model with a single greediness parameter p. The authors link this to groupthink and pluralistic ignorance. Communicating groups deliberate for tens of seconds, behave like "follow a random member", and only marginally beat their average member (escaping dead-end state b).
- Discussion: ant simplicity and uniform rules make cooperation easy and scalable. Human cognitive flexibility produces interpersonal variation that needs richer communication to aggregate. The authors frame this as two evolutionary routes for allocating cognition between individual and collective, with implications for cooperative robotics.

## Open questions

- A clean empirical case that group performance depends on how heterogeneous the members are and on communication bandwidth, not only on group size. It is relevant to multi-agent and ensemble aggregation analogies (majority vote vs. follow-a-leader).
- Check SI Note 10, which claims random-leader choice is strictly better than majority vote when most individual choices are wrong, and check how the greediness parameter p is fitted.
- The comparison between species relies on the restricted-communication condition to match ant-like force-based communication, so check how fair that match is.
