---
number: 10
status: Open
formerly:
- QUESTION-tmpayxxf
title: 'Can a reconstruction chain preserve information sufficient for one family of pragmatic tasks while progressively destroying the relations needed to support another?'
version: 3
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Split under ADR-049. The one-step, information-theoretic form for one
    categorical concept, how much a map can keep about X while keeping
    nothing about A, is QUESTION-249, Answered by THEORY-281. The
    title is unchanged: it asks about chains and relations, which that
    answer does not reach.
- version: 3
  date: '2026-11-15'
  note: >-
    Note of 2026-11-15 added: Elazar et al. §7.1 (a chain restoring what one
    step erased) and Fel, Kowal et al. §6 (a concept regrowing along the
    readout's core directions, so a refit destroys the core task) bear on
    the chain form of the question; Kumar, Tan & Sharma give a third
    one-step case. None poses two task families with relations. The question
    is unchanged.
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-016
summary: >-
  A100, Chapter 9: "The new question introduced by the sheaf-information
  synthesis." Gestured at in the manuscript (§8, §11), not posed. Its
  one-step form for one categorical concept is [QUESTION-249](QUESTION-249.md),
  Answered by [THEORY-281](../theory.d/THEORY-281.md). Chains, and relations, are open.
---
<!-- inactive-ok-file: CLAIM-128 CLAIM-129 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# QUESTION-010: Can a reconstruction chain preserve information sufficient for one family of pragmatic tasks while progressively destroying the relations needed to support another?

## Why it is a question

A100, Chapter 9: "**The new question introduced by the sheaf-information
synthesis:** Can a chain preserve information sufficient for one family of
pragmatic tasks while progressively destroying the relations needed to support
another?" It is the task-relative form of [QUESTION-016](QUESTION-016.md), and the decision-theoretic
twin of [CLAIM-105](../claims.d/CLAIM-105.md).

## Where it stands

The manuscript §11: "Task sufficiency may be retained while historical detail is
lost"; §8: the trajectories of invariants, decision risks and compatibility
structures "need not coincide". Neither poses the question for two task families
at once.

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [CLAIM-129](../claims.d/CLAIM-129.md): A factorization recovers only the structure visible in the
  relations it is fitted to, so a topic can…
- [CLAIM-128](../claims.d/CLAIM-128.md): Transports whose distortion profiles trade off are
  incomparable until a task fixes weights, so no single…
- [CLAIM-031](../claims.d/CLAIM-031.md): A reconstruction chain reorganizes observational constraints
  rather than only accumulating metric error: a…
- [CLAIM-177](../claims.d/CLAIM-177.md): An argument developed with collaborators who keep no memory
  fails at identity, not at structure: concepts…

[CLAIM-177](../claims.d/CLAIM-177.md) is a documented case from the nucleating-argument line: a label
("will") kept while its definition changed five or more times.

## Note of 2026-10-12: a typed partial answer

[THEORY-199](../theory.d/THEORY-199.md) now carries an `answered_by` edge. Low-level features survive past the noise threshold at which the top-level class is lost: one task family is kept while another is destroyed. Limits: it is a single step, not a chain, and an ideal denoiser on a synthetic grammar.

## Note of 2026-10-14: a second one-step partial answer

[THEORY-281](../theory.d/THEORY-281.md), filed from [LIT-963](../literature.d/LIT-963.md), answers the one-step, information-theoretic form for one categorical concept: perfect erasure of a concept A caps what a representation keeps about X at H(X|A). Everything about A can be destroyed while that much is kept, and no more. Limits: one step, not a chain, and task families defined only by a categorical concept.

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** [THEORY-281](../theory.d/THEORY-281.md) is now Active, narrowed to X
of finite support. Its answer, the cap H(X|A) and when a map reaches it,
is [QUESTION-249](QUESTION-249.md), Answered. This question keeps what it leaves: a
chain rather than one step, and relations a task family needs rather than
a categorical label. [THEORY-199](../theory.d/THEORY-199.md) (Proposed) still points here.

## Note of 2026-11-15: erasure along a network, Elazar §7.1 and Goodfire §6

<!-- inactive-ok-file: THEORY-tmpi5d5l THEORY-tmp2ly83 NOTE-tmp88irq THEORY-tmpfrtac THEORY-199 — Proposed or Skimmed; the erasure readings of 2026-11-15 and the earlier partial answer, cited as bearing on the chain form, none answers it -->

Two readings of 2026-11-15 bear on the chain form of this question. Neither answers it.

- **Elazar et al. (2021), §7.1** (LIT-tmp52idf, THEORY-tmpi5d5l). Coarse POS information removed by INLP at one of BERT's first seven layers is "highly recoverable in subsequent layers". The word-prediction cost is 5.72–12.69 points there, against 16.57–46.39 in the second half. This is the reverse of the question's direction: a chain can restore what one of its steps erased, from correlates left behind. The masked setting reverses the layer trend.
- **Fel, Kowal et al. (2026), §6** (LIT-tmp40uoi, THEORY-tmp2ly83). Under a fixed projection at one layer, with training continued, the concept regrows along "the direction the head already uses to read the core features". A refit made early in the rebuild then removes core directions, and "accuracy falls close to chance". This is a chain, in depth and in training time, where what is kept for one task and what is destroyed for another trade places. It is a learning dynamic, not a fixed reconstruction chain, and the paper was skimmed (NOTE-tmp88irq).

Kumar, Tan & Sharma (LIT-tmpzdaep, THEORY-tmpfrtac) give a third one-step case, beside THEORY-281 and THEORY-199. Removal aimed at a concept destroys a main task that shares its directions. All three readings use learned, mostly linear operators. None poses two task families with relations, as the question asks. No status change.
