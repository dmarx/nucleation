---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmp60yfn](../notes.d/NOTE-tmp60yfn.md)), from the arXiv v2; worth
  reading as a precise case of budgeted question choice within a fixed
  vocabulary: which object's correspondence to ask about, scored by an
  exact derivative through entropic transport of a coherence proxy, and
  evaluated on accuracy.
title: 'AvAtar: Learning to Align via Active Optimal Transport'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A7 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2026-05-23 (ICML 2026,
    PMLR 306, 151023–151044) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 2605.24395v2 (15 Jul 2026), 22 pp. with
    appendices A–D, in NOTE-tmp60yfn. THEORY-tmpr2ueq and THEORY-tmpzfqlq
    filed. Summary rewritten from the text. Tagged anthology-candidate
    (ADR-005): its practical content is a query strategy for ML alignment.
    The citation stands. Found: Table 2's entropy utility and its stated
    gradient differ in sign.
tags:
- mathematics
- network-science
- anthology-candidate
date: '2026-10-29'
published: '2026-05-23'
arxiv: '2605.24395'
first_author: 'Yu'
keywords:
- 'active learning'
- 'optimal transport'
- 'network alignment'
- 'adjoint-state method'
- 'entropy regularization'
implementations:
- 'https://github.com/yq-leo/AvAtar-ICML26'
summary: >-
  Yu et al. (2026). Active learning for alignment by entropic optimal
  transport. The oracle answers one fixed question, which target matches
  a given source object, and an answer sets that pair's cost to zero.
  AvAtar ranks source objects by the derivative of a proxy utility of the
  transport plan (its squared norm, entropy, or graph consistency) with
  respect to supervising each candidate match, averaged over matches by
  the current plan. The derivative is exact, from one singular positive
  semidefinite (n + m) linear system solved by conjugate gradients. With
  20% of true pairs given and 20% more chosen in ten rounds, it beats
  uncertainty, centrality and matching-sampling rules on network
  alignment and image–text tasks by up to 2.8 MRR points, without
  reported variances; weighting by the current plan is essential.
---
<!-- inactive-ok-file: TERM-092 CLAIM-475 THEORY-tmpzfqlq — Proposed; cited as open -->

# LIT-tmpe5bbx: AvAtar: Learning to Align via Active Optimal Transport

Yu, Q., Qiu, R., Zeng, Z., Thai, M. T., Liu, H., & Tong, H. (2026). AvAtar: Learning to align via active optimal transport. *ICML 2026*, PMLR 306, 151023–151044.

Read in full in [NOTE-tmp60yfn](../notes.d/NOTE-tmp60yfn.md).

## Key takeaways

- What is chosen is a source object; the oracle names its match; the
  question form, object sets, cost and utility are fixed. It allocates a
  label budget among questions already askable.
- The score is an exact first-order derivative through entropic OT
  ([THEORY-tmpr2ueq](../theory.d/THEORY-tmpr2ueq.md)), of a coherence proxy, not of accuracy.
- Its gains are small and reported without variances ([THEORY-tmpzfqlq](../theory.d/THEORY-tmpzfqlq.md));
  without weighting by the current plan the rule does worse than random.

## Why this is here

A7's highest-priority connection, to the inquiry frontier ([TERM-092](../terms.d/TERM-092.md), [CLAIM-475](../claims.d/CLAIM-475.md)): establishing a correspondence is a budgeted choice of which question to ask. A7's distinction is kept: AvAtar chooses a query within a fixed vocabulary, while [TERM-092](../terms.d/TERM-092.md) also asks how the vocabulary in which new questions become askable is extended.

The reading confirms A7's distinction exactly. One refinement: the budget
counts answers only. The cost of choosing is measured as query time but
not charged, and formulating costs nothing because the questions are
given, so the paper bears on neither of [CLAIM-475](../claims.d/CLAIM-475.md)'s defeaters
([NOTE-tmp60yfn](../notes.d/NOTE-tmp60yfn.md)).
