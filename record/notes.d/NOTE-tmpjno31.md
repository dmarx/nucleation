---
status: Read
paper: LIT-tmpb43n3
title: Chaudhuri & Narasayya — An efficient, cost-driven index selection tool for
  Microsoft SQL Server
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the VLDB Endowment's own proceedings PDF (https://www.vldb.org/conf/1997/P146.PDF;
    10 pp., printed pages 146–155, the conference line (23rd VLDB Conference, Athens,
    Greece, 1997) and the VLDB copying notice on the first page; a scan with an
    OCR text layer, PDF metadata title matching the paper; sha256 96227fcc…54bde).
    A plain curl of that URL returns HTTP 403; the same URL, and the http and no-www
    forms, returned the PDF (200, application/pdf, 1,225,214 bytes) when requested
    with a browser User-Agent string. Text extracted with pdftotext, in layout and
    raw modes. The OCR misreads some characters (the second author's name as "Nqasayya",
    subscripts, "resuhs", run-together words) and Tables 1–4 and Figures 1, 2 and
    6–9 are images, so all four tables, Figures 1, 2 and 6–8, and the algorithm
    boxes (Figures 3, 4, 5, 10) were read from page images rendered at 110 dpi.
    Read: all nine sections, every figure and table, the footnotes and the reference
    list. Nothing skipped. Much is deferred to a technical report in preparation,
    [CN97] (how to choose the interaction threshold x and the seed size m, the branch-and-bound
    variant, the two-tier search, the Insert/Delete details, the example showing
    greedy can be arbitrarily bad, and index-only access); that report was not read,
    so those points are reported as the paper states them, unproven here. The works
    it cites (Finkelstein et al. 1988, Harinarayan et al. 1996) are described as
    it describes them. Every quotation below was checked by script against the raw-mode
    extracted text, with whitespace normalised.
date: '2026-10-15'
summary: >-
  The AutoAdmin tool picks at most k indexes (single- or two-column, clustered or
  not) for a given workload of SQL statements, minimising the unweighted sum of
  the optimizer's estimated costs of those statements, with hypothetical ("what-if")
  indexes made visible to the optimizer by loading their statistics into the catalog.
  Its contribution is search efficiency: candidates are restricted to indexes in
  some single query's best configuration, enumeration is Greedy(m, k) (an exhaustive
  seed of m indexes, then greedy additions), costs of most configurations are derived
  from a few "atomic" ones, and two-column indexes are generated only from winning
  single columns. On five TPC-D workloads this cut running time to 10–24% of a baseline,
  with estimated-cost quality 0–7% worse, and Greedy(2, 4) matched the exhaustive
  optimum on four of five workloads and was within 1% on the fifth. The cost model
  has no build cost, no storage term and no frequency weights, the budget is a count
  of indexes, the workload is fixed, there is no guarantee for the greedy step,
  and quality is never measured by executing anything.
---

# NOTE-tmpjno31: Chaudhuri & Narasayya — An efficient, cost-driven index selection tool for Microsoft SQL Server

## Contribution

An index selection tool built into Microsoft SQL Server 7.0 as part of the AutoAdmin project, whose stated aim is "to self-tune and self-administer database systems". Following Finkelstein, Schkolnick and Tiberio 1988 (DBDSGN), the tool does not model the optimizer; it asks it. The authors' reason: "a selection of indexes is only as good as the optimizer that uses it", and an external model must be kept consistent with "an evolving optimizer". What is new is not the objective but making the search affordable: fewer candidate indexes, fewer configurations enumerated, and fewer optimizer calls per configuration, plus an iterative way to bring in multi-column indexes. The paper is a systems paper. It has no theorem.

## Key insight

The expensive step in optimizer-driven index selection is calling the optimizer, and most calls are redundant. A query's cost under a configuration depends only on the indexes it could use, so it can be read off a few smaller configurations already costed. And the indexes worth considering for a workload are, nearly always, the ones that would be chosen for some single query in it. Interactions between indexes matter, but "the largest cost reductions often results from indexes that are good candidate indexes by themselves", so a small exhaustive seed followed by greedy additions catches the interactions that count.

## Assumptions

- **The objective.** "Given a configuration and a workload, we use the sum of the optimizer estimated costs for all the SQL statements in the workload as the metric of goodness." This is the "total cost"; the optimal configuration minimises it. Costs are the optimizer's estimates, not execution times.
- **The workload.** "A workload consists of a set of SQL data manipulation statements, i.e., Select, Insert, Delete and Update", captured in the implementation with the SQLTrace utility. No frequencies or weights appear in the definition. A trace may repeat statements, which would weight them by repetition, but the paper does not say so.
- **What is priced.** Query cost, and index upkeep through the update statements in the workload: an Insert/Delete's cost is split into selection, updating the table and the indexes used for selection, and updating the other indexes, and the last is taken as additive and independent across indexes, Cost(Q, {I}) − Cost(Q, { }) each (Section 3.1). There is no term for building an index, no storage term in the objective, and no maintenance outside the workload's statements.
- **The budget.** "The index selection process is subject to constraints, e.g., an upper bound on the number of indexes or storage space. In this paper, we describe our technique to deal with the problem of picking a configuration subject to an upper bound on the number of indexes." Space is named and not handled. Greedy(m, k) also stops when "no further reduction in cost is possible by adding an index", so update cost can make it pick fewer than k.
- **Physical options.** Single- or multi-column, clustered or non-clustered indexes, at most one clustered index per table. In the experiments, multi-column means width two. Join indexes and materialized views are left to future work.
- **A well-behaved optimizer.** Derived costs assume the optimizer picks the cheapest available atomic configuration, and "for a Select query, inclusion of an index in a configuration can only reduce cost".
- **What-if indexes.** SQL Server was modified so that for a hypothetical index "the server makes available to the optimizer the distribution information of the column(s) over which the index is defined"; queries are optimized in "no-execute" mode, returning a plan and a cost. The index itself is never built. The statistics are, and "The cost of gathering distribution information can be amortized over multiple executions of the tool and multiple workloads, since the statistics need to be gathered only once per index." This is the paper's only use of amortization, and it is the tool's own cost, not the database's.
- **A static, offline problem.** The tool takes one workload and recommends one configuration. Nothing changes the workload over time, and the tool is run by an administrator ("with administrator privileges since it needs to update system catalogs").

## Key results

**The algorithm (Figure 10).**

1. *Candidate index selection* ("query-specific-best-configuration", BEST-CONF; Figure 4). Split the workload of n statements into n one-statement workloads, run the tool itself on each with all that statement's indexable columns as candidates and no bound on the number of indexes, and take the union of the n best configurations. Rationale: "an index that is not part of the best design for even a single query in the workload, is unlikely to be part of the best design for the entire workload."
2. *Configuration enumeration* by Greedy(m, k) (Figure 5): take the best m-index configuration by exhaustive enumeration; then repeatedly add the one index that lowers total cost most; stop at k indexes or when no index lowers cost. m = 0 is pure greedy and m = k is exhaustive. The paper found "m=2 produced very good solutions". A branch-and-bound variant is mentioned and deferred to [CN97].
3. *Multi-column index generation* (MC-LEAD): from the single-column winners S, consider two-column indexes M(a, b) whose leading column a has an index in S. A stricter MC-ALL requires both a and b in S; MC-BASIC searches all single and multi-column indexes together.
4. Repeat 1 and 2 with the winners and the new two-column indexes. Width w needs w − 1 iterations.

**Cost evaluation.** A configuration is *atomic* for a workload if some query could use all its indexes in one execution. The cost of a non-atomic configuration is derived without calling the optimizer: for a Select/Update, the minimum over the largest atomic subsets; for an Insert/Delete, that minimum for selection plus the separate index-maintenance increments (Section 3.1). Atomic configurations are exponential in the number of tables, so they are limited heuristically to at most j indexes per table and indexes from at most t tables, with j = t = 2 ("single-join atomic configurations", SJ), or found adaptively by evaluating a configuration of size n + 1 only when a size-n configuration's evaluated cost is at least x% below its derived cost (Figure 3; how to choose x is deferred to [CN97]). Two further savings: a query's cost under C equals its cost under the indexes of C on its own indexable columns ("relevant index set optimization"), and is the no-index cost when there are none ("irrelevant index set optimization").

**Guarantees.** Only one, stated without proof: for the candidate selection step, "if the workload is free of updates (including insert and delete statements), and if we do not impose any bound on the number of indexes that may be chosen, then the configuration chosen by this algorithm has less or equal total cost for the workload compared to any other configuration." With updates or a bound it fails. Their example: if the best configuration for a query Q is an index on T1.C1 alone, and an insert U on T1 makes that index's predicted maintenance high, "it is possible for the index selection tool to not recommend any index", because the index on T2.C2 was never a candidate. For enumeration, "a greedy algorithm can be in principle arbitrarily bad for configuration enumeration [CN97]" (the example is not given here). Of the greedy bounds of Harinarayan et al. and Gupta et al.: "their results assume monotonicity, i.e., inclusion of one index does not have any impact on the effectiveness of another."

**Experiments (Section 7).** SQL Server 7.0, the TPC-D schema only; the database size or scale factor is not stated. Five workloads (Table 1):

| Workload | Joins | % pure queries | % updates | # admissible indexes |
|---|---|---|---|---|
| TPCD_1 | 0, 1, 2 | 70 | 30 | 75 |
| TPCD_2 | 3, 4, 5 | 70 | 30 | 143 |
| TPCD_3 | 0–5 | 100 | 0 | 123 |
| TPCD_4 | 0–5 | 50 | 50 | 108 |
| TPCD_0 | – | 100 | 0 | 124 |

TPCD_1–4 come from a synthetic workload generator; TPCD_0 is the 17 TPC-D benchmark queries. k = 10 unless stated. Quality is always the optimizer's estimated total cost.

- *Candidate selection* (Figure 6, Table 2). BEST-CONF keeps well under the admissible count on every workload and lost no quality on any, including the update-heavy TPCD_4. Capping candidates at one or two per query lost up to 82% (BEST-CONF-1: 1%, 82%, 47%, 0%, 15%; BEST-CONF-2: 0%, 4%, 0%, 0%, 2%, for TPCD_1, 2, 3, 4, 0).
- *SJ atomic configurations* (Figures 7, 8). Fewer atomic configurations evaluated, by 50% for TPCD_2 and 61% for TPCD_0, little for TPCD_1. At k = 10 the chosen configuration was identical to the unrestricted one; varying k from 2 to 10 on TPCD_2, quality was the same for k ≤ 5 and fell for 6 ≤ k ≤ 8, at most 7%.
- *Optimizer calls* (7.3.3). Down 79–92% across workloads; irrelevant-index-set optimization gave 58–84%, relevant-index-set a further 9–29%.
- *Greedy vs. exhaustive* (7.3.4). Greedy(2, 4) against exhaustive search for k = 4, without SJ. Greedy enumerated 2–7% of the configurations. It found the optimum on four of five workloads; on TPCD_4 it chose a different clustered index on lineitem, with "the absolute difference in cost between the optimal configuration and the one chosen by Greedy was very small" (under 1%).
- *Multi-column* (Figure 9, Table 3). Drop in quality against MC-BASIC: MC-LEAD 0%, 6%, 0%, 0%, 2%; MC-ALL 0%, 18%, 2%, 5%, 14%. MC-LEAD fails "only when neither a nor b is important as a single column index, but M (a, b) is important."
- *Whole tool vs. baseline* (Table 4). Baseline: non-iterative, no candidate selection, Greedy(2, k) with no SJ restriction. The tool's work as a percentage of the baseline's, for TPCD_1, 2, 3, 4, 0: candidate indexes 38, 33, 43, 32, 30; optimizer calls 52, 8, 11, 11, 3; configurations enumerated 51, 28, 57, 39, 33; running time 24, 12, 14, 18, 10. Drop in quality 0%, 7%, 6%, 0%, 1%, attributed to the multi-column approximation. "The overall running time of our algorithm improves by a factor of 4 to 10 over the baseline algorithm." Absolute times are not given.

## Bearing on the record

**On [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md): it prices organizing ahead no differently from Finkelstein, and in fewer terms.**

- **Same objective, narrower.** Like DBDSGN ([NOTE-tmphbty9](NOTE-tmphbty9.md)), it minimises a steady-state sum of per-statement costs taken from the optimizer, with upkeep entering only as the maintenance part of each Insert/Delete/Update in the workload. Unlike DBDSGN, the paper states no frequency weights, has no storage term in the objective, and enforces no page limit. Its budget is a count of indexes; storage space is named as a possible constraint and set aside. So the question's title, in which every further index "is paid for in space and upkeep", is half true of this tool: upkeep yes, space no.
- **"Paid once" is still unpriced.** No term for building an index. The index is never built during selection; only its statistics are, and the paper amortizes that over runs of the tool. So the one amortization in the paper is of the cost of deciding, not of organizing. The trade the question asks about, sorting as amortized search, one pass of organizing against later retrievals, does not appear.
- **No changing workload, no staleness.** One workload, one recommendation, run offline by an administrator. Self-tuning is the project's motive, not this tool's behaviour. Nothing here says when to rerun it, what to do when the mix drifts, or what a change of configuration costs. Bruno and Chaudhuri 2007 (not held, not read) is where that literature turns to it, according to the question.
- **What it does add.** Two things the record lacked. First, *deciding the arrangement has a cost of its own*, and it can dominate: the paper exists because costing candidate arrangements against the workload is too expensive to do exhaustively, and its savings are in the decision, not in the database. Second, *practical evidence that greedy works when interactions are confined*: a two-index exhaustive seed and greedy additions matched the optimum on four of five workloads, because big savings usually come from indexes good on their own, and the interactions that matter (a merge join on two clustered indexes, index intersection on one table) are few and local. That sits between Harinarayan et al. ([LIT-tmptn63k](../literature.d/LIT-tmptn63k.md): greedy ≥ 63% under monotone benefit, proved) and this paper's own remark that greedy can be arbitrarily bad without monotonicity (asserted, example deferred). It is evidence on five TPC-D workloads, by estimated cost, not a bound.
- **Its one stated guarantee fails exactly where upkeep enters.** Candidate selection is exact only with no updates and no bound; with an insert whose maintenance outweighs a query's best index, the tool may recommend nothing. Upkeep breaks the decomposition of a workload into per-query best choices. Piatetsky-Shapiro's set-cover hardness ([NOTE-tmpxc25d](NOTE-tmpxc25d.md)) is the formal side of the same coupling; this paper meets it in practice and reports it did not hurt on its workloads.

**On [CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md): consistent with parts 1 and 2 by construction; nothing on part 3.**

- **The query mix.** The tool's answer is a function of the workload and nothing else, so the cheapest arrangement depending on the mix is assumed, not tested. One clustered index per table is the constraint the question calls one arrangement, as in Finkelstein. It does not meet the claim's defeat condition and does not add evidence beyond Finkelstein.
- **The bin budget.** The bound of at most k indexes is the nearest thing to a fixed number of bins, but it bounds the number of access paths, not the number of parts of one partition. A LEGO builder's k bins are one clustered order with k values; this paper's k is how many secondary orders to keep. The claim's k/2 + N/(2k) trade within one partition has no counterpart here.
- **A builder choosing bins for a mix of searches, by analogy only.** Three of the tool's heuristics translate and are untested on bricks. (a) Consider only sortings that would be best for at least one kind of search the builder makes, then choose among them; this fails when keeping a sorting up costs more than one search type saves, which for bins is putting new bricks away. (b) Choose the first sorting carefully and add the rest greedily, since most of the saving comes from sortings good on their own. (c) Consider sorting within a bin by b only if sorting by a alone was worth it (MC-LEAD). Part 3 of the claim says sorting on either attribute turns a conjunction search into a feature search, so single attributes are good alone, which is the case MC-LEAD handles and not the one where it fails.
- **Only as good as the optimizer that uses it.** The paper's founding point is that an index's worth is its worth to the procedure that searches, which it gets by asking that procedure. For the builder, the procedure is the eye, and part 3 of the claim (what stands out within a bin) is the optimizer's plan choice in that analogy. A database lookup has nothing like pop-out, and this paper's costs come from an optimizer, not a perceiver, so it supplies the method (cost each arrangement by the searcher's own estimate) and none of the magnitudes.

**What it does not show.** Nothing about real execution times: every quality figure is an optimizer estimate, and the optimizer's errors are the tool's errors. Nothing beyond TPC-D, two-column indexes and k ≤ 10. No theorem, and the details behind several heuristics are in a report that was in preparation.
