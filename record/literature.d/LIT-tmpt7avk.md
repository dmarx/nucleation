---
status: Active
title: 'Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed and read on 2026-11-12. The owner named "the PASS@(k,T) work"
    at U21 of the exchange "Medical Ethics and Media Enshitification"
    (2026-11-11), without a link; A identified it at A44 §1 as arXiv
    2604.14877. Checked on the arXiv API on 2026-11-12: Zhiyuan Zhai,
    Wenjing Yan, Xiaodan Shao and Xin Wang, v1 submitted 2026-04-16, the
    only version. The record held no LIT with this arXiv id or title and
    no entry mentioning PASS@(k,T) or pass@k. Read from the arXiv PDF.
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2026-04-16'
arxiv: '2604.14877'
first_author: 'Zhai'
keywords:
- reinforcement learning
- LLM agents
- tool use
- pass@k
- capability boundary
implementations:
- https://github.com/zhiyuanZhai20/pass-kt-analysis
summary: >-
  Zhai, Yan, Shao and Wang (2026), ARXIV-2604.14877. PASS@(k,T), the
  chance that one of k sampled trajectories with at most T interaction
  rounds succeeds, separates capability expansion (problems newly solvable
  at some sampling budget) from efficiency improvement (problems already
  solvable, solved more reliably). On sequential retrieval, RL expands a
  7B agent's boundary while matched-data SFT contracts it. Here because the
  owner named it at U21 beside the record's work on resource-bounded
  realization and tolerance regions (CLAIM-tmpyc5md). Read in NOTE-tmpa5wyr;
  its account is THEORY-tmps74c5.
---
<!-- inactive-ok-file: CLAIM-tmpyc5md THEORY-tmps74c5 — filed from the same exchange, Proposed -->

# LIT-tmpt7avk: Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis

Zhiyuan Zhai, Wenjing Yan, Xiaodan Shao and Xin Wang (2026). "Does RL Expand
the Capability Boundary of LLM Agents? A PASS@(k, T) Analysis." arXiv
preprint. ARXIV-2604.14877.

## Key takeaways

- A two-axis metric: sampling breadth k and interaction depth T. Its
  large-k limit indicates whether a problem is solvable at all at depth T;
  its k = 1 value is reliability.
- Capability expansion (the solvable set grows) and efficiency improvement
  (higher single-shot success inside the shared solvable set) are defined
  apart and can move in opposite directions: on bridge questions RL is
  slightly worse at k = 1 and better at k = 64.
- The expansion is specific to compositional, sequential retrieval and
  comes from reweighting strategies the base model already samples.

## Standing in the record

Filed for its distinctions, not its training advice. Its recommendation to
prefer RL over expert-trajectory SFT on compositional tool use is ML
practice and belongs to the anthology (ADR-048); hence the flag.
