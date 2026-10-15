---
status: Proposed
promote_when: >-
  A proof that, for uniformly distributed independent data and queries in
  the unit cube and any partition of N points into convex clusters of at
  least two points, the expected fraction of clusters an optimal
  nearest-neighbour search must read tends to one as dimension grows at
  fixed N. The proof must use each query's own nearest-neighbour distance,
  not its expectation. Alternatively, an independent replication with other
  index implementations and data sizes that measures the crossover against
  a scan. More simulations of the paper's own Monte Carlo integrals would
  not settle it, and neither would results on data with low intrinsic
  dimension.
title: "Under uniformly distributed, independent data and queries in the unit cube with Euclidean distance, an optimal nearest-neighbour search over any index that partitions points into blocks or convex clusters must read a fraction of blocks that grows toward all of them as dimension rises; with a five-fold sequential advantage for scanning, estimates put the crossover at about 15–26 dimensions for rectangular and spherical bounding regions, and two tree indexes measured on 50,000 points lost to a scan beyond about 10"
version: 1
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-tmpb8ql6
answers:
- QUESTION-114
summary: >-
  Weber, Schek and Blott (1998), [LIT-tmpb8ql6](../literature.d/LIT-tmpb8ql6.md), read in [NOTE-tmpvtj3f](../notes.d/NOTE-tmpvtj3f.md). Under
  uniformity and independence, with the expected nearest-neighbour distance
  used as every query's radius and integrals evaluated by Monte Carlo,
  the fraction of blocks read passes the 20% line at about d = 15–20 for
  rectangular regions and 26 for spherical ones. A crude bound for any convex
  clustering puts it below 610. The often-quoted "around 10" is the measured
  crossover for an R*-tree and an X-tree. The VA-file, a scan of compact
  per-vector approximations, is the paper's alternative. Nothing is shown
  for data of low intrinsic dimension, and the lower bounds are not
  rigorous as stated.
---

# THEORY-tmpc74vc: Under uniformly distributed, independent data and queries in the unit cube with Euclidean distance, an optimal nearest-neighbour search over any index that partitions points into blocks or convex clusters must read a fraction of blocks that grows toward all of them as dimension rises; with a five-fold sequential advantage for scanning, estimates put the crossover at about 15–26 dimensions for rectangular and spherical bounding regions, and two tree indexes measured on 50,000 points lost to a scan beyond about 10

## Source

Weber, Schek and Blott (1998), [LIT-tmpb8ql6](../literature.d/LIT-tmpb8ql6.md), "A quantitative analysis and
performance study for similarity-search methods in high-dimensional
spaces", VLDB 1998, pp. 194–205. Read in full in [NOTE-tmpvtj3f](../notes.d/NOTE-tmpvtj3f.md), from the VLDB
Endowment's copy.

## What was actually shown

**Setting.** Uniform, independent data and queries in [0, 1]^d; Euclidean
distance; cost is blocks read by the optimal search, which reads exactly
the blocks whose bounding region meets the query's nearest-neighbour
sphere. That sphere's radius is set to the expected nearest-neighbour
distance, which grows with d and barely falls as N grows (Monte Carlo).
A scan is assumed five times faster per block, so an index is counted as
failing once it reads more than 20% of blocks. Building and updating are free.

**Space partitioning.** Either the directory has 2^d entries, or only
about log2(N/m) axes are split. Then every block reaches within ½√d′ of
any point, which does not grow with d, and once the expected
nearest-neighbour distance exceeds it every block is read. For 100 points
per block that happens past about d = 60.

**Data partitioning.** Rectangular bounding regions pass 20% at about
d = 15, 18 and 20 for N = 10^5, 10^6 and 10^7. Spheres, lower-bounded by a
radius of twice the expected nearest-neighbour distance, pass 20% at
d = 26 and reach 100% at d = 45 for N = 10^6.

**Any convex clustering.** A cluster of two or more points contains a
segment whose Minkowski sum lower-bounds its own. With the segment's
length set to the expected nearest-neighbour distance and the best
orientation, the access probability passes 20% at d ≥ 610 and tends to 1
for N = 10^6. The authors say the true crossover is "well below 610".

**Measured.** With an R*-tree and an X-tree, k = 10 and 8K blocks, on
50,000 uniform points and on 50,000 45-dimensional image-colour vectors,
the fraction of leaf blocks read passed 20% beyond d = 10. In wall-clock
time on the image data, the trees fell behind a scan from about the same
point.

**The VA-file.** Store, for each vector, the cell code from 4–8 bits per
dimension at the data's marginal quantiles. Scan this file, 4–8 times
smaller than the vectors, and drop vectors whose lower bound exceeds the
best upper bound. Then read the remaining candidates in order of lower
bound. At d = 50 and N = 500,000, under 0.1% of vectors survived the
filter and about 20 were read for k = 10. On the image data it was fastest
for d ≥ 6.

**What could have come out otherwise.** The measured trees could have
stayed under 20% past 10 dimensions on these data. They did not, on either
the uniform or the image set.

## What this does not say

- **That indexes fail on real high-dimensional data.** Uniformity and
  independence are assumptions. Data with low intrinsic dimension,
  clusters or correlation are covered only by a conjecture that the
  results follow fractal dimension, which is not tested. The one real set
  is 45-dimensional colour features from one image collection.
- **That about ten dimensions is a threshold.** It is the measured
  crossover for two tree implementations at N = 50,000 under an assumed
  cost ratio. The analysis gives 15–26 for those classes and only a loose
  610 in general. The 20% line moves with the assumed sequential
  advantage.
- **That nothing beats a scan.** The bound covers organizations that group
  points into convex regions. The VA-file escapes it by being a scan of
  smaller records, and the paper's claim that all methods "ultimately
  become linear" is stated as a postulate.
- **That the bounds are rigorous.** Using the expected nearest-neighbour
  distance in place of each query's own, and evaluating the volumes by
  Monte Carlo, are not shown to preserve the inequalities.
- **Anything about build cost, upkeep or amortization.** Building is
  free. That organizing fails here even so is the point, but the paper
  does not price the VA-file's space or upkeep either.

## Connections

- [THEORY-tmpazpbe](THEORY-tmpazpbe.md) (Beyer et al., [LIT-tmp0cvca](../literature.d/LIT-tmp0cvca.md)) is the companion on meaning.
  In the same independent-coordinate setting, nearest and farthest
  distances converge in ratio, so the answer these indexes struggle to
  find carries little contrast.
- [QUESTION-114](../questions.d/QUESTION-114.md): a part-answer on when organizing pays. For similarity
  queries over many independent coordinates it does not, even with
  building free. The paying alternative is a compact per-item summary
  scanned in full, not a partition.
- [CLAIM-310](../claims.d/CLAIM-310.md): the bin-budget cost assumes a query opens one bin. For
  similarity over coordinates the query does not name, it opens nearly
  all of them past the crossover. Queries that name a sorted attribute,
  as in LEGO bins, are outside this result.
- [THEORY-340](THEORY-340.md): like Yao, lookup cost only, with building free. Yao has
  theorems for exact membership. This is average-case estimates for
  similarity, where partitioned order loses to no order.
