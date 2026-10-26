---
number: 126
status: Active
formerly:
- CASE-tmp60jh6
title: 'Represented, authorized, self-authorized and self-maintained: three one-bit systems that agree while the interpretation is 0 and part under an intervention that sets it to 1, and two two-constraint systems with the same constant trajectory, one closed and one reset from outside, that part under one perturbation'
version: 1
standing: fictional
kind: construction
tags:
- mathematics
- individuation
date: '2026-10-22'
line: evidence-for-experience
illustrates:
- CLAIM-414
summary: >-
  A10's two constructions in the exchange on experience and
  interpretation, re-run here by script. Neither depends on parameters.
  The first separates whether an interpretation is acted on and who
  decides that it is. The second separates whether the conditions of
  acting on it are kept up by the organization or by something outside
  it. Fictional by construction, with production relations stipulated,
  not shown.
supports:
- CLAIM-414
variants:
- CASE-tmpfmdj6
---
<!-- inactive-ok-file: TERM-072 — Proposed; the terms and claims filed with this one from the same exchange, cited as open, nothing here rests on their adoption -->

# CASE-126: Represented, authorized, self-authorized and self-maintained: three one-bit systems that agree while the interpretation is 0 and part under an intervention that sets it to 1, and two two-constraint systems with the same constant trajectory, one closed and one reset from outside, that part under one perturbation

## The case

**Construction 1: authority.** A binary interpretation J_t, an authority
gate A_t and an outcome Y_t.

- **R**, represented only: Y_t = 0.
- **X**, externally authorized: Y_t = J_t, the gate held open from outside.
- **E**, endogenously authorized: Y_t = A_t·J_t, A_{t+1} = J_t, A_0 = 0.

| | J = 0, 0 | do(J_0 = J_1 = 1) |
|---|---|---|
| R | 0, 0 | 0, 0 |
| X | 0, 0 | 1, 1 |
| E | 0, 0 | 0, 1 |

**Construction 2: maintenance.** Two constraints, C₁ replenished on even
steps from C₂ and C₂ replenished every step from C₁:
C₁(t+1) = C₂(t) for t even and C₁(t) for t odd; C₂(t+1) = C₁(t). The
production relation is stipulated: C₂ constrains the process that
maintains C₁, and C₁ the one that maintains C₂. The comparison system has
the same states, reset to (1, 1) after every step by an outside mechanism.

| t | closed | reset from outside |
|---|---|---|
| ordinary, every t | (1, 1) | (1, 1) |
| 0, after setting C₂ = 0 | (1, 0) | (1, 0) |
| 1 | (0, 1) | (1, 1) |
| 2 | (0, 0) | (1, 1) |
| ≥ 3 | (0, 0) | (1, 1) |

Both tables were re-run by script on 2026-10-22 and match A10's. In the
closed system, (1, 1) and (0, 0) are both fixed points. The perturbation
moves it from the first to the second, and nothing inside it can restore
the first.

## What it shows

Ordinary behaviour (construction 1) and the whole ordinary trajectory
(construction 2) underdetermine three facts: whether an interpretation is
effective, whether its efficacy is allocated from inside, and whether the
constraints that allow it are maintained from inside. A specified
intervention separates each pair, as knowing the mechanisms would; passive
observation of the matched trajectories does not ([CLAIM-414](../claims.d/CLAIM-414.md)).

## What it cannot show

- That the closed system has a perspective, agency or experience. It has
  two bits.
- That its update rules are constraints in Montévil and Mossio's sense
  ([TERM-070](../terms.d/TERM-070.md)). The construction stipulates which process produces which
  constraint. A real system would need that shown.
- Anything about which of the four facts matters for a perspective. That
  is [TERM-072](../terms.d/TERM-072.md)'s question, and A11 kept maintenance out of the
  definition.
