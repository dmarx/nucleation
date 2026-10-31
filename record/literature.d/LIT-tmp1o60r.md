---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmp5ibkm](../notes.d/NOTE-tmp5ibkm.md)), with the main proofs; worth
  reading for the precise
  sense in which evidence must precede commitment: the observation a
  committing action produces cannot justify it, and bounded information
  before commitment leaves a fixed fraction of the oracle gap to every
  uniformly safe controller ([THEORY-tmp78ls3](../theory.d/THEORY-tmp78ls3.md)). It also proves the
  positive case, safe recovery from a repeatable informative experiment,
  and shows certainty equivalence failing at an active constraint
  ([THEORY-tmp7plj0](../theory.d/THEORY-tmp7plj0.md)).
title: 'When Can Safe Controllers Adapt? Information before Commitment'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A20 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2026-07-18). The summary follows the abstract and A20's
    description. The summary follows the abstract and the exchange's
    description; a reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read from arXiv 2607.16895v1 (the only version), 45 pp., in
    NOTE-tmp5ibkm; status Deferred → Active. The citation stands. The
    summary is rewritten from the text. The old one was right in
    substance; it now says that the fraction is of the gap reachable only
    by committing, that the bound comes with the evidence threshold
    log(1/(2α)), and that the paper also proves recovery and partial
    adaptation by certified lists. The duplicated sentence in the first
    history note is left as filed.
    Tagged control-theory first (ADR-066).
tags:
- control-theory
- mathematics
- learning-theory
date: '2026-10-31'
published: '2026-07-18'
arxiv: '2607.16895'
first_author: 'Saligrama'
keywords:
- 'safe control'
- 'adaptation'
- 'information before commitment'
- 'oracle gap'
- 'uniform chance safety'
- 'stopping time'
- 'recursive feasibility'
- 'confidence sequences'
implementations: []
summary: >-
  Saligrama (2026). A safe adaptive controller must stay safe under every
  model not yet ruled out. Its first action that leaves no safe
  continuation under an alternative is a commitment, and the observation
  that action produces comes too late to justify it. With the information
  before commitment measured as a KL divergence between stopped records,
  every uniformly safe policy forfeits at least about ½e^{−I} of the value
  reachable only by committing. Acting on an exclusion at risk α needs
  about log(1/(2α)) nats beforehand. Bounded information and a linear gap
  give linear regret, shown for a headroom-limited device and for
  constrained linear regulation. Finite information can still certify a
  smaller candidate list. Safe recovery at O(√(T log T)) holds when a safe
  experiment is repeatable, informative and returns to a common state.
---
<!-- inactive-ok-file: QUESTION-285 — Open; the question of inquiry this bears on, cited as open -->

# LIT-tmp1o60r: When Can Safe Controllers Adapt? Information before Commitment

Saligrama, V. (2026). When can safe controllers adapt? Information before commitment. arXiv:2607.16895.

Read in full in [NOTE-tmp5ibkm](../notes.d/NOTE-tmp5ibkm.md).

## Why this is here

A20 §11 used it for the condition that inquiry needs information gathered
before a correction is committed to: a discrepancy that cannot be
distinguished in time cannot be corrected, whatever the update rule. It
bears on [CLAIM-312](../claims.d/CLAIM-312.md) and [TERM-085](../terms.d/TERM-085.md)'s deadline. The reading bears A20's use
out and makes it exact. The floor on the evidence needed before the
deadline is about log(1/(2α)) nats, and evidence that the corrective act
itself would generate does not count ([THEORY-tmp78ls3](../theory.d/THEORY-tmp78ls3.md)). Changing the
estimator cannot help; changing the experiment, the sensor (a persistent
imprint rather than a transient signal) or the degree of specialization
can. The "guarantee or exclude" choice, staying safe under every live
alternative at a price fixed by information, bears on [CLAIM-tmp025xj](../claims.d/CLAIM-tmp025xj.md) and
[QUESTION-285](../questions.d/QUESTION-285.md).
