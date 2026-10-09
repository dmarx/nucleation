---
status: Active
title: 'E3: the controlled inference harness, dry run only (C5)'
version: 1
standing: stipulated
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
variant_of:
- CASE-tmpe61ww
summary: >-
  Built at U25: four frame conditions (stable complicit, neutral,
  moralizing; shifting), 12 reset chains each, 5 generations, 240 calls,
  gpt-4.1-mini at temperature 0.7, seed 1729. Only a dry run was
  executed: "No model-generated observations were recorded." The design
  is the manuscript's Case II.
supports:
- CLAIM-tmp8w5c7
---

# CASE-tmpkuw2b: E3: the controlled inference harness, dry run only (C5)

## The case

U25: "use tooling calling with controlled prompts and contexts for the callable
model inference experiment." A66: the tool catalog has "no installed
text-generation action that accepts independent prompts". C5's README: "four
preregistered delivery-frame conditions (complicit, neutral, moralizing,
shifting), 12 independently reset chains per condition, and five sequential
generations per chain: 240 text-generation calls total. Each call includes only
the same fixed system instruction, current frame text, and preceding
generation's passage. No chain receives the original seed after generation 1."
Defaults: gpt-4.1-mini, temperature 0.7, seed 1729. Its own limit: "The framing
conditions are intentionally not matched for semantic content. A later factorial
experiment should disentangle frame content, order, and role-instruction
hierarchy."

Result, A67: "The dry run completed successfully and generated the randomized
protocol for all 240 calls. No model-generated observations were recorded."

## What it can show

Nothing yet. Its design is the manuscript's §10 Case II: "Run independent, reset
interpretation chains using stable complicit, stable admonitory, alternating,
and randomly assigned frames. Only the immediately previous expression is
supplied at each step". The manuscript adds random frames and
heterogeneous-agent chains and drops the neutral condition. It would answer
[QUESTION-tmphs0xr](../questions.d/QUESTION-tmphs0xr.md).
