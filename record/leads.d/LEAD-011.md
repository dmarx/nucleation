---
number: 11
status: Open
formerly:
- LEAD-tmpxn781
title: 'Show which assumptions are needed for a scalar optimum of learning to exist when what is learned changes what can later be learned'
version: 1
stage: idea
method:
- formal
- conceptual
tags:
- learning-theory
- epistemology
date: '2026-11-19'
line:
- learned-structure
advances:
- QUESTION-495
summary: >-
  ChatGPT's next advance for [QUESTION-495](../questions.d/QUESTION-495.md) without an experiment (A84),
  beside [CLAIM-754](../claims.d/CLAIM-754.md)'s point that no context-free scalar ranks learners.
---
<!-- inactive-ok-file: CLAIM-754 — Proposed or newly filed; cited in this filing of 2026-11-19 -->

# LEAD-011: Show which assumptions are needed for a scalar optimum of learning to exist when what is learned changes what can later be learned

## What it would do

State the conditions (a fixed task distribution, resource costs, a
horizon, a valuation) under which an optimal learning policy is well
defined, and show which fail when the learner's own learning changes the
tasks it will face.

## Note of 2026-11-23: the lead run
<!-- inactive-ok-file: CLAIM-tmpy87xn CLAIM-tmp6ppvo CLAIM-tmpl9022 ARG-tmpi8mhy — new; filed by the lead run of 2026-11-23 -->

Not held before: no claim stated the conditions or a counterexample.
Filed, all Proposed and demonstrated:

- CLAIM-tmpy87xn (thesis): four sufficient conditions for an optimal
  learning policy to be a scalar optimum (a declared task law given what
  has been learned, one valuation with costs on its scale, a finite value,
  attainment). A fixed task distribution is not among them: a dependence of
  the tasks on what has been learned, once declared, is a transition of a
  decision process over the learner's organization, and backward induction
  gives an optimum.
- CLAIM-tmp6ppvo (thesis): when what is learned changes what is valued, the
  valuations of the selves policies produce fix no optimum. Judged by each
  produced self the ranking moves under rescalings, self-ratification
  returns two policies or none, and a unique optimum needs a rule that
  privileges a self. The present self's valuation gives an optimum and
  counts nothing only a later valuation sees.
- CLAIM-tmpl9022 (thesis): when each period of learning multiplies later
  returns by g with γg > 1, no policy is optimal, though the task law,
  costs, horizon and valuation are all declared. A bounded version shows
  attainment failing with a finite supremum.
- ARG-tmpi8mhy (existence): the three constructions show the conditions
  are independent.

Numbers checked in `scratch/studies/lead-011/` (22 pytest tests).

Two readings of "changes what can later be learned" are filed side by
side, since they come apart in their answer: as a change in the tasks and
returns met later (CLAIM-tmpy87xn, CLAIM-tmpl9022), where endogeneity
itself breaks nothing and the horizon does the work; and as a change in what
is valued (CLAIM-tmp6ppvo), where the valuation does. What remains: which
evaluator the record adopts when valuation changes, which is the owner's;
condition 1's failure, an undeclared task law, is named but not
constructed; and no worked case ties these to a real learner. Status and
stage unchanged; marking the lead Done is the owner's call.
