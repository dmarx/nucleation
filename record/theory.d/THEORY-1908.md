---
number: 1908
status: Proposed
formerly:
- THEORY-tmpxu3kz
promote_when: >-
  An independent prolonged-RL run from a different start model, reported
  with pass@k up to k of at least 128 per task, showing tasks at zero
  pass@128 before training and above it after, and a negative correlation
  across tasks between the start model's pass@128 and its gain, with the
  gain nil or negative on math.
title: 'Liu and colleagues report that more than 2,000 steps of RL on a diverse task suite, with decoupled clipping and dynamic sampling, a KL penalty and periodic resets of the reference policy, raise DeepSeek-R1-Distill-Qwen-1.5B''s pass@k at k up to 128 on many tasks, including some where the starting model solved nothing, with the gain larger where the starting model''s pass@128 was lower and nil or negative on math'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2623
bounds:
- CLAIM-695
bears_on:
- QUESTION-392
- QUESTION-279
summary: >-
  Liu et al. (2025), [LIT-2623](../literature.d/LIT-2623.md), read in [NOTE-1982](../notes.d/NOTE-1982.md). The counterclaim
  to Yue et al. ([THEORY-1880](THEORY-1880.md)), stated in the terms the paper's
  evidence supports: a distilled start model, k at most 128 and agreement
  on math. Not a rival of Yue's account, since both can be right on their
  own conditions. It is the test case for [CLAIM-576](../claims.d/CLAIM-576.md), whether training ever
  changes what is reachable rather than what is affordable, but does not
  settle it, since a target unreached at k = 128 may be reached at larger
  k; so no CLAIM is listed as corroborated. The wording is the reader's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1880 — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this account tests -->

# THEORY-1908: Liu and colleagues report that more than 2,000 steps of RL on a diverse task suite, with decoupled clipping and dynamic sampling, a KL penalty and periodic resets of the reference policy, raise DeepSeek-R1-Distill-Qwen-1.5B's pass@k at k up to 128 on many tasks, including some where the starting model solved nothing, with the gain larger where the starting model's pass@128 was lower and nil or negative on math

## The result

Liu et al. (2025), [LIT-2623](../literature.d/LIT-2623.md); read in [NOTE-1982](../notes.d/NOTE-1982.md).

Training runs past 2k steps on 136K problems in five domains, with
DAPO's components, a high rollout temperature, a KL penalty (Eq. 4) and
hard resets of the reference policy. The trained model beats its start
"across a wide range of pass@k evaluations, including scenarios where base
models fail entirely regardless of the number of attempts" (abstract).
Across tasks the gain correlates negatively with the start model's
pass@128 (§4.1), and on math the final model shows "decreased or unchanged
reasoning capacity compared to the base model" (§4.2). The experiment
could have shown narrowing everywhere, as Yue et al. found for short runs.

## What it does not show

- That RL expands the boundary of a pretrained base: the start model is
  distilled from a stronger reasoner.
- That the start model cannot solve a task that went from zero to positive: pass@k was read
  to k = 128, not Yue et al.'s 1024, and failure at finite k is not
  unsolvability ([QUESTION-279](../questions.d/QUESTION-279.md)).
- That the expansion is general: it is largest where the start model is
  weak, absent on math, and shown on one 1.5B model.
- An exponential tilt of a fixed reference: with resets there is no fixed
  π0.
