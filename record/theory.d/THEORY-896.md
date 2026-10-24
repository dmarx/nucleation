---
number: 896
status: Proposed
formerly:
- THEORY-tmpj4ciq
promote_when: >-
  Monderer and Shapley (1996), LIT-1462, read first-hand: the lemma's
  wording, number and page confirmed (reported as Lemma 2.5), together
  with the paper's definitions of the finite improvement property and of
  generalized ordinal potential, and agreement with the proof given here.
  The mathematics is checked below. What waits is the attribution and the
  exact statement.
title: 'A finite game in strategic form has the finite improvement property, every path of strict unilateral improvements being finite, exactly when it has a generalized ordinal potential, a real function on strategy profiles that rises with every strict unilateral improvement; so in a finite game an ordering along which every improving move climbs exists exactly when there is no improvement cycle, and every sequence of improving moves ends at a pure equilibrium'
version: 1
tags:
- game-theory
- mathematics
date: '2026-10-23'
source:
- LIT-1462
summary: >-
  Monderer and Shapley (1996), [LIT-1462](../literature.d/LIT-1462.md), unread: reported by Duersch,
  Oechssler and Schipper (arXiv 1003.4274) as Lemma 2.5. A finite game
  has the finite improvement property iff it has a generalized ordinal
  potential. The record proves the finite case here: a potential that
  rises with every improvement forbids cycles, and an acyclic improvement
  graph on finitely many profiles has an integer potential, the length
  of the longest improvement path into each profile. It is the precise
  form of "an ordering prevails" ⇔ "no improvement cycles", and it is
  ordinal.
supports:
- CLAIM-434
- CLAIM-tmp1xoac
---
<!-- inactive-ok-file: LIT-1462 — Unavailable, unread; Monderer and Shapley 1996, the source this result is attributed to -->
<!-- inactive-ok-file: TERM-076 CLAIM-440 CLAIM-436 THEORY-894 — Proposed or draft; the term and claims this result bears on, and the cardinal decomposition filed with it -->

# THEORY-896: A finite game in strategic form has the finite improvement property, every path of strict unilateral improvements being finite, exactly when it has a generalized ordinal potential, a real function on strategy profiles that rises with every strict unilateral improvement; so in a finite game an ordering along which every improving move climbs exists exactly when there is no improvement cycle, and every sequence of improving moves ends at a pure equilibrium

## Source

- Monderer and Shapley (1996), *Potential Games*, [LIT-1462](../literature.d/LIT-1462.md), **not
  read**. No lawful copy was reached by this client (see its status note).
- The attribution is second-hand. Duersch, Oechssler and Schipper,
  *Unbeatable Imitation* (arXiv 1003.4274; Games and Economic Behavior,
  DOI 10.1016/j.geb.2012.05.002), p. 18 of the arXiv PDF: "Monderer and
  Shapley (1996, Lemma 2.5) show that a finite strategic game has no strict
  improvement cycle (what they call the finite improvement property) if
  and only if it is a generalized ordinal potential game." Neither paper is
  filed in the record.
- A second restatement is weaker and differently worded. Biggar and
  Shames, *Preference graphs* (arXiv 2502.03546), p. 18: "Monderer and
  Shapley (1996b) show that ordinal potential games satisfy the ‘finite
  improvement property’". They then characterize *ordinal* potential games
  in their own terms: "Theorem 4.3. A game is ordinal potential if and only
  if its preference graph is acyclic." The two restatements differ on
  whether the class is generalized ordinal or ordinal. Their definitions
  of the improvement relation differ too, which is why the statement waits
  on the original.

## What was actually shown

Shown here, by the record, for finite games. These are standard
definitions, not yet checked against the paper.

- **Strict unilateral improvement.** A step x → y such that y differs from
  x only in player i's strategy and u_i(y) > u_i(x).
- **Improvement path.** A sequence of profiles each obtained from the last
  by such a step.
- **Finite improvement property (FIP).** Every improvement path is finite.
- **Generalized ordinal potential.** A function P from profiles to ℝ such
  that every such step has P(y) > P(x).
- **Ordinal potential.** The stronger requirement u_i(y) > u_i(x) ⇔ P(y) >
  P(x) for every unilateral change.
- **Exact potential.** P(y) − P(x) = u_i(y) − u_i(x).

**Claim.** A finite game has the FIP iff it has a generalized ordinal
potential.

*If.* P rises strictly along any improvement path, so no profile occurs
twice on it. There are finitely many profiles, so the path has at most |X|
− 1 steps.

*Only if.* Suppose the improvement graph, profiles joined by strict
unilateral improvements, had a directed cycle. Going round it forever
would be an infinite improvement path, contradicting the FIP. So the graph
is acyclic. Let P(x) be the number of steps in the longest improvement
path ending at x. That number is finite, since an acyclic graph on
finitely many nodes has only finitely many paths. If x → y is a step, any
path ending at x extends by that step to one ending at y, so P(y) ≥ P(x)
+ 1 > P(x). P is a generalized ordinal potential, and it takes integer
values.

**Corollary (dynamics).** In a finite game with the FIP, every
better-response sequence, one player at a time making some strictly
improving move, terminates. It terminates at a profile from which no
player can strictly improve, which is a pure Nash equilibrium. So pure
equilibria exist. Duersch et al. report this as Monderer and Shapley's
"Lemma 2.5 and the first paragraph on p. 129".

**For the record.** With the perspectives as players, "an ordering
prevails along which every improving move climbs" is equivalent, for a
finite set of profiles, to "no perspective-by-perspective improvement
ever returns to where it began". The ordering needs no more than integer
values. The obstacle [CLAIM-436](../claims.d/CLAIM-436.md) raises for lexicographic orders does
not arise on a finite set. FIP is the property of the incentives that
makes [TERM-076](../terms.d/TERM-076.md)'s "prevails" a theorem rather than a metaphor, in the
ordinal sense. The cardinal sense, an exact potential and the share of
the flow it explains, is [THEORY-894](THEORY-894.md), and the two come apart. A
game can be far from exact, with a large harmonic share, and still have
the FIP ([NOTE-1116](../notes.d/NOTE-1116.md)).

## What this does not say

- **Nothing about simultaneous moves.** The FIP concerns one player moving
  at a time. Under simultaneous best responses a 2×2 coordination game,
  an exact potential game, cycles forever when started off the diagonal.
- **Nothing about the global maximum.** Improvement paths end at local
  maxima of P, pure equilibria, which need not be P's top.
- **Generalized, not ordinal.** The FIP gives only that P rises with
  strict improvements. Indifferent moves are unconstrained. Whether the
  paper characterizes ordinal potentials too, and under what condition on
  indifference, is unread. The restatements disagree.
- **Nothing about infinite games.** Whether a game with infinitely many
  profiles and no improvement cycle has a real-valued potential is a
  different question, and the lexicographic case suggests it can fail. What
  the paper says about infinite games is not known here.
- **Nothing about collective choice.** The result is about unilateral
  improvements by players over joint profiles, not about a rule that
  aggregates rankings of one shared choice ([NOTE-1116](../notes.d/NOTE-1116.md), "Where it
  does not fit").
