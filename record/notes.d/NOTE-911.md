---
number: 911
status: Read
formerly:
- NOTE-tmpam1do
paper: LIT-1105
title: Labrinidis & Roussopoulos — Balancing performance and data freshness in web
  database servers
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the VLDB Endowment's own copy of the proceedings
    paper, https://www.vldb.org/conf/2003/papers/S13P01.pdf (12 pp., "Proceedings
    of the 29th VLDB Conference, Berlin, Germany, 2003" on the first page, no printed
    page numbers; Crossref gives pages 393–404 for DOI 10.1016/B978-012722442-8/50042-2,
    and the file's position in the session order fits). The directory lists files
    by session code only, so the file was identified by fetching candidates and
    reading their first pages; requests need a browser User-Agent. This is the 2003
    conference paper; the 2004 VLDB Journal version (10.1007/s00778-004-0131-7)
    was not read and nothing here comes from it. The PDF uses Type 3 bitmap fonts,
    so pdftotext returns nothing usable; the text was produced by OCR (tesseract,
    200 dpi) and every formula, the pseudo-code of Figures 6 and 7 and the experimental
    setup were read from page images (pages 4, 6 and 9 at 100 dpi, the rest checked
    against the OCR). Read: abstract, Sections 1–6, Figures 1–16 and the reference
    list. Nothing skipped. The plots carry no data tables, so results are described
    as the text states them and as the curves show, without numbers the paper does
    not give. Every quotation below was checked by script against the OCR text,
    with whitespace normalised and line-end hyphens joined, and the OCR of each
    quoted passage was compared with the page image.
date: '2026-10-15'
summary: >-
  The paper poses Online View Selection for a web server whose database takes updates
  while serving requests: choose, as the workload runs, which page fragments (WebViews)
  to keep stored and refreshed on every update and which to cache and invalidate,
  so as to minimize mean response time while the fraction of fresh fragments served
  (QoD) stays above a threshold θ. Its algorithm, OVIS(θ), estimates per fragment
  the response-time and QoD change of switching, and periodically switches up to
  MAX_CHANGE fragments greedily, spending a QoD surplus on speed or buying back
  a deficit; it materializes everything when it detects backlog. Nothing is proved:
  optimality of the greedy step is asserted, and the evidence is one synthetic simulation
  with fixed costs, in which OVIS kept QoD near θ, answered faster than caching
  alone, and recovered from overload. Upkeep and query savings share one cost, but
  staleness is a constraint set by the user, not a priced term, and build cost,
  switching cost and storage are absent.
---

# NOTE-911: Labrinidis & Roussopoulos — Balancing performance and data freshness in web database servers

## Contribution

The authors' SIGMOD 2000 paper ([LIT-1118](../literature.d/LIT-1118.md)) assumed no staleness and
left the per-page choice unsolved. This paper drops the first assumption
and gives an online answer to the second. "In the context of the Web,
selecting which views to materialize must be decided online and needs to
consider both performance and data freshness". It defines a freshness
metric (Quality of Data, QoD), states the Online View Selection problem,
gives the adaptive algorithm OVIS(θ), and tests it in a simulator (osim).

## Key insight

Caching with invalidation puts update handling on the path that serves
requests: every update makes the next request recompute. Materializing a
fragment, keeping it and refreshing it in the background, takes upkeep off
that path at the price of serving it stale while its refresh is queued.
"View materialization is an attractive solution as it decouples the
serving of access requests from the handling of updates." So the two
policies trade speed for freshness, and a server can choose a point on
that trade per fragment, moving fragments between policies as the observed
freshness rises above or falls below what the application will accept.

## Assumptions

- **Architecture.** An Asynchronous Cache (ASC) sits between application
  server and DBMS. Fragments are either non-materialized (cached, invalidated
  by updates, recomputed on the next request) or materialized (cached,
  refreshed after each update, always served from the cache). A virtual
  policy exists but is dropped: if invalidation is cheap, caching is "always
  a better policy than Virtual". The policy choice is the plan.
- **Infinite cache.** "In this paper we assume that the Asynchronous Cache
  module has infinite size and thus there is no need for a cache
  replacement algorithm". There is no storage term.
- **No build or switching cost.** Starting or stopping materialization of a
  fragment is not charged. The only limit on switching is MAX_CHANGE, a
  cap on how many fragments change per step, imposed for stability, not as
  a price.
- **Refresh by recomputation**, only of fragments derived directly from
  relations; HTML fragments composed from others are taken to cost nothing.
- **Single machine.** "Eq. 7 assumes that the cost of refreshing the
  materialized WebViews in the asynchronous cache will impact the response
  time of serving access requests." The authors say this holds when web
  server, ASC and DBMS share one machine.
- **Materialized fragments are served at a near-constant cost.** "We assume
  that the response time remains almost constant, since a Materialized
  WebView is served from ASC even when it is not fresh."
- **Freshness is binary per fragment.** A fragment is fresh at an access
  unless it is materialized and awaiting refresh, or non-materialized with
  an unapplied update to a parent relation. How long or how far it is out
  of date does not enter.
- **Workload is unknown and drifts**; access counts are forecast by
  exponential smoothing with gain 0.25 (Eq. 4, after Jacobson).

## Key results

- **Performance** is mean response time per request, measured at the web
  server (Definition 1).
- **Quality of Data.** "Definition 2: Quality of Data (QoD) for
  data-intensive web servers is the average freshness of the served web
  pages." A page's freshness is the weighted sum of its fragments' 0/1
  freshness, weights a_ij summing to 1 per page and 1/n_j by default
  (Eq. 2); QoD is the mean over the n requests in a window (Eq. 3). A
  threshold θ = 0.9 means "roughly 90% of the accesses must be served with
  fresh data".
- **Problem.** "in the presence of continuous access and update streams,
  dynamically select which WebViews to materialize, so that overall system
  performance is maximized, while the freshness of the served data (QoD) is
  maintained at an acceptable level." A plan is a 0/1 choice per fragment.
- **Per-fragment cost model.** Not materialized: cost = H_r·N_acc·A_hit +
  (1 − H_r)·N_acc·A_miss (Eq. 6), with hit ratio H_r estimated from periods
  when the fragment was not materialized, or set to 100% if there were none
  ("an optimistic estimate"). Materialized: cost = N_acc·A_hit +
  R_r·N_upd·U_mat (Eq. 7), with R_r the fraction of source updates that
  trigger a refresh (below 1 when refreshes are batched). QoD contribution:
  F_r·N_acc-a/n (Eq. 9), F_r the observed weighted freshness ratio under
  each policy. Differentials Δ_perf and Δ_QoD are the differences between
  the two policies' estimates (Eqs. 10–13). Costs are summed per fragment;
  interactions through the shared queue are not modelled.
- **OVIS(θ).** Passive mode collects statistics; at each period (a number
  of requests or a time interval) active mode compares observed QoD Q with
  θ. Surplus (Q > θ): among non-materialized fragments with Δ_perf < 0,
  materialize the one with the most negative Δ_perf while MAX_CHANGE is not
  reached and the surplus stays positive after subtracting its estimated
  QoD loss (Figure 6). Deficit (Q < θ): among materialized fragments with
  Δ_QoD > 0, stop materializing the one with the largest Δ_QoD until the
  estimated deficit is covered or MAX_CHANGE is reached (Figure 7). Warm-up
  and post-lag cool-down periods skip adaptation.
- **The greedy step is asserted, not proved.** The authors note that a
  knapsack-style greedy, Δ_perf per unit of QoD, "would be preferable if
  there was no limit to the number of WebViews", and state that with the cap, taking the top MAX_CHANGE by Δ_perf
  "is the best solution". No argument is given, and none could hold in
  general: picking by Δ_perf alone ignores each fragment's QoD cost.
- **Server lag detection.** Lag is declared when mean response time or QoD
  changes too fast between invocations (examples: +100 ms or −0.1 QoD over
  1000 accesses); OVIS then materializes everything, which the paper
  likens to pressing a panic button, and which the authors use to detect infeasible thresholds.
- **Simulation.** osim, in C++. 200 relations, 500 fragments, 300 pages;
  3–7 fragments per relation, 10–20 per page; Zipf-like accesses over
  pages, updates uniform over relations, random derivation graphs,
  near-exponential interarrivals. "The cost to update a relation was 150
  ms, the cost to access a WebView from the Asynchronous Cache was 10 ms
  and the cost to generate/refresh a WebView was 150 ms in all
  experiments." Runs of 2400 s.
- **Tracking θ (Figures 8–11).** 35,000 accesses and 32,000 updates.
  OVIS started fully materialized, climbed to θ = 0.925 and stayed near it,
  between all-materialized (lowest QoD, near-constant response) and
  caching only (highest QoD, response times fluctuating "up to ten times
  worse than OVIS"). With θ = 0.90 its QoD was lower; "OVIS seems to track
  the specified QoD threshold." With θ = 0.85, near the all-materialized
  QoD, it behaved like all-materialized.
- **Overload (Figures 12–14).** 40,000 accesses and 35,000 updates: caching
  alone saturated, ending three orders of magnitude slower than OVIS or
  all-materialized. OVIS(0.875) detected lag at t = 1563 s and reset to all
  materialized; at θ = 0.90 it reset twice; at 0.85 it settled without lag.
- **Scale (Figures 15–16).** 800 relations, 2000 fragments, 1500 pages,
  40,000 accesses and 25,000 updates: OVIS(0.85) lay between the two static
  plans and avoided the overload that caching alone showed.
- **What is not shown.** No comparison with the best static plan or any
  offline optimum, no repeated runs or variance, no real system or trace,
  costs fixed and equal across fragments, and the sensitivity of results to
  MAX_CHANGE, the period length and the lag thresholds is not reported.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): not the joint model, though the first reading in the
record to put staleness, upkeep and query savings on one online schedule.**
The owner's naming of it as the nearest candidate holds only for the
staleness term, and fails on the test as a whole.

- **Terms present.** Query savings (hits against misses, Eq. 6) and upkeep
  (refresh frequency times refresh cost, Eq. 7) are in one unit, response
  time, and traded per fragment. Staleness is measured, as the fraction of
  served fragments that were stale.
- **Staleness is a constraint, not a price.** θ is set by the application;
  there is no exchange rate between a stale read and a millisecond, and no
  cost of acting on a stale result. The problem is maximize performance
  subject to QoD ≥ θ: the mirror of Gupta and Mumick's maintenance budget
  ([THEORY-350](../theory.d/THEORY-350.md)), with freshness as the budget and upkeep moved into the
  objective.
- **Build cost absent.** Switching a fragment either way is free; MAX_CHANGE
  limits churn without pricing it. Bruno and Chaudhuri ([THEORY-332](../theory.d/THEORY-332.md)) have the
  build cost and no staleness; this has staleness and no build cost.
  Neither contains the other, and the record still holds no paper with all
  four terms.
- **Storage absent** (infinite cache), and the workload is uncertain only
  in the sense of being forecast by smoothing; there is no analysis of
  prediction error.
- **No guarantee.** Unlike Karlin et al. ([THEORY-348](../theory.d/THEORY-348.md)) or the record's
  reading of Bruno and Chaudhuri, there is no competitive or approximation
  result, and the greedy's optimality claim is unsupported. The evidence is
  a simulator with uniform costs.
- **What the freshness metric is.** Binary per fragment at access time,
  weighted within a page, averaged over requests. Age, number of missed
  updates and size of error are not measured. Under this metric a
  non-materialized fragment is stale only while its relation's update is
  queued, so caching alone is almost always fresh and materialization buys
  speed with refresh lag.

**On [CLAIM-303](../claims.d/CLAIM-303.md): a third option the claim's arithmetic lacks, and staleness
as a frequency rather than a cost.**

- [CLAIM-303](../claims.d/CLAIM-303.md) compares filing with upkeep against reconstruction. This paper's
  non-materialized policy is a third: keep the result, mark it invalid when
  a premise changes (dependency tracking, taken as cheap), and rebuild only
  at the next use. It dominates pure recomputation whenever invalidation is
  cheap, and it keeps freshness high at the cost of putting rework on the
  path of use, which in the simulation is what overloads the server when
  changes surge.
- Eager upkeep (materialization) buys speed at the price of serving stale
  results while refreshes queue. That is A11's verification term made
  measurable as the share of uses served stale; the paper bounds that share
  and never prices a stale use, so it neither supports nor tests A11's point
  that reusing an obsolete argument can cost more than recomputing it.
- The panic rule says that under overload a system that must keep
  answering accepts staleness rather than collapse. For a record, that is
  a design choice the claim's break-even condition does not see: the
  criterion changes with load.
