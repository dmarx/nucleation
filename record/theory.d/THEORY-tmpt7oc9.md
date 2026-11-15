---
status: Proposed
promote_when: >-
  A replication on other model families or another lab's protocol, with
  confidence intervals, of two results. (a) Under residual steering, with
  current-token injection held fixed, a cache recomputed without steering
  raises coherence and lowers repetition against the steered cache, on
  most traits tested. (b) Steering from the system prompt's cropped
  attention contribution with per-token gating keeps turn-10 trait
  expression at or above residual steering's, with smaller coherence
  drift, against a layer- and norm-matched residual baseline. Gains under
  one judge, single-turn benchmarks, or the authors' own configuration on
  further traits do not settle it.
title: 'On Kang and colleagues, residual-stream persona steering loses coherence over multi-turn dialogue partly because steered token states written to the KV cache are reused by later tokens, and steering vectors taken from the system prompt''s contribution to self-attention, applied per token through a query–key gate, keep trait expression while largely avoiding that loss'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpi20ed
summary: >-
  Kang, Liu, Ma, Huang, Tan & Jiang (2026), LIT-tmpi20ed, read in
  NOTE-tmp80eb1. The cache account rests on a 2×2 isolation test on one
  model and 7 traits, with intervals. The method's advantage rests on
  point estimates from one judge and one seed on Qwen2.5-7B, with a Llama
  replication and judge checks on 4 traits. The sharp edges: injection
  itself, not the cache, is the larger cause of lost coherence; cleaning
  the cache does not reduce pooled drift; and the title's "duality" is not
  a result.
---

# THEORY-tmpt7oc9: On Kang and colleagues, residual-stream persona steering loses coherence over multi-turn dialogue partly because steered token states written to the KV cache are reused by later tokens, and steering vectors taken from the system prompt's contribution to self-attention, applied per token through a query–key gate, keep trait expression while largely avoiding that loss

## Source

Kang et al. (2026), LIT-tmpi20ed, read in NOTE-tmp80eb1 from arXiv v3.

## What was actually shown

- **The cache test.** In the 2×2 test, a clean cache under steering
  raised coherence by 15 points (interval 12.9 to 17.1) and nearly
  removed repetition loops. It also cut trait expression by 13 points.
- **The method.** On Qwen2.5-7B and Llama-3.1-8B, GCAD held trait
  expression with little coherence drift over 10 turns. Against matched
  residual baselines it was better on coherence or on trait, though not
  always on both.

The cache test could have come out otherwise: a clean cache might have
changed nothing.

## What this does not say

- **That the cache is the main cause.** Injection itself costs more
  coherence.
- **That prompts and activations are dual** in any stated sense.
- **That the method works for behaviours no prompt span can elicit.**
