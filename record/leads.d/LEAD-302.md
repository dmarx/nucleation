---
number: 302
status: Open
formerly:
- LEAD-tmpkh0uz
title: 'Test whether question discovery valued on a different later task beats same-task valuation'
stage: idea
priority: medium
method:
- empirical
tags:
- learning-theory
- representation-learning
date: '2026-11-26'
line:
- learned-structure
- realizability
advances:
- CLAIM-756
- THEORY-2318
summary: >-
  Offered on 2026-11-26 from the Veeriah et al. reading ([NOTE-2427](../notes.d/NOTE-2427.md)): the paper values a learning step by its effect on later learning of the same fixed task, which is a narrow form of [CLAIM-756](../claims.d/CLAIM-756.md); the claim's own case is a later acquisition of a different task. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

# LEAD-302: Test whether question discovery valued on a different later task beats same-task valuation

## What it would do

Meta-learn auxiliary questions, as in [LIT-3295](../literature.d/LIT-3295.md), with the meta-loss
taken over the learning of a held-out task family, not the training task.
Compare:

- questions valued by training-task speed-up;
- questions valued by speed-up on the later family;
- fixed and random questions.

The test, on held-out later tasks, is whether valuing by effect on
different later acquisitions picks questions that same-task valuation
misses, and that rank lower on present performance. That is [CLAIM-756](../claims.d/CLAIM-756.md)'s
reversal.
