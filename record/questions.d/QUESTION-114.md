---
number: 114
status: Open
formerly:
- QUESTION-tmplg07t
title: Is sorting a collection amortized search, and does physical database design,
  where a table is stored in one order and every further index is paid for in space
  and upkeep, give the joint cost
  model that the question on amortized retrieval lacks?
version: 1
tags:
- information-retrieval
- databases
- cognition
- operations-research
date: '2026-10-15'
line: distributed-agency
refines:
- QUESTION-095
summary: >-
  The LEGO parable ([CASE-094](../cases.d/CASE-094.md)) is [QUESTION-095](QUESTION-095.md)'s trade in its plainest form.
  Sorting spends search once, against retrievals later, and leaves the result in
  the world, as the cockpit's speed bugs do. [CLAIM-310](../claims.d/CLAIM-310.md) adds that one set of
  bins realizes one partition, chosen against a query mix. A database table is stored
  in one physical order, and every further index costs space and work on every insert.
  Choosing indexes for a workload is a studied problem with explicit cost models.
  This asks whether that model is the one [QUESTION-095](QUESTION-095.md) is looking for.
answered_by:
- THEORY-332
- THEORY-333
- THEORY-338
- THEORY-344
- THEORY-345
- THEORY-348
- THEORY-350
- THEORY-356
- THEORY-tmp3ren6
- THEORY-tmp4ezx1
- THEORY-tmp4zwbu
- THEORY-tmpc74vc
- THEORY-tmpehk94
- THEORY-tmpg43pg
- THEORY-tmph9339
- THEORY-tmphvzb7
- THEORY-tmpnbhb3
- THEORY-tmpqvlyg
- THEORY-tmprwm4f
- THEORY-tmpsvwtz
- THEORY-tmpxw8fg
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims cited as open, nothing here rests on their being settled -->

# QUESTION-114: Is sorting a collection amortized search, and does physical database design, where a table is stored in one order and every further index is paid for in space and upkeep, give the joint cost model that the question on amortized retrieval lacks?

## Why it is a question

[QUESTION-095](QUESTION-095.md) asks whether leaving a computation's result where it can be
read cheaply is the same trade as amortizing the computation. Its
citation search found pieces and no joint cost model. The LEGO
collection has every part of the trade, with nothing hidden:

- **Paid once.** Sorting N bricks takes about one pass. Pulling one
  hard-to-find kind out of a bin costs about one search, m/(c+1) items
  for c copies among m others ([CLAIM-307](../claims.d/CLAIM-307.md)). If that is done when the brick is
  found anyway, as in [CASE-094](../cases.d/CASE-094.md), it costs nothing more.
- **Saved each time.** Each later retrieval skips that search, so a bin
  pays when expected retrievals times search saved exceed its cost.
  That is [CLAIM-303](../claims.d/CLAIM-303.md)'s condition, "worth its cost only when expected reuse
  covers it", with the terms countable.
- **Staleness.** New bricks arrive unsorted and bins drift as the
  collection grows. The arrangement has upkeep, as a filed argument does
  ([QUESTION-098](QUESTION-098.md)).
- **One arrangement.** One set of bins realizes one partition ([CLAIM-310](../claims.d/CLAIM-310.md)),
  chosen against what the builder searches for. A database table has the
  same constraint and the same remedy. A secondary index serves other
  queries at a cost in space and in work on every insert.

The candidate: the index-selection problem in database physical design
is a worked cost model for this trade. It covers a workload of queries,
a budget of space and upkeep, and arrangements that serve some queries
at others' expense. If so, [QUESTION-095](QUESTION-095.md)'s three cases are instances of
it, with retrieval cost counted as computation.

## What would answer it

A reading of the index-selection literature, with a test: does its cost
model price the cockpit's bugs, a filed argument and a LEGO bin with the
same terms, and does it handle cues and search that pops out ([CLAIM-310](../claims.d/CLAIM-310.md) part
3), which a database lookup does not have? The record holds no work from
that literature. Registering one is the first step.

## Candidates, from a survey of 2026-10-15, and four readings

At the owner's request ("I'm wondering if maybe we could benefit from some
work at the intersection of database theory and information retrieval"),
a survey looked for work joining the two. Citations were checked against
Crossref. It found no paper that gives one cost model covering bugs,
filing and bins.

**Read the same day, at the owner's request.** Each split off one part of
the trade, and three of the four corrected how the survey had described
them.

- **Finkelstein, Schkolnick and Tiberio 1988** ([LIT-1084](../literature.d/LIT-1084.md), [NOTE-898](../notes.d/NOTE-898.md)).
  It chooses indexes and the one clustered order per table ("records can be
  ordered only one way") against a weighted workload, with the System R
  optimizer's own estimates. Costs are access, update, index upkeep and
  storage. The model is **steady-state per period** and has no term for
  the one-time cost of building an index or sorting a table, so it does
  not price "paid once". It chooses ways to reach stored data, not
  precomputed answers, so it does not cover the cockpit's bugs. Upkeep is
  charged at each insert. Letting bricks pile up and sorting later is not
  modelled. It supports [CLAIM-310](../claims.d/CLAIM-310.md)'s "one arrangement" and its
  dependence on the query mix, the latter by construction.
- **Yao 1981** ([LIT-1097](../literature.d/LIT-1097.md), [NOTE-891](../notes.d/NOTE-891.md)). "Founding cell-probe paper"
  holds. "When sorted order beats other arrangements" does not. Sorted
  order with binary search is optimal only for astronomically large
  universes and cells that hold nothing but keys. For small universes, or
  with one cell of arbitrary encoding, other arrangements beat it. It counts
  lookup cost only, building the table is free, so it says nothing on
  amortization.
- **Idreos, Kersten and Manegold 2007, database cracking** ([LIT-1090](../literature.d/LIT-1090.md),
  [NOTE-892](../notes.d/NOTE-892.md)). It is **amortized search, measured**. Each range query
  partitions in place the part of a copied column it touched, so the index
  grows from use. On 10⁷ integers the first query costs about 40% more
  than a scan, against about 12 times a scan for sorting first. Later
  queries are microseconds, and sorting upfront wins in total only after
  about 10⁵ queries. The claim that only regions of interest get organized
  is asserted, not tested: every workload was uniform. As an analogue of
  [CASE-094](../cases.d/CASE-094.md)'s setting a found brick aside, it holds in principle
  (reorganization as a by-product of search) and fails in mechanism.
  Cracking splits everything it searched, needs a sortable key, and
  reorganizes on every query whatever the chance of reuse. The authors say
  a cost model "is needed".
- **Sleator and Tarjan 1985** ([LIT-1093](../literature.d/LIT-1093.md), [NOTE-903](../notes.d/NOTE-903.md)). For one list
  searched from the front, move-to-front costs at most twice what any
  rule for that one list costs on the same sequence, **including rules that know the future
  and rearrange as they go**. A fixed order by access frequency is within
  no constant factor. Their Theorem 3: paying to rearrange ahead of need
  never beats moving the found item for free. In that model sorting ahead
  does not pay, and **[CASE-094](../cases.d/CASE-094.md)'s practice of setting a brick aside when
  it is found is the near-optimal one**. The model is one pile, where cost
  is depth, so bins are outside it. The paging half prices not knowing
  future requests (a ratio up to the cache size), for [QUESTION-095](QUESTION-095.md)'s
  caching reading, and nothing on precomputation or staleness.

**What the four give the question.** No joint model. They price separate
terms: steady-state upkeep against per-query savings (Finkelstein), the
cost of the lookup alone (Yao), a measured break-even between organizing
up front and organizing as a by-product of search (cracking), and the price
of not knowing future requests (Sleator and Tarjan). The cockpit's case,
a precomputed answer, is not in any of them.

**A fifth, for precomputed answers.** Harinarayan, Rajaraman and Ullman
1996 ([LIT-1094](../literature.d/LIT-1094.md), [NOTE-895](../notes.d/NOTE-895.md)), read at the owner's request. A stored answer is
worth the saving on every query that can be answered from it, less what the
answers already stored save. Choosing which to store is NP-complete. The
greedy choice of k views gets at least 1 − ((k−1)/k)^k ≥ (e−1)/e ≈ 63% of
the best benefit, with or without query weights, and the bound is tight. Under
a space budget it holds only less the largest view's share of the space.
The benefit is measured against storing only the top view, not against
total query cost. It has no build cost (size stands in for it), no upkeep
or staleness, no phases and no uncertain workload. So it names the
cockpit's category, a precomputed answer read back cheaply, but not what
makes the bugs pay: moving the work to a low-workload phase before the
deadline. For filing ([CLAIM-303](../claims.d/CLAIM-303.md)) it adds one usable term: coverage with
diminishing returns. A filed argument's worth depends on what is filed
already, so judging each item alone can misjudge it. The finding that
most changes this question is Sleator and Tarjan's: under uncertainty about
what will be wanted, reorganizing at the moment of use is within a
constant of the best possible, so "sorting is amortized search" may be
the wrong framing of what a good collector does.

**Hardness of the trade.** The survey cited Comer 1978 ([LIT-1086](../literature.d/LIT-1086.md)) for
"optimal index selection is NP-complete". Comer could not be obtained
(Unavailable), and a secondary account says it proves something else:
choosing a few attributes that tell every pair of records apart, with no
workload. The workload-based result is Piatetsky-Shapiro 1983
([LIT-1089](../literature.d/LIT-1089.md), [NOTE-902](../notes.d/NOTE-902.md)), read at the owner's request. One relation,
known frequencies of equality queries and updates, and single-attribute
indexes. A query costs a full scan without an index and one access with
one, and each index adds a fixed upkeep charge on updates. Choosing the
cheapest index set is NP-hard by reduction from set cover. Index cost here
is upkeep only, with no storage, build cost or physical order. The hardness
grows with the number of attributes and query types, so a handful of brick
attributes stays trivially enumerable. That is what the paper's own report
of an exact O(2^√M log M) algorithm for M domains suggests. So the trade
can be stated exactly and is hard in general, but not at the size of a LEGO
collection's sorting choices.

**When to stop paying per use.** Karlin, Manasse, Rudolph and Sleator 1988
([LIT-1096](../literature.d/LIT-1096.md), [NOTE-893](../notes.d/NOTE-893.md)), read at the owner's request, give the first
competitive analysis of rent-or-buy without the name. A cache holding a
shared block pays 1 per write to keep it current, or drops it and pays p
to fetch it again on a later read. Dropping once the writes since the last
read have cost p is within 2 of the offline optimum on every sequence, and
no deterministic online rule does better. In their words, "the change from
a state A to a state A' is made when the cost of making the change equals
the extra cost incurred due to being in state A instead of A'". For a LEGO
bin, the mirror case: make the bin once the extra search already spent on
a brick equals the bin's cost. Setting a brick aside when it is found costs
almost nothing, so the rule says do it at once, as [CASE-094](../cases.d/CASE-094.md) does. For
filing ([CLAIM-303](../claims.d/CLAIM-303.md)), counting uses weighted by what each reconstruction cost
is a criterion that stays within 2 in the worst case, with no forecast of
reuse. The guarantee assumes fixed prices and exactly two options, and the
paper prices no staleness: it forbids stale reads instead.

**The practice.** Chaudhuri and Narasayya 1997 ([LIT-1083](../literature.d/LIT-1083.md), [NOTE-900](../notes.d/NOTE-900.md)),
read at the owner's request, is Microsoft's AutoAdmin index tool. It
minimizes the optimizer's estimated cost summed over a fixed workload of
SQL statements, with no frequency weights, under a cap of k indexes. It
asks the optimizer about indexes that do not yet exist ("what-if"). Upkeep
enters only through the workload's update statements. There is no build
cost and no storage term, so of this question's title "space and upkeep",
only upkeep is priced, while Finkelstein et al. price storage too. Greedy
search seeded with an exhaustive pair found the optimum on four of five
TPC-D workloads and was within 1% on the fifth, by estimated cost only. No
guarantee is proved. Its own amortization is of the tool's
statistics-gathering: the cost of deciding, not of organizing. Its k counts
secondary orders kept, not the parts of one partition, so it does not match
[CLAIM-310](../claims.d/CLAIM-310.md)'s bin budget.

**Upkeep for stored answers.** Gupta 1997 ([LIT-1091](../literature.d/LIT-1091.md), [NOTE-889](../notes.d/NOTE-889.md)), read at the
owner's request as the follow-up to Harinarayan et al. with maintenance:
Harinarayan himself wrote none. It minimizes query frequency × lookup cost
plus update frequency × upkeep over the stored views, under a space
budget: the shape of the joint model this question lacks. But maintenance
enters one result only, AND graphs where each view is updated less often
than it is queried. For the data cube the paper assumes no updates, so it
does not add upkeep to Harinarayan's problem. Its greedy reaches 1 − 1/e
of the best benefit while using up to twice the space. It has no build
cost and no experiments. It prices keeping a stored answer current, not
acting on one gone stale: speed bugs are reset each approach, and a filed
argument goes stale without anyone propagating updates to it. Its
condition that a stored item is read more often than its source changes
sits close to [CLAIM-303](../claims.d/CLAIM-303.md)'s "worth its cost only when expected reuse covers
it", but in the paper it is only what the proof needs.

**Upkeep as a budget.** Gupta and Mumick 1999 ([LIT-1092](../literature.d/LIT-1092.md), [NOTE-890](../notes.d/NOTE-890.md)),
read at the owner's request, take up Gupta 1997's open problem. They
minimize query cost subject to a cap on total maintenance time, not a cap
on space. Their main finding bears on this question: upkeep is not
additive, because storing one view can make another cheaper to keep
current, so the value of a stored answer depends on what else is stored
and one-at-a-time greedy can fail arbitrarily. Their guarantee covers OR
view graphs only (1 − 1/e of an optimum's benefit at up to twice the
budget, under an assumption on the optimum), is stated without proof there (the 2005
journal version below proves it), and
needs greedy stages that are exponential in general. Upkeep is a
constraint, not a cost weighed against savings; every view is refreshed in
a nightly batch, so staleness is not priced, and nor are build cost or
storage. It does not give the joint model, and comes no closer than
Bruno and Chaudhuri below.
The journal version, Gupta and Mumick 2005 ([LIT-1080](../literature.d/LIT-1080.md), [NOTE-901](../notes.d/NOTE-901.md)),
also read at the owner's request, merges the 1997 and 1999 papers and
proves the maintenance-budget greedy and the A* search, but adds no new
problem: the space and maintenance constraints are never combined, the
guarantee still covers OR graphs only, and a new footnote says the 1997
lemma behind the only upkeep-in-the-objective result fails for OR graphs.
It changes nothing here.

**The nearest to a joint model.** Bruno and Chaudhuri 2007 ([LIT-1095](../literature.d/LIT-1095.md),
[NOTE-896](../notes.d/NOTE-896.md)), read at the owner's request from the accepted version on
Microsoft Research's page. It is the first work the record has read that
puts one-time organizing cost, per-query savings, upkeep, space and an
unknown, changing workload on one schedule. Each index has a build cost
B_I; dropping is free. The tuner keeps a running sum of the savings an
index would have given. It creates the index once that sum has risen by
B_I above its last low point, and drops it once it has fallen by B_I below
its last high. That is rent-or-buy in both directions, with hysteresis,
though the paper cites no competitive-analysis work and the survey's
"rent-or-buy framing" is the record's reading. Its "three-competitive"
result covers one index with no storage limit, and the proof shows only
that the ratio can approach 3. A simulation done for this reading found
the ratio exceeding 3 when a single statement's saving is large relative
to B_I, so the guarantee needs a small-step condition the paper does not
state. The general case is heuristic. It falls short of the question's
model in four ways: dropping is free, there is no staleness or deferred
upkeep, builds take no time, and it covers access paths, not precomputed
answers. For a LEGO bin: make it once the extra search already spent on
the brick, net of the bin's other costs, equals the bin's cost, and
remove it by the mirror rule. With a near-free bin, that says set the
brick aside at the first retrieval it would have sped up ([CASE-094](../cases.d/CASE-094.md)),
but one search through a large pile of similar bricks can cost more than
the bin, which is outside the small-step condition.

**A vocabulary, not a model.** Athanassoulis et al. 2016 ([LIT-1085](../literature.d/LIT-1085.md),
[NOTE-888](../notes.d/NOTE-888.md)), the RUM conjecture, read from the open EDBT proceedings. It defines
read, update and memory overhead as ratios to the base data, each at least
1, and conjectures that bounding two forces a lower bound on the third. It
is unproved, and as worded nearly empty, since each overhead is already at
least 1. In its terms, sorting with no auxiliary structure is an upkeep
trade, not a space trade: a sorted column reads in O(log N) and updates in
O(N). The extremes are not symmetric: the space-minimal design (an
unsorted pile) is also update-minimal. Build cost, workload, deadlines and
pop-out are all outside it. An unsorted pile, one labelled bin per kind,
and a tray of new bricks left to sort later map onto its three extreme
designs. Kirsh 1995 ([LIT-1076](../literature.d/LIT-1076.md), [NOTE-871](../notes.d/NOTE-871.md)) is already held.
The learned-index line (Kraska et al. 2018) belongs in the anthology.

## Database theory and semantic search, read 2026-10-15

At the owner's request, 23 works at the intersection of database theory
and similarity search were registered and read (two Unavailable). What
they give the question, by the gap each was chosen for:

**Staleness, priced.** Cho and Garcia-Molina 2000 ([LIT-tmpxjwsp](../literature.d/LIT-tmpxjwsp.md), [NOTE-tmp4d27w](../notes.d/NOTE-tmp4d27w.md)) is the
first reading that prices staleness instead of forbidding it: freshness
or age of a local copy under a fixed refresh budget, with Poisson changes
at known rates. Uniform refresh beats refresh in proportion to change
rate, and the optimum is neither; items that change too fast get no
refresh ([THEORY-tmphvzb7](../theory.d/THEORY-tmphvzb7.md)). Staleness is the objective, not a cost weighed against
reads or build. Olston, Loo and Widom 2001 ([LIT-tmpgbn1t](../literature.d/LIT-tmpgbn1t.md), [NOTE-tmparaq2](../notes.d/NOTE-tmparaq2.md)) put upkeep and
tolerated imprecision in one objective with an optimum between them
([THEORY-tmpsvwtz](../theory.d/THEORY-tmpsvwtz.md)), but staleness there is message traffic, and a source must see
every change. Olston and Widom 2000 ([LIT-tmpuohnv](../literature.d/LIT-tmpuohnv.md), [NOTE-tmpxqtc4](../notes.d/NOTE-tmpxqtc4.md)) make it a hard bound per
query ([THEORY-tmp4ezx1](../theory.d/THEORY-tmp4ezx1.md)). The journal paper of Cho and Garcia-Molina ([LIT-tmp580ot](../literature.d/LIT-tmp580ot.md)) is
Unavailable.

**Not the joint model.** Labrinidis and Roussopoulos 2003 ([LIT-tmp9g81t](../literature.d/LIT-tmp9g81t.md), [NOTE-tmpam1do](../notes.d/NOTE-tmpam1do.md)),
named as the nearest candidate, puts query savings, upkeep and measured
staleness on one online schedule, but staleness is a threshold, not a
price, and there is no build cost and no guarantee ([THEORY-tmpqvlyg](../theory.d/THEORY-tmpqvlyg.md)). It
complements [THEORY-332](../theory.d/THEORY-332.md) rather than beating it. Their 2000 paper
([LIT-tmpv6qcw](../literature.d/LIT-tmpv6qcw.md), [NOTE-tmp6f7qy](../notes.d/NOTE-tmp6f7qy.md)) forbids staleness, and on its testbed a stored result lost to
recomputing because reading it cost as much as rebuilding it ([THEORY-tmprwm4f](../theory.d/THEORY-tmprwm4f.md)).
The question stays Open: no reading prices build, upkeep, staleness and
savings together.

**Recognition is a cost.** Every stored-answer model above assumes that
knowing a stored answer serves a new query is free. Levy, Mendelzon,
Sagiv and Srivastava 1995 ([LIT-tmp3l2ha](../literature.d/LIT-tmp3l2ha.md), [NOTE-tmp7vihx](../notes.d/NOTE-tmp7vihx.md)), Chandra and Merlin 1977
([LIT-tmpkq8zv](../literature.d/LIT-tmpkq8zv.md), [NOTE-tmp5wypo](../notes.d/NOTE-tmp5wypo.md)) and Halevy's survey ([LIT-tmpu418n](../literature.d/LIT-tmpu418n.md), [NOTE-tmpxpujb](../notes.d/NOTE-tmpxpujb.md)) show it is not: certifying an
exact rewriting with views is NP-complete for conjunctive queries, in the
size of the definitions, not the data ([THEORY-tmpxw8fg](../theory.d/THEORY-tmpxw8fg.md), [THEORY-tmpe404c](../theory.d/THEORY-tmpe404c.md), [THEORY-tmpg43pg](../theory.d/THEORY-tmpg43pg.md)), while
a maximally contained rewriting is polynomial. A joint model would need a
recognition term. Dar et al. 1996 ([LIT-tmpmpt11](../literature.d/LIT-tmpmpt11.md), [NOTE-tmp256om](../notes.d/NOTE-tmp256om.md)) show partial reuse by
remainder queries in simulation, and no eviction rule won everywhere
([THEORY-tmpgvxim](../theory.d/THEORY-tmpgvxim.md), [THEORY-tmpghhhx](../theory.d/THEORY-tmpghhhx.md)).

**Organizing for similarity.** Andoni, Laarhoven, Razenshteyn and
Waingarten 2017 ([LIT-tmpxroug](../literature.d/LIT-tmpxroug.md), [NOTE-tmptdi3z](../notes.d/NOTE-tmptdi3z.md)) give the exact curve between space spent
organizing and query time for hashing-based approximate search
([THEORY-tmpehk94](../theory.d/THEORY-tmpehk94.md)), building on Indyk and Motwani 1998 ([LIT-tmpa1ovj](../literature.d/LIT-tmpa1ovj.md), [NOTE-tmp3up5l](../notes.d/NOTE-tmp3up5l.md), [THEORY-tmpvi601](../theory.d/THEORY-tmpvi601.md)), with
cell-probe floors from Panigrahy, Talwar and Wieder 2010 ([LIT-tmp7a48f](../literature.d/LIT-tmp7a48f.md), [NOTE-tmpc6udp](../notes.d/NOTE-tmpc6udp.md),
[THEORY-tmpnbhb3](../theory.d/THEORY-tmpnbhb3.md)): the similarity counterpart of [THEORY-340](../theory.d/THEORY-340.md). Where organizing stops
paying is in Weber, Schek and Blott 1998 ([LIT-tmpb8ql6](../literature.d/LIT-tmpb8ql6.md), [NOTE-tmpvtj3f](../notes.d/NOTE-tmpvtj3f.md), [THEORY-tmpc74vc](../theory.d/THEORY-tmpc74vc.md)) and Beyer
et al. 1999 ([LIT-tmp0cvca](../literature.d/LIT-tmp0cvca.md), [NOTE-tmps473y](../notes.d/NOTE-tmps473y.md), [THEORY-tmpazpbe](../theory.d/THEORY-tmpazpbe.md)). Graph indexes are guaranteed only for a
cubic-time build (Indyk and Xu 2023, [LIT-tmpllfsb](../literature.d/LIT-tmpllfsb.md), [NOTE-tmpak6ah](../notes.d/NOTE-tmpak6ah.md), [THEORY-tmpry4qh](../theory.d/THEORY-tmpry4qh.md)); HNSW's
logarithmic search is measured, not proved ([LIT-tmp08vve](../literature.d/LIT-tmp08vve.md), [NOTE-tmpkpp45](../notes.d/NOTE-tmpkpp45.md), [THEORY-tmp4zwbu](../theory.d/THEORY-tmp4zwbu.md)).
Fagin, Lotem and Naor ([LIT-tmpqp9aa](../literature.d/LIT-tmpqp9aa.md), [NOTE-tmpzuj15](../notes.d/NOTE-tmpzuj15.md)) price a conjunctive query over
feature-sorted lists ([THEORY-tmp3ren6](../theory.d/THEORY-tmp3ren6.md), [THEORY-tmp095vr](../theory.d/THEORY-tmp095vr.md)); Fagin 1996 ([LIT-tmpem2ov](../literature.d/LIT-tmpem2ov.md)) is
Unavailable.
