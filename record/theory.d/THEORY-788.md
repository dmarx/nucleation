---
number: 788
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'
formerly:
- THEORY-tmpnkoyu

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: 'Replication outside the protocol of LIT-618, read in the record. That protocol had balanced classes, no augmentation, dropout removed, one run per learning rate and the best run shown. Measurements of NC1 and NC2 through the terminal phase under augmentation, label noise and several seeds per cell would promote this, and of NC1 under class imbalance. NC2 is predicted for balanced classes only: under imbalance the geometry to test is that of THEORY-286, not equiangularity. So would a held paper that derives collapse as the limit of gradient descent on cross-entropy, which would turn the measured regularity into an account. No held paper meets that yet: LIT-974 derives collapse for MSE under a re-whitened flow, and LIT-994 gives an endpoint, not a gradient-descent derivation. The claim is refuted if standard training run well past zero error leaves within-class variability of last-layer features flat, or, with balanced classes, leaves the centred class means far from equiangular. Further runs under the original protocol cannot settle it. Nor can the theorems, which assume the collapsed end state.'

# The claim. Repeat it as the body's `# THEORY-788:` heading; the lint checks
# that the two agree.
title: 'Training a deep classifier past zero training error generally collapses its last-layer features onto their class means, drives the centred means toward a simplex equiangular tight frame aligned with the classifier, and makes the decision nearest class mean, as Papyan, Han and Donoho propose from their runs'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- representation-learning
- learning-theory
- information-theory
- anthology-candidate

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-618
- LIT-613

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Papyan, Han and Donoho (2020), [LIT-618](../literature.d/LIT-618.md), title their paper on the "prevalence" of neural collapse and present it as a pervasive outcome of the terminal phase of training. The record holds as shown, in [THEORY-083](THEORY-083.md), only what their runs measured: three architectures with cross-entropy on seven balanced datasets without augmentation. This is the general law, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-083
answers:
- QUESTION-202
---

<!-- inactive-ok-file: THEORY-286 — Proposed; the imbalanced-class geometry this claim defers to, cited as open -->

# THEORY-788: Training a deep classifier past zero training error generally collapses its last-layer features onto their class means, drives the centred means toward a simplex equiangular tight frame aligned with the classifier, and makes the decision nearest class mean, as Papyan, Han and Donoho propose from their runs

## Source

Papyan, Han and Donoho (2020, PNAS), [LIT-618](../literature.d/LIT-618.md), read in [NOTE-476](../notes.d/NOTE-476.md). Their
title and discussion present neural collapse (NC1 to NC4) as prevalent in
the terminal phase of canonical deep-learning training, not as a property
of their particular runs. [LIT-613](../literature.d/LIT-613.md) is the companion reading the narrowed
entry also rests on.

## What is asserted

That standard training of a deep classifier well past zero training error
generally drives within-class variability of last-layer features to zero
(NC1), the centred class means to a simplex equiangular tight frame (NC2),
the classifier into alignment with them (NC3), and the decision to nearest
class mean (NC4), across architectures, datasets and training details.

## What the record holds toward it

[THEORY-083](THEORY-083.md), Active, is the measured part: in 480 VGG, ResNet and DenseNet
runs with cross-entropy on seven balanced datasets without augmentation,
the four phenomena moved in the predicted direction, nearly to completion
on the four easier datasets and only partly on ImageNet. [QUESTION-202](../questions.d/QUESTION-202.md) asks
whether collapse holds outside that protocol and whether gradient descent
on cross-entropy provably reaches it. Under class imbalance the record's
expected geometry is [THEORY-286](THEORY-286.md)'s, not the simplex ETF, so NC2 as stated
here is a claim for balanced classes.

## What this does not say

- Not why collapse happens. The held theorems assume the collapsed state.
- Not that the terminal phase improves generalization; the measured test
  gains are small and without seeds ([THEORY-083](THEORY-083.md)).

## What would confirm or reject it

Confirmed by the promote_when: collapse measured outside the original
protocol, under augmentation, label noise and several seeds, or a
gradient-descent derivation for cross-entropy. Rejected if standard
training run well past zero error leaves within-class variability flat or,
with balanced classes, the means far from equiangular.
