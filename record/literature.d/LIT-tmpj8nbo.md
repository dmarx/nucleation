---
status: Active
title: 'What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12, in NOTE-tmpjmhp7; account THEORY-tmpb7699. Status
    Active.
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Medical Ethics and Media Enshitification" (2026-11-11). Checked on the arXiv API on 2026-11-12. The record held no LIT with this identifier, title or first author. The arXiv API gives v1 submitted 2026-11-04. The summary is how A describes the work; a reading should check it first.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2026-11-04'
arxiv: '2611.06483'
first_author: 'Zhu'
keywords: []
implementations: []
summary: >-
  Zhu et al. (2026), [ARXIV-2611.06483](https://arxiv.org/abs/2611.06483).
  Read on 2026-11-12 in NOTE-tmpjmhp7: The paper asks what multi-turn
  agentic RL (GRPO mainly, also PPO and GiGPO, on Qwen3-4B/8B) improves over
  its base model, on four interactive benchmarks (DeepCoder-MT, BFCL v3,
  InterCode-SQL, FrozenLake), using the two-dimensional metric Pass@(K, T)
  of Zhai et al. (2026; arXiv 2604.14877, held as LIT-tmpt7avk). Across
  sampling breadth K, the RL model beats the base model at every k, so in
  multi-turn settings RL pushes success beyond the base model's empirical
  Pass@K boundary (unlike single-turn results). Its account is
  THEORY-tmpb7699. Registered from the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11), where A cited it at A44 §1.
---
<!-- inactive-ok-file: THEORY-tmpb7699 — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: CLAIM-tmpyc5md — Proposed; filed from the same exchange -->

# LIT-tmpj8nbo: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

Kejian Zhu, Zhuoran Jin, Shangqing Tu, Tianyi Men, Yupu Hao, Jiachun Li and others (2026). "What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?" *arXiv preprint*. [ARXIV-2611.06483](https://arxiv.org/abs/2611.06483).

## Key takeaways

Read on 2026-11-12 ([NOTE-tmpjmhp7](../notes.d/NOTE-tmpjmhp7.md)). An evaluation showing that
trajectory-level gains from multi-turn agentic RL are budget-conditional and
come from error recovery and long-horizon composition rather than better
per-step decisions, with a simple budget-randomized training remedy.

## Standing in the record

Registered on 2026-11-12 from the exchange "Medical Ethics and Media Enshitification" (2026-11-11), where A cited it at A44 §1. It bears on [CLAIM-tmpyc5md](../claims.d/CLAIM-tmpyc5md.md).

Read on 2026-11-12; the reading is [NOTE-tmpjmhp7](../notes.d/NOTE-tmpjmhp7.md) and its account
[THEORY-tmpb7699](../theory.d/THEORY-tmpb7699.md).
