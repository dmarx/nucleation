---
number: 1881
status: Proposed
formerly:
- THEORY-tmpc29mv
promote_when: >-
  A replication, at the same or larger scale and on a corpus other than
  OpenWebText, in which the normalized architecture (all embeddings,
  hidden states and weight rows on the unit hypersphere, residual sums
  replaced by learned per-dimension interpolation toward the normalized
  block output and renormalization) reaches a tuned pre-norm baseline's
  validation loss in several times fewer training tokens, with the gap
  growing with context length. Refuted if a tuned baseline closes most of
  the token gap at matched scale. Wall-clock comparisons do not bear on
  the title, which is about tokens.
title: 'Hypersphere-normalized GPT trains 4–20× faster'
statement: >-
  In decoder-only transformers of 0.5B and 1B parameters trained on
  OpenWebText, normalizing all embeddings, hidden states and weight rows to
  the unit hypersphere and replacing each residual addition by a learned
  per-dimension interpolation toward the normalized block output followed by
  renormalization reaches the baseline GPT's validation loss in about 4, 10
  and 20 times fewer training tokens at context lengths of 1k, 4k and 8k, as
  Loshchilov, Hsieh, Sun and Ginsburg report
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Filed Proposed from NOTE-1971, the reading of nGPT's main text in
    full on 2026-11-15.
tags:
- representation-learning
date: '2026-11-15'
source:
- LIT-2616
summary: >-
  Loshchilov, Hsieh, Sun & Ginsburg (ICLR 2025), [LIT-2616](../literature.d/LIT-2616.md), read in
  [NOTE-1971](../notes.d/NOTE-1971.md): a transformer kept on the unit hypersphere, each block
  moving the state a learned fraction toward its normalized output, trains
  to GPT's loss in 4–20 times fewer tokens at two scales on one corpus, at
  60–80% more time per step. The optimizer reading of the layers is an
  interpretation. The wording is the reader's; adopting it is the owner's
  call.
---

# THEORY-1881: Hypersphere-normalized GPT trains 4–20× faster

## Source

Loshchilov, Hsieh, Sun & Ginsburg (2024), [LIT-2616](../literature.d/LIT-2616.md); read in
[NOTE-1971](../notes.d/NOTE-1971.md).

## The result

Against a GPT baseline at its best learning rate, at 0.5B and 1B
parameters on OpenWebText: "approximately 4x, 10x, and 20x faster at
context lengths of 1k, 4k, and 8k tokens" (§3.1), counted in tokens; at 1B
and 4k, nGPT matches after 20k iterations the loss GPT reaches after 200k.
The learned steps are modest, 20–30% of the way (§3.2). Each step costs
60–80% more time (A.5).

## What it does not show

- That the speed-up holds at larger scale, on other corpora or against
  other tuned baselines; the authors note saturation in the longest runs.
- That it holds in wall-clock time.
- That the layers are optimizer steps of any objective: the reading of
  the block output as a gradient target is stipulated.
- Anything about representations as trajectories across inputs, such as
  branched flow.
