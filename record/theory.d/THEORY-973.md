---
number: 973
status: Active
formerly:
- THEORY-tmp8cat0
title: 'In small attention-only transformer language models of two to six layers, in-context learning, measured as the loss at token 500 minus the loss at token 50, appears abruptly in one early window of training in which induction heads form, and ablating those heads at test time removes nearly all of it; one-layer models show neither, and letting a single layer attend by the previous token brings the jump to one-layer models and moves it earlier in two-layer ones'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1173, the reading of Olsson et al. (2022) in
    full. One study, but the title claims no more than it measured, its
    own design supports it (ablation and co-perturbation, not only
    co-occurrence), and nothing in the record contradicts it (ADR-047 v3).
    The paper's wider thesis for large models is the Proposed
    THEORY-990.
tags:
- representation-learning
- learning-theory
date: '2026-10-26'
source:
- LIT-1538
answers:
- QUESTION-039
summary: >-
  Olsson et al. (2022), [LIT-1538](../literature.d/LIT-1538.md), read in [NOTE-1173](../notes.d/NOTE-1173.md): Arguments
  1–3 for the small attention-only series, with the smeared-key models.
  The score jumps from under 0.15 to about 0.4 nats in the window where
  induction heads form, pattern-preserving ablation of the induction heads
  removes nearly all of it to the end of training, and an architecture that
  lets one layer express induction moves the jump. It says nothing causal
  about models with MLPs or large models, and nothing about few-shot task
  learning, which the score does not measure.
extended_by:
- THEORY-990
---
<!-- inactive-ok-file: THEORY-990 THEORY-783 THEORY-039 — Proposed; the wider thesis and neighbouring accounts, cited as open -->
# THEORY-973: In small attention-only transformer language models of two to six layers, in-context learning, measured as the loss at token 500 minus the loss at token 50, appears abruptly in one early window of training in which induction heads form, and ablating those heads at test time removes nearly all of it; one-layer models show neither, and letting a single layer attend by the previous token brings the jump to one-layer models and moves it earlier in two-layer ones

## Source

Olsson, Elhage, Nanda, Joseph et al. (2022), *In-context learning and
induction heads*, [LIT-1538](../literature.d/LIT-1538.md), read in full in [NOTE-1173](../notes.d/NOTE-1173.md) from the
arXiv print of the Transformer Circuits article. The account rests on
Arguments 1–3, the smeared-key models, Model Details, the data-collection
appendix (pattern-preserving ablation) and the small attention-only rows
of the Model Analysis Table.

## What was actually shown

**The models.** Attention-only transformers of one to six layers, d_model
768, 12 heads per layer, trained once each for 10,000 steps (about 10¹⁰
tokens) with 200 snapshots, and one- and two-layer "smeared key" variants
trained the same way. Everything is measured on the same 10,000 examples of
512 tokens.

**The measures.** The in-context learning score is the mean loss at token
500 minus the mean loss at token 50. An induction head is a head that, on
repeated random tokens, attends to the token that followed an earlier copy
of the present one (prefix matching) and raises that token's logit
(copying).

**Co-occurrence.** In every model with two or more layers the score falls
from above −0.15 to about −0.4 nats within one early window and then stays
there. In the same window heads acquire high prefix-matching scores, the
training loss has its one non-convex stretch, and the models' trajectories
in the PCA of per-token losses turn. The one-layer model shows none of the
four.

**Co-perturbation.** A smeared key, k_j = σ(α)k_j + (1 − σ(α))k_{j−1} with
α trained per head, lets a head attend by the previous token without a
second layer. With it the one-layer model's score drops abruptly too, and
the two-layer model's drop comes earlier than in the vanilla model.

**Ablation.** Zeroing one head's output with all attention patterns frozen
shows the induction heads carrying the score: "almost all the in-context
learning in small attention-only models appears to come from these
induction heads! This begins at the start of the phase change, and remains
true through the end of training." In an attention-only model with frozen
patterns, the logits are a sum of per-head terms and a direct path term up
to LayerNorm rescaling, so single-head ablations are close to an exact
decomposition. That is why the authors treat these ablations as dispositive
here and not for models with MLPs.

**What could have come out otherwise.** The score could have grown
gradually, or with depth. The jump could have appeared in one-layer models,
or stayed put under smeared keys. Ablating the induction heads could have
left most of the score, with other copying heads carrying it; the authors
note that basic copying heads exist in one-layer models, which never make
the jump.

## What this does not say

- **Not about models with MLPs, or large models.** There the evidence is
  correlational, anecdotal or by analogy, and the authors say so. That
  thesis is [THEORY-990](THEORY-990.md).
- **Not that induction drives the transition rather than accompanying
  it.** The authors name a shared cause they cannot exclude: the transition
  may be "the point at which the model learns how to compose layers through
  the residual stream", of which induction heads are one product. The
  ablations show that induction heads carry the score afterwards, not
  that their formation caused the bump.
- **Not about few-shot task learning.** The score measures loss improvement
  with position. A model can raise it by getting worse at ordinary
  prediction: ablating most non-induction heads increases it (footnote 17).
- **Not robust to data order.** Each model was trained once, and all models
  saw the same examples in the same order. The window also overlaps the
  learning-rate warm-up, which ends at 1.5 × 10⁹ tokens.
- **Not that sequential onset comes from the optimizer.** No optimizer is
  varied. The timing evidence here is a dependency: the jump waits on a
  composition, and removing the need to compose moves it.

## Connections

- **[QUESTION-039](../questions.d/QUESTION-039.md): answers in part.** For in-context learning in small
  attention-only transformers, the moment of acquisition is set by when
  a two-head composition becomes available. It does not say what sets
  that, and it is one model family.
- **[THEORY-253](THEORY-253.md) and [THEORY-783](THEORY-783.md).** Those hold the optimizer as a source of
  sequential onset, beside dependence between skills. This account is a
  measured case of the second kind: removing a dependency moves the onset.
- **[QUESTION-275](../questions.d/QUESTION-275.md).** This is the setting the question names first, and
  its circuit-only measurements (per-head scores and ablations at every
  snapshot) are a baseline the question's coupled model has to beat.
- **[THEORY-169](THEORY-169.md).** The in-context learning here is conditioning on fixed
  weights, the case [THEORY-169](THEORY-169.md) describes for single layers.
- **[THEORY-977](THEORY-977.md).** The same mechanism read from the weights of one
  trained two-layer model (Elhage et al., [LIT-1534](../literature.d/LIT-1534.md)): K-composition with
  a previous-token head. This account says when the mechanism forms; that
  one says what it is once formed.
- **Refinements of the mechanism, not of its timing.** Causal scrubbing's
  induction result, 35% of the loss recovered by the naive
  previous-token-key hypothesis and 86% once three pathways are added,
  held only from a summary ([NOTE-1168](../notes.d/NOTE-1168.md)); and induction at the level of
  sparse-autoencoder features, in pieces, in Pythia-70M
  ([NOTE-1187](../notes.d/NOTE-1187.md)). Neither measures when the composition becomes
  available.
