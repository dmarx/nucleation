---
number: tmp1zkcf
status: Rejected
status_note: 'read in full 2026-09-27 ([NOTE-tmp6uhuc](../notes.d/NOTE-tmp6uhuc.md)); not worth a reader''s time as a source. Its one sound calculation (the infinite-bond MPS is a linear model in a fixed product-kernel feature space, so its NTK is its GP kernel up to a constant) follows in a line from multilinearity. Tensor Programs II ([ANTH-LIT-557](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-557.md)) covers such architectures rigorously. The paper''s distinctive claims are the lazy-training proof, positive-definiteness "without any extra assumptions of the data set", and "over-fitting is naturally avoided". The first is circular, the second is false for the finite local dimensions it uses, and the third is contradicted by its own memorisation result.'
title: 'Neural Tangent Kernel of Matrix Product States: Convergence and Applications'
version: 2
history:
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (Full text of arXiv 2111.14046 v1 (the only version), from
    the arXiv PDF: 19 pp. I read the abstract, §§1–5, the references, and
    Appendices A (the GP limit), B (the NTK limit, lazy training,
    positive-definiteness) and C (the Born-machine partition function). The
    one figure is a schematic, seen only as its caption. `pdftotext` was not
    available in this session, so I extracted the text with PyMuPDF. Some
    equations came through garbled. Where an exponent was ambiguous (e.g.
    "2n−1"), I resolved it from the surrounding derivation and say so where
    it matters. I checked the Born-machine ODE solution numerically myself.
    The paper contains no numerics.); the first NOTE on it, since it was
    seeded from the abstract alone. Status set from the reading: Rejected.
tags:
- learning-theory
- probabilistic-modeling
- mathematics
date: '2026-09-27'
published: '2021-11-28'
arxiv: '2111.14046'
first_author: 'Guo'
keywords:
- 'neural tangent kernel'
- 'matrix product states'
- 'tensor networks'
- 'Gaussian process limit'
- 'Born machines'
- 'lazy training'
implementations: []
summary: >-
  Guo & Draper (2021), [ARXIV-2111.14046](https://arxiv.org/abs/2111.14046). In the sequential
  infinite-bond-dimension limit, with tensor variances
  σ_i²/√(|α_i||α_{i+1}|) and per-tensor learning rates
  (|α_i||α_{i+1}|)^{-1/2}, the NTK of a periodic MPS tends to K(x,x′)=Σ_k
  φ(x_k)·φ(x′_k) Π_{l≠k} σ_l² φ(x_l)·φ(x′_l). By my reduction this is (Σ_k
  σ_k⁻²) times the MPS's own GP covariance, so gradient flow is kernel
  regression with a fixed product kernel. The Born-machine solution
  P_x(t)=1/m−(1/m−P_x(0))e^{−4mKt/Z} is correct (I checked it; Z is in
  fact conserved). The lazy-training lemma is heuristic, the
  positive-definiteness "proof" shows at most semi-definiteness, several
  constants are off by factors of n or 2^{−n}, and there are no
  experiments.
---

# LIT-tmp1zkcf: Neural Tangent Kernel of Matrix Product States: Convergence and Applications

Guo & Draper (2021), *arXiv preprint* — [ARXIV-2111.14046](https://arxiv.org/abs/2111.14046)

## Standing in the record

Filed on 2026-09-27 at the owner's request. It is held here rather than in
the anthology because it is a theory paper with no experiments and nothing
for ML practice to act on; the anthology holds the NTK line it extends
([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md), [ANTH-LIT-557](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-557.md)). Only v1 exists, and no published version is
known.

It was filed `Deferred`, unread. [NOTE-tmp6uhuc](../notes.d/NOTE-tmp6uhuc.md) is the close reading of 2026-09-27, and it placed the work: **Rejected** — not worth a reader's time as a source. Its one sound calculation (the infinite-bond MPS is a linear model in a fixed product-kernel feature space, so its NTK is its GP kernel up to a constant) follows in a line from multilinearity. Tensor Programs II ([ANTH-LIT-557](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-557.md)) covers such architectures rigorously. The paper's distinctive claims are the lazy-training proof, positive-definiteness "without any extra assumptions of the data set", and "over-fitting is naturally avoided". The first is circular, the second is false for the finite local dimensions it uses, and the third is contradicted by its own memorisation result.
