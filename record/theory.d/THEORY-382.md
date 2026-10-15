---
number: 382
status: Proposed
formerly:
- THEORY-tmpqvlyg
promote_when: >-
  An analysis bounding the response time of OVIS(θ), or of any rule of its
  kind, against the best plan that meets the same freshness threshold (the
  best fixed plan, or an offline optimum over the same access and update
  streams), or a measurement on a real server or recorded web workload that
  compares it with that best plan. More synthetic simulations in which OVIS
  lies between all-materialized and caching-only cannot settle it: that is
  what is already held, and it says nothing about how far from the best plan
  OVIS is.
title: "When a web server keeps each page fragment either cached and invalidated by updates or stored and refreshed after them, materializing trades staleness for response time, and in one synthetic simulation with fixed costs a periodic greedy that moves a capped number of fragments between the two, to keep the share of fresh fragments served above a set threshold, held freshness near the threshold, answered faster than caching alone and recovered from overload by materializing everything; no bound on its distance from the best plan is shown"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1105
answers:
- QUESTION-114
summary: >-
  Labrinidis and Roussopoulos (2003), [LIT-1105](../literature.d/LIT-1105.md), read in [NOTE-911](../notes.d/NOTE-911.md). Quality
  of Data is the share of fresh fragments in served pages; OVIS(θ) estimates
  per fragment the change in response time (hits and misses against refresh
  load) and in QoD from switching policy, and each period greedily switches up
  to MAX_CHANGE fragments to spend a QoD surplus on speed or buy back a
  deficit. The paper asserts the greedy step is best under the cap and proves
  nothing; the evidence is one simulator with uniform costs and no comparison
  with an optimum. The reading the evidence does not support: that this is a
  joint cost model of build, upkeep, staleness and savings. Staleness is a
  user-set threshold, not a price, and switching and storage are free.
---

# THEORY-382: When a web server keeps each page fragment either cached and invalidated by updates or stored and refreshed after them, materializing trades staleness for response time, and in one synthetic simulation with fixed costs a periodic greedy that moves a capped number of fragments between the two, to keep the share of fresh fragments served above a set threshold, held freshness near the threshold, answered faster than caching alone and recovered from overload by materializing everything; no bound on its distance from the best plan is shown

## Source

Labrinidis and Roussopoulos (2003), [LIT-1105](../literature.d/LIT-1105.md), VLDB 2003, pp. 393–404, read
in full in [NOTE-911](../notes.d/NOTE-911.md) from the VLDB Endowment's copy (OCR of a bitmap-font PDF,
formulas and pseudo-code read from page images). The 2004 journal version was
not read.

## What was actually shown

**The trade.** A cached fragment is recomputed on the next request after an
update; a materialized one is refreshed in the background and served from the
cache even while its refresh is pending. "View materialization is an
attractive solution as it decouples the serving of access requests from the
handling of updates." The price is staleness while refreshes queue.

**The metric and the problem.** "Definition 2: Quality of Data (QoD) for
data-intensive web servers is the average freshness of the served web pages",
a page's freshness being the weighted share of its fragments that are fresh
(binary each) at access time. The problem: maximize performance (mean response
time) while QoD stays at least θ, with an infinite cache.

**The cost model.** Not materialized: H_r·N_acc·A_hit + (1 − H_r)·N_acc·A_miss.
Materialized: N_acc·A_hit + R_r·N_upd·U_mat. Query savings and upkeep share one
unit and are summed per fragment; switching costs nothing.

**The algorithm.** Each period, with surplus Q > θ, materialize fragments in
order of largest estimated speed gain while the estimated QoD stays above θ;
with deficit, stop materializing in order of largest QoD gain until it is
covered; at most MAX_CHANGE switches per period. On detected backlog,
materialize everything.

**The evidence.** osim, 500 fragments, Zipf-like accesses, uniform updates,
costs fixed at 150 ms (update, refresh) and 10 ms (cache hit), runs of 2400 s.
OVIS(0.925) climbed from all-materialized to θ and stayed near it; with 0.90
its QoD was lower ("OVIS seems to track the specified QoD threshold"). Caching
alone had response times "up to ten times worse than OVIS", and under a heavier
workload saturated, ending three orders of magnitude slower; OVIS(0.875)
detected the lag and reset to all-materialized.

## What this does not say

- **That OVIS is near optimal.** The greedy's optimality under the cap is
  asserted; choosing by speed gain alone ignores each fragment's QoD cost.
  No run compares OVIS with the best fixed plan or any optimum.
- **That staleness is priced.** θ is chosen by the application. No stale read
  has a cost, and age or error size do not enter the metric.
- **That build cost, switching cost or space are handled.** All are absent.
- **That the per-fragment estimates are right.** They ignore that refresh load
  from one fragment delays others through the shared queue; the panic rule is
  how the algorithm copes when that bites.
- **That it holds on real systems.** One simulator, uniform costs, no repeated
  runs, and no sensitivity analysis of MAX_CHANGE, period or lag thresholds.

## Connections

- For [QUESTION-114](../questions.d/QUESTION-114.md) it is the first held reading with staleness, upkeep and
  query savings on one online schedule, but it is not the joint model.
  [THEORY-332](THEORY-332.md) (Bruno and Chaudhuri) has build cost and no staleness; this has
  staleness and no build cost. Neither contains the other.
- It mirrors [THEORY-350](THEORY-350.md): Gupta and Mumick budget upkeep and minimize query
  cost; this budgets staleness and puts upkeep in the objective.
- [THEORY-348](THEORY-348.md) forbids stale reads; this permits them up to a share.
- Its predecessor, [LIT-1118](../literature.d/LIT-1118.md) ([THEORY-383](THEORY-383.md)), assumed no staleness and left
  selection unsolved.
- For [CLAIM-303](../claims.d/CLAIM-303.md) the invalidate-and-rebuild-on-use policy is a third option
  beside filing with upkeep and reconstruction, and staleness appears as the
  share of uses served stale, not as the cost of a stale use.
