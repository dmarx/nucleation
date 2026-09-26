---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'The Hidden Uniform Cluster Prior in Self-Supervised Learning'
version: 1
tags:
- representation-learning
- probabilistic-modeling
- anthology-candidate
date: '2026-09-26'
published: '2022-10-13'
arxiv: '2210.07277'
first_author: 'Assran'
keywords:
- 'self-supervised learning'
- 'volume maximization'
- 'uniform prior'
- 'class imbalance'
- 'Masked Siamese Networks'
implementations: []
summary: >-
  Assran et al. (2022), [ARXIV-2210.07277](https://arxiv.org/abs/2210.07277). Joint-embedding SSL methods that rely on mini-batch volume maximization (SimCLR, VICReg, SwAV, MSN) implicitly impose a prior toward features that cluster the data into equal-sized groups, which hurts on class-imbalanced data; replacing it with a power-law prior (PMSN) improves representations on long-tailed data.
---

# LIT-tmpc3f51: The Hidden Uniform Cluster Prior in Self-Supervised Learning

Mahmoud Assran, Randall Balestriero, Quentin Duval, Florian Bordes, Ishan Misra, Piotr Bojanowski, et al. (2022), *International Conference on Learning Representations (ICLR 2023, poster)* — [ARXIV-2210.07277](https://arxiv.org/abs/2210.07277)

## Key takeaways

- Joint-embedding SSL methods that rely on mini-batch volume maximization (SimCLR, VICReg, SwAV, MSN) implicitly impose a prior toward features that cluster the data into equal-sized groups, which hurts on class-imbalanced data; replacing it with a power-law prior (PMSN) improves representations on long-tailed data.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Many successful self-supervised pretraining methods use tasks built on mini-batch statistics. The authors argue that all of these formulations carry an overlooked prior toward learning features that split the data into uniformly sized clusters. That prior suits class-balanced data like ImageNet but hampers learning on class-imbalanced data. They extend Masked Siamese Networks to accept arbitrary feature priors and show that a power-law prior improves representation quality on real-world long-tailed datasets.

## Standing in the record

Filed on 2026-09-26 at the owner's request, from a list they grouped under the heading *Representation learning as a spectral approximation*. `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: medium — the mechanism is captured by the skim; a deeper read would be for the PMSN results table and the SimCLR assumptions.**

What a deeper reading should check:

- Gives a cluster/probabilistic reading of SSL regularizers that complements the spectral reading of k17; together they say what the "collapse-prevention" term actually commits the representation to.
- Practice implication: SSL on long-tailed or uncurated data may want a non-uniform prior; check §5.2 gains on iNat18 and how the power-law exponent is chosen without labels.
- Check how strong the "limited assumptions" for SimCLR are.

Access when seeded: arXiv abs page (v1 only, submitted 2022-10-13) and full PDF v1 read via pymupdf text extraction; ICLR 2023 poster acceptance confirmed via OpenReview API search (note 04K3PMtMckp, venue "ICLR 2023 poster"). No DOI found. Full author list (9): Assran, Balestriero, Duval, Bordes, Misra, Bojanowski, Vincent, Rabbat, Ballas.
