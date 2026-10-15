---
status: Open
title: How should the cost of recovering a distinction from a representation be
  defined, relative to an encoding, a class of procedures and a success criterion?
version: 1
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

# QUESTION-tmprdpkh: How should the cost of recovering a distinction from a representation be defined, relative to an encoding, a class of procedures and a success criterion?

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
[CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md)'s infeasible case and [CLAIM-199](../claims.d/CLAIM-199.md)'s helpful garbling sit on one
scale.

An answer is a definition with those three parameters fixed, shown to
recover [CLAIM-199](../claims.d/CLAIM-199.md)'s rule-class case and [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md)'s computational case as
special cases. Time-bounded Kolmogorov complexity and computational
learning theory are the nearest existing tools.
