---
number: 10
status: Open
formerly:
- QUESTION-tmpayxxf
title: 'Can a reconstruction chain preserve information sufficient for one family of pragmatic tasks while progressively destroying the relations needed to support another?'
version: 4
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
- version: 4
  date: '2026-11-15'
  note: >-
    The assistant's design note added: matched training worlds tell
    information that survived an erasure from information rebuilt
    downstream. No other change.
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

<!-- inactive-ok-file: THEORY-1888 THEORY-1870 NOTE-1958 THEORY-1886 THEORY-199 — Proposed or Skimmed; the erasure readings of 2026-11-15 and the earlier partial answer, cited as bearing on the chain form, none answers it -->

Two readings of 2026-11-15 bear on the chain form of this question. Neither answers it.

- **Elazar et al. (2021), §7.1** ([LIT-2621](../literature.d/LIT-2621.md), [THEORY-1888](../theory.d/THEORY-1888.md)). Coarse POS information removed by INLP at one of BERT's first seven layers is "highly recoverable in subsequent layers". The word-prediction cost is 5.72–12.69 points there, against 16.57–46.39 in the second half. This is the reverse of the question's direction: a chain can restore what one of its steps erased, from correlates left behind. The masked setting reverses the layer trend.
- **Fel, Kowal et al. (2026), §6** ([LIT-2620](../literature.d/LIT-2620.md), [THEORY-1870](../theory.d/THEORY-1870.md)). Under a fixed projection at one layer, with training continued, the concept regrows along "the direction the head already uses to read the core features". A refit made early in the rebuild then removes core directions, and "accuracy falls close to chance". This is a chain, in depth and in training time, where what is kept for one task and what is destroyed for another trade places. It is a learning dynamic, not a fixed reconstruction chain, and the paper was skimmed ([NOTE-1958](../notes.d/NOTE-1958.md)).

Kumar, Tan & Sharma ([LIT-2653](../literature.d/LIT-2653.md), [THEORY-1886](../theory.d/THEORY-1886.md)) give a third one-step case, beside [THEORY-281](../theory.d/THEORY-281.md) and [THEORY-199](../theory.d/THEORY-199.md). Removal aimed at a concept destroys a main task that shares its directions. All three readings use learned, mostly linear operators. None poses two task families with relations, as the question asks. No status change.

## Note of 2026-11-15: telling survival from rebuilding after an erasure
<!-- inactive-ok-file: CASE-274 — Proposed or new; the study and the readings this note is about -->

The readings noted above share one ambiguity. Elazar et al. find a property erased at one layer and decodable again downstream ([THEORY-1888](../theory.d/THEORY-1888.md)). Fel, Kowal et al. find a concept re-encoded under shaping ([THEORY-1870](../theory.d/THEORY-1870.md)). Neither can say whether the information survived the erasure or was rebuilt from other retained information. That difference is exactly what this question needs.

The assistant's suggestion: use matched training worlds, as [CASE-274](../cases.d/CASE-274.md) does. Train twins that differ only in the target association. If a downstream reader, fitted after the erasure, recovers the world-specific value, the twin trained on the other value supplying the contrast, then the target survived. If it recovers only what the rest of the input implies, it was rebuilt. This is cheap to add to the study. Not run. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-22: the matched worlds, run in a toy
<!-- inactive-ok-file: CASE-tmprir2y CLAIM-tmp2eemo CLAIM-tmpqvkag — new; the run of LEAD-043 and the claims filed from it -->

[LEAD-043](../leads.d/LEAD-043.md)'s toy-scale run ([CASE-tmprir2y](../cases.d/CASE-tmprir2y.md)) used the twins this question's note of 2026-11-15 proposed: each model has a twin trained on a world that differs only in the target facts' values. Two things came of it. With random facts nothing else implies a target value, so recovery above the twin's rate is survival, not rebuilding; by that test, facts fine-tuned away by unlearning, overwriting or an unrelated task mostly survived ([CLAIM-tmp2eemo](../claims.d/CLAIM-tmp2eemo.md)). And the twin was needed: a battery of eleven readers recovered a value the twin never held in 28 to 46 percent of facts, so any-reader tests without it would have overstated survival ([CLAIM-tmpqvkag](../claims.d/CLAIM-tmpqvkag.md)). The toy has one chain step and one task family, so it does not answer the question. No status change.
