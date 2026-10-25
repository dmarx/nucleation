---
status: Answered
title: 'When the task''s target and the probes'' outcome laws are both linear in one unknown state, as for the pairwise comparisons of actions under partial monitoring and for the authority shares of a mixture of known response profiles, when does a family of probes separate what the task needs told apart?'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Split off from QUESTION-031 under ADR-049 at the owner's direction,
    from the readings of 2026-10-25. Answered by THEORY-tmpwtj3m for the
    pairwise comparisons of actions, and by CLAIM-tmpa8ttt for the
    authority shares of a mixture.
tags:
- mathematics
- mathematical-statistics
date: '2026-10-25'
line: pragmatic-transport
refines:
- QUESTION-031
summary: >-
  The part of [QUESTION-031](QUESTION-031.md) that the readings of 2026-10-25 settle, split
  off under [ADR-049](../decisions.d/ADR-049.md). Both answers are linear: a probe family separates
  what the task needs exactly when the task's target lies in the span of
  what the probes reveal. For pairwise comparisons of actions under
  partial monitoring, that is the loss difference lying in the probes'
  combined signal row space ([THEORY-tmpwtj3m](../theory.d/THEORY-tmpwtj3m.md)). For the authority shares of
  a mixture of known profiles, it is the profiles over the probe contexts
  being affinely independent ([CLAIM-tmpa8ttt](../claims.d/CLAIM-tmpa8ttt.md)). The general stochastic,
  decision-relative case, where the target or the outcome laws are not
  linear in a common state, stays with [QUESTION-031](QUESTION-031.md).
answered_by:
- THEORY-tmpwtj3m
- CLAIM-tmpa8ttt
---
<!-- inactive-ok-file: THEORY-tmpz3a05 — Proposed; the four-class classification, cited for context, nothing here rests on it -->

# QUESTION-tmp1wykc: When the task's target and the probes' outcome laws are both linear in one unknown state, as for the pairwise comparisons of actions under partial monitoring and for the authority shares of a mixture of known response profiles, when does a family of probes separate what the task needs told apart?

## Answer

Exactly when the task's target lies in the span of what the probes
reveal. Two cases are settled.

- **Pairwise comparisons of actions** ([THEORY-tmpwtj3m](../theory.d/THEORY-tmpwtj3m.md), Active, from
  Bartók, Foster, Pál, Rakhlin and Szepesvári 2014, read in [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)).
  Two outcome laws that agree on every probe's signal in a set D agree on
  the comparison of actions i and j iff ℓᵢ − ℓⱼ lies in Σ_{k∈D} Im S_kᵀ,
  the combined row space of the signal matrices. It is checkable before
  any data, and it is the condition that sorts partial-monitoring games
  into classes ([THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md), Proposed).
- **Authority shares of a mixture** ([CLAIM-tmpa8ttt](../claims.d/CLAIM-tmpa8ttt.md), Active, demonstrated).
  For a response that is the authority-weighted mixture of known
  profiles, the shares are identified by a set of contexts iff the
  profiles over those contexts are affinely independent, equivalently iff
  the design's Fisher information is positive definite on the simplex's
  tangent space ([CASE-tmplg5jg](../cases.d/CASE-tmplg5jg.md)).

## What it does not settle

The general case of [QUESTION-031](QUESTION-031.md): a target or outcome laws that are not
linear in one state, profiles that must themselves be estimated, and
probes whose availability depends on the organization's own choices. Nor
does it say how well a probe family separates; that is the design
criterion's question ([THEORY-tmpig9py](../theory.d/THEORY-tmpig9py.md), [THEORY-tmpg6jfa](../theory.d/THEORY-tmpg6jfa.md)).
