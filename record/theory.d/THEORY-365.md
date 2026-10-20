---
number: 365
status: Active
formerly:
- THEORY-tmp4zwbu
title: "In one study of a stack of proximity graphs on nested random subsets of the data, each element's top layer drawn geometrically, greedy search on uniform random data in 8 dimensions needed a number of distance computations that grew no worse than logarithmically with the number of items and stayed below a single-layer navigable graph's at every size tested, and in 4 dimensions the beam width needed for a fixed recall saturated; the logarithmic bound is derived only for exact Delaunay graphs of bounded degree, which the index does not build, and on 200 million SIFT vectors the measured growth departs from it"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-365 (batch 039, ADR-047 v3). The title keeps what LIT-1098's
    text reports, checked against the extracted text of arXiv v4. Three
    phrasings that went past it are dropped. Single-layer graphs'
    polylogarithmic growth is the paper's account of earlier work, and
    only "below NSW at every size" was measured. At d = 4 the measured
    quantity is the beam width, not the cost. "Makes" claimed an
    isolated effect. The promote_when moves unchanged to
    QUESTION-187.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 072, ADR-047 v4) filed THEORY-tmp880z4,
    Proposed, to carry what the narrowing dropped. This entry's status,
    title and claims are unchanged; a dated note says what moved.
tags:
- databases
- information-retrieval
- network-science
date: '2026-10-15'
source:
- LIT-1098
answers:
- QUESTION-114
summary: >-
  Malkov and Yashunin (2020), [LIT-1098](../literature.d/LIT-1098.md), read in [NOTE-916](../notes.d/NOTE-916.md) from arXiv
  v4. They build an index like a skip list, with proximity graphs in place
  of linked lists, and argue that search costs a constant per layer over
  O(log N) layers. That holds if each layer is an exact Delaunay graph of
  bounded mean degree. HNSW does not build such graphs, and Delaunay
  degree grows exponentially with dimension. For the graphs it does build,
  cost no worse than logarithmic is measured on uniform random data at
  d = 8, a saturating beam width at d = 4, and at d = 128 (200M SIFT) the
  growth departs from a logarithm. A proof for the graphs HNSW builds is
  QUESTION-187. The
  paper gives no worst-case bound and no recall guarantee. Construction is
  argued to cost about N searches.
extended_by:
- THEORY-tmp880z4
---
<!-- inactive-ok-file: THEORY-tmp880z4 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->

# THEORY-365: In one study of a stack of proximity graphs on nested random subsets of the data, each element's top layer drawn geometrically, greedy search on uniform random data in 8 dimensions needed a number of distance computations that grew no worse than logarithmically with the number of items and stayed below a single-layer navigable graph's at every size tested, and in 4 dimensions the beam width needed for a fixed recall saturated; the logarithmic bound is derived only for exact Delaunay graphs of bounded degree, which the index does not build, and on 200 million SIFT vectors the measured growth departs from it

## Source

Malkov and Yashunin, IEEE TPAMI 42(4), 2020, [LIT-1098](../literature.d/LIT-1098.md). Read in full
in [NOTE-916](../notes.d/NOTE-916.md) from the authors' arXiv version 4 (2018), whose abstract
matches the published one. Version 1 (2016) was compared for its claims.

## What was actually shown

**The construction.** Each element gets a level l = ⌊−ln(u)·mL⌋, with u
uniform. That is geometric, with P(l ≥ 1) = 1/M at the default
mL = 1/ln M. The paper says this "corresponds to the skip list parameter
p=1/M". The element is linked into layers l down to 0, each layer a
proximity graph with at most Mmax links per element, and Mmax0 = 2M on
layer 0. Search descends greedily from the single top entry point and runs
a beam of width ef on layer 0. Insertion is the same search, followed by
neighbour selection.

**The derivation, and its condition.** Levels are independent of
position, so on each layer the expected number of greedy steps before
reaching an element of the layer above is bounded. If the mean degree is
also bounded, the work per layer is constant, and over O(log N) layers
search is O(log N). The paper states the condition outright: the analysis
holds "under the assumption that we build exact Delaunay graphs instead
of the approximate ones", with mean Delaunay degree capped, which "can be
in principle violated in exotic spaces". As printed, the per-step
probability is exp(−mL) where the level rule gives exp(−1/mL). That slip
changes the constant, not the form.

**Measurements.** For d = 4 uniform data, the beam width needed for
recall 0.9 to 0.999 levels off as N grows over about eight orders of
magnitude. On d = 8 uniform data at recall 0.95, distance computations
grow no faster than log N up to about 10⁸ items, while NSW's grow faster.
On subsets of 1B SIFT up to 200M (d = 128), "the scaling deviates from
the pure logarithm". For high dimensions the paper says that confirming
the bound "requires having extremely large datasets" and that "Further
analitical evidence is required".

**Build cost.** One insertion is about one search, since the expected
number of layers per element is constant. Construction is therefore
argued to be O(N log N) "at least for relatively low dimensional
datasets". Measured: 10M SIFT in about 3 minutes on 40 cores, and 200M
SIFT in 42 minutes to 5.6 hours depending on efConstruction. Larger
efConstruction buys little query speed for much longer builds.

## What this does not say

- **Not that single-layer graphs were measured to grow
  polylogarithmically.** The paper measures HNSW below NSW at every
  size. NSW's polylogarithmic scaling is its account of the authors'
  earlier work, which is not read here.
- **No worst-case bound.** The analysis is an expected-case sketch under
  an assumption the index does not meet. Nothing bounds the cost on
  adversarial data, and nothing bounds recall: the search is
  approximate, and the beam width needed for a given recall is found by
  measurement. Indyk and Xu ([LIT-1112](../literature.d/LIT-1112.md)) take up worst cases.
- **Not logarithmic in high dimension.** The one large high-dimensional
  measurement departs from a logarithm, and the authors attribute this to
  dimension. The logarithmic result here is a low-dimensional one.
- **Not Kleinberg's theorem applied.** The paper cites Kleinberg
  ([LIT-1103](../literature.d/LIT-1103.md)) as background and as a contrast. His construction needs
  the data distribution in advance and routes polylogarithmically "at
  best". The logarithmic claim rests on the skip-list analogy, not on Kleinberg's
  result.
- **No upkeep under deletion.** v4 has no deletion and lists it as future
  work. v1 claimed deletion and argued its cost without an algorithm. The
  published line dropped the claim.
- **Not for any query mix.** Every test drew its queries from the data.
  How costs behave for queries distributed unlike the data is not tested.

## Connections

- [QUESTION-114](../questions.d/QUESTION-114.md): one structure, with a measured build-against-query trade,
  build cost as a real term, and insertion upkeep about one search. There
  is no break-even analysis and no deletion. It adds a built-cost term
  that Finkelstein et al. ([LIT-1084](../literature.d/LIT-1084.md)) and Harinarayan et al. ([LIT-1094](../literature.d/LIT-1094.md))
  lack, and nothing on staleness.
- [CLAIM-310](../claims.d/CLAIM-310.md): the √N optimum in part 1 is the cost of a single level of
  bins. Nested levels, as in a skip list, are how this index reaches
  log N. That reading is the record's, not the paper's.
- [THEORY-385](THEORY-385.md) is the paper's other finding, on neighbour selection and
  clustered data.

## Note of 2026-10-19: what the text reports

Checked against pdftotext output of arXiv v4 for the promotion audit. The
three measured clauses of the title rest on these sentences.

- §5.1, d = 8: "Hierarchical NSW has a complexity scaling for this
  setting not worse than logarithmic and outperforms NSW at any dataset
  size".
- §4.2, d = 4: "the dependence of the required ef parameter … to get a
  fixed recall saturates with the rise of the dataset size".
- §5.4, SIFT: "the scaling deviates from the pure logarithm".

The range, 10² to about 10⁸ items, and the shapes of the curves are read
from Figs. 11, 12b and 15, not from the text. So the title says "no worse
than logarithmically", not "logarithmically".

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 072) filed [THEORY-tmp880z4](THEORY-tmp880z4.md)
as Proposed, extending this entry. It carries the claim this entry's
title gave up when batch 039 narrowed it: that the layered hierarchy is what makes greedy search logarithmic, where single-layer navigable graphs grow polylogarithmically, as Malkov and Yashunin argue, stated for data of low intrinsic dimension because the paper's own 200-million-vector SIFT measurement departs from a logarithm.
This entry is its evidence and is not changed by the filing.
