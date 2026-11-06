---
status: 'Open'
title: 'Does an independent experiment or calculation on finite Miura-ori sheets find soft deformations decaying from the boundaries with the predicted wavenumber-dependent decay length, and a count of degrees of freedom that scales with the perimeter rather than the area?'
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-11-06'
line:
- realizability
summary: >-
  The promotion condition formerly on [THEORY-1428](../theory.d/THEORY-1428.md), moved here when the
  thirtieth status review narrowed and promoted that reading under
  [ADR-065](../decisions.d/ADR-065.md). Evans, Silverberg and Santangelo predict the edge modes and the
  perimeter scaling, and check decay lengths on one 8 × 8 paper sheet;
  whether another group's experiment or calculation agrees is this
  question.
---

# QUESTION-tmpwo0r9: Does an independent experiment or calculation on finite Miura-ori sheets find soft deformations decaying from the boundaries with the predicted wavenumber-dependent decay length, and a count of degrees of freedom that scales with the perimeter rather than the area?

## Why it is a question

[THEORY-1428](../theory.d/THEORY-1428.md) reports what Evans, Silverberg and Santangelo's lattice theory predicts ([NOTE-1587](../notes.d/NOTE-1587.md)). The prediction was checked against decay lengths on a single 8 × 8 paper Miura-ori, and for a pop-through defect the decay length "can be estimated to within 100%". The record holds no other group's test.

## What would answer it

The condition as it stood on [THEORY-1428](../theory.d/THEORY-1428.md):

> An independent experiment or calculation on finite Miura-ori sheets finds soft deformations decaying from the boundaries with the predicted wavenumber-dependent decay length, and a count of degrees of freedom that scales with the perimeter rather than the area.

## Partly bearing (2026-11-06)

Reader J's bar-and-joint count gives B − 3 infinitesimal floppy modes for a triangulated folded Miura-ori at every size tried, where B is the number of boundary vertices (scratch/formal/evans_miura_check.py, second-checked by the coordinator on 2026-11-06). That is a perimeter count, but it comes from Maxwell counting, not from the paper's theory. It does not test the decay length, so it does not answer the question.
