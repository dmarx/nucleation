---
number: 467
status: Proposed
formerly:
- CLAIM-tmpocjxw
title: 'Under full-information, independent audits, a learned allocation of influence among specialists is no better than a contextual router trained on the same audits, which is a mixture of experts whose experts earn responsibility by fitting better; whatever governance adds over routing has to be shown where evaluation fails, and the record has not yet found such a regime'
version: 2
history:
- version: 2
  date: '2026-10-28'
  note: >-
    complements CLAIM-278 becomes undercuts ARG-tmpvyhbs: under
    ADR-061 CLAIM-278 moved to that argument, from the lab's
    restricted models to CLAIM-286, and this claim, a claim about
    the subject matter, defeats it for one model class. The claim is
    unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A run of CASE-158's design, with the router given the same audit delay
  and cost, in which audited governance has lower held-out error than the
  router under full-information, independent audits; that would show
  governance using something a router trained on the audits cannot.
tags:
- self-governance
- learning-theory
- complex-systems
date: '2026-10-27'
line:
- distributed-agency
answers:
- QUESTION-271
grounds:
- CASE-158
- CASE-162
- THEORY-937
undercuts:
- ARG-tmpvyhbs
summary: >-
  The prediction [CASE-158](../cases.d/CASE-158.md) states ("Under full information, governance
  should not beat it") and held by no claim, found in the audit of
  2026-10-27; the runs were reported in [CASE-158](../cases.d/CASE-158.md) and reproduced in
  [CASE-162](../cases.d/CASE-162.md), where the router had the lower error in all four cells,
  selective and captured audits included. It gives [CLAIM-278](CLAIM-278.md)'s objection a
  definite form for this model class. The edge: it bounds governance by
  routing under full information; it does not say governance never helps,
  and the regimes where it might ([QUESTION-271](../questions.d/QUESTION-271.md)'s four failures) are
  untested or, so far, lost.
---

# CLAIM-467: Under full-information, independent audits, a learned allocation of influence among specialists is no better than a contextual router trained on the same audits, which is a mixture of experts whose experts earn responsibility by fitting better; whatever governance adds over routing has to be shown where evaluation fails, and the record has not yet found such a regime

## The claim

[CASE-158](../cases.d/CASE-158.md), "What the record predicts": "A router trained on the same audits
is a mixture of experts whose experts earn responsibility by fitting
better ([THEORY-937](../theory.d/THEORY-937.md)). Under full information, governance should not beat
it." The reason is that with every proposal audited and the audits
independent, governed reallocation and a learned router are both fitting
the allocation to the same signal, and the router does it directly.

The runs agree. A47's reported results, reproduced in the lab ([CASE-162](../cases.d/CASE-162.md),
v1.1): mean post-reversal error 0.02237 for the router against 0.02546
for governance with independent, full audits. In the same table the
router also had the lower mean error under selective audits (0.03284
against 0.03477) and under 80% capture (0.0448 and 0.0438 against 0.0697
and 0.0698), though under selective, independent audits governance
recovered on 7 of 12 seeds and the router on 4.

So the first half, the bound under full information, is predicted and
observed. The second half is what [CASE-158](../cases.d/CASE-158.md) says would make the design
informative: arms in which evaluation fails as [QUESTION-271](../questions.d/QUESTION-271.md) lists, with
cycles, no common scale, capture and bandit feedback. Two of those
(selective and captured audits) have been run in one form, and governance
did not win on mean error. [CLAIM-278](CLAIM-278.md)'s objection, that the framework adds
vocabulary and not prediction, stands for this model class until one does.

## What it does not say

- **That governance never helps.** Cycles and incommensurable criteria are
  untried, and so is the entrenchment loop with competence that grows.
- **That the router saw only what governance saw.** [CASE-158](../cases.d/CASE-158.md)'s caveat: A47
  did not say whether its router faced the same audit delay and cost;
  [CASE-162](../cases.d/CASE-162.md) reports a check with the delay matched, in which the router
  still won, but the case calls the design's information-matching a
  condition of every future arm.
- **Anything about organizations.** Specialist denoisers in a lab.
