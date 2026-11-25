---
number: 916
status: Proposed
formerly:
- CLAIM-tmpke0ap
title: 'What realizes a capacity fixes its constraints'
statement: >-
  A regulatory capacity's constraint set is fixed by what realizes it: K
  holds each constraint the capacity's own constraints depend on for their
  production, at the least level at which what depends on it is still
  produced, so once the agent and the capacity are named only the agent's
  boundary is left to choose
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §8.6, §12.6. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A case in which, with the agent's boundary and the capacity both fixed,
  two constraint sets that each satisfy the rule (membership by production
  dependence, each threshold the least level at which what depends on the
  constraint is still produced) give opposite verdicts on whether the
  capacity is precarious. Or a regulatory capacity that can be lost while
  every constraint it depends on stands at its level, so that the rule's K
  misses the loss. Not defeated by a case where the dependencies are
  unknown: the rule says where K comes from, not that it is easy to find.
tags:
- agency
- self-governance
- complex-systems
date: '2026-11-22'
line:
- will-organization
grounds:
- THEORY-134
- CASE-342
uses:
- TERM-070
complements:
- CLAIM-195
bears_on:
- QUESTION-128
summary: >-
  [LEAD-053](../leads.d/LEAD-053.md)'s rule for [ARG-007](../arguments.d/ARG-007.md)'s weakest step, the choice of the maintenance
  constraints K for an agent's regulatory capacities. Membership of K by
  production dependence ([TERM-070](../terms.d/TERM-070.md)'s "depends on") from the constraints that
  realize the named capacity; each threshold set by what depends on the
  constraint, ending at the level at which the capacity can be exercised;
  a union over substitutable routes. The kernel then comes from the
  dynamics, and K stays distinct from it. What is left to choose is the
  agent's boundary, filed as two readings, [CLAIM-917](CLAIM-917.md) (narrow) and
  [CLAIM-915](CLAIM-915.md) (wide), for the owner. Tested in [CASE-342](../cases.d/CASE-342.md). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CASE-342 CLAIM-917 CLAIM-915 — new, filed in this pull request for LEAD-053 -->
<!-- inactive-ok-file: CASE-227 — Proposed; a case the rule is tested on, cited as open -->

# CLAIM-916: What realizes a capacity fixes its constraints

## The claim

[ARG-007](../arguments.d/ARG-007.md)'s mapping premise: applying viability needs a constraint set K,
and the paper "gives no non-arbitrary way to choose the maintenance
constraints for an agent's regulatory capacities". [THEORY-134](../theory.d/THEORY-134.md) is explicit
that viability theory "takes the answer as given". This claim gives a rule.

Name the capacity C whose loss is at issue: for [CLAIM-099](CLAIM-099.md), the capacity
to govern among regimes. Then:

1. **Realizers.** R is the set of the agent's constraints whose standing
   makes C exercisable: in [CASE-036](../cases.d/CASE-036.md), the lifting decision and the
   evidence it is judged on.
2. **Membership by dependence.** K constrains R and every constraint R
   depends on for its production, directly or through others, in
   [TERM-070](../terms.d/TERM-070.md)'s sense: C₁ depends on C₂ when C₂ constrains a process that
   produces C₁. The regime C governs is not a member unless C depends on
   it. K is about the capacity, not about the operative regime.
3. **Thresholds by function.** Each member must stand at the least level at
   which the constraints depending on it are still produced; for the
   members of R, the least level at which C can be exercised. The levels
   are read off what each constraint maintains, so K is fixed apart from
   the member's own dynamics, as [THEORY-134](../theory.d/THEORY-134.md) requires.
4. **Routes.** Where C can be realized by substitutable routes, K is the
   union, over routes, of the states in which every member of that route
   stands.

The viability kernel of K is then computed from the dynamics, and C is
precarious at a state that lies in K near the kernel's edge, or in K and
outside the kernel.

**Why this is not arbitrary.** Once C and the agent are named, nothing in
steps 1–4 is the analyst's choice: what produces what, and at what level a
constraint stops producing what depends on it, are facts about the system
at a time scale ([CLAIM-395](CLAIM-395.md)), however hard to find. C is fixed by the claim
under test; [CLAIM-099](CLAIM-099.md) names it. What remains open is the agent's boundary:
whether a constraint C depends on, produced outside the agent, is a member
of K or a condition under which K is assessed. That is the one choice left,
and it is filed as two readings for the owner, the narrow
[CLAIM-917](CLAIM-917.md) and the wide [CLAIM-915](CLAIM-915.md).

**Two thresholds it rules out, and why.**

- *The separatrix.* Setting each member's level at the edge of the basin
  of its maintained state ([CASE-111](../cases.d/CASE-111.md)'s b₋) makes K the basin, so K and
  its kernel coincide by construction and [CLAIM-079](CLAIM-079.md)'s gap, a state that
  satisfies K with no trajectory that keeps satisfying it, can never
  arise. The level must come from what the constraint maintains, not from
  its own dynamics.
- *Any positive level.* K = {b > 0} is never left by a decay toward zero,
  so on [CASE-111](../cases.d/CASE-111.md)'s lower branch every state is viable and nothing is
  precarious.

**The test.** [CASE-342](../cases.d/CASE-342.md) applies the rule to [CASE-036](../cases.d/CASE-036.md), the ground
of [ARG-007](../arguments.d/ARG-007.md), and to [CASE-111](../cases.d/CASE-111.md), [CASE-112](../cases.d/CASE-112.md) and [CASE-227](../cases.d/CASE-227.md). On Northstar,
as a finite toy, the organization's operative trajectory leaves K while the
emergency regime and its criteria hold throughout, and the rival in which
the organization's own standard is K ([CLAIM-195](CLAIM-195.md)'s route carried to an
agent) registers nothing. On [CASE-227](../cases.d/CASE-227.md) K is c > ½, set by the
anti-phase mode c maintains, and the kernel is c ≥ 0.642, set by c's own
production: the case's c = 0.6 is in K and outside the kernel, which is
the case's point, now with K chosen by rule.

## What it does not say

- **That the dependencies are known.** For an organization they are an
  empirical matter; the rule says where K comes from, not how to measure
  it. In [CASE-036](../cases.d/CASE-036.md) the case text states them, which is why the test can
  run.
- **That the K it gives ought to be kept.** It fixes what the capacity
  needs, not whether the capacity is worth having ([CLAIM-075](CLAIM-075.md)). It answers
  [QUESTION-128](../questions.d/QUESTION-128.md)'s "It does not explain why K is the right set" only on
  the functional rung: right for C, not right simply.
- **That the agent's boundary is settled.** That is the remaining choice,
  left to individuation ([CLAIM-152](CLAIM-152.md)) and to the owner's reading.
- **That the agent's own standard is irrelevant.** For an argument the
  record stipulates K ([CLAIM-195](CLAIM-195.md)), and nothing here says it should not.
  The test shows only that a stipulated K cannot do [ARG-007](../arguments.d/ARG-007.md)'s work,
  because on Northstar the stipulated standard is the lock-in's own
  ([TERM-020](../terms.d/TERM-020.md), step 4).
