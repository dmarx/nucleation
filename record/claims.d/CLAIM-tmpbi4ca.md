---
status: Proposed
title: 'For a fixed architecture, the resource threshold for reaching a target configuration need not equal the resource requirement of the target: it is the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a path from 0 to 1 within [0, 1] whose
  largest value of r(q) = 0.7 + 2.4q(1 − q) is below 1.3, a bottleneck
  budget below the larger endpoint requirement, or a mistake in the
  sublevel set at 1.0. Not defeated by resources that are cumulative or
  rate-limited rather than capacities, by several resources at once, or
  by a change of architecture that lowers the threshold; the claim is
  about one capacity under one fixed architecture.
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-05'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-tmps6lqg
- THEORY-tmpqzxwh
complements:
- CLAIM-tmp9jvpb
uses:
- TERM-tmp2ysyt
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4. A's wording,
  with A's own definition of the threshold, B*(A, B) = inf over paths of
  max r along the path, written into it. Demonstrated by A's example
  r(q) = 0.7 + 2.4q(1 − q), checked: both endpoints cost 0.7, the
  threshold is 1.3, and at 1.0 the feasible set has two components.
  Mirth et al. show the threshold is the zero-dimensional merge level of
  the sublevel sets; Berry, Lee-Trimble and Santangelo give a case where
  it is infinite. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmps6lqg THEORY-tmpqzxwh CLAIM-tmp9jvpb CLAIM-tmpuk8gq TERM-tmp2ysyt CASE-tmp06sg5 CASE-tmp0g3pa CLAIM-354 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed, nothing here rests on their being settled -->

# CLAIM-tmpbi4ca: For a fixed architecture, the resource threshold for reaching a target configuration need not equal the resource requirement of the target: it is the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two

## The claim

A: "For a fixed architecture, the resource threshold for reaching a
target configuration need not equal the resource requirement of the
target. It depends on admissible transition paths, and may be infinite
when the configurations are disconnected under the allowed
transformations."

**The construction (A's).** Fix an architecture. Let Q be its
configurations, r(q) the resource it takes to hold q (an instantaneous
capacity), and Γ(A, B) the continuous paths from A to B that the declared
transformations allow. The bottleneck budget is

  B*(A, B) = inf over γ ∈ Γ(A, B) of max_t r(γ(t)),

with the infimum over no paths read as +∞.

- **Never below the endpoints.** Every path contains A and B, so
  B*(A, B) ≥ max(r(A), r(B)).
- **Can be above them.** A's example: Q = [0, 1], A = 0, B = 1,
  r(q) = 0.7 + 2.4q(1 − q). Then r(0) = r(1) = 0.7. Every path from 0 to
  1 in [0, 1] passes through q = 1/2, where r = 1.3, and the straight path
  reaches no more, so B* = 1.3. At a budget of 1.0 the feasible set
  {q : r(q) ≤ 1.0} is q(1 − q) ≤ 1/8, that is [0, 0.1464…] ∪ [0.8536…, 1],
  the roots being (1 ± √½)/2: two components, each endpoint feasible and
  neither reachable from the other. The components merge at 1.3. Checked
  by the filer.
- **Can be infinite.** If the declared transformations admit no path,
  B* = +∞ whatever the endpoints cost.

The gap B* − max(r(A), r(B)) is the reconfiguration slack of the
transition ([TERM-tmp2ysyt](../terms.d/TERM-tmp2ysyt.md)): 0.6 in the example.

**What the readings add.**

- **The threshold is a merge level** (Mirth et al., [NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md);
  [THEORY-tmpqzxwh](../theory.d/THEORY-tmpqzxwh.md)). In sublevel-set persistent homology "two configurations
  are in the same connected component if there is a path between the
  configurations that does not exceed the chosen energy barrier". So B*
  is the level at which A and B first share a component of {r ≤ b}, the
  death of a zero-dimensional bar, the node joining them in a
  disconnectivity graph. That summary keeps only the lowest barrier:
  "Though disconnectivity graphs encode the energy barrier of the minimal
  energy pathway between two local minima, they do not represent multiple
  transition pathways." Other routes and their barriers are in the
  one-dimensional bars, which B* does not use.
- **A case where it is infinite** (Berry, Lee-Trimble and Santangelo,
  [NOTE-tmpt066u](../notes.d/NOTE-tmpt066u.md); [THEORY-tmps6lqg](../theory.d/THEORY-tmps6lqg.md)). For a near-flat rigid origami vertex with
  positive curvature, "the two nappes have split into two disconnected
  components". Every state on either nappe is feasible; under folding
  without self-intersection none on one can reach the other at any cost.
  It is relative to the declared transformations: "Anecdotally, it does
  appear that when faces are allowed to pass through each other,
  isometric trajectories can pass from one nappe to the other for any K."
  A: "impossibility is relative to the declared model of admissible
  transformations".

**The architecture is part of the statement.** Change it and Q, r and Γ
change with it. [CASE-tmp06sg5](../cases.d/CASE-tmp06sg5.md) lowers the threshold in A's example from 1.3
to 1.0 by admitting a switch to a staging architecture as a move, and
[CASE-tmp0g3pa](../cases.d/CASE-tmp0g3pa.md) shows a per-period budget of 1.0 reaching 1.3 by carry-over.

It is the resource-quantitative form of the separation between a feasible
target and a reachable one ([CLAIM-tmp9jvpb](CLAIM-tmp9jvpb.md)).

## What it does not say

- **That the peak is the only cost.** B* is for a capacity that must be
  held at each moment. A's table of resource types also has fixed stock,
  rate limit, cumulative expenditure, replenishable reserve and deadline.
  For cumulative expenditure a path costs its integral, not its peak, and
  time can substitute for peak capacity: A's example is two units for one
  minute against one unit for two.
- **Anything for several resources at once.** Then there is no scalar
  threshold ([CLAIM-tmpuk8gq](CLAIM-tmpuk8gq.md)).
- **That organizations have such an r.** The construction is formal; an
  organizational configuration space with a holding requirement is A's
  model, not something the record has measured.
- **That sublevel-set inclusion is viability.** Mirth et al.'s sublevel
  sets are caps on a scalar, not viability kernels ([THEORY-134](../theory.d/THEORY-134.md)); and
  inclusion of what is reachable under a cap is only a scalar case of the
  inclusion [CLAIM-354](CLAIM-354.md) compares agents by.
