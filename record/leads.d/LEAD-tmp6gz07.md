---
status: Open
title: 'Model the query-induced capability trap: a questioner whose sampling of queries is reinforced by observed passes and a target that maintains capacities in proportion to how often they are queried, against a questioner with independently generated stress tests, measuring whether the sampled family narrows and readiness for an unasked query decays'
version: 1
stage: specified
method:
- formal
tags:
- society-and-governance
- operations-research
date: '2026-11-23'
line:
- readiness
advances:
- CLAIM-tmp9o6yv
- QUESTION-395
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A50 §7 of the exchange "Explain First Contact RL"
  (2026-11-23), whose query-induced capability trap ([CLAIM-tmp9o6yv](../claims.d/CLAIM-tmp9o6yv.md))
  asserts that query and response strategies "co-adapt" without a model:
  A50's query update G is left unspecified. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp9o6yv TERM-tmpu5k0o — Proposed; the claim this would test and the lock-in it extends -->

# LEAD-tmp6gz07: Model the query-induced capability trap: a questioner whose sampling of queries is reinforced by observed passes and a target that maintains capacities in proportion to how often they are queried, against a questioner with independently generated stress tests, measuring whether the sampled family narrows and readiness for an unasked query decays

## The idea

A target holds capacities c_1, …, c_n, each learned by use and decaying
with disuse (the dynamics of [CLAIM-602](../claims.d/CLAIM-602.md)), under a budget that falls with
what was spent, as in [CLAIM-577](../claims.d/CLAIM-577.md). A questioner samples queries from ρ_t,
each query exercising some capacities. Three questioners:

- **Reinforced:** ρ_{t+1} shifts weight toward queries the target passed,
  A50's "Its success under repeated questioning reinforces the regulator's
  belief that its tests are adequate".
- **Fixed routine:** ρ fixed on the routine family Q₀ (the lock-in of
  [TERM-tmpu5k0o](../terms.d/TERM-tmpu5k0o.md) with no query-side adaptation).
- **Anchored:** the routine family plus a fixed share of independently
  generated stress tests, A50's safeguard.

Measures: the entropy and support of ρ_t; readiness ([TERM-115](../terms.d/TERM-115.md)) for an
unasked query q⋆ needing a capacity outside Q₀; the time at which q⋆
becomes unanswerable within its deadline; and the stress-test share that
keeps it answerable.

## What it would settle

Whether the trap's own content, the narrowing of the query family by the
target's success, occurs at all beyond the fixed-family lock-in; and how
large the independent share must be, which is [QUESTION-395](../questions.d/QUESTION-395.md)'s question of
what evidence can tell a warranted reserve from waste when ordinary
operation seldom exercises it.
