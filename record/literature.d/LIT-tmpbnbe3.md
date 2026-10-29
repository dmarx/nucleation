---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md)), from arXiv v3; worth reading for the exact relation between co-optimal transport and Gromov–Wasserstein (a lower bound, equal for squared Euclidean distances) and for what its zero theorem implies: joint sample and feature plans are fixed only up to the matrix's joint row–column symmetries.
title: 'CO-Optimal Transport'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2020-02-10 (NeurIPS
    2020; the proceedings list Vayer first, arXiv Redko) (ADR-002). The
    NeurIPS proceedings list Vayer first; A6 followed arXiv's order.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 2002.03731v3 (6 November 2020, the NeurIPS camera-ready with supplement), with numerical checks (NOTE-tmpghx1t); THEORY-tmps958l and THEORY-tmpvn82m filed. Citation unchanged. The summary is rewritten from the text. One error in the paper: its claim that COOT is strictly positive when the sizes differ is false (duplicated rows give zero).
tags:
- mathematics
- representation-learning
- anthology-candidate
date: '2026-10-29'
published: '2020-02-10'
arxiv: '2002.03731'
first_author: 'Redko'
keywords:
- 'optimal transport'
- 'incomparable spaces'
- 'samples and features'
- 'heterogeneous domain adaptation'
- 'co-clustering'
implementations: []
summary: >-
  Redko, Vayer, Flamary & Courty (2020). Co-optimal transport matches two data matrices of different shapes by fitting a coupling of rows (samples) and a coupling of columns (features) together, under an entry-wise bilinear cost. With equal sizes and uniform weights it is zero exactly when the matrices agree up to separate row and column permutations, and it satisfies the triangle inequality; it proves no uniqueness of the plans, which are fixed only up to joint row–column symmetries. For symmetric matrices it lower-bounds Gromov–Wasserstein, with equality and shared optimal couplings for squared Euclidean distances. Exact solution is NP-hard in general; block coordinate descent reaches block-wise optima. It reports the best accuracy among the baselines on heterogeneous domain adaptation and co-clustering.
---

# LIT-tmpbnbe3: CO-Optimal Transport

Redko, I., Vayer, T., Flamary, R., & Courty, N. (2020). CO-optimal transport. *NeurIPS 2020*.

## Why this is here

A6's highest-priority extension: with utterances as samples and pragmatic probes as features, it matches what two communities say and the questions through which they read it, so the correspondence of probes is fitted, not assumed. That is [CLAIM-257](../claims.d/CLAIM-257.md)'s change of cover and [TERM-092](../terms.d/TERM-092.md)'s frontier in fittable form. A6's warning is kept: utterances and probes can be swapped together at equal cost, so anchors must be independent. An arm of [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md).

The reading ([NOTE-tmpghx1t](../notes.d/NOTE-tmpghx1t.md)) makes the warning exact. COOT never matches an utterance with a probe; the tie is a joint relabelling, within each side, of a block of utterances together with its block of probes ([THEORY-tmpvn82m](../theory.d/THEORY-tmpvn82m.md)). Its fixed-marginal probe coupling also cannot leave a probe unmatched, so [CLAIM-257](../claims.d/CLAIM-257.md)'s change of cover would be absorbed rather than reported unless an unbalanced variant is used.
