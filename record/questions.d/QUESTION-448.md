---
number: 448
status: Open
formerly:
- QUESTION-tmp416y5
title: 'Where does the criterion that a faithful translation preserves the source''s distribution over communicative situations sit in the fidelity profile: is it one component of the profile, a weighting of several, or a rival to the profile; and does the divergence and tolerance it needs fix a ranking of failing renderings that the theory of fidelity is said not to fix?'
version: 1
tags:
- translation
- pragmatics
- information-theory
date: '2026-11-07'
line:
- pragmatic-transport
summary: >-
  A by-product of the third synthesis review of 2026-11-07. The reader of
  the pragmatic-transport cluster found the line's account of fidelity
  verdicts held by [TERM-043](../terms.d/TERM-043.md), [CLAIM-371](../claims.d/CLAIM-371.md) and [CLAIM-128](../claims.d/CLAIM-128.md), and tested by
  [CLAIM-220](../claims.d/CLAIM-220.md). One part was unplaced: where [CLAIM-111](../claims.d/CLAIM-111.md)'s criterion sits in
  [TERM-043](../terms.d/TERM-043.md)'s profile. [CLAIM-214](../claims.d/CLAIM-214.md) shows the criterion can fail every
  rendering. When it does, the choice of divergence orders the failures,
  and that seems to fix a ranking [CLAIM-128](../claims.d/CLAIM-128.md) says the theory does not fix.
  The wording is the assistant's (Claude, in this session); pursuing it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-111 CLAIM-128 CLAIM-220 — Proposed; the criterion, the task-relativity claim and the line's thesis, cited with their standing -->

# QUESTION-448: Where does the criterion that a faithful translation preserves the source's distribution over communicative situations sit in the fidelity profile: is it one component of the profile, a weighting of several, or a rival to the profile; and does the divergence and tolerance it needs fix a ranking of failing renderings that the theory of fidelity is said not to fix?

## Why it is a question

[TERM-043](../terms.d/TERM-043.md) makes fidelity a profile of distortions, adding that "a scalar
exists only once a task fixes weights". [CLAIM-128](../claims.d/CLAIM-128.md) says translations are
ranked only relative to a task, "and the theory of fidelity fixes no
weighting". [CLAIM-111](../claims.d/CLAIM-111.md) offers a criterion of another shape: a translation is
faithful by preserving the source's distribution over possible
communicative situations. The record has kept that factorization as a
"candidate explanatory model", not as a fidelity criterion. [TERM-043](../terms.d/TERM-043.md) places
several of the line's terms in the profile, but not this one.

So it is open whether the criterion is:

- one component of the profile, the decision-theoretic one over latent
  situations, say;
- a weighting of several components;
- a rival to the profile.

## Where it bites

[CLAIM-214](../claims.d/CLAIM-214.md) shows that the criterion can fail every rendering. When the source
conveys something by implicature that the target language cannot, no
rendering preserves the distribution. Comparing the failures needs a
divergence and a tolerance, and the criterion's "preserving" names neither.
The choice reverses orderings even over two situations.

Take a source posterior of (3/4, 1/4), [CLAIM-214](../claims.d/CLAIM-214.md)'s value, and two renderings
that do not preserve it:

| rendering | total variation | KL(P‖R) | KL(R‖P) |
|---|---|---|---|
| (0.50, 0.50) | 0.25 | 0.131 | 0.144 |
| (0.95, 0.05) | 0.20 | 0.225 | 0.144 |

Total variation ranks the second rendering better, and KL(P‖R) ranks the
first better. So either:

- the criterion fixes a ranking of failing renderings once its divergence
  is chosen, against [CLAIM-128](../claims.d/CLAIM-128.md); or
- the divergence is itself a task's weighting, which places the criterion
  inside the profile.

The figures are the reader's computation, checked by the filer.

## What would answer it

Any of these would answer it:

- a reason, from the criterion's own grounds, for one divergence over
  another;
- a showing that the choice of divergence is a task's weighting in
  [TERM-043](../terms.d/TERM-043.md)'s sense;
- a case where the criterion's verdicts and the profile's come apart for a
  fixed task.

It bears on [QUESTION-021](QUESTION-021.md), where [CLAIM-111](../claims.d/CLAIM-111.md) sits among the rival answers, and
on [QUESTION-005](QUESTION-005.md), which asks how responses can be operationalized without
building in the preferred notion of fidelity.
