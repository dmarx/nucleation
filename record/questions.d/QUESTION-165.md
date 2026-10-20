---
number: 165
status: Open
formerly:
- QUESTION-tmpbqvmq
title: "On the Random Hierarchy Model, is the number of examples a deep network needs set by when patch-label correlations become detectable, or by the size of the grammar, once the two are separated by moving the correlations with n_c, m and L fixed?"
version: 1
tags:
- learning-theory
- compositionality
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The promotion condition formerly on [THEORY-195](../theory.d/THEORY-195.md), moved here unchanged when
  [THEORY-195](../theory.d/THEORY-195.md) was narrowed and promoted on 2026-10-19 to what the experiments
  measured. In the model as given, the correlation threshold and the
  grammar's size are the same expression, n_c m^L, so the measurements
  cannot say which one sets the number of examples.
answered_by:
- THEORY-786
---

# QUESTION-165: On the Random Hierarchy Model, is the number of examples a deep network needs set by when patch-label correlations become detectable, or by the size of the grammar, once the two are separated by moving the correlations with n_c, m and L fixed?

## Why it is a question

[THEORY-195](../theory.d/THEORY-195.md), narrowed on 2026-10-19 under [ADR-047](../decisions.d/ADR-047.md) v3, holds what Cagnetta
et al. ([LIT-877](../literature.d/LIT-877.md)) measured: deep CNNs matched to the tree learn the Random
Hierarchy Model from about n_c m^L examples, at the same training-set size
at which their hidden layers become invariant to synonym swaps, while
shallow and fixed-kernel learners need a number proportional to the whole
input space. The paper's explanation is a large-v scaling estimate: the
class statistics of input patches rise above sampling noise at the same
n_c m^L. Until that date [THEORY-195](../theory.d/THEORY-195.md)'s title also asserted that explanation,
and its promote_when asked for a way to test it. At the owner's direction,
from the promotion audit's batch 027 ([ADR-047](../decisions.d/ADR-047.md)), the THEORY was narrowed to
the measured result, and the condition moved here unchanged.

It is open because, in the model as given, the threshold and the grammar's
size are the same number. Removing the correlations altogether (Fig. 9)
shows they are necessary, not that their detectability fixes the count
([NOTE-677](../notes.d/NOTE-677.md)).

## What would answer it

The condition formerly on [THEORY-195](../theory.d/THEORY-195.md), unchanged: a result that separates
the number of examples a deep network needs from the counting of the
grammar, by moving the input–label correlations while n_c, m and L stay
fixed. For instance, non-uniform production probabilities could make some
tuples' class statistics detectable earlier than others, with the
training-set sizes at which each level becomes synonym-invariant, and at
which test error falls, tracking the predicted detection thresholds rather
than n_c m^L. Or a proof that gradient descent on a deep network learns the
Random Hierarchy Model from a number of examples of order n_c m^L,
polynomial in the input dimension. Further collapses of learning curves on
n_c m^L at other parameter values cannot settle it, because the threshold
and the grammar's size are the same number there.
