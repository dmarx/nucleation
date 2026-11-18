---
number: 1899
status: Proposed
formerly:
- THEORY-tmpr8g5y
promote_when: >-
  An independent replication of forward and reverse divergence-thresholded
  cross-sampling on another base–RLVR model pair and benchmark, showing
  most token positions at near-zero divergence and intervention at under
  about 10% of tokens moving accuracy most of the way from one model's
  level to the other's in both directions.
title: 'Meng and colleagues find that RLVR fine-tuning of Qwen2.5-32B leaves most next-token distributions nearly unchanged, over 83% of positions at near-zero Jensen–Shannon divergence under DAPO and over 98% under SimpleRL, and that sampling the RL model''s token only at the highest-divergence positions, a few percent of tokens, raises the base model to RL-level accuracy on AIME while sampling the base model''s token there drops the RL model to base level, RLVR rarely promoting tokens the base model found unlikely'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2640
bears_on:
- QUESTION-392
summary: >-
  Meng et al. (2026), [LIT-2640](../literature.d/LIT-2640.md), read in [NOTE-1966](../notes.d/NOTE-1966.md). The difference
  between base and RLVR models is sparse and sufficient: a few percent of
  decisions carry it. Token-level support for Yue et al.'s sharpening
  ([THEORY-1880](THEORY-1880.md)). No CLAIM is listed as corroborated: its bearing on
  [CLAIM-576](../claims.d/CLAIM-576.md) is indirect, since it measures reallocation, not whether new
  paths are added. The wording is the reader's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-1880 — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this account bears on indirectly -->

# THEORY-1899: Meng and colleagues find that RLVR fine-tuning of Qwen2.5-32B leaves most next-token distributions nearly unchanged, over 83% of positions at near-zero Jensen–Shannon divergence under DAPO and over 98% under SimpleRL, and that sampling the RL model's token only at the highest-divergence positions, a few percent of tokens, raises the base model to RL-level accuracy on AIME while sampling the base model's token there drops the RL model to base level, RLVR rarely promoting tokens the base model found unlikely

## The result

Meng et al. (2026), [LIT-2640](../literature.d/LIT-2640.md); read in [NOTE-1966](../notes.d/NOTE-1966.md).

Token-level JS divergence between base and RL next-token distributions,
on the models' own AIME generations, is near zero at most positions
(§2.2). Cross-sampling swaps in the other model's token only where
divergence exceeds a threshold. Forward, under SimpleRL, "fewer than 4%"
of tokens close the gap from about 8% to about 25% on AIME 2024; under
DAPO about 7.8% (some 280 tokens) take it from 8% to over 44%. Reverse,
about 5% to 10% collapse the RL model to base level (§3.2). At divergent
positions under DAPO only about 5% of RL top-1 tokens have base
probability below 0.01 (§4.2). Either half could have failed: the gap could
have needed dense changes, or survived the reverse swap.

## What it does not show

- That RL adds no new reasoning path. The rare promotions of unlikely
  tokens "may still be important" (§7), and pass@k at large k is not
  measured here.
- Which semantic choices the critical positions are (§2.5, not read).
- Generality beyond the model pairs and two AIME years reported.
- The KL-regularized optimum: DAPO trains without KL, and the paper does
  not state the closed form.
