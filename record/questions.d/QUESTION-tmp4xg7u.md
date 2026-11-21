---
status: Open
title: "How common is signalling in language data, once it is estimated without the bias that makes plug-in signalling positive when the true marginals agree?"
version: 1
tags:
- linguistics
- probabilistic-modeling
- contextuality
date: '2026-11-21'
line:
- pragmatic-transport
summary: >-
  The empirical question behind the conclusion [ARG-037](../arguments.d/ARG-037.md) rejected a route
  to: [CLAIM-125](../claims.d/CLAIM-125.md)'s version 1 read "69 of the 90 systems signal" ([LIT-851](../literature.d/LIT-851.md))
  as showing that signalling is the typical case for language data. That
  route fails, because plug-in estimates from one or a few occurrences per
  context signal in expectation even when the true marginals agree
  ([CLAIM-235](../claims.d/CLAIM-235.md)). It does not show signalling is rare. Whether an extension
  of the line's quantities to signalling data is needed depends on the
  answer, which no entry holds. Filed on the owner's view, on 2026-11-21,
  that the conclusions the sweep under [ADR-tmp44npm](../decisions.d/ADR-tmp44npm.md) left without an entry
  "don't look useless". The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-037 — Rejected, Deferred or new; the history this question carries -->

# QUESTION-tmp4xg7u: How common is signalling in language data, once it is estimated without the bias that makes plug-in signalling positive when the true marginals agree?

## Why it matters

[CLAIM-125](../claims.d/CLAIM-125.md) (Active) holds two open problems for directed transport between empirical models, one of them how transport extends to signalling data. If signalling is typical in language data, that extension is not optional. If it is an artefact of small samples, it is a corner case. [CLAIM-125](../claims.d/CLAIM-125.md)'s version 2 kept only "common in these corpus data", as weak evidence.

## What would answer it

- **Repeated measures.** A corpus or judgement design that samples each context many times, so that the marginals can be compared with a test whose null is no signalling, with its error rate stated.
- **A bias-corrected estimator.** A signalling measure that is unbiased, or whose bias is known, under the sampling [CLAIM-235](../claims.d/CLAIM-235.md) describes, applied to the systems [LIT-851](../literature.d/LIT-851.md) counted.
- **What would not.** Any count from one or a few occurrences per context, by [CLAIM-235](../claims.d/CLAIM-235.md).

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
