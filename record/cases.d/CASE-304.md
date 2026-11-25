---
number: 304
status: Proposed
formerly:
- CASE-tmpqo06u
title: 'HKB coordination mode near a capacity fold'
statement: >-
  A coordination mode kept by a capacity near its fold: in the HKB model
  whose coupling c is produced at αc²/(1 + c²) against unit decay, as α
  falls toward 2 the capacity's recovery rate at its stable level goes to
  zero while anti-phase coordination stays stable, its relaxation time near
  1
version: 1
standing: stipulated
kind: construction
tags:
- complex-systems
- mathematics
date: '2026-11-21'
line:
- distributed-agency
- formal-apparatus
variant_of:
- CASE-227
illustrates:
- CLAIM-521
summary: >-
  The near case that [ARG-068](../arguments.d/ARG-068.md)'s body computes and no entry held, filed on
  the owner's view that the conclusions the sweep under [ADR-136](../decisions.d/ADR-136.md) left
  without an entry "don't look useless". It is [CASE-227](CASE-227.md)'s model
  (φ̇ = −sin φ − c sin 2φ, with c produced at αc²/(1 + c²) against unit
  decay) at its upper branch near the fold, where [CASE-227](CASE-227.md) sat at its
  threshold instead. As α falls toward 2, the stable level
  c₊ = (α + √(α² − 4))/2 falls toward 1 and the capacity's maintenance
  eigenvalue −(c₊² − 1)/(c₊² + 1)·ε goes to zero, while anti-phase stays
  stable with relaxation time 1/(2c₊ − 1) near 1 and barrier near ¼. So
  the coordination's own stability does not reveal that its maintenance is
  losing its recovery rate: [CLAIM-521](../claims.d/CLAIM-521.md)'s dissociation, with an HKB
  coupling. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-227 ARG-068 — Proposed, Rejected or new; the case this varies, the argument whose body held it, and the decision -->

# CASE-304: HKB coordination mode near a capacity fold

**The construction.** The relative phase follows φ̇ = −sin φ − c sin 2φ, and anti-phase (φ = π) is stable when c > ½, with relaxation time 1/(2c − 1) and escape barrier (2c − 1)²/(4c) ([CASE-227](CASE-227.md)). The capacity c is produced at αc²/(1 + c²) and decays at unit rate, on the slow scale ε: ċ = ε(αc²/(1 + c²) − c). For α > 2 it has two positive levels, c± = (α ± √(α² − 4))/2: c₋ unstable, the ignition threshold, and c₊ stable. Its eigenvalue at an equilibrium is ε(1 − c²)/(1 + c²).

**Near the fold.** As α falls toward 2, c₊ and c₋ meet at 1, a saddle-node. Checked with `python3 -I`:

| α | c₊ | c₋ | maintenance eigenvalue at c₊ | anti-phase relaxation time | barrier |
|---|---|---|---|---|---|
| 2.2 ([CASE-227](CASE-227.md)) | 1.558 | 0.642 | −0.417ε | 0.47 | 0.72 |
| 2.01 | 1.105 | 0.905 | −0.100ε | 0.83 | 0.33 |
| 2.001 | 1.032 | 0.969 | −0.032ε | 0.94 | 0.27 |

The capacity's recovery rate goes to zero, while the coordination stays stable, with a relaxation time near 1 and a barrier near ¼ that does not close. An observer who reads only the coordination's stability sees nothing alarming as the maintenance loses its recovery rate.

**How it differs from [CASE-227](CASE-227.md).** [CASE-227](CASE-227.md) starts below the unstable level, so the capacity decays as a transient and the coordination's own stability falls with it. That is [CLAIM-604](../claims.d/CLAIM-604.md)'s threshold, not [CLAIM-521](../claims.d/CLAIM-521.md)'s fold, as [ARG-068](../arguments.d/ARG-068.md) found. Here the system sits at its stable level, and slowing appears in the maintenance, not in the coupling, as [CLAIM-521](../claims.d/CLAIM-521.md) says. [CLAIM-521](../claims.d/CLAIM-521.md)'s note of 2026-11-07 records a rebuild with Adler coupling; this is the HKB version.

**Where it came from.** [ARG-068](../arguments.d/ARG-068.md)'s section "What would bear on the conclusion" computed the α = 2.01 and 2.001 rows. They are filed here as an entry of their own ([ADR-136](../decisions.d/ADR-136.md)).
