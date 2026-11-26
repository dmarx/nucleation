---
status: Open
title: 'Intervene on the decoded in-context training set to test mesa-optimization'
stage: idea
priority: medium
method:
- empirical
tags:
- learning-theory
- representation-learning
date: '2026-11-26'
line:
- pragmatic-transport
advances:
- THEORY-tmp8xq94
- CLAIM-118
summary: >-
  Offered on 2026-11-26 from the von Oswald et al. reading ([NOTE-tmpcktnn](../notes.d/NOTE-tmpcktnn.md)): [THEORY-tmp8xq94](../theory.d/THEORY-tmp8xq94.md)'s promote_when asks for an intervention, not only probes or loss matching. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp8xq94 — new or Proposed; the entries this lead would advance and the works it names -->

# LEAD-tmprek0f: Intervene on the decoded in-context training set to test mesa-optimization

## What it would do

In a small Transformer trained as in [LIT-tmpuv16r](../literature.d/LIT-tmpuv16r.md), edit the representations
that probes decode as the bound in-context training set, or as the
preconditioned inputs. Then check whether the model's predictions move as
the identified optimizer would predict from the edited data.

- **For mesa-optimization:** predictions follow the optimizer on the
  edited data.
- **Against it:** the edits leave predictions unchanged, or move them in
  ways no optimizer over the edited set predicts.

The fixed-teacher control (Appendix E.2) gives a baseline for [CLAIM-118](../claims.d/CLAIM-118.md),
in which the information sits in the weights.
