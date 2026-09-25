---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Community Detection on Networks with Ricci Flow'
version: 1
tags:
- network-science
date: '2026-09-25'
published: '2019-07-01'
arxiv: '1907.03993'
doi: '10.1038/s41598-019-46380-9'
first_author: 'Ni'
keywords:
- 'community detection'
- 'Ollivier-Ricci curvature'
- 'discrete Ricci flow'
- 'optimal transport'
- 'network surgery'
implementations: []
summary: >-
  Ni et al. (2019), [ARXIV-1907.03993](https://arxiv.org/abs/1907.03993). Iterating an Ollivier-Ricci-curvature-driven flow on edge weights stretches inter-community (negatively curved) edges and shrinks intra-community (positively curved) ones, so thresholding the evolved weights ("surgery") recovers communities with accuracy competitive with or better than standard methods on SBM, LFR and several labelled real networks.
---

# LIT-tmp3on2v: Community Detection on Networks with Ricci Flow

Chien-Chun Ni, Yu-Yao Lin, Feng Luo, Jie Gao (2019), *Scientific Reports 9, 9984 (2019)* — [ARXIV-1907.03993](https://arxiv.org/abs/1907.03993)

## Key takeaways

- Iterating an Ollivier-Ricci-curvature-driven flow on edge weights stretches inter-community (negatively curved) edges and shrinks intra-community (positively curved) ones, so thresholding the evolved weights ("surgery") recovers communities with accuracy competitive with or better than standard methods on SBM, LFR and several labelled real networks.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Real networks often contain communities, and most detection methods are statistical or combinatorial. The authors instead treat a network as a geometric object and communities as a geometric decomposition, borrowing curvature and discrete Ricci flow, tools that decompose smooth manifolds in mathematics. They apply this to networks with known ground-truth communities and report that the geometric approach is effective.

## Standing in the record

Filed by the reading-time triage of 2026-09-25: 770 seconds of active reading over 5 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — the algorithm and headline results are fully captured by this skim and the owner spent ~13 min (t=770 s); only read deeper if implementing Ricci-flow clustering or needing the SI proof.**

What a deeper reading should check:

- The empirical superiority claims rest on a limited benchmark set (SBM, LFR, GNet, ~6 labelled real graphs) compared against iGraph baselines; check sensitivity to the surgery threshold and number of iterations, which are hand-set.
- Theorem 4.1 covers only a highly symmetric toy family; whether any guarantee extends to SBM-like graphs is not shown here.
- ML link: Ollivier-Ricci curvature and the GraphRicciCurvature tooling are used in later graph-learning work (e.g. curvature-based analyses of GNN message passing); this paper is the community-detection source, not a GNN paper.

Access when seeded: arXiv abs page and full v1 PDF (29 pp. incl. supplementary information) read via arxiv.org. DOI confirmed via Crossref (Sci. Rep. 9, article 9984, published 2019-07-10). The paper lists no keywords; those above are chosen from its text. Supplementary proofs (Theorem 4.1) not checked.
