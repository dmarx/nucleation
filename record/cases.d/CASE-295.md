---
number: 295
status: Proposed
formerly:
- CASE-tmpplox8
title: 'A stipulated two-step acquisition: a procedure that loses money on the one question it serves but cuts the cost of acquiring a second competence from 10 to 1, so that acquiring it first is the best policy though each step alone shows a loss'
version: 1
standing: stipulated
kind: construction
tags:
- learning-theory
date: '2026-11-19'
line:
- realizability
- learned-structure
bears_on:
- QUESTION-495
summary: >-
  The filer's numbers, extending A48 §2's worked example in the exchange
  "Topological protection explained" (2026-11-19), memorizing against
  learning a procedure, to A48 §4's point that an acquisition can be
  valued by what it does to later acquisitions. Built to separate the
  value of an acquisition on its own tasks from its value in a sequence.
  Fictional by construction. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---

# CASE-295: A stipulated two-step acquisition: a procedure that loses money on the one question it serves but cuts the cost of acquiring a second competence from 10 to 1, so that acquiring it first is the best policy though each step alone shows a loss

## The construction

Costs and savings are in one unit of work.

- **P**, a procedure: acquiring it costs 4; it saves 2 on the one question
  in the declared task distribution that it directly serves.
- **Q**, a second competence: it saves 3 on each of three later questions
  (9). Acquiring it costs 10 from scratch, and 1 if P is already held.

| policy | cost | savings | net |
|---|---|---|---|
| nothing | 0 | 0 | 0 |
| P alone | 4 | 2 | −2 |
| Q alone | 10 | 9 | −1 |
| P then Q | 4 + 1 | 2 + 9 | +6 |

Checked by computation on 2026-11-19.

## What it shows

A rule that acquires a competence only when its own savings exceed its
own cost rejects P and Q both and acquires nothing; the best policy
acquires both, P first. P's value lies almost wholly in what it does to
Q's cost. In [TERM-117](../terms.d/TERM-117.md)'s terms P is a productive nucleus for Q: its
establishment improves the resource-feasible accessibility of forming Q
against the comparator of not having it.

## What it could and could not show

It shows that the ranking can reverse. It does not show how often such
structure arises, or how a learner would know Q is coming. A48 §11's
proposed study, skills that unlock different later learning
opportunities with learners that optimize the immediate task, the known
horizon, the worst case, or future acquisition capacity, would test the
first.

## Note of 2026-11-19: Bengio, Louradour, Collobert and Weston, read
<!-- inactive-ok-file: THEORY-tmp0lbb1 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

A real instance of this case's pattern ([THEORY-tmp0lbb1](../theory.d/THEORY-tmp0lbb1.md); NOTE-tmpk9cmk), in final-error terms: training on easier shapes alone "yielded poor results", yet spending half of a fixed budget on them first gave the best final error, better than unordered training on both sets. Chen and colleagues ([NOTE-tmpwrmog](../notes.d/NOTE-tmpwrmog.md)) add a cost this case leaves out, finding which earlier acquisition helps, and show it can be paid and recouped.
