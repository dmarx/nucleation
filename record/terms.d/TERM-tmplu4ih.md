---
status: Active
title: 'conferral, between an organization''s processes: any effect one process has on another''s share of future influence, of which an explicit vote is one case; negative conferral withdraws influence'
version: 1
tags:
- self-governance
- social-ontology
date: '2026-11-04'
line: distributed-agency
summary: >-
  TERM-053's definition under a new name, at the owner's decision
  (ADR-070). Process i confers influence on process j in region x to the
  extent that an intervention of i raises j's chance of acquiring
  influence there; a negative effect is negative conferral. Attending to
  j's output, keeping it active, passing it resources and suppressing its
  rivals all confer. It is an effect, not a stance: not Frankfurt's
  endorsement (TERM-tmp0evbm), and not a grant (TERM-tmp08c21), which is
  conferral through a maintained relation.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070; named as the former word for conferral -->
<!-- inactive-ok-file: TERM-tmp0evbm CLAIM-285 CLAIM-367 THEORY-120 — Proposed or new; cited as open -->

# TERM-tmplu4ih: conferral, between an organization's processes: any effect one process has on another's share of future influence, of which an explicit vote is one case; negative conferral withdraws influence

## Definition

This is TERM-053's definition, renamed by ADR-070. Counterfactually,

  C_ij(x, t) = ∂I_j(x, t + Δt)/∂u_i(t),

where u_i is an intervention available to i and I_j is j's influence in
region x. Positive values are conferral, negative values withdrawal or
opposition. A5 §7's examples, from TERM-053: "Allocating attention to its
output", "Maintaining its activation", "Transferring representational
resources", "Increasing its eligibility to influence a decision",
"Suppressing competing processes". The budgeted vote of the owner's U2 of
2026-10-13 is the special case in which the effect runs through an
aggregation rule.

As in TERM-053, three quantities are kept apart: the authority a process
holds, what it confers on others, and how far its preferred policies are
realized (CLAIM-285).

## What it is not

- **Not endorsement in Frankfurt's sense.** That is a reflective attitude
  toward a motive, TERM-tmp0evbm. A conferral may be subpersonal and not
  represented, and an attitude may confer nothing (the unwilling addict
  of CASE-112, whose volition falls short of switching the regime).
- **Not a grant.** A grant (TERM-tmp08c21) is conferral that runs through
  a maintained relation of granting, delegation, eligibility or support.
  Suppressing a rival confers on j and grants j nothing.
- **Not an external update rule.** An optimizer that raises a component's
  influence confers nothing, because the effect does not run from an
  intervention available to another process (TERM-053's note of
  2026-10-18; CLAIM-367).
- **Not observable from behaviour alone.** Raised influence is observed;
  who raised it, and how, is the question (TERM-053, quoting A7 §14 and
  A8 §7).

## History

TERM-053 called this "endorsement". The word invited the reflective sense,
and readers took it so, in the exchange "Organizational Nucleation and
SLT" among others (TERM-053's note of 2026-11-04). ADR-070 renames it and
splits off the grant.
