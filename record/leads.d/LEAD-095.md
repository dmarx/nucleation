---
number: 95
status: Open
formerly:
- LEAD-tmphc6xs
title: 'Build a small stochastic assembly model in which support can be withdrawn at chosen intermediate states and the nucleus''s relations switched on as a state and as a rate modifier separately'
version: 1
stage: idea
priority: high
method:
- formal
- empirical
tags:
- complex-systems
- natural-sciences
date: '2026-11-19'
line:
- transient-support
- realizability
- nucleating-argument
advances:
- QUESTION-398
- QUESTION-397
summary: >-
  [QUESTION-398](../questions.d/QUESTION-398.md) is the most-cited entry of its slice and its notes give
  only analogues, never a measured effect of withdrawal. Named in
  [QUESTION-398](../questions.d/QUESTION-398.md) and [QUESTION-397](../questions.d/QUESTION-397.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmplsvee CLAIM-tmp5hyz1 — new; the executed study and claim of 2026-11-22 -->

# LEAD-095: Build a small stochastic assembly model in which support can be withdrawn at chosen intermediate states and the nucleus's relations switched on as a state and as a rate modifier separately

## What it would do

Write the Markov chain and compute the difference in committor between
supported and withdrawn at each intermediate state, with the rival "the
system merely completed before withdrawal" excluded.

Where the record names it:

- [QUESTION-398](../questions.d/QUESTION-398.md): "A system where support can be withdrawn at chosen
  intermediate states, with the committor measured afterwards from each, in
  molecules or in a model."
- [QUESTION-397](../questions.d/QUESTION-397.md): "a small Markov chain in which the nucleus's relations are
  both a state and a modifier of other rates, so the two effects can be
  switched on separately."

## What would count

A difference that persists after withdrawal from some states answers
[QUESTION-398](../questions.d/QUESTION-398.md) in the model; the two effects switched on separately answer
[QUESTION-397](../questions.d/QUESTION-397.md).

## Note of 2026-11-22: the model built and run

The chain is built and solved exactly: [CASE-tmplsvee](../cases.d/CASE-tmplsvee.md), with code and tests under scratch/studies/lead-095/. It has a nucleus and eight other units. A scaffold forms and holds the nucleus and is withdrawn for good at chosen states. Feedback from bound units, the nucleus's rate effect and its state effect are separate switches.

- **[QUESTION-398](../questions.d/QUESTION-398.md)'s half: a difference that persists after withdrawal occurs.** With feedback and the rate effect, D is under 0.05 from a quarter of the way through. Withdrawing at unfinished states excludes the rival, and withdrawing at a clock time does not.
- **[QUESTION-397](../questions.d/QUESTION-397.md)'s half: the two effects were switched on separately.** Both raise the committor at matched progress, and only Δk separates them.
- **The general form.** [CLAIM-tmp5hyz1](../claims.d/CLAIM-tmp5hyz1.md) states the identity behind the results, and the condition it gives: what has been built holds the nucleus or no longer needs it.

What remains:

- other kinds of support, such as one that raises binding rates directly rather than holding a nucleus;
- withdrawals of finite length, [CLAIM-604](../claims.d/CLAIM-604.md)'s case;
- any measured system.

The lead stays Open.
