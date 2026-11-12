---
number: 107
status: Proposed
formerly:
- TERM-tmp46hcg
title: 'organizational slack: resources an organization holds beyond what its current output requires, some useful and some wasteful, which the output alone does not tell apart'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Provenance only: NOTE-1576, NOTE-1577 went to Read in the
    twenty-ninth status review, so "skimmed in" becomes "read in" (2
    places). The sense is unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Now draws on THEORY-1401 ("The definition is Bogetoft and
    Hougaard's"), THEORY-1421 ("Slack held idle for an uncertain need")
    and THEORY-1416 ("Headroom that is busy"). First application of
    draws_on (ADR-095). No other change.
tags:
- society-and-governance
- operations-research
- agency
date: '2026-11-04'
line:
- readiness
summary: >-
  Filed at the owner's request on 2026-11-04, to account for an idea the
  readings of the pasted bibliography on emergency readiness surfaced and
  the record lacked: no held entry concerned organizational slack, and the
  readers' searches for it returned nothing. Its sources are Bogetoft and
  Hougaard ([LIT-2096](../literature.d/LIT-2096.md)), from whom the definition comes; Bogetoft and
  Kerstens ([LIT-2076](../literature.d/LIT-2076.md), Unfetched; abstract only), who pose useful
  against wasteful slack as the problem; Liebman and Mahoney
  ([LIT-2028](../literature.d/LIT-2028.md)), whose precautionary buffer is slack held for uncertain
  needs; and van Leeuwaarden and colleagues ([LIT-2059](../literature.d/LIT-2059.md)), standing in
  for Halfin and Whitt, whose headroom is spare capacity that is busy, not
  held idle. The wording is the filer's; adopting it is the owner's call.
draws_on:
- THEORY-1401
- THEORY-1421
- THEORY-1416
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision this entry's history note of 2026-11-12 applies -->
<!-- inactive-ok-file: LIT-2076 — Unfetched; cited for its published abstract, nothing here rests on it -->
<!-- inactive-ok-file: LIT-2085 — Unavailable; Halfin and Whitt, cited through the neighbour that stands in for it -->
<!-- inactive-ok-file: TERM-113 — Proposed; terms of the same filing, cited as filed -->
<!-- inactive-ok-file: THEORY-1421 — Proposed; the readings' accounts, cited as filed, nothing here rests on their being settled -->
<!-- inactive-ok-file: CASE-200 — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->

# TERM-107: organizational slack: resources an organization holds beyond what its current output requires, some useful and some wasteful, which the output alone does not tell apart

## Definition

**Organizational slack** is the part of an organization's resources
beyond what its current output requires: its inputs minus the least
inputs that would produce the same output. The definition is Bogetoft and
Hougaard's ([LIT-2096](../literature.d/LIT-2096.md), read in [NOTE-1576](../notes.d/NOTE-1576.md); [THEORY-1401](../theory.d/THEORY-1401.md)), after
Cyert and March: "organizational slack can be interpreted as the
existence of excess resources to produce a given output". Measured against
output, slack is what an efficiency analysis calls technical inefficiency.

The term's job is to hold open the question that word closes. Slack
measured against current output is the same quantity whether it is waste
or a reserve, because what a reserve is for is not in the current output.
So the term names the quantity and leaves the verdict to a further test:

- **Useful slack** has a use the output measure leaves out. The motives
  Bogetoft and Kerstens's abstract lists ([LIT-2076](../literature.d/LIT-2076.md), unread) are that it
  may "serve as a buffer against environmental shocks", decouple units,
  ease planning, support innovation and allow responses to competitors.
- **Wasteful slack** has none: by their Pareto criterion, "If an
  organization can maintain the same levels of output and slack at lower
  cost, there is wasteful or nonrationalizable spending."

They state the problem the term leaves open: "We acknowledge that slack
may be both useful and wasteful. The challenge is how to separate the
two." Bogetoft and Hougaard: "The distinction between valuable and
non-valuable waste is a challenging one." Against both, "the economic
literature tends to view slack as wasteful".

## Two kinds of reserve the readings separate

- **Slack held idle for an uncertain need.** Liebman and Mahoney
  ([LIT-2028](../literature.d/LIT-2028.md), [NOTE-1553](../notes.d/NOTE-1553.md); [THEORY-1421](../theory.d/THEORY-1421.md)): under uncertain future needs,
  "organizations have an incentive to hold back on marginal spending early
  in the budget cycle and then burn through this buffer-stock at the end
  of the year." A short rollover keeps the reserve useful, "maintaining
  sufficient precautionary balances to respond to emergency spending
  needs", and removes the wasteful spending of it at expiry. The same
  balance is useful slack until the deadline and becomes wasteful at it,
  by a rule of the budget, not by anything in the organization.
- **Headroom that is busy.** The square-root staffing rule
  ([LIT-2059](../literature.d/LIT-2059.md), read in [NOTE-1577](../notes.d/NOTE-1577.md), standing in for Halfin and Whitt,
  [LIT-2085](../literature.d/LIT-2085.md); [THEORY-1416](../theory.d/THEORY-1416.md)) sizes servers above mean load by a margin of
  the order of the load's fluctuations. Its spare capacity is in use
  nearly all the time, and large pooled systems need proportionally less
  of it. That is slack against mean output, not a reserve held idle for a
  rare contingency, and the term should not be read as implying one.

## What it is not

- **Operational availability** ([TERM-055](TERM-055.md)): the chance a resource is
  deployed for a task by a deadline. Slack is a stock, measured against
  output, and says nothing about whether it can be deployed in time.
  Bogetoft and Kerstens's test values slack as held, not as deployed.
- **Redundancy as reliable coverage** (see the coverage term filed the
  same day, [TERM-113](TERM-113.md)): several units placed over one demand so that one
  is free with a stated probability. That is a reason slack can be useful,
  not the slack itself.
- **Scenario-conditioned readiness** (A's term, [TERM-115](TERM-115.md)): a
  probability of effective response to an imposed contingency. Slack is
  one input to it; the question of telling a warranted reserve from
  wasteful redundancy is A's [QUESTION-395](../questions.d/QUESTION-395.md), which this term gives a
  word to and does not answer.

## What would settle it

A claim of the record's own stated in it, or a reading of Bogetoft and
Kerstens that shows their test separates the two kinds of slack on data.
Adopting it is the owner's call.

## Note of 2026-11-05: slack that is a reconfiguration reserve

[TERM-106](TERM-106.md) refines this term. In [CASE-200](../cases.d/CASE-200.md) the 0.3 a budget leaves unspent is slack against current output and is exactly what makes a transition possible, a use that output alone cannot show. No status changes.

## Note of 2026-11-06: Bogetoft and Hougaard, read in full

The full reading ([NOTE-1576](../notes.d/NOTE-1576.md) v2) supports the definition and sharpens it. Bogetoft and Hougaard's slack is s = x − z for any feasible plan z with z ≤ x. With several inputs it is therefore a set, the "slack possibility set" S(x) (§2, pp. 7–8), not the difference from one least input vector. Which point of the set a unit takes is what their regimes and value function decide. The Cyert and March quotation is theirs, verbatim (§1, p. 4). [THEORY-1401](../theory.d/THEORY-1401.md) is now Active. No status changes.
