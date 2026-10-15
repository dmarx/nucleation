---
status: Read
paper: LIT-tmptn63k
title: Harinarayan, Rajaraman & Ullman — Implementing data cubes efficiently
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' own copy on Stanford InfoLab's
    papers server, http://infolab.stanford.edu/pub/papers/cube.ps (PostScript, 249,867
    bytes, sha256 01b4df2d…a07641; dvips output of a TeX run dated 8 January 1996;
    the directory listing dates the file 27 June 1996). It is a 25-page version,
    dated five months before the conference, with the same title and authors as
    the SIGMOD '96 paper (pp. 205–216). It is not the proceedings typesetting, and
    it was not compared with the published text, since the ACM Digital Library returned
    403 and no other copy was found, so wording, page numbers and any late changes
    may differ from the version of record. Unpaywall and OpenAlex list no open-access
    copy; Semantic Scholar was rate-limited; the ilpubs.stanford.edu technical-report
    server timed out or reset; Ullman's personal pages gave 403/404; CiteSeerX was
    not used. Converted with ps2pdf and extracted with pdftotext -layout. The extraction
    drops the fi/ff/fl ligatures and most mathematical operators, so the benefit
    definition (p. 13), the inequalities of Fig. 13 and the derivation that follows
    (p. 18), the tightness statement (p. 19) and the space-budget bound (p. 20)
    were checked against page images rendered at 110 dpi. Read: abstract, all six
    sections, every example, figure and table, the proof sketch of §4.3 and the
    lower-bound sketch of §4.4, and the reference list. Nothing skipped. The paper
    itself omits the detailed construction of the worst cases for general k. Every
    quotation from the paper was checked against the extracted text by script, with
    whitespace removed and ligature letters dropped from both sides, except three
    formulas (the benefit definition, the tightness statement and the 0.63 − f bound),
    which were checked against the page images. The two quotations from the record
    (CLAIM-303 and this work's LIT summary) were checked against the record's files.
date: '2026-10-15'
summary: >-
  Treats a data cube's group-by queries as a lattice in which a query can be answered
  from any stored ancestor, prices a query at the number of rows of the smallest
  materialized ancestor, and chooses which views to precompute. Choosing k views
  to maximize the total reduction in query cost (the "benefit") is NP-complete;
  a greedy rule that adds the view of largest marginal benefit gets at least 1 −
  ((k−1)/k)^k ≥ (e−1)/e ≈ 63% of the optimal benefit, a bound that is tight, holds
  unchanged with query-frequency weights, and weakens to 0.63 − f under a space
  budget when no view takes more than a fraction f of it. The cost of building views
  is represented only by their size, maintenance and updates are not modelled, the
  data are static, and the bound is on benefit, not on query cost. On TPC-D data
  the greedy order reaches nearly the minimum total query time with five views and
  barely more space than the base view.
---

# NOTE-tmpb6yin: Harinarayan, Rajaraman & Ullman — Implementing data cubes efficiently

## Contribution

Decision-support queries aggregate a large table along some subset of its dimensions. Each such group-by is a view, and many views can be computed from others: sales by part can be summed from sales by part and customer. Storing every view is too costly, storing none sends every query to the raw data. The paper asks which views to store. It gives a lattice framework for the dependencies among views, including dimensions with hierarchies (day, week, month, year), a cost model, a greedy selection algorithm with a worst-case guarantee, and a closer analysis of the hypercube lattice, where the views are all subsets of n attributes.

## Key insight

A stored answer is worth what it saves on every query that can be derived from it, less what those queries already save from answers stored before it. So the value of storing one more answer depends on what is already stored, and the best set cannot be built by ranking answers one at a time on their own merits: in Example 4.1 the view f "wasn't even close to the best choice at the first round" and was the greedy choice at the second. Picking at each step the answer with the largest marginal saving is provably never worse than about 63% of the best saving achievable with the same number of stored answers.

## Assumptions

- **Lattice of queries.** Q1 ⪯ Q2 when Q1 "can be answered using only the results of query Q2". The paper needs only that ⪯ is a partial order with a top element, the view every view depends on (the finest grouping, which must always be stored, since nothing else can produce it).
- **Linear cost model.** "The cost of answering Q is the number of rows present in the table for that query QA used to construct Q", where QA is the materialized ancestor used, taken to be the smallest. A validation on TPC-D (Fig. 5) fits T = mS + c: one query for a single supplier took 2.07 s from its own cell, 2.38 s from the supplier view (10,000 rows), 20.77 s from (part, supplier) (800,000 rows) and 226.23 s from the top view (6,000,000 rows). The fixed cost c is the cell-itself time; the per-row ratios are .000031, .000023 and .000037.
- **All queries are whole views.** Single-cell queries are folded in by assuming that, over time, many queries for different cells of one view cost as much together as reading that view: "We assume that all queries are identical to some element (view) in the given lattice." Indexes and clustering are set aside: "Clearly there are other factors, not considered here, that influence query cost."
- **Uniform query mix by default.** The objective is total (equivalently average) cost over all views, each counted once. Probabilities per view are an extension (§4.6).
- **View sizes are known or estimated**, by materializing on a sample, by analytic estimates under independence, or by sampling distinct values (§3.3).
- **Static data.** There are no updates, no insertions and no cost of keeping views current anywhere in the model.
- **Build cost is not a separate term.** Space stands in for it: "the space consumed by the data cube is also a good indicator of the time it takes to create the data cube". The lattice also gives an order for building the chosen views, each from its smallest already-built ancestor (§2.5, point 3), but that order is outside the objective.

## Key results

- **Benefit (§4.1).** With C(v) the rows of view v and S the views already chosen (always including the top view), for each w ⪯ v let u be the cheapest view in S with w ⪯ u; v's contribution for w is C(u) − C(v) if positive, else 0; the benefit B(v, S) is the sum over all w ⪯ v. (This copy prints "B_w = C(v) − C(u)" on p. 13, a sign slip; the prose and every worked example use C(u) − C(v).)
- **Hardness.** "Even in this simple setting, the optimization problem is NP-complete; there is a straightforward reduction from Set-Cover." The problem is: maximize total benefit choosing k views besides the top view, regardless of their size. The reduction is asserted, not given.
- **Greedy algorithm (Fig. 6).** Start with S = {top view}; k times, add the view not in S with the largest B(v, S).
- **Guarantee (§4.3).** For a budget of k views and any lattice, the total benefit A of the greedy selection and the total benefit B of the optimal k views satisfy A/B ≥ 1 − ((k−1)/k)^k. For k = 2 that is 3/4; as k grows it decreases to 1 − 1/e = (e−1)/e ≈ 0.63: "for no lattice whatsoever does the greedy algorithm give a benefit less than 63% of the optimal benefit." The quantity bounded is benefit, the reduction in total query cost relative to storing the top view alone. It is not a bound on the ratio of query costs, and the paper does not translate it into one. The proof is a sketch: it bounds B by the family B ≤ k·a_j + a_1 + … + a_{j−1} (Fig. 13) and argues that the bound is loosest when all right sides are equal, which it calls "easy to show".
- **Tightness (§4.4).** "For any k, the ratio A/B = 1 − ((k−1)/k)^k can be reached." Example 4.2 gives a lattice with ratio 6241/8200 for k = 2, and variants approach 3/4. For general k the construction is described only in outline: "We omit the detailed construction of the sequence of bad cases, one for each k, from this paper."
- **When greedy is optimal (§4.5).** If the first greedy benefit a_1 dwarfs the rest, greedy is near optimal; if all the a_i are equal it is optimal.
- **Query frequencies (§4.6).** "When computing benefits, we weight each view by its probability. The greedy algorithm will then have exactly the same bounds on its performance: at least 63% of optimal." Frequencies are fixed and known in advance.
- **Space budget (§4.6).** With a total space limit instead of a count, greedy uses benefit per unit space. A small view of high benefit per unit space can crowd out a large view of nearly the same ratio, so no constant bound holds in general: "Choosing the small view excludes the large view, because there is not enough space available for the large view after we choose the small." If no view uses more than a fraction f of the space allowed, the ratio of greedy to optimal benefit "is no less than 0.63 − f". This is stated with "the same analysis as given above says", without a separate proof.
- **TPC-D experiments.** The 1 GB TPC-D database. The motivating three-dimension example (part, supplier, customer; Fig. 1) has a full cube of a little over 19 million rows; storing the top view plus the small views gives nearly the same average query cost "using only 7 million rows, an improvement of more than 60% in terms of space consumed and thus in the cost of creating the data cube." Seventy percent of the cube's cells are dependent cells. On the hierarchical part-by-customer lattice of Fig. 4 (12 views), the greedy order (Fig. 10) cuts total time from 72M rows with the top view alone to 30.1M with four views (space 6.1M) and 24.3M with five (space 6.3M); the remaining seven views take space to 22.3M and time only to 22.3M. The paper reads Fig. 11 as a clear stopping point after five views. The guarantee is not tested empirically against an optimum on real data.
- **Hierarchies (§2.4–2.5).** A dimension with a hierarchy is itself a lattice (week is not comparable with month or year), and views over several hierarchical dimensions form the direct product of the dimension lattices, which is not a hypercube. The greedy algorithm applies to any such lattice.
- **Hypercube, equal domain sizes (§5.1–5.3).** n attributes each with r values, m rows of raw data, data spread at random. A view grouping on i attributes has about min(r^i, m) rows, so sizes grow exponentially up to a "cliff" at rank k = log_r m and are flat above it. Storing only the top view gives space m and total time m·2^n. Storing everything: views at or above the cliff are as large as the top view and need not be stored; with j = nr/(r+1) the rank of largest total size, if k > j space and time are both about (2r^{r/(r+1)})^n; if k < j and k ≤ n/2, space and time are about m and m·2^n, the same as the space-optimal case; if k < j and k > n/2, space is about m and time about C(n, j)·r^j (Fig. 16). With unequal domain sizes the cliff is spread across ranks and the analysis carries over in words (§5.4).
- **Future work named by the authors.** Cost models with indexing and clustering, MDDB storage, and "dynamic materialization": "The views, in some sense, form a memory hierarchy with differing access times." "It would be interesting to compare dynamic materialization with the static materialization scheme we investigate in this paper."

## Bearing on the record

**On [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): it supplies the precomputed-answer term the four readings lacked, and it is not the joint cost model.**

- *What it adds.* The survey's pointer holds. The objects chosen are answers, not access paths: "Materialize" means precompute a query result and keep it. And the model has a feature none of Finkelstein et al., Yao, cracking or Sleator and Tarjan has: a stored answer serves every query derivable from it, its value is counted over all of them, and that value is marginal on what is already stored. That gives a precise form to [CLAIM-303](../claims.d/CLAIM-303.md)'s "worth its cost only when expected reuse covers it": reuse is coverage of descendant queries, weighted by their frequency, and the saving per query is the gap between the cheapest previous source and the new one. It also shows the selection is hard (NP-complete) but approximable by a simple rule within a constant, about 63% of the best saving for a count of k stored answers, 0.63 − f for a space budget when no single answer is large.
- *What the guarantee is.* It is on benefit (saving against the top view alone), for a fixed number of views besides the top one, with any lattice, with or without fixed query probabilities. It is not on total query cost, and under a space budget it holds only with the cap f on any one view's share. The record's LIT summary ("under a space budget, with a greedy algorithm and a guarantee") should name the count budget as the main case.
- *What it leaves out.* (1) **Build cost.** Only space stands for it; there is no term for the work of computing a view, so "paid once" is not priced any better than in Finkelstein et al. (2) **Upkeep and staleness.** The data never change. No view goes out of date, nothing is charged for refreshing, and a derived answer is always exact; [CLAIM-303](../claims.d/CLAIM-303.md)'s dependency tracking and refresh and [QUESTION-095](../questions.d/QUESTION-095.md)'s staleness risk have no counterpart. (3) **Time.** Cost is total or average query time. There is no deadline, no peak load and no moment at which the work is done, which is the whole point of the cockpit's timing. (4) **Uncertainty about queries.** The mix is uniform or a known fixed distribution; the authors list dynamic materialization as untested future work, so Sleator and Tarjan's finding that reorganizing at use is near optimal is neither met nor answered. (5) **Retrieval medium and cues.** Every source is a table scanned at the same per-row rate. Perceptual reading, pop-out and cueing ([CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md) part 3) are outside it, and so is any choice between holding a result in the head and in the world: there is one store, and the only decision is what goes in it.
- *Speed bugs.* The bugs are precomputed answers stored where they are cheap to read, so the category fits. The model's content does not. There are four speeds for one approach, all needed; there is no lattice of answers derived from other answers, no budget that forces a choice, and the trivial solution is to store them all. What makes the bugs worth setting is that the computation is moved from a high-workload phase to a low-workload one and the reading becomes perceptual, and this model has neither phases nor reading modes. It is not a model of the speed bugs beyond naming the category.
- *Filed arguments.* The nearest fit of the three. If a filed argument or THEORY document is a general answer from which narrower questions are derived, the lattice and the marginal benefit carry over in outline: file the synthesis that serves the most unfiled questions at the largest saving, given what is already filed, and expect the second choice to depend on the first. But the record's arguments have no partial order of derivability with known costs, and deriving a narrow answer from a filed argument costs reading and reasoning, not something proportional to the argument's size. So this is an analogy with a usable term (coverage, with diminishing returns), not a model.
- *Reused inferences.* An answer derived from a stored ancestor here is exact. In the amortized-inference work of [QUESTION-095](../questions.d/QUESTION-095.md) the reused computation carries error into the new query; the record's cost of reuse is that bias, and this model has none. It covers the saving and not the cost.
- *LEGO bins.* Bins are an arrangement for finding items, an access path, which is Finkelstein et al.'s case, not this one. A data-cube view is an aggregate; a bin holds the items. This paper does not bear on the bins.
- *Net.* Of the five terms [QUESTION-095](../questions.d/QUESTION-095.md) named (precompute cost, storage and upkeep, retrieval cost, staleness risk, expected reuse), this paper prices storage and expected reuse (as weighted coverage) and retrieval cost (as rows scanned from the cheapest stored ancestor). It leaves precompute cost to a size proxy and omits upkeep and staleness. Together with the four readings, the terms are now each priced somewhere, but in five models with different units, and no one of them joins them.

**On [CLAIM-303](../claims.d/CLAIM-303.md).** Supports the break-even's structure for materialization and adds that value depends on what else is stored, so a rule that judges each item alone (for instance a fixed second-occurrence threshold) can misjudge it in either direction, as Example 4.1's f shows. It says nothing on [CLAIM-303](../claims.d/CLAIM-303.md)'s indexing, dependency tracking or refresh expenditures.
