---
number: 53
status: Active
formerly:
- TERM-tmpij1jr
title: 'endorsement, between an organization''s processes: any effect one process has on another''s share of future influence, of which an explicit vote is one case'
version: 1
tags:
- self-governance
- social-ontology
date: '2026-10-13'
line: distributed-agency
summary: >-
  The owner's "vote" at U2, generalized at A5 §7 to an effective causal
  relation. Process i endorses process j in region x to the extent that an
  intervention of i raises j's chance of acquiring influence there.
  Opposition is negative endorsement. Attending to j's output, keeping it
  active, passing it resources and suppressing its rivals are all
  endorsement. The term is about authority among processes. It is not
  Frankfurt's identification with a desire.
used_by:
- CLAIM-285
- CLAIM-336
- CLAIM-375
---
<!-- inactive-ok-file: CLAIM-285 THEORY-120 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# TERM-053: endorsement, between an organization's processes: any effect one process has on another's share of future influence, of which an explicit vote is one case

## Definition

The owner's design at U2 had the processes "essentially vote on how much
influence the other denoisers contribute". A2 began with an endorsement
matrix E_ij, a budgeted distribution of i's support over the others with
E_ii = 0. A5 §7 then asked whether endorsement requires explicit
evaluation: "Perhaps endorsement should be understood more generally as any
process that changes another operator's probability of acquiring influence."
Its examples: "Allocating attention to its output", "Maintaining its
activation", "Transferring representational resources", "Increasing its
eligibility to influence a decision", "Suppressing competing processes".

Counterfactually, E_ij(x, t) = ∂I_j(x, t + Δt)/∂u_i(t), where u_i is an
intervention available to i and I_j is j's influence in region x. A5:
"Positive values correspond to effective endorsement, negative values to
opposition." The budgeted vote is the special case in which the effect runs
through an aggregation rule.

The term distinguishes three quantities: the authority a process holds, its
endorsements of others, and how far its preferred policies are realized
([CLAIM-285](../claims.d/CLAIM-285.md)).

## What it is not

- Not identification. Frankfurt's endorsement is a person's higher-order
  attitude toward a desire ([THEORY-120](../theory.d/THEORY-120.md)). This is a relation between
  processes, and it may be subpersonal and not represented. A10 §2.3:
  "constitutive endorsement may be distributed, subpersonal, and not
  propositionally represented."
- Not agreement. A2 §8: a process "may endorse j's role as an error detector
  without endorsing j's authority over final policy selection."
- Not observable from behaviour alone. A7 §14: "Inferring trust or
  endorsement from observed causal facilitation may conflate authorization,
  incidental coupling, and common-cause effects." On r/place, A8 §7:
  "endorsement remains a latent explanatory hypothesis, not an observed
  variable."

## Note of 2026-10-18: being reinforced is not endorsing

The exchange of 2026-10-17 applied this term to training. A32 §4: "being
reinforced ≠ endorsing". "A network component may acquire greater influence
because the external optimizer makes it more effective. That's different
from the component influencing the future authority of other components
through an internally maintained endorsement relation." A32 also: "a gate
weight is not automatically an endorsement". A33 put it as a chain of three
kinds of object: "a gradient is not an update, and an update is not an
endorsement".

So, beside the three items above: **not an external update rule.** An
optimizer that raises a component's influence is not an endorsement of it
by any process of the organization, because the effect does not run from
an intervention available to another process. This is the clause above on
behaviour, applied to training: raised influence is observed, and who
raised it is the question. Where the governance of updates sits is
[CLAIM-367](../claims.d/CLAIM-367.md).

<!-- inactive-ok-file: CLAIM-367 — Proposed; filed or read from the exchange of 2026-10-17 and cited in the note of 2026-10-18 as open -->
