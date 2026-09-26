---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Kernel Mean Embedding of Distributions: A Review and Beyond'
version: 1
tags:
- probabilistic-modeling
- mathematics
- learning-theory
- anthology-candidate
date: '2026-09-26'
published: '2016-05-31'
arxiv: '1605.09522'
doi: '10.1561/2200000060'
first_author: 'Muandet'
keywords:
- 'kernel mean embedding'
- 'reproducing kernel Hilbert space'
- 'maximum mean discrepancy'
- 'characteristic kernels'
- 'covariance operators'
implementations: []
summary: >-
  Muandet et al. (2016), [ARXIV-1605.09522](https://arxiv.org/abs/1605.09522). Point evaluation is bounded on an RKHS, so the Riesz theorem gives the reproducing kernel k_x. Likewise, when E√k(X,X) < ∞ the expectation functional f ↦ E_P f is bounded, so Riesz gives a unique mean embedding μ_P with E_P f = ⟨f, μ_P⟩. MMD is then the RKHS distance ‖μ_P − μ_Q‖, and it separates distributions exactly when the kernel is characteristic.
---

# LIT-tmpyrhlj: Kernel Mean Embedding of Distributions: A Review and Beyond

Krikamol Muandet, Kenji Fukumizu, Bharath Sriperumbudur, Bernhard Schölkopf (2016), *Foundations and Trends in Machine Learning 10(1–2):1–141 (2017); first appeared as arXiv preprint* — [ARXIV-1605.09522](https://arxiv.org/abs/1605.09522)

## Key takeaways

- Point evaluation is bounded on an RKHS, so the Riesz theorem gives the reproducing kernel k_x. Likewise, when E√k(X,X) < ∞ the expectation functional f ↦ E_P f is bounded, so Riesz gives a unique mean embedding μ_P with E_P f = ⟨f, μ_P⟩. MMD is then the RKHS distance ‖μ_P − μ_Q‖, and it separates distributions exactly when the kernel is characteristic.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

A kernel mean embedding maps a probability distribution into a reproducing kernel Hilbert space, so that kernel methods can be applied to distributions themselves. It generalizes the feature map used by SVMs and other kernel machines. The survey introduces positive-definite kernels and RKHSs, treats the embedding of marginal distributions (theory, estimation, applications such as two-sample and independence testing and learning on distributional data), then conditional distributions (graphical models, probabilistic inference, reinforcement learning, causal discovery). It closes with open problems.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *Riesz, reproducing kernels and spectral representation learning* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: medium — the load-bearing statements (Thm 2.4, Prop. 2.1, Thm 2.5, Lemma 3.1, MMD identity) are captured; the rest is a broad survey to consult rather than read through.**

What a deeper reading should check:

- It is the one held text that runs the whole chain Riesz → k_x → Moore–Aronszajn → μ_P → MMD/HSIC in numbered statements. That makes it the natural citation for the claim that "Riesz makes kernels exist".
- For SSL: any objective written as E k(z,z′) over pairs is a squared norm or inner product of mean embeddings. SSL-HSIC (ra6) makes this explicit. A deeper read of §3.6 (HSIC) should supply the operator-level statements.
- Check §5, the relation to other methods, for anything on learned (non-fixed) kernels. Every result here assumes a fixed k, whereas SSL learns the feature map.

Access when seeded: arXiv abs page (v1 submitted 2016-05-31, v4 2020-12-13, comment "147 pages; this is the final version", DOI shown) and the full v4 PDF (147 pp.) read via pymupdf text extraction: contents, §1.2, §2.2 (Def. 2.4, Thm 2.4, Prop. 2.1, Thm 2.5), Thm 2.1, §3.1 (Lemma 3.1), §3.2 (eqs. 3.14–3.16), §3.3.1 (Def. 3.2), §3.5 opening. Crossref (no contact parameter sent) gives the journal version as vol. 10, issue 1–2, pp. 1–141, published 2017-06-28.
