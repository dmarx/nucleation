---
number: 489
status: Answered
formerly:
- QUESTION-tmpsyjy0
title: 'Setting staleness aside, under fixed known costs, when is an inferential structure worth filing?'
version: 1
tags:
- design-rationale
- epistemology
date: '2026-11-18'
line: nucleating-argument
refines:
- QUESTION-098
summary: >-
  The part of [QUESTION-098](QUESTION-098.md) the record has answered, split off under [ADR-049](../decisions.d/ADR-049.md)
  at the status review of 2026-11-18. Where reuse can be forecast, a
  structure is worth filing when expected reuse covers its cost, and
  recurrence is evidence of reuse ([CLAIM-303](../claims.d/CLAIM-303.md)). Where it cannot, file at the
  first use at which reconstructing again would take the overpayment past
  the cost of filing, within twice the hindsight optimum ([CLAIM-308](../claims.d/CLAIM-308.md)).
  Staleness, upkeep risk and when the second-occurrence rule fails stay
  with [QUESTION-098](QUESTION-098.md).
---

# QUESTION-489: Setting staleness aside, under fixed known costs, when is an inferential structure worth filing?

## Answer

Two Active claims answer it between them, one for each case of whether
future reuse can be forecast.

- **Reuse can be forecast.** [CLAIM-303](../claims.d/CLAIM-303.md) (Active, interpretive): filing moves
  work across time, paid for now against reconstruction later, so it is
  worth its cost only when expected reuse covers it. Recurrence is evidence
  of reuse, not the criterion.
- **Reuse cannot be forecast.** [CLAIM-308](../claims.d/CLAIM-308.md) (Active, demonstrated): recurrence
  weighted by reconstruction cost is then the criterion. Filing at the
  first use at which reconstructing again would take the overpayment past
  the cost of filing is within 2 − (c_a + u)/c_r of the hindsight optimum
  on every sequence of uses, and no deterministic rule without foresight
  guarantees materially better. The bound is re-derived in [CLAIM-308](../claims.d/CLAIM-308.md) and
  checked by scratch/formal/claim308_rent_or_buy_check.py.

## What it leaves to [QUESTION-098](QUESTION-098.md)

Both answers hold costs fixed and known, and leave staleness out: [CLAIM-308](../claims.d/CLAIM-308.md)
says so in its title, and [CLAIM-303](../claims.d/CLAIM-303.md) counts the cost of keeping a filing
current without giving a criterion for it. The risk of reusing a structure
after it has gone stale, and when the second-occurrence rule fails in each
direction ([CLAIM-630](../claims.d/CLAIM-630.md), Proposed), stay with the parent.
