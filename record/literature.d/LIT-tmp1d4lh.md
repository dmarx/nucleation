---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Self-Supervised Learning with Kernel Dependence Maximization'
version: 1
tags:
- representation-learning
- probabilistic-modeling
- anthology-candidate
date: '2026-09-26'
published: '2021-06-15'
arxiv: '2106.08320'
first_author: 'Li'
keywords:
- 'self-supervised learning'
- 'Hilbert-Schmidt Independence Criterion'
- 'InfoNCE'
- 'maximum mean discrepancy'
- 'kernel dependence'
implementations: []
summary: >-
  Li et al. (2021), [ARXIV-2106.08320](https://arxiv.org/abs/2106.08320). With image identity as the label, the SSL-HSIC loss −HSIC(Z,Y) + γ√HSIC(Z,Z) has a dependence term that is proportional to the average squared MMD between the per-image distributions of augmented-view representations (App. B.2). InfoNCE approximates the same term plus a variance penalty (eq. 7), so contrastive SSL separates the kernel mean embeddings of each image's view distribution.
---

# LIT-tmp1d4lh: Self-Supervised Learning with Kernel Dependence Maximization

Yazhe Li, Roman Pogodin, Danica J. Sutherland, Arthur Gretton (2021), *Advances in Neural Information Processing Systems 34 (NeurIPS 2021); first appeared as arXiv preprint* — [ARXIV-2106.08320](https://arxiv.org/abs/2106.08320)

## Key takeaways

- With image identity as the label, the SSL-HSIC loss −HSIC(Z,Y) + γ√HSIC(Z,Z) has a dependence term that is proportional to the average squared MMD between the per-image distributions of augmented-view representations (App. B.2). InfoNCE approximates the same term plus a variance penalty (eq. 7), so contrastive SSL separates the kernel mean embeddings of each image's view distribution.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The paper treats self-supervised learning as dependence maximization. It proposes SSL-HSIC, which maximizes the Hilbert–Schmidt Independence Criterion between representations of transformed images and the image's identity while penalizing the kernelized variance of the representations. This reframes InfoNCE, usually read as a mutual-information bound, as implicitly approximating SSL-HSIC with a slightly different regularizer. It also sheds light on negative-free BYOL. The loss is estimated directly from mini-batches in time linear in batch size via random Fourier features, and it matches the state of the art on ImageNet linear evaluation and on transfer tasks.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *Riesz, reproducing kernels and spectral representation learning* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: medium — the MMD/mean-embedding identity is captured exactly; the InfoNCE approximation's conditions and the BYOL argument need the appendix.**

What a deeper reading should check:

- It is the published statement that makes an SSL objective literally a function of kernel mean embeddings, closing the loop from Riesz via Lemma 3.1 of ra4 to "SSL spreads distributions".
- The InfoNCE ≈ HSIC link is a Taylor approximation in a small-variance regime, not an identity. A deeper read of App. B.1 should state its conditions before anyone cites it as an equivalence.
- The paper's kernels act on the learned representation Z (a fixed kernel on features), not on inputs. Compare this with Johnson et al. (ra2), where the kernel learned is the positive-pair kernel on inputs.

Access when seeded: arXiv abs page (v1 submitted 2021-06-15, v2 2021-12-02) and the full v2 PDF (26 pp., footer "35th Conference on Neural Information Processing Systems (NeurIPS 2021)") read via pymupdf text extraction: abstract, §1, §2.2 (eqs. 1–3), §3 (eqs. 4–10), App. B.2, App. C.1. No DOI found.
