---
number: 272
status: Answered
formerly:
- QUESTION-tmp1wykc
title: 'When the task''s target and the probes'' outcome laws are both linear in one unknown state, as for the pairwise comparisons of actions under partial monitoring and for the authority shares of a mixture of known response profiles, when does a family of probes separate what the task needs told apart?'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Split off from QUESTION-031 under ADR-049 at the owner's direction,
    from the readings of 2026-10-25. Answered by THEORY-962 for the
    pairwise comparisons of actions, and by CLAIM-452 for the
    authority shares of a mixture.
- version: 2
  date: '2026-10-25'
  note: >-
    From the reading of Lattimore and Szepesvári (LIT-1524, NOTE-
    tmpkgxba). The pairwise-comparisons answer names THEORY-963, the
    classification for every finite game, beside THEORY-964, and adds
    that the probe set for a neighbouring pair is its whole neighbourhood,
    degenerate actions included, with the separating direction in the kernel
    of all their signal matrices (THEORY-961). The answer and status
    are unchanged.
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
  combined signal row space ([THEORY-962](../theory.d/THEORY-962.md)). For the authority shares of
  a mixture of known profiles, it is the profiles over the probe contexts
  being affinely independent ([CLAIM-452](../claims.d/CLAIM-452.md)). The general stochastic,
  decision-relative case, where the target or the outcome laws are not
  linear in a common state, stays with [QUESTION-031](QUESTION-031.md).
answered_by:
- THEORY-962
- CLAIM-452
---
<!-- inactive-ok-file: THEORY-964 — Superseded by THEORY-963; the four-class classification as Bartók et al. state it, cited for context beside THEORY-963 (Active), nothing here rests on it -->

# QUESTION-272: When the task's target and the probes' outcome laws are both linear in one unknown state, as for the pairwise comparisons of actions under partial monitoring and for the authority shares of a mixture of known response profiles, when does a family of probes separate what the task needs told apart?

## Answer

Exactly when the task's target lies in the span of what the probes
reveal. Two cases are settled.

- **Pairwise comparisons of actions** ([THEORY-962](../theory.d/THEORY-962.md), Active, from
  Bartók, Foster, Pál, Rakhlin and Szepesvári 2014, read in [NOTE-1164](../notes.d/NOTE-1164.md)).
  Two outcome laws that agree on every probe's signal in a set D agree on
  the comparison of actions i and j iff ℓᵢ − ℓⱼ lies in Σ_{k∈D} Im S_kᵀ,
  the combined row space of the signal matrices. It is checkable before
  any data, and it is the condition that sorts partial-monitoring games
  into classes ([THEORY-964](../theory.d/THEORY-964.md), Superseded; for every finite game
  [THEORY-963](../theory.d/THEORY-963.md), Active). For the classification, the probe set that
  matters for a neighbouring pair i, j is N⁺_{i,j}, which includes
  actions optimal only on the boundary between them; their signals count,
  and the separating direction must lie in the kernel of all of them
  ([THEORY-961](../theory.d/THEORY-961.md), from [LIT-1524](../literature.d/LIT-1524.md)).
- **Authority shares of a mixture** ([CLAIM-452](../claims.d/CLAIM-452.md), Active, demonstrated).
  For a response that is the authority-weighted mixture of known
  profiles, the shares are identified by a set of contexts iff the
  profiles over those contexts are affinely independent, equivalently iff
  the design's Fisher information is positive definite on the simplex's
  tangent space ([CASE-159](../cases.d/CASE-159.md)).

## What it does not settle

The general case of [QUESTION-031](QUESTION-031.md): a target or outcome laws that are not
linear in one state, profiles that must themselves be estimated, and
probes whose availability depends on the organization's own choices. Nor
does it say how well a probe family separates; that is the design
criterion's question ([THEORY-956](../theory.d/THEORY-956.md), [THEORY-954](../theory.d/THEORY-954.md)).
