---
number: 198
status: Proposed
formerly:
- CASE-tmp06sg5
title: 'An architecture-mediated transition: moving between two configurations by first switching to a staging architecture under which the path is cheaper, moving, then switching back, lowers the peak resource need from 1.3 to 1.0'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Names CASE-233, the example it alters, by variant_of, now that
    CLAIM-571's construction is a case (ADR-096). No other change.
standing: fictional
kind: construction
tags:
- mathematics
- operations-research
- complex-systems
date: '2026-11-05'
line:
- readiness
- realizability
variant_of:
- CASE-233
illustrates:
- CLAIM-571
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: the
  architecture-mediated transition (q_A,z0)→(q_A,z1)→(q_B,z1)→(q_B,z0),
  with A's states A and B and a staging C. A gives the sequence only; the
  numbers are the filer's. Under the home architecture the move costs
  1.3 at its peak; switching to a staging architecture that is dearer to
  hold but flatter to cross, crossing, and switching back costs 1.0. The
  bottleneck of a fixed architecture is not the bottleneck once changing
  the architecture is a move. The construction is the filer's, from A's
  architecture-mediated transition; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-233 ADR-096 — Proposed; the construction this case alters, and the decision that filed it -->
<!-- inactive-ok-file: CASE-208 — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->

# CASE-198: An architecture-mediated transition: moving between two configurations by first switching to a staging architecture under which the path is cheaper, moving, then switching back, lowers the peak resource need from 1.3 to 1.0

## The case

**Setting.** A state is a pair (q, z): a configuration q ∈ [0, 1] and an
architecture z ∈ {z0, z1}. The organization holds q_A = 0 under its home
architecture z0 and is to reach q_B = 1, also under z0. One resource, a
capacity; [CLAIM-571](../claims.d/CLAIM-571.md)'s bottleneck budget is the least peak over
admissible paths.

**The two architectures (the filer's numbers).**

- **Home, z0**: r(q, z0) = 0.7 + 2.4q(1 − q), A's example. The endpoints
  cost 0.7, the midpoint 1.3.
- **Staging, z1**: r(q, z1) = 0.8 + 0.4q(1 − q). Dearer to hold at the
  endpoints, 0.8, and flatter across, peaking at 0.9.
- **Switching** z at a fixed q costs the dearer of the two architectures
  there, plus s = 0.2 for the switch itself.

**Two routes.**

- **Direct**, (0, z0) → (1, z0): peak 1.3.
- **Architecture-mediated**, A's sequence (q_A,z0)→(q_A,z1)→(q_B,z1)→(q_B,z0):
  - switch at q = 0: max(0.7, 0.8) + 0.2 = 1.0;
  - cross under z1: peak 0.9;
  - switch back at q = 1: 1.0.

  Peak 1.0.

No route does better. A route that never switches stays under z0 and
peaks at 1.3; a route that switches anywhere pays at least
0.8 + 0.2 = 1.0, since r(q, z1) ≥ 0.8 everywhere. So with architecture
changes admitted the bottleneck budget is 1.0, and the reconfiguration
slack ([TERM-106](../terms.d/TERM-106.md)) falls from 0.6 to 0.3. Checked by the filer.

## What it can show

- **That the qualifier *for a fixed architecture* is load-bearing** in [CLAIM-571](../claims.d/CLAIM-571.md).
  An organization that cannot afford a transition under its present
  architecture may afford it by changing the architecture first. A: the
  readiness that matters may be "transition capability", R^π(c|b,z),
  conditioned on the budget and the architecture.
- **Why a staging architecture is not a place to stay.** z1 costs 0.8 to
  hold where z0 costs 0.7. It is worth entering only for the crossing.
  This is A's proposed experiment's "staging C" between states A and B.
- **That the capacity to transform the architecture is a separate
  capacity.** The route needs the organization to be able to switch z at
  all. [CLAIM-025](../claims.d/CLAIM-025.md) holds that an operative regime, the governing
  organization among regimes, and the capacity to transform that
  organization can persist or fail separately; here the third decides
  whether the cheaper route exists.

## What it cannot show

- **That real reorganizations have such costs.** The functions are
  invented to make the comparison exact.
- **Anything about time or cumulative cost.** Three steps instead of one
  may take longer and spend more in total; only the peak is compared.
- **That the switch is reversible at the stated cost**, or that it leaves
  the organization's commitments intact. Both are assumed.

## Note of 2026-11-05: A's resource models and further distinctions

[CASE-208](CASE-208.md) is a physical counterpart: in Zang et al.'s Kresling stack, prestress applied from outside reorders the barriers and opens transitions that no budget under the old arrangement opens. No status changes.
