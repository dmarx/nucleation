---
status: Open
title: "Test the owner's truncated-band picture in trained language models: whether the unembedding's top singular directions track token frequency as stop words do, and where a low-signal floor sits below the discriminating band"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2990 (NOTE-tmpzethm, THEORY-tmphbp5a): the
    design now records training regime (step size) and training stage as
    variables, since in Park and colleagues' experiments top directions
    track the data's principal components only in the large-step regime.
    That also lets the test separate the owner's claim from the rival
    reading CLAIM-tmp9atj9.
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
- CLAIM-tmp9atj9
- CLAIM-tmpufbx6
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
  Xu uses) suffice. Since 2026-11-22 it records step size and training
  stage, after Park and colleagues (LIT-2990), so as to tell the claim from
  its rival readings CLAIM-tmp9atj9 and CLAIM-tmpufbx6. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2r6ur CLAIM-tmp9atj9 CLAIM-tmpufbx6 THEORY-tmphbp5a THEORY-tmpwtoad — Proposed; the claim this would test, its two rival readings and the readings behind them -->

# LEAD-tmptgrc7: Test the owner's truncated-band picture in trained language models: whether the unembedding's top singular directions track token frequency as stop words do, and where a low-signal floor sits below the discriminating band

**Design.**
1. **The stop-word half.** For each model, take the centred, norm-folded unembedding, as Xu builds it. Project every token's row onto each singular band, then correlate the projection's magnitude with the token's log frequency. The claim predicts the top band tracks frequency and the lower retained band does not.
2. **The floor.** Sweep a lower cut through the bottom of the spectrum and recompute Xu's K at each cut, against equal-length random changes drawn above the cut. The claim predicts K rises as the floor is removed, then falls once the cut eats into the discriminating band.

3. **Regime and stage, recorded** (added 2026-11-22, version 2). Record each model's step size (peak learning rate and schedule) and run both measurements across checkpoints of one training run, early to final. In Park and colleagues' MLPs (LIT-2990, THEORY-tmphbp5a, Fig. 16) the leading first-layer direction overlaps the data's first principal component at 0.68 in the large-step regime, which converges to a worse minimum, and at 0.056 in the well-trained phase. The owner's claim predicts the frequency correlation of the top band in well-trained final checkpoints; the rival CLAIM-tmp9atj9 predicts it strongest early or at large steps and fading with training. The Pythia suite's released checkpoints serve for stage.
4. **The floor, with the estimator controlled.** Where the floor is measured from a sample spectrum, repeat at two sample sizes: the rival CLAIM-tmpufbx6 predicts the floor's edge moves with the sample, the owner's claim that it stays.

**What would count against.** No frequency structure in the top band, or K flat or falling as the floor is removed.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
