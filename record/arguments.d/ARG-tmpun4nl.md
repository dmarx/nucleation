---
status: Proposed
title: 'Park and colleagues'' Fig. 16, by analogy from an MLP regressor''s first-layer weights to a language model''s unembedding, suggests that top directions tracking the data''s common high-variance structure belong to large-step or under-trained regimes, a rival to the stop-word half of the truncated-band account'
version: 1
form: analogy
grounds:
- THEORY-tmphbp5a
concludes:
- CLAIM-tmp9atj9
tags:
- representation-learning
- learning-theory
date: '2026-11-22'
line:
- learned-structure
summary: >-
  Whether Park and colleagues' finding transfers to the owner's
  truncated-band claim. In UTKFace MLPs, leading first-layer directions
  overlap the data's first principal component at 0.68 and 0.64 only in
  the large-step regimes, which converge to a worse minimum, and at 0.056
  in the well-trained phase. The respect of likeness, top directions
  inheriting the input's common covariance when the supervised signal is
  weak, is the one the rival reading needs; the objects differ. A weak
  analogy, enough to make the rival worth testing and not to prefer it.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmphbp5a CLAIM-tmp9atj9 CLAIM-tmp2r6ur LEAD-tmptgrc7 — Proposed or new; the reading, the rival claim, the owner's claim it rivals and the test -->

# ARG-tmpun4nl: Park and colleagues' Fig. 16, by analogy from an MLP regressor's first-layer weights to a language model's unembedding, suggests that top directions tracking the data's common high-variance structure belong to large-step or under-trained regimes, a rival to the stop-word half of the truncated-band account

## The inference

THEORY-tmphbp5a, §V C: in the convergent large-step regime "learning is
dominated by the principal covariance directions of the data rather than
by task-relevant nonlinear representations", because the supervised part
of the backpropagated error is "effectively incoherent" and the weights
inherit the input covariance; in the well-trained phase the leading modes
"capture nontrivial structure in the data that deviates from the principal
components". By analogy, a language model's top unembedding directions
would track common structure such as token frequency more in early or
large-step training than in a well-trained model: CLAIM-tmp9atj9.

## Critical questions

- **In what respect are they alike, and is it the respect the conclusion
  needs?** Both are weight matrices whose top directions can inherit the
  data's dominant covariance when the task gradient is weak. That is the
  respect the rival needs.
- **What relevant difference is there?** Several. A first layer reads
  inputs; an unembedding writes logits, and token frequency is part of the
  next-token task itself, not only nuisance covariance, so a frequency
  direction at the top of a well-trained unembedding would be task
  structure (THEORY-tmpcij35 has top outliers from feature means carrying
  task signal). One dataset, MLPs, regression; phases set by step size and
  initial variance, not training stage, though the linear model's t_c makes
  stage the same kind of variable.
- **What transfers?** The hypothesis that the common-structure signature
  depends on regime and stage, so a single measurement cannot establish the
  stop-word half. Not the overlaps.

## Verdict

A weak analogy that makes CLAIM-tmp9atj9 a live alternative to part of
CLAIM-tmp2r6ur and changes what LEAD-tmptgrc7 must record; it does not
prefer the rival. Proposed.
