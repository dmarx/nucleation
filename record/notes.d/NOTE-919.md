---
number: 919
status: Read
formerly:
- NOTE-tmpvtj3f
paper: LIT-1107
title: 'Weber, Schek & Blott — Similarity search in high-dimensional spaces: when
  partitioning loses to a scan'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the VLDB Endowment's open copy of the proceedings
    paper, www.vldb.org/conf/1998/p194.pdf: Proceedings of the 24th VLDB Conference,
    New York, 1998, pp. 194–205, 12 pages. The server returned 200 with a browser
    User-Agent header. The PDF is a scan of the printed proceedings with an OCR
    text layer (PDF created 26 October 1998, MD5 2ed44ad0…). Text was extracted
    with pdftotext in raw and layout modes. The OCR layer garbles symbols and some
    numbers (2^d and 10^6 among them), so equations 2–19, Table 2 and Figures 7–17
    and their captions were read from page images rendered at 100 dpi. Read: abstract,
    all five sections, every assumption, observation, equation and conclusion, all
    seventeen figures and both tables, the acknowledgments and the reference list.
    Nothing was skipped. The VA-file is only sketched here, and the paper refers
    to a technical report by Weber and Blott (1997) for details; that report was
    not read. Berchtold et al.'s cost model, whose notation and Minkowski-sum method
    this paper follows, was not read. Every quotation below was checked against
    the extracted text by script, with whitespace normalised. Three failed only
    on OCR damage in the text layer ("st,ructure", a lost hyphen in "data-partitioning",
    "d^" for d̂) and were checked against the page images. The one quotation of
    the record is from the record.
date: '2026-10-15'
summary: >-
  Under uniformly distributed, independent data and queries in the unit cube with
  Euclidean distance, the paper estimates the average fraction of blocks that an
  optimal nearest-neighbour search must read in a partitioned or clustered index.
  That fraction reaches the 20% at which a sequential scan wins, given an assumed
  five-fold sequential advantage, at about 15–20 dimensions for rectangular regions,
  26 for spherical ones, and below a crude 610 for any partitioning into convex
  clusters of two or more points. The "around 10" in the abstract is the measured
  crossover for an R*-tree and an X-tree on 50,000 uniform points and on 45-dimensional
  image features. As an alternative it proposes the VA-file, a scanned file of compact
  per-vector approximations that filters out all but a few vectors. The analysis
  says nothing about data with low intrinsic dimension; that the results carry over
  by fractal dimension is a conjecture.
---

# NOTE-919: Weber, Schek & Blott — Similarity search in high-dimensional spaces: when partitioning loses to a scan

## Contribution

Earlier work had reported that tree indexes for similarity search degrade as dimension grows. This paper gives an average-case cost model for nearest-neighbour search over three classes of organization: space-partitioning (grid file, quadtree, K-D-B-tree), data-partitioning with rectangular or spherical bounding regions (R*-tree, X-tree, SR-tree, M-tree, TV-tree), and any scheme that groups points into clusters. Under uniformity and independence it finds the dimension beyond which each must read a fraction of blocks that makes a sequential scan cheaper. It then proposes the VA-file, which does not partition at all but makes the unavoidable scan smaller, and compares it with an R*-tree, an X-tree and a scan on synthetic and real data.

## Key insight

In the uniform cube the expected nearest-neighbour distance grows steadily with dimension and hardly shrinks as the data set grows. A partition with m points per block can split only about log2(N/m) axes, so its blocks stay large in every other direction, and their greatest distance to any point of the space is fixed by the number of splits, not by dimension. Once the expected nearest-neighbour distance exceeds that, every block touches every query's nearest-neighbour sphere and must be read. The same happens, later, for any convex cluster of two or more points. Since sparse space defeats partitioning, the VA-file exploits the sparseness instead: with a few bits per dimension almost every point has a cell of its own, so a short code per point is enough to rule most of them out.

## Assumptions

- **Assumption 1 (data and metric).** Data in the unit hypercube [0, 1]^d; Euclidean distance. "the structure of our analysis might equally be repeated for other data spaces" and metrics, which is asserted, not done.
- **Assumption 2.** "Data and query points are uniformly distributed within the data space, and dimensions are independent." Correlations are assumed removed beforehand by SVD, Karhunen–Loève or similar.
- **Fractal dimension, conjectured.** "we conjecture that, for d-dimensional data sets, the results obtained here under the uniformity and independence assumptions generally apply also to arbitrary higher-dimensional data sets of fractal dimension d." The support offered is Faloutsos and Kamel's result for R-trees. The paper does not test it.
- **Cost model (§3.1).** Cost is blocks read. The search is the optimal one, which reads exactly the blocks whose bounding region meets the query's nearest-neighbour sphere. The sphere's radius is replaced by the expected nearest-neighbour distance E[nn^dist], estimated by Monte Carlo (equations 5–7), and a block is read with probability equal to the volume of its Minkowski sum with that radius, inside the cube (equation 8). Using the expectation in place of each query's own distance is an approximation; the paper does not show that it preserves the lower bounds it states.
- **The 20% line.** A sequential scan is assumed five times faster per block than random access. "Although a factor of 10 for this phenomenon is frequently assumed elsewhere (and was observed in our own PC and workstation environments), we assume a more conservative factor of only 5 here." An index is considered "to work 'well'" if on average it reads less than 20% of blocks, and to fail above that.
- **Blocks.** m = 100 points per block in the analyses of Figures 7–9. Splits are at the midpoint because the data are uniform.
- **Clusters (§3.4).** A cluster has a bounding region that covers its points and is convex, and holds at least two points. Organization above the clusters is ignored. Only the fraction of clusters visited is counted.
- **Nothing is charged for building** any structure, and nothing for updates.

## Key results

**Observations (§2.3), uniform cube.** Splitting each dimension once gives 2^d partitions, so at d = 100 nearly all of about 10^30 partitions are empty for 10^6 points. A cube range query of side 0.95 holds 0.95^100, about 0.59%, of points at d = 100. The largest sphere inside the cube (radius 0.5 at the centre) holds 0.785 of the volume at d = 2, 0.002 at d = 10 and about 2.5·10^-8 at d = 20. On average a data set needs more than 40 million points at d = 20 for one to fall in it (Table 2). The expected nearest-neighbour distance grows with d and, "Beyond trivially-small data sets", decreases "only marginally as the size of D increases" (Figures 3 and 4).

**Space-partitioning (§3.2).** Either the directory has B·2^d entries, or only d′ ≤ ⌈log2(N/m)⌉ dimensions are split (equation 10). A block's greatest distance to any point of the space is then l_max = ½√d′ (equation 11), which does not depend on d. When E[nn^dist] exceeds it, the Minkowski sum covers the cube and every block is read. For m = 100, "if the dimensionality exceeds around 60, then the entire data set must be accessed, even for very large databases" (Figure 7, N = 10^5 to 10^7).

**Rectangular bounding regions (§3.3.1).** With d′ = 10, 14 and 17 split axes for N = 10^5, 10^6 and 10^7, the probability of reading a block passes 20% at about d = 15, 18 and 20 (Figure 8). The paper calls these "upper bounds on the dimensionality at which any data-partitioning method with rectangular MBRs can be expected to perform 'well'". For d < 10 it finds "considerable scope" for such methods.

**Spherical bounding regions (§3.3.2).** Each block is taken to be a centre and its m − 1 nearest neighbours, and the sphere radius is lower-bounded by one nearest-neighbour distance, giving a block-read probability of at least the in-cube volume of a sphere of radius 2·E[nn^dist] (equations 12–13). For N = 10^6 this passes 20% at d = 26 and reaches 100% at d = 45 (Figure 9).

**Any partitioning or clustering (§3.4).** A convex cluster with two points contains the segment between them. The Minkowski sum of that segment, with the segment's length set to the expected nearest-neighbour distance and its direction chosen to minimise the sum, lower-bounds the cluster's (equations 15–17). By Monte Carlo for N = 10^6 the bound passes 20% at d ≥ 610 and tends to 1 (Figure 10). Three conclusions follow, "always having our assumptions in mind". (1) For any such method there is a dimension beyond which a scan is faster, and "in practice this threshold d̂ will be well below 610". (2) "The complexity of any clustering and partitioning methods tends towards O(N) as dimensionality increases." (3) Beyond some dimension all blocks are read on average.

**Where "around 10" comes from.** The analytical crossovers are 15–20 (rectangular), 26 (spherical) and below 610 (any convex clustering). The figure 10 in the abstract and conclusion is from the experiments of §4.2. With 50,000 uniform points and with 50,000 45-dimensional image-feature vectors, k = 10, 8K blocks, the R*-tree and X-tree passed the 20% line "if dimensionality exceeds 10" (Figures 14 and 15). Only these two trees were tested. The paper does not say how the lower-dimensional versions of the 45-dimensional real vectors were formed.

**The VA-file (§4).** Each dimension i gets b_i bits, typically 4 to 8, and 2^{b_i} slices chosen so that "all slices are equally full", that is, at the data's marginal quantiles. Each vector is stored as the bit-string of its cell, in a flat array. The approximation file is 4 to 8 times smaller than the vectors. The 2^b cells far outnumber the points, so few points share a cell (equations 18–19). A query scans the whole approximation file, using each cell's lower and upper bounds on distance to drop vectors whose lower bound exceeds the best upper bound so far. It then visits the remaining candidates in order of lower bound and stops when the next lower bound exceeds the k-th distance found. At d = 50, uniform, k = 10, b_i = 6: under 0.1% of vectors remain after filtering at N = 500,000, and about 19–20 vectors are read in all (Figure 12). The fraction of vector blocks read falls as d rises (Figure 13, N = 100,000). This counts only the vector file, not the approximation file, which is always read whole.

**Timings.** On the 45-dimensional image data (Figure 16, log scale), the sequential scan is fastest for 5 ≤ d ≤ 6 and the X-tree for d < 5. For d ≥ 6 the VA-file is fastest, and the trees are slower than the scan from about 10 dimensions on, as read from the figure. On 5-dimensional uniform data (Figure 17), the X-tree is faster than the VA-file, though "the performance gain compared to the VA-File is not overwhelming", and its cost grows linearly with N.

**Stated in the conclusions, not shown.** "we postulate that all approaches to nearest-neighbor search in HDVSs ultimately become linear at high dimensionality." This is a postulate, and the VA-file itself is linear.

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md).** This is the record's first reading of a regime where organizing does not pay even with building free. Under uniform independent data with nearest-neighbour queries, any partition into blocks or convex clusters ends up reading every block. With a cost model that gives the scan a five-fold sequential advantage, that happens at a modest dimension. [QUESTION-114](../questions.d/QUESTION-114.md) asks when sorting pays as amortized search. This paper's answer is a precondition on the data and query geometry, not a ledger of build cost against savings. If the data are spread out, so that the nearest neighbour is far relative to block size, the lookup savings that would repay any build cost do not exist. Its remedy is not a better arrangement but a compressed summary of every item, scanned in full. That is a different kind of organizing: precomputed per-item descriptions, not partition into bins. It pays for the approximation file's space and its upkeep on inserts (fixed slice boundaries), and the paper prices neither. It does not supply the joint model the question lacks.

**On [CLAIM-310](../claims.d/CLAIM-310.md).** It narrows the claim's part 1. The bin-budget arithmetic (expected cost k/2 + N/(2k), least near k = √N) assumes a query opens one bin and scans it. For similarity queries over many independent continuous coordinates, a query must open nearly every bin once dimension passes the crossover, so the cost is N however the bins are drawn. The claim's dependence on the query mix survives in sharpened form. Bins pay for queries that name a sorted attribute, which is an exact or partial match, and do not pay for nearest-by-overall-similarity over many coordinates. LEGO sorting is the first kind: a few discrete attributes, named in the query. So the paper does not threaten the claim for its own case. It marks the boundary where arrangement stops doing work: similarity over many dimensions, none of which the query names.

**On [CLAIM-309](../claims.d/CLAIM-309.md).** No bearing. It is about the cost of finding the nearest item, not about discriminability or preference. The LIT's filing ties it to [CLAIM-309](../claims.d/CLAIM-309.md) together with [QUESTION-114](../questions.d/QUESTION-114.md), and only the latter link holds.

**On [THEORY-340](../theory.d/THEORY-340.md).** A counterpart. Yao shows sorted order optimal for exact membership only under narrow conditions, counting worst-case probes. Weber et al. show partitioned order beaten by no order at all for high-dimensional nearest-neighbour search, counting average blocks. Both price lookup only, with building free. The results are of different strength. Yao's are theorems over all schemes in Yao's class. Weber et al.'s are Monte Carlo estimates under uniformity, with the expected nearest-neighbour distance substituted for each query's own, and with the 20% line set by an assumed cost ratio.

**What the results do not show.**
- That indexes fail on real high-dimensional data in general. The analysis assumes uniform, independent coordinates. Data with low intrinsic dimension, clusters or correlations are outside it except by the untested fractal-dimension conjecture. The one real set (45-dimensional colour features from one image collection, N = 50,000) degraded like uniform data. That is one data set.
- That partitioning degrades to a scan "beyond about ten dimensions" as a general threshold, which is how the LIT's filing put it. It is the measured crossover for two tree implementations on 50,000 points, under the 20% line. The analysis gives 15 to 26 for those classes and a loose bound of 610 for convex clustering in general.
- That no structure beats a scan. Only structures that partition or cluster into convex regions of two or more points are covered. The VA-file is outside the theorem by design, and so are hashing schemes and structures that do not bound groups of points.
- That the lower bounds are rigorous. Replacing each query's nearest-neighbour distance with its expectation, and the Monte Carlo evaluation of the integrals, are not shown to preserve the inequalities.
- Anything about whether the nearest neighbour is worth finding. That is Beyer et al. ([LIT-1099](../literature.d/LIT-1099.md)). The two agree on the setting that defeats search: independent coordinates, under which the expected nearest-neighbour distance grows with dimension (Weber et al. cite the central limit theorem) and distances bunch together.
