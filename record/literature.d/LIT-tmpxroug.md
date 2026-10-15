---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' arXiv full version (arXiv:1608.03580v2,
  21 May 2017, 62 pp.), which merges the two preprints behind the SODA 2017 extended
  abstract; the SODA text itself was not seen, and the quantum-information steps
  of the two-probe proof were followed, not checked. Worth reading as the exact
  time–space curve for approximate near-neighbour search: for every c > 1, space
  n^{1+ρu+o(1)} and query time n^{ρq+o(1)} whenever c²√ρq + (c²−1)√ρu ≥ √(2c²−1)
  in Euclidean space (c√ρq + (c−1)√ρu ≥ √(2c−1) in Hamming and ℓ_1), on worst-case
  data, and optimal for list-of-points (hashing-based) structures on random instances,
  with unconditional cell-probe matches only for one or two probes at the n^{o(1)}-query
  end (n^{(c/(c−1))²−o(1)} words). For [QUESTION-114](../questions.d/QUESTION-114.md) it prices organizing against
  per-query cost exactly within the hashing model, as replication of each point
  into n^{ρu} lists against n^{ρq} lists scanned, and its closest-pair remark makes
  the best point depend on the number of queries; it says nothing about workloads,
  query mixes, build cost beyond space, exact nearest neighbours or structured data,
  and data-dependent schemes are covered only by conjecture. For [CLAIM-310](../claims.d/CLAIM-310.md) it shows
  overlapping bins are needed for fast similarity queries; for [THEORY-340](../theory.d/THEORY-340.md) it gives
  the similarity analogue of Yao's lookup floor in the unrestricted cell-probe model
  at one and two probes; no bearing on [THEORY-345](../theory.d/THEORY-345.md) or [CLAIM-309](../claims.d/CLAIM-309.md).
title: Optimal Hashing-based Time-Space Trade-offs for Approximate Near Neighbors
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: SODA 2017. arXiv v1 submitted
    11 August 2016. Not held in the Anthology of the SOTA: a grep of its record/
    (clone of 2026-10-15, commit d1573d2) for the title and authors found nothing.
    Read the same day (NOTE-tmptdi3z).
tags:
- databases
- information-retrieval
- mathematics
date: '2026-10-15'
published: '2016-08-11'
arxiv: '1608.03580'
first_author: Andoni
keywords: []
implementations: []
summary: >-
  Andoni et al. (2017), SODA 2017. For c-approximate near-neighbour search (find
  a point within cr when one lies within r) over n points in Euclidean space, the
  paper gives a data structure for every pair of exponents with c²√ρq + (c²−1)√ρu
  ≥ √(2c²−1), using space n^{1+ρu+o(1)} + O(dn) and query time n^{ρq+o(1)} + dn^{o(1)},
  on worst-case data (for Hamming and ℓ_1, c√ρq + (c−1)√ρu ≥ √(2c−1)). It proves
  the curve cannot be beaten by list-of-points structures, the model of all known
  data-independent hashing schemes, on random instances, and unconditionally in
  the cell-probe model only at one end (query n^{o(1)}) for one or two probes. So
  the exact trade between space spent organizing and per-query time is known within
  the hashing model; outside that model, for more than two probes, it is not, and
  data-dependent schemes are covered only by conjecture.
---

# LIT-tmpxroug: Optimal Hashing-based Time-Space Trade-offs for Approximate Near Neighbors

Andoni, A., Laarhoven, T., Razenshteyn, I. and Waingarten, E. (2017). Optimal hashing-based time-space trade-offs for approximate near neighbors. In *Proc. SODA 2017*, pp. 47–66. DOI 10.1137/1.9781611974782.4

## Key takeaways

Read in full ([NOTE-tmptdi3z](../notes.d/NOTE-tmptdi3z.md)). For c-approximate near-neighbour search (find a point within cr when one lies within r) over n points in Euclidean space, the paper gives a data structure for every pair of exponents with c²√ρq + (c²−1)√ρu ≥ √(2c²−1), using space n^{1+ρu+o(1)} + O(dn) and query time n^{ρq+o(1)} + dn^{o(1)}, on worst-case data (for Hamming and ℓ_1, c√ρq + (c−1)√ρu ≥ √(2c−1)). It proves the curve cannot be beaten by list-of-points structures, the model of all known data-independent hashing schemes, on random instances, and unconditionally in the cell-probe model only at one end (query n^{o(1)}) for one or two probes. So the exact trade between space spent organizing and per-query time is known within the hashing model; outside that model, for more than two probes, it is not, and data-dependent schemes are covered only by conjecture.

## Why this is here

[QUESTION-114](../questions.d/QUESTION-114.md) and [THEORY-340](../theory.d/THEORY-340.md) (Yao 1981): the exact trade-off curve between space spent organizing and query time for hashing-based approximate similarity search. Its lower bounds hold on random instances in the list-of-points model, and unconditionally only for one or two probes.
