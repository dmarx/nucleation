---
status: Active
title: 'On a finite set of outcomes, some function rises with every move that wins one of a negotiation''s conflicts exactly when no chain of winning moves returns to where it began, and the length of the longest such chain ending at an outcome is one such function; and a perfectly transitive record of which side won each pair among n options leaves a cyclic share of (n − 2)/3n under the Hodge decomposition, so a cyclic share measures ambivalence only above that baseline, and a coherent record is not yet one aligned with any single perspective''s ordering'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either construction below, or in the computation of the
  transitive record's residual.
tags:
- mathematics
- game-theory
- emotion-and-affect
date: '2026-10-23'
line:
- formal-apparatus
- organizational-affect
grounds:
- THEORY-tmpj4ciq
- THEORY-tmp4zhyp
summary: >-
  The formal core of the rename of 2026-10-23 from "ascendancy" to
  "potential" ([TERM-tmp8gbrt](../terms.d/TERM-tmp8gbrt.md)). Part 1 is the finite case of Monderer and
  Shapley's equivalence between the finite improvement property and a
  generalized ordinal potential, proved here because the record has not
  read their paper ([LIT-tmpp4esg](../literature.d/LIT-tmpp4esg.md)). Part 2 is a calibration of the Hodge
  decomposition (Candogan et al.; Jiang et al.) for binary conflict
  records, computed here: even a perfect ranking leaves a cyclic residual.
  Part 3 separates coherence from alignment.
---
<!-- inactive-ok-file: THEORY-tmpj4ciq TERM-tmp8gbrt — Proposed; the second-hand reading of Monderer and Shapley and the term this claim underwrites, cited as open -->
<!-- inactive-ok-file: LIT-tmpp4esg — Unavailable, no lawful copy reached; Monderer and Shapley, whose lemma part 1 proves for itself -->

# CLAIM-tmp7df5r: On a finite set of outcomes, some function rises with every move that wins one of a negotiation's conflicts exactly when no chain of winning moves returns to where it began, and the length of the longest such chain ending at an outcome is one such function; and a perfectly transitive record of which side won each pair among n options leaves a cyclic share of (n − 2)/3n under the Hodge decomposition, so a cyclic share measures ambivalence only above that baseline, and a coherent record is not yet one aligned with any single perspective's ordering

## The claim

**1. A potential exists exactly when winning moves never cycle.** Let X be
a finite set of outcomes and write x → y when the negotiation can move
from x to y by a move that wins a conflict. A *potential* is a function
P : X → ℝ with P(y) > P(x) whenever x → y.
- If P exists, no chain x₀ → x₁ → … → x_k = x₀ exists, since it would give
  P(x₀) > P(x₀).
- If no chain cycles, the graph of winning moves on the finite set X is
  acyclic, so every chain is finite, of length at most |X| − 1. Let P(x)
  be the length of the longest chain ending at x. If x → y, a longest
  chain ending at x extends to one ending at y, so P(y) ≥ P(x) + 1.

So "some ordering prevails", read as "the negotiation has a potential",
is exactly "no chain of winning moves cycles", and integer values
suffice. This is the finite case of what Monderer and Shapley call the
finite improvement property and a generalized ordinal potential
([THEORY-tmpj4ciq](../theory.d/THEORY-tmpj4ciq.md)), proved here because their paper is unread ([LIT-tmpp4esg](../literature.d/LIT-tmpp4esg.md)).

**2. A transitive binary record has a cyclic share of (n − 2)/3n.** Take n
options, every pair contested once, and the record Y on the complete
graph with Y = +1 on each pair in the direction of the winner, the
winners forming a strict ranking 1 ≻ 2 ≻ … ≻ n. The least-squares
potential of the Hodge decomposition ([THEORY-tmp4zhyp](../theory.d/THEORY-tmp4zhyp.md)) on the complete
graph is s = (1/n) div Y up to a constant, and option i's net wins are
(n − i) − (i − 1) = n + 1 − 2i, so s_i − s_j = 2(j − i)/n. On the pair
i ≻ j with d = j − i the residual is 1 − 2d/n, and there are n − d such
pairs. With A = Σ(n − d), B = Σ(n − d)d and C = Σ(n − d)d², summed over
d = 1, …, n − 1,

  A = n(n − 1)/2, B = n(n − 1)(n + 1)/6, C = n²(n − 1)(n + 1)/12,

and the squared residual is A − (4/n)B + (4/n²)C = (n − 1)(n − 2)/6.
Divided by ‖Y‖² = n(n − 1)/2, the cyclic share is (n − 2)/3n: 1/9 for
three options, rising towards 1/3. It was also computed numerically for
n = 3, 4, 5, 8 and 20.

So a binary record's cyclic share is not ambivalence. A perfect ranking
already leaves one, because binary outcomes are not differences of any
scores. Ambivalence is the excess over this baseline, or, without the
least-squares step, the count of circular triads.

**3. Coherence is not alignment.** A record can be wholly gradient while
no single perspective wins: a stable compromise that splits every
conflict the same way is as coherent as one perspective deciding all of
them. Whether a particular perspective's ordering ≿_v is the potential is
a further fact, measured by how far the record's gradient agrees with the
flow ≿_v alone would produce, not by the gradient share.

## What it does not say

- That a negotiation is a game in Monderer and Shapley's sense. A
  potential game has players changing their own coordinates of a joint
  profile; a negotiation over one indivisible choice has no such
  coordinates. Part 1 needs only the relation of winning moves, so it
  holds for either; the game-theoretic reading fits where the
  organization's choice is divided into jurisdictions, as Sen's is
  ([THEORY-027](../theory.d/THEORY-027.md)).
- That the potential's existence fixes the dynamics. One-at-a-time
  winning moves climb it and stop at a local maximum; simultaneous moves
  can cycle even in an exact potential game.
- That the Hodge shares are invariant. They depend on the weights given
  to pairs, the aggregation of repeated contests and the norm; on
  continuous magnitudes a lexicographic override has no real-valued
  potential at all ([CLAIM-tmp85p0g](CLAIM-tmp85p0g.md)), so the term is read ordinally there.
  [CLAIM-369](CLAIM-369.md) makes the same point for population dynamics: which part of a
  flow counts as gradient depends on a chosen metric.
