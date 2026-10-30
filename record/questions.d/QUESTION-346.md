---
number: 346
status: Open
formerly:
- QUESTION-tmprxak2
title: 'On confounded causal systems larger than toy models, with a known causal partition, does gradient search for the causal information bottleneck through an adjustment set find the partition by p(y | do(x)) reliably, and how often does it fail?'
version: 1
tags:
- causality
- information-theory
date: '2026-10-30'
line: formal-apparatus
summary: >-
  The promotion condition formerly on [THEORY-1146](../theory.d/THEORY-1146.md), moved here when the
  twenty-second status review narrowed that reading to what three toy
  models showed and promoted it ([ADR-065](../decisions.d/ADR-065.md)). That the causal partition is the
  optimum is [THEORY-1125](../theory.d/THEORY-1125.md); whether search finds it at scale is this
  question.
---

# QUESTION-346: On confounded causal systems larger than toy models, with a known causal partition, does gradient search for the causal information bottleneck through an adjustment set find the partition by p(y | do(x)) reliably, and how often does it fail?

## Why it is a question

Simoes, Dastani and van Ommen (2025), [LIT-1802](../literature.d/LIT-1802.md), show that at full causal
control the causal information bottleneck is optimised by the partition of
X by p(y | do(x)) ([THEORY-1125](../theory.d/THEORY-1125.md)), and that projected gradient search found
it in 95 to 100 percent of runs on three toy models whose X has at most 16
values ([THEORY-1146](../theory.d/THEORY-1146.md)). The search needed ensembles of 4 to 12 optimisers and
a penalty against unused values of T, and the authors expect local minima
to need "modifications" at scale. They do not claim that it scales.

## What would answer it

Results on causal systems larger than toy SCMs, with confounding and a
known causal partition, in which the information bottleneck at full
sufficiency recovers the observational partition by p(y | x) and the
causal bottleneck, computed through an adjustment set, recovers the
partition by p(y | do(x)), reliably and with the optimiser's failure rate
reported; or a case where the observational and causal partitions differ
and the causal bottleneck does not find the latter.
