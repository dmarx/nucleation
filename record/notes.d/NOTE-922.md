---
number: 922
status: Read
formerly:
- NOTE-tmpxqtc4
paper: LIT-1117
title: Olston & Widom — Offering a precision-performance tradeoff for aggregation
  queries over replicated data
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the VLDB Endowment's own copy of the proceedings
    paper (https://www.vldb.org/conf/2000/P144.pdf, 12 pp., printed pages 144–155,
    "Proceedings of the 26th VLDB Conference, Cairo, Egypt, 2000" on the first page),
    fetched with a browser User-Agent header; without one the server does not return
    the PDF. Text extracted with pdftotext, in both raw and layout modes; the layout
    extraction was used where the raw one lost the two-column order around the cost
    model in Section 4. Read: abstract, Sections 1–8, Figures 1–7, acknowledgments
    and the reference list. Nothing skipped. The proofs of optimality for MIN and
    MAX, the MAX algorithms, the tuple classification for predicates, the full AVG-with-predicate
    algorithm and the bound-function analysis are all deferred to the authors' technical
    report ([24], trapp-ag.ps), which was not read, so for those the paper's statements
    are its claims and not checked arguments. Every quotation below was checked
    against the extracted text by script, with whitespace normalised; the one containing
    ε, which the extraction drops, was checked against the page image of printed
    page 150, as were the values read off Figures 5 and 6.
date: '2026-10-15'
summary: >-
  Olston and Widom propose TRAPP: caches hold, for each numeric value, an interval
  its source guarantees to contain the current value, the source pushing a refresh
  whenever the value leaves it. A query carries a precision constraint R, and the
  system chooses which values to fetch exactly so that the answer interval is at
  most R wide whatever the true values, at least total refresh cost. For SUM (and
  AVG without a predicate) that choice is a 0/1 knapsack problem, NP-complete in
  general and polynomial with equal costs; COUNT and MIN have simple rules. Staleness
  becomes bounded imprecision, never error, and the cost of the source-side upkeep
  that guarantees this, and of setting the bound widths, is outside the optimization.
  The one experiment is 90 stock prices with random costs.
---

# NOTE-922: Olston & Widom — Offering a precision-performance tradeoff for aggregation queries over replicated data

## Contribution

Stale replication normally offers two modes: read the cached copy, fast but
with no guarantee of how wrong it is, or read the source, exact but slow.
TRAPP ("Tradeoff in Replication Precision and Performance") replaces the
cached value by a guaranteed interval and lets each query name how wide an
answer it will accept. "Caches store ranges that are guaranteed to bound the
current data values, instead of storing stale exact values." The paper
defines the architecture, gives bounded versions of COUNT, MIN, MAX, SUM and
AVG with and without selection predicates, and gives algorithms for choosing
the cheapest set of values to refresh so the answer meets the constraint
(TRAPP/AG). Joins are discussed without an algorithm.

## Key insight

If the source promises to tell the cache whenever a value leaves its
interval, a cached interval is never wrong, only wide. Staleness then has a
measure, the width, and a query can buy width down by paying for exact reads.
Because the answer interval of SUM is the sum of the member widths, choosing
which members to read exactly is choosing which widths to keep within a
budget R while leaving out the most expensive reads, which is knapsack.

## Assumptions

- **One master per value, numeric.** Each object O_i has one real value V_i
  at one source. Caches hold [L_i, H_i]; a value may be cached in several
  caches with different bounds.
- **Source-side guarantee.** "The source guarantees that the actual value for
  O will stay in this bound, or if the value does exceed the bound then the
  source will immediately send a new refresh." This is the value-initiated
  refresh. The source's Refresh Monitor tracks every bound in every cache.
- **No time passes.** "the level of precision offered by our system does not
  account for elapses of time while sending refresh messages or while
  processing a single query." Value-initiated refreshes are assumed not to
  occur while a query runs.
- **Insertions and deletions are propagated immediately** to all caches, so
  table cardinality is always exact (this is why COUNT without a predicate is
  free).
- **Additive, known, per-tuple refresh costs.** "We are assuming that the cost
  to refresh a set of tuples is the sum of the costs of refreshing each member
  of the set, in order to keep the optimization problem manageable. This
  simplification ignores possible amortization due to batching multiple
  requests to the same source."
- **Batch choice.** The refresh set is chosen before any refresh, so the
  constraint must hold "for any possible precise values for the tuples in
  TR". Refreshing one at a time and stopping early is left to future work.
- **Absolute precision constraints** R ≥ 0 on answer width; R = ∞ if omitted.
  Relative constraints are future work.
- **Bounds are given.** "All of the subsequent algorithms and results in this
  paper are independent of how bounds are selected and specified." Bounds may
  be functions of time, zero-width at refresh and widening after; the paper
  reports, without the analysis, that with no knowledge of update behaviour
  widths growing as the square root of time since refresh are appropriate,
  with the proportionality "chosen at run-time" (details in [24]).

## Key results

The cost model optimized is the total refresh cost Σ_{t_i ∈ T_R} C_i of the
query-initiated refreshes for one query. A CHOOSE_REFRESH algorithm is
optimal "if it finds the cheapest subset TR of T's tuples to refresh (i.e.,
the subset with the least total cost) that guarantees the final answer to the
query will satisfy the precision constraint for any precise values of the
refreshed tuples within the current bounds."

- **MIN, no predicate.** Answer [min L_i, min H_i]. Refresh exactly the tuples
  with L_i < min_k H_k − R, independent of cost. Running time O(|T|), sublinear
  with B-tree indexes on both endpoints. Optimality: "the algorithm's
  justification and proof of optimality is nontrivial (see [24])"; not in this
  paper. MAX is symmetric, also in [24].
- **SUM, no predicate.** Answer [Σ L_i, Σ H_i], so HA − LA = Σ (H_i − L_i) and a
  refreshed tuple contributes zero width. The constraint becomes Σ over tuples
  not refreshed of (H_i − L_i) ≤ R, and minimizing the cost of T_R is
  maximizing the cost of the tuples kept. This is shown to be isomorphic to
  0/1 knapsack (profit C_i, weight H_i − L_i, capacity R), which is
  NP-complete. The implementation uses Ibarra and Kim's approximation, within
  a fraction ε of optimal profit in O(n log n) + O((3/ε)² n) time. Note that ε
  bounds the profit kept, not directly the refresh cost paid. With equal costs
  the optimum is greedy by increasing width, O(n log n).
- **COUNT, no predicate.** No refresh is needed, because cardinality is exact
  by assumption.
- **AVG, no predicate.** Run SUM with constraint R·COUNT and divide; same
  complexity as SUM.
- **With predicates over bounded columns.** Tuples are classified into T⁻
  (cannot satisfy), T? (may) and T⁺ (must). MIN becomes
  [min over T⁺ ∪ T? of L_i, min over T⁺ of H_i], with the same refresh rule
  restricted to T⁺ ∪ T?. SUM extends each T? bound to include 0 and remains a
  knapsack. COUNT is [|T⁺|, |T⁺| + |T?|] and the optimal refresh set is the
  ⌈|T?| − R⌉ cheapest tuples in T?, since each refresh removes one tuple from
  T?. AVG's tight bound takes O(n log n); a looser linear bound is given; the
  refresh choice "preserves the Knapsack Problem structure" with details in [24].
- **Joins.** Bounded answers are computed as for predicates. Choosing tuples
  to refresh is left open: "optimal algorithms are not provided".
- **Experiments.** One set, for SUM without predicate: "90 actual stock prices
  that varied highly in one day", with the day's high and low as bounds, the
  close as the exact value and refresh costs random between 1 and 10, on a Sun
  Ultra-1. Figure 5 (R = 100, ε varied from 0 to 0.1) shows algorithm
  time rising from near zero to about 120 seconds as ε falls, while total
  refresh cost falls only from about 360 to about 330; the authors
  conclude it is "not in general advantageous to set ε below 0.1". Figure 6
  (ε = 0.1, R varied) shows total refresh cost falling continuously and
  monotonically from about 4000 at R = 0 to near zero at R = 140. No system was measured: source–cache cooperation
  was still being implemented, and value-initiated refresh traffic was not
  measured at all.

## Bearing on the record

**[QUESTION-114](../questions.d/QUESTION-114.md) and staleness.** This is the first reading in the record's
[QUESTION-114](../questions.d/QUESTION-114.md) line that gives staleness a quantity. A cached value is an
interval; its width is how stale it is allowed to be; a query states how much
staleness its answer tolerates (R); and the price of removing staleness is the
refresh cost of the values read exactly. [THEORY-348](../theory.d/THEORY-348.md) forbids stale reads
(coherence is enforced) and [THEORY-350](../theory.d/THEORY-350.md) refreshes everything in a batch; here a
stale read is lawful and its imprecision is bounded and known.

But the paper prices only one side. Its optimization is the query-time cost of
meeting R. The other side, the source's upkeep that makes the interval a
guarantee (monitoring every cached bound and pushing a refresh whenever a
value escapes), is assumed and never costed, and how wide to make the bounds,
which governs that upkeep, is set outside the paper. There is no cost of
imprecision either: R is a hard constraint chosen by the user, not a loss
traded against refresh cost. And there is no cost of being wrong, because
under the guarantee a stale read cannot be wrong. So it supplies a unit for
staleness (bound width against a stated tolerance) and the price of buying it
down per query, not a joint model of upkeep, staleness and use. The companion
paper [LIT-1109](../literature.d/LIT-1109.md) prices the upkeep side. Like [THEORY-332](../theory.d/THEORY-332.md)'s tuner it covers
access to stored data, not stored answers: the cached items are base values,
and aggregates are computed fresh at each query.

**[CLAIM-303](../claims.d/CLAIM-303.md).** [CLAIM-303](../claims.d/CLAIM-303.md)'s terms map partly. Its "checking it is still
current" (c_a) has two parts here: the source's push on escape, which is
upkeep (u), and the query's exact read when the interval is too wide, which
is a per-use verification cost. The precondition matters more: the guarantee
rests on a source that knows the true value and watches every copy. A filed
argument has no such source; nothing notices when its conclusion has moved
outside what it claims. So the paper does not supply A11's term that "the cost
of incorrectly reusing an obsolete argument may exceed the cost of recomputing
it". It removes that risk by assumption, at an unpriced cost. What it does
offer [CLAIM-303](../claims.d/CLAIM-303.md) is a sharper form of "verification manages the risk of reusing
stale conclusions": if a filed item states a bound on how far it can be off,
each use can decide whether that bound is good enough for its purpose, and pay
for reconstruction only when it is not. Which items to reconstruct for one
use is then a knapsack choice, NP-complete when items add their imprecision
and costs differ.

**[CLAIM-308](../claims.d/CLAIM-308.md).** Nothing here touches the rent-or-buy argument. The paper has no
sequence of uses, no decision about when to start or stop caching, and no
competitive analysis. It confirms [CLAIM-308](../claims.d/CLAIM-308.md)'s own boundary: the staleness that
[THEORY-348](../theory.d/THEORY-348.md) forbids can be admitted and priced, but only with machinery (a
source-side guarantee and per-query tolerances) that lies outside a two-state,
fixed-price model.
