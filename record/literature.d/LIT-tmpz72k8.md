---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'A Generalized Representer Theorem'
version: 1
tags:
- learning-theory
- mathematics
date: '2026-09-26'
published: '2001-09-13'
doi: '10.1007/3-540-44581-1_27'
first_author: 'Schölkopf'
keywords:
- 'representer theorem'
- 'reproducing kernel Hilbert space'
- 'regularized risk'
- 'kernel methods'
- 'support vector expansion'
implementations: []
summary: >-
  Schölkopf et al. (2001), DOI-10.1007/3-540-44581-1_27. For any strictly increasing regularizer g(‖f‖) and any (even non-convex, coupled) cost on the training outputs, every RKHS minimizer of c((x_i,y_i,f(x_i))_i) + g(‖f‖) is a finite kernel expansion f = Σ α_i k(·,x_i). The proof needs only the reproducing property and orthogonal decomposition onto span{k(·,x_i)}, not the Riesz theorem.
---

# LIT-tmpz72k8: A Generalized Representer Theorem

Bernhard Schölkopf, Ralf Herbrich, Alex J. Smola (2001), *Computational Learning Theory (COLT/EuroCOLT 2001), Lecture Notes in Artificial Intelligence 2111, Springer, pp. 416–426* — DOI-10.1007/3-540-44581-1_27

## Key takeaways

- For any strictly increasing regularizer g(‖f‖) and any (even non-convex, coupled) cost on the training outputs, every RKHS minimizer of c((x_i,y_i,f(x_i))_i) + g(‖f‖) is a finite kernel expansion f = Σ α_i k(·,x_i). The proof needs only the reproducing property and orthogonal decomposition onto span{k(·,x_i)}, not the Riesz theorem.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Wahba's representer theorem says that solutions of certain regularized empirical risk problems with a quadratic regularizer are expansions in kernel functions centred on the training points. The authors generalize it to a larger class of regularizers and risk terms and give a short self-contained proof in the feature space of the kernel. The result shows that many learning problems posed in possibly infinite-dimensional RKHSs have optimal solutions in the finite-dimensional span of the mapped training data, which is what makes kernel algorithms computable.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *Riesz, reproducing kernels and spectral representation learning* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: low — short and fully captured by this skim; cite it for the theorem and read a textbook for the modern general form.**

What a deeper reading should check:

- It corrects a natural overstatement: the representer theorem rests on the reproducing property plus orthogonal projection. Riesz is what runs the other direction, from a Hilbert space with bounded evaluations to a kernel (ra4, Prop. 2.1). The chain "Riesz → RKHS → representer theorem" is right only if the RKHS is given abstractly rather than built from k.
- Example 5 (kernel PCA) is the bridge to SSL. Johnson et al. (ra2) and [LIT-242](LIT-242.md) both land on kernel PCA, and [LIT-242](LIT-242.md)'s Prop. 5.1(c) characterizes the SSL solution as a minimum-RKHS-norm interpolant with a finite kernel expansion, i.e. representer-theorem-shaped.
- Note that the class F in Thm 1 is the set of countable kernel expansions with finite norm, not stated as the full completed RKHS. A deeper read (or a textbook) should confirm the extension to the full H_k.

Access when seeded: Read the full 11-page paper as published (Springer LNAI footer) from the author-hosted PDF at alex.smola.org/papers/2001/SchHerSmo01.pdf, via pymupdf text extraction: §1.1–1.2, Thm 1 and its proof, Thm 2, Remark 1, Examples 1–5, §3. Springer's chapter page gives the DOI and pp. 416–426 and "First Online: 01 January 2001", which looks like a placeholder. Crossref gives published-online 2001-09-13, used here. The COLT 2001 meeting itself was presumably earlier in 2001, but its date is unverified.
