---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Characterizing Complex Networks with Forman-Ricci Curvature and Associated Geometric Flows'
version: 1
tags:
- network-science
- mathematics
date: '2026-09-25'
published: '2016-07-01'
arxiv: '1607.08654'
doi: '10.1093/comnet/cnw030'
first_author: 'Weber'
keywords:
- 'Complex networks'
- 'Forman-Ricci-curvature'
- 'Ricci-flow'
- 'Laplacian flow'
- 'data mining'
implementations: []
summary: >-
  Weber et al. (2016), [ARXIV-1607.08654](https://arxiv.org/abs/1607.08654). Forman's combinatorial discretization of Ricci curvature gives a cheap, edge-based network characteristic whose distribution separates model network classes (real networks resemble Barabasi-Albert) and whose associated Ricci and Laplacian flows can be used for change detection and denoising in evolving weighted networks.
---

# LIT-tmpm8djm: Characterizing Complex Networks with Forman-Ricci Curvature and Associated Geometric Flows

Melanie Weber, Emil Saucan, Jürgen Jost (2016), *Journal of Complex Networks 5, 527-550 (2017); first posted as arXiv preprint* — [ARXIV-1607.08654](https://arxiv.org/abs/1607.08654)

## Key takeaways

- Forman's combinatorial discretization of Ricci curvature gives a cheap, edge-based network characteristic whose distribution separates model network classes (real networks resemble Barabasi-Albert) and whose associated Ricci and Laplacian flows can be used for change detection and denoising in evolving weighted networks.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The paper proposes Forman-Ricci curvature, and the geometric flow built on it, as edge-level descriptors of complex networks to complement the usual node-based statistics. After motivating the construction mathematically, the authors compute these quantities on static and time-evolving networks and compare them with established node-degree-based measures. They argue the tools could support data-mining tasks such as denoising, clustering, and extrapolating how a network evolves.

## Standing in the record

Filed by the reading-time triage of 2026-09-25: 1,790 seconds of active reading over 3 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — frequently cited foundational source for Forman curvature on networks and the owner spent ~30 min (t=1790 s); the skim captures the constructions, but the curvature formula and flow definitions (§2.3, §4) are worth a careful pass if graph curvature is being used downstream.**

What a deeper reading should check:

- The practical claim (Forman ~ Ollivier at a fraction of the cost) is asserted with "strong indications" and deferred to a forthcoming study; verify against later comparison papers before relying on it.
- Empirical evidence is small (three real networks, three models); the "classification scheme" is demonstrated on a handful of samples.
- ML link: discrete Ricci curvature (Forman and variants) later became a tool for diagnosing over-squashing and guiding graph rewiring in GNNs; this paper is an early network-science source for Forman curvature on graphs, not for those GNN results themselves.

Access when seeded: arXiv abs page and full v2 PDF (29 pp., "extended version") read via arxiv.org. The arXiv page gives no DOI (comment says "To appear in: Journal of Complex Networks"); the DOI was matched through a Crossref bibliographic search (same title, authors Weber/Saucan/Jost, J. Complex Networks vol. 5 pp. 527-550, online 2017-01-16). Keywords are taken verbatim from the line after the abstract in the PDF. Supplemental Material (implementation details) not read.
