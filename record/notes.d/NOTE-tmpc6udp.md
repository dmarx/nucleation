---
status: Read
paper: LIT-tmp7a48f
title: Panigrahy, Talwar & Wieder — Lower bounds on near neighbor search via metric
  expansion
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' arXiv preprint, arXiv:1005.0418v1
    (3 May 2010, the only version), https://arxiv.org/pdf/1005.0418 (290,307 bytes,
    sha256 feea2778…, 29 pages), posted by the authors under Microsoft Research
    affiliations. It is the preprint of the FOCS 2010 paper; the IEEE text (DOI
    10.1109/FOCS.2010.82, pp. 805–814) was not seen, and Unpaywall lists no open
    copy of it, so changes made for the proceedings are unknown. Text extracted
    with pdftotext, which scatters exponents and fractions; Theorems 1.4, 1.5 and
    1.8, Conjectures 1.6 and 1.7, Table 1 and the hypercube calculations of Section
    4.2 were checked against page images (pp. 4, 5, 22 and 25). Read: all six sections,
    every definition, lemma, theorem and proof, and the references. The Chernoff
    and union-bound steps of the randomized proofs (Sections 3.4–3.5) were followed,
    not re-derived. Every quotation below was checked against the extracted text
    by script, whitespace normalised.
date: '2026-10-15'
summary: >-
  Cell-probe lower bounds for near-neighbour search follow from the expansion of
  the graph joining points within distance r: a deterministic t-probe structure
  with m cells of w bits must have (mwt/n)^t at least the vertex expansion, and
  a randomized one must have m^t w/n at least the robust expansion at measure 1/m^t,
  on random data sets with weakly overlapping neighbourhoods. For the hypercube
  this recovers known bounds and gives, for example, space n^{1+Ω(1/(ct))} for approximation
  c and n^{Ω(1/(tε²))} for 1 + ε; for symmetric (Cayley) graphs a one-probe structure
  matches the bound, and for dynamic low-contention structures the update time must
  be at least the robust expansion over poly(t). The bounds are average case, for
  approximate decision search, and weak in t: they fall off exponentially in the
  number of probes, so they are tight only for a constant number of probes and say
  little about structures that probe n^ρ cells.
---

# NOTE-tmpc6udp: Panigrahy, Talwar & Wieder — Lower bounds on near neighbor search via metric expansion

## Contribution

Lower bounds for near-neighbour data structures had been proved metric by
metric, mostly by communication complexity. This paper gives one recipe:
define the graph on the metric space joining points within distance r,
compute how much that graph expands, and read off a time–space lower bound.
Vertex expansion gives deterministic bounds, a new "robust expansion" gives
randomized ones, and the same quantity gives a matching one-probe upper
bound for highly symmetric spaces. The paper states the aim: "Our work
reduces the problem of proving cell probe lower bounds of near neighbor
search to computing the appropriate expansion parameter."

## Key insight

A query must find its neighbour by reading a few cells. If the near
neighbourhoods of the space expand, the set of queries that read any one
cell is small, so the near neighbours of any one data point are scattered
over many cells (shattered). Then a small random sample of cells already
lets one decode many data points' hidden bits, so if the structure were
small it would compress n random bits below n, which is impossible. The
more the space expands, the more cells a fast structure must have.

## Assumptions

- **Problem.** Graphical neighbour search (GNS), which the decision version
  of (c, r)-approximate near neighbour reduces to (Theorems 4.1, 4.2): data
  points carry hidden bits, and a query with a unique neighbour among the
  data must return that neighbour's bit. "Clearly a lower bound for these
  problems holds also for nearest neighbor search."
- **Cell-probe model.** t tables of m cells of w bits; the i-th probe's
  address may depend on the query and on the contents already read
  (adaptive); computation is free and cell contents may encode anything.
  Lookup functions are fixed independently of the data.
- **Average case.** Data points are drawn independently from a distribution
  µ; deterministic bounds need strong independence (two random points'
  neighbourhoods meet with probability at most 1/(100n²)); randomized bounds
  need weak independence (a random neighbour of one data point is a
  neighbour of another with probability at most γ/n) and t ≤ n^{1/4}
  (Theorem 3.10). "We stress that these bounds hold for the average case
  where the n data-set points are sampled randomly from a distribution
  over" the space.
- **Expansion.** Vertex expansion Φv(δ): least ratio µ(N(A))/ν(A) over query
  sets A of measure at most δ. Robust expansion Φr(δ, γ): the least measure
  ratio of a set B that captures a γ fraction of the edges from A
  (Definitions 1.1, 1.2, 3.1).

## Key results

- **Theorem 1.4 (deterministic).** If µ is strongly independent and Φv is
  the vertex expansion, any deterministic GNS algorithm satisfies
  (mwt/n)^t ≥ Φv (1) and m^t t w/n ≥ Φv(1/m^t) (2). Proofs: cell sampling
  (Theorem 2.1) and path sampling (Theorem 2.2); (2) also holds for
  communication protocols.
- **Theorem 1.5 (randomized).** For a weakly independent instance and
  success probability at least 1/2: (mwt⁴/n)^{2t} ≥ Φr(1/m, γ/t) (3) and
  m^t w/n ≥ Φr(1/m^t, γ/t) (4), γ an absolute constant.
- **Hypercube applications (Section 4, Table 1).** Deterministic, with
  approximation 1/ε: t ≥ dε²·log a/log(mwd/n) by Harper's theorem, slightly
  improving t ≥ dε³/log(mwd/n) (the table attributes a dε² bound to earlier
  work; the text says dε³). Randomized, approximation 1 + Θ(ε) (r = (1/2−ε)d):
  space n^{Ω(1/(tε²))}, recovering Andoni–Indyk–Pătraşcu (the exponent's
  constant differs between p. 4, (n/w)^{1/(4tε²)}, and p. 25,
  (n/(wt⁵))^{4/(tε²)}). Randomized, approximation about 1/ε (r = εd/2):
  m ≥ (n/w)^{1+Ω(ε/t)}, that is space n^{1+Ω(1/(ct))} for approximation c,
  strengthening the authors' 2008 search-version bound to the decision
  version. ℓ∞, approximation O(log_ρ log d): m ≥ (n/(wt))^{ρ/t},
  deterministic, from Andoni–Croitoru–Pătraşcu's expansion bound.
- **Conjecture 1.6.** Any randomized t-probe structure on a weakly
  independent instance satisfies (mw/n)·t ≥ Φr(1/m, 1/(2t))^{Ω(1)}, which
  would make the dependence on t polynomial. Not proved.
- **Theorem 5.1 (upper bound).** On an undirected Cayley graph with weak
  independence under the uniform distribution, with m such that
  m = nΦr(1/m, γ), γ ≥ 3/4, a one-probe structure of m words of log|G| bits
  succeeds with constant probability on random data and a random neighbour
  query, matching (4) at t = 1. "We stress that the upper bound is in the
  cell probe model, which allows us to ignore the (practically very
  important) issue of actually computing the LSH efficiently."
- **Theorem 1.8 (dynamic, low contention).** If no cell is read by queries
  of total measure more than τ, any dynamic t-probe GNS structure has update
  time Ω(Φr(τ, 1/(4t²))/32t⁴). The paper notes LSH and its own upper bound
  are dynamic and low contention, and asserts that "for a wide range of
  parameters Locality Sensitive Hashing is optimal for the class of the low
  contention dynamic data structures over the hypercube"; the hypercube
  calculation behind that sentence is not written out.
- **The weakness in t.** "In our results, as in all previous results, the
  dependence on t is weak; that is, the bound drops exponentially in t."

## Bearing on the record

**On [THEORY-340](../theory.d/THEORY-340.md): the similarity analogue of Yao's lookup floor, in the same
model, with arbitrary encoding allowed.** [THEORY-340](../theory.d/THEORY-340.md) found sorted order
optimal for membership only when cells hold keys and pointers, and beaten
by two probes once one cell may hold an encoded value. Here cells may hold
anything, and still a near-neighbour structure answering in a constant
number of probes needs space polynomially larger than the data, with an
exponent set by how much the space expands and by the approximation. So for
similarity, unlike membership, a lookup floor survives arbitrary encoding.
The differences matter: these are approximate, average-case bounds on random
data, and Yao's are exact and worst case.

**On [QUESTION-114](../questions.d/QUESTION-114.md): a floor under the per-query side, priced in space, and
a lower bound on upkeep, in a restricted class.**

- Equations (3) and (4) say what organizing must cost if queries are to be
  answered in t probes: m^t w/n at least the robust expansion. Fast queries
  require large space; there is no structure that is both small and fast
  for expanding spaces.
- Theorem 1.8 bounds update time for low-contention dynamic structures by
  the robust expansion, and Conjecture 1.7 would trade update time against
  query probes (tU·t ≥ Φr(1/(n·tU), 1/(2t))^{Ω(1)}). That is upkeep against
  per-query cost. The database readings gathered under [QUESTION-114](../questions.d/QUESTION-114.md) price
  upkeep as a cost inside a model; this is a lower bound on it, and the
  ANN papers read with it ([LIT-tmpa1ovj](../literature.d/LIT-tmpa1ovj.md), [LIT-tmpxroug](../literature.d/LIT-tmpxroug.md)) give only upper
  bounds on update time. Only the restricted, low-contention form is
  proved.
- What it does not say. The bounds are exponentially weak in t, so they
  are tight only for constant t and leave open the regime of LSH's n^ρ
  probes ([LIT-tmpxroug](../literature.d/LIT-tmpxroug.md) closes it for hashing-based structures, not here).
  There is no query workload, no amortization over a query sequence, and no
  build time; data are random, so structure in a real collection could make
  search cheaper than the bound.

**On [CLAIM-310](../claims.d/CLAIM-310.md).** The bound is driven by the expansion of the
neighbourhood graph. When near neighbourhoods expand, as in high-dimensional
space, no assignment of points to cells keeps a query's neighbours together.
Exact lookup on a discrete attribute has neighbourhoods of a single value,
with no expansion, so the bound is empty there, which is consistent with
bins working for bricks sorted by attribute. That reading is the record's,
not the paper's. Nothing here concerns query mixes.

**On [THEORY-345](../theory.d/THEORY-345.md) and [CLAIM-309](../claims.d/CLAIM-309.md).** No bearing.

## Limitations

- Average-case lower bounds on random data sets under independence
  conditions; nothing about structured data.
- Exponentially weak in t; tight only for constant t (Theorem 5.1 at t = 1).
- Decision version of approximate near neighbour.
- Randomized bounds need t ≤ n^{1/4}; constants are loose and differ between
  the introduction and Section 4.
- The dynamic bound holds only for low-contention structures, and the
  conjectures that would remove the restriction are open.
- Preprint, not the FOCS text.
