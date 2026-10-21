---
status: Answered
title: 'Must the optimal representations of an information-bottleneck objective at two budgets be nested, so that the coarser optimum is a (possibly noisy) function of the finer?'
version: 1
tags:
- information-theory
- learning-theory
- representation-learning
date: '2026-10-21'
line: learned-structure
refines:
- QUESTION-220
summary: >-
  The yes-or-no part of [QUESTION-220](QUESTION-220.md), split off under [ADR-049](../decisions.d/ADR-049.md). No, for
  deterministic encoders ([CLAIM-387](../claims.d/CLAIM-387.md)) and for stochastic ones ([CLAIM-392](../claims.d/CLAIM-392.md)),
  on one four-state source with binary Y. Raising the budget can
  reorganize the optimum rather than split it. What condition on P(X, Y)
  guarantees nesting stays with [QUESTION-220](QUESTION-220.md).
answered_by:
- CLAIM-387
- CLAIM-392
---

# QUESTION-tmp5fsie: Must the optimal representations of an information-bottleneck objective at two budgets be nested, so that the coarser optimum is a (possibly noisy) function of the finer?

## Answer

No. Both halves rest on one source: X uniform on four states, Y binary
with P(Y=1|x) = (0, 0, 1/8, 3/8). A single counterexample answers a
"must" question, and [QUESTION-220](QUESTION-220.md)'s own "what would count" accepts "a
small discrete distribution whose optima at two budgets are incomparable
partitions".

- **Deterministic encoders.** [CLAIM-387](../claims.d/CLAIM-387.md) (Active, demonstrated), by
  enumerating the partitions. The optimum is {0,1,2 | 3} for
  6.91 < β < 9.26 and {0,1 | 2,3} for 9.26 < β < 16.06. Neither refines
  the other, and they are not even laminar, so no fixed tree holds both.
- **Stochastic encoders.** [CLAIM-392](../claims.d/CLAIM-392.md) (Active, demonstrated). The unique
  optima at β = 8 and β = 12 fail [THEORY-753](../theory.d/THEORY-753.md)'s hull test, so no Markov
  chain X → T₂ → T₁ joins them.

**The caveat on the second half.** [CLAIM-392](../claims.d/CLAIM-392.md)'s certificate of optimality
and uniqueness is a fine grid with local search, not interval arithmetic.
Its warrant is `demonstrated`, but a sharper certificate would make it a
theorem. If that certificate failed, the stochastic half would reopen
here, as [ADR-049](../decisions.d/ADR-049.md) provides.

## What it leaves to [QUESTION-220](QUESTION-220.md)

When nesting does hold. [THEORY-757](../theory.d/THEORY-757.md) gives two special cases, Y a function
of X and both binary. [QUESTION-220](QUESTION-220.md) keeps the structural condition on
P(X, Y), how large the loss from forcing nesting can be (0.49% of the
budget here), and whether [THEORY-163](../theory.d/THEORY-163.md)'s annealed colour hierarchy nests.
