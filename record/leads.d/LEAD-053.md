---
number: 53
status: Open
formerly:
- LEAD-tmp92u7x
title: 'Find a non-arbitrary way to choose the constraint set for an agent''s regulatory capacities'
version: 1
stage: idea
priority: medium
method:
- conceptual
- formal
tags:
- agency
- self-governance
date: '2026-11-19'
line:
- will-organization
advances:
- CLAIM-099
summary: >-
  Named in [ARG-007](../arguments.d/ARG-007.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-tmpke0ap CLAIM-tmpnhrot CLAIM-tmp8onwv CASE-tmp6mcpv — new, filed under LEAD-053 on 2026-11-22 -->

# LEAD-053: Find a non-arbitrary way to choose the constraint set for an agent's regulatory capacities

## What it would do

Propose a rule for choosing the set and test it on the record's cases.

Where the record names it:

- [ARG-007](../arguments.d/ARG-007.md): "gives no non-arbitrary way to choose the maintenance
  constraints"

## What would count

A rule meets [ARG-007](../arguments.d/ARG-007.md)'s weakest step.

## Note of 2026-11-22: carried out by a delegated lead worker

Done, on the branch claude/lead-053-maintenance-rule:

- **The rule**, [CLAIM-tmpke0ap](../claims.d/CLAIM-tmpke0ap.md) (Proposed): K holds the constraints that
  realize the named capacity and every constraint they depend on for their
  production ([TERM-070](../terms.d/TERM-070.md)), each at the least level at which what depends on
  it is still produced, with a union over substitutable routes. Two
  thresholds are ruled out with reasons: the separatrix (K becomes its own
  kernel) and any positive level (never left by decay).
- **The one choice it leaves**, the agent's boundary, filed as two
  alternatives for the owner: narrow, [CLAIM-tmpnhrot](../claims.d/CLAIM-tmpnhrot.md) (an outside-produced
  dependency is a condition), and wide, [CLAIM-tmp8onwv](../claims.d/CLAIM-tmp8onwv.md) (it is a member of
  K).
- **The test**, [CASE-tmp6mcpv](../cases.d/CASE-tmp6mcpv.md) (executed-study), on [CASE-036](../cases.d/CASE-036.md) as a finite toy
  with a computed viability kernel, and on [CASE-111](../cases.d/CASE-111.md), [CASE-112](../cases.d/CASE-112.md) and
  [CASE-227](../cases.d/CASE-227.md). On Northstar the operative trajectory leaves K while the
  regime and its criteria hold; a stipulated K ([CLAIM-195](../claims.d/CLAIM-195.md)'s route) sees
  nothing. Script and tests in scratch/studies/lead-053/.

Remaining: the owner's choice between the two readings; and a test on a
documented case whose dependencies are measured, not stated ([CASE-135](../cases.d/CASE-135.md) or
[CASE-176](../cases.d/CASE-176.md) are candidates). [ARG-007](../arguments.d/ARG-007.md)'s "What would count" is met if the rule
is adopted, up to the boundary choice. The status and stage are the
owner's.
