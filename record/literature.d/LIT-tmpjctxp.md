---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'When Does Closeness in Distribution Imply Representational Similarity? An Identifiability Perspective'
version: 1
tags:
- representation-learning
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-09-26'
published: '2025-06-04'
arxiv: '2506.03784'
first_author: 'Nielsen'
keywords:
- 'identifiability'
- 'representational similarity'
- 'KL divergence'
- 'embeddings and unembeddings'
- 'linear equivalence'
implementations: []
summary: >-
  Nielsen et al. (2025), [ARXIV-2506.03784](https://arxiv.org/abs/2506.03784). For softmax models p(y|x) ∝ exp(f(x)ᵀg(y)) under a diversity condition, the model distribution determines the embeddings and unembeddings up to an invertible linear map (f = Af′, g₀ = A⁻ᵀg′₀). The determination is not stable under KL divergence, though: two models can be ε-close in KL, even both near maximum likelihood, while their embeddings are far from linearly equivalent.
---

# LIT-tmpjctxp: When Does Closeness in Distribution Imply Representational Similarity? An Identifiability Perspective

Beatrix M. G. Nielsen, Emanuele Marconato, Andrea Dittadi, Luigi Gresele (2025), *NeurIPS 2025 (39th Conference on Neural Information Processing Systems), per the arXiv v2 PDF footer; first appeared as arXiv preprint* — [ARXIV-2506.03784](https://arxiv.org/abs/2506.03784)

## Key takeaways

- For softmax models p(y|x) ∝ exp(f(x)ᵀg(y)) under a diversity condition, the model distribution determines the embeddings and unembeddings up to an invertible linear map (f = Af′, g₀ = A⁻ᵀg′₀). The determination is not stable under KL divergence, though: two models can be ε-close in KL, even both near maximum likelihood, while their embeddings are far from linearly equivalent.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The authors approach representational similarity through identifiability theory: a similarity measure should be invariant to exactly the transformations that leave the model's distribution unchanged. For a model family covering autoregressive language models, contrastive predictive coding and standard classifiers, they prove that a small KL divergence between model distributions does not imply similar representations, so models near maximum likelihood can still represent differently, as their CIFAR-10 experiments also show. They then define a different distributional distance under which closeness does bound representational dissimilarity. In synthetic experiments, wider networks are closer in that distance and more similar in representation.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *GNS, unitary equivalence and the convergence of representations* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: high — it states precisely the invariant/realisation relationship this strand is about, for LM-style models, and its negative result bears directly on convergence claims.**

What a deeper reading should check:

- It is the closest ML statement found to the GNS pattern "the state determines the representation up to a symmetry group". Here the "state" is the model distribution, and the group is GL(M) (paired A and A⁻ᵀ), not the orthogonal group. The group differs because the observable is the cross inner product f·g, not the Gram matrix of f alone.
- Theorem 3.1 is a warning for the Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)). Convergence of distributions (or of performance) does not by itself give convergence of representations, and the right distance matters.
- A deeper reading should check whether Theorem 4.7's distance relates to kernel-based comparisons, and the extended-linear identifiability of Marconato et al. cited in the Discussion.

Access when seeded: Read the arXiv abstract page (v1 submitted 2025-06-04) and the full v2 PDF text (53 pp. incl. appendices; v2 dated 2025-10-17): §§1–3 in full, the definitions and theorem statements of §4, and the Discussion. Experiments (§5) and appendix proofs were skimmed or not read. A Crossref search showed a NeurIPS 2025 DOI prefix 10.52202 for the proceedings, but I did not confirm this paper's own DOI, so doi is none.
