---
number: 98
status: Open
formerly:
- QUESTION-tmp2vbup
title: 'How do the cost of keeping a filed inferential structure current and the risk of reusing it after it has gone stale change when it is worth filing, and when does the second-occurrence rule fail in each direction?'
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Split under ADR-049 at the status review's ruling (the owner delegated
    these rulings). The answered part, when a structure is worth filing
    with staleness set aside and costs fixed and known, is
    QUESTION-tmpsyjy0, answered by CLAIM-303 and CLAIM-308. This question
    narrows to the remainder. The old title was "When is an inferential
    structure worth filing: when does the reconstruction it is expected to
    save outweigh the cost of filing it, keeping it current and the risk of
    reusing it after it has gone stale?"
tags:
- design-rationale
- epistemology
date: '2026-10-15'
line: nucleating-argument
refines:
- QUESTION-038
summary: >-
  The owner at U11: "the record could probably benefit from some content to the
  effect of computation-storage tradeoffs". A11 posed filing as a decision under
  uncertainty about future use. [QUESTION-038](QUESTION-038.md) asks how an anchor works. This asks
  when one is worth making.
---
<!-- inactive-ok-file: CLAIM-185 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-098: How do the cost of keeping a filed inferential structure current and the risk of reusing it after it has gone stale change when it is worth filing, and when does the second-occurrence rule fail in each direction?

## Why it is a question

A11 §4: "The original question is concerned with how anchoring works.
The new question asks when anchoring is worth doing." Filing an item is
worth it when the expected reconstruction it saves, and any decision it
improves, exceed its cost over its life. A11 named the sub-problems: which
ideas recur, which are expensive to reconstruct, which are likely to
change, and which become dangerous if reused unchecked.

It bears on the record's own rule that a thing gets a code the second
time it turns up ([ADR-032](../decisions.d/ADR-032.md)) and on the nucleation threshold of [CLAIM-185](../claims.d/CLAIM-185.md).
A11: "Repeated occurrence is potentially evidence of future reuse. But
frequency alone is not a sufficient filing rule: a rare,
expensive-to-reconstruct argument might deserve persistence more than an
often-repeated trivial observation." [CLAIM-303](../claims.d/CLAIM-303.md) states the trade. [CASE-088](../cases.d/CASE-088.md) is the
arithmetic of one case.

An answer would say what the second-occurrence rule approximates, and
when it fails in each direction.

## Note of 2026-11-18: split

The part answered with staleness set aside, under fixed known costs, is
[QUESTION-tmpsyjy0](QUESTION-tmpsyjy0.md): [CLAIM-303](../claims.d/CLAIM-303.md) answers it where reuse can be forecast and
[CLAIM-308](../claims.d/CLAIM-308.md) where it cannot. What stays open here is what the split child
leaves out: how upkeep and the risk of stale reuse move the threshold, and
when the second-occurrence rule files too early or too late ([CLAIM-630](../claims.d/CLAIM-630.md),
Proposed, bears on the second).
