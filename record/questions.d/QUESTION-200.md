---
number: 200
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpkpb79

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Is the subspace-patching effect measured in GPT-2 Small's layer-8 MLP an instance of the dormant-direction construction, rather than two cancelling subspaces in that component, and does its dependence on the disconnected component replicate in a second model family?"

version: 1
tags:
- causality
- representation-learning
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'pragmatic-transport'

# refines: [QUESTION-000]   # the broader question this sharpens

refines:
- QUESTION-030
summary: >-
  The promotion condition formerly on [THEORY-282](../theory.d/THEORY-282.md). [THEORY-282](../theory.d/THEORY-282.md) was promoted
  on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) for what its construction proves: a subspace
  patch can reproduce a variable's output effect without localizing it.
  Whether the measured cases are such patches, rather than two cancelling
  subspaces in the patched component, is open.
---

<!-- unresolved-ok-file: QUESTION-000 — the placeholder a new document replaces -->

# QUESTION-200: Is the subspace-patching effect measured in GPT-2 Small's layer-8 MLP an instance of the dormant-direction construction, rather than two cancelling subspaces in that component, and does its dependence on the disconnected component replicate in a second model family?

## Why it is a question

[THEORY-282](../theory.d/THEORY-282.md) holds the construction. A patch along a direction that mixes
a component the next layer cannot read with one that is constant on the
data moves the output as changing the variable would. Neither part
alone has any effect. Makelov, Lange and Nanda then measure the same
signature in GPT-2 Small's layer-8 MLP on indirect-object identification:
46.7% FLDD, falling to 13.5% without the null-space part. They find it
again in GPT2-XL's MLPs on factual recall. They leave open a rival
reading: two subspaces in the same component that both mediate the
feature and cancel on the data. The reply by Wu et al. contests the
label, not the measurements. Until 2026-10-20 this was [THEORY-282](../theory.d/THEORY-282.md)'s
promote_when.

## What would answer it

- A replication, in a second model family, of the dependence on the
  disconnected component, for a feature whose mediating location is
  known independently.
- A test that moves the two candidate subspaces while holding the
  component's total output fixed on the data, which separates the
  dormant-direction reading from cancellation.

Against it: interventions that stay on the data distribution and show
that the component the illusory direction lives in does take part in
the behaviour.

What would not answer it: more successful patches, or more directions
that fail the rowspace test, since the construction predicts both.
