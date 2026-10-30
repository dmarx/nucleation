---
number: 942
status: Active
formerly:
- THEORY-tmpwc2nk
title: "The α-Rank chain over pure strategy profiles, built from Fermi-imitation fixation probabilities in finite populations with rare mutation, has a unique stationary distribution at every finite ranking intensity; as the intensity grows without bound its transition matrix converges to that of a chain that moves only along weakly better unilateral deviations, whose closed classes are the sink strongly connected components of the game's weakly-better-response graph, on each of which it is a Markov-Conley chain, and each of which lies inside a single chain component of the replicator flow"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active at the status review's ruling (the
    owner delegated these rulings), under ADR-065 §5 and §3 and ADR-047's
    "Where a narrowing's dropped claims go". A second checker (the
    twenty-fourth status review) followed Theorems 2.1.2 and 2.5.1 and the
    containment half of Theorem 2.4.24, and checked them by script with
    controls; the steps are in the note of 2026-10-30. The last clause
    needs only chain transitivity along the polytope's edges, not the
    conjugation step. The conjugation serves the converse, that every
    asymptotically stable sink chain component contains an MCC, which the
    title does not assert. That converse, which the source asserts, is kept
    as THEORY-tmp9386m, Proposed, which extends this entry and inherits the
    promote_when (ADR-047, kind 1). The title was narrowed for precision:
    the limit chain also moves out of transient profiles, so it is not
    only chains confined to the sinks. The body's "Only the converse is
    proved" is corrected, since the converse is the half not proved. The
    old title: The α-Rank chain over pure strategy profiles, built from Fermi-imitation fixation probabilities in finite populations with rare mutation, has a unique stationary distribution at every finite ranking intensity; as the intensity grows without bound its transitions become those of Markov chains confined to the sink strongly connected components of the game's weakly-better-response graph, each of which lies inside a single chain component of the replicator flow. The old promote_when: A checked re-derivation recorded in this file of Theorems 2.1.2 and 2.5.1, which the reading made (NOTE-1156), together with a complete proof of Theorem 2.4.24's conjugation step (the volume-preserving transformation of the interior replicator flow), from the paper's sources or another, read and checked. It is refuted by a finite game in which some asymptotically stable sink chain component of the replicator flow contains no sink strongly connected component of the weakly better-response graph, or by one MCC meeting two chain components. The title says nothing about the limit of the stationary distribution as α grows, nor about invariance to copies. Results on those neither promote nor refute it.
tags:
- game-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-1516
summary: >-
  Omidshafiei et al. (2019), LIT-1516, Theorems 2.1.2, 2.4.24 and 2.5.1,
  read from arXiv v4 in NOTE-1156, proofs followed. Irreducibility is
  immediate, and the α → ∞ limit is of transition matrices. That each MCC
  lies in one chain component follows from chain transitivity, re-derived
  and second-checked on 2026-10-30. The converse, that attracting
  components contain MCCs, rests on a conjugation step that is asserted,
  not carried out, and is THEORY-tmp9386m. Not shown: what the stationary
  distribution tends to, how it splits among several sinks, or invariance
  to duplicated strategies, which the reader found it lacks.
---
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-tmp9386m — Proposed; the converse half of Theorem 2.4.24, which extends this entry -->

# THEORY-942: The α-Rank chain over pure strategy profiles, built from Fermi-imitation fixation probabilities in finite populations with rare mutation, has a unique stationary distribution at every finite ranking intensity; as the intensity grows without bound its transition matrix converges to that of a chain that moves only along weakly better unilateral deviations, whose closed classes are the sink strongly connected components of the game's weakly-better-response graph, on each of which it is a Markov-Conley chain, and each of which lies inside a single chain component of the replicator flow

## Source

Omidshafiei, Papadimitriou, Piliouras, Tuyls, Rowland, Lespiau, Czarnecki,
Lanctot, Pérolat & Munos, [LIT-1516](../literature.d/LIT-1516.md), read in [NOTE-1156](../notes.d/NOTE-1156.md) from
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
- **The link to dynamics.** On each edge of the profile polytope, where one
  population mixes two strategies and the rest are pure, the replicator
  flow stays on the edge and runs to the better end, or rests when the
  payoffs tie. So every weakly better reply is reachable by an ε-chain:
  an ε-push onto the edge, or small hops along a line of rest points.
  Within a sink strongly connected component every profile reaches every
  other, so an MCC is chain transitive and lies in one chain component.
  The paper's converse, that every asymptotically stable sink chain
  component contains an MCC, is argued through a volume-preserving
  conjugation of the interior flow. That argument is asserted, not
  carried out, and is THEORY-tmp9386m.

What could have come out otherwise: a sink of the better-response graph
could have straddled two chain components, or an attracting component
could have avoided the pure profiles altogether.

## What this does not say

- **That α-Rank's ranking has a limit, or which.** At α = ∞ the chain is
  reducible whenever there are several MCCs, as the authors say. At large
  finite α the split among sinks depends on payoff differences and m, and
  no result characterizes it.
- **That every MCC is in an asymptotically stable component, or the
  converse.** Neither is proved here. The paper claims the converse, that
  every asymptotically stable sink chain component contains an MCC, and
  that is THEORY-tmp9386m.
- **That the ranking resists padding.** In the symmetric
  single-population model, duplicating scissors in rock-paper-scissors
  moves rock to first place at every α tried ([NOTE-1156](../notes.d/NOTE-1156.md)).
- **That its masses are evolutionary strength in a population-dependent
  sense.** The single-population fitness is local: payoff against the one
  opponent met, regardless of the population's composition.

## Connections

The discrete form of its Conley reading is the condensation of a win
digraph, acyclic and so always carrying an ordinal potential, with MCCs as
its sinks. That bears on how [TERM-077](../terms.d/TERM-077.md) and [CLAIM-451](../claims.d/CLAIM-451.md) treat cyclic
records. In a game with [THEORY-896](THEORY-896.md)'s finite improvement property and no payoff
ties, every MCC is a single profile, a pure equilibrium ([NOTE-1156](../notes.d/NOTE-1156.md)).

## Note of 2026-10-30: the re-derivation, written out

The second check at the status review (ADR-065 §5) followed each step.

1. **Uniqueness.** With finite payoffs, the fixation probability (1 −
e^(−αΔ))/(1 − e^(−mαΔ)), or 1/m at Δ = 0, is positive. So every move that
changes one population's strategy has positive probability η·ρ. Any
profile reaches any other by changing populations one at a time, so the
finite chain is irreducible and its stationary distribution is unique and
positive.

2. **The limit.** As α → ∞ the fixation probability tends to 1 for
Δ > 0. For Δ < 0 it behaves as e^((m−1)αΔ) and tends to 0. At Δ = 0 it is
1/m, which is also the formula's limit as Δ → 0. The transition matrix
converges entrywise to the matrix with η on weakly better strict moves,
η/m on neutral moves and 0 otherwise. A closed class of a finite chain is
a sink strongly connected component of its transition graph, and here
that graph is the weakly-better-response graph. On a sink the limit chain
is the paper's MCC.

3. **Containment in one chain component.** Fix an edge of the polytope:
population p mixes strategies s and s′, and the others are pure. The
payoff difference Δ between s′ and s does not depend on population p's own
mix, so the flow on the edge is ẋ = x(1 − x)Δ. Faces are invariant. For
Δ > 0 the orbit runs from s to s′, so an ε-chain goes from s to s′ by a
push of size ε onto the edge. For Δ = 0 the edge is rest points, so
⌈1/ε⌉ hops of size ε join s and s′. Pure profiles are rest points and so
chain recurrent. In a sink strongly connected component every profile
reaches every other by weakly better moves, so they are pairwise chain
equivalent, and they lie in one chain component. This step does not use
the conjugation.

4. **What the converse would need (THEORY-tmp9386m).** In log-ratio
coordinates u = log(x_{i+1}/x_1) for each population, population p's
payoff differences do not depend on its own coordinates, so the interior
vector field has divergence 0. That is the conjugation the paper
mentions, and it is the easy part. What the paper does not carry out is
the rest. A volume-preserving interior flow has no interior attractor.
An attractor's trace on a face is again an attractor there, so the
induction reaches a vertex. And the vertex's weakly-better closure lies
in the attractor.

A script (numpy, in the session's scratchpad, s942_alpharank.py) checked
steps 1 to 4 on 400 random games with 2 or 3 players, 2 or 3 strategies
each, and integer payoffs from 0 to 2, so that ties occur. At α = 0.1
and m = 20, each chain had every one-population move positive, a
transition matrix of rank n − 1 (so a unique stationary distribution), and
a positive stationary vector. At α = 200 the transition matrix was within
10⁻¹² of the limit matrix. The limit matrix's closed classes equalled the
sink SCCs of the weakly-better-response graph, computed separately from the
payoffs, in all 400 games. Integrating the full replicator flow from the
midpoints of 932 polytope edges, the flow stayed on the edge to 10⁻¹² and
ended at the better end, or did not move when payoffs tied. The interior
log-ratio divergence of two-population flows was 0 at 100 random points.
It had two controls, each of which had to find a difference. Dropping
neutral moves from the graph changed the sink structure in 359 of 400
games, which shows the ties matter. And a one-population replicator, whose
payoffs depend on its own mix, had divergence up to 1.23, which shows the
divergence check can detect a non-zero value.

## Note of 2026-10-30: the clause the narrowing drops

The old title said that, as the intensity grows, the chain's transitions
"become those of Markov chains confined to the sink strongly connected
components". The limit chain also has transitions out of profiles that
are not in any sink. It moves along weakly better deviations everywhere.
It is the MCC only on the sinks, which are its closed classes. The old
wording was imprecise rather than false in substance, so it is recorded
here only (ADR-047's kind 3). The paper's Theorem 2.5.1 says "the
macro-model's transition probabilities become the MCC transitions"
(NOTE-1156), with the same ellipsis.
