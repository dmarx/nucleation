---
status: Open
title: 'Does the per-step nostalgia of a driven system without feedback fail to bound its dissipation when the drive is not Markov or the kernel does not keep each equilibrium stationary, and does any physical system show dissipation tracking nonpredictive information?'
version: 1
tags:
- thermodynamics
- information-theory
date: '2026-10-19'
line: 'formal-apparatus'
summary: >-
  The promotion condition formerly on [THEORY-026](../theory.d/THEORY-026.md), with the part met
  removed. [THEORY-026](../theory.d/THEORY-026.md) was promoted on 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md) v2) on a
  derivation that the per-step nostalgia I[s_t;x_t] − I[s_t;x_{t+1}] is
  nonnegative under a Markov drive and, summed, bounds dissipation from
  below when the kernel keeps each equilibrium stationary. What is left is
  whether the bound fails when either condition is dropped, and a
  physical system.
---

# QUESTION-tmpu8tif: Does the per-step nostalgia of a driven system without feedback fail to bound its dissipation when the drive is not Markov or the kernel does not keep each equilibrium stationary, and does any physical system show dissipation tracking nonpredictive information?

## Why it is a question

[THEORY-026](../theory.d/THEORY-026.md) holds, by a derivation in its dated note, that for a system
driven without feedback the average work dissipated at a switch of the
drive is kT times I[s_t;x_t] − I[s_t;x_{t+1}]. That nostalgia is
nonnegative when the drive is Markov, by data processing on
s_t – x_t – x_{t+1}. Summed over a protocol, it bounds the dissipation from
below when each relaxation kernel keeps its equilibrium stationary,
because relative entropy to that equilibrium then contracts.

The derivation uses each condition. It does not show that either is
needed. A non-Markov drive lets a state that remembers x_{t−1} predict
x_{t+1} better than it tracks x_t, which would make one step's nostalgia
negative. But the record has no kernel that keeps each equilibrium
stationary and still holds that memory, so the failure is not exhibited.
Until 2026-10-19 this, with a physical test, was [THEORY-026](../theory.d/THEORY-026.md)'s
promote_when.

## What would answer it

- A fixed-kernel, feedback-free system, with each kernel keeping its
  equilibrium stationary and a non-Markov drive, in which one step's
  nostalgia is negative or the summed nostalgia exceeds the dissipation.
  Or a proof that no such system exists.
- The same with a Markov drive and a kernel that does not keep its
  equilibrium stationary.
- A worked physical system in which measured dissipation tracks the
  nonpredictive information.

What would not answer it: results on systems with feedback. Those bear on
[THEORY-026](../theory.d/THEORY-026.md)'s scope, which is already limited, not on the bound.
