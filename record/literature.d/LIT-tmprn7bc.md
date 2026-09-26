---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'Mutual Information Neural Estimation'
version: 1
tags:
- information-theory
- probabilistic-modeling
- representation-learning
- anthology-candidate
date: '2026-09-26'
published: '2018-01-12'
arxiv: '1801.04062'
first_author: 'Belghazi'
keywords:
- 'mutual information'
- 'Donsker-Varadhan representation'
- 'neural estimation'
- 'information bottleneck'
- 'GANs'
implementations: []
summary: >-
  Belghazi et al. (2018), [ARXIV-1801.04062](https://arxiv.org/abs/1801.04062). Mutual information is stated measure-theoretically as the expectation under the joint of log dP_XZ/d(P_X⊗P_Z), and its Donsker–Varadhan dual is tight exactly at T* = log dP/dQ + C, so a neural critic trained on the dual is a log Radon–Nikodym-derivative estimator.
---

# LIT-tmprn7bc: Mutual Information Neural Estimation

Mohamed Ishmael Belghazi, Aristide Baratin, Sai Rajeswar, Sherjil Ozair, Yoshua Bengio, Aaron Courville, R Devon Hjelm (2018), *Proceedings of the 35th International Conference on Machine Learning (ICML 2018), PMLR 80:531-540* — [ARXIV-1801.04062](https://arxiv.org/abs/1801.04062)

## Key takeaways

- Mutual information is stated measure-theoretically as the expectation under the joint of log dP_XZ/d(P_X⊗P_Z), and its Donsker–Varadhan dual is tight exactly at T* = log dP/dQ + C, so a neural critic trained on the dual is a log Radon–Nikodym-derivative estimator.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

The authors argue that mutual information between high-dimensional continuous variables can be estimated by gradient descent over neural networks. Their estimator, MINE, scales linearly with dimension and sample size, is trainable by backpropagation and is shown strongly consistent. They apply it to improve adversarially trained generative models and to the information bottleneck in supervised classification.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *Radon–Nikodym, density ratios and contrastive objectives* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: medium — the RN statement is fully captured by the skim; the estimator's statistical claims are superseded in part by rb1.**

What a deeper reading should check:

- This is the representation-learning paper that states MI as the expectation of a log Radon–Nikodym derivative in so many words — the link from Adler's coda ([LIT-243](LIT-243.md), Thm 5.1) to the bottleneck objective.
- Poole et al. (rb1, §2.2) note that the Monte-Carlo DV estimate MINE uses is neither an upper nor a lower bound; a deeper reading should check how §3 handles this and what "strongly consistent" is proved under.
- Read §5.3 to see whether the IB experiment is stated in the RN form or with densities.

Access when seeded: arXiv abs page (v1 submitted 12 Jan 2018; five versions) and the current arXiv PDF, text extracted; read abstract, §1 opening, §2.1–2.2 in full, section list, appendix 8.2.1 (Donsker–Varadhan proof) and the opening of 8.2.2. PMLR landing page (v80/belghazi18a) confirmed title and pages 531–540. §3–5 (estimator, bias correction, consistency, GAN and IB applications) not read beyond headings.
