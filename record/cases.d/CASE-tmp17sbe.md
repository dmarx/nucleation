---
status: Proposed
title: 'The staging experiment run on a model with a home and a staging architecture and one capacity: every kind of case A named occurs on an open region of budget and reserve, admitting the staging architecture creates reachability or only lowers the bottleneck budget according to whether the home space is connected, and a deadline shorter than every staging route takes the architectural remedy away'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-075 as a
    delegated lead worker. The model, its tests and its results are
    committed under scratch/studies/lead-075/.
standing: documented
kind: executed-study
tags:
- operations-research
- mathematics
date: '2026-11-22'
line:
- realizability
- readiness
variant_of:
- CASE-198
bears_on:
- QUESTION-392
summary: >-
  [LEAD-075](../leads.d/LEAD-075.md) asked for A's staging experiment of [QUESTION-392](../questions.d/QUESTION-392.md): states A and B
  with a staging state C, measuring the bottleneck budget B*(A,B) of
  [CLAIM-571](../claims.d/CLAIM-571.md), the least time T*(A,B;b) at budget b and the readiness of
  [TERM-115](../terms.d/TERM-115.md). It was run on [CASE-198](CASE-198.md)'s model, a configuration q on [0, 1]
  under a home or a staging architecture, with its numbers, over budget,
  reserve, deadline and the model's parameters; numpy, 14 pytest tests.
  With the staging architecture admitted, B* falls from 1.3 to 1.0, and
  the cases A asked for all occur on open regions of budget and reserve:
  statically feasible but unreachable, reachable but too expensive,
  reachable only through the architectural change, reachable only with a
  temporary reserve, and two compound kinds, either remedy sufficing and
  both needed together. The staging routes are slow: every one takes at
  least 2.58 time units where the home route takes 1, so at a deadline of
  2 admitting the staging architecture changes nothing, and the kind
  "only through architectural change" disappears. In a 960-point sweep,
  admitting it created reachability in every setting with a disconnected
  home space and only lowered B* (or did nothing) in every connected one.
  A fictional model run for real: the computation is documented, the
  organization is not. The modelling choices are the assistant's
  (Claude, in this session); adopting them is the owner's call.
---
<!-- inactive-ok-file: CASE-198 — Proposed; the case this study runs, cited as filed -->
<!-- inactive-ok-file: CLAIM-tmpmvt0a — new; the claim filed from this study in the same batch -->

# CASE-tmp17sbe: The staging experiment run on a model with a home and a staging architecture and one capacity: every kind of case A named occurs on an open region of budget and reserve, admitting the staging architecture creates reachability or only lowers the bottleneck budget according to whether the home space is connected, and a deadline shorter than every staging route takes the architectural remedy away

## What was done

[QUESTION-392](../questions.d/QUESTION-392.md) records A's proposed experiment: states A and B and a
staging state C, measuring the bottleneck budget B*(A,B) of [CLAIM-571](../claims.d/CLAIM-571.md),
the least time T*(A,B;b) at budget b, and the readiness R^π(A→B;b,z) in
[TERM-115](../terms.d/TERM-115.md)'s sense, so as to produce cases "where B is statically feasible
but unreachable, reachable but too expensive, reachable only through an
architectural change, or reachable only when temporary reserve capacity is
available." [LEAD-075](../leads.d/LEAD-075.md) asked for it to be run. It was run on a computer, in
numpy, with 14 pytest tests (scratch/studies/lead-075/, whose README says
how to rerun it in about three minutes).

**The model.** [CASE-198](CASE-198.md)'s, made a graph. A state is (q, z), q on a
grid of 201 points on [0, 1] and z the home architecture or the staging one;
A = (0, home), B = (1, home), and the staging state C is any (q, staging).
One capacity. Holding costs r0(q) = 0.7 + 2.4q(1 − q) under home and
r1(q) = 0.8 + 0.4q(1 − q) under staging; a switch of architecture at q
peaks at max(r0, r1) + 0.2. A step along q costs the dearer of its ends.
Crossing [0, 1] takes 1 under home and 2 under staging; a switch takes 0.5.
Moves are reversible. Variants: a crease constraint forbidding home steps
in q ∈ (0.45, 0.55), which disconnects the home space; switching allowed
only on q ≤ 0.4; a dearer staging architecture, r1 = 1.0 + 0.4q(1 − q).

**The measures.** B*(Z), the least peak over paths using the
architectures in the repertoire Z ({home}, or {home, staging}); T*(b; Z),
the least time over paths whose peak is within b; c_τ(Z), the least
capacity that reaches B by a deadline τ; and readiness, the probability of
being at B by τ when the contingency is imposed while a background load
U ~ Uniform[0, 0.3] holds part of the budget b and a temporary reserve
of 0.2 is there with probability 0.5, under the policy that takes the
fastest route its capacity and repertoire allow. Holding B afterwards must
not need the reserve.

**The kinds.** At budget b and reserve ρ: reachable as is
(B*(home) ≤ b); only through the architectural change
(B*(staging) ≤ b < B*(home) and b + ρ < B*(home)); only with the reserve
(B*(home) ≤ b + ρ and B*(staging) > b); either remedy; both together;
reachable but too expensive (finite B* above b + ρ); statically feasible
but unreachable (no path, both ends holdable). Under a deadline, c_τ
replaces B*, and "reachable, but not by the deadline" is its own kind.

The choices the lead left open, each with its reason, are in the README:
C read as a staging architecture, as [CASE-198](CASE-198.md) reads it; the
disconnection made by a crease constraint, [CLAIM-568](../claims.d/CLAIM-568.md)'s geometric kind;
time depending only on the route, not on headroom; z in R^π read as the
repertoire of architectures the policy may use.

## Results

**Bottleneck budgets.** B*(home) = 1.3 ([CASE-233](CASE-233.md)), B*(staging
admitted) = 1.0 ([CASE-198](CASE-198.md)), both reproduced. With the crease constraint,
B*(home) is infinite and B*(staging admitted) is 1.0. With switching only
on q ≤ 0.4 and the crease, both are infinite. With the dearer staging
architecture, 1.3 and 1.2.

**The kinds over budget and reserve** (base model; b from 0.6 to 1.5,
ρ from 0 to 0.6, step 0.025; ends cost 0.7):

| budget b | kind |
|---|---|
| below 0.7 | not holdable |
| 0.7 to 1.0 | only with the reserve if b + ρ ≥ 1.3; both together if 1.0 ≤ b + ρ < 1.3; too expensive if b + ρ < 1.0 |
| 1.0 to 1.3 | either remedy if b + ρ ≥ 1.3; only through the architectural change otherwise |
| 1.3 and above | reachable as is |

Each of A's four kinds has a witness: statically feasible but unreachable
at b = 1.0 in the variant with the crease and switching only on q ≤ 0.4;
reachable but too expensive at b = 0.8, ρ = 0.1; only through the
architectural change at b = 1.1, ρ = 0.1; only with the reserve at
b = 0.95, ρ = 0.4. With the crease the home space is disconnected, and
every case reachable at all is reachable only through the architectural
change (b ≥ 1.0) or with it and the reserve together. With the dearer
staging architecture "only through the architectural change" shrinks to
the band 1.2 ≤ b < 1.3 with b + ρ < 1.3.

**Least time.** Home only: T* = 1 for b ≥ 1.3, unreachable below.
Staging admitted: T* = 3.0 at b = 1.0, falling in small steps to 2.58
just below 1.3 as more of the crossing can stay under home (the switch
moves inward), then 1.0 at b = 1.3. With the crease, T* falls from 3.0 at
b = 1.0 to 2.1 at b ≈ 1.49, where only the forbidden stretch is crossed
under staging. Every route through the staging architecture pays two
switches and a slower crossing, so the budget that admitting the staging
architecture saves is bought with time.

**Deadlines.** At τ = 2 no staging route arrives in time: c_τ is 1.3
with or without the staging architecture, and the kinds "only through
the architectural change", "either" and "both together" vanish; their
cells become "only with the reserve" or "too expensive". With the crease
at τ = 2, every holdable case is "reachable, but not by the deadline". At
τ = 2.8, c_τ(staging admitted) = 1.116; at τ = 3, 1.0, and the untimed
picture returns.

**Readiness** (base, no reserve): at τ ≥ 3, R rises linearly from 0 at
b = 1.0 to 1 at b = 1.3 with the staging architecture admitted, and from 0
at 1.3 to 1 at 1.6 without it; at τ = 2.8 the first curve starts at
1.116 instead; at τ ≤ 2 the two curves are the same. The reserve, there
half the time, moves each curve left by up to 0.2 and caps its first part
at half. Exact values were checked against a Monte Carlo simulation of the
contingency.

**What admitting the staging architecture does** (960 settings: crease or
not, home barrier 0.4 to 3.2, staging holding cost 0.7 to 1.2, switch
surcharge 0 to 0.4, staging barrier 0 to 1.2). With the crease, it
creates reachability in all 480. Without it, it lowers B* in 211 and
changes nothing in 269. In every setting,
B*(staging admitted) = min(B*(home), max(max(0.7, h1) + s, h1 + β1/4)),
which follows because every path passes q = 1/2, and passing it under
staging needs at least one switch. A budget or a reserve never changes B*
or T*; it changes only whether the capacity meets them.

## What it can show

- **That A's four kinds are all realized**, with two compound kinds
  beside them, in one small model, so none of them is empty
  ([LEAD-075](../leads.d/LEAD-075.md)'s "what would count"). What separates them is two thresholds
  per repertoire set against the budget and the budget plus the reserve.
- **That the same intervention is capability-creating in one setting and
  cost-lowering in another.** Admitting the staging architecture creates
  reachability where the home space is disconnected and lowers the
  bottleneck where it is connected. Whether it creates a capability is
  read off the home architecture, not off the intervention
  ([CLAIM-tmpmvt0a](../claims.d/CLAIM-tmpmvt0a.md)).
- **That the kind of a case depends on the contingency's deadline.** The
  architectural remedy saves capacity and costs time, so a tight deadline
  turns "only through the architectural change" into "only with the
  reserve", or into "not in time".

## What it cannot show

- **Anything about real organizations.** The costs and times are invented;
  the computation is real, the system is not.
- **That a staging route is always slower.** Here it is because the
  staging crossing was set to take twice as long and switches take time;
  with a faster staging architecture the trade would go the other way.
- **Several resources, cumulative costs, or uncertainty along the way.**
  One capacity, fixed for the transition; the uncertainty is only at the
  start.
- **Policies that are not the best for their repertoire.** Readiness was
  computed only for the policy that takes the fastest admissible route;
  [TERM-115](../terms.d/TERM-115.md) is about the policy actually followed.
