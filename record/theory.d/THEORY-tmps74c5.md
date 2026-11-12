---
status: Proposed
title: 'Scoring an agent by whether one of k sampled trajectories of at most T interaction rounds succeeds separates capability expansion, a larger set of problems solved at some sampling budget, from efficiency improvement, more reliable success on problems already solvable; on sequential retrieval, RL expanded a 7B agent''s boundary while matched-data SFT contracted it'
version: 1
source:
- LIT-tmpt7avk
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
  Zhai, Yan, Shao and Wang's PASS@(k,T) (LIT-tmpt7avk, read in
  NOTE-tmpa5wyr). The distinction is definitional and holds whatever the
  experiment shows; the experiment is one model, one tool and differences
  of a few problems. Its stated monotonicity in T holds of a policy that
  ignores unused budget, and its own per-depth estimates are not
  monotone. Proposed on the experimental half.
---

# THEORY-tmps74c5: Scoring an agent by whether one of k sampled trajectories of at most T interaction rounds succeeds separates capability expansion, a larger set of problems solved at some sampling budget, from efficiency improvement, more reliable success on problems already solvable; on sequential retrieval, RL expanded a 7B agent's boundary while matched-data SFT contracted it

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
retrieval over HotPotQA (NOTE-tmpa5wyr).

## What it does not say

That RL expands capability in general, or that an unsolved problem in 64
attempts is unsolvable. It does not consider evaluators that can be wrong:
success is exact match against a gold answer.
