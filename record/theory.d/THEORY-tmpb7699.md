---
status: Proposed
title: 'Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model''s empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets'
version: 1
source:
- LIT-tmpj8nbo
corroborates:
- CLAIM-tmpff0cq
- CLAIM-tmpyc5md
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
  (Zhu, Jin, Tu, Men, Hao, Li, Liu, Zhao 2026), read in [NOTE-tmpjmhp7](../notes.d/NOTE-tmpjmhp7.md)
  (Read). The paper asks what multi-turn agentic RL (GRPO mainly, also PPO
  and GiGPO, on Qwen3-4B/8B) improves over its base model, on four
  interactive benchmarks (DeepCoder-MT, BFCL v3, InterCode-SQL, FrozenLake),
  using the two-dimensional metric Pass@(K, T) of Zhai et al. (2026; arXiv
  2604.14877, held as [LIT-tmpt7avk](../literature.d/LIT-tmpt7avk.md)). Across sampling breadth K, the RL model
  beats the base model at every k, so in multi-turn settings RL pushes
  success beyond the base model's empirical Pass@K boundary (unlike
  single-turn results).
---

# THEORY-tmpb7699: Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model's empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets

## The account

Zhu and colleagues find, evaluating multi-turn agentic RL by Pass@(K, T) on four interactive benchmarks, that RL lifts success above the base model's empirical Pass@K boundary only when the interaction budget is ample, the advantage shrinking or reversing under tight budgets; at matched states the RL policy does not choose better single steps but recovers better from errors and composes locally plausible steps into successful long trajectories far more reliably; and training with randomized, announced budgets (BudgetMix) recovers performance at tight budgets.

## Evidence

The reading in [NOTE-tmpjmhp7](../notes.d/NOTE-tmpjmhp7.md); its key results are quoted there with locations.
