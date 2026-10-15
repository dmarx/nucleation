---
status: Active
title: "For c-approximate near-neighbour search over n points in Euclidean space, space n^{1+ρu+o(1)} and query time n^{ρq+o(1)} are achievable on any data set whenever c²√ρq + (c²−1)√ρu ≥ √(2c²−1) (c√ρq + (c−1)√ρu ≥ √(2c−1) in Hamming space), and no list-of-points structure, the model of known data-independent hashing, does better on random instances; without that model the curve is matched only at query time n^{o(1)} by one or two cell probes"
version: 1
tags:
- databases
- information-retrieval
- mathematics
date: '2026-10-15'
source:
- LIT-tmpxroug
answers:
- QUESTION-114
extends:
- THEORY-tmpvi601
presupposes:
- THEORY-tmpnbhb3
summary: >-
  Andoni, Laarhoven, Razenshteyn and Waingarten (2017), [LIT-tmpxroug](../literature.d/LIT-tmpxroug.md), read in
  [NOTE-tmptdi3z](../notes.d/NOTE-tmptdi3z.md) from the arXiv full version. A data-dependent tree of spherical
  caps, with different thresholds for filing points and for routing queries,
  realizes every pair of exponents on the curve, for worst-case data, with
  constant success probability; the equal-threshold point is LSH. On random
  instances with d = ω(log n), list-of-points structures cannot beat the curve
  (a lower bound the paper calls conditional), and one- or two-probe cell-probe
  structures need n^{(c/(c−1))²−o(1)} words, the curve's space at ρq = 0.
  Optimality for data-dependent schemes, for more probes, and for
  d = Θ(log n) is not shown. The curve prices space against per-query time
  for one query at a time; it has no workload and no build cost beyond space.
supports:
- CLAIM-310
---

# THEORY-tmpehk94: For c-approximate near-neighbour search over n points in Euclidean space, space n^{1+ρu+o(1)} and query time n^{ρq+o(1)} are achievable on any data set whenever c²√ρq + (c²−1)√ρu ≥ √(2c²−1) (c√ρq + (c−1)√ρu ≥ √(2c−1) in Hamming space), and no list-of-points structure, the model of known data-independent hashing, does better on random instances; without that model the curve is matched only at query time n^{o(1)} by one or two cell probes

## Source

Andoni, Laarhoven, Razenshteyn and Waingarten (2017), [LIT-tmpxroug](../literature.d/LIT-tmpxroug.md), SODA 2017,
read in [NOTE-tmptdi3z](../notes.d/NOTE-tmptdi3z.md) from arXiv:1608.03580v2, the full version merging the two
preprints behind the extended abstract.

## What was actually shown

**The problem.** (c, r)-ANN, c > 1: given that some point lies within r of
the query, return a point within cr. Randomized structures, success
probability at least 0.9 per query, expected space and time.

**Upper bound (Theorem 1.1).** For every ρq, ρu ≥ 0 with
c²√ρq + (c² − 1)√ρu ≥ √(2c² − 1), a structure for any data set in ℝ^d has
space n^{1+ρu+o(1)} + O(dn) and query time n^{ρq+o(1)} + dn^{o(1)}. Points are
filed under every Gaussian cap of threshold ηu they fall in, queries look in
every cap of threshold ηq they fall in, and dense clusters are removed and
recursed on so that what remains looks random. Endpoints: query n^{o(1)}
with space n^{c⁴/(c²−1)²}; near-linear space with query n^{(2c²−1)/c⁴},
sublinear for every c > 1; ρq = ρu = 1/(2c²−1). For c = 2: n^{1.77} with
n^{o(1)}, n^{1.14} with n^{0.14}, n^{1+o(1)} with n^{0.43}. By cited
reductions, c² becomes c^p for ℓ_p, 1 ≤ p < 2. Updates cost dn^{ρu+o(1)}.

**Lower bound in the hashing model (Theorem 1.6).** A list-of-points
structure fixes sets A_i independently of the data, keeps L_i = P ∩ A_i,
and has a query scan the lists in I(q); space counts list entries and time
counts entries scanned. On random Hamming instances (uniform points,
d = ω(log n), query a noisy copy of a data point), any such structure with
space n^{1+ρu}, query time n^{ρq−o(1)} and success 2/3 satisfies
c√ρq + (c − 1)√ρu ≥ √(2c − 1). The paper says it captures "all
hashing-based frameworks we are aware of", but not data-dependent ones,
including its own upper bound.

**Unconditional bounds at one end (Theorems 1.3, 1.4).** In the cell-probe
model, one probe with cells of n^{o(1)} bits, or two probes with cells of
o(log n) bits, need n^{(c/(c−1))²−o(1)} words on the random instance: the
curve's space at ρq = 0. The one-probe bound applies the robust-expansion
framework of [THEORY-tmpnbhb3](THEORY-tmpnbhb3.md) with a tight expansion estimate; the two-probe
bound goes through locally decodable codes. "Informally speaking, Theorem
1.4 shows that the second cell probe cannot improve the space bound by more
than a subpolynomial factor."

**What could have come out otherwise.** A list-of-points scheme beating the
curve on random instances, or a one-probe structure with fewer words, would
refute the theorems; and the upper bound could have needed worse exponents
on worst-case data than on random data, as the data-independent scheme alone
does ((c² + 1)√ρq + (c² − 1)√ρu ≥ 2c, Theorem 1.2).

## What this does not say

- **That the curve is optimal for every data structure.** It is shown for
  list-of-points structures and, at ρq = 0, for one or two probes. The paper:
  "proving similar lower bounds unconditionally is far beyond the current
  reach of techniques." Data-dependent schemes are covered by conjecture.
- **That it holds in low dimension.** The lower bounds need d = ω(log n);
  the case d = Θ(log n) is open.
- **That real collections cost this much.** The hard inputs are random. A
  data-dependent scheme may do better on data with structure; the bound does
  not say how much.
- **Anything about exact nearest neighbours**, ranking, or query
  distributions.
- **An amortized or workload-based cost model.** Costs are per query for a
  fixed data set. The paper's one amortized remark is that n queries cost
  n^{1+ρu} + n^{1+ρq} "(implying that the balanced, LSH regime is most
  relevant)". Build time is taken as near-linear in space, and upkeep enters
  only as dynamized update time.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): for one problem, the exact price of organizing ahead
  against per-query cost, as replication (each point in about n^{ρu} lists)
  against lists scanned (about n^{ρq}). With Q queries the total is about
  n^{1+ρu} + Q·n^{ρq} (the record's arithmetic), so the best point moves
  toward more organization as expected use grows. It is a part-answer: one
  query type, no workload, no staleness.
- [CLAIM-310](../claims.d/CLAIM-310.md): the lists may overlap, and at near-linear space query time is
  at least n^{(2c−1)/c²−o(1)} in Hamming space, so fast similarity search
  needs items filed in many bins. Nothing here bears on query mixes.
- [THEORY-340](THEORY-340.md): the similarity analogue of a lookup floor, holding at one and
  two probes with arbitrary cell encoding, where Yao's sorted-order
  optimality needed restricted cell contents.
- [THEORY-345](THEORY-345.md): a different question (one structure for one query type, no
  index choice for a workload); no conflict.
- Extends [THEORY-tmpvi601](THEORY-tmpvi601.md), whose bit-sampling LSH is a balanced (ρq = ρu)
  data-independent point, ρ = 1/c in Hamming space, above this curve's
  1/(2c−1); presupposes [THEORY-tmpnbhb3](THEORY-tmpnbhb3.md) for the one-probe bound.
