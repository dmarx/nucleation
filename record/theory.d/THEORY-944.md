---
number: 944
status: Active
formerly:
- THEORY-tmpxh6cj
title: "The value of the zero-sum game between two populations' evaluation matrices does not depend on which Nash equilibrium is used, is unchanged by adding agents that behave as mixtures of existing members, and is not positive for a population whose agents are all behavioural mixtures of the other's"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed the three
    parts step by step, including the reader's step from Proposition 2 to
    the value, and re-ran them by script with controls (status review 22).
    The old promote_when: A checked re-derivation recorded in this file,
    which the reading made (NOTE-1143) and which ADR-047 counts toward
    promotion. It is refuted by two finite populations whose zero-sum game
    has Nash pairs of different value, by a population whose value against
    some other population changes when a member behaviourally equal to a
    mixture of members is added, or by a population P, each of whose
    agents is a behavioural mixture of Q's, with v(P, Q) > 0. Results on
    how to grow a population, or on PSRO's performance, neither promote
    nor refute it.
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1509
summary: >-
  Balduzzi et al. (2019), [LIT-1509](../literature.d/LIT-1509.md), Propositions 2 and 5, read from
  arXiv v2 in [NOTE-1143](../notes.d/NOTE-1143.md), proofs followed and re-derived. Relative
  population performance is a game value, so equilibrium selection never
  arises. Behaviourally redundant members leave it unchanged, and a
  population contained in another's behavioural hull cannot beat it.
  It scores populations, not members, it is cardinal, and populations not
  nested by hull can still beat one another in a cycle.
---
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->

# THEORY-944: The value of the zero-sum game between two populations' evaluation matrices does not depend on which Nash equilibrium is used, is unchanged by adding agents that behave as mixtures of existing members, and is not positive for a population whose agents are all behavioural mixtures of the other's

## Source

Balduzzi, Garnelo, Bachrach, Czarnecki, Pérolat, Jaderberg & Graepel,
[LIT-1509](../literature.d/LIT-1509.md), read in [NOTE-1143](../notes.d/NOTE-1143.md) from arXiv:1901.08106v2: Definition 3
and Proposition 5 (p. 5, proof p. 13), Proposition 2 (p. 4) and
Definitions 6–7 (proof p. 12).

## What was actually shown

- **Definition.** For populations P and Q, v(P, Q) = pᵀA_{P,Q}q at a Nash
  pair (p, q) of the zero-sum game with payoff φ(v, w), v ∈ P, w ∈ Q.
- **Independence of the choice.** A zero-sum game has one value whichever
  equilibrium attains it (Proposition 5(i)).
- **Redundancy.** If an added agent's results against every member equal
  those of a mixture of members, every mixture available after the
  addition was available before, so the value is unchanged. Proposition 2
  shows the gamescape is unchanged up to an isometric embedding. The
  reader made the step to the value: a game's value depends only on the
  sets of payoff vectors each side can mix, and those sets are unchanged.
- **Containment (Proposition 5(iii)).** If every agent of P is
  behaviourally a mixture of agents of Q, Q can reproduce any mixture P
  plays. By antisymmetry the mirrored play is worth zero, so v(P, Q) ≤ 0,
  and v(P, R) ≤ v(Q, R) for every R. The paper writes hull(P) ⊂ hull(Q);
  the proof needs it read behaviourally, not in weight space.

What could have come out otherwise: a population score that rewards
numbers, such as a mean over members or a sum of wins, rises when members
are duplicated. This one does not.

## What this does not say

- **That it ranks individuals.** It compares populations. In a cyclic
  game the paper holds that an individual's performance is meaningless.
- **That populations are totally ordered.** Only hull-nested populations
  are ordered by it. Singletons in rock-paper-scissors are populations,
  and their values cycle.
- **That it detects strength a population does not exhibit.** It is
  computed from the evaluation matrix of the agents present. The paper's
  concentric rock-paper-scissors populations all score 0 against each
  other, though the outer one exploits a fixed opponent better.
- **Anything ordinal.** The value uses payoff magnitudes.

## Connections

Of the scoring rules in this group it is the one that a padded
population cannot move without any further condition. Compare
[THEORY-946](THEORY-946.md), which needs a unique equilibrium and covers exact copies
only. For [CLAIM-451](../claims.d/CLAIM-451.md) it is the formal shape of relief by mixing:
evaluate the portfolio, not the option ([NOTE-1143](../notes.d/NOTE-1143.md)).

## Note of 2026-10-30: the second check

The second check at the status review ([ADR-065](../decisions.d/ADR-065.md) §5) followed each step.

Independence. By the minimax theorem every Nash pair of a finite zero-sum
game attains max_p min_q pᵀMq = min_q max_p pᵀMq, so the value does not
depend on which pair is used.

Redundancy. The value is the maximum, over the convex hull of P's payoff
vectors against Q, of the smallest entry, and dually for Q's columns. An
agent x added to P with φ(x, w) = Σ_k λ_k φ(m_k, w) for every w has its
payoff vector inside the hull of P's, so the hull and the value are
unchanged. An agent y added to Q equal to a mixture μ of Q's members has,
by antisymmetry, φ(v, y) = −φ(y, v) = −Σ_k μ_k φ(q_k, v) = Σ_k μ_k φ(v,
q_k), a mixture of Q's columns, so again nothing changes.

Containment. Let each v_i in P satisfy φ(v_i, w) = Σ_k λ_ik φ(q_k, w) for
every w. For any mixture p over P put ν = λᵀp, a mixture over Q. If Q
plays ν, P's payoff is pᵀA_{P,Q}ν = νᵀA_{Q,Q}ν = 0 by antisymmetry, so
v(P, Q) ≤ 0. P's payoff vector against any R equals ν's, so v(P, R) ≤ v(Q,
R).

A script (numpy, with an exact linear-programming solver, in the session's
scratchpad) checked these on 300 random antisymmetric games of 4 to 8
agents split into two populations. Adding an agent that behaved as a
random mixture of one side's members left the value unchanged to 10⁻⁹, on
either side. Three such mixture agents of Q, taken as a population, scored
at most 0 against Q and no more than Q against a third population. Two
controls moved: a mean-over-members score went from 0.086 to −0.250 when a
member was duplicated, and adding an agent that beats every member of Q
moved the value from 0.444 to 1.750.
