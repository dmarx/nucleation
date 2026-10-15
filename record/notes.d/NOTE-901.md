---
number: 901
status: Read
formerly:
- NOTE-tmpuaboe
paper: LIT-1080
title: Gupta & Mumick — Selection of views to materialize in a data warehouse (TKDE
  2005)
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the first author's own copy, linked as "PDF"
    against "H. Gupta, I. Mumick. Selection of Views to Materialize in a Data Warehouse.
    IEEE Transactions of Knowledge and Data Engineering (TKDE), 17 (1), 2004" on
    Gupta's publication list (https://hgupta.org/publications/), at https://www3.cs.stonybrook.edu/~hgupta/ps/sel-views-tkde.pdf
    (605,049 bytes, sha256 77c5d3ab…cfdf4, 41 pages, US letter, single column, produced
    by AFPL Ghostscript 6.50). The Stony Brook server answered 200 with a browser
    User-Agent. The copy is the authors' manuscript of the journal paper, not IEEE's
    typeset text. Its title and affiliations (SUNY Stony Brook; Kirusa Inc.) match
    Crossref's record for the DOI, it cites work up to 2003, it names the ICDT 1997
    and ICDT 1999 papers as where the work "first appeared", and its content is
    the merger of both. It was not compared with the 20 typeset pages (pp. 24–43),
    so page numbers below are the manuscript's and changes made at proof are unknown.
    Other places looked, all 2026-10-15: Unpaywall (closed, no OA location, no repository
    copy); OpenAlex (closed; its only other location is a CiteSeerX summary page,
    10.1.1.30.3892, not fetched); Semantic Scholar (openAccessPdf CLOSED, and its
    record conflates the DOI with the 1997 ICDT paper); www3.cs.stonybrook.edu/~hgupta/
    itself (an HTTP 200 page of 403 bytes), whose content now lives at hgupta.org.
    IEEE Xplore was not tried. The PDF's fonts are Type 3 with custom encodings,
    so pdftotext gives gibberish; pages were rendered at 200 dpi with pdftoppm and
    read by OCR (tesseract). OCR garbles sums, τ, φ, Greek letters and some subscripts,
    so the objective (p. 7), Section 4.3 and Lemma 1 (p. 15) were checked against
    page images, and theorem statements are given from the OCR where it reads cleanly.
    Read: abstract, all eight sections, every definition, observation, algorithm,
    lemma and theorem, the proofs given (Theorems 1, 2 and 8 in the text; Lemmas
    1 to 5 in Appendix A; Theorem 10 and Algorithm 6 in Appendix B), the experiments
    and Figure 7, Table 1 and the references. Nothing skipped. Not proved here:
    Theorems 3 and 5 (said to be similar to Theorems 1 and 2), Theorem 4 (it follows
    from Lemmas 1 and 2), Theorems 6, 7 and 9 (proofs referred to Gupta's 1999 Stanford
    thesis), the 63% inapproximability for OR graphs, and the claim that the maintenance
    guarantees survive falling query frequencies. The comparison with the conference
    version was made against the ICDT '99 text read for LIT-1092 (InfoLab copy,
    extracted text kept with that reading) and against the record's reading of the
    ICDT '97 paper (LIT-1091, NOTE-889). Every quotation below was checked
    by script against the OCR text, whitespace normalised and curly quotes straightened,
    except one sentence of Section 4.3 (on C1 ∪ C2) and the comment in Algorithm
    6 (on the knapsack effect), which the OCR garbles and which were checked against
    the page images (pp. 15 and 41); the quotations of the publication list and
    of the record's filing were checked against those sources.
date: '2026-10-15'
summary: >-
  The journal paper merges Gupta's 1997 space-budget results and the 1999 maintenance-budget
  results into one article; it adds proofs, not new problems or new guarantees.
  Theorem 8 (the conference Theorem 1: inverted-tree greedy on OR view graphs, at
  most 2S of maintenance, at least 1 − 1/e of an optimum with the same maintenance,
  assuming no inverted-tree piece of the optimum exceeds S) and Theorem 10 (A* is
  exact on AND-OR graphs) are now proved, while Theorem 9 (the assumption-free half-density
  bound) is referred to Gupta's thesis. The maintenance-budget guarantee stays confined
  to OR view graphs, the greedy stays exponential in the worst case, and the two
  constraints are never combined. The only place upkeep is traded against query
  cost is the 1997 formulation carried over, query cost plus maintenance cost minimized
  under a space budget, with a guarantee only for AND view graphs in which every
  view is queried more often than it is updated; build cost and staleness are not
  modelled anywhere.
---

# NOTE-901: Gupta & Mumick — Selection of views to materialize in a data warehouse (TKDE 2005)

## Contribution

The paper says what it is: "The work presented in this article is an extension and generalization of the work in [10], and first appeared in [15] and [18]", that is, of Harinarayan, Rajaraman and Ullman ([LIT-1094](../literature.d/LIT-1094.md)), and in Gupta's ICDT 1997 paper ([LIT-1091](../literature.d/LIT-1091.md)) and Gupta and Mumick's ICDT 1999 paper ([LIT-1092](../literature.d/LIT-1092.md)). Sections 2 to 5 are the 1997 framework and its space-budget results (OR view graphs, AND view graphs, each with indexes, AO-greedy and r-level greedy for general AND-OR graphs), renumbered and with some proofs added. Section 6 is the 1999 maintenance-budget paper, with the proofs that paper left out partly supplied and a fuller account of its experiments. Related work is updated to 2003, and the conclusion lists the results in one table. There is no new problem, model or guarantee.

## Key insight

Unchanged from the two papers it merges. A greedy that adds the item of greatest benefit per unit of resource gets 1 − 1/e of the optimum's benefit for the resource it ends up using, provided benefit is subadditive over the pieces an optimum splits into (the "monotonicity property"). Maintenance cost breaks this two ways. In the objective, one stored view can make another cheaper to maintain, so "the benefit of C1 ∪ C2 might be more than the sum of their benefits individually" (Section 4.3, checked against the page image). As a budget, effective maintenance cost is not additive, so benefit per unit of maintenance is not monotone. The paper repairs the first only for AND view graphs where reads outnumber updates, and the second only for OR view graphs, by greedy over inverted tree sets.

## Assumptions

- **Model.** AND-OR view graph; each node has space S_v, query frequency f_v, update frequency g_v and reading cost R_v. New in the journal text: g_v "is the sum of the update frequencies of all the base relations used for derivation of the view. Here, we only consider direct updates on base relations and assume that the updates on base relations are independent."
- **General objective (Section 2.3, p. 7, page image).** Minimize τ(G, M) = Σ_{i=1..k} f_{q_i} Q(q_i, M) + Σ_{i=1..m} g_{V_i} UC(V_i, M) subject to Σ_{v∈M} S_v ≤ S. "In this article, we have ignored maintenance costs except in Section 4.3 and Section 6." Section 4.3 uses this objective; Section 6 replaces it.
- **Maintenance-budget problem (Section 6.1).** Minimize τ(G, M) = Σ_{v∈V(G)} f_v Q(v, M) subject to U(M) = Σ_{v∈M} g_v UC(v, M) ≤ S. No space constraint. "In this article, we do not discuss various maintenance cost models possible for an AND-OR view graph, and hence we assume that the function UC is given as part of an input with the AND-OR graph." In OR graphs UC(v, M) is the shortest maintenance-length path from v to a stored view or base relation.
- **Operating picture,** as in 1999: "Usually, changes to the source data are queued and propagated periodically to the warehouse views in a large batch update transaction." Every stored view is refreshed in each batch.
- **Data cubes are update-free** in the OR-graph space results: "As OLAP databases have very few or no updates at the base table, we assume that there are no maintenance costs at the materialized views throughout this section."
- **Guarantees are bicriteria and on benefit,** compared with an optimum given the resource the algorithm actually used.
- **Not modelled.** The one-time cost of building a view (the abstract still lists "materialization time" among possible resources; no result uses it), staleness or deferred refresh, changing workloads, and any combination of the space and maintenance constraints.

## Key results

Theorem numbers are the journal's; the 1997 and 1999 numbers are given where they help.

- **Space budget, OR view graphs, no updates (Theorem 1).** The single-view greedy (O(kn²)) uses at most S + r space, r the largest view, and its absolute benefit is at least (1 − 1/e) of the optimum in that space. Proved here; the 1997 paper stated the OR case without proof and proved the AND case. With a hard budget, the better of greedy-minus-last-view and the best single view gets (1 − 1/e)/2 ("It can be easily shown"). No polynomial algorithm beats 63% on OR view graphs unless P = NP, by "a very natural reduction" from set cover with Feige's threshold; the reduction is not given (1997 credited it to a personal communication).
- **Indexes (Theorems 2 and 5).** Inner-level greedy, at most 2S, at least 1 − 1/e^0.63 ≈ 0.467, assuming no structure exceeds S; Theorem 2 (OR) proved, Theorem 5 (AND) not.
- **AND view graphs (Theorem 3), no updates.** As Theorem 1; proof omitted as similar.
- **Upkeep in the objective (Section 4.3, Lemmas 1–2, Theorem 4).** In an AND view graph, if at every view the update frequency is below the query frequency, B(v, ∅) ≥ B(v, M) (Lemma 1), benefit is subadditive over single views (Lemma 2), and the greedy's absolute benefit is at least (1 − 1/e) of the optimum achievable in the space it uses (Theorem 4, which again omits the S + r statement). A footnote, not in the 1997 reading's account, says of Lemma 1: "The claim doesn't hold for OR view graphs." Lemma 1's proof (Appendix A) still rests on bounds the model does not state: Q(v, ∅) ≥ Q(v, M) ≥ UC(x, M) − UC(x, M ∪ {v}) for stored x, and Q(v, ∅) − Q(v, M) ≥ UC(v, v) − UC(v, M). So, as in 1997, the guarantee holds for maintenance costs bounded by query costs, not for an arbitrary UC.
- **General AND-OR graphs, space budget (Theorems 6 and 7).** "Unfortunately, we couldn't devise a polynomial time algorithm for the general AND-OR view graphs that delivers a competitive solution." AO-greedy: at most 2S, at least 1 − 1/e, exponential in the edges of the intersection graph. r-level greedy: at most 2S, at least g(r + 1) with g(r) = 1 − 1/e^{g(r−1)}, g(0) = 1, time O((kn)^{2r}) excluding the last level. Lemmas 3 and 4 are proved in Appendix A; the theorems' proofs "can also be found in [14]", the thesis. Footnote 9 still asserts, without showing, that maintenance costs "can be incorporated by adding additional nodes".
- **Maintenance budget: non-monotonicity (Examples 1–2, Figures 4–5).** Same as 1999: benefit per unit maintenance of {V2}, {V3}, {V2, V3} is 1, 1 and 7/4; single-view greedy picks {V1} (benefit 5) where {V2, V3, V4, V5} gets 11 for the same budget 4, and Figure 5 makes the gap arbitrary. "The effective maintenance-cost may be negative. The results in this section hold nevertheless."
- **Lemma 5 (was Lemma 1).** In an OR view graph, any O splits into inverted tree sets O_1, …, O_m with Σ EU(O_i, M) ≤ EU(O, M). Proof as in 1999, with the step Rd(M, O) ≤ Σ Rd(M, O_i) now justified: "as any view uses at most one view to help maintain itself".
- **Theorem 8 (was Theorem 1), now proved.** For an OR view graph and budget S, the inverted-tree greedy (Algorithm 4) returns M with U(M) ≤ 2S and query benefit at least (1 − 1/e) of an optimal solution whose maintenance cost is at most U(M), "under the assumption that the optimal solution doesn't have an inverted tree" set O_i with U(O_i) > S (statement as in 1999; OCR of p. 26). The proof is the 1997 argument with effective maintenance in place of space: by Lemma 5 and subadditivity of query benefit, some piece O_i has benefit per unit effective maintenance at least B(O, M)/k, k = U(M); the assumption makes O_i eligible (EU(O_i, M) ≤ U(O_i) ≤ S); the usual recurrence gives 1 − 1/e. The ratio argument divides by effective maintenance costs, which the paper allows to be negative; that case is not treated in the proof, and Algorithm 4's test B/EU > B_c would pass over a set with negative effective cost and positive benefit. The assumption is defended as before: "The simplifying assumption made in the above algorithm is almost always true, because U(M) is not expected to be much higher than".
- **Theorem 9 (was Theorem 2).** Without the assumption, U(M) ≤ 2S and B(M, ∅)/U(M) ≥ 0.5 B(O, ∅)/S for an optimal O with U(O) ≤ S. Still not proved in the paper: "(see [14] for proof)".
- **Falling query frequencies.** Unchanged: "It can be shown that the above performance guarantees hold even when the query frequency of a view decreases with the materialization of other views." No proof.
- **Running time.** "In the worst case the total number of inverted tree sets in an OR view graph G is exponential in the size of the graph." Balanced binary trees: O(n²) per stage. The conference's explicit count (a node with A_v ancestors roots 2^{A_v} inverted tree sets) is dropped, and Table 1 gives the greedy's complexity as "Exponential", footnoted "polynomial in the number of inverted tree sets". The sparsity argument for data cubes (3^n edges on 2^n vertices, edge density about 0.75^n) is kept from 1999; it concerns edge density, and does not address that in a cube lattice the finest view has every other view as an ancestor, so the number of inverted tree sets, and a greedy stage, is exponential there. Nothing in the running-time claims is corrected.
- **Theorem 10 (was Theorem 3), now proved.** A* (Algorithm 5) on general AND-OR graphs returns an optimal solution. Appendix B gives the lower bound h(x) as Algorithm 6 (fill the remaining budget S − U(M_x) with undecided views by profit p(v) = f_v Q(v, N − {v}) per least maintenance s(v) = g_v UC(v, N), first setting aside the most profitable view, "To nullify the 'knapsack' effect") and proves h(x) ≤ h*(x). Worst case exponential time and space.
- **Experiments (Section 6.5).** The same results as 1999 (random OR graphs and balanced trees, 10 to 25 nodes; greedy optimal in 96% of instances, about 95% of optimal benefit otherwise; 10 to 500 times faster than A* below 40% edge density, A* marginally faster on very dense graphs), now with the cost model stated: linear query cost; maintaining u from stored descendant v costs time proportional to |Δu| + |Δv|, taken proportional to |u| + |v|; view sizes random but smaller than their descendants'. Figure 7 shows balanced trees and 10%, 15%, 25% and 40% density (the 1999 figure also had 80%). A* could not run beyond about 25 nodes for memory. No real workload.
- **Open problems (Section 8).** "there is still very little known on the approximability of the view-selection problem in general AND-OR view graphs"; "the view-selection problem in AND view graphs is not yet known to be NP-hard".

### Diff from the ICDT '99 paper ([LIT-1092](../literature.d/LIT-1092.md)), item by item

- (a) **Proofs.** Theorem 1 → Theorem 8: proved. Theorem 3 → Theorem 10: proved, with h(x) formalized. Theorem 2 → Theorem 9: not proved, referred to the thesis. The falling-query-frequency claim: not proved. Lemma 1 → Lemma 5: same proof, the sub-additivity step now given a one-line reason.
- (b) **Beyond OR graphs, under maintenance.** No. The inverted-tree greedy and its guarantees remain for OR view graphs only; general AND-OR graphs get only exact A*. The AND and AND-OR results in the article are space-budget results from 1997.
- (c) **Space and maintenance together.** No. Sections 2–5 use a space budget, Section 6 a maintenance budget; no problem has both.
- (d) **Trading upkeep against query cost.** Only in the 1997 objective carried over (Section 4.3): τ = query cost + maintenance cost under a space budget, with a guarantee only for AND view graphs where every view's update frequency is below its query frequency (Theorem 4), and only under unstated bounds of maintenance savings by query costs. Section 6 keeps upkeep as a budget, not a cost.
- (e) **Staleness, build cost, storage.** Storage is the 1997 space budget. No build cost; no staleness; refresh is a full batch per period, as before.
- (f) **Corrections.** None of substance. Theorem 8 keeps the assumption on the optimum. The worst-case count of inverted tree sets is generalized to "exponential" but the data-cube case is not addressed. The new text states that update frequencies are sums over independent base-relation updates.
- (g) **Experiments.** No new experiments; the 1999 results restated, with the maintenance cost model now described and one density panel fewer.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): this version does not change the answer. Bruno and Chaudhuri 2007 ([LIT-1095](../literature.d/LIT-1095.md)) stays the closest.**

- **No joint build–upkeep–staleness model.** The journal paper contains two models and never joins them. One (from 1997) puts upkeep in the objective, query cost plus maintenance cost, under a space budget; the other (from 1999) puts upkeep in the budget and query cost alone in the objective. Neither prices first materialization or staleness, and every stored view is refreshed in each batch.
- **The one trade-off has a narrow guarantee.** Where upkeep is traded against query savings, the greedy guarantee holds only in AND view graphs (one plan per view) with every view queried more often than updated, and only for maintenance costs bounded by query costs, which the model does not state. The new footnote makes the limit explicit: the key lemma "doesn't hold for OR view graphs", the class that contains data cubes.
- **What the proofs settle.** With Theorem 8 proved, the record can treat the OR-graph result as a theorem rather than a claim: under a maintenance budget, greedy over inverted tree sets gets 1 − 1/e of an optimum allowed the same maintenance, at up to twice the budget, assuming no tree-piece of the optimum alone exceeds the budget. It remains bicriteria, OR-only and exponential-time in general. The half-density bound without the assumption is still unproved here. The point the NOTE for [LIT-1092](../literature.d/LIT-1092.md) drew, that upkeep must be priced for the set, not per item, because stored items make each other cheaper to keep, is the same here and now rests on a proved lemma.
- **On the record's filing ([LIT-1080](../literature.d/LIT-1080.md)).** The filing calls this "The journal version of the ICDT '99 paper on choosing views to materialize under a maintenance-time constraint." That understates it: it is the journal version of both the 1997 and 1999 ICDT papers, and most of its pages are the 1997 space-budget results. The filing's "Why this is here" expected it to settle that the conference version "stated its guarantees without proof and covered OR view graphs only". It settles the first in part (Theorems 8 and 10 proved, Theorem 9 not) and not the second.
