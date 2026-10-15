---
status: Active
title: "Locality-sensitive hashing answers approximate near-neighbour queries over n points with O(n^ρ) hash evaluations in O(dn + n^{1+ρ}) space, where ρ = ln(1/p1)/ln(1/p2) is set by how much more often near pairs collide than far ones and is at most 1/(1+ε) for approximation 1+ε in Hamming space, with constant success probability per query; the paper gives upper bounds only and proves no limit on what organizing can buy"
version: 1
tags:
- databases
- information-retrieval
- mathematics
date: '2026-10-15'
source:
- LIT-tmpa1ovj
summary: >-
  Indyk and Motwani (1998), [LIT-tmpa1ovj](../literature.d/LIT-tmpa1ovj.md), read in [NOTE-tmp3up5l](../notes.d/NOTE-tmp3up5l.md) from the
  authors' 1999 expanded version, compared with the STOC text. A hash family
  under which points within r1 collide with probability at least p1 and points
  beyond r2 with at most p2 gives n^ρ random tables, each storing every point:
  O(dn + n^{1+ρ}) space and O(n^ρ) hash evaluations per query, ρ =
  ln(1/p1)/ln(1/p2), for the decision version, which ring-cover trees connect
  to approximate nearest neighbour with polylog overhead. Bit sampling gives
  ρ ≤ 1/(1+ε) in Hamming space and, by embedding, ℓ_p for p in [1, 2]; the
  STOC text states 1/ε and only for ε > 1. Grid bucketing gives Õ(d) queries
  for n·O(1/ε)^d preprocessing. Preprocessing is counted as space. Nothing is
  proved about whether these exponents can be beaten.
extended_by:
- THEORY-tmpehk94
---

# THEORY-tmpvi601: Locality-sensitive hashing answers approximate near-neighbour queries over n points with O(n^ρ) hash evaluations in O(dn + n^{1+ρ}) space, where ρ = ln(1/p1)/ln(1/p2) is set by how much more often near pairs collide than far ones and is at most 1/(1+ε) for approximation 1+ε in Hamming space, with constant success probability per query; the paper gives upper bounds only and proves no limit on what organizing can buy

## Source

Indyk and Motwani (1998), [LIT-tmpa1ovj](../literature.d/LIT-tmpa1ovj.md), STOC 1998 pp. 604–613, read in
[NOTE-tmp3up5l](../notes.d/NOTE-tmp3up5l.md) from the authors' "preliminary version" of December 30, 1999
(Indyk's MIT directory), with every statement compared against the STOC
text. Theorem numbers are the 1999 text's.

## What was actually shown

**The problem and the cost model.** Given n points in a metric space,
answer a query q with a point within (1+ε) times the nearest distance, or,
in the decision version (ε-PLEB), say whether some point lies within r or
none within (1+ε)r. The algorithms are randomized and succeed with constant
probability per query, for every data set and query. "Throughout,
preprocessing cost refers to the space requirement; typically, the
preprocessing time is roughly the same."

**The LSH theorem (Theorem 5).** If a family H is (r1, r2, p1, p2)-sensitive
(near pairs collide with probability at least p1, far pairs at most p2), then
concatenating k = log_{1/p2} n functions per table and keeping l = n^ρ tables
answers (r1, r2)-PLEB in O(dn + n^{1+ρ}) space with O(n^ρ) hash evaluations,
ρ = ln(1/p1)/ln(1/p2). Every point is stored in every table. Bit sampling is
sensitive in Hamming space (Proposition 4), giving ρ ≤ 1/(1+ε) (Corollary 3);
embeddings carry this to ℓ_p, p in [1, 2] (Proposition 1). Min-wise hashing
does the same for set resemblance (Corollary 4).

**The STOC text is weaker.** It defines ρ = ln(1/p1)/ln(p1/p2), and states
Proposition 1 and Corollary 3 "For ε > 1" with exponent 1/ε, so in the
published version sublinear queries are claimed only for approximation
factors above 2.

**The other end (Propositions 2, 3).** Storing every grid cell that meets a
ball in a perfect hash table gives Õ(d) query time for n·O(1/ε)^d
preprocessing, any ℓ_p; random projection first gives (nd)^{O(1)}
preprocessing with an exponent growing in 1/ε.

**From decision to search (Section 3).** One PLEB structure per radius costs
O(log R) space for R the spread of distances; ring-cover trees remove R,
built in Õ(n²) time with O(log² n · log k) PLEB queries per search. Some
proofs are sketches.

**What could have come out otherwise.** A sensitive family with the stated
p1, p2 for which no choice of k and l reaches the stated bounds would refute
Theorem 5; the analysis is a short calculation and has been reused since.

## What this does not say

- **That these exponents are the best possible**, for hashing or for any
  structure. The paper proves no lower bound. That question is
  [THEORY-tmpehk94](THEORY-tmpehk94.md)'s and [THEORY-tmpnbhb3](THEORY-tmpnbhb3.md)'s.
- **That organizing ahead pays after some number of queries.** Costs are per
  query, worst case; there is no query sequence, workload or break-even, no
  build cost apart from space, and upkeep only in dynamic variants that
  need bounded integer coordinates.
- **Anything about exact nearest neighbours**, or about answers with higher
  than constant probability without extra copies.
- **That one partition suffices.** The construction needs n^ρ independent
  random partitions precisely because one separates near pairs too often.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): three points on the trade between space paid once and time
  per query for similarity search (n^{1+1/(1+ε)} against n^{1/(1+ε)};
  n·O(1/ε)^d against Õ(d); linear space against a linear scan). It prices
  neither side's minimum.
- [CLAIM-310](../claims.d/CLAIM-310.md): the single-arrangement constraint is escaped by keeping many
  random partitions and storing every point in each, paid for in space;
  the partitions ignore the query mix.
- [THEORY-340](THEORY-340.md): the same convention that building is free, for similarity
  rather than membership; algorithms, not a lower bound.
- [THEORY-tmpehk94](THEORY-tmpehk94.md) extends this account to the full curve of space against query
  exponents and shows where it is optimal.
