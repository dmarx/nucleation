---
status: Open
title: 'Read Geirhos and colleagues on shortcut learning, and test whether shortcuts are the earliest-learnable reliable correlates'
stage: idea
priority: medium
method:
- reading
- empirical
tags:
- learning-theory
- representation-learning
date: '2026-11-27'
line:
- learned-structure
advances:
- CLAIM-tmpgmvhl
- CLAIM-tmp7crnt
- QUESTION-493
summary: >-
  From the owner's question of 2026-11-27 on the record's account of
  shortcut learning. Geirhos and colleagues (2020) named the phenomenon, and
  the record holds none of the shortcut-learning literature. The test is a
  design, not yet worked out. The wording is the assistant's (Claude, in
  this session).
---
<!-- inactive-ok-file: CLAIM-tmpgmvhl — Proposed, Open or new; the entries this lead would advance -->

# LEAD-tmp2592n: Read Geirhos and colleagues on shortcut learning, and test whether shortcuts are the earliest-learnable reliable correlates

## Read

- Geirhos, Jacobsen, Michaelis, Zemel, Brendel, Bethge and Wichmann (2020), "Shortcut learning in deep neural networks", Nature Machine Intelligence 2:665-673, arXiv 2004.07780, confirmed by search.
  - Shortcuts are decision rules that do well on standard benchmarks and fail to transfer.
  - The paper gives a taxonomy (§3) and an account of where shortcuts come from (§4).
- Read it for:
  - whether its account of origin matches [CLAIM-tmpgmvhl](../claims.d/CLAIM-tmpgmvhl.md)'s;
  - whether its taxonomy separates reading an effect of the truth from reading a correlate ([CLAIM-1086](../claims.d/CLAIM-1086.md)).

## Test

Train a small network on a family in which a cheap correlate (say, a colour
patch) and the true feature are both perfectly reliable. Vary two things:
- which of them is lower-order;
- when the correlate is broken in training.

[CLAIM-tmpgmvhl](../claims.d/CLAIM-tmpgmvhl.md) predicts:
- the network reads whichever is cheaper;
- a correlate learned first persists after the true feature becomes learnable;
- breaking the correlate, not adding data, removes it.
