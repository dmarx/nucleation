---
number: 977
status: Active
formerly:
- THEORY-tmpb4xka
title: 'In the two-layer attention-only transformer that Elhage et al. reverse-engineer, the second-layer heads that compose substantially with first-layer heads do so through their keys, mainly with a head that attends to the previous token and, after the published correction, also with one that attends over the last several tokens; these heads are induction heads, attending from a token to the one after its earlier occurrence, including on repeated random tokens, with positive-eigenvalue copying OV and same-matching QK circuits, and the second-order virtual-head terms add little to the loss reduction'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1189, the reading of Elhage et al. (2021) in
    full. One model in one study, but the title claims no more than the
    paper reports for it, with the authors' later correction included,
    and nothing in the record contradicts it (ADR-047 v3). The claims are
    taken from the text: the composition diagram, the eigenvalue scatter
    and the term-importance plots are interactive figures the reading did
    not see. The induction-head mechanism is corroborated in the record by
    Olsson et al.'s Argument 5 and Scherlis's replication in two-layer
    attention-only models (NOTE-1173).
tags:
- representation-learning
- compositionality
date: '2026-10-26'
source:
- LIT-1534
summary: >-
  Elhage et al. (2021), [LIT-1534](../literature.d/LIT-1534.md), read in [NOTE-1189](../notes.d/NOTE-1189.md): Analyzing a
  Two-Layer Model, Induction Heads, Term Importance Analysis, and the
  Correction. Composition between heads was scored by a normalized
  Frobenius norm of matrix products, minus its value for random matrices.
  The heads it picked out attend to the token after the present token's
  previous occurrence and copy it, which is the minimal induction circuit
  the framework predicts from K-composition with a previous-token head. It
  is one model, with no seeds or training details reported, and says
  nothing about models with MLPs or about when the heads form.
---
<!-- inactive-ok-file: THEORY-990 THEORY-967 — Proposed; the wider thesis and the developmental account beside this, cited as open -->

# THEORY-977: In the two-layer attention-only transformer that Elhage et al. reverse-engineer, the second-layer heads that compose substantially with first-layer heads do so through their keys, mainly with a head that attends to the previous token and, after the published correction, also with one that attends over the last several tokens; these heads are induction heads, attending from a token to the one after its earlier occurrence, including on repeated random tokens, with positive-eigenvalue copying OV and same-matching QK circuits, and the second-order virtual-head terms add little to the loss reduction

## Source

Elhage, Nanda, Olsson et al. (2021), [LIT-1534](../literature.d/LIT-1534.md), read in full in
[NOTE-1189](../notes.d/NOTE-1189.md), from the current article page with its correction.

## What was actually shown

**The model.** A two-layer attention-only transformer, 12 heads per layer
with d_head = 64, positions added only to queries and keys, trained on the
data of Kaplan et al.

**Composition.** For each first-layer head h₁ and second-layer head h₂,
the size of Q-, K- and V-composition is ‖product‖_F divided by the
product of the two norms, minus the expected value for random matrices
of the same shapes. As first published: "there is only significant
K-composition, and only with one layer 0 head". After the correction of a
bug that computed the norm of a cyclic permutation of the product, "the
importance of K-composition with the previous token head remains
unchanged", and two of the induction heads also compose with a head
"which attends to the last several tokens".

**What the heads do.** On the first paragraph of *Harry Potter and the
Philosopher's Stone*, and on a random token sequence repeated three times,
the composing heads attend from a token to the token that followed its
previous occurrence, and raise that token's logit. If none is found they
attend to the start token.

**Mechanism check.** The minimal theory needs a copying OV circuit and a
same-matching QK term Id ⊗ A^{h₋₁} ⊗ W. By the positive-eigenvalue
statistic, all the induction heads sit in the corner where both are
positive. The authors note that large K-composition did not imply that its
sign would be positive, so this is not circular.

**Term importance.** Running the model with frozen patterns and replacing
head outputs with those of the previous run removes the paths through n
or more V-composed heads; the second-order (virtual-head) terms have "a
pretty small marginal effect", and the second-layer single-head terms
carry most of the reduction in loss.

**What could have come out otherwise.** Composition could have been spread
across many heads and kinds, the composing heads could have done something
other than induction, their eigenvalues could have been of mixed sign, and
virtual heads could have mattered in aggregate.

## What this does not say

- **Not the size of each effect.** The composition scores, eigenvalues and
  term-importance losses are given in figures; the reading has them only
  as the text describes them.
- **Not that the minimal circuit is the whole story.** The correction adds
  composition with a several-token head.
- **Not about MLPs or large models.** The extension to large models is
  [THEORY-973](THEORY-973.md) (small models, causal) and [THEORY-990](THEORY-990.md) (large
  models, Proposed), from the next paper.
- **Not about training.** One trained model, read once.

## Connections

- **[THEORY-988](THEORY-988.md)** is the decomposition used.
- **[THEORY-973](THEORY-973.md)** finds such heads forming in one window of training in
  small attention-only models and carrying their in-context learning.
- **[THEORY-975](THEORY-975.md) and [THEORY-967](THEORY-967.md)** track previous-token and
  induction heads over training in a two-layer attention-only model on the
  Pile, the developmental counterpart of this snapshot.
- **[THEORY-1009](THEORY-1009.md) and [THEORY-981](THEORY-981.md)** analyse the gradient dynamics of
  such an induction circuit in a two-layer attention-only model.
