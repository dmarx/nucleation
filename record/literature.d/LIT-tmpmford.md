---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Similarity of Neural Network Representations Revisited'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-09-26'
published: '2019-05-01'
arxiv: '1905.00414'
first_author: 'Kornblith'
keywords:
- 'representational similarity'
- 'centered kernel alignment'
- 'CCA'
- 'invariance'
- 'HSIC'
implementations: []
summary: >-
  Kornblith et al. (2019), [ARXIV-1905.00414](https://arxiv.org/abs/1905.00414). A similarity index for neural representations should be invariant to orthogonal transformation and isotropic scaling but not to arbitrary invertible linear maps, and comparing the example-by-example Gram matrices (linear or kernel CKA) achieves exactly that, while any index invariant to invertible linear maps becomes uninformative once width reaches the number of examples.
---

# LIT-tmpmford: Similarity of Neural Network Representations Revisited

Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton (2019), *ICML 2019 (Proceedings of the 36th International Conference on Machine Learning, PMLR vol. 97); first appeared as arXiv preprint* — [ARXIV-1905.00414](https://arxiv.org/abs/1905.00414)

## Key takeaways

- A similarity index for neural representations should be invariant to orthogonal transformation and isotropic scaling but not to arbitrary invertible linear maps, and comparing the example-by-example Gram matrices (linear or kernel CKA) achieves exactly that, while any index invariant to invertible linear maps becomes uninformative once width reaches the number of examples.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The paper examines ways of comparing the representations of different layers and networks, starting from CCA-based methods. It shows that CCA is one of a family of multivariate similarity statistics, and proves that no statistic invariant to invertible linear transformation can meaningfully compare representations whose dimension exceeds the number of data points. It proposes centered kernel alignment (CKA), a normalised Hilbert–Schmidt independence criterion on example-by-example kernel matrices, and shows it identifies correspondences between layers of networks trained from different initializations where CCA-style methods fail.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *GNS, unitary equivalence and the convergence of representations* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: high — the standard kernel-comparison reference for representations, short, and the skim already captures the load-bearing equations; a full read is cheap.**

What a deeper reading should check:

- It is the reference the Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)) cites for comparing representations by their kernels. It is also where "invariant to orthogonal transformation" is argued to be the right equivalence for representations, which is the finite-sample shadow of "determined up to unitary equivalence".
- A deeper reading should check how the centering matrix H interacts with the constant offset c_X in the Platonic paper's PMI-kernel argument (K + c11ᵀ has the same centred form), and how RBF-CKA's bandwidth choice breaks scale invariance (Table 1 footnote).
- The invariance arguments in §2.2 are heuristic, about training dynamics rather than a theorem that O(p) is the right group. Later work (the identifiability literature) argues for other groups.

Access when seeded: Read the arXiv abstract page (v1 submitted 2019-05-01; comment "ICML 2019") and the full arXiv PDF text (20 pp.): §2 (invariances) and §3 (comparing similarity structures) in full, section heads and the results of §6, the conclusion (§7) and Appendix A–B. No DOI (PMLR issues none).
