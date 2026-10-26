---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpcuw4h) in full, from the arXiv copy (v2); worth
  reading for its proof that symmetries of the data confine population
  gradient descent to a subspace of interpretable head actions
  (THEORY-tmpdxhxm), for its theorem that a saturated memorized shortcut
  starves the in-context circuit of gradient on the data it solves
  (THEORY-tmpvqsx2), and for its scan in which initialization picks one of
  several induction circuits, read by the authors as cooperation through
  shared units and competition for layers (THEORY-tmpq4l9j). Read it
  knowing that the architecture is idealized (fixed orthogonal write maps,
  merged key-query, orthonormal embeddings), that invariance is proved
  and attraction is not, that the results are for gradient descent while
  its circuit-detection experiment uses AdamW, and that the competition
  scan was run in training projected onto seven coordinates.
title: 'Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply says "A July 2026 theoretical study
    already derives low-dimensional invariant training dynamics for a class
    of inductive reasoning tasks and investigates competing circuit
    solutions", with no author or title. An arXiv search on 2026-10-26 found
    this paper, whose abstract matches each clause. Checked against the
    arXiv record: Tiberiu Musat, Tiago Pimentel, Nicolas Zucchet and Thomas
    Hofmann, arXiv 2607.11875, v1 submitted 13 July 2026, which is
    `published:`; v2 followed on 14 July 2026. No venue is given. The
    summary follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpcuw4h), from the arXiv copy, v2 of 14 July 2026,
    fetched 2026-10-26. Status Deferred → Active. Three THEORYs filed:
    THEORY-tmpdxhxm and THEORY-tmpvqsx2 Active (re-derived),
    THEORY-tmpq4l9j Proposed. The summary is checked against the reading
    and made exact about which results are proved and which are empirical.
    The identification from T24 is confirmed: the paper derives
    low-dimensional invariant training dynamics for a class of inductive
    reasoning tasks and studies competing circuit solutions.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2026-07-13'
arxiv: '2607.11875'
first_author: 'Musat'
keywords:
- 'inductive reasoning'
- 'invariant manifold'
- 'training dynamics'
- 'in-context learning'
- 'in-weights learning'
- 'circuit competition'
implementations: []
summary: >-
  Musat, Pimentel, Zucchet & Hofmann (2026), arXiv:2607.11875. For a class
  of block-list inductive tasks that includes associative recall, k-hop
  induction and in-context n-grams, it proves that population gradient
  descent keeps an idealized attention-only transformer's key–query and
  output weights on a low-dimensional invariant manifold fixed by the
  data's symmetries, whose coordinates are interpretable head actions. On
  it, it proves that a saturated in-weights circuit suppresses the
  in-context circuit's gradient by the fraction of data it does not solve and
  that burstiness multiplies it, shows empirically that initialization
  decides which of several induction circuits wins, and detects circuits
  in trained models by projecting onto the coordinates.
---
<!-- inactive-ok-file: THEORY-tmpq4l9j — Proposed; an account drawn from this reading, cited as open -->

# LIT-tmp01if4: Invariant Learning Dynamics of Transformers in Inductive Reasoning Tasks

Musat, T., Pimentel, T., Zucchet, N. & Hofmann, T. (2026). Invariant
learning dynamics of transformers in inductive reasoning tasks.
arXiv:2607.11875.

Read in full on 2026-10-26 (NOTE-tmpcuw4h). Three accounts were drawn
from it: THEORY-tmpdxhxm, THEORY-tmpvqsx2 and THEORY-tmpq4l9j.

## Why this is here

Cited at T24 as "particularly valuable prior art and a strong comparator —
not merely background motivation" for the reply's proposed study of
induction-circuit formation. Its competition between circuit solutions
decided by data statistics and initialization is what the record's framework
would have to predict better than to earn [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md)'s prospective test. It
bears on [QUESTION-039](../questions.d/QUESTION-039.md) and on [THEORY-253](../theory.d/THEORY-253.md), the record's toy-scope account of
skills learned in order.
