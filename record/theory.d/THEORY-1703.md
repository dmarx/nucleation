---
number: 1703
status: Proposed
formerly:
- THEORY-tmps74c5
title: 'Scoring an agent by whether one of k sampled trajectories of at most T interaction rounds succeeds separates capability expansion, a larger set of problems solved at some sampling budget, from efficiency improvement, more reliable success on problems already solvable; on sequential retrieval, RL expanded a 7B agent''s boundary while matched-data SFT contracted it'
version: 1
source:
- LIT-2441
bears_on:
- QUESTION-279
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-12'
promote_when: >-
  The bridge-question result, a net gain in the capability boundary under
  RL and a net loss under SFT on the same training data, holds in a
  replication with another base model or retrieval setting, or the
  released code reproduces Table 1.
summary: >-
  Zhai, Yan, Shao and Wang's PASS@(k,T) ([LIT-2441](../literature.d/LIT-2441.md), read in
  [NOTE-1749](../notes.d/NOTE-1749.md)). The distinction is definitional and holds whatever the
  experiment shows; the experiment is one model, one tool and differences
  of a few problems. Its stated monotonicity in T holds of a policy that
  ignores unused budget, and its own per-depth estimates are not
  monotone. Proposed on the experimental half.
---

# THEORY-1703: Scoring an agent by whether one of k sampled trajectories of at most T interaction rounds succeeds separates capability expansion, a larger set of problems solved at some sampling budget, from efficiency improvement, more reliable success on problems already solvable; on sequential retrieval, RL expanded a 7B agent's boundary while matched-data SFT contracted it

## The account

PASS@(k,T) is the probability that at least one of k independent
trajectories, each of at most T rounds of tool use, ends in a correct
answer. Its large-k limit says whether a problem is in the policy's
capability boundary at depth T; its k = 1 value says how reliably. Training
that raises reliability inside the shared boundary improves efficiency;
training that adds problems to the boundary expands capability. The two
can trade: on bridge questions the RL agent was slightly worse at one
attempt and better at 64. The expansion appeared only where the second
retrieval depends on the first, and came from reweighting strategies the
base model already produced, not from longer chains.

## Evidence

Table 1 and Figures 1–4 of the paper, on Qwen2.5-7B-Instruct with BM25
retrieval over HotPotQA ([NOTE-1749](../notes.d/NOTE-1749.md)).

## What it does not say

That RL expands capability in general, or that an unsolved problem in 64
attempts is unsolvable. It does not consider evaluators that can be wrong:
success is exact match against a gold answer.

## Note of 2026-11-12: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? (Zhu, Jin, Tu, Men, Hao, Li, Liu, Zhao 2026), read

From the reading in [NOTE-1769](../notes.d/NOTE-1769.md) ([LIT-2414](../literature.d/LIT-2414.md)), the reader's assessment as
checked by the filer: **extends**: an independent group confirms boundary
expansion along K for multi-turn RL and adds that the depth axis decides
whether the gain appears.

## Note of 2026-11-15: the single-turn readings, read

<!-- inactive-ok-file: THEORY-tmp9rnyv THEORY-tmpr8g5y THEORY-tmppt44k THEORY-tmpxu3kz — Proposed; the single-turn readings of 2026-11-15, cited as this account's predecessors, nothing here rests on them -->

Yue et al. ([THEORY-tmp9rnyv](THEORY-tmp9rnyv.md)) is the single-turn study whose question this account extends with an interaction-depth axis: there RLVR contracts the large-k boundary, here RL expands it on bridge questions. Both find the gain comes from reweighting strategies the base model already samples, which Meng et al. ([THEORY-tmpr8g5y](THEORY-tmpr8g5y.md)) measure at the token level and Balasubramanian and Kasiviswanathan ([THEORY-tmppt44k](THEORY-tmppt44k.md)) prove for a tilt of a fixed reference. ProRL ([THEORY-tmpxu3kz](THEORY-tmpxu3kz.md)) finds single-turn expansion after long training, largest where the start model was weak, which is consistent with expansion here appearing only where the second retrieval depends on the first. Whether Zhai et al. cite Yue et al. was not checked, so no `extends` is proposed between the LITs. No status change.
