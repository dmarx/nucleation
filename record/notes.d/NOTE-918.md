---
number: 918
status: Read
formerly:
- NOTE-tmptdi3z
paper: LIT-1120
title: Andoni, Laarhoven, Razenshteyn & Waingarten — Optimal hashing-based time–space
  trade-offs for approximate near neighbors
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read on 2026-10-15 from the authors' arXiv preprint, arXiv:1608.03580v2 (submitted
    11 August 2016, this version 21 May 2017, title page dated May 23, 2017), https://arxiv.org/pdf/1608.03580
    (1,175,732 bytes, sha256 e8a3a01a…, 62 pages). Its first footnote says it merges
    two earlier preprints (Laarhoven 2015 and Andoni, Laarhoven, Razenshteyn and
    Waingarten 2016) and that "An extended abstract of this paper appeared in the
    proceedings" of SODA 2017; so this is the full version, not the 20-page SODA
    text, which was not seen. Unpaywall lists the arXiv copy as the open location
    for DOI 10.1137/1.9781611974782.4 (green, submitted version) and also a TU/e
    repository record; nothing else was tried. Text extracted with pdftotext; the
    extraction scatters square roots, exponents and subscripts, so the statements
    of Theorems 1.1, 1.3, 1.4, 1.6 and 8.1 were checked against page images (pp.
    3, 8 and 42 of the PDF's numbering). Read: Sections 1, 2 and 3 in full; Section
    4 (the data-dependent construction) in full for the description, the parameter
    settings and the statements of Lemmas 4.2, 4.8–4.13, with the potential-function
    calculations of Claims 4.3–4.7 followed but not re-derived; Sections 5, 6 and
    7 in full; Section 8 (two-probe lower bound) in full for its structure and lemma
    statements, with the quantum-information steps (Section 8.6, adapted from Kerenidis
    and de Wolf) followed, not checked; the references skimmed. Every quotation
    below was checked against the extracted text by script, whitespace normalised;
    the one quotation of the record was checked against CLAIM-310.
date: '2026-10-15'
summary: >-
  For c-approximate near-neighbour search (find a point within cr when one lies
  within r) over n points in Euclidean space, the paper gives a data structure for
  every pair of exponents with c²√ρq + (c²−1)√ρu ≥ √(2c²−1), using space n^{1+ρu+o(1)}
  + O(dn) and query time n^{ρq+o(1)} + dn^{o(1)}, on worst-case data (for Hamming
  and ℓ_1, c√ρq + (c−1)√ρu ≥ √(2c−1)). It proves the curve cannot be beaten by list-of-points
  structures, the model of all known data-independent hashing schemes, on random
  instances, and unconditionally in the cell-probe model only at one end (query
  n^{o(1)}) for one or two probes. So the exact trade between space spent organizing
  and per-query time is known within the hashing model; outside that model, for
  more than two probes, it is not, and data-dependent schemes are covered only by
  conjecture.
---

# NOTE-918: Andoni, Laarhoven, Razenshteyn & Waingarten — Optimal hashing-based time–space trade-offs for approximate near neighbors

## Contribution

Locality-sensitive hashing (LSH, from [LIT-1106](../literature.d/LIT-1106.md)) gives one point on a
curve: space n^{1+ρ} and query time n^ρ with the same exponent. Earlier work
had other isolated points: polynomial space with polylog queries
(Indyk–Motwani, Kushilevitz–Ostrovsky–Rabani), and near-linear space with
sublinear queries only for large enough c. This paper gives the whole curve
of exponents (ρq for query time, ρu for space) for every c > 1, as one
family of structures, and shows the curve is optimal for hashing-based
structures, with unconditional cell-probe bounds at the fast-query end.

## Key insight

Store each point under every spherical cap it falls in, and send each query
into every cap it falls in, but let the two thresholds differ. Points are
filed under caps of threshold ηu, queries look in caps of threshold ηq. A
low ηu files each point in many caps, costing space, and lets the query use a
high ηq and look in few, which saves time; ηu above ηq does the reverse.
The equal-threshold case is LSH. Worst-case data are first broken into dense
clusters, which are re-centred and recursed on, until what remains looks
random, where the cap scheme is analysed. The lower bound rests on the
robust expansion of the hypercube: in a random instance a query's true
neighbour is a noisy copy, and no family of lists can catch noisy copies
with few short lists unless points are replicated into many lists.

## Assumptions

- **Approximate near neighbour, not nearest.** (c, r)-ANN with c > 1: given
  the promise that some point is within r of the query, return any point
  within cr. Exact search and the nearest (not near) version are not
  addressed here; the paper notes that a randomized lower bound for the
  nearest version is a different problem.
- **Worst-case data, randomized structure.** The upper bounds hold for any
  data set; success probability is at least 0.9 per query (Lemma 4.9);
  space and query time are in expectation.
- **Dimension.** Upper bounds assume d is reduced to Θ(log n · log log n) by
  Johnson–Lindenstrauss; the lower bounds need d = ω(log n). The open
  problems say the constructions are optimal when d lies between ω(log n)
  and n^{o(1)}, and ask: "Do the same constructions give optimal algorithms
  in the d = Θ(log n) regime?"
- **Lower bounds are average case.** They use the random instance: n uniform
  points of {−1, 1}^d, and a query made by flipping each coordinate of a
  random data point with probability 1/(2c). A bound for random instances
  implies one for worst-case data.
- **The list-of-points model (Definition 1.5).** Fixed, possibly random,
  sets A_1, …, A_m of the space, independent of the data; list L_i = P ∩ A_i;
  a query q scans the lists in a set I(q). Space s = m + Σ|L_i|; query time
  |I(q)| + Σ_{i∈I(q)} |L_i|. The paper says it captures "all hashing-based
  frameworks we are aware of" except data-dependent schemes, including its
  own upper bound: "we conjecture that the natural extension of the
  list-of-point model to data-dependent setting would yield the same lower
  bound".
- **Cell-probe bounds** allow arbitrary computation and encoding but count
  probes: words of n^{o(1)} bits for one probe, o(log n) bits for two.
- **Preprocessing time.** Not counted separately from space; the paper notes
  that for dynamization "one needs to ensure that the preprocessing time is
  near-linear in the space used, which is the case for our data structure."

## Key results

- **Theorem 1.1 (Theorem 4.1), upper bound, Euclidean, worst case.** For
  every c > 1, r > 0, ρq ≥ 0, ρu ≥ 0 with
  c²√ρq + (c² − 1)√ρu ≥ √(2c² − 1), there is a data structure for (c, r)-ANN
  in ℝ^d with space n^{1+ρu+o(1)} + O(dn) and query time n^{ρq+o(1)} + dn^{o(1)}.
  Special points: ρu = 0 gives query time n^{(2c²−1)/c⁴+o(1)}, sublinear for
  every c > 1 (first such result); ρq = ρu gives n^{1/(2c²−1)}, the best
  data-dependent LSH; ρq = 0 gives space n^{c⁴/(c²−1)²+o(1)}, which for
  c = 1 + ε is about n^{1/(4ε²)}. For c = 2: space n^{1.77} with query
  n^{o(1)}; n^{1.14} with n^{0.14}; n^{1+o(1)} with n^{0.43}.
- **ℓ_p.** By a cited reduction, the same with c² replaced by c^p for
  1 ≤ p < 2; for ℓ_1, c√ρq + (c − 1)√ρu ≥ √(2c − 1).
- **Dynamic.** Insertions and deletions with logarithmic loss, update time
  dn^{ρu+o(1)}, by a standard dynamization of decomposable search problems.
- **Theorem 1.2 / Corollary 3.4 (data-independent, worst case).** The
  cap scheme alone gives the weaker curve (c² + 1)√ρq + (c² − 1)√ρu ≥ 2c on
  all of ℝ^d; on random instances it gives the optimal curve (Corollary
  3.5). Data dependence is what closes the gap for worst-case data.
- **Theorem 1.6 (Theorem 7.1), list-of-points lower bound.** Any
  list-of-points structure for (c, r)-ANN on random instances in Hamming
  space with d = ω(log n), space n^{1+ρu} and query time n^{ρq−o(1)}, success
  2/3, satisfies c√ρq + (c − 1)√ρu ≥ √(2c − 1). This matches the ℓ_1 upper
  bound, and through the cited reduction the Euclidean one. The paper calls
  it "conditional": "proving similar lower bounds unconditionally is far
  beyond the current reach of techniques."
- **Theorem 1.3, one cell probe (unconditional).** Any structure solving
  (c, r)-ANN on the Hamming random instance with probability 2/3, with cells
  of n^{o(1)} bits and one probe per query, needs n^{(c/(c−1))²−o(1)} words.
  This equals the upper bound's space at ρq = 0 (1 + ρu = c²/(c−1)² in
  Hamming). Corollary 6.8 gives n^{1+(2c²−1)/(c²−1)²−o(1)} cells for ℓ_2 on
  the sphere. Proof: Lemma 6.2 bounds the hypercube's robust expansion by
  hypercontractivity and Hölder; Panigrahy–Talwar–Wieder's Theorem 1.5
  ([LIT-1102](../literature.d/LIT-1102.md)) turns it into a space bound.
- **Theorem 1.4, two cell probes (unconditional).** The same bound,
  n^{(c/(c−1))²−o(1)} words, for the decision version with cells of o(log n)
  bits and two probes. "Informally speaking, Theorem 1.4 shows that the
  second cell probe cannot improve the space bound by more than a
  subpolynomial factor." Proof: a too-good two-probe structure would give a
  weak two-query locally decodable code, contradicting Kerenidis–de Wolf.
  The argument cannot go past word size 2^{Θ̃(√log n)}.
- **Offline use.** "ANN solutions with" the stated space and query time
  give a closest-pair algorithm in time n^{1+ρu} + n^{1+ρq} "(implying that
  the balanced, LSH regime is most relevant)".

## Bearing on the record

**On [QUESTION-114](../questions.d/QUESTION-114.md): for one problem, the exact curve of paying up front to
organize against per-query cost, tight in the model that covers hashing.**

- The curve is the price list. Each unit of space exponent bought lowers the
  query exponent along c²√ρq + (c² − 1)√ρu = √(2c² − 1). It is a straight
  line in √ρq and √ρu, so there are no free points: lowering query time to
  n^{o(1)} costs space n^{c⁴/(c²−1)²}, and holding space near-linear costs
  query time n^{(2c²−1)/c⁴}. Within list-of-points structures, and at the
  fast-query end for one or two probes in general, nothing does better.
- What is paid up front here is replication. Space n^{1+ρu} means each point
  is filed in about n^{ρu} lists. The trade is between how many places an
  item is filed and how many places a query looks. This is close to the
  question's bins: filing a brick under several attributes against
  searching several bins.
- The paper itself makes one amortization statement. Answering n queries
  costs n^{1+ρu} + n^{1+ρq}, so for n queries the balanced point is best.
  More generally, Q queries cost about n^{1+ρu} + Q·n^{ρq} (the record's
  arithmetic, not the paper's), so the best point on the curve moves toward
  more organization as the expected number of queries grows. That is
  [QUESTION-114](../questions.d/QUESTION-114.md)'s trade, paid once against saved each time, with both terms
  priced.
- What it does not say. The bounds are per query, for one query at a time
  over a fixed data set; there is no query distribution, no workload mix, no
  learning from queries (data-dependent means dependent on the data set,
  not on the queries), no build cost apart from space, and upkeep only as a
  dynamized update cost. It is about approximate near neighbours: nothing
  here prices exact nearest-neighbour search, and the lower bounds are for
  random data, so on structured data that a scheme can exploit the curve
  need not bind for that data. Its optimality is within list-of-points
  structures; beyond two probes, cell-probe lower bounds remain far weaker.

**On [THEORY-340](../theory.d/THEORY-340.md).** Yao's membership question has its similarity analogue
here, with a sharper answer. For membership, sorted order is optimal only
when cells hold nothing but keys and pointers, and arbitrary encoding beats
it. Here, at the one- and two-probe end, the bound holds in the cell-probe
model, which allows arbitrary encoding; so for approximate similarity the
cost of fast lookup is not an artefact of a restricted cell content. Both
treat building as free.

**On [THEORY-345](../theory.d/THEORY-345.md).** No direct bearing. [THEORY-345](../theory.d/THEORY-345.md) concerns choosing among
candidate indexes for a known workload, which is NP-hard in general. Here
there is one query type, no workload, and the structure is fixed by n, c and
the chosen exponents. The two are different questions about organizing.

**On [CLAIM-310](../claims.d/CLAIM-310.md).** It narrows "a fixed number of bins realizes one
partition" for similarity search. The lists A_i in the list-of-points model
need not be disjoint, so the lower bound is about overlapping bins, and it
says overlap (replication) is necessary for fast queries: at near-linear
space, which allows each point in only n^{o(1)} lists, query time is at
least n^{(2c−1)/c²−o(1)} in Hamming. That fits the claim's dependence on the
bin budget. It does not bear on its dependence on the query mix: the hard
queries are random, and the structure serves all queries alike. And bricks
with discrete attributes are not high-dimensional similarity search.

**On [CLAIM-309](../claims.d/CLAIM-309.md).** No bearing. The approximation factor c is a ratio of far
to near distance, a separation, not a measure of goodness.

## Limitations

- Optimality is conditional on the list-of-points model except at ρq = 0
  for one or two probes. Data-dependent schemes, including the paper's own
  upper bound, are outside the model; that they obey the same bound is a
  conjecture (supported for ρq = ρu by cited work).
- Lower bounds use random instances with d = ω(log n); the case
  d = Θ(log n) is open.
- The worst-case construction is, in the paper's words, a set of algorithms
  that "are, unfortunately, impractical"; o(1) terms in exponents are not
  quantified.
- Approximate near neighbour only; no exact search, no ranking of several
  neighbours, no query distribution.
