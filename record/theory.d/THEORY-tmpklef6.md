---
status: Proposed
title: 'Acharya, Rimal and Dhakal find that in 17 decoder-only language models, word-level concept directions taken from final-layer activations put less of their Euclidean energy in the top eigendirections of the unembedding''s regularized second moment, the unembedding''s right singular basis, than a uniform-in-variance baseline, and more in its tail than norm-matched random directions in 13 of the 17, while differences of the same concepts'' unembedding rows lean toward the top eigendirections'
promote_when: >-
  An independent replication, or the authors' released code run on at
  least the four models of Table 10, reproduces both the activation-side
  tail alignment against norm-matched random directions in most models and
  the opposite sign for unembedding-row contrasts against random token
  pairs.
version: 1
tags:
- representation-learning
- information-geometry
date: '2026-11-21'
source:
- LIT-2959
summary: >-
  Acharya, Rimal and Dhakal, [LIT-2959](../literature.d/LIT-2959.md), read in [NOTE-tmpwvltp](../notes.d/NOTE-tmpwvltp.md). Where
  concept vectors point in the logit metric's eigenbasis, from the
  activation side and the vocabulary side. A placement of directions, not
  a measure of information or of importance; the paper's own effect
  measures run with the metric. Its sign flip is what Park, Choe and
  Veitch's map predicts ([CLAIM-tmpqy8mq](../claims.d/CLAIM-tmpqy8mq.md)).
---
<!-- inactive-ok-file: CLAIM-tmpqy8mq — Proposed or new; the reading this account comes from and the claim filed on its sign flip -->

# THEORY-tmpklef6: Acharya, Rimal and Dhakal find that in 17 decoder-only language models, word-level concept directions taken from final-layer activations put less of their Euclidean energy in the top eigendirections of the unembedding's regularized second moment, the unembedding's right singular basis, than a uniform-in-variance baseline, and more in its tail than norm-matched random directions in 13 of the 17, while differences of the same concepts' unembedding rows lean toward the top eigendirections

## Source

Acharya, Rimal and Dhakal, "Concepts Whisper: Spectral Anti-Concentration
and the Dual Geometry of Transformer Representations", EMNLP 2026,
[LIT-2959](../literature.d/LIT-2959.md), read from arXiv 2605.01609v2 in [NOTE-tmpwvltp](../notes.d/NOTE-tmpwvltp.md).

## What was actually shown

- The spectrum is "the regularized uncentered second moment of the
  unembedding rows" (Eq. 1), WᵀW up to scale and ridge.
- Raw Gini deviation negative in all 17 models (mean −0.282); since random
  directions already score −0.16 to −0.28, the matched null is the test:
  "more tail-aligned than their matched nulls in 13 of 17 models, with a
  mean true-minus-null Gini gap of −0.082" (§5).
- Unembedding-row contrasts: mean +0.07 against −0.10 for random token
  pairs, p < 10⁻⁴ on four models (§7).

What could have failed: concept directions could have matched their
random nulls, or both sides could have leaned the same way; in 4 of 17
models the first happened.

## What this does not say

- Not that concept information lives in the tail: no decoding from the
  tail except POS probing, which favours the head.
- Not representation variance: the spectrum is the unembedding's.
- Not that tail directions are causally important: steering strength is
  "untested".
- Not about learning: the only trajectory is through depth.
- Not invariant under invertible maps of the residual stream ([THEORY-018](THEORY-018.md)).
