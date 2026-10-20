---
number: 368
status: Active
formerly:
- THEORY-tmpc25xn
title: "On two-dimensional point sets constructed for the purpose, the authors' code for fast-preprocessing DiskANN, HNSW and NSG, at parameters from the original papers, in most cases found none or few of a query's five nearest neighbours until the search queue held about 10% of the points, for n from 10⁵ to 2·10⁶, and at that queue length ten graph indexes averaged recall@5 between 0.0 and 0.42; this is shown by experiment on one query per instance, and no theorem bounds these algorithms"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision
    for THEORY-368 (batch 053, ADR-047 v3): one study read in full,
    rechecked against the arXiv text. The "until about 10%" clause is now
    held to DiskANN, HNSW and NSG, the only indexes measured below that
    queue length. Of the other seven, three were run from a survey's
    reimplementations, not their authors' code. The promote_when asked for
    an independent replication, which moves to QUESTION-230.
tags:
- databases
- information-retrieval
date: '2026-10-15'
source:
- LIT-1112
summary: >-
  Indyk and Xu (2023), [LIT-1112](../literature.d/LIT-1112.md), read in [NOTE-910](../notes.d/NOTE-910.md). The instances are
  grids of points in the plane in which a large cluster, reached first
  from the start vertex, lies closer to the query than the only points
  linked to its nearest neighbour. At queue length 0.1n, average recall@5
  ranged from 0.0 (DiskANN) to 0.42 (KGraph). The paper calls the query
  time linear and says so "empirically"; the only argument beyond the
  experiment is an informal Ω(n/R) for DiskANN's fast build. It does not
  show that these indexes fail on natural data or natural queries.
---

# THEORY-368: On two-dimensional point sets constructed for the purpose, the authors' code for fast-preprocessing DiskANN, HNSW and NSG, at parameters from the original papers, in most cases found none or few of a query's five nearest neighbours until the search queue held about 10% of the points, for n from 10⁵ to 2·10⁶, and at that queue length ten graph indexes averaged recall@5 between 0.0 and 0.42; this is shown by experiment on one query per instance, and no theorem bounds these algorithms

## Source

Indyk and Xu (2023), [LIT-1112](../literature.d/LIT-1112.md), NeurIPS 2023 (arXiv 2310.19126v1),
read in full in [NOTE-910](../notes.d/NOTE-910.md): Section 4, Table 1 and Appendix C. Figures
were read from their captions and the text.

## What was actually shown

**The instances.** In the plane, three square grids M (0.8n points,
containing the start vertex), P and P′ (0.1n each), a query q, its
nearest neighbour a and four points near a. Construction leaves edges to
a only from P′ (and, for DiskANN, from P's random initial edges), while
every point of P is closer to q than the way into P′, so best-first
search exhausts P first. For NSG and HNSW, chains of 4,400 points (0.44%)
connect the grids so that k-NN graphs are connected. A six-dimensional
variant defeats KD-tree seeding (SPTAG-KDT, EFANNA). The point sets have
constant doubling dimension.

**The measurements.** For 20 sizes from 10⁵ to 2·10⁶ and queue lengths
L from 1% to 50% of n, recall@5 and average approximation ratio, over 5
or 10 runs with fresh random seeds. Fast-preprocessing DiskANN: "the
query procedure can take at least 0.1n steps on instances of size n
before it encounters any of the 5 nearest neighbors of the query." NSG
and HNSW: "for most values of n, both NSG and HNSW algorithms cannot
achieve good Recall@5 unless scanning at least 10% of the vertex set."
Table 1, L = 0.1n: DiskANN 0.0, NSG 0.27, HNSW 0.1, NGT 0.05, SSG 0.16,
KGraph 0.42, DPG 0.37, NSW 0.02, SPTAG-KDT 0.02, EFANNA 0.12. On the same
DiskANN instance, the slow-preprocessing build ([THEORY-384](THEORY-384.md)) found the
exact neighbour in two steps, measured up to n = 10⁵.

**What could have come out otherwise.** The builds could have placed
edges from the near cluster to the true neighbour, as the slow build
does, and recall could have risen at small L.

## What this does not say

- **That these algorithms take linear time in the worst case, as a
  theorem.** No lower bound is proved for HNSW, NSG or fast DiskANN. The
  result is a measurement on particular instances, implementations and
  parameters, with one query each.
- **That they fail on natural data.** The authors say their results "do
  not contradict the empirical evaluations given in the original papers",
  and list replication on real data with adversarially chosen queries as
  open.
- **That the failure needs high dimension.** It does not: the instances
  are two-dimensional. Low intrinsic dimension does not protect these
  builds.
- **That 10% is a property of the algorithms.** It is set by the
  instance: P holds 0.1n points. A larger trapping cluster would demand
  a longer queue.

## Connections

- [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions): with the points and the
  metric fixed, which graph is built over them decides between a
  two-step search and a scan of a tenth of the collection.
- [THEORY-384](THEORY-384.md): the guaranteed build these heuristics approximate, and
  the property (α-shortcut reachability) these instances are built to
  break.
- [THEORY-370](THEORY-370.md): Kleinberg's r = 0 network has short paths no local
  searcher finds quickly; here the right point is reachable, but the
  links lead search through a decoy first.

## Note of 2026-10-20: what the paper measured, rechecked

Rechecked against arXiv 2310.19126v1 for the promotion audit (batch 053,
[ADR-047](../decisions.d/ADR-047.md) v3).

- **Below L = 0.1n, only three builds.** The paper runs DiskANN with fast
  preprocessing (R = 70, L = 125, α = 2), HNSW (efConstruction = 200, M = 64)
  and NSG (K = 400, L = 400, iter = 12, S = 15, R = 100) from their authors'
  code over queue lengths from 1% to 50% of n. Its words: DiskANN "in most
  cases ... cannot achieve non-zero Recall@5 unless scanning at least 10% of
  the vertex set"; NSG and HNSW "for most values of n ... cannot achieve good
  Recall@5 unless scanning at least 10%".
- **At L = 0.1n, ten builds.** Table 1, averaged over n and 5 or 10 runs:
  DiskANN 0.0, NSG 0.27, HNSW 0.1, NGT 0.05, SSG 0.16, KGraph 0.42, DPG 0.37,
  NSW 0.02, SPTAG-KDT 0.02, EFANNA 0.12. KGraph, DPG and NSW were run from
  the survey's reimplementations, not their authors' code.

The title is narrowed to these. Whether an independent run reproduces them,
and whether the trap appears on natural data, is
[QUESTION-230](../questions.d/QUESTION-230.md).
