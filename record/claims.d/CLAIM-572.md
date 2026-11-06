---
number: 572
status: Proposed
formerly:
- CLAIM-tmpcyj43
title: 'When observing and acting draw on one budget, the cheapest readiness always buys a whole prefix of the probes and stops where a probe lowers the response budget, the splits a fixed budget affords can be disconnected, so shifting resources gradually from response to observation can pass through splits that are not ready, and stopping when the next probe does not pay can miss the optimum'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: under nested probe families and a fixed
  standing posture, a system whose least total budget o + a* is reached
  only strictly between two probe costs; or a proof that the affordable
  splits at a fixed budget always form one interval; or that buying
  probes one at a time while each lowers the total always reaches the
  least total. Not defeated by probes that are not nested, by acting that
  also informs (dual control), or by more than one decision, which the
  claim excludes.
tags:
- society-and-governance
- mathematics
- epistemology
date: '2026-11-05'
line:
- readiness
- realizability
- formal-apparatus
rests_on:
- CLAIM-535
- CLAIM-570
- CLAIM-574
complements:
- CLAIM-592
- CLAIM-561
grounds:
- CASE-206
bears_on:
- QUESTION-374
summary: >-
  The assistant's, on the owner's request of 2026-11-05 to investigate
  organizations whose observing and acting draw on one budget. Take
  [CLAIM-535](CLAIM-535.md)'s single decision and give both halves a cost. The
  organization stands in a posture; each circumstance has acceptable
  configurations, each reachable from the posture at some cost; probes
  bought in a fixed order refine what it can tell apart. The acting
  budget it needs, a*(o), is the largest, over what it cannot tell apart
  at o, of the cheapest configuration acceptable throughout. With
  o + a ≤ B, three things follow. The least total is reached at a probe
  cost, never between. The affordable splits can fall apart into
  separate intervals: an organization moving money from response to
  intelligence can pass through splits where it has paid for observation
  it cannot yet use and given up response it still needs. And a probe's
  worth depends on the probes after it, so stopping when the next one
  does not pay misses the least total in about a quarter of random
  systems. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-570 CLAIM-592 CLAIM-561 CASE-206 — Proposed or Open in this pull request, cited as open -->

# CLAIM-572: When observing and acting draw on one budget, the cheapest readiness always buys a whole prefix of the probes and stops where a probe lowers the response budget, the splits a fixed budget affords can be disconnected, so shifting resources gradually from response to observation can pass through splits that are not ready, and stopping when the next probe does not pay can miss the optimum

## The model

[CLAIM-535](CLAIM-535.md)'s setting, with costs on both halves.

- **Circumstances and responses.** Circumstances w ∈ W. For each w, a set
  A(w) of acceptable configurations of the organization.
- **Acting.** The organization stands in a posture x₀. Reaching
  configuration y costs r(y), for instance the peak cost of the cheapest
  path from x₀ ([CLAIM-581](CLAIM-581.md)).
- **Observing.** Probes are bought in a fixed order at cumulative costs
  0 = c₀ < c₁ < … < c_k. Each refines the partition of W into what the
  organization cannot tell apart, so the partitions are nested
  ([CLAIM-574](CLAIM-574.md)).
- **Readiness at (o, a).** For every class C of the partition bought with
  o, some configuration acceptable throughout C is reachable within a.
- **The response budget.** The least such a is

    a*(o) = max over classes C of min{r(y) : y ∈ ∩_{w ∈ C} A(w)},

  infinite when some class has no common acceptable configuration. With
  zero costs this is [CLAIM-535](CLAIM-535.md)'s criterion.

One budget: o + a ≤ B.

## The claim

1. **a\* falls in steps at the probe costs.** Finer classes have larger
   common acceptable sets ([CLAIM-535](CLAIM-535.md)'s refinement), so a\*(o) does not
   rise with o. It is constant between consecutive probe costs, because the
   partition is.
2. **The least total is at a probe cost.** B\* = min over i of
   c_i + a\*(c_i). On [c_i, c_{i+1}) the total o + a\*(o) rises with o, so
   observing budget that buys no further probe is pure loss. The
   organization's cheapest readiness buys a whole prefix of the probes.
   B\* is finite at i = 0 exactly when some configuration is acceptable in
   every circumstance, a hedge; its reach cost bounds B\*.
3. **The affordable splits can be disconnected.** At budget B the ready
   splits are the union over i of the intervals from c_i to
   min(c_{i+1}, B − a\*(c_i)). The union need not be one interval.
4. **Marginal reasoning fails.** A probe's contribution,
   a\*(c_{i−1}) − a\*(c_i) − (c_i − c_{i−1}), can be negative while a later
   probe's is large, because a probe may separate nothing that a common
   response cannot already cover until a later one completes the
   separation. Buying probes while each lowers the total can stop short of
   B\*.

## The worked cases

**Triage.** Three kinds of call, W = {1, 2, 3}. Each kind has its own
response, a, b or c, reachable at cost 1; a general response h is
acceptable for all three at cost 5. The first probe, at cost 1, asks
"is it kind 1?"; the second, at cost 1 more, separates 2 from 3.

| o bought | classes | a\* | o + a\* |
|---|---|---|---|
| 0 | {1, 2, 3} | 5 (h) | 5 |
| 1 | {1} {2, 3} | 5 (h for {2, 3}) | 6 |
| 2 | {1} {2} {3} | 1 | 3 |

B\* = 3, by observing fully. At B = 5 the ready splits are o = 0 and o in
[2, 4]; nothing between is ready. An organization at o = 0 that buys the
first probe sees its total rise and stops, at 5 instead of 3.

**The degree-4 vertex** ([CASE-206](../cases.d/CASE-206.md)), as self-individuation:
the "classes" are the vertex's own states, readiness is that everything the
observer identifies is mutually reachable ([CLAIM-570](CLAIM-570.md)'s up-set S), and
a\* is [CLAIM-570](CLAIM-570.md)'s a_S. With the probe costs 1, 2, 3, 4 of the case,
a_S = 1.866, 1.866, 1.866, 1.125, 0, so the totals are 1.866, 2.866,
3.866, 4.125 and 4. The least total, 1.866, is pure acting. At B = 4 the
ready splits are o in [0, 2.134] and o = 4: disconnected.

**Random systems.** Checked with python3 -I on 20,000 random systems of
three to six circumstances, three to seven configurations and one to four
nested probes: the formula for B\* matched a grid search every time; of the
16,180 with a finite B\*, 1,394 had disconnected ready splits at some budget
and 4,103 had greedy stopping short of B\*.

## What it adds

- **To readiness.** A budget split between knowing and responding is not
  a dial to turn smoothly. Its good settings are discrete (a probe
  prefix), can be far apart, and the path between them can pass through
  splits that are worse than either end. A reallocation of this kind is a
  transition with its own threshold, as in [CLAIM-571](CLAIM-571.md), but in budget
  space rather than configuration space.
- **To provisional dispatch** ([CLAIM-561](CLAIM-561.md)). Sending the general
  response early is the hedge at o = 0. Whether it is the cheapest
  readiness depends on the whole probe sequence, not on the next probe.
- **To [CLAIM-535](CLAIM-535.md).** With costs, there is no need to find the coarsest
  sufficient observation. The question is which point on the frontier
  between the two budgets is cheapest, and the answer can be no
  observation at all.

## What it does not say

- **One decision only.** It is not March's exploration and exploitation
  ([LIT-729](../literature.d/LIT-729.md)), which is about returns over time, and it says nothing of
  learning.
- **Acting does not inform.** In dual control (Feldbaum) an action also
  observes; that case is excluded, and its citation is unchecked
  ([CLAIM-535](CLAIM-535.md)).
- **Probes in a fixed order.** Choosing which probes to buy, not only how
  many, is a set-function problem the claim does not treat. The
  disconnection and the failure of greedy stopping already show in the
  fixed order.
- **Economics.** A non-concavity in the value of information is usually
  credited to Radner and Stiglitz; it is not registered here and the
  citation is unchecked. This claim's point 4 is of that family but is
  proved here only in this model.

## Note of 2026-11-05: the DNA origami readings, read across

The assistant's reading across the eight DNA origami readings filed on the owner's request to connect the record's inquiry to DNA origami. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

Two readings touch the shared budget, neither within its scope. Wagenbauer, Wachauf and Dietz ([NOTE-1637](../notes.d/NOTE-1637.md)) spent on a quality assay and used it to replace a 16-hour ramp with a 1.5-hour three-step schedule of matched quality, observing bought cheaper acting, but across experiments, not within one decision. Rothemund's AFM ([NOTE-1631](../notes.d/NOTE-1631.md)) is an observation that acts on the sample, the converse of the dual-control case the claim excludes, so there the split between the budgets is not even defined.

No status changes.
