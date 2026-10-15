---
number: 890
status: Read
formerly:
- NOTE-tmp5yp6e
paper: LIT-1092
title: Gupta & Mumick — Selection of views to materialize under a maintenance cost
  constraint
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' PostScript copy on the Stanford
    InfoLab papers server, http://infolab.stanford.edu/pub/papers/update.ps (288,171
    bytes, sha256 fc4ad341…b9784; dvips output of "paper.dvi" dated 8 October 1998;
    18 pages, LLNCS style; the directory listing dates it 9 December 1998 and pairs
    it with update.abs, an abstract naming both authors). The Stanford data-warehousing
    project's publication page (http://infolab.stanford.edu/warehousing/publications.html)
    lists the paper as "Selection of Views to Materialize Under a Maintenance-Time
    Constraint", ICDT, Jerusalem, January 1999, and links Gupta's personal copy
    (http://infolab.stanford.edu/~hgupta/ps/update.ps), which returned HTTP 403,
    as did the www-db.stanford.edu form; the https form reset the connection. The
    copy read carries the ICDT title "Selection of Views to Materialize Under a
    Maintenance Cost Constraint", the authors' 1999 affiliations (Stanford; Savera
    Systems) and the camera-ready date, and its 18 pages match the 18 of LNCS 1540
    pp. 453–470. It is the conference paper, not the 2005 IEEE TKDE journal version
    or Gupta's 1997 ICDT paper (LIT-1091), which it cites as [Gup97]. Its pagination
    is the preprint's, and it was not compared with Springer's typeset text, so
    page numbers and any late changes are unconfirmed. Other places looked: Unpaywall
    and OpenAlex report the DOI closed with no repository copy; Semantic Scholar
    gives openAccessPdf CLOSED; the ilpubs.stanford.edu:8090 report server timed
    out; Gupta's Stony Brook page (www3.cs.stonybrook.edu/~hgupta/) redirects to
    hgupta.org, and the guessed ps/ and papers/ paths there returned 404; Springer
    and ACM were not tried. The PostScript was converted with ps2pdf and the text
    extracted with pdftotext (layout and raw modes). The extraction drops the fi/ff
    ligatures and garbles ≤, ≥, ∅, τ, sums and A*, so the problem statement (§4),
    the definition of benefit and effective maintenance cost (§5), Algorithm 1,
    Definition 8, Lemma 1 and its proof, Theorems 1 and 2, the time-complexity paragraph,
    Algorithm 2, the lower bound h(x) and Theorem 3 were checked against page images
    rendered at 110 dpi. Read: abstract, all eight sections, every definition, example,
    algorithm, lemma and theorem, the experiments and Figure 6, and the reference
    list. Nothing skipped. The paper proves Lemma 1 only; Theorems 1, 2 and 3 and
    the claim that the guarantees survive query frequencies that fall as other views
    are materialized are stated without proof ("It can be shown"), so they are reported
    as stated. Every quotation below was checked by script against the extracted
    text with whitespace removed and, because the extraction drops them, the letter
    pairs fi, ff and fl removed from both sides, and line-end hyphens in the extraction
    joined; titles quoted from the Stanford web page and the record's own wording
    are quoted from those sources, not the paper.
date: '2026-10-15'
summary: >-
  Gupta and Mumick choose views to materialize so as to minimize frequency-weighted
  query cost subject to a cap S on total maintenance time, the sum over chosen views
  of update frequency times a per-update maintenance cost that depends on which
  other views are stored. Because storing one view can make another cheaper to maintain,
  benefit per unit of maintenance is not monotone and the single-view greedy of
  earlier work can be arbitrarily bad. For OR view graphs (each view computed from
  one other, as in data cubes) a greedy that adds whole "inverted tree sets" gets
  at least 1 − 1/e (63%) of the benefit of an optimal solution that may use as much
  maintenance as the greedy did, the greedy using up to 2S, assuming no inverted-tree
  piece of the optimum alone exceeds S (Theorem 1, unproved here); without that
  assumption it gets half the optimum's benefit per unit of maintenance (Theorem
  2). Each greedy stage enumerates exponentially many sets in general; for general
  AND-OR graphs there is only an exact A* search with exponential worst case. Upkeep
  is a budget, not a term traded against query savings; build cost, storage and
  staleness are not modelled, and the experiments are on random graphs of 10 to
  25 nodes.
---

# NOTE-890: Gupta & Mumick — Selection of views to materialize under a maintenance cost constraint

## Contribution

Earlier view-selection results with guarantees (Harinarayan, Rajaraman and Ullman, [LIT-1094](../literature.d/LIT-1094.md); Gupta, Harinarayan, Rajaraman and Ullman on indexes; Gupta 1997, [LIT-1091](../literature.d/LIT-1091.md)) all budget disk space. The authors argue space is the wrong budget: "In practice, the real constraining factor that prevents us from materializing everything at the warehouse is the maintenance time incurred in keeping the materialized views up to date at the warehouse." They pose the maintenance-cost view-selection problem, show why it is harder than the space-budget problem, give a set-at-a-time greedy with a 63% guarantee for OR view graphs, an exact A* search for general AND-OR view graphs, and a small experiment. They present it as answering one of the open questions of [LIT-1091](../literature.d/LIT-1091.md), and say "Ours is the first article to address the problem of selecting views to materialize in a data warehouse under the constraint of a given amount of total view maintenance time."

## Key insight

Maintenance costs interact. A stored view can be maintained from another stored view's changes more cheaply than from the base data, so "the maintenance cost of a view v depends on the set of other materialized views", and adding a view can lower total maintenance (the effective maintenance cost "may be negative"). Then two dependent views together can be worth more benefit per unit of maintenance than either alone, and a greedy that adds the best single view "could deliver an arbitrarily bad solution". The repair is to let the greedy add groups: in an OR view graph, the views of any solution split into trees along which changes flow (the update graph), and the effective maintenance costs of those trees sum to no more than that of the whole (Lemma 1). Greedy over such trees ("inverted tree sets") recovers the usual 1 − 1/e argument.

## Assumptions

- **Data and workload.** An AND-OR view graph over base relations; each node v has a query frequency f_v, an update frequency g_v and a reading cost R_v. Frequencies are fixed numbers. The paper notes it does not assume query and update frequencies independent, and says the guarantees hold when a view's query frequency falls as other views are materialized (stated, not proved).
- **Cost models.** "We do not make any assumptions about the query or the maintenance cost models." Q(v, M) is the cheapest evaluation of v from M plus the base relations. In general AND-OR graphs UC(v, M) is an arbitrary given function. In OR view graphs, edges carry a query cost and a maintenance cost; Q(v, M) is the shortest query-length path to a stored view or base relation (including that node's reading cost) and UC(v, M) the shortest maintenance-length path to a stored view or base relation other than v.
- **Objective and constraint (§4).** Minimize τ(G, M) = Σ_{v∈V(G)} f_v Q(v, M) subject to U(M) ≤ S, where U(M) = Σ_{v∈M} g_v UC(v, M). Maintenance appears only in the constraint.
- **Operating picture.** "Usually, changes to the source data are queued and propagated periodically to the warehouse views in a large batch update transaction." The batch runs overnight, so S is the length of the update window. Every chosen view is fully refreshed in each window.
- **Knapsack effect.** A solution may exceed the budget "slightly"; "This assumption is made to ignore the knapsack component of the view-selection problem." Guarantees compare against an optimum allowed the same amount of maintenance as the solution found.
- **Not modelled.** The cost of first building (materializing) a view, storage, how stale a view may be or what serving stale answers costs, uncertainty about future queries or updates, and changing workloads. The abstract lists "materialization time" among possible resources; no result uses it.

## Key results

Notation: B(C, M) = τ(G, M) − τ(G, M ∪ C) is the query benefit of adding C; EU(C, M) = U(M ∪ C) − U(M) its effective maintenance cost.

- **Hardness.** The space-budget problem is the special case in which each view's maintenance cost is independent of the others, so the problem is "trivially NP-hard" by the set-cover reduction of [LIT-1091](../literature.d/LIT-1091.md). No inapproximability result is given.
- **Non-monotonicity (§2, Example 2, Figure 4).** In the space-budget problem, benefit per unit space of a set of views never exceeds that of its best member (Definition 1, the "monotonicity property"). Here it can: in Figure 3, benefit per unit maintenance of {V2}, {V3} and {V2, V3} is 1, 1 and 7/4. With budget 4, single-view greedy picks {V1} (benefit 5) while {V2, V3, V4, V5} has benefit 11 at the same maintenance; Figure 4 extends this to an optimum of arbitrarily large benefit with greedy unchanged. The paper names this non-monotonicity of benefit per unit cost; it does not use the word submodularity.
- **Lemma 1 (proved).** In an OR view graph, for any M, a set O splits into inverted tree sets O_1, …, O_m (the trees of its update graph) with Σ EU(O_i, M) ≤ EU(O, M). The proof rests on the step Rd(M, O) ≤ Σ Rd(M, O_i), the reduction in M's maintenance due to O being at most the sum of the reductions due to its parts, which is asserted rather than argued.
- **Algorithm 1 (Inverted-tree greedy).** Repeatedly add the inverted tree set T disjoint from M with EU(T, M) ≤ S and the largest B(T, M)/EU(T, M), until U(M) ≥ S.
- **Theorem 1 (stated, no proof).** For an OR view graph and budget S, Algorithm 1 returns M with U(M) ≤ 2S and query benefit at least (1 − 1/e) ≈ 63% of that of an optimal solution whose maintenance cost is at most U(M), "under the assumption that the optimal solution doesn't have an inverted tree set" O_i with U(O_i) > S. The authors defend the assumption: "The simplifying assumption made in the above algorithm is almost always true, because U(M) is not expected to be much higher than S."
- **Theorem 2 (stated, no proof).** Without that assumption, U(M) ≤ 2S and B(M, ∅)/U(M) ≥ 0.5 B(O, ∅)/S for an optimal O with U(O) ≤ S. This bounds benefit per unit of maintenance, not benefit.
- **Running time.** A stage considers every inverted tree set; a node v with A_v ancestors roots 2^{A_v} of them, so a stage costs Σ_v 2^{A_v}, "which is in the worst case exponential in n". For a balanced binary tree a stage is O(n²). The paper does not note that in a data-cube lattice, its leading application, the finest view has every other view as an ancestor, so by its own count a stage there is exponential in the number of views. Space is polynomial.
- **Algorithm 2 and Theorem 3 (A*, stated, no proof).** For general AND-OR graphs, an A* search over a binary include/exclude tree in inverse topological order, with g(x) the query cost of views decided so far and h(x) a lower bound from filling the remaining budget with undecided views in order of p(v)/s(v), where s(v) = g_v UC(v, N) is a view's least possible maintenance and p(v) = f_v Q(v, N − {v}) its least possible query cost if not stored. Theorem 3: it "returns an optimal solution". It "can take exponential time in the number of nodes in the view graph", and its space is exponential.
- **Experiments (§7).** Random OR view graphs, balanced trees and DAGs of varying edge density, 10 to 25 nodes, random frequencies, the linear cost model of [LIT-1094](../literature.d/LIT-1094.md), S from the cost of the cheapest view to that of all views. Inverted-tree greedy "returned an optimal solution for almost all (96%) view graph instances", and about 95% of optimal benefit otherwise. For trees and graphs under 40% edge density it ran 10 to 500 times faster than A*; on very dense graphs A* could be marginally faster. Optimality was judged against A*. No real workload, no measured query or maintenance times.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): it prices upkeep, as a budget; it does not price staleness or building; it does not close the question.**

- **Upkeep is priced, and more carefully than in [LIT-1091](../literature.d/LIT-1091.md).** U(M) = Σ g_v UC(v, M) charges each stored view its update frequency times its per-update maintenance cost, and lets that cost depend on what else is stored. Upkeep here is a resource drawn from a fixed window, not a term added to query cost: the model minimizes query cost subject to U(M) ≤ S. So it does not trade a unit of upkeep against a unit of query savings. It answers the question of which views to keep given this much maintenance time; a joint model would also answer how much maintenance time is worth spending Sweeping S traces a frontier between the two, which the paper does not do.
- **Staleness is not priced at all.** Staleness is fixed outside the model by the operating picture: changes queue during the day and every chosen view is refreshed in the overnight batch. Query answers are treated as equally good whether or not a view's source has changed since the last batch, there is no option to refresh a view less often, and no cost of a stale answer. The budget S is how long the refresh window is, not how fresh the views must be.
- **Build cost is not priced.** First materialization appears nowhere in the model; it would matter for the question's "build" term only if the workload or view set changed, and both are static here. Storage is dropped deliberately ("disk-space is very cheap in real life").
- **The guarantee is narrow.** It holds only for OR view graphs; it is bicriteria (up to twice the budget, compared against an optimum given the larger budget); Theorem 1 adds an assumption on the unknown optimum; Theorem 2 bounds only benefit density; Theorems 1 to 3 are not proved in the paper; and the greedy is not polynomial in general, including on the data cube its authors name as the main case. For general AND-OR graphs there is no approximation guarantee, only an exact search with exponential worst case.
- **What it adds to the "amortized search" reading.** Upkeep is not additive across stored structures: one stored result can make another cheaper to keep current, so the effective upkeep of adding a structure can be negative, and the value of stored results per unit of upkeep is not monotone. Any joint cost model for precomputation has to price upkeep of the set, not of each item, or it inherits the arbitrarily bad behaviour of Example 2. That is a constraint on the form the record's model can take, and the clearest result here for the question.
- **Relative to the other readings.** It does what [LIT-1091](../literature.d/LIT-1091.md) left open, for OR graphs and under the stated assumptions. It keeps the query-cost objective and (1 − 1/e) form of [LIT-1094](../literature.d/LIT-1094.md). It does not come closer to a joint model than Bruno & Chaudhuri 2007 ([LIT-1095](../literature.d/LIT-1095.md)), which the record holds as the closest; this paper has one cost in the objective and one in the constraint, with build and staleness absent.
- **On the record's filing ([LIT-1092](../literature.d/LIT-1092.md)).** The filing's summary, view selection "that maximizes query benefit while capping the total time spent keeping the stored views current", is accurate, as is "This paper makes upkeep the budget". It should not be read as a cost model that balances upkeep against savings, and nothing in it bears on staleness.
