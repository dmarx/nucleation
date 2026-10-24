---
status: Read
paper: 'LIT-tmpkx8qe'
title: 'Omidshafiei et al. — α-Rank: multi-agent evaluation by evolution'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1903.01373v4 (4 October 2019), a
    45-page PDF under arXiv's non-exclusive distribution licence, extracted
    by pdftotext. Read: sections 1–4 (pp. 1–21), the captions of Figures
    1–17, and supplementary sections 5.1–5.4 (pp. 38–45), with every proof
    followed. The reference list was skimmed. The version of record in
    Scientific Reports (CC BY 4.0) predates v4 and was not compared. Page
    numbers below are v4's. Every quotation was checked against the
    extracted text by script. The single-population chain of supplement
    5.3 was reimplemented and run by script
    (scratchpad/marlb_scripts/alpharank_clone.py).
date: '2026-10-24'
summary: >-
  A methods paper with theory and applications. Agents are ranked by the
  stationary distribution of a finite-population, rare-mutation Fermi
  imitation chain on pure profiles, unique at every finite α. As α grows
  its transitions become those of Markov-Conley chains, the sinks of the
  better-response graph, which the paper ties to chain components of the
  replicator flow. The limit of the ranking is not characterized, and it
  is not invariant to copies.
---
<!-- inactive-ok-file: THEORY-tmpwc2nk — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmpuxcp6 CLAIM-tmp1xoac CLAIM-tmp8z857 CLAIM-tmp28sti THEORY-896 — Proposed; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpxufhw: Omidshafiei et al. — α-Rank: multi-agent evaluation by evolution

## What the paper does

**The motivation** (pp. 2, 10). Nash is hard to compute in general-sum
games (PPAD-complete), has a selection problem, and dynamics need not
reach it. The authors go further: "In fact, all known dynamics in games
(the replicator dynamics, the many continuous variants of the dynamics
used in the proof of Nash’s theorem, etc.) do cycle" (p. 10). That is an
overstatement as written, since many dynamics converge in potential games,
as the paper itself says on p. 16. They want a solution concept fitted to
dynamics.

**The macro-model** (pp. 4–8).
- K finite populations of m individuals, one per player slot. One
  individual from each population plays a meta-game.
- A focal individual copies another's strategy with the Fermi probability
  (1 + e^{α(f_τ − f_σ)})⁻¹, and mutates with a rate µ → 0. So at most one
  population is ever mixed, and only two strategies at a time.
- The fixation probability of a mutant τ against residents σ is
  (1 − e^{−αΔ})/(1 − e^{−mαΔ}) for payoff advantage Δ ≠ 0, and 1/m for
  Δ = 0 (eq. 9).
- The chain on pure profiles moves one population at a time.
- Theorem 2.1.2: with finite payoffs every transition is positive, so the
  chain is irreducible and its stationary distribution π unique. The
  ranking is the order of π's masses (p. 16).
- Single-population version (supplement 5.3): fitness is "local". The
  mutant's fitness is its payoff against the resident and the resident's
  is its payoff against the mutant, f(τ, σ) = M_τσ, whatever the
  population's composition (p. 42). Theorem 2.1.3 says the multi-population
  model contains this one; its proof is a sketch.
- Theorem 2.1.4 (proof p. 43): for large m the mean dynamics along an
  edge of the simplex are ẋ = x(1 − x)·tanh(α(f_τ − f_σ)/2), a replicator
  form with the Fermi revision in place of fitness.

**Conley** (pp. 10–13). Chain recurrence (ε, T-chains), chain components,
and a complete Lyapunov function. Such a function strictly decreases off
the chain recurrent set and is constant on each component. By Conley's
theorem one exists for every flow on a compact metric space. Hence: "every
game is a “potential” game, if only we change our solution concept from
equilibria to chain recurrent sets" (p. 13). Theorem 2.4.13: reachability
partially orders chain components (proof p. 44, followed: reflexive,
antisymmetric by maximality, transitive by chain transitivity).

**Markov-Conley chains** (p. 14).
- The response graph has an edge s → s′ when one player's deviation is
  weakly better for that player.
- An MCC is a Markov chain on a sink strongly connected component of that
  graph. Strict improvements get equal probability; payoff-neutral moves
  get a smaller one.
- A singleton MCC is a pure Nash equilibrium.
- The paper notes that this transition rule makes MCCs invariant under
  positive affine transformations of the payoffs.

**Theorem 2.4.24** (p. 14, proof p. 44). For the replicator flow, every
asymptotically stable sink chain component contains at least one MCC, and
each MCC lies in exactly one chain component. Since there are finitely
many pure profiles, the asymptotically stable sink chain components are
finitely many. The proof: replicator dynamics preserve volume in the
interior after a conjugation, so an asymptotically stable set must meet
the boundary. Inductively it reaches a vertex. Weakly better replies
from there are chain-reachable, by an ε-push into the better strategy or
⌈1/ε⌉ small hops along a payoff-neutral edge. The sink property then
pulls in the whole reachable set. The conjugation step is asserted
("the formal argument works by transforming"), not carried out. The
theorem does not give the converse: an MCC need not lie in an
asymptotically stable component, and a component containing one can be
much larger. In matching pennies the whole square is one component.

**Theorem 2.5.1** (p. 15, proof p. 45). As α → ∞, the macro-model's
transition probabilities become the MCC transitions, with neutral moves
at 1/m. Read exactly, this is a statement about transition matrices. At
α = ∞ the chain is reducible whenever there are several sinks, and the
authors say so: "In practice, setting the ranking-intensity to infinity
may not be computationally feasible; in this case, the underlying Markov
chain may be reducible and the existence of a unique stationary
distribution (which we use for our rankings) may not be guaranteed"
(p. 15). α-Rank therefore uses a large finite α, chosen by "a sweep over
α, starting from a small value and increasing it exponentially until
convergence of rankings" (p. 16).

**Examples and applications** (pp. 9, 16–21).
- Rock-paper-scissors: uniform at every α.
- Biased rock-paper-scissors: the Nash is (1/16, 5/8, 5/16) and α-Rank
  is uniform at large α, after favouring paper at intermediate α.
- Battle of the sexes: the two coordination profiles at large α. Figure
  3's caption names (O, O) and (M, O), where the text says (M, M), a slip
  in the caption.
- AlphaGo, 7 variants: all mass on AG(rvp), no cycles.
- AlphaZero chess, 56 snapshots: AZ(99.4) first with 0.39 and AZ(93.9)
  second with 0.22. AZ(86.4) ranks fifth, above longer-trained snapshots.
  α-Rank and the maximum-entropy Nash broadly agree, and earlier snapshots
  re-enter both supports at times.
- MuJoCo soccer, 10 agents: 6 survive, with many cycles.
- Kuhn poker with 3 and 4 players: 64 and 256 profiles.
- Leduc poker's 3 × 3 PSRO meta-game: profile (0, 0) takes all the mass.
- Property 3.3.2: computing π is cubic in the number of profiles, which is
  itself exponential in the number of players.

The authors' framing: "As such, our approach is descriptive rather than
prescriptive" (p. 16), a ranking by long-run survival, not advice on what
to play.

## What it establishes and what it does not

**Proved, and followed.** Theorem 2.1.2, Theorem 2.1.4's mean dynamics
(the tanh form re-derived), Theorem 2.4.13, Theorem 2.5.1 as a limit of
transition matrices, and Theorem 2.4.24 modulo the conjugation step.

**Not proved: the claim to have solved selection.** The paper says its
rankings "involve no equilibrium selection issues as the evolutionary
process converges to a unique stationary distribution" (p. 16). Uniqueness
holds at each finite α. But nothing is proved about the limit of π as
α → ∞. When there are several MCCs, how a large finite α divides mass
among them depends on the payoff differences that govern escape from each
sink and on m. That is a stochastic-stability question the paper does not
take up. MCCs are invariant to positive affine transformations of payoffs,
but a finite-α ranking need not be. Rescaling one player's payoffs alone
acts like a different α for that population, and the paper does not
show that the ranking survives it. Selection is moved into the choice of α, not removed.

**What the reader added, by derivation and by script.**
- *Single-population, symmetric zero-sum.* Under the local fitness of
  supplement 5.3, a transition σ → τ depends only on M(τ, σ) − M(σ, τ),
  so on τ's head-to-head result against σ. As α → ∞, transitions toward
  a strategy that beats the resident tend to η, and transitions toward
  one that loses vanish. The large-α support is the sink strongly
  connected component of the "beats" digraph. With no draws that digraph
  is a tournament and its sink component is unique: the top cycle. Within
  it the limiting masses depend only on who beats whom. A run of
  rock-paper-scissors with unequal margins (½, 3, 1) gives (0.42, 0.27,
  0.31) at α = 1 and the uniform distribution at α = 10 and 50. When the
  wins are acyclic all mass goes to the top element, which is what the
  AlphaGo data show.
- *Copies move it.* Rock-paper-scissors with scissors duplicated: the
  stationary distribution is (R, P, S₁, S₂) = (0.4, 0.2, 0.2, 0.2) at
  α = 0.1, 1, 10 and 50, m = 50. Rock, which beats the duplicated
  strategy, is promoted from a three-way tie to first place. The paper
  notes that Elo "can be artificially inflated by including duplicate
  copies of weaker agents in the set" (p. 39), and α-Rank has the same
  weakness.
- *Not population-dependent.* Because the fitness is local, the model
  has no channel by which a strategy's score depends on its own share.

## How it bears on the record

- **[TERM-077](../terms.d/TERM-077.md), [THEORY-896](../theory.d/THEORY-896.md) and [CLAIM-tmpuxcp6](../claims.d/CLAIM-tmpuxcp6.md): what order there is when wins
  cycle.** The paper's sentence on Conley has an exact discrete form that
  the record can use. Collapse each strongly connected component of the
  record's win digraph to a point. The quotient, the condensation, is
  acyclic, so it has an ordinal potential in [TERM-077](../terms.d/TERM-077.md)'s sense. The MCCs are
  its sinks. So a cyclic record always has a potential at one level up,
  with nonintegrability confined inside the components. This is standard
  graph theory and is not proved in the paper, which proves the
  continuous analogue by citation. Two consequences for [CLAIM-tmpuxcp6](../claims.d/CLAIM-tmpuxcp6.md).
  First, the claim's degree of nonintegrability, the minimum feedback-arc
  fraction, and the component structure are different facts: one large
  component can need very few reversals. Second, α-Rank sees only the
  sink component; a cycle among strategies that something else beats is
  transient and gets no mass. With [THEORY-896](../theory.d/THEORY-896.md)'s finite improvement
  property and no payoff ties every sink is a singleton, a pure
  equilibrium. Games whose sinks are all singletons are the paper's
  "weakly acyclic games", where it says its concept agrees with Young's
  conventions. **Supports [TERM-077](../terms.d/TERM-077.md)'s ordinal reading, and refines
  [CLAIM-tmpuxcp6](../claims.d/CLAIM-tmpuxcp6.md): the claim should say at which level, components or the
  quotient between them, its cycles lie.**
- **[CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md) and [CLAIM-tmp1xoac](../claims.d/CLAIM-tmp1xoac.md).** α-Rank's chain is the
  finite-population, rare-mutation imitation dynamic. Its stationary
  distribution is the "how hard each regime is to leave" measure that
  [CLAIM-tmp1xoac](../claims.d/CLAIM-tmp1xoac.md) lists among the replicator tools. But its fitness is
  local, so it cannot represent [CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md)'s share-dependent scoring.
  The lock-in of that case's part 4 needs fitness that depends on π.
  **Narrows: a ready tool for the claim's stochastic-stability item, not
  for the lock-in item.**
- **[CASE-124](../cases.d/CASE-124.md): capture by padding.** α-Rank does not resist it. Duplicating
  a strategy promotes whatever beats it. As a scoring layer it can be
  captured the way Elo can, unlike Nash averaging and population value.
  **Complicates any reading of α-Rank as a neutral ranking.**
- **[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md) and [CLAIM-tmp28sti](../claims.d/CLAIM-tmp28sti.md).** An MCC is a set of regimes that
  no single improving deviation leaves. That is a formal sense of a
  self-maintaining regime, in which the regime is a sink and not
  necessarily an optimum. In the biased game, a sink includes strategies
  Nash weights very differently. That is vocabulary, not evidence about
  anxiety or protective regimes. **Irrelevant beyond the analogy.**
