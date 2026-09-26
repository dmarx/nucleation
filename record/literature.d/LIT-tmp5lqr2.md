---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'The Conditional Entropy Bottleneck'
version: 1
tags:
- representation-learning
- learning-theory
- information-theory
- anthology-candidate
date: '2026-09-26'
published: '2020-02-13'
arxiv: '2002.05379'
doi: '10.3390/e22090999'
first_author: 'Fischer'
keywords:
- 'Information theory'
- 'Machine Learning'
- 'Information Bottleneck'
implementations: []
summary: >-
  Fischer (2020), [ARXIV-2002.05379](https://arxiv.org/abs/2002.05379). Training a representation to minimize I(X;Z|Y) while maximizing I(Y;Z) — the Conditional Entropy Bottleneck, targeting the "Minimum Necessary Information" point I(X;Y)=I(X;Z)=I(Y;Z) — empirically improves accuracy, adversarial robustness, OoD detection and calibration and refuses to memorize random labels.
---

# LIT-tmp5lqr2: The Conditional Entropy Bottleneck

Ian Fischer (2020), *Entropy 22(9):999 (2020)* — [ARXIV-2002.05379](https://arxiv.org/abs/2002.05379)

## Key takeaways

- Training a representation to minimize I(X;Z|Y) while maximizing I(Y;Z) — the Conditional Entropy Bottleneck, targeting the "Minimum Necessary Information" point I(X;Y)=I(X;Z)=I(Y;Z) — empirically improves accuracy, adversarial robustness, OoD detection and calibration and refuses to memorize random labels.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Adversarial vulnerability, poor out-of-distribution detection, miscalibration and memorization of random labels are grouped as failures of "robust generalization". Fischer hypothesizes a common cause: models retain too much information about the training data. He proposes the Minimum Necessary Information (MNI) criterion for judging representations and a training objective, the Conditional Entropy Bottleneck, closely related to the Information Bottleneck, that targets it. Experiments comparing CEB with deterministic and Variational IB models across datasets and robustness challenges give strong empirical support for the hypothesis.

## Standing in the record

Filed on 2026-09-26 at the owner's request, from a list they grouped under the heading *Relating K-complexity to minimum sufficient statistics*. `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: high — directly states the minimal-sufficient-representation criterion as a training objective, and carries both a practice and a theory claim worth filing separately.**

What a deeper reading should check:

- MNI is an operational version of a minimal sufficient statistic for the label — directly on the heading's theme; a deeper reading should check how the paper relates MNI to sufficiency formally, if it does.
- Separate the practice claim (use CEB as a training objective) from the theory claim (robustness failures are caused by excess retained information); the second is hypothesized and supported only empirically — candidates for a SOTA and a THEORY filed apart.
- Check whether results replicate beyond Fashion-MNIST/CIFAR-10 and whether CEB is used in practice today.

Access when seeded: arXiv abs page (v1 2020-02-13, only version) and v1 PDF read for §1–§5 and §8, appendix A opening; Semantic Scholar API for the corpus-id match (CorpusID 86765551, DOI, PMC7597329); Europe PMC for the journal record (electronic publication 2020-09-08, keywords as listed). The Entropy version itself was not read and may differ from arXiv v1. Earlier appearance: an anonymous ICLR 2019 blind submission with the same title exists on OpenReview (forum rkVOXhAqY7, created 2018-09-27); I did not read it and its authorship is not shown, so `published:` uses the arXiv v1 date of this text.
