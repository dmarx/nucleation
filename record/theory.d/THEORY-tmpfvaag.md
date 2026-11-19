---
status: Proposed
title: 'Blakeney and colleagues find that a 7B language model trained for one trillion tokens scores higher on knowledge, math and code benchmarks when the last fifth or so of training replaces large-scale web text with domain-specific and code data, at the same total tokens, with general benchmarks best at an intermediate duration and math and code still rising'
version: 1
source:
- LIT-tmps3oxd
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent run, or the released checkpoints with repeated late
  phases from several seeds or data orders, reproduces at a stated scale
  with total tokens fixed that a late phase upsampling domain and code
  data raises those benchmarks over continuing the base mix, and that
  general-benchmark scores peak at an intermediate late-phase duration.
summary: >-
  From the reading of [LIT-tmps3oxd](../literature.d/LIT-tmps3oxd.md) in [NOTE-tmpfwg5y](../notes.d/NOTE-tmpfwg5y.md). A late-phase result;
  it qualifies [THEORY-tmpd6smn](THEORY-tmpd6smn.md)'s reading of late code. Proposed until its
  promote_when is met.
---

# THEORY-tmpfvaag: Blakeney and colleagues find that a 7B language model trained for one trillion tokens scores higher on knowledge, math and code benchmarks when the last fifth or so of training replaces large-scale web text with domain-specific and code data, at the same total tokens, with general benchmarks best at an intermediate duration and math and code still rising

## The account

A 7B model on 1T tokens, with the last 0, 5, 10, 20 or 30 per cent re-weighted toward domain and code data: MMLU 35.69 rising to 43.19 at 10 per cent, GSM8K 14.71 rising to 24.56 at 30 per cent. Removing math subsets from a 10 per cent late phase leaves most benchmarks below no late phase.

## Evidence

One run per condition; no throughout arm; benchmarks at the endpoint only.
