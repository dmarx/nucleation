---
number: 916
status: Read
formerly:
- NOTE-tmpkpp45
paper: LIT-1098
title: Malkov & Yashunin — Hierarchical navigable small world graphs for approximate
  nearest neighbour search
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' arXiv preprint, version 4 (arxiv.org/pdf/1603.09320v4,
    posted 14 August 2018, 13 pp.), the last arXiv version. The published article
    is IEEE TPAMI 42(4), pp. 824–836, also 13 pages. The v4 PDF still carries the
    IEEE submission template ("This work has been submitted to the IEEE for possible
    publication") and predates the DOI's registration (Crossref, 28 December 2018).
    Its abstract matches the published abstract, as Semantic Scholar serves it,
    except for copy-editing ("consisting of a hierarchical set" for "consisting
    from hierarchical set"). The published body was not seen, so later copy-editing
    or changes cannot be ruled out. Version 1 (arxiv.org/pdf/1603.09320v1, 30 March
    2016, 18 pp.) was also fetched, and its abstract, complexity analysis and discussion
    were compared with v4. The two differ in substance: v1's abstract says the structure
    admits "simple insertion, deletion and K-nearest neighbor queries", and v1 has
    an "Element removal complexity" paragraph. v4 drops both and lists removal as
    future work. v1 also has no Faiss comparison and no Delaunay-graph argument.
    Places looked: arXiv abstract page (four versions, v1 to v4; fetched); Unpaywall
    (is_oa false, closed, no OA location); OpenAlex (closed, any_repository_has_fulltext
    false; locations doi.org and PubMed 30602420, no PDF); Crossref (pages 824–836,
    print 2020-04-01, no abstract); Semantic Scholar (openAccessPdf points to the
    arXiv copy); IEEE Xplore document page (HTTP 202 bot challenge, not used). Text
    was extracted with pdftotext, both raw and layout. Page 7 was checked against
    a rendered image for the search-complexity argument and for equation 1, which
    extraction garbles. Read: every section of v4 (1–6), Algorithms 1–5, Figures
    1–15 and their captions, Tables 1–3, and the reference list. Nothing skipped.
    Kleinberg (LIT-1103), Pugh's skip lists, the NSW papers [25, 26, 44] and
    the Delaunay-degree result [48] were not read, so what the paper says they show
    is its account of them. Every quotation below was checked by script against
    the extracted text of the version named, with whitespace normalised.
date: '2026-10-15'
summary: >-
  HNSW is a stack of proximity graphs on nested random subsets of the data. Each
  element's top layer is drawn from a geometric distribution, and new neighbours
  are chosen by a pruning rule that favours diverse directions. Searching from the
  sparse top layer down makes per-query cost grow about logarithmically with N on
  uniform random data in 4 and 8 dimensions, which flat NSW graphs did not. The
  logarithmic bound is derived only for exact Delaunay graphs of bounded mean degree,
  which HNSW does not build. For the graphs it does build, logarithmic scaling is
  measured, at low dimension only, and on 200M SIFT vectors the paper reports the
  scaling "deviates from the pure logarithm". The neighbour-selection rule is what
  keeps clustered data searchable: in the paper's synthetic test with 100 isolated
  clusters, linking each element to its nearest neighbours fails to reach high recall.
  There is no worst-case or recall guarantee, no deletion, and no analysis of query
  distributions unlike the data.
---

# NOTE-916: Malkov & Yashunin — Hierarchical navigable small world graphs for approximate nearest neighbour search

## Contribution

A graph index for approximate K-nearest-neighbour search that needs only a
distance function, with no auxiliary tree or quantizer to pick a starting
point. Earlier proximity-graph methods route greedily through one graph. The
paper locates their weakness in that routing: "the power-law scaling of the
proximity graph routing causes extreme performance degradation in case of
low dimensional or clustered data". Flat k-NN graphs scale as a power law.
The authors' earlier Navigable Small World (NSW) graph was polylogarithmic,
because both the hop count and the degree of the hubs on the greedy path
grow as log N. HNSW separates links by length scale into layers and caps
the degree on every layer, so that, the paper argues, cost is constant per
layer and logarithmic overall. Its other contribution is a neighbour-selection
heuristic. The paper presents HNSW as a skip list generalized from a linked
list to proximity graphs.

## Key insight

A skip list finds a key in a sorted list in about log N steps because each
element is promoted to the next level with fixed probability, and the
levels are nested random samples, each coarser than the one below. HNSW
does the same with proximity graphs in place of lists. The top layer is a
graph on a few elements with long links, and each layer below adds
elements and shorter links. Greedy search finds the nearest element on one
layer and starts from it on the next. Because levels are drawn independently
of position, the expected number of steps on a layer before reaching an
element that also sits on the layer above is bounded by a constant. With
bounded degree per layer, that bounds the work per layer. The heuristic
adds that the right neighbours are not simply the nearest: a candidate is
linked only if it is nearer the new element than to any neighbour already
chosen. This keeps links that bridge between clusters. Linking only to the
nearest neighbours drops those bridges.

## Assumptions

- **A distance function and nothing else.** The method is stated for
  general metric and non-metric spaces. The experiments use L2, cosine,
  Jensen–Shannon divergence, SQFD and Levenshtein distance.
- **Levels independent of position.** Algorithm 1 line 4 sets an element's
  level to l = ⌊−ln(unif(0..1))·mL⌋. That is geometric, with
  P(l ≥ 1) = exp(−1/mL), which is 1/M at mL = 1/ln M. The search-complexity
  argument depends on this independence.
- **Exact Delaunay graph, bounded degree** (for the complexity argument
  only). "The complexity scaling of a single search can be strictly analyzed
  under the assumption that we build exact Delaunay graphs instead of the
  approximate ones." The mean Delaunay degree is assumed capped by a
  constant as N grows: "this is the case for random Euclid data [48], but
  can be in principle violated in exotic spaces". The paper itself says
  the mean Delaunay degree "scales exponentially with the dimensionality".
- **Low intrinsic dimension for the scaling claims.** Every logarithmic
  statement is qualified by low dimension: "in agreement with the
  simulations on low dimensional datasets". Construction: "at least for
  relatively low dimensional datasets the construction time scales as
  O(N∙log(N))."
- **Queries drawn like the data.** In the ann-benchmark tests the 1,000
  queries were "randomly extracted from the initial dataset". No test uses
  queries distributed unlike the data.
- **Insert-only.** The structure is built by successive insertions. v4 has
  no deletion or update.

## Key results

**Construction (Section 4, Algorithms 1–5).**
- Insertion (Alg. 1): draw the level l. From the top layer L down to
  l+1, greedy search with ef = 1 finds one entry point per layer. From
  min(L, l) down to 0, a beam search (Alg. 2) keeps the efConstruction
  nearest candidates found. M of them become bidirectional links, chosen by
  Alg. 3 (nearest) or Alg. 4 (heuristic). A neighbour whose list exceeds
  Mmax (Mmax0 on layer 0) is pruned by the same rule. If l > L, the new
  element becomes the entry point.
- Search (Alg. 5): greedy with ef = 1 from the top layer down to layer 1,
  then a beam of size ef on layer 0, returning the K nearest found.
- Heuristic (Alg. 4): candidates are taken in order of distance, and one
  is kept "only if it is closer to the base (inserted) element compared to
  any of the already connected candidates". extendCandidates (adding the
  candidates' own neighbours) is "useful only for extremely clustered data".
  keepPrunedConnections refills to M from the discarded candidates. With
  enough candidates the result contains the exact relative neighbourhood
  graph. In 1D it gives the exact Delaunay graph, "thus making a direct
  transition from Hierarchical NSW to the 1D probabilistic skip list
  algorithm".
- No shuffling is needed before insertion. The paper claims "truly
  incremental indexing even in case of temporarily alterating data
  distribution (though changing the order of the insertion slightly alters
  the performace due to only partially determenistic construction
  procedure)".

**Parameters (Section 4.1, measured).**
- mL = 0 with Mmax0 = M gives directed k-NN graphs, with power-law search.
  mL = 0 with Mmax0 = ∞ gives NSW, polylogarithmic. mL > 0 gives the
  hierarchy. "A simple choice for the optimal mL is 1/ln(M), this
  corresponds to the skip list parameter p=1/M with an average single
  element overlap between the layers." Supported by query-time against mL
  curves: 10M random d=4 vectors, where raising mL from 0 gives a large
  speed-up; 100k random d=1024, a small speed-up; and 5M SIFT (Figs. 3–5).
- Mmax0 = 2M is near optimal. Mmax0 = M carries "a very strong performance
  penalty at high recall" (Fig. 6, 5M SIFT).
- M from about 5 to 48. Smaller M is better at low recall or low
  dimension, larger M at high recall or high dimension (Fig. 8).
- The heuristic is never worse than nearest-neighbour linking in the
  paper's tests. Its gain is largest at low dimension, at high recall for
  mid dimensions, and on clustered data. On 10M random d=10 vectors in 100
  isolated clusters (Fig. 7), with nearest-neighbour links, "the
  Hierarchical NSW algorithm fails to achieve a high recall for clustered
  data because the search stucks at the clusters boundaries". With the
  heuristic and candidate extension, "clustering leads to even higher
  performance". "For uniform and very high dimensional data there is a
  little difference between the neighbors selecting methods".

**Complexity (Section 4.2): argued, partly derived, partly measured.**
- *Search, derived under exact Delaunay.* Each layer takes a bounded
  expected number of steps, S = 1/(1−exp(−mL)), and at most C·S distance
  evaluations if the mean Delaunay degree is at most C. The expected
  number of layers is O(log N), so search is O(log N). The argument is a
  sketch, not a proof. As printed it sets the per-node probability of
  belonging to the layer above to "p=exp(-mL)". Algorithm 1's level rule
  gives exp(−1/mL), so the printed S is not the bound the construction
  implies; a simulation done for this reading confirmed exp(−1/mL). The
  shape of the argument does not change: a constant per layer, times
  log N layers.
- *For the graphs actually built, measured only.* HNSW's graphs are not
  Delaunay graphs, so the paper relies on backtracking on layer 0. For d=4
  random data, the ef needed for recall 0.9, 0.99 and 0.999 levels off as N
  grows over about eight orders of magnitude (Fig. 11), which the paper
  reads as "inaccuracies of the Delaunay graph approximation do not alter
  the scaling". For high dimensions it says the check is infeasible:
  "Further analitical evidence is required to confirm whether the
  resilience of Delaunay graph aproximations generalizes to higher
  dimensional spaces."
- *Scaling measurements.* On d=8 random hypercube data at recall 0.95
  (10-NN), distance computations grow no faster than logarithmically, for
  N from 10² to about 10⁸, while NSW's grow faster (Fig. 12b). On subsets
  of 1B SIFT up to 200M (Fig. 15 inset): "Note that the scaling deviates
  from the pure logarithm, possibly due to relatively high dimensionality
  of the dataset."
- *Construction.* Each insertion is about one search, since the expected
  number of layers is constant. Equation 1 gives E[l+1] = mL + 1, dropping
  the floor, so this is an upper bound; the exact value at mL = 1/ln M is
  M/(M−1). Construction is therefore O(N log N), "at least for relatively
  low dimensional datasets".
- *Memory.* (Mmax0 + mL·Mmax) links per element, about 60–450 bytes per
  object with 4-byte links and M between 6 and 48.

**Build cost (measured).** 10M SIFT (d=128, M=16, efConstruction=100)
builds in about 3 minutes on 40 cores. Construction parallelizes with
"no measurable effect on index quality" (Fig. 9). Raising efConstruction
buys little query speed for much longer builds (Fig. 10). 200M SIFT
(Table 3): HNSW took 5.6 h (efConstruction=500) or 42 min
(efConstruction=40), with 64 GB peak memory. Faiss PQ indexes took 11–12 h,
with 23.5–30 GB.

**Experiments (Section 5).** All comparisons are single-threaded, with
parameters tuned for each recall range.
- Against NSW (5.1): d=4 random (10M) and d=8 random (10² to about 10⁸).
  HNSW needs fewer distance computations, especially at high recall.
- Euclidean benchmark (5.2, Table 1, Fig. 13; the caption says five
  datasets, six are plotted): SIFT 1M (d=128), GloVe 1.2M (d=100, cosine),
  CoPhIR 2M (d=272), random 30M (d=4), DEEP 1M (d=96), MNIST 60k (d=784),
  all 10-NN. Against NSW, FLANN, Annoy, VP-tree and FALCONN. "For SIFT,
  GloVE, DEEP and CoPhIR datasets Hierarchical NSW clearly outperforms the
  rivals by a large margin." At d=4 it is only slightly faster than Annoy
  at high recall.
- General spaces (5.3, Table 2, Fig. 14): Wiki-sparse 4M (sparse cosine),
  Wiki-8 and Wiki-128 2M (JS divergence), ImageNet 1M (SQFD), DNA 1M
  (Levenshtein). Against NSW or NNDescent graphs, VP-tree, NAPP and
  brute-force filtering. HNSW leads on all five. "The strongest
  enhancement over NSW, almost by 3 orders of magnitude is observed for
  the dataset with the lowest dimensionality, the wiki-8 with
  JS-divergence." That result is counted in distance computations.
- Against product quantization (5.4, Fig. 15): 200M SIFT, 1-NN, against
  Faiss. HNSW reaches higher recall at lower query time and builds faster,
  at more than twice the memory.

**Discussion (Section 6).** The paper claims robustness across data whose
effective dimension changes with scale. Its example is points on a curve
that fills a high-dimensional cube. Future work: inferring M, full
billion-scale tests, and "add support for element updates and removal".
It loses NSW's distributed search, because every search starts at the top
layer and the top-layer elements become congested. Skip-list distribution
methods are suggested and not tested.

## Bearing on the record

**On [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions): supports the general
point, in another setting, and narrows part 2.**
- The paper holds the description fixed and varies the arrangement: the
  same vectors under the same distance, linked as a k-NN graph, as NSW,
  or as HNSW, with nearest-neighbour links or with the heuristic. Search
  costs differ by orders of magnitude (Fig. 12; Wiki-8 in Fig. 14). On
  clustered data, nearest-neighbour linking does not merely cost more: it
  fails to reach high recall (Fig. 7). So which items can be found at all,
  not only how fast, is a property of the arrangement. This is
  [CLAIM-310](../claims.d/CLAIM-310.md)'s thesis carried over from bins to graphs.
- **Query mix.** [CLAIM-310](../claims.d/CLAIM-310.md) part 2 says the cheapest arrangement depends on
  what is searched for. HNSW is built from the data alone, with no
  workload, and every test drew its queries from the data. The paper does
  not show that one arrangement serves every query mix. It does not test
  query mixes at all. Its arrangement is chosen for queries distributed
  like the data, which is the special case where [CLAIM-310](../claims.d/CLAIM-310.md)'s dependence on
  the query mix does not arise.
- **Bin budget.** [CLAIM-310](../claims.d/CLAIM-310.md)'s cost k/2 + N/(2k), least at k = √N, is a
  two-level arrangement. A skip list, and HNSW by its own analogy, uses
  about log N nested levels with a constant number of steps on each. The
  paper does not make this comparison; it is the record's. It suggests
  part 1's √N is the cost of having only one level of bins.
- **Pop-out (part 3).** Nothing here corresponds to it. Every step is a
  pairwise distance computation, and cost is counted in those.

**On [CLAIM-309](../claims.d/CLAIM-309.md) (goodness vs discriminability): no bearing on the claim,
one clarification.** Recall here is the fraction of the true K nearest
neighbours under the chosen distance that were found. It measures
fidelity to the distance, not whether the nearest items are the wanted
ones. A retrieval-quality claim that rests on HNSW recall is a claim about
nearness, not about value.

**On [QUESTION-114](../questions.d/QUESTION-114.md) (sorting as amortized search; build against per-query
cost; upkeep).**
- **Build cost against query cost, priced for one structure.**
  efConstruction trades build time against query time along a measured
  curve (Fig. 10), with diminishing returns. The 200M comparison (Table 3)
  sets build hours, memory and query speed side by side. Construction is
  argued to cost about N searches, O(N log N) at low dimension. Build is a
  real term here, unlike in Finkelstein et al. ([LIT-1084](../literature.d/LIT-1084.md)) or Harinarayan
  et al. ([LIT-1094](../literature.d/LIT-1094.md)). The paper does not compute a break-even number of
  queries.
- **Upkeep under insertion.** Insertion is incremental and costs about one
  search. Insertion order has a small effect on quality ("slightly alters
  the performace"). No staleness is modelled.
- **Upkeep under deletion: absent.** v4 has no deletion or update and
  lists them as future work. v1's abstract claimed deletion, and its
  removal-cost paragraph argued, without an algorithm, that removal costs
  "a complexity independent of N". The published line dropped that claim.
  The record should not cite this paper for deletion.

**On [THEORY-358](../theory.d/THEORY-358.md) (feature vs conjunction search).** No bearing beyond a
contrast. HNSW's cost is a count of serial pairwise comparisons, and its
gains come from visiting fewer items, never from a parallel test that
picks a target out at once. It is not a model of visual search, and
should not be read as one.

**Related readings in progress.** Kleinberg (2000) is the paper's [41]
([LIT-1103](../literature.d/LIT-1103.md)). HNSW cites it as motivation and as a contrast: Kleinberg's
criterion needs the data distribution "beforehand", and greedy routing on
Kleinberg's graphs "suffers from polylogarithmic complexity scalability at best". HNSW's logarithmic argument
rests on the skip-list analogy and the Delaunay sketch, not on Kleinberg's
theorem. Indyk and Xu (2023; [LIT-1112](../literature.d/LIT-1112.md)) supply the worst cases this
paper does not address. The paper itself states no worst-case bound and
no recall guarantee. Its only analytic claim is an expected-case sketch
under an assumption it does not meet, and it says higher-dimensional
behaviour needs "Further analitical evidence" (sic).
