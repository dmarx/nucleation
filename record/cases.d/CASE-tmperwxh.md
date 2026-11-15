---
status: Proposed
title: 'An executed run of the pinned kink: under Allen–Cahn relaxation on a bounded line, the demand that a kink''s centre lie in [−0.5, 0.5] is met by a static solution with or without a pinning bump, but a kink displaced to +2 stays at +2 without the bump and returns to the centre with it, with its boundary charge 1 throughout, so the demand is feasible in both cases and attracting in one'
version: 1
standing: stipulated
kind: executed-study
tags:
- mathematics
- complex-systems
date: '2026-11-15'
line:
- formal-apparatus
bears_on:
- QUESTION-438
illustrates:
- CLAIM-618
summary: >-
  The assistant's run of the pinned kink that A proposed in the exchange
  "Explain String Theory" (A5 §7) and that this filing noted on
  [QUESTION-438](../questions.d/QUESTION-438.md). It was executed when the owner asked for the assistant's
  ideas to be filed (scratch/formal/pinned_kink_run.py, about twenty
  seconds). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpovvk2 — Proposed or new; the claims the run illustrates in a field -->

# CASE-tmperwxh: An executed run of the pinned kink

## The run

The field obeys ∂ₜφ = κφ'' − λφ(φ² − v²) − 2a·g(x)·φ on [−20, 20], with
φ(±20) = ±v, κ = 1, λ = 2, v = 1 and 801 grid points. g is a unit Gaussian
bump at 0. For a > 0 this is gradient flow of the φ⁴ energy plus
a∫g(φ² − v²), which is lowest when the kink's core sits on the bump. Each
run starts from the exact kink at centre x₀ and relaxes to t = 200.

| pinning a | start x₀ | final centre | charge Q |
|---|---|---|---|
| 0 | 0 | 0.000 | 1 |
| 0 | +2 | +2.000 | 1 |
| 0.3 | 0 | 0.000 | 1 |
| 0.3 | +2 | 0.000 | 1 |

## What it shows

The demand "the centre lies in [−0.5, 0.5]" is in the compatibility
complex either way, because the centred kink is static with or without the
bump. It is in the attracting subcomplex only with the bump. Raising a
from 0 changes 𝒯 and leaves 𝒦 alone, which is one of [QUESTION-438](../questions.d/QUESTION-438.md)'s ways
of coming apart, in a field. The charge is the same in every run, as
[CLAIM-tmpovvk2](../claims.d/CLAIM-tmpovvk2.md) says: it fixes the sector, not where the kink is.

## Its limits

A deterministic, one-dimensional run with one pinning strength and no
noise. Translation is only approximately neutral on a bounded domain, but
the unpinned kink did not move within the run.
