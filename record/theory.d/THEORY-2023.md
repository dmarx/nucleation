---
number: 2023
status: Proposed
formerly:
- THEORY-tmpddlli
title: 'Lu and Kankanhalli show that a policy trained to decide, per query, whether to answer directly, reuse a stored test-time-trained LoRA skill or build a new one with one of five test-time-training methods roughly doubles a 7B model''s verified utility on a benchmark enriched for queries where adaptation helps, cuts adaptation compute by about 30% without loss of utility under a moderate compute penalty, and amortizes skill construction through reuse'
version: 1
source:
- LIT-2806
tags:
- representation-learning
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-095
corroborates:
- CLAIM-303
promote_when: >-
  An independent evaluation, on the authors' benchmark or a comparable
  enriched stream, reproduces a learned policy beating every fixed test-
  time-training method and direct answering on overall utility, with
  reused skills helping far more often than they harm and a compute
  penalty lowering adaptation compute without lowering utility.
summary: >-
  From the reading of [LIT-2806](../literature.d/LIT-2806.md) in [NOTE-2084](../notes.d/NOTE-2084.md). Lu and Kankanhalli
  (2026), arXiv 2610.12002. Five test-time-training methods become tools
  that produce reusable LoRA skills over a frozen backbone, and a policy
  trained by distillation and GRPO decides per query whether to answer
  directly, reuse a skill or build one, on utility gain minus a compute
  penalty. On a benchmark deliberately enriched for queries where
  adaptation helps, it raises Qwen2.5-7B's verified utility from 0.256 to
  0.510, cuts adaptation compute by about 30% under a moderate penalty
  without losing utility, and amortizes skill construction through reuse
  (61 of 100 reuses help, 1 harms). Here because A58 cited it for learning
  when to update: its rule, build when gain amortized over expected reuse
  covers the compute, is [QUESTION-095](../questions.d/QUESTION-095.md)'s trade and [CLAIM-303](../claims.d/CLAIM-303.md)'s criterion
  for parameter skills. Read in its NOTE.
---

# THEORY-2023: Lu and Kankanhalli show that a policy trained to decide, per query, whether to answer directly, reuse a stored test-time-trained LoRA skill or build a new one with one of five test-time-training methods roughly doubles a 7B model's verified utility on a benchmark enriched for queries where adaptation helps, cuts adaptation compute by about 30% without loss of utility under a moderate compute penalty, and amortizes skill construction through reuse

## The account

Test-time training methods (PoT, few-shot TTT, TTRL, SEAL, TLM) each help in some settings and hurt in others. Turning them into tools that produce reusable LoRA skills, and training a policy on utility gain over direct answering minus a compute penalty, gives on Qwen2.5-7B an overall utility of 0.510 against 0.256 for direct answers, with gains in all eight domains, a help-to-harm ratio near 20:1, and 100 reuses of earlier skills of which 61 help and 1 harms. Raising the compute penalty makes the policy answer directly more often and drop costly low-gain methods first.

## What it does not show

Gains on ordinary distributions, where queries that benefit from adaptation are rare (7.0% of MATH-500 by the paper's criterion); reliable abstention on other backbones; training on the policy's own streams; costs of storage, upkeep or a stale or poisoned skill.
