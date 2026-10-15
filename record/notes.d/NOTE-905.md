---
number: 905
status: Read
formerly:
- NOTE-tmp3up5l
paper: LIT-1106
title: 'Indyk & Motwani — Approximate nearest neighbors: towards removing the curse
  of dimensionality'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read on 2026-10-15 in two copies of the same paper. (1) The authors' own expanded
    text, "Approximate Nearest Neighbors: Towards Removing the Curse of Dimensionality
    (preliminary version)", dated December 30, 1999, 20 pages, Stanford affiliations,
    served from Indyk's MIT page at https://people.csail.mit.edu/indyk/nndraft.ps
    (PostScript, 271,935 bytes, sha256 d6de8f93…; dvips output of nnff.dvi), converted
    with ps2pdf and extracted with pdftotext. The identical file is posted on a
    Stanford course page (graphics.stanford.edu/courses/cs468-06-fall/Papers/06
    indyk motwani - stoc98.pdf, 316,230 bytes, title nnff.dvi, same text). This
    was read in full: abstract, Sections 1–4, the proof sketches, Appendices A and
    B, and the references. (2) The STOC 1998 proceedings text itself (pp. 604–613,
    page numbers printed), a 10-page scan with an OCR layer posted on a Princeton
    course page, COS 598B, Spring 2004 (https://www.cs.princeton.edu/courses/archive/spr04/cos598B/bib/IndykM-curse.pdf,
    1,329,799 bytes, sha256 f5bf7733…). That copy is the publisher's printed paper
    hosted by a course, not an author's copy; it was used to compare statements,
    not as the reading text. The OCR is poor, so the STOC statements were compared
    section by section with the 1999 text, and pages 605, 609, 610, 611 and 613
    were checked as page images. The two differ in the LSH exponent and its range
    of ε (see Key results), and the STOC version has two appendix theorems (Theorems
    5 and 6) that the 1999 text drops. Theorem numbers below are the 1999 text's
    unless marked STOC. Not read: the journal version, Har-Peled, Indyk and Motwani,
    Theory of Computing 8 (2012) 321–350 (https://theoryofcomputing.org/articles/v008a014/v008a014.pdf,
    open access, fetched, 30 pp.), which merges this paper with Indyk's FOCS 2001
    paper and was opened only to identify it. Other places looked, all 2026-10-15:
    Unpaywall for 10.1145/276698.276876 (closed, no OA location); OpenAlex (closed,
    only the ACM landing page); ACM DL PDF (403); a Princeton spring 2013 course
    URL (404); Indyk's MIT home page (200, does not link nndraft.ps directly; the
    file is served from Indyk's directory). Quotations below are from the 1999 text
    unless marked STOC, and were checked against its pdftotext extraction by script,
    whitespace normalised; that extraction drops the fi/ff ligatures and Greek letters,
    so the check ignores ligature letters. The two short STOC quotations ("For ε
    > 1" and "(for ε > 1)") were checked against the page image of p. 605 and the
    OCR of p. 604, and the one quotation of the record against QUESTION-114.
date: '2026-10-15'
summary: >-
  Approximate nearest-neighbour search in d dimensions reduces, with small overhead,
  to a decision problem (is there a point within r, or none within (1+ε)r), and
  that decision problem is solved by locality-sensitive hashing: if hash functions
  make near pairs collide with probability at least p1 and far pairs with at most
  p2, then n^ρ random hash tables with ρ = ln(1/p1)/ln(1/p2) answer queries with
  O(n^ρ) hash evaluations in O(dn + n^{1+ρ}) space, with constant success probability.
  For Hamming space by bit sampling, and for ℓ_p with p in [1, 2] by embedding,
  ρ ≤ 1/(1+ε) in the 1999 text (1/ε, for ε > 1, in STOC). The paper also gives the
  other end of the trade: Õ(d) query time for n·O(1/ε)^d or (nd)^{O(1)} preprocessing.
  It is an upper bound only: it proves no lower bound, does not claim its exponents
  are best, solves only the approximate problem with constant probability, and counts
  preprocessing as space.
---

# NOTE-905: Indyk & Motwani — Approximate nearest neighbors: towards removing the curse of dimensionality

## Contribution

Before this paper, exact nearest-neighbour structures in high dimension had
either query time linear in n or preprocessing exponential in d, and the
paper says the approximate problem had not escaped either: "The known
algorithms are of two types: (a) low preprocessing cost but query time
linear in n and d; and, (b) query time sublinear in n and polynomial in d,
but with severely exponential preprocessing cost". It gives the first
structures for ε-approximate nearest neighbour with space polynomial in n
and d and query time sublinear in n, and the first with polynomial
preprocessing and query time polynomial in d and log n. The vehicle for the
first is locality-sensitive hashing (LSH), introduced here. The paper also
introduces ring-cover trees, which reduce the search problem to its
decision version.

## Key insight

A query need not search a space; it can look in a few buckets if the
bucketing was chosen at random so that near points tend to share buckets
and far points tend not to. One random partition separates a near pair
too often, so the structure keeps many independent partitions and stores
every point in each of them. How many partitions are needed is set by how
much more often near pairs collide than far ones: n^ρ partitions, with
ρ = ln(1/p1)/ln(1/p2). Space is paid once, by copying each point into every
partition; per-query time is paid by looking in one bucket of each. The
paper's own words: "The key idea is to use hash functions such that the
probability of collision is much higher for objects that are close to each
other than for those that are far apart."

## Assumptions

- **Approximate answers.** A point p with d(p, q) ≤ (1+ε) d(p′, q) for all
  p′ in the set (ε-NNS), or the decision version ε-PLEB (point location in
  equal balls): say yes with a witness if some point is within r, no if
  none is within (1+ε)r, either otherwise. Exact search is not solved.
- **Randomized, constant success probability.** "Our algorithms are
  randomized and return an approximate nearest neighbor with constant
  probability." Lower error costs a factor O(log(1/δ)) in parallel copies.
  The guarantee is per query over the algorithm's coins, for every data
  set and query; no distribution on data or queries is assumed.
- **Cost model.** Footnote 1: "Throughout, preprocessing cost refers to
  the space requirement; typically, the preprocessing time is roughly the
  same." Query time counts hash evaluations or distance computations; Õ
  hides polylog n factors.
- **Metrics.** LSH applies directly to Hamming space; ℓ_1 reaches it by an
  embedding that needs bounded integer coordinates (Fact 4, Linial, London
  and Rabinovich), and ℓ_p for p in [1, 2] reaches ℓ_1 by
  Johnson–Schechtman (Fact 3). The bucketing method works for any ℓ_p.
  Set resemblance (Broder's measure) gets its own hash family.
- **Static data**, except Section 4.3's dynamic variants, which need
  integer coordinates bounded by M.

## Key results

Notation: n points, dimension d, approximation 1+ε (1999 text).

- **Proposition 1 (LSH).** For ε > 0, ε-NNS in ℝ^d under ℓ_p, p in [1, 2],
  with Õ(n^{1+1/(1+ε)} + dn) preprocessing and Õ(dn^{1/(1+ε)}) query time.
  *STOC version:* "For ε > 1", Õ(n^{1+1/ε} + dn) preprocessing and
  Õ(dn^{1/ε}) query time, checked on the page image (p. 605). The STOC
  abstract qualifies sublinear query time "(for ε > 1)". So the STOC paper
  claims sublinear query time only for approximation factor above 2 in its
  own (1+ε) convention; the 1999 text extends it to every ε > 0.
- **Proposition 2 (bucketing).** For 0 < ε < 1, ε-NNS under any ℓ_p with
  Õ(n)·O(1/ε)^d preprocessing and Õ(d) query time. Theorem 4 (STOC 3):
  ε-PLEB in ℓ_p^d with O(n)·O(1/ε)^d preprocessing and O(1) hash
  evaluations per query, by storing every grid cell of side ε/√d that meets
  a ball in a perfect hash table.
- **Proposition 3.** For any ε > 0, under ℓ_p, p in [1, 2], (nd)^{O(1)}
  preprocessing and Õ(d) query time, by random projection to O(ε⁻² log n)
  dimensions and Proposition 2. The exponent of the polynomial grows with
  1/ε, and the paper calls this "a purely theoretical result".
- **Theorem 5 (STOC 4), the LSH theorem.** If H is (r1, r2, p1, p2)-sensitive
  for D (Pr[h(q) = h(p)] ≥ p1 when p is within r1 of q, ≤ p2 when p is beyond
  r2), there is an algorithm for (r1, r2)-PLEB using O(dn + n^{1+ρ}) space
  and O(n^ρ) hash evaluations per query, with ρ = ln(1/p1)/ln(1/p2). The
  construction concatenates k = log_{1/p2} n functions per table, keeps
  l = n^ρ tables, and stops a query after 2l points. *STOC version:*
  ρ = ln(1/p1)/ln(p1/p2), which is larger, with a different stopping rule
  (each bucket keeps one arbitrary point).
- **Corollary 3.** Bit sampling, (r, r(1+ε), 1 − r/d, 1 − r(1+ε)/d)-sensitive
  (Proposition 4), gives ε-PLEB in Hamming space, and in ℓ_p for p in [1, 2],
  with O(dn + n^{1+1/(1+ε)}) space and O(n^{1/(1+ε)}) hash evaluations, each
  O(d) operations. The proof assumes r < d/ln n, achieved by padding
  coordinates. *STOC:* ε > 1, n^{1/ε}.
- **Corollary 4.** Min-wise hashing (Proposition 5, from Broder et al.) is
  (r1, r2, r1, r2)-sensitive for set resemblance, giving the same kind of
  structure for resemblance queries, and for dot product among binary
  vectors of near-equal weight.
- **Reduction to the decision problem (Section 3).** The simple reduction
  keeps one PLEB structure per radius (1+ε)^i: query overhead
  O(log log R), space overhead O(log R), where R is the ratio of the
  extreme interpoint distances; "the O(log R) space overhead is
  unacceptable when R is large; in general, R may be unbounded". The
  ring-cover tree removes the dependence on R: built in deterministic
  Õ(n²) time (Theorem 3), depth O(log² n) (Lemma 2), O(log² n · log k)
  distance computations or PLEB queries per search (Lemma 3), and total
  space O(f(n polylog n)) given a PLEB structure of convex space f(n)
  (Corollary 2). Lemmas 2 and 3 are stated without proof, and the base case
  is omitted "in this abstract".
- **Dynamic variants (Corollaries 5, 6).** With integer coordinates bounded
  by M: bucketing gives O(1/ε)^d poly(log M, log n) per insertion, deletion
  or query in O(1/ε)^d n storage; LSH gives Õ(dn^{1/(1+ε)}) per operation in
  O(dn + n^{1+1/(1+ε)}) storage (STOC: O(Mdn^{1/ε}) time, so the STOC
  dynamic bound is linear in M).
- **Experiments.** None in this paper. It cites its authors' manuscript
  with Gionis: for 20,000 colour histograms with d up to 64, "only 3-9
  disk accesses were required in order to achieve small average error".
- **Appendix A.** A simpler proof of a Johnson–Lindenstrauss-type lemma
  with Gaussian projections (Lemma 6; STOC Lemma 7). STOC only: Theorem 5,
  any n points of ℓ_p, p in [1, 2], map to ℓ_2^k with k = O(log n) so that
  the squared ℓ_2 distance is within 1 ± ε of the ℓ_p distance; Theorem 6,
  the Johnson–Lindenstrauss lemma fails for ℓ_∞ (some n-point set needs
  distortion Ω(log n/√f) in f dimensions).

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): the first price list for organizing a collection for
similarity queries, with the two costs on one axis each.**

- The paper's three propositions are three points on a trade between what
  is paid once and what is paid per query: about n^{1+1/(1+ε)} space for
  about n^{1/(1+ε)} query time (Proposition 1), n·O(1/ε)^d or (nd)^{O(1)}
  for Õ(d) (Propositions 2 and 3), and linear space for linear-time scan.
  Neither end is free, and the paper offers no point that is cheap in both.
  That is the shape the question's trade, paid once against saved each
  time, has when the query is similarity rather than membership.
- What is paid once is space, and the paper says preprocessing time is
  "roughly the same". There is no separate build cost, no upkeep beyond
  the dynamic corollaries (each update costs as much as a query), and no
  number of queries at which organizing pays. The bounds are per query,
  worst case over data and query; the paper never amortizes over a query
  sequence and has no workload or query mix.
- It does not say that organizing is necessary. It proves no lower bound,
  so it cannot say that linear scan is the only way to avoid large space.
  That is K14 and K15's subject ([LIT-1120](../literature.d/LIT-1120.md), [LIT-1102](../literature.d/LIT-1102.md)).

**On [CLAIM-310](../claims.d/CLAIM-310.md): LSH escapes the constraint that one set of bins realizes
one partition by keeping many sets of bins, and pays for each in a copy of
the data.**

- Each hash table is a partition of the space into buckets, and every
  point is stored in every table: n^ρ partitions, so n^{1+ρ} stored
  entries. The paper's own reason for many partitions is that one random
  partition separates a near pair too often. So for similarity queries in
  high dimension, the paper's remedy for the single-arrangement constraint
  is redundancy, priced in space, as [QUESTION-114](../questions.d/QUESTION-114.md)'s title has it: "every
  further index is paid for in space".
- This does not test the claim's dependence on the query mix. LSH's
  partitions are random and chosen without any knowledge of queries; the
  structure serves every query equally. And the claim is about discrete
  attributes of bricks, which a hash table on the attribute serves in O(1);
  the paper's hardness lives in high-dimensional similarity.

**On [THEORY-340](../theory.d/THEORY-340.md).** Yao's question, which arrangement minimizes worst-case
probes for membership, has its similarity analogue here, with the same
convention that building is free (space stands in for it). But this paper
gives algorithms, not a lower bound, and its cost unit is hash evaluations
and distance computations, not cell probes. It neither extends nor narrows
[THEORY-340](../theory.d/THEORY-340.md).

**On [THEORY-345](../theory.d/THEORY-345.md).** No bearing. That theory concerns choosing among indexes
for a known workload; this paper builds one structure for an unknown query
with worst-case guarantees, and its parameters (k, l) are set by n and ε,
not by a workload.

**On [CLAIM-309](../claims.d/CLAIM-309.md).** No bearing beyond an analogy the record should not lean
on: the cost here is governed by the ratio of far to near distance (1+ε),
a separation, and the paper's motivation is that similarity metrics are
heuristic, so "it seems like an overkill to insist on the absolute nearest
neighbor". That is an argument about tolerance, not about goodness against
discriminability.

## Limitations

- Upper bounds only. Whether ρ = 1/(1+ε) is best possible for Hamming is
  not addressed (later work cited in [LIT-1120](../literature.d/LIT-1120.md) says 1/c is optimal for
  ℓ_1 LSH, and 1/c² for ℓ_2 is achievable).
- The ℓ_p results for p in [1, 2] pass through embeddings, which for ℓ_1
  need bounded integer coordinates and blow up dimension.
- Several proofs are sketches (Lemmas 2–4, the PLEB storage bound, Corollary
  4), and the STOC and 1999 versions disagree on the exponent and on the
  range of ε for Proposition 1 and Corollary 3.
- Proposition 3's exponent grows with 1/ε; Proposition 2 is exponential in d.
- No experiments in the paper; the practical claims rest on a cited
  manuscript.
