---
status: Open
title: "Test the owner's truncated-band picture in trained language models: whether the unembedding's top singular directions track token frequency as stop words do, and where a low-signal floor sits below the discriminating band"
version: 1
stage: idea
method:
- empirical
tags:
- representation-learning
- linguistics
date: '2026-11-22'
line:
- learned-structure
advances:
- CLAIM-tmp2r6ur
summary: >-
  The test of the two halves of the owner's truncated-band claim ([CLAIM-tmp2r6ur](../claims.d/CLAIM-tmp2r6ur.md))
  that the record's readings leave open. (1) Stop words: project each
  token's unembedding row onto the top singular directions and correlate
  with log token frequency in the training corpus; the claim predicts a
  strong correlation for the top band and not for the lower retained
  band. (2) The floor: in models without Qwen's degenerate normalization
  coordinates, sweep the cut from the bottom and track Xu's
  discriminating ratio K, to see whether a floor below the band dilutes
  it there too. Open models with released checkpoints (the Pythia suite
  Xu uses) suffice. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2r6ur — Proposed; the claim this would test -->

# LEAD-tmptgrc7: Test the owner's truncated-band picture in trained language models: whether the unembedding's top singular directions track token frequency as stop words do, and where a low-signal floor sits below the discriminating band

**Design.**
1. **The stop-word half.** For each model, take the centred, norm-folded unembedding, as Xu builds it. Project every token's row onto each singular band, then correlate the projection's magnitude with the token's log frequency. The claim predicts the top band tracks frequency and the lower retained band does not.
2. **The floor.** Sweep a lower cut through the bottom of the spectrum and recompute Xu's K at each cut, against equal-length random changes drawn above the cut. The claim predicts K rises as the floor is removed, then falls once the cut eats into the discriminating band.

**What would count against.** No frequency structure in the top band, or K flat or falling as the floor is removed.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
