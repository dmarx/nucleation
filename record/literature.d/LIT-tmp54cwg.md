---
status: Active
status_note: 'read 2026-10-23 (NOTE-tmp7wl76): in full, from arXiv 0811.1067v2 (42 pp.). HodgeRank. Pairwise comparisons, aggregated into a weighted edge flow on the graph of alternatives, decompose orthogonally into a gradient flow, the l2-best global ranking found by weighted least squares, and a divergence-free residual. The residual splits into curl (local, triangular inconsistency) and harmonic (global inconsistency) parts. Binary win/loss data enter as averaged signs, and on complete balanced binary data the ranking is Borda''s. The decomposition is cardinal: curl-freeness is stronger than transitivity. It is the tool for reading the record''s conflict record.'
title: 'Statistical ranking and combinatorial Hodge theory'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: arXiv 0811.1067v2 (10 August 2009), §§1–8. Details checked
    against Crossref (DOI 10.1007/s10107-010-0419-x: Mathematical
    Programming 127(1):203–244, online 28 November 2010, issue March 2011).
    `published:` is the arXiv v1 date. The published version was not seen,
    so page and result numbers are the arXiv version's. No duplicate was
    found in literature.d by title, DOI, arXiv id or author.
tags:
- mathematical-statistics
- mathematics
- network-science
- anthology-candidate
date: '2026-10-23'
published: '2008-11-07'
arxiv: '0811.1067'
doi: '10.1007/s10107-010-0419-x'
first_author: 'Jiang'
keywords:
- 'statistical ranking'
- 'rank aggregation'
- 'combinatorial Hodge theory'
- 'discrete exterior calculus'
- 'combinatorial Laplacian'
- 'graph Helmholtzian'
- 'Kemeny optimization'
- 'Borda count'
implementations: []
summary: >-
  Jiang, Lim, Yao & Ye (2011), Mathematical Programming 127:203–244.
  HodgeRank: an edge flow of aggregated pairwise comparisons splits
  orthogonally into a gradient flow, whose potential is the
  least-squares global ranking (a Borda count generalized to incomplete
  data), and a cyclic residual, which splits into curl (local) and
  harmonic (global) inconsistency (Theorems 4.8, 5.1). The residual's
  share, the "cyclicity ratio", certifies the ranking.
---
<!-- inactive-ok-file: TERM-tmp8gbrt CLAIM-tmpz8lli QUESTION-tmpsqwu5 THEORY-tmp4zhyp — Proposed, Open or draft; the term, claim and question this reading bears on, and the reading filed with it -->

# LIT-tmp54cwg: Statistical ranking and combinatorial Hodge theory

Xiaoye Jiang, Lek-Heng Lim, Yuan Yao and Yinyu Ye (2011), *Mathematical
Programming* 127(1):203–244 — DOI-10.1007/s10107-010-0419-x, ARXIV-0811.1067

## Key takeaways

- **Comparisons as a flow.** Voters' pairwise comparisons are aggregated
  into a skew-symmetric Ȳ on the graph whose edges are the compared pairs,
  weighted by w_ij, the number of comparisons (eqs. 4–8). Four
  aggregations are offered (§2.2.1). One of them is binary: Ȳ_ij is the
  share preferring j minus the share preferring i, which "is invariant up
  to a monotone transformation" (p. 10).
- **HodgeRank** (eq. 7, Theorem 5.1, pp. 21–22). The global ranking is the
  weighted least-squares projection of Ȳ onto gradient flows, s* = −∆₀†
  div Ȳ. The residual is divergence-free. It splits into a curl part,
  which is "a local cyclic ranking accounting for local inconsistencies",
  and a harmonic part, which is "a harmonic ranking accounting for global
  inconsistencies" (p. 22).
- **Local implies global when there are no holes** (Theorem 5.2, p. 24).
  If the comparison graph's 3-clique complex has β₁ = 0, "every locally
  consistent pairwise ranking is also globally consistent". The harmonic
  part is always zero on a complete comparison graph.
- **Cardinal, not ordinal.** Curl measures triangular inconsistency. It
  "extends the consistency index of Kendall and Smith [26], which counts
  the number of circular triads, from ordinal settings to cardinal
  settings" (p. 12). The impossibility theorems of social choice "are
  about intransitivity", while their approach deals with inconsistency,
  "which is a cardinal condition" (p. 30).
- **Social choice.** For complete, balanced, binary data the HodgeRank
  ranking is the Borda count (p. 31). Kemeny optimization is the ordinal
  counterpart, an l1 projection onto the transitive region, and it is
  NP-hard (Theorem 7.1, pp. 31–32).
- **Certificate.** "the data may be ‘explained’ by a global ranking only
  when the cyclic component is small" (p. 30). The cyclicity ratio
  C_p = ‖R*‖²/‖Ȳ‖² measures it (p. 35).

## Standing in the record

Filed on 2026-10-23 at the owner's request. It is the measure the
renamed term needs: QUESTION-tmpsqwu5's conflict record is a set of
pairwise decisions, and this paper decomposes such a set. Read in
NOTE-tmp7wl76, whose bearing section sets out what the measure assumes.
The decomposition theorem is THEORY-tmp4zhyp, with Candogan et al.
(LIT-tmp7pue2).
