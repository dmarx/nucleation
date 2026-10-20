---
number: 212
status: Open
formerly:
- QUESTION-tmp4627m
title: "Does a one-off random shock to a prediction-market price persist for weeks on other platforms and at real-money stakes, and do the traders come to believe the shocked price?"
version: 1
tags:
- social-science
- epistemology
date: '2026-10-20'
line: distributed-agency
refines:
- QUESTION-047
summary: >-
  Filed when the promotion audit (batch 050, [ADR-047](../decisions.d/ADR-047.md) v3) narrowed and
  promoted [THEORY-267](../theory.d/THEORY-267.md) to what Rasooly and Rozzi measured on Manifold. The
  former promote_when asked for a second randomised experiment elsewhere,
  or a design that measures traders' beliefs; this question holds it.
---

# QUESTION-212: Does a one-off random shock to a prediction-market price persist for weeks on other platforms and at real-money stakes, and do the traders come to believe the shocked price?

## Why it is a question

[THEORY-267](../theory.d/THEORY-267.md) now states one measurement. In a pre-registered randomised
field experiment on 817 Manifold markets ([LIT-958](../literature.d/LIT-958.md), read in [NOTE-778](../notes.d/NOTE-778.md)), about
59% of a ±5-point shock that no trader's information supported was still
in the price after 60 days in unresolved markets. Reversion was about 25%
in the first week and slowed afterwards. That is one platform, play money
redeemable as charity, and one shock size. The small real-money follow-up
reverted faster and ran a week. The paper's model gets partial persistence
from finite, risk-averse traders even when no one learns from the price,
but the data cannot tell that from learning. So two things are open:
whether the persistence holds beyond Manifold, and whether the persisting
price is something the traders came to believe, which is what bears on
[QUESTION-047](QUESTION-047.md).

## What would answer it

For the first part, a second randomised manipulation experiment on a
different prediction market, preferably a real-money one with larger
markets. It is answered yes if most of a one-off random shock is still
present after several weeks, and no if the price returns within days. For
the second part, a design that measures traders' beliefs before and after
the shock and shows whether the persistence comes from learning from the
price or from limited rebalancing. More simulations of the authors' model
cannot settle either part. Nor can observational studies of historical
manipulation attempts, which have no counterfactual price path.
