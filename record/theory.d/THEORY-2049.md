---
number: 2049
status: Proposed
formerly:
- THEORY-tmpv904w
title: 'Test-time training matches attention, not recall'
statement: >-
  Tandon and colleagues show that a sliding-window Transformer which keeps
  training on its context by next-token prediction at test time, from an
  initialization meta-learned for its loss after those updates, matches full
  attention's improvement in language-modelling loss with context length up
  to 128K at 3B parameters with constant per-token latency, while losing to
  full attention on verbatim retrieval, and that without the meta-learned
  initialization the test-time updates add little
version: 1
source:
- LIT-2801
tags:
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-095
corroborates:
- CLAIM-118
promote_when: >-
  An independent replication at 1B parameters or more shows TTT-E2E's loss
  gap to full attention staying flat from 8K to 128K context, its needle-
  in-a-haystack retrieval near the sliding-window baseline, and TTT on an
  ordinarily pretrained initialization falling well short of TTT-E2E.
summary: >-
  From the reading of [LIT-2801](../literature.d/LIT-2801.md) in [NOTE-2087](../notes.d/NOTE-2087.md). Tandon, Dalal, Li,
  Koceja, Rød, ... and Sun (2025), arXiv 2512.23675. A sliding-window
  Transformer keeps learning at test time by next-token prediction on its
  context, compressing it into the MLP weights of its last quarter of
  blocks, from an initialization meta-learned for the loss after those
  updates. At 3B parameters it keeps full attention's scaling of loss with
  context length to 128K at constant per-token latency (2.7× faster at
  128K), but loses to full attention on needle-in-a-haystack recall, and
  training is 3.4× slower at 8K. Here because A58 cited it for the owner's
  U26 case: its per-sequence weights and meta-learned initialization
  separate signal from interpreter ([CLAIM-118](../claims.d/CLAIM-118.md)), it prices work moved from
  inference into training ([QUESTION-095](../questions.d/QUESTION-095.md)), and its finding that test-time
  updates on an ordinarily trained model add little bears on the TTT arm
  of [CASE-294](../cases.d/CASE-294.md). Read in its NOTE.
---
<!-- inactive-ok-file: CASE-294 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2049: Test-time training matches attention, not recall

## The account

Long context is handled by compressing it into weights: the MLPs of the last quarter of blocks take a gradient step on the next-token loss of each 1K-token mini-batch, while an 8K sliding window holds the recent tokens. The initialization is trained by meta-learning on the loss after these updates. At 3B parameters and 164B training tokens, the loss gap to full attention stays the same from 8K to 128K, where Mamba 2, Gated DeltaNet and others fall behind; prefill is 2.7× faster at 128K. The price is paid in training (3.4× slower at 8K) and in recall: on needle-in-a-haystack tests it is no better than a sliding window.

## What it does not show

Downstream task ability beyond loss and synthetic recall; behaviour above 3B parameters or with other data; that the updated weights act as memory across documents (they are reset at document boundaries); that test-time updates help an initialization not meta-learned for them (the toy says they help little).
