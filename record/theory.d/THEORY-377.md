---
number: 377
status: Proposed
formerly:
- THEORY-tmph9339
promote_when: >-
  A proof that, under stated processes for value changes and query precision
  demands, the width set by the widen-on-push, narrow-on-fetch rule converges
  (in distribution or in time-average cost) to within a stated factor of the
  best fixed width, or a trace study on data other than the authors' that
  measures its cost against the best fixed width and against an adaptive
  cache-or-not rule. Further simulations on random walks, or results on the
  authors' own traces, do not settle it.
title: "A rule that multiplies a cached interval's width by 1 + α on a pushed refresh with probability min{ρ, 1}, and divides it by 1 + α on a query's exact fetch with probability min{1/ρ, 1}, came within 1% to 5% of the best fixed width on simulated random walks; on network-traffic traces, restricted to exact copies, it matched an adaptive cache-or-not rule, and where queries tolerated imprecision it cost less; that it converges to the best width is argued, not proved"
version: 1
tags:
- databases
- operations-research
date: '2026-10-15'
source:
- LIT-1109
answers:
- QUESTION-114
extends:
- THEORY-386
summary: >-
  Olston, Loo and Widom (2001), [LIT-1109](../literature.d/LIT-1109.md), read in [NOTE-912](../notes.d/NOTE-912.md). The rule
  treats a pushed refresh as "too narrow" and a fetch as "too wide", weighted
  by ρ = 2C_vr/C_qr, and needs no measurement of update rates, query rates or
  precision demands. Within 1% of the best fixed width on one random walk and
  within 5% over eight settings; with α = 1 and thresholds it tracked a
  50-host traffic trace. With every copy forced exact it decided cache-or-not
  as well as an adaptive exact-caching rule, and did better where imprecision
  was allowed, except with a small cache. Convergence is argued from the
  balance condition only, all evidence is the authors' simulation, and there
  is no worst-case guarantee.
---

# THEORY-377: A rule that multiplies a cached interval's width by 1 + α on a pushed refresh with probability min{ρ, 1}, and divides it by 1 + α on a query's exact fetch with probability min{1/ρ, 1}, came within 1% to 5% of the best fixed width on simulated random walks; on network-traffic traces, restricted to exact copies, it matched an adaptive cache-or-not rule, and where queries tolerated imprecision it cost less; that it converges to the best width is argued, not proved

## Source

Olston, Loo and Widom (2001), [LIT-1109](../literature.d/LIT-1109.md), SIGMOD 2001, read in full in
[NOTE-912](../notes.d/NOTE-912.md): Section 2 (the rule), Sections 4.2–4.7 (the simulations).

## What was actually shown

**The rule.** At each refresh the source sets the next width. After a
value-initiated refresh, with probability min{ρ, 1}, W′ = W·(1 + α); after a
query-initiated one, with probability min{1/ρ, 1}, W′ = W/(1 + α). Widths below
τ₀ are sent as exact and widths at or above τ∞ as uncached; the source keeps
the unthresholded width. The aim is the balance ρ·P_vr = P_qr of [THEORY-386](THEORY-386.md),
found from refresh events alone. The paper's argument: "our algorithm adapts to
always move W toward the optimal width W*". No theorem on convergence, its
rate or its stationary behaviour is given.

**Steady state, simulated.** One value on a random walk: the rule settled at
W = 3.11, "within 1% of the optimal W*"; over T_q ∈ {1, 2}, δ_avg ∈ {10, 20},
ρ ∈ {1, 4}, within 5%.

**Dynamic data, simulated.** A two-hour wide-area trace, 50 hosts, SUM or MAX
over 10 random sources per query, with ρ ∈ {1, 4}. α = 1 worked well overall.
τ₀ should be a small constant below the smallest meaningful precision demand;
τ∞ = ∞ for mixed demands, τ∞ = 0 for SUM workloads that need exact answers.
Uncentred intervals, widths growing with time, and decisions from the last r
refreshes did no better.

**Exact caching as the endpoint.** With τ∞ = 0 every copy is exact or absent,
and the rule "almost precisely matches" an adaptive cache-or-not algorithm
derived from Wolfson, Jajodia and Huang, whose window was tuned per run, across
query periods, cache sizes 50 and 20, and ρ ∈ {1, 4}. With τ∞ = ∞ it cost
markedly less for workloads tolerating imprecision, slightly more for exact
SUM workloads, and much less for MAX; with a cache of 20 the gain mostly went.
Adapted to update-count staleness, it did modestly better than Divergence
Caching.

## What this does not say

- **That it converges, or how fast.** The balance argument says where the
  optimum is, not that a randomized multiplicative walk on W reaches it or
  stays near it. The evidence is simulation.
- **That it is near-optimal against an adaptive optimum.** The benchmark is the
  best fixed width, or another adaptive heuristic, never a hindsight optimum
  over changing widths. No competitive ratio is given.
- **That the evidence is independent.** One random-walk model, one trace,
  query loads of the authors' design, all run by the authors.
- **That staleness is priced beyond messages.** As in [THEORY-386](THEORY-386.md), validity is
  guaranteed by the source, and wrong or imprecise answers cost nothing.
- **Anything about build cost, stored answers or space** beyond evicting the
  widest intervals.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): a forecast-free rule for how much staleness to tolerate,
  driven by counting the two kinds of refresh, which reduces to deciding
  whether to keep a copy at all.
- [THEORY-348](THEORY-348.md) and [CLAIM-308](../claims.d/CLAIM-308.md): in the exact case the rule is in the same family
  as the break-even rule, a decision from counted events with no forecast, but
  its support is an expected-cost balance and a simulation, not a worst-case
  ratio, so it neither adds to nor weakens the "within 2" guarantee.
- [THEORY-332](THEORY-332.md): Bruno and Chaudhuri's tuner also adapts from observed events
  without a forecast, with build cost and no staleness; this has staleness and
  no build cost.
- [CLAIM-303](../claims.d/CLAIM-303.md): a filed item could carry a tolerance adjusted the same way,
  loosened when upkeep fires and tightened when a use needs more, if something
  watched its premises.
