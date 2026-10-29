---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmp6e5aw](../notes.d/NOTE-tmp6e5aw.md)), from arXiv v3; worth reading for the metric and interpolation theorems of fused Gromov–Wasserstein, from which it follows that anchors as features break exactly the structural symmetries that move them.
title: 'Optimal Transport for structured data with application on graphs'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A6 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2018-05-23 (ICML 2019,
    PMLR 97; PMLR's metadata scrambles the authors' names) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from arXiv 1805.09114v3 (13 May 2019, ICML camera-ready with supplement; v1 was titled "Optimal Transport for structured data"), with numerical checks (NOTE-tmp6e5aw); THEORY-tmpwl8e3 and THEORY-tmp7cnkm filed. Citation unchanged. The summary is rewritten from the text; the earlier summary's "beats graph kernels and convolutional networks" is qualified by the paper's own supplement, where Wasserstein on features alone matches or beats FGW on six of nine attributed datasets.
tags:
- mathematics
- network-science
- anthology-candidate
date: '2026-10-29'
published: '2018-05-23'
arxiv: '1805.09114'
first_author: 'Vayer'
keywords:
- 'Fused Gromov-Wasserstein'
- 'optimal transport'
- 'structured data'
- 'graph classification'
- 'barycenters'
implementations: []
summary: >-
  Vayer, Chapel, Flamary, Tavenard & Courty (2019). Fused Gromov–Wasserstein compares two attributed graphs with one coupling whose cost mixes, with weight α, a Wasserstein term on node features and a Gromov–Wasserstein term on structure. It tends to W as α → 0 and to GW as α → 1, and for q = 1, interior α and distance-matrix structures it is a metric that vanishes exactly when a bijection preserves weights, features and structure (a 2^{q−1}-relaxed semi-metric for q > 1). A conditional-gradient solver reaches stationary points, and a block coordinate barycenter supports graph k-means. On graph classification it is competitive with kernels and graph CNNs, though the supplement's Wasserstein-only scores match or beat it on several datasets.
---

# LIT-tmpjs7kp: Optimal Transport for structured data with application on graphs

Vayer, T., Chapel, L., Flamary, R., Tavenard, R., & Courty, N. (2019). Optimal transport for structured data with application on graphs. *ICML 2019*, PMLR 97, 6275–6284.

## Why this is here

A6 thought it "probably the most practical model for [CASE-055](../cases.d/CASE-055.md)": independently validated anchor matches break the symmetries pure GW cannot, and the weight between structure and anchors is a scientific parameter to vary, not a hyperparameter to tune. An arm of [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md).

The reading ([NOTE-tmp6e5aw](../notes.d/NOTE-tmp6e5aw.md)) confirms the first point with a condition: anchors break a symmetry only if it moves them, so anchors placed on an axis of symmetry leave the tie ([THEORY-tmp7cnkm](../theory.d/THEORY-tmp7cnkm.md)). The paper itself treats α as a cross-validated hyperparameter and proves only its endpoint limits; the exact FGW value is concave in α, which suits reading α as a parameter to vary.
