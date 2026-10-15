---
status: Read
paper: LIT-tmpn0tsb
title: Gupta — Selection of views to materialize in a data warehouse
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the author's PostScript copy on the Stanford
    InfoLab papers server (http://infolab.stanford.edu/pub/papers/SelectionViews.ps,
    200,257 bytes, 15 pages, LLNCS style, dvips-dated 5 March 1997), linked as "In
    Proceedings of the International Conference on Database Theory, Athens, Greece,
    January 1997" from the Stanford warehousing project's publication page (http://infolab.stanford.edu/warehousing/publications.html).
    The copy's 15 pages match the 15 of LNCS 1186 pp. 98–112, but its pagination
    is the preprint's, so the printed page numbers were not confirmed against Springer's
    version. Unpaywall and OpenAlex both report the DOI closed with no repository
    copy; Springer was not tried. The PostScript was converted with ps2pdf and the
    text extracted with pdftotext (layout and raw modes). The extraction drops the
    fi/ff ligatures and garbles summation signs, τ, φ and exponents, so the objective
    (p. 4), Lemma 1 and its proof (p. 7), Theorem 5.1 (p. 13) and Theorem 5.2 (p.
    14) were checked against page images. Read: abstract, all six sections, every
    definition, algorithm, observation, lemma, theorem and the proofs given, both
    footnoted caveats, the conclusions and the reference list. Nothing skipped.
    The paper gives no proofs for Observations 1–5, Theorem 3.2 (it follows from
    Lemma 1), Theorem 5.1 or Theorem 5.2, and only a sketch for Theorem 3.3 ("skipping
    some tedious details here"); what those results say is stated as the paper states
    it. The later papers on maintenance-constrained selection (Gupta & Mumick, ICDT
    1999, and the IEEE TKDE 2005 journal version) were not read and nothing below
    comes from them; the InfoLab link to the 1999 paper (infolab.stanford.edu/~hgupta/ps/update.ps)
    returned 403. Every quotation below was checked against the extracted text by
    script, with whitespace normalised and ligature losses allowed for.
date: '2026-10-15'
summary: >-
  Gupta states view selection on general AND-OR view graphs as minimizing frequency-weighted
  query cost plus update-frequency-weighted maintenance cost under a space budget.
  He proves greedy guarantees of 1 − 1/e (about 63%) of the optimal benefit, with
  the budget overrun by one view or up to double, but almost all of them assume
  no updates. Maintenance cost enters exactly one theorem: AND view graphs (each
  view has one way of being computed) in which every view is queried more often
  than it is updated. For OR view graphs, which include Harinarayan, Rajaraman and
  Ullman's data cube, the paper sets update costs aside outright, so it does not
  add upkeep to that problem. Maintenance is an abstract per-update charge for keeping
  a view consistent. Nothing prices building a view, tolerated staleness or deferred
  refresh, and there are no experiments.
---

# NOTE-tmp4p0w6: Gupta — Selection of views to materialize in a data warehouse

## Contribution

Harinarayan, Rajaraman and Ullman ([LIT-tmptn63k](../literature.d/LIT-tmptn63k.md)) chose which cuboids of a data cube to precompute under a budget, with no update costs. This paper sets out a general framework for choosing views to materialize in a warehouse. Queries and candidate views form an AND-OR view graph. Each node carries a query frequency, a size and an update frequency, and the objective adds a maintenance term to the query term. On that framework it proves greedy approximation results for special cases: AND view graphs, OR view graphs (which include data cubes), both with indexes, and general AND-OR graphs through an exponential-time AO-greedy and an r-level greedy. It names the earlier cube work's gap directly: "Both these works ignore update costs." The framework closes that gap. The theorems close it only for AND graphs in which no view is updated as often as it is queried.

## Key insight

A greedy that adds, at each step, the view with the greatest benefit per unit of space gets within 1 − 1/e of the best benefit possible in the space it ends up using, provided the benefit of a set never exceeds the sum of its parts' benefits (the paper's "monotonicity property", which is subadditivity). Without updates that holds for AND graphs, OR graphs and a view-plus-its-indexes grouping. Maintenance cost can break it, because one stored view can make another cheaper to keep current: "consider a view C1 which helps in maintaining another view C2. Hence, the benefit of C1 ∪ C2 might be more than the sum of their benefits individually." Upkeep turns the benefit superadditive, and the greedy guarantee then lapses. The paper restores it only where queries outnumber updates at every view.

## Assumptions

- **The view graph is given.** For a query set, an expression AO-DAG is built for each query, listing the "useful" ways of computing it from base relations and other views (it defers to Roussopoulos 1982 for how), and the DAGs are merged. "Each node in the AND-OR view graph G will represent a view that could be selected for materialization, and these are the only views considered for materialization." Base relations (sinks) are always available.
- **Node parameters** (Definition 2.3): f_u, "frequency of the queries on u"; S_u, "space occupied by u"; g_u, "frequency of updates on u". Costs sit on the AND arcs (the cost of computing a node from its children). Frequencies and costs are fixed and known.
- **Query cost** Q(u, M) is "the evaluation cost of the cheapest embedded expression A-DAG for u in G whose sinks belong to the set M ∪ L", L the base relations.
- **Maintenance cost** U(u, M) is "the maintenance cost for the view u in the presence of the set of materialized views M and the set of sinks, L". It is never given a functional form. The introduction frames it as the cost of incremental maintenance: "In order to keep a materialized view consistent with the data at sources, the view has to be incrementally maintained [ZGMHW95, GM95]. This maintenance of views incurs what is known as view maintenance or update costs." Views are kept consistent. There is no notion of a view being allowed to lag.
- **One resource constraint: space.** The abstract mentions "a limited amount of resource, e.g., materialization time, storage space etc.", but every formal problem uses space alone. The one-time cost of computing a view in the first place does not appear in τ.
- **Indexes** (Sections 3.4, 4.3) are built only on materialized views, and "if an index is not materialized, then it is never 'computed' while answering user queries". All index results assume no updates.
- **Data cubes are assumed update-free**: "As OLAP databases have very few or no updates, we assume that there are no update costs throughout this section" (Section 4, OR view graphs).
- **Guarantees are bicriteria.** Each bound compares the greedy's benefit with the optimum achievable in the space the greedy actually used, which may exceed S by the largest view (S + r) or reach 2S. Benefit is the reduction in τ from materializing nothing, not τ itself.

## Key results

Notation: τ(G, M) is the objective, B(C, M) = τ(G, M) − τ(G, M ∪ C) the benefit of adding C, and B(C, ∅) the "absolute benefit".

- **Objective** (Section 2.3, checked against the page image). Choose M to minimize
  τ(G, M) = Σ_{i=1..k} f_{Q_i} Q(Q_i, M) + Σ_{i=1..m} g_{V_i} U(V_i, M), subject to Σ_{v∈M} S_v ≤ S.
  In words, "minimizes the sum of total query response time and total maintenance cost, under the constraint that the total space occupied by M is less than S." Maintenance is charged per update, at update frequency times the cost of one maintenance, for each materialized view, and that cost depends on what else is materialized.
- **Hardness.** "The view-selection problem is NP-hard even for the special case of an AND-OR graph where each AND arc binds at most one edge, and when the update frequencies are zero." By reduction from minimum set cover; no proof given. For AND view graphs: "the view-selection problem in AND view graphs is not known to be NP-complete." For OR view graphs, a reduction from set cover with Feige's threshold means no polynomial algorithm guarantees better than 63% unless P = NP. That is attributed to a personal communication (Chekuri 1996) and not proved.
- **Theorem 3.1 (AND view graph, no updates).** The greedy (Algorithm 3.1: repeatedly add the view of greatest benefit per unit space, running time O(kn²)) uses at most S + r space, r the largest view, and its absolute benefit is at least (1 − 1/e) of the optimum achievable in that space. Proof given.
- **Greedy-interchange (Algorithm 3.2).** Swaps a chosen view for an unchosen one while that improves the benefit. "Unfortunately, not much can be proved about the competitiveness of the solution produced by the greedy interchange algorithm except that it is obviously at least as good as the greedy algorithm." Its running time is unbounded. For the OR case the paper reports Cornuéjols, Fisher and Nemhauser's facility-location experiments (interchange about 1.5 times greedy's running time, much better solutions), not experiments of its own.
- **Lemma 1 and Theorem 3.2: the only result with maintenance cost.** "In an AND view graph, the benefit function B satisfies the monotonicity property for any M with respect to sets consisting of single views, if the update frequency g_v at any view v is less than its query frequency f_v." Theorem 3.2: in an AND view graph where every view's update frequency is below its query frequency, the greedy's absolute benefit is at least (1 − 1/e) of the optimum in the space it uses. The proof needs two inequalities about U that the model never states: that adding v cuts another view's maintenance cost by no more than v's query cost, U(x, M) − U(x, M ∪ {v}) ≤ Q(v, M) ≤ Q(v, ∅), and that U(v, ∅) − U(v, M) ≤ U(M_D, ∅) ≤ Q(M_D, ∅), M_D being v's materialized descendants. So the guarantee holds for maintenance costs that behave like bounded recomputation, not for an arbitrary U. Theorem 3.2 drops the S + r statement that Theorem 3.1 carries.
- **Theorem 3.3 (AND view graph with indexes, no updates).** The inner-level greedy (Algorithm 3.3: at each stage, the best view-plus-greedily-chosen-indexes, or a single index of a chosen view; O(k²m²)) uses at most 2S space, and its benefit is at least 1 − 1/e^0.63 ≈ 0.467 of the optimum in that space, "assuming that no structure occupies more than S units of space". Proof sketched.
- **Theorem 4.1 (OR view graph, no updates).** The same greedy, with the same S + r and 1 − 1/e guarantee. This "generalizes the problem considered by Harinarayan et al. in [HRU96]" and proves their greedy keeps its guarantee on any OR view graph. It is stated without proof here (cf. Theorem 3.1).
- **Theorem 4.2 (OR view graph with indexes, no updates).** The inner-level greedy: at most 2S, at least 0.467.
- **Theorem 5.1 (general AND-OR, via query-view graphs, no updates).** The AO-greedy, which picks at each stage the connected subgraph of the intersection graph with the greatest benefit per unit space, uses at most 2S and gets at least 1 − 1/e. It can take exponential time. Proof omitted ("due to space constraints"). On OR graphs it reduces to the plain greedy. Footnote 6: "Though we ignore update costs, it can be incorporated by adding possibly additional nodes in ζ and additional edges in F". This is asserted, not shown.
- **Theorem 5.2 (r-level greedy, no updates).** At most 2S space, benefit at least 1 − (1/e)^(0.63^r), time O((kn)^(2r)) excluding the final level, assuming no view exceeds S. Proof omitted.
- **Open problems (Section 6),** among them: "Are there heuristics which optimize total query benefit under the constraint of total maintenance time?" That is the problem of Gupta and Mumick's 1999 follow-up, not of this paper.
- **No experiments, no implementation, no workload data.**

## Bearing on the record

**On what [LIT-tmpn0tsb](../literature.d/LIT-tmpn0tsb.md) says.** The filing calls this "the follow-up by his co-author that adds maintenance cost to the view selection of [LIT-tmptn63k](../literature.d/LIT-tmptn63k.md)". That needs narrowing. Gupta adds a maintenance term to the formulation, and on general AND-OR graphs. But for OR view graphs, the class that contains Harinarayan, Rajaraman and Ullman's data cube, the paper assumes no updates throughout, and its Theorem 4.1 is their greedy's guarantee carried to arbitrary OR graphs, still without upkeep. The one theorem that prices maintenance (3.2) covers AND view graphs only, in which each view has a single plan, and only when every view is queried more often than it is updated. The paper's own open problem, optimizing query benefit under a maintenance-time budget, is the follow-up that actually takes up upkeep (Gupta & Mumick, ICDT 1999; journal version IEEE TKDE 2005). Neither was read. The 1999 paper is listed on the InfoLab page, but its copy returned 403.

**On [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md)'s joint cost model.** In form, τ is the joint model the question asks for. It adds a reuse term (query frequency × cost of answering from what is stored) to an upkeep term (update frequency × cost of keeping each stored item current, where the cost depends on what else is stored) and puts both under a capacity budget. For a LEGO bin, a filed argument or a speed bug the terms would be: how often the item is looked up, what a lookup costs with or without the arrangement, how often the underlying thing changes, and what bringing the arrangement back into line costs per change. Three limits stop it from being the whole model the question wants.

- **The build cost is missing.** τ charges no one-time cost to materialize a view. The question's "paid once" term, sorting the bricks or setting the bugs, is absent. Only space limits what is stored, and the steady-state rates of querying and updating price everything else.
- **Upkeep, not staleness.** Maintenance is charged per update, at g_v × U(v, M), as the cost of keeping the view "consistent with the data at sources". Every update is propagated. Nothing models tolerating a stale answer, deferring refresh, or the cost of acting on an out-of-date view. If the record's "staleness" term means the cost of keeping a precomputed answer current, this prices it, abstractly. If it means the risk or cost of using a precomputed answer that has gone out of date (bugs set for a weight that has since changed, a filed argument whose evidence has moved), this does not model it. Speed bugs are reset per approach, not maintained per change in weight, so they fit the paper's model only if each change is treated as an update that must be propagated.
- **Theorems only in a corner.** With maintenance in the objective the benefit can be superadditive, because one stored item can make another cheaper to keep. The greedy then loses its guarantee, except in AND graphs where reads outnumber writes at every view, under unstated bounds on U. The paper's cue for the record is a condition, not a theorem: precomputation is tractable to choose well when every stored item is read more often than its source changes. That is close to [CLAIM-303](../claims.d/CLAIM-303.md)'s "worth its cost only when expected reuse covers it", applied per item, but the paper uses it as a sufficient condition for the proof, not as a claim about when storing pays.

U(u, M) is left abstract, and the paper has no data, so it supplies a shape for the joint model and no magnitudes. Nothing in it bears on cues or pop-out search ([CLAIM-tmpjmtw0](../claims.d/CLAIM-tmpjmtw0.md) part 3).
