---
status: Active
status_note: >-
  read 2026-10-21 ([NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md)) in full, from arXiv:2002.10689v1, the ICLR 2020 camera-ready; worth reading as the usable-information literature the record lacked: it defines predictive V-information, the information a predictor restricted to a family V can extract, shows that computation can create it (so the data-processing inequality fails for it), and bounds its estimation error by the Rademacher complexity of V ([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md), [THEORY-tmp9m1g4](../theory.d/THEORY-tmp9m1g4.md)). Read it knowing that the failure of the data-processing inequality is shown by informal examples (decryption, feature learning), not by a theorem, that V-information is not bounded by Shannon information unless V's input-free predictions include the true marginal (the record's counterexample, [THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)), that Proposition 1.2's "mean absolute deviation" is the deviation about the geometric median, and that the experiments are small.
title: 'A Theory of Usable Information Under Computational Constraints'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed at the owner's request ("also this one: https://arxiv.org/abs/2002.10689"), in the exchange of 2026-10-20/21. Citation checked against arXiv on 2026-10-21: v1 submitted 25 February 2020, the only version, with the comment "ICLR 2020 (Talk)". `published:` is that date, per ADR-002. Crossref returned no DOI for the title. Flagged `anthology-candidate` as a machine-learning paper the anthology may want; it carries no instruction for ML practice. CLAIM-199 says the usable-information literature is not held; this is that literature's founding paper.
- version: 2
  date: '2026-10-21'
  note: >-
    Read in full the same day (NOTE-tmpvnsxo), from the arXiv PDF, text extracted with pdftotext. Status Deferred → Active. The summary is checked against the reading and kept, with the asymmetry and estimation results added.
tags:
- information-theory
- learning-theory
- anthology-candidate
date: '2026-10-21'
published: '2020-02-25'
arxiv: '2002.10689'
first_author: 'Xu'
keywords:
- 'predictive V-information'
- 'usable information'
- 'computational constraints'
- 'data processing inequality'
- 'PAC estimation'
- 'structure learning'
- 'fair representation learning'
implementations: []
summary: >-
  Xu, Zhao, Song, Stewart & Ermon (2020). Predictive V-information, H_V(Y) − H_V(Y | X) with the conditional entropies taken as the least expected log loss over a predictive family V, is the information about Y that a predictor restricted to V can use. It recovers Shannon mutual information when V is unrestricted and the coefficient of determination for linear-Gaussian V, is non-negative and zero under independence, can be asymmetric, can be raised by computing on X, and can be estimated with PAC guarantees from the Rademacher complexity of V.
---
<!-- inactive-ok-file: CLAIM-199 CLAIM-081 — Proposed; the claims this reading bears on, cited as open -->
# LIT-tmp07k7g: A Theory of Usable Information Under Computational Constraints

Xu, Y., Zhao, S., Song, J., Stewart, R. & Ermon, S. (2020). A Theory of Usable Information Under Computational Constraints. *International Conference on Learning Representations* (ICLR 2020). arXiv:2002.10689 (25 February 2020).

Read 2026-10-21 in full, in [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md). The summary was checked against
the reading.

## Why this is here

The owner asked for it in the exchange of 2026-10-20/21: "get started reading the proposed works. also this one: https://arxiv.org/abs/2002.10689". It is the usable-information literature that [CLAIM-199](../claims.d/CLAIM-199.md) says the record does not hold ("the literature on usable information is not held here"), and [TERM-tmp5lqn0](../terms.d/TERM-tmp5lqn0.md) repeats the gap. Its V-information is [CLAIM-199](../claims.d/CLAIM-199.md)'s "best risk over the rules in a class the receiver can apply" under log loss, with the risk turned into an information. It bears on [CLAIM-225](../claims.d/CLAIM-225.md), [CLAIM-081](../claims.d/CLAIM-081.md) and [CLAIM-270](../claims.d/CLAIM-270.md), on [QUESTION-110](../questions.d/QUESTION-110.md) and [QUESTION-111](../questions.d/QUESTION-111.md), and on [CLAIM-304](../claims.d/CLAIM-304.md)'s computational case.
