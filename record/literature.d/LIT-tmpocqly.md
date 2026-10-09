---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp4751w](../notes.d/NOTE-tmp4751w.md)); worth reading as an empirical check, on synthetic trees and four benchmark graphs, of the assumption that a hyperbolic model trained on an ordinary task loss lays out the data''s hierarchy by itself, root near the origin and leaves near the boundary. It does so only partly. On two 3-ary trees of 1,093 nodes, a hyperbolic graph convolutional network (HGCN) trained for link prediction or node classification puts the root nowhere near the smallest distance to the origin, and the nodes'' distances to the origin come out roughly bell-shaped rather than piling up at the leaves; read off as levels, those distances order random node pairs correctly 69–75% of the time. The proposed fix, HIE, recentres the embedding on its hyperbolic centroid and adds a loss that pushes every node outward in proportion to its current distance. It raises that ordering to 75–84% and lifts benchmark scores, most on the least tree-like graphs (Citeseer, Cora). There is no theory of why task losses fail to produce the hierarchy, and the fix itself uses no level information.'
title: 'Hyperbolic Representation Learning: Revisiting and Advancing'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 in a batch of six works on
    hierarchy and hyperbolic geometry, and read in full the same day
    (NOTE-tmp4751w) from the arXiv PDF of v1 (15 June 2023, 21 pp.), text
    extracted with pdftotext: §§1–6 and Appendices A–H, figures read from
    their captions, inset statistics and text. The owner described the work
    only as "Yang et al. (2023): why hyperbolic latent geometry does not
    automatically produce the intended hierarchical structure". The
    identification was checked before filing. An arXiv API search of
    2022–2024 papers with an author Yang and "hyperbolic" with
    "hierarch*", "latent" or "variational" in the abstract, a title search
    for "hyperbolic" with an author Yang, and two web searches for a 2023
    Yang et al. paper on hyperbolic VAEs or latent spaces failing to capture
    hierarchy found no better match. The near candidates were Zhang, Zhu,
    Yang et al. on dimensional collapse in hyperbolic graph contrastive
    learning (arXiv:2310.18209; first author Zhang, and about collapse,
    not hierarchy) and Xu et al. on hyperbolic hierarchical margins
    (arXiv:2311.11019; no author Yang). This paper's abstract states the
    described thesis in so many words ("Current endeavors ... presuppose
    that the underlying hierarchies can be automatically inferred and
    preserved ... This assumption, however, is questionable"). Title, the
    five authors and the comment "ICML 2023" from the arXiv abstract page
    (arXiv:2306.09118, one version, submitted 15 June 2023). The PMLR
    volume page confirms the published version: Proceedings of the 40th
    International Conference on Machine Learning, PMLR 202:39639–39659,
    proceedings.mlr.press/v202/yang23u.html, same title and authors. It has
    no DOI: a Crossref title search returned nothing for it, and dblp's API
    did not answer. `published:` is the arXiv v1 date, 15 June 2023,
    earlier than the conference in July (ADR-002). Not held in nucleation
    before this filing: a grep of record/ for the identifier, the title,
    "Menglin" and "hyperbolic" found only unrelated uses (hyperbolic
    discounting, hyperbolic coordinates). Not held in the Anthology of the
    SOTA as far as its clone shows: a grep of its record/ (clone at commit
    d8b5ba5, 9 October 2026, possibly stale) for the identifier, the title,
    "Menglin" and "hyperbolic" found only "hyperbolic secant" in
    ANTH-LIT-692 and ANTH-THEORY-106. It is a method paper for graph
    representation learning, which an anthology topic could hold, hence
    `anthology-candidate`. The OpenReview forum (id 9CZZ8tIhSv) was not
    read.
tags:
- representation-learning
- network-science
- anthology-candidate
date: '2026-10-09'
published: '2023-06-15'
arxiv: '2306.09118'
first_author: 'Yang'
keywords:
- 'hyperbolic representation learning'
- 'hyperbolic graph neural networks'
- 'Poincaré ball'
- 'Lorentz model'
- 'hyperbolic distance to origin'
- 'hierarchy'
- 'root alignment'
- 'hyperbolic informed embedding'
implementations: []
summary: >-
  Yang, Zhou, Ying, Chen and King (2023), ICML 2023, PMLR 202. Tracks the
  hyperbolic distance from each node to the origin and finds that hyperbolic
  models trained on ordinary task losses do not by themselves place a tree's
  root nearest the origin or spread its levels outward: on synthetic 3-ary
  trees the root sits well off the minimum and the distances are roughly
  bell-shaped, ordering node pairs by level only 69–75% of the time.
  Proposes HIE, which recentres the embedding on its hyperbolic centroid and
  pushes nodes outward; it improves that ordering and benchmark scores, most
  on the least tree-like graphs.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 CLAIM-119 LIT-267 — Open or Proposed; cited as the question this batch was filed for and the accounts it joins -->

# LIT-tmpocqly: Hyperbolic Representation Learning: Revisiting and Advancing

Menglin Yang, Min Zhou, Rex Ying, Yankai Chen and Irwin King (2023),
*Proceedings of the 40th International Conference on Machine Learning*
(ICML 2023), PMLR 202:39639–39659 — [ARXIV-2306.09118](https://arxiv.org/abs/2306.09118)

## Key takeaways

- **The assumption tested.** Hyperbolic embedding methods are trained on
  losses that never mention the hierarchy: a softmax over hyperbolic
  distances for shallow embeddings, cross-entropy for node classification,
  a Fermi–Dirac link likelihood for link prediction. The expected outcome,
  root near the origin and each level further out, is assumed to arise by
  itself. The paper measures it with one statistic, the hyperbolic
  distance of each node to the origin (HDO), read as its level.
- **What it finds.** On two synthetic 3-ary trees of eight levels (1,093
  nodes) that differ only in how labels follow the tree, HGCN trained for
  link prediction or node classification leaves the root at HDO 1.8–3.3
  while the minimum is 1.2–2.4. The HDO distribution is roughly normal,
  where a tree's leaf-heavy level counts would put most nodes far out.
  Pairs of nodes ordered by HDO match their true levels in 69–75% of 5,000
  random pairs (Table 9). The geometry has room for the tree, but the
  trained embedding uses the room only partly.
- **The fix, and what it does.** HIE recentres the embedding on its
  hyperbolic centroid (the Möbius gyromidpoint or Lorentzian centroid),
  taken as a stand-in for the root, and adds a loss that rewards a large
  HDO-weighted mean of HDO, pushing every node outward in proportion to
  how far out it already is. No level labels enter. It raises the pairwise
  level ordering to 75–84%, and it improves link prediction on DISEASE by
  up to 21.4% (with 25% of links for training) and node classification on
  four graphs. The largest classification gains are on Citeseer and Cora,
  the least tree-like, which the authors put down to the outward push
  separating classes rather than to hierarchy.
- **What it does not give.** No account of why task losses fail to produce
  the radial ordering, and no measure of hierarchy on the real graphs,
  whose levels are unknown. The evidence that HIE recovers hierarchy rather
  than just spreading the embedding is Table 9 alone, on the two synthetic
  trees.

## Standing in the record

Filed on 2026-10-09 at the owner's request, in a batch of six works on
hierarchy and hyperbolic geometry asked for right after the record opened
[QUESTION-025](../questions.d/QUESTION-025.md): whether correlated or hierarchical attributes in
co-occurrence still give linear attribute directions, and a concept
lattice that is not Boolean. That question builds on [THEORY-185](../theory.d/THEORY-185.md) and [LIT-863](LIT-863.md).
The batch's other works are Cagnetta et al.'s random hierarchy model,
Krioukov et al. (2010) on the hyperbolic geometry of complex networks, Sala
et al. (2018) on representation trade-offs for hyperbolic embeddings, Lin
et al. (2023) on multiscale geometry recovering a latent hierarchy, and
Zhang et al. (2023) on hyperbolic geometry in hippocampal representations.
This paper cites Krioukov et al. for the tree–hyperbolic-space analogy that
motivates its statistic, and Sala et al. among works on hyperbolic
embedding.

Read on 2026-10-09 ([NOTE-tmp4751w](../notes.d/NOTE-tmp4751w.md)). It does not answer [QUESTION-025](../questions.d/QUESTION-025.md).
It encodes hierarchy as distance from an origin rather than as linear
directions, and it trains graph models rather than embedding co-occurrence.
What it adds is a caution that applies to any proposed answer. A
representation space that *can* hold a hierarchy, here a geometry built
for trees, does not show that a trained representation *does* hold it. The
hierarchy has to be measured directly, as the measurement arm of the
question asks.
