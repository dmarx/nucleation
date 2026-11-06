---
status: Open
title: 'Does an independent replication on the Omniglot one-shot task, or on a comparable held-out set of characters, confirm that a program-induction model of handwritten characters reaches human one-shot classification accuracy and produces exemplars and new characters that judges cannot tell from people''s, and that removing compositionality or its learned priors makes it worse?'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Filed by the thirtieth status review, at the status review's ruling (the
    owner delegated these rulings): the replication demand of THEORY-1357's
    promote_when, moved here when that reading was narrowed to what Lake,
    Salakhutdinov and Tenenbaum measured and promoted (ADR-065).
tags:
- cognition
- compositionality
- probabilistic-modeling
date: '2026-11-06'
line: learned-structure
summary: >-
  Lake, Salakhutdinov and Tenenbaum (2015, [LIT-2009](../literature.d/LIT-2009.md), [NOTE-1542](../notes.d/NOTE-1542.md); [THEORY-1357](../theory.d/THEORY-1357.md))
  report human-level one-shot classification and near-chance visual Turing
  tests for Bayesian Program Learning, with lesions. It is one study by the
  model's authors, on the data set they built, with naive judges; the record
  holds no replication.
---

# QUESTION-tmpn1jcn: Does an independent replication on the Omniglot one-shot task, or on a comparable held-out set of characters, confirm that a program-induction model of handwritten characters reaches human one-shot classification accuracy and produces exemplars and new characters that judges cannot tell from people's, and that removing compositionality or its learned priors makes it worse?

## Why it is a question

[THEORY-1357](../theory.d/THEORY-1357.md) holds what the 2015 study measured. Whether the result
survives other hands is open: the model, the Omniglot set and the visual
Turing tests are the authors', the judges were naive Mechanical Turk
workers, and the lesions differ by test (the type-level priors mattered
for generating new characters, not for classification). The authors' own
progress report on the Omniglot challenge (Lake, Salakhutdinov and
Tenenbaum 2019) is not held and would not be independent.

## What would answer it

The test [THEORY-1357](../theory.d/THEORY-1357.md)'s promote_when named: an independent replication on
the Omniglot one-shot task, or a comparable held-out set of characters,
that confirms that the program-induction model reaches human one-shot
classification accuracy, that its generated exemplars and characters are
near chance in human-against-machine identification, and that the lesions
without compositionality or without learned priors do worse on both.
