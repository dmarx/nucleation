---
status: Skimmed
paper: LIT-tmpismt7
title: 'Local separators and community structure'
version: 1
date: '2026-09-25'
summary: >-
  Decomposing a graph at local 1-separators (local cut-vertices) finds the densest communities, denser than modularity-based methods produce, on large sparse real networks and especially road networks. Local 2-separators then expose hierarchical sub-structure, at the risk of over-fragmenting small clusters.
---

<!-- inactive-ok-file: LIT-tmpismt7 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpz49bi: Local separators and community structure

## Contribution

Standard community detection, such as modularity optimization, looks for densely connected groups and can miss natural local bottlenecks. The authors study local-separator methods, which split a network at small vertex sets that separate their local neighbourhood. They compare these methods systematically with established algorithms on large real networks. Local 1-separators consistently find the densest communities. Local 2-separators reveal hierarchy but may break up small clusters. Results are strongest on road networks, and the authors present local separators as a scalable, interpretable alternative.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Motivation (§1, Fig. 1): on the dolphins network, modularity methods only partly recover the two known social groups, while the local-separator decomposition recovers them up to two boundary nodes, with overlap allowed.
- Baselines (§2.2): Infomap, Label Propagation, Leiden (modularity) and Best Multi-Level, all taken from igraph.
- Modularity comparison (§2.3, Table 2): modularity-optimizing methods score highest, as expected. Local separators score comparably to Infomap and Label Propagation.
- Critique of modularity (§2.4): modularity favours few large communities and never decreases when communities are merged, so it confounds quality with community count and size. Hence a new, explicitly algorithm-independent density-based evaluation (§2.5).
- Road networks and conclusions (§4–6, Fig. 4): on Euroroads and NRW, local 1-separators give the densest clusters, and local 2-separators refine large clusters hierarchically. Future work: biological, social and communication networks, and hybrids with modularity methods.

## Open questions

- The paper is useful mainly for its argument against using modularity as the sole evaluation criterion, which applies to any community-detection comparison.
- Its own density criterion (§2.5) needs scrutiny, since the authors define it themselves and it may favour their method despite the stated intent. A deeper reading should also check the scalability claims (runtime is not obviously reported) and whether the theory of local separators (the authors' refs [7, 9]) should be the cited source instead.
