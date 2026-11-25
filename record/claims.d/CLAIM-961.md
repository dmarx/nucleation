---
number: 961
status: Proposed
formerly:
- CLAIM-tmpw4lvx
title: 'The determinacy cover is not a sheaf cover'
statement: >-
  Reading the full set of askable questions as the fixed scenario, the
  operational cover is a thresholded determinacy functional of the empirical
  model, not a cover: a change in which questions a population answers
  determinately is a change of model on a fixed cover, so the operational
  notion earns its own name (the determinacy cover) and the sheaf cover is
  kept apart
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A construction, on a fixed measurement scenario (X, M, O), of a canonical
  parameter-free map from empirical models to covers under which
  determinate-answerability is an invariant of the cover M itself rather than
  of the response distributions e, so that changing which questions are
  answered determinately changes M without changing e.
tags:
- contextuality
- mathematics
- translation
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- CASE-368
uses:
- TERM-155
corroborates:
- CLAIM-251
complements:
- CLAIM-962
bears_on:
- QUESTION-005
---
<!-- inactive-ok-file: CLAIM-251 CLAIM-201 — Proposed; the counter this reading corroborates, the thesis whose "cover" it would rename, and the measure that uses the operational sense -->
<!-- inactive-ok-file: CLAIM-962 TERM-155 CASE-368 — new in this contribution; the alternative reading, the term this claim uses, and the construction it rests on -->

# CLAIM-961: The determinacy cover is not a sheaf cover

## The claim

This is one of two readings [CASE-368](../cases.d/CASE-368.md) supports; it is the owner's
choice between them. It takes the modelling decision that the fixed scenario
(X, M, O) is the full set of questions a population could be asked, with M the
sheaf-theoretic cover ([TERM-042](../terms.d/TERM-042.md), [THEORY-012](../theory.d/THEORY-012.md)).

On that reading, which questions the population answers determinately is the
determinacy functional D_θ(e) = {x : max_o m_x(o) ≥ θ} of the empirical model
e ([TERM-155](../terms.d/TERM-155.md)). [CASE-368](../cases.d/CASE-368.md) shows (fact 3) that two models on the
same M give different determinacy covers: the operational cover is a function
of the responses, and M does not move. So a change in determinate-answerability
is a change of empirical model on a fixed cover, not a change of cover. This is
exactly [CLAIM-251](CLAIM-251.md)'s position, and this claim corroborates it with the
explicit construction: the operational notion is not by itself a cover in the
sheaf sense, and it earns its own name ([TERM-155](../terms.d/TERM-155.md)) so that
[CLAIM-201](CLAIM-201.md), [CLAIM-257](CLAIM-257.md), [CLAIM-256](CLAIM-256.md) and [CLAIM-125](CLAIM-125.md) can say which sense of
"cover" they mean.

The construction does supply the induced sub-site of determinable measurements
([CASE-368](../cases.d/CASE-368.md), fact 2), so a sheaf-theoretic object exists; but on this
reading it is a derived readout of e, not the thing that changes when
determinacy changes. The map e ↦ D_θ(e) is thresholded and non-injective
(fact 4), so it is no canonical functor, which is why [CLAIM-251](CLAIM-251.md)'s "until a
functorial link is shown" is not met and the separate name stands.

## What it does not say

- It does not say the operational notion is empty or useless; it is the base
  the observational distortion D_obs sums over ([CLAIM-257](CLAIM-257.md), [TERM-043](../terms.d/TERM-043.md)).
- It does not deny that an induced sub-cover with restriction maps can be
  built; [CASE-368](../cases.d/CASE-368.md) builds one. It denies that building it makes
  determinate-answerability a cover-level property on the fixed full scenario.
- It does not decide the rename. Whether to retire "cover" for the operational
  entries in favour of [TERM-155](../terms.d/TERM-155.md), or to keep "cover" under the rival
  reading [CLAIM-962](CLAIM-962.md), is the owner's call.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
