---
number: 434
status: Active
formerly:
- CLAIM-tmp7df5r
title: 'On a finite set of outcomes, some function rises with every move that wins one of a negotiation''s conflicts exactly when no chain of winning moves returns to where it began, and the length of the longest such chain ending at an outcome is one such function; a perfectly transitive record of which side won each pair, in a complete tournament contesting every pair once, leaves a cyclic share of (n − 2)/3n under the Hodge decomposition, a baseline that does not carry to sparse records; the Hodge gradient can reverse a comparison the wins settle, netting a record erases alternation, a record fixes a class of potentials rather than one, a coherent record is not yet one aligned with any single perspective''s ordering, a best-fitting ordering of a cycle is no Lyapunov function, the sign a class of potentials gives can be set-valued, and an ordering fitted to a record overstates its agreement there'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in any construction below, in the computation of the
  transitive record's residual, or in the synthetic cases of
  scratch/formal/valence.py.
tags:
- mathematics
- game-theory
- emotion-and-affect
date: '2026-10-23'
line:
- formal-apparatus
- organizational-affect
grounds:
- THEORY-896
- THEORY-894
summary: >-
  The formal core of the rename of 2026-10-23 from "ascendancy" to
  "potential" ([TERM-076](../terms.d/TERM-076.md)). Part 1 is the finite case of Monderer and
  Shapley's equivalence between the finite improvement property and a
  generalized ordinal potential, proved here because the record has not
  read their paper ([LIT-1462](../literature.d/LIT-1462.md)). Part 2 is a calibration of the Hodge
  decomposition (Candogan et al.; Jiang et al.) for binary conflict
  records, computed here: even a perfect ranking leaves a cyclic residual.
  Part 3 separates coherence from alignment. Parts 9 to 11 were added
  after a second review. Parts 4 to 8 were added
  when a review of the pull request found that the measures built on
  parts 2 and 3 confused ordinal and cardinal structure; each is checked
  in scratch/formal/valence.py.
uses:
- TERM-077
supports:
- CLAIM-tmpuxcp6
---
<!-- inactive-ok-file: THEORY-896 TERM-076 — Proposed; the second-hand reading of Monderer and Shapley and the term this claim underwrites, cited as open -->
<!-- inactive-ok-file: LIT-1462 — Unavailable, no lawful copy reached; Monderer and Shapley, whose lemma part 1 proves for itself -->

# CLAIM-434: On a finite set of outcomes, some function rises with every move that wins one of a negotiation's conflicts exactly when no chain of winning moves returns to where it began, and the length of the longest such chain ending at an outcome is one such function; a perfectly transitive record of which side won each pair, in a complete tournament contesting every pair once, leaves a cyclic share of (n − 2)/3n under the Hodge decomposition, a baseline that does not carry to sparse records; the Hodge gradient can reverse a comparison the wins settle, netting a record erases alternation, a record fixes a class of potentials rather than one, a coherent record is not yet one aligned with any single perspective's ordering, a best-fitting ordering of a cycle is no Lyapunov function, the sign a class of potentials gives can be set-valued, and an ordering fitted to a record overstates its agreement there

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
([THEORY-896](../theory.d/THEORY-896.md)), proved here because their paper is unread ([LIT-1462](../literature.d/LIT-1462.md)).

**2. A transitive binary record has a cyclic share of (n − 2)/3n, in a
complete tournament.** Take n options, every pair contested once, and the record Y on the complete
graph with Y = +1 on each pair in the direction of the winner, the
winners forming a strict ranking 1 ≻ 2 ≻ … ≻ n. The least-squares
potential of the Hodge decomposition ([THEORY-894](../theory.d/THEORY-894.md)) on the complete
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
scores. The baseline is exact only for the complete, equally weighted
tournament; part 6 shows it does not carry to sparse records. Ambivalence
is better counted without the least-squares step, as circular triads or
as the least fraction of wins whose reversal leaves them acyclic
([TERM-077](../terms.d/TERM-077.md)).

**3. Coherence is not alignment.** A record can be wholly gradient while
no single perspective wins: a stable compromise that splits every
conflict the same way is as coherent as one perspective deciding all of
them. Whether a particular perspective's ordering ≿_v is the potential is
a further fact, measured ordinally by the share of contested wins that
agree with ≿_v, not by the gradient share. With perspectives v: A ≻ B ≻ C
and w: C ≻ B ≻ A and a compromise settling every conflict as B ≻ A ≻ C,
the record is wholly acyclic, and its agreement is 2/3 with v and 1/3
with w; where v decides everything, it is 1 and 0 (valence.py, case 6).

**4. The Hodge gradient can reverse a comparison the wins settle.** Take
margins A over B by 1, B over C by 10 and A over C by 1. The wins are
transitive, A ≻ B ≻ C, and the longest-chain potential of part 1 keeps
that order. On the complete graph the least-squares potential is
s = (1/3) div Y, and div Y = (1 + 1, 10 − 1, −10 − 1) = (2, 9, −11), so
s = (2/3, 3, −11/3): B above A, though A won their contest. The cyclic
share is 0.33, though nothing cycles. So the gradient is not an ordinal
potential, and its cyclic share mixes uneven margins with cycles. The
counterexample is the review's; it was checked by hand and in valence.py,
case 1.

**5. Netting a record erases alternation.** Let one pair be contested six
times, won by A and B in turn. The netted flow on the pair is zero, the
record of a pair never in conflict. Kept as a sequence, it has six
contests and five reversals in five transitions, the most variable record
the pair can have (case 4). Direction, the number of contests and their
variability are three quantities; a measure built on the net flow sees
only the first.

**6. The baseline does not carry to sparse records.** Take four options
and a transitive record A ≻ B ≻ C ≻ D on every pair except (A, C), never
contested. Its cyclic share is 0.200, against 1/6 for the complete
tournament; with the same graph and orientations drawn from other
orderings it ranges from 0.1 to 0.2 (case 3). The baseline for a sparse
record is a null model that keeps its graph of contested pairs, not
(n − 2)/3n.

**7. A record fixes a class of potentials, not one.** Every strictly
increasing transform of a potential is one. And where pairs are not
contested, distinct orderings can agree with every win: on wins A over B,
C over D and A over D, both A ≻ B ≻ C ≻ D and C ≻ A ≻ D ≻ B agree with all
three (case 7). Only a contest on a pair the two rank differently, such
as B against C, separates them.

**8. A vacuous record has every potential.** With no contested pairs the
relation of wins is empty and acyclic, so by part 1 every ordering is a
potential (case 5). Agreement, as in part 3, is undefined there, having
no wins to count.

**9. A best-fitting ordering of a cycle is no Lyapunov function.** Let
the moves recur A → B → C → A. The best-fitting ordering misfits one move
in three, a reversal fraction of 1/3. But a function non-decreasing along
all three moves has P(A) ≤ P(B) ≤ P(C) ≤ P(A), so it is constant: no
ordering is a Lyapunov function of these dynamics, however well it fits
(valence.py, case 10). Fit within a tolerance and monotonicity along the
dynamics are different properties; the second is what resumption needs.

**10. The sign a class gives can be set-valued.** Take the two orderings
of part 7, both potentials of the same record, a state B and a reference
state C. A ≻ B ≻ C ≻ D puts the state ahead of its reference and
C ≻ A ≻ D ≻ B puts it behind (case 12). So {sgn_P(x, r) : P in the class}
is {+, −}, and the record does not fix the sign.

**11. An ordering fitted to a record overstates its agreement there.**
Draw every pair's winner among five options at random, so that no
ordering prevails, and fit the best ordering to one such record. Over
200 trials it agrees with 0.87 of the contests it was fitted to, and with
0.50 of a fresh record drawn the same way, which is chance (case 13).
Agreement of a selected ordering is scored on held-out contests.

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
- That the Hodge decomposition is useless here. It measures cardinal
  inconsistency, and where margins are intensities that is worth
  measuring. Parts 4 to 6 say only that it is not the test of an ordinal
  potential.
- That the Hodge shares are invariant. They depend on the weights given
  to pairs, the aggregation of repeated contests and the norm; on
  continuous magnitudes a lexicographic override has no real-valued
  potential at all ([CLAIM-436](CLAIM-436.md)), so the term is read ordinally there.
  [CLAIM-369](CLAIM-369.md) makes the same point for population dynamics: which part of a
  flow counts as gradient depends on a chosen metric.
