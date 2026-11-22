---
status: Proposed
title: 'Reading the full set of askable questions as the fixed scenario, the operational cover is a thresholded determinacy functional of the empirical model, not a cover: a change in which questions a population answers determinately is a change of model on a fixed cover, so the operational notion earns its own name (the determinacy cover) and the sheaf cover is kept apart'
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
- CASE-tmpqg5fa
uses:
- TERM-tmpqfgw9
corroborates:
- CLAIM-251
complements:
- CLAIM-tmpyj388
bears_on:
- QUESTION-005
---
<!-- inactive-ok-file: CLAIM-251 CLAIM-201 CLAIM-257 — Proposed; the counter this reading corroborates, the thesis whose "cover" it would rename, and the measure that uses the operational sense -->
<!-- inactive-ok-file: CLAIM-tmpyj388 TERM-tmpqfgw9 CASE-tmpqg5fa — new in this contribution; the alternative reading, the term this claim uses, and the construction it rests on -->

# CLAIM-tmpw4lvx: Reading the full set of askable questions as the fixed scenario, the operational cover is a thresholded determinacy functional of the empirical model, not a cover: a change in which questions a population answers determinately is a change of model on a fixed cover, so the operational notion earns its own name (the determinacy cover) and the sheaf cover is kept apart

## The claim

This is one of two readings [CASE-tmpqg5fa](../cases.d/CASE-tmpqg5fa.md) supports; it is the owner's
choice between them. It takes the modelling decision that the fixed scenario
(X, M, O) is the full set of questions a population could be asked, with M the
sheaf-theoretic cover ([TERM-042](../terms.d/TERM-042.md), [THEORY-012](../theory.d/THEORY-012.md)).

On that reading, which questions the population answers determinately is the
determinacy functional D_θ(e) = {x : max_o m_x(o) ≥ θ} of the empirical model
e ([TERM-tmpqfgw9](../terms.d/TERM-tmpqfgw9.md)). [CASE-tmpqg5fa](../cases.d/CASE-tmpqg5fa.md) shows (fact 3) that two models on the
same M give different determinacy covers: the operational cover is a function
of the responses, and M does not move. So a change in determinate-answerability
is a change of empirical model on a fixed cover, not a change of cover. This is
exactly [CLAIM-251](CLAIM-251.md)'s position, and this claim corroborates it with the
explicit construction: the operational notion is not by itself a cover in the
sheaf sense, and it earns its own name ([TERM-tmpqfgw9](../terms.d/TERM-tmpqfgw9.md)) so that
[CLAIM-201](CLAIM-201.md), [CLAIM-257](CLAIM-257.md), CLAIM-256 and CLAIM-125 can say which sense of
"cover" they mean.

The construction does supply the induced sub-site of determinable measurements
([CASE-tmpqg5fa](../cases.d/CASE-tmpqg5fa.md), fact 2), so a sheaf-theoretic object exists; but on this
reading it is a derived readout of e, not the thing that changes when
determinacy changes. The map e ↦ D_θ(e) is thresholded and non-injective
(fact 4), so it is no canonical functor, which is why [CLAIM-251](CLAIM-251.md)'s "until a
functorial link is shown" is not met and the separate name stands.

## What it does not say

- It does not say the operational notion is empty or useless; it is the base
  the observational distortion D_obs sums over ([CLAIM-257](CLAIM-257.md), [TERM-043](../terms.d/TERM-043.md)).
- It does not deny that an induced sub-cover with restriction maps can be
  built; [CASE-tmpqg5fa](../cases.d/CASE-tmpqg5fa.md) builds one. It denies that building it makes
  determinate-answerability a cover-level property on the fixed full scenario.
- It does not decide the rename. Whether to retire "cover" for the operational
  entries in favour of [TERM-tmpqfgw9](../terms.d/TERM-tmpqfgw9.md), or to keep "cover" under the rival
  reading [CLAIM-tmpyj388](CLAIM-tmpyj388.md), is the owner's call.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
