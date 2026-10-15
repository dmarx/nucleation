---
number: 303
status: Proposed
formerly:
- CLAIM-tmpygqjz
title: 'Filing an argument moves work across time: it is paid for now, in filing,
  indexing, tracking dependencies and checking it is still current, against reconstruction
  later, so it is worth its cost only when expected reuse covers it, and recurrence
  is evidence of reuse, not the criterion'
version: 1
role: thesis
defeated_if: >-
  A record in which the second-occurrence rule is shown to file at least as well
  as any rule using estimates of reconstruction cost and staleness, so that recurrence
  is the criterion and not merely evidence for it. Or an accounting of the record's
  own filings in which upkeep and stale reuse are negligible, so that only the reuse
  count matters.
tags:
- design-rationale
- epistemology
date: '2026-10-15'
line: nucleating-argument
answers:
- QUESTION-098
complements:
- CLAIM-185
- CLAIM-182
summary: >-
  A11, at the owner's request for "content to the effect of computation-storage
  tradeoffs". A11's four expenditures (materialization, indexing, dependency tracking,
  refresh) and its break-even condition. The arithmetic is trivial. The thesis is
  about the record: that its second-occurrence rule ([ADR-032](../decisions.d/ADR-032.md)) and the nucleation
  threshold of [CLAIM-185](CLAIM-185.md) are approximations to this trade, and can fail in both
  directions.
illustrated_by:
- CASE-088
objected_by:
- CLAIM-308
---
<!-- inactive-ok-file: CLAIM-182 CLAIM-185 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-303: Filing an argument moves work across time: it is paid for now, in filing, indexing, tracking dependencies and checking it is still current, against reconstruction later, so it is worth its cost only when expected reuse covers it, and recurrence is evidence of reuse, not the criterion

## The claim

A11: "Memory does not merely preserve information. It allocates work
across time. Filing an argument performs computation now to avoid
uncertain future reconstruction; indexing makes the result accessible;
dependency tracking makes it revisable; verification manages the risk of
reusing stale conclusions."

For a fixed workload: upfront cost F, reconstruction c_r per use, access
and verification c_a per use, upkeep u per use, n uses. Filing is cheaper
when F + n(c_a + u) < n·c_r, that is, when c_r > c_a + u and
n > F/(c_r − c_a − u). [CASE-088](../cases.d/CASE-088.md) works one case. A11 added the term that makes
this more than caching: "the cost of incorrectly reusing an obsolete
argument may exceed the cost of recomputing it", and "persistence can
preserve errors as efficiently as valid discoveries."

## What it bears on

[ADR-032](../decisions.d/ADR-032.md) files a thing the second time it turns up, as a throttle on
capture by agents. A11 reads recurrence as evidence of reuse: "But
frequency alone is not a sufficient filing rule: a rare,
expensive-to-reconstruct argument might deserve persistence more than an
often-repeated trivial observation." [CLAIM-185](CLAIM-185.md) calls the threshold
"whatever makes a structure persist"; this says what makes persisting
worth it. [CLAIM-182](CLAIM-182.md) is not touched: A11's null case, an argument filed for
20 units that never recurs, is an anchor that works and does not pay.

## What it does not say

- Not that the record's filing pays off. A11: "I would keep that last
  statement as a proposed economic account of nucleation, not an
  established explanation of how this particular repository performs."
- Not that saved effort is better reasoning. A filed answer to an
  objection can be wrong, and can stop being right.
