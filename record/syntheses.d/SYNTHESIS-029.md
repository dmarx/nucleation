---
number: 29
status: Proposed
formerly:
- SYNTHESIS-tmpha4sq
title: 'Optimal compressions at two budgets need not nest: for one four-state source both the deterministic and the stochastic information-bottleneck optima at two budgets are incomparable, so raising the budget can reorganize the optimum rather than refine it; nesting is settled under the top level and for two classes of source, and what guarantees it otherwise, and whether refinement, relevance and acquisition share one chain, is open'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (whether representations at
  different budgets or stages refine one another, and when that order
  agrees with relevance and acquisition) left out without a reason given;
  or a link this account states that no component states. Its standing is
  its components'.
tags:
- information-theory
- learning-theory
- representation-learning
date: '2026-11-10'
line:
- learned-structure
integrates:
- QUESTION-217
- QUESTION-220
- QUESTION-244
- QUESTION-291
- CLAIM-387
- CLAIM-392
- CLAIM-394
bears_on:
- QUESTION-217
- QUESTION-220
---
<!-- inactive-ok-file: ADR-083 THEORY-186 THEORY-759 — Proposed; components, citations and the decisions this account follows, with their standing -->
<!-- inactive-ok-file: QUESTION-244 QUESTION-291 — Answered; components and citations, with their standing -->

# SYNTHESIS-029: Optimal compressions at two budgets need not nest: for one four-state source both the deterministic and the stochastic information-bottleneck optima at two budgets are incomparable, so raising the budget can reorganize the optimum rather than refine it; nesting is settled under the top level and for two classes of source, and what guarantees it otherwise, and whether refinement, relevance and acquisition share one chain, is open

*A part account of the learned-structure line ([ADR-083](../decisions.d/ADR-083.md)); the line's account is built over it and its sibling parts. No relation or mention joins this part to any other component of the line.*

## The account

- **Three orders.** [QUESTION-217](../questions.d/QUESTION-217.md) (A1 and A2 of the exchange of
  2026-10-19; Open) separates three relations on a family of
  representations, refinement, relevance and acquisition, and asks when
  they share one chain. A2: "Crucially, the default should not be to
  assume these orderings agree." Its body sorts the record's readings
  into cases where two orders agree because they come from one
  eigenbasis (diffusion maps, diffusion wavelets, slow feature analysis,
  the hopping model) and cases where they come apart ([THEORY-186](../theory.d/THEORY-186.md)'s
  fine-first case, [THEORY-759](../theory.d/THEORY-759.md)'s order by frequency). Its note of
  2026-10-21 files the monotone half of A5's "two different mathematical
  order structures" as [CLAIM-409](../claims.d/CLAIM-409.md).
- **Whether optima nest.** [QUESTION-220](../questions.d/QUESTION-220.md) (A2's "most consequential
  missing bridge"; Open) refines [QUESTION-217](../questions.d/QUESTION-217.md). Its reason: "If none
  exist, an optimal learner's trajectory may merge or reshuffle
  categories rather than split them, and a coarse-to-fine reading of it
  is wrong." Two splits under [ADR-049](../decisions.d/ADR-049.md) left it the structural condition on
  P(X, Y) beyond the special cases, the size of the loss, and whether
  [THEORY-163](../theory.d/THEORY-163.md)'s colour hierarchy nests.
- **No, in general.** [QUESTION-244](../questions.d/QUESTION-244.md) (Answered) refines [QUESTION-220](../questions.d/QUESTION-220.md) and
  answers no on one source. [CLAIM-387](../claims.d/CLAIM-387.md) (demonstrated, Active) enumerates
  the deterministic encoders: the optima at 6.91 < β < 9.26 and
  9.26 < β < 16.06 are incomparable and not even laminar, so no fixed tree
  holds both, and "[NOTE-676](../notes.d/NOTE-676.md)'s nesting is bought by its tree restriction"
  (its summary). [CLAIM-392](../claims.d/CLAIM-392.md) (demonstrated, Active) rests on [CLAIM-387](../claims.d/CLAIM-387.md) and
  finds the same for the unique stochastic optima at β = 8 and β = 12 by
  [THEORY-753](../theory.d/THEORY-753.md)'s hull test. [QUESTION-244](../questions.d/QUESTION-244.md) keeps [CLAIM-392](../claims.d/CLAIM-392.md)'s caveat: the
  certificate is a fine grid with local search, and if it failed "the
  stochastic half would reopen here".
- **Yes, in the settled cases.** [QUESTION-291](../questions.d/QUESTION-291.md) (Answered) refines
  [QUESTION-220](../questions.d/QUESTION-220.md): every finite optimum nests under the β → ∞ one
  ([THEORY-743](../theory.d/THEORY-743.md)), a hull test decides a given pair ([THEORY-753](../theory.d/THEORY-753.md)), and the
  optima nest at every pair of budgets when Y is a function of X or both
  are binary ([THEORY-757](../theory.d/THEORY-757.md)).
- **Slowness and closure.** [CLAIM-394](../claims.d/CLAIM-394.md) (demonstrated, Active; first line
  distributed-agency) bears on [QUESTION-217](../questions.d/QUESTION-217.md): in a reversible linear
  Gaussian VAR(1) every slow-feature direction is a left eigenvector, so
  slowness selects exactly closed coarse-grainings. [QUESTION-217](../questions.d/QUESTION-217.md)'s body
  places it beside Schüler and Wiskott's variational reading and says:
  "Neither speaks to the order of acquisition."

## The components

- [QUESTION-217](../questions.d/QUESTION-217.md), A's (A1, A2) from the exchange of 2026-10-19, Open.
- [QUESTION-220](../questions.d/QUESTION-220.md), A2's, Open; narrowed on 2026-10-21 and 2026-10-27.
- [QUESTION-244](../questions.d/QUESTION-244.md), split from [QUESTION-220](../questions.d/QUESTION-220.md) on 2026-10-21, Answered by
  [CLAIM-387](../claims.d/CLAIM-387.md) and [CLAIM-392](../claims.d/CLAIM-392.md).
- [QUESTION-291](../questions.d/QUESTION-291.md), split from [QUESTION-220](../questions.d/QUESTION-220.md) on 2026-10-27, Answered by
  [THEORY-743](../theory.d/THEORY-743.md), [THEORY-753](../theory.d/THEORY-753.md) and [THEORY-757](../theory.d/THEORY-757.md).
- [CLAIM-387](../claims.d/CLAIM-387.md), found by brute force in the reading of Equitz and Cover
  ([NOTE-988](../notes.d/NOTE-988.md)) and re-run, thesis, demonstrated, Active; second line
  formal-apparatus; corroborates [CLAIM-405](../claims.d/CLAIM-405.md) (distributed-agency).
- [CLAIM-392](../claims.d/CLAIM-392.md), computed in the reading of Charvin et al. ([NOTE-981](../notes.d/NOTE-981.md)) and
  re-run, thesis, demonstrated, Active; second line formal-apparatus. Its
  note of 2026-10-21 records that A2 and A5 proposed a paper on it and
  [CLAIM-387](../claims.d/CLAIM-387.md) that dropped three of its limits.
- [CLAIM-394](../claims.d/CLAIM-394.md), derived in the reading of Schüler and Wiskott ([NOTE-1015](../notes.d/NOTE-1015.md))
  and re-checked, thesis, demonstrated, Active; lines distributed-agency,
  formal-apparatus and, since the sweep of 2026-11-10, learned-structure.

## Links tested as claims

None is filed.

- **Non-nesting makes a coarse-to-fine reading of an optimal learner
  wrong.** Stated: [QUESTION-220](../questions.d/QUESTION-220.md)'s reason, quoted above.
- **Where the record finds nesting, a fixed basis or tree imposes it,
  never optimality.** Each instance is stated ([QUESTION-217](../questions.d/QUESTION-217.md)'s commuting
  cases; [CLAIM-387](../claims.d/CLAIM-387.md) on [NOTE-676](../notes.d/NOTE-676.md)). As a general sentence it is false on the
  record: [THEORY-757](../theory.d/THEORY-757.md) proves nesting by optimality when Y is a function of
  X or both are binary ([QUESTION-291](../questions.d/QUESTION-291.md)).
- **[CLAIM-394](../claims.d/CLAIM-394.md) against [CLAIM-387](../claims.d/CLAIM-387.md): slow-feature spans nest, IB optima need
  not.** Held side by side in [QUESTION-217](../questions.d/QUESTION-217.md)'s body, which says the slow
  spans nest "by slowness" and are "a refinement order of spans, not of
  features". Their objectives differ, so the contrast is not a claim about
  either.

## Not stated on the record

- **Acquisition here and in [SYNTHESIS-034](SYNTHESIS-034.md).** [QUESTION-217](../questions.d/QUESTION-217.md)'s acquisition relation
  is [QUESTION-039](../questions.d/QUESTION-039.md)'s subject, and both cite [THEORY-086](../theory.d/THEORY-086.md) and the deep linear
  readings. Neither refines or names the other.
- **A condition on P(X, Y) for nesting**, and whether the loss from
  forcing it is always small ([QUESTION-220](../questions.d/QUESTION-220.md)).

## What it does not say

- That information-bottleneck optima generally fail to nest: [CLAIM-392](../claims.d/CLAIM-392.md)
  finds nesting for far-apart budgets in an uncertified scan, and
  [QUESTION-291](../questions.d/QUESTION-291.md) holds two classes where it always holds.
- That the loss from forcing nesting is large: 0.49% of the budget in the
  one case computed ([CLAIM-392](../claims.d/CLAIM-392.md)).
- That any learner acquires its representations in a refinement order.
- Anything with standing of its own.
