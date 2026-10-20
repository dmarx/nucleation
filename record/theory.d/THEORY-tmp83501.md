---
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

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "A result that separates the number of examples a deep network needs from the counting of the grammar, by moving the input–label correlations while n_c, m and L stay fixed: for instance, non-uniform production probabilities that make some tuples' class statistics detectable earlier than others, with the training-set sizes at which each level becomes synonym-invariant, and at which test error falls, tracking the predicted detection thresholds rather than n_c m^L. Or a proof that gradient descent on a deep network learns the Random Hierarchy Model from a number of examples of order n_c m^L, polynomial in the input dimension. Further collapses of learning curves on n_c m^L at other parameter values cannot settle it, because the threshold and the grammar's size are the same number there."

# The claim. Repeat it as the body's `# THEORY-tmp83501:` heading; the lint checks
# that the two agree.
title: 'Deep networks learn hierarchically generated data from a number of examples set by when the correlations between input patches and the class rise above sampling noise, so detecting those correlations is how they learn the grammar, as Cagnetta and coauthors propose'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- learning-theory
- compositionality
- representation-learning

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-877

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Cagnetta, Petrini, Tomasini, Favero and Wyart (2023), [LIT-877](../literature.d/LIT-877.md), propose that deep networks learn compositional data by detecting the correlations between input patches and the class, and that the sample complexity is where those correlations emerge from sampling noise. The record holds as shown, in [THEORY-195](THEORY-195.md), the measured law and the synonym-invariance it coincides with. This is the mechanism, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-195
answers:
- QUESTION-165
---

<!-- inactive-ok-file: THEORY-201 — Proposed; the companion mechanism for next-token prediction, cited as open -->

# THEORY-tmp83501: Deep networks learn hierarchically generated data from a number of examples set by when the correlations between input patches and the class rise above sampling noise, so detecting those correlations is how they learn the grammar, as Cagnetta and coauthors propose

## Source

Cagnetta, Petrini, Tomasini, Favero and Wyart (2023; Phys. Rev. X 2024),
[LIT-877](../literature.d/LIT-877.md), read in [NOTE-677](../notes.d/NOTE-677.md). The paper's title, "How deep neural networks
learn compositional data", and its argument present correlation detection
as the mechanism: synonymous tuples share class statistics, and a network
groups them once those statistics rise above sampling noise.

## What is asserted

That the number of examples a deep feature-learning network needs to learn
data from a random hierarchical grammar is set by when the input-patch
class correlations become detectable, and that detecting them is how the
network comes to represent the grammar's hidden symbols.

## What the record holds toward it

[THEORY-195](THEORY-195.md), Active, is the measured part: on the Random Hierarchy Model
with s = 2, L ≤ 4 and small v, deep CNNs matched to the tree reach a tenth
of chance error from about n_c m^L examples, where their hidden layers
become synonym-invariant, while shallow and lazy learners need an
exponential number and deep ones fail when the correlations are removed.
In that model the correlation threshold and the grammar's size are the
same expression, so the data cannot say which sets the number;
[QUESTION-165](../questions.d/QUESTION-165.md) asks for the separating test. [THEORY-201](THEORY-201.md) proposes the
corresponding mechanism for next-token prediction, and [THEORY-778](THEORY-778.md) holds
its derived correlation statistics.

## What this does not say

- Not that end-to-end training reaches the better rate a clustering
  algorithm attains; the authors leave it open.
- Not that depth alone escapes the curse of dimensionality.

## What would confirm or reject it

Confirmed by the promote_when: moving the correlations with n_c, m and L
fixed and finding that sample complexity tracks the detection threshold,
or a proof for gradient descent. Rejected if, with the correlations moved
and the grammar fixed, sample complexity stays at n_c m^L.
