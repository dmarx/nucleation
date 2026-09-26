---
number: 221
status: Skimmed
formerly:
- NOTE-tmp6dakr
paper: LIT-253
title: 'Closeness in Distribution vs Representational Similarity'
version: 1
date: '2026-09-26'
summary: >-
  For softmax models p(y|x) ∝ exp(f(x)ᵀg(y)) under a diversity condition, the model distribution determines the embeddings and unembeddings up to an invertible linear map (f = Af′, g₀ = A⁻ᵀg′₀). The determination is not stable under KL divergence, though: two models can be ε-close in KL, even both near maximum likelihood, while their embeddings are far from linearly equivalent.
---
<!-- inactive-ok-file: LIT-253 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-221: Closeness in Distribution vs Representational Similarity

## Contribution

The authors approach representational similarity through identifiability theory: a similarity measure should be invariant to exactly the transformations that leave the model's distribution unchanged. For a model family covering autoregressive language models, contrastive predictive coding and standard classifiers, they prove that a small KL divergence between model distributions does not imply similar representations, so models near maximum likelihood can still represent differently, as their CIFAR-10 experiments also show. They then define a different distributional distance under which closeness does bound representational dissimilarity. In synthetic experiments, wider networks are closer in that distance and more similar in representation.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 and footnote 3: representations are "equivalent" when they give equal likelihoods. The equivalence classes form a quotient Θ/∼_L, and the similarity measure should be invariant to exactly that group.
- §2, Definition 2.1 (diversity) and Theorem 2.2 (Linear Identifiability, citing Roeder et al. and others): equal conditionals imply f(x) = Af′(x) and g₀(y) = A⁻ᵀg′₀(y). In the authors' words, "to each probability distribution … corresponds a unique (up to equivalence) choice of embeddings and unembeddings".
- §3, Theorem 3.1 and Corollary 3.2 (informal): with |Y| ≥ M+1 there are model pairs with d_KL ≤ ε whose embeddings are not close to linearly equivalent. The construction permutes the unembedding clusters and sends their norm ρ → ∞.
- §4: Definition 4.4 (the log-likelihood variance distance), Definition 4.5 (a PLS-SVD dissimilarity) and Theorem 4.7, which bounds dissimilarity by 2Mε in that distance.
- Discussion: the invariance group here is a subset of invertible linear maps, not the orthogonal group argued for by Kornblith et al. The authors frame "what measure best captures representational similarity" as open, and extending the analysis beyond the embedding and unembedding layers as needing intermediate-layer identifiability results that do not yet exist.

## Open questions

- It is the closest ML statement found to the GNS pattern "the state determines the representation up to a symmetry group". Here the "state" is the model distribution, and the group is GL(M) (paired A and A⁻ᵀ), not the orthogonal group. The group differs because the observable is the cross inner product f·g, not the Gram matrix of f alone.
- Theorem 3.1 is a warning for the Platonic hypothesis ([ANTH-LIT-458](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-458.md)). Convergence of distributions (or of performance) does not by itself give convergence of representations, and the right distance matters.
- A deeper reading should check whether Theorem 4.7's distance relates to kernel-based comparisons, and the extended-linear identifiability of Marconato et al. cited in the Discussion.
