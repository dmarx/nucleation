---
number: 1672
status: Proposed
formerly:
- THEORY-tmpb7699
title: 'Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model''s empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets'
version: 1
source:
- LIT-2414
corroborates:
- CLAIM-654
- CLAIM-663
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-12'
promote_when: >-
  The budget dependence of the RL advantage and the absence of a
  matched-state step-quality gain are reproduced on other model families or
  benchmarks, or by a second group.
summary: >-
  What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?
  (Zhu, Jin, Tu, Men, Hao, Li, Liu, Zhao 2026), read in [NOTE-1769](../notes.d/NOTE-1769.md)
  (Read). The paper asks what multi-turn agentic RL (GRPO mainly, also PPO
  and GiGPO, on Qwen3-4B/8B) improves over its base model, on four
  interactive benchmarks (DeepCoder-MT, BFCL v3, InterCode-SQL, FrozenLake),
  using the two-dimensional metric Pass@(K, T) of Zhai et al. (2026; arXiv
  2604.14877, held as [LIT-2441](../literature.d/LIT-2441.md)). Across sampling breadth K, the RL model
  beats the base model at every k, so in multi-turn settings RL pushes
  success beyond the base model's empirical Pass@K boundary (unlike
  single-turn results).
---

# THEORY-1672: Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model's empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets

## The account

Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model's empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets.

## Evidence

The reading in [NOTE-1769](../notes.d/NOTE-1769.md); its key results are quoted there with locations.

## Note of 2026-11-15: the single-turn results, read

<!-- inactive-ok-file: THEORY-tmp9rnyv THEORY-tmpxu3kz — Proposed; the single-turn readings of 2026-11-15, cited as the result this account contrasts with -->

The single-turn result this account contrasts with is Yue et al. ([THEORY-tmp9rnyv](THEORY-tmp9rnyv.md)): RLVR models overtaken by their base models at large k. It is not uniform: ProRL ([THEORY-tmpxu3kz](THEORY-tmpxu3kz.md)) reports single-turn expansion after long, diversity-preserving training from a distilled model, with gains largest where the start model was weak and nil or negative on math. So the contrast is between multi-turn RL at ample budgets and short single-turn RLVR from pretrained bases, not between multi-turn and single-turn as such. No status change.
