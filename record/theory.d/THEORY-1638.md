---
number: 1638
status: Proposed
formerly:
- THEORY-tmpw3g5u
title: 'Chen, Kuo, Liu, Poon, Towey, Tse and Zhou hold that metamorphic testing alleviates but cannot solve the test-oracle problem: a program is checked against metamorphic relations, necessary properties relating two or more inputs and their outputs, so a violation shows a fault while satisfying them does not show correctness'
version: 1
tags:
- software-engineering
date: '2026-11-12'
source:
- LIT-2333
promote_when: >-
  The paper is confirmed, in its published version, to define a
  metamorphic relation as a necessary property of the target function or
  algorithm over two or more inputs and their outputs, to say that
  metamorphic testing alleviates the oracle problem but can never
  completely solve it, and to give the necessary but not sufficient nature
  of the relations as the reason. Nothing about how effective the method
  is, which the paper reports from other studies, is asked.
summary: >-
  The central account of [LIT-2333](../literature.d/LIT-2333.md), read in [NOTE-1717](../notes.d/NOTE-1717.md) from the
  authors' manuscript. It is the account the exchange "luria experiment
  design" leaned on, at A50 §11, when it proposed metamorphic relations as
  the hidden scorer of a change to a record's schema, and it carries the
  limit that use has: such a scorer can find a wrong change but cannot
  certify a right one. Proposed until checked against the published
  version.
---

# THEORY-1638: Chen, Kuo, Liu, Poon, Towey, Tse and Zhou hold that metamorphic testing alleviates but cannot solve the test-oracle problem: a program is checked against metamorphic relations, necessary properties relating two or more inputs and their outputs, so a violation shows a fault while satisfying them does not show correctness

## The account

Where no practical oracle checks a single output, the program is run on a
source input and on follow-up inputs derived from it, and the outputs are
checked against a metamorphic relation: a necessary property of the target
function over "a sequence of two or more inputs" and their outputs
(Definition 1). A violation shows the program faulty. Satisfying every
relation does not show it correct: even a complete set "might still not be
equivalent to a test oracle due to the necessary (but not sufficient)
nature of the properties" (§4.1). So the method alleviates the oracle
problem, and "one can never completely solve it".

## What it does not claim

- How many relations suffice. The figure of three to six diverse relations
  catching about 90% of oracle-detectable faults is a report of another
  study, with diversity undefined.
- That relations are proven. "In MT, MRs are tested and not proven" (§5.1).
