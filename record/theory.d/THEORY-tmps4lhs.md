---
status: Proposed
promote_when: >-
  An independent measurement on another model and task with an automatic
  verifier showing coverage rising with the number of independent samples
  over at least two orders of magnitude, and on a task without one showing
  majority-vote or reward-model accuracy plateauing while coverage keeps
  rising.
title: 'Drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over orders of magnitude across models and tasks, so that with an automatic verifier repeated sampling converts inference compute into success, while without one majority voting and reward-model selection plateau far below coverage'
version: 1
tags:
- learning-theory
- anthology-candidate
date: '2026-11-20'
source:
- LIT-2622
extends:
- THEORY-1894
summary: >-
  Brown and colleagues' wider thesis, filed beside [THEORY-1894](THEORY-1894.md), which
  reports what they found, when the status review of 2026-11-20 promoted it
  ([ADR-065](../decisions.d/ADR-065.md): each promoted attribution gets its wider thesis filed beside it,
  Proposed). The authors read their fitted curves as an inference-time
  scaling law ([NOTE-1972](../notes.d/NOTE-1972.md)). [THEORY-1894](THEORY-1894.md)'s old promote_when moves here
  word for word: the thesis waits on a measurement by others on another
  model and task.
---
<!-- inactive-ok-file: THEORY-1880 — Proposed; Yue and colleagues' use of the same metric, cited as neither a replication nor a test -->

# THEORY-tmps4lhs: Drawing more independent samples from a language model raises coverage, the fraction of problems at least one sample solves, smoothly and often log-linearly over orders of magnitude across models and tasks, so that with an automatic verifier repeated sampling converts inference compute into success, while without one majority voting and reward-model selection plateau far below coverage

## Source

Brown et al. (2024), [LIT-2622](../literature.d/LIT-2622.md), read in [NOTE-1972](../notes.d/NOTE-1972.md). [THEORY-1894](THEORY-1894.md) holds what
the paper measured, Active on that reading.

## The thesis

The paper reports its curves across coding, formal-proof and math tasks and
several model families, and reads them as a law: log coverage fit by an
exponentiated power law in the number of samples (§3.1, Eq. 2), an
inference-time scaling law ([NOTE-1972](../notes.d/NOTE-1972.md), "Concepts"). This entry asserts that law and
the verifier gap as properties of repeated sampling from language models,
beyond the runs reported.

## Why it is Proposed

Its only evidence is the one paper whose runs [THEORY-1894](THEORY-1894.md) reports. The
paper itself notes curves that "do not follow this trend closely" (Fig. 5),
and its SWE-bench figure is one model in one agent framework ([NOTE-1972](../notes.d/NOTE-1972.md)).
Yue and colleagues ([THEORY-1880](THEORY-1880.md)) use the same coverage metric to compare
base and RL-trained models; that is a use of the metric, not an
independent test of the law.

## What this does not say

What [THEORY-1894](THEORY-1894.md) does not say carries over: that a problem unsolved at the
largest budget is unsolvable, that sampling helps where per-sample success
is zero, or that coverage is deployable success without a verifier.
