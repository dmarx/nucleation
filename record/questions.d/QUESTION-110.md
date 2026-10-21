---
number: 110
status: Open
formerly:
- QUESTION-tmprdpkh
title: How should the cost of recovering a distinction from a representation be
  defined, relative to an encoding, a class of procedures and a success criterion?
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the reading of Xu et al. on usable
    information (NOTE-tmpvnsxo): V-information fixes two of the three
    parameters and has no cost of recovery, so it does not answer. The
    question is unchanged and stays Open.
tags:
- information-theory
- mathematics
date: '2026-10-15'
line: formal-apparatus
summary: >-
  A18's sixth candidate, "recovery complexity", filed as a question at A18's own
  suggestion rather than as a term. The exchange used the idea under five names
  and never fixed one.
---
<!-- inactive-ok-file: CLAIM-199 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# QUESTION-110: How should the cost of recovering a distinction from a representation be defined, relative to an encoding, a class of procedures and a success criterion?

## Why it is a question

A18: "We have discussed statistical distinguishability, information
retention, availability, reconstructibility, access cost, and action
feasibility. These shouldn't all be compressed into 'usable
information.'" Its schematic definition: C_ε(D | M) = inf over procedures
δ of the cost C(δ) such that P[δ(M) ≠ D] ≤ ε. It said what is missing:
"a distribution over tasks or inputs, a computational-cost model, and a
specification of the target variable."

[CLAIM-199](../claims.d/CLAIM-199.md)'s usable information fixes a rule class and asks what it can
extract. This asks for the cost of extraction as a quantity, so that
[CLAIM-304](../claims.d/CLAIM-304.md)'s infeasible case and [CLAIM-199](../claims.d/CLAIM-199.md)'s helpful garbling sit on one
scale.

An answer is a definition with those three parameters fixed, shown to
recover [CLAIM-199](../claims.d/CLAIM-199.md)'s rule-class case and [CLAIM-304](../claims.d/CLAIM-304.md)'s computational case as
special cases. Time-bounded Kolmogorov complexity and computational
learning theory are the nearest existing tools.

## Note of 2026-10-21: V-information fixes two of the three parameters

Xu, Zhao, Song, Stewart and Ermon 2020 ([LIT-tmp07k7g](../literature.d/LIT-tmp07k7g.md), [NOTE-tmpvnsxo](../notes.d/NOTE-tmpvnsxo.md)),
read in full on 2026-10-21. Their V-information fixes the class of
procedures (a predictive family V) and the success criterion (log loss),
and with V the one-coordinate rules it recovers [CLAIM-199](../claims.d/CLAIM-199.md)'s rule-class case
([THEORY-tmpgz4cf](../theory.d/THEORY-tmpgz4cf.md)). It has no cost of recovery: a procedure is in V or not.
[CLAIM-304](../claims.d/CLAIM-304.md)'s computational case would be V the efficient predictors, which
the paper names (its §3.3) and proves nothing about. Its PAC bound
([THEORY-tmp9m1g4](../theory.d/THEORY-tmp9m1g4.md)) makes the quantity estimable for a family of bounded
complexity, which is a cost of measuring it, not of recovering the
distinction. So it is one of the "nearest existing tools", not an answer.
The question stays Open.
