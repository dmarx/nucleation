---
status: Answered
title: 'In the coupled meaning–influence model linearized at its symmetric state, when is the symmetric state unstable, and does scoring endorsement independently of the interpretation remove the instability?'
version: 1
tags:
- self-governance
- complex-systems
date: '2026-10-21'
line: distributed-agency
refines:
- QUESTION-100
summary: >-
  The linear part of [QUESTION-100](QUESTION-100.md), split off under [ADR-049](../decisions.d/ADR-049.md) and answered by
  [CLAIM-330](../claims.d/CLAIM-330.md). With each field stable alone and nonnegative couplings, the
  symmetric state is unstable exactly when βγ > (1 − α)(1 − δ). Only the
  loop can destabilize it, and independent scoring (γ ≈ 0) removes the
  instability. The nonlinear regime, and whether capture costs fidelity,
  stay with [QUESTION-100](QUESTION-100.md).
answered_by:
- CLAIM-330
---

# QUESTION-tmphi1l2: In the coupled meaning–influence model linearized at its symmetric state, when is the symmetric state unstable, and does scoring endorsement independently of the interpretation remove the instability?

## Answer

[CLAIM-330](../claims.d/CLAIM-330.md) (Active, demonstrated), from the construction in [CASE-099](../cases.d/CASE-099.md). For
J = [[α, β], [γ, δ]] with nonnegative entries and α, δ < 1:

- **When.** The leading eigenvalue exceeds 1 exactly when
  βγ > (1 − α)(1 − δ).
- **Only the loop.** If either coupling is zero the eigenvalues are α and
  δ, so capture that starts at symmetry needs both arrows: authority
  shaping interpretation, and interpretation shaping endorsement.
- **Independent scoring.** Scoring operators independently of the
  dominant interpretation (Regime B, γ ≈ 0) removes the coupling-driven
  instability, whatever the memory of endorsement.
- **What grows.** The leading eigenvector, (β, λ+ − α), is positive in
  both components: a joint lean of meaning and authority.

[CLAIM-340](../claims.d/CLAIM-340.md) adds that committing predictions before the evidence is not by
itself Regime B. That is [QUESTION-tmp7x8l1](QUESTION-tmp7x8l1.md).

## What it leaves to [QUESTION-100](QUESTION-100.md)

The answer holds for the linearization at symmetry. [CLAIM-330](../claims.d/CLAIM-330.md) does not
say that [CASE-092](../cases.d/CASE-092.md)'s full model has this linearization, since the sign and
size of γ in Regime A are assumptions about an unbuilt model. It says
nothing about the bounded nonlinear system's attractors or hysteresis,
about whether capture costs fidelity, or about role-indexed endorsement.
