---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'On Mutual Information Maximization for Representation Learning'
version: 1
tags:
- representation-learning
- information-theory
- anthology-candidate
date: '2026-09-26'
published: '2019-07-31'
arxiv: '1907.13625'
first_author: 'Tschannen'
keywords:
- 'mutual information'
- 'representation learning'
- 'InfoMax'
- 'InfoNCE'
- 'inductive bias'
- 'metric learning'
implementations: []
summary: >-
  Tschannen et al. (2019), [ARXIV-1907.13625](https://arxiv.org/abs/1907.13625). The success of InfoNCE-style representation learning cannot be attributed to mutual information itself: MI is invariant under invertible reparametrizations, invertible encoders that maximize true MI can be worse than raw pixels, and tighter MI bounds from higher-capacity critics can give worse representations.
---

# LIT-tmp0wgvt: On Mutual Information Maximization for Representation Learning

Michael Tschannen, Josip Djolonga, Paul K. Rubenstein, Sylvain Gelly, Mario Lucic (2019), *International Conference on Learning Representations (ICLR 2020)* — [ARXIV-1907.13625](https://arxiv.org/abs/1907.13625)

## Key takeaways

- The success of InfoNCE-style representation learning cannot be attributed to mutual information itself: MI is invariant under invertible reparametrizations, invertible encoders that maximize true MI can be worse than raw pixels, and tighter MI bounds from higher-capacity critics can give worse representations.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Many unsupervised and self-supervised methods train feature extractors by maximizing an estimate of mutual information between views. The authors point out that MI is hard to estimate and, being invariant under invertible transformations, can favour entangled representations. They argue with experiments that these methods' success depends strongly on the inductive biases of the encoder architecture and of the MI estimator's parameterization, not on MI, and connect InfoNCE to triplet losses from deep metric learning as a more plausible account.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *Radon–Nikodym, density ratios and contrastive objectives* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: high — the necessary counterweight to any THEORY claim that "contrastive learning works because it maximizes MI"; the skim captures the claims but not the evidence.**

What a deeper reading should check:

- It is the limit on what the density-ratio/MI reading buys: the optimal critic being a log RN derivative is a fact about the critic at the optimum, not an explanation of why the encoder's features are good.
- Check the §3 experiments' setups (which bounds, critics and datasets) before citing any specific number.

Access when seeded: arXiv abs page (v1 31 Jul 2019; v2 23 Jan 2020, comment "ICLR 2020") and the v2 PDF, text extracted; read abstract, §1, the contribution list in §2–3, and the opening of §4 (metric-learning view). The §3 experiments themselves (figures 1–2 captions aside) and the appendices not read.
