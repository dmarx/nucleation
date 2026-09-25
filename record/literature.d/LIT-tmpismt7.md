---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'How Local Separators Shape Community Structure in Large Networks'
version: 1
tags:
- network-science
- mathematics
date: '2026-09-25'
published: '2025-04-20'
arxiv: '2504.14501'
first_author: 'Frenkel'
keywords:
- 'community detection'
- 'local separators'
- 'graph decomposition'
- 'modularity'
- 'road networks'
implementations: []
summary: >-
  Frenkel et al. (2025), [ARXIV-2504.14501](https://arxiv.org/abs/2504.14501). Decomposing a graph at local 1-separators (local cut-vertices) finds the densest communities, denser than modularity-based methods produce, on large sparse real networks and especially road networks. Local 2-separators then expose hierarchical sub-structure, at the risk of over-fragmenting small clusters.
---

# LIT-tmpismt7: How Local Separators Shape Community Structure in Large Networks

Sarah Frenkel, Johannes Carmesin (2025), *arXiv preprint* — [ARXIV-2504.14501](https://arxiv.org/abs/2504.14501)

## Key takeaways

- Decomposing a graph at local 1-separators (local cut-vertices) finds the densest communities, denser than modularity-based methods produce, on large sparse real networks and especially road networks. Local 2-separators then expose hierarchical sub-structure, at the risk of over-fragmenting small clusters.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Standard community detection, such as modularity optimization, looks for densely connected groups and can miss natural local bottlenecks. The authors study local-separator methods, which split a network at small vertex sets that separate their local neighbourhood. They compare these methods systematically with established algorithms on large real networks. Local 1-separators consistently find the densest communities. Local 2-separators reveal hierarchy but may break up small clusters. Results are strongest on road networks, and the authors present local separators as a scalable, interpretable alternative.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier C): 300 seconds of active reading over 3 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — A short empirical comparison that the skim captures. Moderate owner time (t=300 s over 3 sessions). Worth filing only if the Ricci-flow community-detection note wants a comparison partner.**

What a deeper reading should check:

- The paper is useful mainly for its argument against using modularity as the sole evaluation criterion, which applies to any community-detection comparison.
- Its own density criterion (§2.5) needs scrutiny, since the authors define it themselves and it may favour their method despite the stated intent. A deeper reading should also check the scalability claims (runtime is not obviously reported) and whether the theory of local separators (the authors' refs [7, 9]) should be the cited source instead.

Access when seeded: I read the arXiv abstract page (v1 20 Apr 2025, cs.SI and cs.DM) and the full PDF (15 pp.): §1, §2.1–2.5 (methodology and critique of modularity), the empirical sections by heading and figure (Netscience, Euroroads, NRW road network), and §6 (Concluding Remarks). arXiv lists no journal reference. Note that the text never mentions Ricci flow, so the survey's "companion of held Ricci-flow community detection" is the survey's own link, not the paper's.
