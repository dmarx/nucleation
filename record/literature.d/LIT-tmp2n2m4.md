---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpiys9p](../notes.d/NOTE-tmpiys9p.md)); worth reading as the first closed-form account of what a contrastive word-embedding algorithm learns under a rank constraint, and in what order. Replacing word2vec''s logistic loss by its quartic Taylor approximation, and choosing symmetric reweightings whose aggregate weight is constant, turns the objective into unweighted symmetric matrix factorisation of M*, the matrix of relative deviations of word co-occurrence from independence (Theorem 1, proved). From vanishing random initialisation, gradient flow then learns the eigenvectors of M* one at a time, each by a sigmoidal step in time (ln(λ_k/σ²))/λ_k (Result 3, a derivation that drops terms, not a proof). The resulting embeddings track word2vec''s features and benchmark scores closely, and much more closely than truncated factorisations of PMI or positive PMI. The analogy part is empirical: difference vectors of semantic pairs look like a spiked random matrix, and the spike''s strength tracks analogy accuracy.'
title: 'Closed-Form Training Dynamics Reveal Learned Features and Linear Structure in Word2Vec-like Models'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read in full on 2026-10-09 (NOTE-tmpiys9p) from the arXiv PDF
    of v3 (16 October 2025, 26 pages): main text, Appendices A–D, every
    proof and the derivation of Result 3 followed. Identified from the arXiv
    abstract page (arXiv:2502.09863; v1 submitted 14 February 2025, v2 28
    May 2025, v3 16 October 2025). v1 was titled "Solvable Dynamics of
    Self-Supervised Word Embeddings and the Emergence of Analogical
    Reasoning", with the same four authors; the title here is v2's and v3's
    and the published one. Crossref confirms the published version:
    Advances in Neural Information Processing Systems 38 (NeurIPS 2025),
    pp. 4507–4540, DOI 10.52202/085713-0140, authors Dhruva Karkada, James
    B. Simon, Yasaman Bahri, Michael R. DeWeese. `published:` is the arXiv
    v1 date, 14 February 2025 (ADR-002; the earlier of the dates on offer).
    v1 was not read. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone at commit d8b5ba5, 9 October 2026, possibly stale) for
    the arXiv id, the first author, both titles and "QWEM" found nothing.
    It holds word2vec itself (ANTH-LIT-604, ANTH-LIT-610), Levy and
    Goldberg's PMI factorisation (ANTH-LIT-612) and the linear
    representation hypothesis (ANTH-LIT-606). The authors' code is at
    github.com/dkarkada/qwem (not inspected).
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-10-09'
published: '2025-02-14'
arxiv: '2502.09863'
first_author: 'Karkada'
keywords:
- 'word2vec'
- 'skip-gram with negative sampling'
- 'quadratic word embedding models'
- 'matrix factorization'
- 'gradient flow'
- 'small initialization'
- 'incremental rank learning'
- 'silent alignment'
- 'pointwise mutual information'
- 'analogy completion'
- 'linear representation hypothesis'
- 'spiked covariance model'
implementations: []
summary: >-
  Karkada, Simon, Bahri and DeWeese (2025), [ARXIV-2502.09863](https://arxiv.org/abs/2502.09863), NeurIPS 2025.
  The quartic approximation of word2vec's loss, under symmetric reweighting
  with constant aggregate weight, is exactly unweighted factorisation of
  M*, the co-occurrence matrix's relative deviation from independence, and
  from small initialisation gradient flow learns M*'s eigenvectors one at a
  time in sigmoidal steps. The embeddings this predicts match word2vec's
  features and benchmark scores far better than truncated PMI or PPMI
  factorisations do.
extends:
- LIT-242
---
<!-- inactive-ok-file: LIT-242 — Deferred: Simon et al.'s stepwise SSL paper, whose SimCLR observation this paper's Appendix D.2 explains; cited for the lineage, not as read -->
<!-- inactive-ok-file: THEORY-001 — Proposed; named as the record's account of the unconstrained contrastive optimum that this paper's rank-constrained result sits beside -->
<!-- inactive-ok-file: THEORY-009 — Proposed; named as the spectral self-supervised line this paper extends -->
<!-- inactive-ok-file: THEORY-tmpw5yp5 — Proposed; the account this reading produced -->

# LIT-tmp2n2m4: Closed-Form Training Dynamics Reveal Learned Features and Linear Structure in Word2Vec-like Models

Dhruva Karkada, James B. Simon, Yasaman Bahri and Michael R. DeWeese (2025),
*Advances in Neural Information Processing Systems 38* (NeurIPS 2025),
pp. 4507–4540 — [ARXIV-2502.09863](https://arxiv.org/abs/2502.09863) (first posted 14 February 2025 as *Solvable
Dynamics of Self-Supervised Word Embeddings and the Emergence of Analogical
Reasoning*)

## Key takeaways

- **The target is a deviation from independence.** With tied weights and
  the quartic Maclaurin approximation of the word2vec loss, the objective is
  (1/4)Σ G_ij (W Wᵀ − M*)²_ij + const, where
  M*_ij = (Ψ⁺P_ij − Ψ⁻P_iP_j) / (½(Ψ⁺P_ij + Ψ⁻P_iP_j)) and
  G_ij = Ψ⁺P_ij + Ψ⁻P_iP_j (Proposition 2). M* agrees with PMI to third
  order in its argument (Appendix D.1) but is bounded, |M*_ij| ≤ 2 when the
  two reweightings are equal, so least squares no longer over-weights
  rarely co-occurring pairs.
- **Which low-rank solution is learned.** When G is constant (Setting 3.1:
  symmetric Ψ⁺, Ψ⁻ with Ψ⁺P_ij + Ψ⁻P_iP_j = g), the problem is unweighted
  factorisation, and the global minima are the top-d eigenvectors of M*
  scaled by the square roots of their eigenvalues, up to a right orthogonal
  transformation (Theorem 1, by completing the square and Eckart–Young).
  For G of rank one the minimiser is also known (Proposition 2); for
  general G it is weighted low-rank approximation, which is NP-hard, and the
  paper does not treat it.
- **The order in which it is learned.** From aligned initialisation each
  singular value follows Saxe et al.'s sigmoid, s_k²(t) =
  s_k²(0)λ_k e^{λ_k t} / (λ_k + s_k²(0)(e^{λ_k t} − 1)), realised at
  τ_k = (1/λ_k) ln(λ_k/s_k²(0)) (Lemma 3.1, proved). From vanishing random
  initialisation, the embeddings first align silently with the eigenbasis
  and then follow the same steps (Result 3). Result 3 is derived by
  discarding off-diagonal couplings and checking that they stay small; the
  authors call it a conjecture to be made rigorous. Early stopping and small
  d therefore both limit the number of eigen-features, not their character.
- **It is a good proxy for word2vec.** On 2 billion Wikipedia tokens
  (V = 10,000, d = 200): Google analogies 68.0% for word2vec, 65.1% for the
  trained quadratic model, 66.3% for explicit factorisation of M*, 50.6% for
  truncated PPMI and 8.4% for truncated PMI. The leading principal
  directions of word2vec and the quadratic model are the same interpretable
  topics. An ablation shows the clean stepwise separation comes from the
  reweighting, not from the quartic approximation.
- **Analogy structure, empirically.** Difference vectors within a semantic
  class (male − female, verb − past tense) concentrate on a few
  eigen-features, and the spectrum of their Gram matrix looks like a
  Marchenko–Pastur bulk plus one spike, the mean difference vector. The
  spike's signal-to-noise ratio first rises and then falls as rank is
  added, and its maximum tracks analogy accuracy across classes. This part
  is observation with a manual fit, not theorem.

## Standing in the record

Filed on 2026-10-09 at the owner's request, with no stated context; it came
in a batch with arXiv 2509.24914, 2504.12916, 2205.10343 and 2410.17770. It
was read on its own merits ([NOTE-tmpiys9p](../notes.d/NOTE-tmpiys9p.md)), and the reading produces
[THEORY-tmpw5yp5](../theory.d/THEORY-tmpw5yp5.md).

It carries `anthology-candidate`: it is a theory of the training dynamics of
an ML algorithm, published at NeurIPS, of the kind the anthology holds
alongside word2vec ([ANTH-LIT-604](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-604.md)) and Levy and Goldberg ([ANTH-LIT-612](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-612.md)). It
stays here for now beside the record's spectral self-supervised line
([LIT-242](LIT-242.md), [THEORY-001](../theory.d/THEORY-001.md), [THEORY-009](../theory.d/THEORY-009.md)), which it extends to language data.
