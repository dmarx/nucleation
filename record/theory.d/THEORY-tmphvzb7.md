---
status: Active
title: "When items change as independent Poisson processes with known rates and a fixed total refresh rate is shared among them, refreshing every item equally keeps the copy at least as fresh and at most as old, averaged over time, as refreshing in proportion to change rate, for any spread of rates; the freshness-optimal share rises and then falls with change rate and gives nothing to items that change too fast for the budget"
version: 1
tags:
- databases
- operations-research
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-tmpxjwsp
answers:
- QUESTION-114
summary: >-
  Cho and Garcia-Molina (2000), [LIT-tmpxjwsp](../literature.d/LIT-tmpxjwsp.md), read in [NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md). Freshness is
  the fraction of items equal to their source, age the mean time since an
  unseen change, both averaged over time and over equally weighted items.
  With fixed-interval refresh, uniform refresh is never worse than
  proportional on either measure, by convexity (proof in the authors'
  technical report). Under a fixed budget the freshness-optimal allocation
  starves the fastest-changing items; the age-optimal one refreshes them
  somewhat more. It prices staleness as an objective under a fixed budget:
  there are no reads, no query savings, no build cost and no cost of a stale
  use, so it is a staleness term and not a model trading staleness against
  upkeep.
---
<!-- inactive-ok-file: CLAIM-303 CLAIM-308 — Proposed; claims this account bears on, not leaned on -->

# THEORY-tmphvzb7: When items change as independent Poisson processes with known rates and a fixed total refresh rate is shared among them, refreshing every item equally keeps the copy at least as fresh and at most as old, averaged over time, as refreshing in proportion to change rate, for any spread of rates; the freshness-optimal share rises and then falls with change rate and gives nothing to items that change too fast for the budget

## Source

Cho and Garcia-Molina (2000), [LIT-tmpxjwsp](../literature.d/LIT-tmpxjwsp.md), SIGMOD 2000 pp. 117–128, read
in full in [NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md) from the PDF on ACM SIGMOD's SIGMOD Record site. The
conference paper states the general results and defers their proofs to
the authors' 1999 Stanford technical report, whose Appendices D and E were
read for this account.

## What was actually shown

**The measures.** An item's freshness is 1 while it equals its source and 0
otherwise; its age is 0 while current and otherwise the time since the
source changed. A copy's freshness and age are the means over items, and
policies are compared by their time averages. With r = λ/f, the ratio of an
item's change rate to its refresh rate, fixed-interval refresh gives
time-averaged freshness (1 − e^(−r))/r, which is (e − 1)/e ≈ 0.63 when an
item is refreshed exactly as often as it changes; freshness 0.8 needs about
two refreshes per change. Fixed order beats random order, which beats
picking items at random, on both measures.

**Uniform against proportional.** For fixed-interval refresh, freshness is
convex and age concave in the change rate at a fixed refresh rate. By
Jensen's inequality, uniform refresh gives freshness at least, and age at
most, that of proportional refresh, for any distribution of rates, the
two agreeing when all rates are equal (report, Theorems 3 and 4). Under a
gamma distribution of rates the gap widens as the rates spread (Table 3,
Figure 7). In [NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md) the convexity and concavity were also checked
numerically for the fixed-order formulas.

**The optimum.** Maximizing mean freshness subject to the budget gives,
for every refreshed item, the same marginal freshness per unit of refresh
rate, µ, with items that cannot reach µ left unrefreshed (report, Appendix
E); the solution curve has one shape, scaled by 1/µ, for every database
(report, Theorem 5). For rates 1 to 5 and five refreshes per day the
freshness-optimal rates are 1.15, 1.36, 1.35, 1.14 and 0: the fastest item
is never refreshed. The age-optimal rates rise with change rate, 0.84 to
1.09, closer to uniform than to proportional. [NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md) reproduced both
rows by script. From the fixed-order formula, the marginal freshness of a
first refresh is 1/λ, so an item is left unrefreshed exactly when λ ≥ 1/µ;
that threshold is the reading's derivation, not stated in the paper.

**The data.** Daily crawls of about 720,000 pages from 270 popular sites
over four months fit exponential intervals between changes for pages
changing about every ten days. Extrapolated to 100 million pages refreshed
monthly, proportional, uniform and optimal refresh give freshness 0.12,
0.57 and 0.62 and age 400, 5.6 and 4.3 days (Table 6), an estimate the
paper calls "a crude approximation".

What could have come out otherwise: the convexity of freshness in the
change rate. If refreshing a fast item bought proportionally as much
freshness as refreshing a slow one, proportional refresh would not lose.

## What this does not say

- **Not that staleness is priced against upkeep.** The refresh budget is
  fixed, and the paper only maximizes freshness or minimizes age within
  it. µ is a shadow price of refresh, but no cost of refreshing is weighed
  against any value of being current.
- **Not the cost of a stale read.** There is no model of reads or queries.
  Items count equally whether read often or never, and a stale item costs
  the same whatever it is used for. Time-averaged freshness equals the
  share of reads that find current data only if reads arrive at random
  times, evenly over items, which the paper does not model.
- **Not that fast-changing items do not matter.** Starving them is optimal
  for a measure that scores only whether an item is current. Under age
  they get more refresh, and with unequal importance the paper's own
  preliminary finding is that a more important item is refreshed more,
  "but not necessarily twice as often". Which items to keep current
  depends on how staleness is scored.
- **Not for arbitrary change.** Rates are known, constant and independent,
  and changes are Poisson. Bursty, regular or correlated change, and rates
  that must be estimated, are outside the results.
- **Not a joint model of build, upkeep, staleness and savings.** There is
  no build cost, no saving per query and no alternative of fetching on
  demand, so this is one term of the model [QUESTION-114](../questions.d/QUESTION-114.md) asks for.

## Connections

It answers part of [QUESTION-114](../questions.d/QUESTION-114.md): the record's earlier readings either
forbid stale reads ([THEORY-348](THEORY-348.md), Karlin et al.), refresh everything in a
batch (Gupta and Mumick, [LIT-1092](../literature.d/LIT-1092.md)), or leave staleness out ([THEORY-332](THEORY-332.md),
Bruno and Chaudhuri). This is the first account that measures staleness as
a function of change rate and refresh rate.

For [CLAIM-303](../claims.d/CLAIM-303.md), it models the term "checking it is still current" as a rate
per unit time whose value depends on how fast an argument's grounds change,
not on how often the argument is used, and it does not reach A11's cost of
reusing an obsolete argument. [CLAIM-308](../claims.d/CLAIM-308.md) leaves staleness out, and this
account does not supply what it lacks: it has no online decision, no
sequence of uses and no choice whether to keep a copy at all.

The journal version, Cho and Garcia-Molina 2003 ([LIT-tmp580ot](../literature.d/LIT-tmp580ot.md)), extends
the same model and was not obtainable.
