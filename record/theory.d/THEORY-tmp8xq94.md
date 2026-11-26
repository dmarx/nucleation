---
status: Proposed
promote_when: >-
  An independent analysis of Transformers trained by next-token prediction
  on sequences whose generating parameters change per sequence finds, by an
  intervention and not only by probes or loss matching, that early layers
  bind tokens into an in-context training set and later layers optimize an
  in-context objective over it: for example, that editing the decoded
  training set or the preconditioned inputs changes predictions as the
  optimizer would. Whether such optimization occurs in language models is
  not asserted.
title: 'Trained transformers bind tokens, then optimize in context'
statement: >-
  von Oswald and colleagues propose that Transformers trained only by
  next-token prediction on synthetic sequences whose generating parameters
  change per sequence learn in context by mesa-optimization: early layers
  bind consecutive tokens into an in-context training set, and later layers
  optimize a least-squares objective over it, exactly one gradient step for
  one linear self-attention layer on constructed tokens and approximately
  preconditioned descent toward ridge regression for deeper linear and
  softmax models; a mesa-layer that solves that regression exactly by
  recursive least squares matches or beats the deep models
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    At the owner's prompting, the reading's bearings on the record's own
    claims and questions were filed: it corroborates CLAIM-118, and it bears
    on QUESTION-020 and QUESTION-161. The account is unchanged.
tags:
- learning-theory
- representation-learning
date: '2026-11-26'
source:
- LIT-tmpuv16r
extends:
- THEORY-169
bears_on:
- QUESTION-159
- QUESTION-020
- QUESTION-161
corroborates:
- CLAIM-118
summary: >-
  von Oswald et al. (2023), [LIT-tmpuv16r](../literature.d/LIT-tmpuv16r.md), read in [NOTE-tmpcktnn](../notes.d/NOTE-tmpcktnn.md). The exact
  part is Proposition 1, a one-layer gradient-step identity, together with
  the mesa-layer, which optimizes by construction. Everything about deep and
  softmax models rests on matched loss curves, weight structure, linear
  probes and distillation, so Proposed. It extends [THEORY-169](THEORY-169.md) with a further
  exact identity and a ridge-learner layer, and it bears on [QUESTION-159](../questions.d/QUESTION-159.md)
  without answering it. The wording is the reader's, revised by the filer;
  adopting it is the owner's call.
---

# THEORY-tmp8xq94: Trained transformers bind tokens, then optimize in context

von Oswald et al., "Uncovering mesa-optimization algorithms in Transformers" (2023), [LIT-tmpuv16r](../literature.d/LIT-tmpuv16r.md).

## The account

"we refer to this hypothetical acquired process as mesa-optimization, to
distinguish it from the base-optimization of Eq. 1" (p. 2). The first
layer's mechanism "exactly coincides with the first layer of the induction
head circuit" (p. 6). One causally masked linear self-attention head's
transformation "is identical to the gradient-induced update" (Proposition
1, p. 3). Deeper models show that "Base-optimization has therefore
discovered a hybrid algorithm that descends over layers the mesa-objective"
(p. 7).

## What it does not show

- **That deep or softmax models execute Proposition 2.** The paper concedes
  that the compressed fit is hard "to connect it exactly to the theoretical
  construction of Proposition 2".
- **That probed quantities are used.** No intervention is reported.
- **Anything about language models.** "Strictly speaking, these results are
  not sufficient to make claims on whether mesa-optimization is occurring
  within standard Transformers" (Appendix G).
