---
status: Proposed
title: 'A system persists as the same self over an interval when a coherence measure is approximately conserved along its own trajectory, not merely matched by some map between its states'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Dual-filed from MOM-CLM-153 under ADR-037. Proposed here, though
    Active in MOM: the repair is sound as logic (it turns a condition
    everything satisfies into one that can fail), but the coherence
    measure γ is left unspecified in MOM's source, and nothing has been
    measured. There was nothing to re-run.
role: thesis
defeated_if: >-
  A system whose coherence measure is conserved under its own dynamics
  over an interval and which, by every other mark, is not the same self
  over it. Or a choice of γ under which every trajectory conserves it,
  which would make the condition empty again.
tags:
- personhood
- self
- complex-systems
date: '2026-10-11'
line: distributed-agency
summary: >-
  Dual-filed from [MOM-CLM-153](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-153.md) ([ADR-037](../decisions.d/ADR-037.md)). The corpus's selfhood condition,
  that some map φ preserves a coherence score γ, is satisfied by any two
  systems with similar scores. Requiring the map to be the system's own
  evolution Φ_Δt makes selfhood approximate conservation of γ along the
  trajectory: γ is an approximate first integral, and the defect is a
  number. Proposed here because γ is unspecified.
---
<!-- inactive-ok-file: ADR-037 — Proposed; the decision this entry is filed under -->

# CLAIM-tmpdqsrb: A system persists as the same self over an interval when a coherence measure is approximately conserved along its own trajectory, not merely matched by some map between its states

## The claim

From [MOM-CLM-153](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-153.md). The condition "there exists φ with γ(S) ≈ γ(φ(S))" holds
of my system at noon and yours at midnight, so it is no condition. Replace
"some φ" with the system's own evolution: γ(Φ_Δt(S(t))) ≈ γ(S(t)) for Δt in
the interval of interest. The self is then the region of state space on
which γ stays level. The defect, sup over Δt of |γ(Φ_Δt(s)) − γ(s)|, is
measurable.

## Why this record files it, and why Proposed

It gives the person across time (the reluctant writer's afternoons,
[CASE-013](../cases.d/CASE-013.md); the child and adult reader, [CASE-tmpifi9m](../cases.d/CASE-tmpifi9m.md)) a test that can fail.
That is what this record's diachronic material lacked. It also matches the
corporate case's drift and cadence ([CASE-tmpk52n6](../cases.d/CASE-tmpk52n6.md)): a firm whose coherence
decays between events conserves γ only over short windows. That bearing is
this record's.

It stays Proposed because everything rests on γ, and MOM's source defines γ
elsewhere as a representational alignment score, not as a dynamical
quantity. Until γ is fixed, the claim says what form a persistence criterion
must take, not which one is right.

## What it does not say

- **That a conserved γ is sufficient for being a self.** It is a persistence
  condition, in the sense [ADR-024](../decisions.d/ADR-024.md) keeps apart from being a subject.
- **Which γ.** Different choices give different selves. [CLAIM-tmp3qyzh](CLAIM-tmp3qyzh.md)'s
  target-relativity applies.
