---
status: Superseded
superseded_by:
- THEORY-tmpyulw1
promote_when: >-
  A step-by-step re-derivation, recorded under ADR-047 v2, of the upper
  bound for locally observable games (CBP's Corollary 3 against stochastic
  opponents, or a corrected NeighborhoodWatch bound against adversarial
  ones), together with the T^2/3 lower bound of Theorem 4, or a reading of
  a later complete source that restates the classification with its
  proofs, such as Lattimore and Szepesvári's corrected adversarial
  analysis. A citation of the classification by others does not count.
title: 'The minimax regret of a finite partial-monitoring game takes one of four rates, decided by its loss and signal matrices: 0 when only one action is non-dominated, Θ̃(√T) when every pair of neighbouring actions is locally observable, Θ(T^2/3) when the game is globally but not locally observable, and Θ(T) when it is not globally observable; against stochastic opponents for every game, against oblivious adversaries for non-degenerate games'
version: 3
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Proposed from NOTE-tmpupizd, as Bartók et al.'s Theorems 1 and 2
    state it. The observability lemma beneath it is re-derived in
    THEORY-tmpwtj3m. Theorem 4's lower bound was read with its proof. The
    upper bounds' analyses were read at the level of statements and main
    steps, and the adversarial one was later corrected by Lattimore and
    Szepesvári, which was not read. Hence Proposed.
- version: 2
  date: '2026-10-25'
  note: >-
    Lattimore and Szepesvári are now read (LIT-tmpfjv79, NOTE-tmpkgxba), and
    cited in place of the arXiv number. A dated note records that the
    promote_when is met by its second disjunct, but that two clauses are
    mis-stated: the trivial class is "no pair of neighbouring actions", and
    the lower bound's v must lie in the kernel of every signal matrix in
    N_ab (THEORY-tmpwqg2f). The reading proposes that this entry be
    Superseded by THEORY-tmpyulw1 rather than promoted, which is the owner's
    decision under ADR-047. The status is unchanged.
- version: 3
  date: '2026-10-25'
  note: >-
    Superseded by THEORY-tmpyulw1, at the owner's decision of 2026-10-25
    under ADR-047, from the reading of Lattimore and Szepesvári
    (NOTE-tmpkgxba). That entry restates the classification for every
    finite game with proofs of its missing pieces, as this entry's
    promote_when asked. Two clauses here are mis-stated: the trivial class
    is "no pair of neighbouring actions", not "one non-dominated action",
    and the lower bound's v must lie in the kernel of every signal matrix
    in N_ab (THEORY-tmpwqg2f). Bartók et al.'s CBP results remain as read
    in NOTE-tmpupizd. The body is unchanged.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-tmpwpq36
summary: >-
  Bartók, Foster, Pál, Rakhlin and Szepesvári (2014), [LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md), read
  in [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md). Four classes, trivial, easy, hard and hopeless, with
  conditions checkable from the matrices before play. It classifies the
  best policy for a fixed, known game. It does not cover a policy that is
  barred from some actions, a feedback structure that changes during play,
  or finite-horizon constants, and its adversarial half excludes
  degenerate games.
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose example is classified here, nothing here rests on it -->
# THEORY-tmpz3a05: The minimax regret of a finite partial-monitoring game takes one of four rates, decided by its loss and signal matrices: 0 when only one action is non-dominated, Θ̃(√T) when every pair of neighbouring actions is locally observable, Θ(T^2/3) when the game is globally but not locally observable, and Θ(T) when it is not globally observable; against stochastic opponents for every game, against oblivious adversaries for non-degenerate games

## Source

Bartók, Foster, Pál, Rakhlin and Szepesvári (2014), [LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md), Theorems
1 and 2, assembled in their §7 from Piccolboni and Schindelhauer (2001) for
the linear lower bound, Antos et al. (2012) for the √T lower bound, their
own Theorem 4 for the T^{2/3} lower bound, FeedExp (Piccolboni and
Schindelhauer; Cesa-Bianchi, Lugosi and Stoltz 2006) for the T^{2/3} upper
bound, CBP (Corollary 3) and NeighborhoodWatch (Corollary 5) for the √T
upper bounds. Read in [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md).

## What was actually shown

For a game G = (L, H) with K non-dominated actions:

| class | condition | stochastic (Thm 1) | adversarial, non-degenerate (Thm 2) |
|---|---|---|---|
| trivial | K = 1 | 0 | 0 |
| easy | K > 1, locally observable | Θ̃(√T) | Θ(√T) |
| hard | globally, not locally observable | Θ(T^{2/3}) | Θ(T^{2/3}) |
| hopeless | not globally observable | Θ(T) | Θ(T) |

The observability conditions are [THEORY-tmpwtj3m](THEORY-tmpwtj3m.md)'s span condition, with D
equal to all actions (global) or to the neighbourhood action set N⁺_{i,j}
(local). The lower bound of Theorem 4 places two outcome distributions
p₀ ± εv about the boundary between two neighbours that are not locally
observable, with v in the kernel of both signal matrices, and sets
ε ∝ T^{−1/3}. Telling them apart needs plays of actions outside the
neighbourhood, each costing at least a constant β. Balancing the
ε-regret of guessing against the β-cost of looking gives T^{2/3}.

In the stochastic easy class the individual regret for a fixed p is
logarithmic in T (Corollary 1). A hard game is easy against opponents kept
away from its unobservable boundaries, and CBP adapts to that without being
told (Theorem 5).

What could have failed: there could have been games with intermediate
exponents between 1/2 and 2/3. The paper closes that gap, which was the
open part.

## What this does not say

- **Not about a constrained learner.** The class is the minimax regret of
  the best algorithm, which may play any action. A policy that never plays
  some action has whatever regret that restriction costs, linear in T if
  the action is sometimes optimal, whatever the game's class.
- **Not about degenerate games against adversaries.** The paper leaves them
  open. Lattimore and Szepesvári ([LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md)) "complete the
  classification of finite adversarial partial monitoring to include all
  games" and "correct errors in previous analyses", by their abstract.
- **Not about constants or finite T.** The constants depend on the game and
  can be large.
- **Not about learned or changing feedback.** L and H are fixed and known.
  Authority that edits the losses or the signal channels during learning is
  outside the theorem, as A29 already cautioned ([CLAIM-446](../claims.d/CLAIM-446.md)'s note).
- **Not about adaptive adversaries.** The adversarial results are for
  oblivious ones.

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** Its approach–avoid example is in the easy class
  ([THEORY-tmpwtj3m](THEORY-tmpwtj3m.md)). Approach with suppressed feedback is hopeless, and
  information available only from a dominated check is hard.
- **Kwon and Perchet ([LIT-tmpm3j41](../literature.d/LIT-tmpm3j41.md))** give the vector-payoff counterpart.
  For approachability under partial monitoring the worst-case rates are
  T^{−1/2} with outcome-dependent signals and T^{−1/3} in general, the
  average-payoff forms of √T and T^{2/3}.
- **[QUESTION-271](../questions.d/QUESTION-271.md).** The classification says when feedback that depends on
  the action played costs more than full information, and by how much.

## Note of 2026-10-25: the reading of Lattimore and Szepesvári

Lattimore and Szepesvári, "Cleaning up the neighborhood" ([LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md)),
is now read ([NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md)). This entry's promote_when is met by its
second disjunct: the paper restates the classification and proves the two
pieces that were open or flawed, the √n upper bound for all locally
observable games (NeighborhoodWatch2) and the corrected T^{2/3} lower
bound, and cites the rest as Bartók et al. did. Its first disjunct is met
in substance too, by the re-derivation recorded in [THEORY-tmpyulw1](THEORY-tmpyulw1.md).

Two clauses here are mis-stated, so the reading proposes that this entry
be Superseded by [THEORY-tmpyulw1](THEORY-tmpyulw1.md) rather than promoted:

- **The trivial class.** It is "no pair of neighbouring actions", not
  "only one action is non-dominated". The latter misplaces games with
  degenerate or duplicate actions: L = ((0, 0), (0, 1)), or two duplicate
  actions, have two non-dominated actions, no neighbours and regret 0, yet
  the wording puts them in the easy class.
- **The lower bound's kernel.** The vector v must lie in the kernel of
  every signal matrix in N_ab, not only of the two neighbours' signal
  matrices, as "with v in the kernel of both signal matrices" above has it
  ([THEORY-tmpwqg2f](THEORY-tmpwqg2f.md)). The theorem stands; the slip is harmless for
  non-degenerate games, where N_ab = {a, b}.

Its adversarial scope, non-degenerate games only, is also narrower than is
now known. Whether to supersede or to correct in place and promote is the
owner's decision under [ADR-047](../decisions.d/ADR-047.md). The status is unchanged.

## Superseded, 2026-10-25

At the owner's decision under ADR-047, this entry is Superseded by
THEORY-tmpyulw1 rather than promoted, for the two mis-stated clauses in
the note above. Cite THEORY-tmpyulw1 for the classification and
THEORY-tmpwqg2f for the role of degenerate actions and the corrected lower
bound.
