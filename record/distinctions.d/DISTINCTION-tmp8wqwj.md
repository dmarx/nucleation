---
status: Proposed
title: 'A shortcut fails its objective off the family; a proxy optimum satisfies it'
between:
- TERM-tmp5d01f
- TERM-108
bears_on:
- QUESTION-493
- QUESTION-tmpr4p3a
rests_on:
- CLAIM-tmpnjaik
statement: >-
  A shortcut (TERM-tmp5d01f) and the optimum of a proxy objective (TERM-108)
  are distinct failures of optimization against a declared family: in a
  shortcut the objective is right and the solution reads a correlate of what
  it rewards, so the solution scores badly by its own objective off the
  family; in a proxy optimum the objective is wrong and the solution
  satisfies it, so it scores well by its own objective while failing the
  outcome the objective stood for
criterion: >-
  Whether the failure lies in the solution or in the objective: whether the
  declared objective, evaluated on the cases where the system fails, still
  rewards the intended outcome
tells_apart: >-
  Evaluate the system's own training objective on cases outside the
  training family. A shortcut scores badly there by that objective; a proxy
  optimum scores well, as a paperclip maximizer scores perfectly on
  paperclips. The same system can be both, relative to different
  objectives: a sycophantic model is a proxy optimum relative to the
  approval it was rewarded for, since it goes on earning approval off the
  family, and a shortcut relative to the correctness its designers intended
defeated_if: >-
  A failure that cannot be assigned to the solution or to the objective even
  in principle, because the objective is defined only on the training family,
  so that its value off the family is not given; or a showing that every
  proxy optimum is a shortcut relative to some objective and conversely, so
  that the distinction marks only which objective one chooses to name.
version: 1
tags:
- shortcut-learning
- learning-theory
- agency
date: '2026-11-27'
line:
- learned-structure
- organizational-normativity
summary: >-
  Filed when the owner connected shortcut learning to the record's account
  of paperclip maximization (2026-11-27). The connection holds
  ([CLAIM-tmpnjaik](../claims.d/CLAIM-tmpnjaik.md)), but the two fail in different places, and the test that
  locates the failure is cheap. The defeater's second clause is the
  strongest objection. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmp5d01f TERM-108 CLAIM-tmpnjaik CLAIM-tmp7crnt CASE-416 — Proposed, Open or new; the terms bound, the claim it rests on, the questions, and the claim and case it ties to -->

# DISTINCTION-tmp8wqwj: A shortcut fails its objective off the family; a proxy optimum satisfies it

## The sides

- **Shortcut** ([TERM-tmp5d01f](../terms.d/TERM-tmp5d01f.md)). The objective is right and the solution is
  wrong. [CASE-416](../cases.d/CASE-416.md)'s classifier is trained to predict the class, and off the
  family, where the watermark and the class come apart, it predicts badly by
  that very objective.
- **Proxy optimum** ([TERM-108](../terms.d/TERM-108.md)). The objective is wrong and the solution is
  right *for it*. The paperclip maximizer is trained to maximize paperclips,
  and it does.

## Telling them apart

| | Shortcut | Proxy optimum |
|---|---|---|
| Where the failure lies | the solution | the objective |
| The system's own objective, off the family | scores badly | scores well |
| Cured by | a family in which the correlate is unreliable | a different objective, or constraints from outside it ([CLAIM-1252](../claims.d/CLAIM-1252.md)) |
| Paperclip case | — | the paperclip maximizer |
| Watermark case | [CASE-416](../cases.d/CASE-416.md) | — |

The test is to evaluate the system's own objective where it fails, and it
locates sycophancy in two places. Relative to approval, a sycophantic model is
a proxy optimum: it goes on earning approval on new items. Relative to the
correctness its designers meant approval to track, it is a shortcut. That
corrects [CLAIM-tmp7crnt](../claims.d/CLAIM-tmp7crnt.md), which called sycophancy a shortcut without saying
relative to which objective.

## What it does not say

That the two cannot occur together; the sycophancy case is both. Nor that the
choice of objective is arbitrary: the defeater's second clause says what
would make it so.
