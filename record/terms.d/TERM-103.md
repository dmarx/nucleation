---
number: 103
status: Active
formerly:
- TERM-tmplu4ih
title: 'conferral, between an organization''s processes: any effect one process has on another''s share of future influence, of which an explicit vote is one case; negative conferral withdraws influence'
version: 1
tags:
- self-governance
- social-ontology
date: '2026-11-04'
line: distributed-agency
summary: >-
  [TERM-053](TERM-053.md)'s definition under a new name, at the owner's decision
  ([ADR-070](../decisions.d/ADR-070.md)). Process i confers influence on process j in region x to the
  extent that an intervention of i raises j's chance of acquiring
  influence there; a negative effect is negative conferral. Attending to
  j's output, keeping it active, passing it resources and suppressing its
  rivals all confer. It is an effect, not a stance: not Frankfurt's
  endorsement ([TERM-102](TERM-102.md)), and not a grant ([TERM-101](TERM-101.md)), which is
  conferral through a maintained relation.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070; named as the former word for conferral -->
<!-- inactive-ok-file: CLAIM-285 CLAIM-367 — Proposed or new; cited as open -->

# TERM-103: conferral, between an organization's processes: any effect one process has on another's share of future influence, of which an explicit vote is one case; negative conferral withdraws influence

## Definition

This is [TERM-053](TERM-053.md)'s definition, renamed by [ADR-070](../decisions.d/ADR-070.md). Counterfactually,

  C_ij(x, t) = ∂I_j(x, t + Δt)/∂u_i(t),

where u_i is an intervention available to i and I_j is j's influence in
region x. Positive values are conferral, negative values withdrawal or
opposition. A5 §7's examples, from [TERM-053](TERM-053.md): "Allocating attention to its
output", "Maintaining its activation", "Transferring representational
resources", "Increasing its eligibility to influence a decision",
"Suppressing competing processes". The budgeted vote of the owner's U2 of
2026-10-13 is the special case in which the effect runs through an
aggregation rule.

As in [TERM-053](TERM-053.md), three quantities are kept apart: the authority a process
holds, what it confers on others, and how far its preferred policies are
realized ([CLAIM-285](../claims.d/CLAIM-285.md)).

## What it is not

- **Not endorsement in Frankfurt's sense.** That is a reflective attitude
  toward a motive, [TERM-102](TERM-102.md). A conferral may be subpersonal and not
  represented, and an attitude may confer nothing (the unwilling addict
  of [CASE-112](../cases.d/CASE-112.md), whose volition falls short of switching the regime).
- **Not a grant.** A grant ([TERM-101](TERM-101.md)) is conferral that runs through
  a maintained relation of granting, delegation, eligibility or support.
  Suppressing a rival confers on j and grants j nothing.
- **Not an external update rule.** An optimizer that raises a component's
  influence confers nothing, because the effect does not run from an
  intervention available to another process ([TERM-053](TERM-053.md)'s note of
  2026-10-18; [CLAIM-367](../claims.d/CLAIM-367.md)).
- **Not observable from behaviour alone.** Raised influence is observed;
  who raised it, and how, is the question ([TERM-053](TERM-053.md), quoting A7 §14 and
  A8 §7).

## History

[TERM-053](TERM-053.md) called this "endorsement". The word invited the reflective sense,
and readers took it so, in the exchange "Organizational Nucleation and
SLT" among others ([TERM-053](TERM-053.md)'s note of 2026-11-04). [ADR-070](../decisions.d/ADR-070.md) renames it and
splits off the grant.
