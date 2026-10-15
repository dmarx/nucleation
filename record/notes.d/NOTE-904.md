---
number: 904
status: Read
formerly:
- NOTE-tmp256om
paper: LIT-1113
title: Dar, Franklin, Jónsson, Srivastava & Tan — Semantic data caching and replacement
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the VLDB Endowment's own copy of the proceedings
    paper, https://www.vldb.org/conf/1996/P330.PDF, which answered 200 (application/pdf,
    1,663,834 bytes, sha256 ba2004f3…b73de) to a request with a browser User-Agent;
    without one the server is known to refuse. The copy is the typeset proceedings
    text, 12 pages printed 330–341, with the Endowment's copying notice and "Proceedings
    of the 22nd VLDB Conference Mumbai(Bombay), India, 1996" on the first page;
    it is a scan with an OCR text layer (PDF 1.2, created 1998). Text extracted
    with pdftotext. The OCR layer runs words together in the abstract and garbles
    some symbols (∧, ¬, ≤), so the probe and remainder definitions (p. 334), the
    operational model and Table 1 (p. 335), Table 2 (p. 336), Figures 4 to 9 (pp.
    337–338) and the directional Manhattan formula and Table 3 (p. 340) were read
    from page images rendered at 110 dpi. Read: abstract, all eight sections, all
    figures and tables, footnotes and the reference list. Nothing skipped. Every
    quotation below was checked by script against the extracted text with all whitespace
    removed (the OCR layer drops spaces between words) and curly quotes straightened;
    one quotation that the OCR garbles ("sixes" for "sizes") was checked against
    the page image of p. 340 and is marked there; so is the first-page line naming
    the conference, whose OCR reads "MumbaQBombay)" (checked against the image of
    p. 330). Quotations of CLAIM-303 and CLAIM-308 were checked against those files.
    Keller and Basu's predicate caching [KB96], the nearest prior work, was not
    read, so what the paper says about it is its own account.
date: '2026-10-15'
summary: >-
  A client cache described by the selection predicates of past queries can answer
  a new selection query partly from cache (the probe query, Q ∧ V) and fetch only
  the rest from the server (the remainder query, Q ∧ ¬V), and can evict by semantic
  region rather than by page or tuple. In one simulator, one client and one server,
  read-only selection queries on a single 10,000-tuple relation, this matched page
  caching on a clustered index, beat it heavily when clustering was bad, answered
  over 60% of small queries on an unindexed attribute with no server contact, and
  let a value function based on semantic distance beat LRU on a skewed workload.
  No replacement rule won everywhere: on regular cyclic paths MRU was best. Everything
  is measured, nothing is proved; updates, joins, and the CPU cost of reasoning
  about cache contents were not modelled.
---

# NOTE-904: Dar, Franklin, Jónsson, Srivastava & Tan — Semantic data caching and replacement

## Contribution

The paper proposes semantic caching for client-server databases that ship data to clients: the client keeps "a semantic description of the data in its cache", as constraint formulas, instead of a list of pages or tuple identifiers. It compares this with page caching and tuple caching in a simulation study, on three factors: the unit of cache management, remainder queries against faulting, and the replacement policy. The idea it adds over the nearest prior work, predicate caching (Keller and Basu 1996), is the semantic region as the unit of replacement, which lets the replacement value depend on where a region lies in the space of queries.

## Key insight

If the cache knows what it holds as a predicate, then deciding what a new query still needs is a computation on predicates, not a lookup of items. The query splits into a part the cache already answers and a remainder the server must answer, and the remainder can be sent as a query, so the server can work in parallel and, when the remainder is empty, need not be contacted at all. The same predicates group tuples into regions that are shaped by the queries actually asked, so replacement information is kept per region (cheaply, and independent of how tuples happen to be clustered on pages), and a region's value can be its distance from the current query rather than its age.

## Assumptions

- **Queries.** "In this study, we consider selection queries on single relations, where the selection condition is an arbitrary constraint formula (that is, a disjunction of conjunctions of built-in predicates)". Joins and more complex queries are named as future work: "dealing with more complex queries within the framework of semantic caching is an important direction of future research".
- **Read-only.** "Since we do not consider updates in this study, we do not model the overhead needed to facilitate updates." No consistency, invalidation or staleness is modelled.
- **Reasoning about the cache is free.** "We also do not model the CPU cost of cache management at the client." Computing Q ∧ V and Q ∧ ¬V over formulas that need not be convex or connected is not charged; only the space for region descriptors is (24 bytes per region, 8 bytes per attribute per factor plus a 4-byte pointer, 4 bytes per tuple).
- **Simulator.** An extension of the simulator of Franklin, Jónsson and Kossmann (1996), in C++ with CSIM, configured for one client and one server. Table 1 defaults: 50 MIPS per site, one disk, 250 Kb client cache, 4,096-byte pages, 8 Mbit/s network, message and per-page CPU costs in instructions.
- **Workload (Table 2).** One relation of 10,000 tuples of 200 bytes; queries select 1–10% of it; 90% of queries have their centre point in a hot region of the middle 10%. Attributes from the Wisconsin benchmark: Unique2 indexed and perfectly clustered, Unique1 indexed and unclustered, Unique3 unindexed and unclustered. Each run is 50 warm-up queries and 500 measured; results average three runs. A tenfold scale-up gave "nearly identical" relative results (footnote 3).
- **All three architectures ship page-sized units**, so the comparison isolates cache management, not transfer granularity.

## Key results

The paper has no theorems. The model results are definitions; the performance results are simulation measurements.

**The model (Section 3).**
- With V the formula describing the cached part of relation R and Q a query on R, the probe query is P(Q, V) = Q ∧ V and the remainder query is R(Q, V) = Q ∧ ¬V (p. 334, page image). The two are disjoint and together give Q, by construction.
- Regions: "each tuple in the client cache is associated with exactly one semantic region". A query that intersects a region splits it into the intersection and the difference, and the remainder's result forms a new region, so "the execution of a query that overlaps n semantic regions in the cache can result in the formation of 2n + 1 regions". Regions need not be convex or connected.
- Coalescing: always coalescing regions of equal value gives large regions whose eviction "can empty a significant portion of the cache"; never coalescing gives many small regions. The heuristic used: "Regions with the same cache replacement value may be coalesced if either one of them is smaller than 1% of the cache size."
- Replacement: "the semantic region with the lowest value and all tuples within that region are discarded from the cache". A region is evicted whole. Value functions: recency per region (LRU, MRU); the negative of the Manhattan distance between the centre of gravity of the region and that of the most recent query; and, for the mobile workload, a directional Manhattan distance −(d_par + d_perp) with weights p_a, p_b, p_l, p_r for regions ahead, behind, left and right of the user's position and direction (p. 340, page image). No value function uses the cost of fetching a region again.
- The operational model (Section 3.4) processes each query in six steps: probe and remainder, repartition regions, fetch the remainder, evict lowest-valued regions until there is room, answer the rest, recompute V and the regions.

**Measurements (Sections 5 and 6).**
- *Clustered index (Unique2, Figure 4).* The three architectures perform similarly; tuple caching is worst because of its overhead (36 bytes per 200-byte tuple). Semantic caching's lower overhead is offset by coarser replacement as queries grow: "Replacing large regions temporarily opens up large holes in the cache".
- *Unclustered index (Unique1, Figure 5).* Page caching "performs far worse" than tuple and semantic caching, which are close to each other.
- *Space overhead (Figure 6, two-attribute queries).* Page caching 6.5% of the cache, tuple caching 15.2%, at all query sizes. Semantic caching's overhead depends on query size and coalescing: never coalescing is highest ("For 1% queries, there are 55 regions and nearly 275 factors"); always coalescing cuts overhead by 85% for the smallest queries but has "as much as 10% lower cache utilization compared to never coalescing"; the 1% heuristic has overhead slightly above always-coalesce and utilization close to never-coalesce (utilization curve not shown). In the two-dimensional space the never-coalesce overhead for small queries is over four times the single-attribute case; the heuristic's is about one third higher.
- *Unindexed attribute, disk cache (Unique3, Figures 7 and 8).* Every request to the server costs a full scan there. Tuple caching that scans its cache first and then asks the server is slower than ignoring the cache, though it sends fewer bytes. Semantic caching is faster for small queries because the client can tell when it needs no server at all: "over 60% of the small (1%) queries are answered completely from the client's cache". When no query is answered wholly from cache, semantic caching equals ignoring the cache (footnote 6).
- *Distance against recency (Unique1, Figure 9).* Manhattan distance beats LRU at every query size, because the 10% of queries landing in the cold region stay in an LRU cache until they age out, while under distance they lose value at the next hot query.
- *Mobile navigation (Section 6, Table 3).* A 2-D map relation, 8,192 × 8,192 tuples (one per coordinate pair), Z-ordered; each query an 8 × 16 rectangle (128 tuples); 500 queries per path. Response times relative to the best policy on each path (1.00):
  - Random paths, four probability settings: directional Manhattan 1.00 on all four (29.4 to 56.1 ms); LRU 1.01 to 1.06; MRU 1.04 to 2.24 (2.24 on the fully random path).
  - Square 32 × 32: MRU 1.00 (7.23 ms), directional Manhattan 2.29, LRU 9.57. Square 160 × 160: MRU 1.00 (51.9 ms), the other two 1.22.
  - Lollipop (32 × 32 square on a stick of 160), square traversed 1, 5, 10, 50 times per cycle: MRU best once round (Manhattan 1.86, LRU 2.02); Manhattan best at 5, 10, 50 (LRU 1.22, 1.38, 1.69; MRU 1.11, 1.60, 2.54). Break-even between MRU and Manhattan at 4 rounds, between MRU and LRU between 6 and 7.
  - The paper's summary: "This query profile - predictable and cyclic - is ideal for MRU, which is the clear winner", and on the lollipop "The directional Manhattan distance function is always better than LRU". It claims the distance function "performs robustly, across a wide range of loop sizes" (p. 340; the OCR reads "sixes", checked against the page image).
  - Footnote 7: "In the absence of loops, i.e., when data is touched at most once, caching is not useful, and no value function will perform well." (The OCR has a full stop for the comma after "useful"; checked against the page image.)

## Bearing on the record

**On [CLAIM-303](../claims.d/CLAIM-303.md): reuse of a stored answer is partial, and the cost of finding the reusable part is the term this paper leaves out.**

- [CLAIM-303](../claims.d/CLAIM-303.md) prices a filed argument as reused whole or not at all, with a fixed reconstruction cost c_r saved per use. Here a stored answer serves a new question in part: the probe answers Q ∧ V from storage and only Q ∧ ¬V is recomputed. The saving per use is the size of the overlap, which depends on the new question, not a constant. The paper's results show this is where the gains come from: over 60% of small queries were answered whole from cache, and the rest paid only for their remainders.
- The paper has a mechanism for partial reuse only because answers are stored with a description of what they answer (a predicate) and questions arrive in the same language, so containment and difference are computable. A filed argument has no such description, and deciding how much of a new question it settles is itself work. That work is [CLAIM-303](../claims.d/CLAIM-303.md)'s c_a (access and verification). The paper sets it to zero by assumption ("We also do not model the CPU cost of cache management at the client"), so it offers no evidence on how large c_a is. It shows that c_a has a natural form, a containment test of the new question against the stored descriptions, and that its space cost grows with fragmentation (55 regions and 275 factors for 1% queries without coalescing, four times that in two dimensions).
- It is read-only, so nothing here bears on [CLAIM-303](../claims.d/CLAIM-303.md)'s staleness term or on "persistence can preserve errors". The paper itself says updates are needed "to make these techniques applicable to a larger class of applications".
- Filing is not a choice in the paper: every remainder result is cached. The decision studied is what to drop.

**On [CLAIM-308](../claims.d/CLAIM-308.md) and [THEORY-348](../theory.d/THEORY-348.md): the replacement policies here are forecasts, not rent-or-buy rules, and none dominates.**

- The value functions rank regions by recency or by distance from the current query and evict the lowest. None prices what it would cost to fetch the region again, and none carries a competitive guarantee. So this paper neither supports nor bears directly on [CLAIM-308](../claims.d/CLAIM-308.md)'s worst-case rule. Its eviction rule is not of the break-even kind, and the paper does not compare against one.
- It is evidence for [CLAIM-308](../claims.d/CLAIM-308.md)'s own caveat: "Where reuse can be forecast, a rule using the forecast can do better". Semantic distance is a forecast of reuse from content: a region near the current query is predicted to be needed again. Where queries have semantic locality (the skewed workload, random and lollipop paths) it beat recency. Where the access pattern is a regular cycle larger than the cache, MRU beat it by up to 2.29 times. Footnote 7 adds that with no loops no value function helps. So the better forecast depends on the workload, and the paper measures this on one simulator with synthetic workloads and does not explain it.
- Evicting a whole region is a coarse unit, and the paper names its cost: "Semantic caching discards entire regions from the cache, often resulting in poor cache utilization". For the record that is a granularity question [CLAIM-303](../claims.d/CLAIM-303.md) does not raise: whether a filed argument is kept or dropped as a unit, or in parts.

## Limitations

- One simulator, one client, one server, one synthetic relation; synthetic query paths for the mobile case. Relative results only; no real system.
- Selection queries on one relation only. Joins, aggregation and query containment for general queries are not addressed; the paper notes that using cached results is "a simple case of" answering queries using views.
- No updates, so no consistency, invalidation or staleness.
- No cost for computing probe and remainder queries or maintaining region formulas.
- No theorems: no bound on the number of regions, on the complexity of the formulas, or on replacement quality.
- Value functions do not include refetch cost or region size.

## Open questions

- What does probing cost when the cache's description grows complex (many non-convex regions in several dimensions), and when does that cost exceed fetching from the server?
- Would a value function that weights distance by refetch cost (a remainder query's server cost) behave like the break-even rule of [THEORY-348](../theory.d/THEORY-348.md)?
- Which workload property decides between distance and MRU? The paper's numbers point to cycle length relative to cache size, but it does not test that directly.
