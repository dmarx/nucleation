---
status: Active
status_note: 'read 2026-10-16 (NOTE-tmpfnjjj) in full; worth reading as the paper that turns the Johnson–Lindenstrauss lower bound into a bit count, determining how many bits it takes to store every inner product of n points of the unit ball to additive ε, and so extending Larsen and Nelson''s dimension lower bound to every ε ≥ 2/√n with log(2 + ε²n)/ε² in place of log n/ε². Read it knowing that its dimension statements are for additive error on squared distances, the relative form being stated only for ε ≥ 1/n^0.49; that the step from bits to dimension is a short remark; that constants are unstated; and that its small-ε upper bound is bipartite, keeps only cross inner products and does not bound norms, so the one-set JL lemma at log(2 + ε²n)/ε² stays open. Filed as THEORY-tmpup7x5 and THEORY-tmpbh0v2.'
title: 'Optimal compression of approximate inner products and dimension reduction'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed at the owner's request as later work flagged by the reading of
    Larsen and Nelson (NOTE-tmp4mti8), whose §1.2 reports it. Citation checked against arXiv and Crossref on 2026-10-16.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone pulled 2026-10-16) for the authors' names and the identifiers found nothing. Published at FOCS 2017, pp. 639–650.
- version: 2
  date: '2026-10-16'
  note: >-
    Read in full (NOTE-tmpfnjjj) from the arXiv PDF, v4 of 2 April 2017,
    supplied by the owner: §§1–7, with the convex-geometry proofs of
    §§6.3–6.4 in outline. The citing-work takeaways are replaced with the
    reading, the summary is rewritten from it, the status moved from
    Deferred to Active, and Standing in the record names THEORY-tmpup7x5
    and THEORY-tmpbh0v2. The copy does not state the venue, so the FOCS
    details stand on the version 1 check.
tags:
- mathematics
- information-theory
date: '2026-10-16'
published: '2016-10-02'
arxiv: '1610.00239'
doi: '10.1109/FOCS.2017.65'
first_author: 'Alon'
keywords:
- 'dimension reduction'
- 'inner products'
- 'compression'
- 'Johnson-Lindenstrauss lemma'
- 'lower bound'
- 'sketching'
- 'Gaussian correlation inequality'
extends:
- LIT-tmp8s1wj
implementations: []
summary: >-
  Alon & Klartag (2017), FOCS 2017, [ARXIV-1610.00239](https://arxiv.org/abs/1610.00239). For n points of norm at most 1 in R^k and 1/n^0.49 ≤ ε ≤ 0.1, storing every inner product and squared distance to additive ε takes Θ(n log n/ε²) bits once k ≥ log n/ε², Θ(nk log(2 + log n/(ε²k))) for log n ≤ k ≤ log n/ε², and Θ(nk log(1/ε)) below, with an efficient per-point sketch. Comparing the counts across dimensions re-proves Larsen and Nelson's bound and extends it: for every ε ≥ 2/√n some n such points need Ω(min{k, log(2 + ε²n)/ε²}) dimensions under any map with additive error ε. A bipartite JL lemma keeps cross inner products in O(log(2 + ε²n)/ε²) dimensions, without bounding norms.
---

# LIT-tmp08fvg: Optimal compression of approximate inner products and dimension reduction

Noga Alon and Bo'az Klartag (2017), "Optimal compression of approximate inner products and dimension reduction", FOCS 2017: 639–650 — [ARXIV-1610.00239](https://arxiv.org/abs/1610.00239)

## Key takeaways

*From the reading, [NOTE-tmpfnjjj](../notes.d/NOTE-tmpfnjjj.md).*

- **Bits (Theorem 1.1).** For 1/n^0.49 ≤ ε ≤ 0.1, an additive ε-sketch of
  n points of the unit ball of R^k needs Θ(n log n/ε²) bits for
  k ≥ log n/ε², Θ(nk log(2 + log n/(ε²k))) for log n ≤ k ≤ log n/ε², and
  Θ(nk log(1/ε)) for k ≤ log n. Upper bound by a volume count of
  ε-separated Gram matrices; lower bound by n/2 random probes against n/2
  net points.
- **An efficient sketch (Theorem 4.1).** JL into 40 log n/ε² dimensions,
  then unbiased randomized rounding, O(1) bits per coordinate, with norms
  stored apart.
- **Dimension (Corollaries 2.1, 2.3).** For every ε ≥ 2/√n, some n points
  in R^k cannot be mapped into ℓ ≤ ck dimensions with additive error ε on
  squared distances unless ℓ = Ω(log(2 + ε²n)/ε²). For ε ≥ 1/n^0.49 this
  is Larsen and Nelson's bound, also stated for relative error.
- **Small ε (Theorem 2.2).** The count is Θ(nk log(2 + t/k)) for
  k ≤ t = log(2 + ε²n)/ε²; above t only Ω(nt) to O(n log n/ε²) is known.
  The union bound is replaced by the Gaussian correlation inequality.
- **Bipartite JL (Theorem 1.2).** Two families of n vectors of norm at
  most 1 have images in ⌊C log(2 + ε²n)/ε²⌋ dimensions with every
  ⟨x_i, y_j⟩ within ε, by a randomized polynomial algorithm. Norms are
  not bounded; bounding them is Conjecture 2.4, proved only for t of
  order n (Theorem 2.5).
- **Scope.** Additive error, worst-case sets, unstated constants; the
  relative-error sketch problem keeps a log gap.

## Standing in the record

Filed on 2026-10-16 as later work flagged by [NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md), and read the
same day in [NOTE-tmpfnjjj](../notes.d/NOTE-tmpfnjjj.md). The registration said the paper proves the
lower bound of Larsen and Nelson's Conjecture 1 "for all parameters". The
reading qualifies that. The paper proves it for every ε ≥ 2/√n, smaller ε
being the trivial case, in additive form on squared distances of points
of norm at most 1, with the step from bits to dimension given as a short
remark. The relative form follows for small ε but is not stated. The
upper half of the conjecture is proved only in a bipartite form without
norm bounds, so the one-set JL lemma at log(2 + ε²n)/ε² is still open.

For [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) it extends [THEORY-tmpfo89o](../theory.d/THEORY-tmpfo89o.md)'s lower bound to the
whole range of ε, filed as [THEORY-tmpup7x5](../theory.d/THEORY-tmpup7x5.md), and gives the bipartite upper
bound, filed as [THEORY-tmpbh0v2](../theory.d/THEORY-tmpbh0v2.md). On the distances thread its count is the
log of a family's size, but for small ε that log is of 2 + ε²n, not of
the n² pairs a union bound counts. On superposition it says nothing
directly. `information-theory` is for its question, the bits needed to
store approximate inner products. It carries no instruction for
machine-learning practice.
