---
number: 892
status: Read
formerly:
- NOTE-tmp6iazx
paper: LIT-1090
title: Idreos, Kersten & Manegold — Database cracking
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the paper as published in the CIDR 2007 proceedings,
    fetched from https://cidrdb.org/cidr2007/papers/cidr07p07.pdf, which redirected
    to https://www.cidrdb.org/cidr2007/papers/cidr07p07.pdf (HTTP 200, application/pdf;
    11 PDF pages, printed pages 68–78; SHA-256 7c994b18c7238104994ef3a8f3598aade258a205d4fcd49a5fafa5b923aad3c9).
    The first page states that the paper is published under a Creative Commons Attribution
    2.5 licence. Text extracted with pdftotext, both in reading order and in layout
    mode. The extraction loses superscripts (10^7 prints as "107", 10^5 as "105")
    and scrambles the figures, so Figures 1–5 and every number taken from them were
    checked against page images rendered with pdftoppm. Read: all ten sections,
    Algorithms 1 and 2, all five figures and the reference list. Nothing skipped.
    The earlier paper this one builds on, Kersten and Manegold 2005 ("Cracking the
    database store", CIDR), was not read, nor any later cracking paper, so nothing
    here says what the line of work went on to show. Numbers marked "read off the
    figure" are approximate readings of plotted curves, not values stated in the
    text. Every quotation below was checked against the extracted text by script,
    with whitespace normalised.
date: '2026-10-15'
summary: >-
  Database cracking builds an index as a by-product of answering range queries.
  Each select partitions, in place, the part of a copy of the column that the query
  had to touch, so that the qualifying values lie contiguously, and records the
  new boundaries in a small tree; later queries touch only the pieces at the edges
  of their range, so per-query cost falls as the column is split into more pieces.
  On a 10^7-value column under uniformly random range queries, the first cracking
  select costs 0.38 s against 0.27 s for a scan and about 3.3 s for sort-then-search,
  and cumulative cost stays below sorting's until about 10^5 queries, after which
  upfront sorting wins. The authors claim that only ranges of past interest get
  organized, but every experiment uses uniformly random ranges, so that claim is
  not measured; there is no cost model, no rule for when a reorganization is worth
  making, and updates, concurrency and out-of-memory data are left as open problems.
---

# NOTE-892: Idreos, Kersten & Manegold — Database cracking

## Contribution

The paper proposes moving index maintenance from update time to query
time: "index maintenance should be a byproduct of query processing, not of
updates." Each query is treated "not only as a request for a particular
result set, but also as an advice to crack the physical database store into
smaller pieces." It presents what it calls "the first mature cracking
architecture", implemented in MonetDB/SQL, a column store: two
reorganization algorithms, two new relational operators
(crackers.select and crackers.rel_select), changes to the query plans,
micro-benchmarks against scan and sort, and full-SQL comparisons with
PostgreSQL, MySQL and MonetDB/X100. Section 8, about a third of the paper,
is a research agenda, not results. The authors say their goal "is not to
present solid solutions for each issue that appears but to argue that the
cracking direction deserves our attention and research".

## Key insight

A range query on an unindexed column must look at every value anyway. If,
while looking, it also swaps values so that those below, inside and above
the range end up in three contiguous blocks, it has done one step of
quicksort on the region it scanned, at little more than the cost of the
scan. Recording the two boundaries means no later query ever has to look
inside a block it falls wholly within or wholly outside. Every query then
splits only the one or two pieces that contain its own end points. The
pieces shrink, per-query cost shrinks with them, and the column becomes
more sorted in exactly the regions that queries have asked about. In the
paper's words: "Only database portions of past interest are easily
localized. The remainder is unexplored territory and remains non-indexed
until a query becomes interested."

## Mechanism

- **Cracker column.** "The first time a range query is posed on an
  attribute A, a cracker database makes a copy of column A." This copy,
  A_crk, is the only thing reorganized. The original column keeps
  insertion order, so that whole records can still be reassembled by
  position. "Cracking based on a query q on an attribute A is the act of
  physically reorganizing Acrk in such a way that the values of A that
  satisfy q are stored in a contiguous space."
- **Cracker index.** One per cracker column. "In our current
  implementation, the cracker index is an AVL-tree." Each node holds a
  value v and a position p such that everything before p is smaller than v
  and everything after is greater, with a flag for inclusiveness. A query
  whose bounds match known values is answered "at the cost of searching
  the index, only"; otherwise the index restricts the values to examine.
- **How a range query reorganizes the data.** crackers.select (i) searches
  the cracker index for the pieces that hold the query's bounds,
  (ii) physically reorganizes those pieces, (iii) inserts the new
  boundaries in the index, and (iv) returns the result as a slice (a view)
  of the cracker column at no copying cost. Pieces lying wholly inside the
  range are not touched. Two in-place, non-stable, swap-based algorithms
  do the reorganizing: CrackInTwo splits a piece on one bound
  (Algorithm 1); CrackInThree splits a piece on both bounds in one pass
  (Algorithm 2). "Three-piece cracking is used only when all the tuples
  with values in the range requested by a select operator fall into the
  same piece of the cracker column", which is likely for the first queries
  and less likely as pieces multiply. Otherwise only the first and last
  pieces of the range are split, each with CrackInTwo.
- **Worked example (Figure 1).** On a 14-value column, Q1 (10 < A < 14)
  copies the column and splits it into three pieces. Q2 (7 < A ≤ 16)
  splits only pieces 1 and 3, leaving piece 2 untouched, and its answer is
  pieces 2–4. A query for A > 16 would then match piece 5 exactly. (The
  printed SQL for Q2 reads "R.A >= 16"; the pieces drawn show the intended
  predicate is A ≤ 16.)
- **Plans.** Replacing select by crackers.select alone did not speed up
  whole queries: "Although the crackers.select is much faster, its initial
  overall effect on the plan turned out to be negligible." Its output is no
  longer in row-id order, so the following intersection of row-id lists
  had to use hashing; on TPC-H query 6 at scale factor 0.1 this "led to
  OIDintersect being 7 times more expensive." crackers.rel_select, which
  filters a second column by positional lookup into its uncracked original,
  removes that intersection. In consequence only one attribute per
  relation is cracked per query.

## Assumptions

- **A column store with an ordered attribute.** Cracking partitions by
  value ranges, so it needs a total order on the attribute. Row stores are
  discussed only as an envisioned extension (§3.1).
- **Range selections only.** Joins, aggregates and other operators are
  research agenda (§8.3–8.4).
- **Main memory.** "The experiments presented in this paper are all in an
  inmemory environment." (The extraction joins "in-memory" across a line
  break.)
- **No upfront knowledge of the workload and no idle time.** The paper
  confines its claim to that setting. If the interesting attributes are
  known in advance, there is time to prepare, and no updates intervene,
  "then sorting is a superior strategy. Cracking is not challenging any
  strategy in such conditions."
- **Storage for a copy.** Each cracked attribute costs a second copy of the
  column plus its index. The paper calls both "completely disposable".
- **Reorganize on every query.** The experiments crack on every select and
  update the index every time. When not to crack is left open (§8.8).

## Key results

All micro-benchmarks: MonetDB 5.0alpha, 2.4 GHz AMD Athlon 64, 2 GB
memory, in memory. Column of 10^7 distinct integers 1 to 10^7; queries
v1 < A < v2 with v1 and v2 "randomly chosen".

- **Cost of the first query.** "The sort loads the first query with an
  extra cost of 3 seconds, while a simple scan-select needs 0.27 seconds,
  and the first cracking operation costs 0.38 seconds." So the first
  cracking query costs about 40% more than a scan here; elsewhere the
  paper says "The initial crackers.select call on an attribute is
  typically 30% slower than algebra.select since it has to reorganize
  large parts of the column." The authors give the first cracking step as
  O(N) against O(N log N) for sorting.
- **Cost per later query.** It "highly depends on the size of the piece
  that is being physically reorganized". Over the run of Figure 2(a)
  cracking costs "ranging from 10 to 100 micro seconds" per query; after
  sorting, a query costs "a few micro seconds" by binary search. No
  analytical bound on per-query cost or on total cost over a sequence is
  given.
- **Evolution over a sequence (Figure 2(b)).** Tuples touched per query
  fall roughly as a power of the query count on a log–log plot: "already
  after the first 8-10 queries cracking touches an order of magnitude less
  data and becomes significantly faster (10 times faster than simple
  select)". Read off the figure: about 10^4 tuples touched near query 100,
  and between about 10 and 1,000 near query 10^5, with large scatter.
- **Convergence and break-even with sorting (Figure 2(a)).** Scan cost
  grows linearly, reaching about 2×10^4 s cumulative over 10^5 queries
  (read off the figure). Cracking's cumulative curve bends and flattens.
  "For a 10 M values table", the break-even with sort-then-search "is at
  around 10^5 queries in our current implementation"; after that "the
  investment of sorting starts to pay off." So cracking approaches, but in
  10^5 queries does not reach, the per-query cost of a sorted column. The
  paper says ordering is approached: "A cracking strategy eventually
  enforces order in a cracker column, i.e., the pieces of a cracker column
  are ordered." It does not claim or measure full convergence to a sorted
  column.
- **Larger columns (Figure 2(c)).** For 10, 20 and 40 million values,
  "As the size increases, cracking becomes more advantageous." Read off
  the figure for 40M at 10^5 queries: roughly 23 s cumulative for sorting
  against roughly 11 s for cracking.
- **Selectivity (Figure 3).** With result size fixed at S = 1, 10, 100,
  1,000 or 10,000 tuples and random placement, "the lower the selectivity
  the less effort is needed for cracking to reach optimal performance":
  queries returning large results split the column into even pieces
  sooner, while very selective queries leave large pieces for later
  queries to split. All five curves lie within about 2.8–3.0 s cumulative
  at 5×10^4 queries (read off the figure); the authors say the effect "is
  not one that dramatically affects performance".
- **Full SQL (Figure 4(a)).** select count(*) with a random range, on a
  single-column table of 10^7 random values in 0–9999, a thousand random
  queries, against PostgreSQL and MySQL with and without a B-tree.
  Cracking "significantly reduces the cost of MonetDB (eventually more
  than two orders of magnitude) while the rest of the systems maintain a
  quite stable performance." Read off the figure: MonetDB without cracking
  about 100 ms per query; with cracking about 30 ms at first, falling below
  1 ms. MySQL with a B-tree is fast only for highly selective queries.
- **TPC-H query 6 (Figure 4(b)).** 25 runs. Cracking brings MonetDB/SQL
  from about 270 ms to about 50 ms (read off the figure), close to
  MonetDB/X100 on unclustered data. A pre-clustered, compressed X100 table
  with a hand-compiled plan is faster still (about 14 ms), with the cost of
  the clustering excluded. "The graph flattens quickly due to the limited
  variation in the values of the lineitem shipdate attribute".
- **Batch inserts (Figure 5).** 10^3 queries on a 10-million column, then
  10 million tuples appended to the cracker column and the cracker index
  erased, repeated five times. Each insertion makes the next query
  expensive again; cost then falls back within some hundreds of queries.
  "The figure clearly shows that cracking quickly reaches high performance
  after each insertion." The floor rises with each batch, as the column
  grows.
- **Stable cracking.** Keeping insertion order within pieces made the
  algorithms "more complex and two times slower", so the experiments use
  non-stable cracking.

## Workload adaptivity: what is claimed and what is shown

The claims are strong. The cracker index is "a discriminative index";
"Only database portions of past interest are easily localized"; "In case
the focus shifts to a different part of the data, the cracker index
automatically adjusts to that"; the main characteristic of cracking is
"doing just enough, touching enough of the data each time, and being able
to change the focus to different parts of the data dynamically". The
abstract says self-organization "is visible even when the user focus is
randomly shifting to different parts of the data."

What is shown is narrower. Every workload in the paper is uniformly random
ranges (or TPC-H query 6, whose parameters are not described). No
experiment has a skewed workload, a hot range, or a focus that moves from
one region to another, and none measures how much of the column stays
unorganized. Under uniform queries every region is eventually asked about,
so the experiments show organization by use spreading over the whole
column, not organization confined to frequently queried ranges. The
abstract's randomly shifting focus means uniformly random queries. The claim
that only frequently queried ranges get organized follows from the
mechanism (a piece no query bound falls in is never split), but the paper
does not test it.

## Costs and limits stated by the authors

- **First-query penalty and copy.** About 30–40% over a scan on first
  touch, plus a full copy of the column per cracked attribute. "The
  overhead of penalizing the first queries however remains."
- **Index growth.** "Each time the index is updated we pay the cost of
  this update and future searches in the index become more expensive."
  "Administration and maintenance of the cracker column-cracker index pair
  becomes obviously more expensive when the number of pieces is
  increased." Cut-offs (stop updating the index, a minimum piece size, or
  merging pieces) are proposed; manually disabling index updates after a
  number of queries sped up later selects. "Here a cost model is needed to
  make a proper decision based on current workload, size of the column
  etc." No such model is given.
- **Updates.** Open. The only experiment is append-only batches, handled
  by appending to the cracker column and discarding the index. Deletions
  and in-place updates are discussed only as deferred delta tables.
- **Concurrency.** Open; reads and reorganizations of the same cracker
  column conflict (§8.5).
- **Out of memory.** Open; partitioning the column into memory-sized
  chunks with an index each is sketched (§8.7).
- **Plan effects.** Reorganization destroys row-id order, which made a
  downstream operator seven times dearer until a new operator was added.
- **Against sorting.** With a known workload, time to prepare and no
  intervening updates, sorting or a conventional index is better, and on
  the paper's own benchmark sorting overtakes cracking after about 10^5
  queries.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): the paper supports reading sorting as amortized search
directly, and does not supply the joint cost model.**

- It frames the comparison exactly as the question does: an upfront sort
  is an investment repaid by cheaper later searches, cracking spreads that
  investment over the searches themselves, and the choice between them is
  a break-even in cumulative cost (Figure 2(a), about 10^5 queries on 10^7
  values). The search a scan must do anyway is turned into a step of
  sorting, so sorting is amortized search in a literal sense here.
- It gives measurements, not a model. There is no expression for
  per-query cost as a function of piece sizes, no bound on total cost, and
  no rule for when a reorganization or an index entry is worth its cost;
  the authors say such a model "is needed". So it does not answer what
  would answer the question: it prices nothing in terms that would carry
  over to speed bugs, a filed argument or a bin.
- It does not cover cues or pop-out ([CLAIM-310](../claims.d/CLAIM-310.md) part 3). Lookup is by
  value on an ordered key.
- On "one arrangement" ([CLAIM-310](../claims.d/CLAIM-310.md)): cracking sidesteps the
  constraint by duplication. The original column keeps insertion order,
  and every cracked attribute gets its own reorganized copy, so a table
  can hold several physical orders at the cost of space; the paper notes
  cracking "allows to maintain independent individual physical orders for
  each attribute". In the implemented plans only one attribute per
  relation is cracked per query, which reintroduces a choice (§8.1).

**On the analogy with [CASE-094](../cases.d/CASE-094.md) (setting a hard-to-find brick aside in
its own bin once found).**

Where it holds:

- The reorganization is done during, and because of, a retrieval, with no
  plan of what will be wanted. That is the case's practice, and the paper's
  central idea.
- The extra work rides on work the search does anyway. After the first
  query, each cracking select is cheaper than the scan it replaces, so
  "the extra cost of the new bin is small" is true of every query but the
  first, and better than true: the query is cheaper, not just slightly
  dearer.
- What gets organized follows use. A region no query asks about is never
  split, as an unsought brick is never binned.
- The cracker index is the set of bin labels: it says where each piece
  starts and what range it holds.

Where it fails:

- **Cracking splits the whole region it searched, not just what it
  found.** Every value the query touches is moved to the correct side of
  each bound, so the column is partitioned into below, inside and above,
  one quicksort step. Setting one brick aside leaves the rest of the bin as
  it was. That is why a cracked range speeds up later queries for
  "similar, overlapping or even disjoint data", and why per-query cost
  keeps falling: each query roughly halves the regions that later queries
  must search. A brick set aside speeds up later searches for that brick,
  and others only by the few items removed from the bin. The brick
  practice is closer to a partial index or a cache of one answer, which
  the paper distinguishes from cracking (§9).
- **It needs an order.** Pieces are value ranges, and "below" and "above"
  carry the benefit. Bricks are grouped by kind and by similarity, which
  has no such order, so a brick search does not split the remaining bin
  into halves that help other searches.
- **The first time is not small.** The first query on an attribute costs
  30–40% more than a scan and makes a full copy of the column. The case's
  "extra cost of the new bin is small", and [QUESTION-114](../questions.d/QUESTION-114.md)'s statement
  that pulling a brick out when it is found anyway "costs nothing more",
  have no counterpart for the first query.
- **No selection by worth.** The case makes the bin for a brick that is
  rare and often used, which is [CLAIM-303](../claims.d/CLAIM-303.md)'s condition, "worth its cost only
  when expected reuse covers it". Cracking reorganizes on every query,
  whatever the chance of reuse, and the paper names the choice of when to
  stop (cut-offs, minimum piece size, merging) as open and lacking a cost
  model. So the paper does not show that the case's selection criterion
  is right; it shows that, for range queries on an ordered key, an
  unselective version pays off.
- **It converges toward a sort.** Under uniform queries cracking drives
  the whole column toward sorted order, and on the paper's benchmark a
  full upfront sort becomes cheaper after about 10^5 queries. Setting
  aside rare bricks never converges to a fully sorted collection, and the
  case does not consider the point at which sorting everything would pay.
- **Adaptivity to a skewed mix is asserted, not measured.** The analogy
  rests on organization going only where use goes. The paper's mechanism
  implies that, but all its experiments use uniformly random queries.

In short, the analogy holds for the principle (organize as a by-product
of retrieval, driven by use, at small marginal cost) and fails on the
mechanism: cracking is incremental sorting of an ordered key, whose payoff
comes from splitting what was searched, not from setting aside what was
found.
