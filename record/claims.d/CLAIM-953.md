---
number: 953
status: Proposed
formerly:
- CLAIM-tmpocjfb
title: 'Where a nucleus forms fast only on a constraint that it produces once formed, and formation is cooperative enough that a founding is needed, the moment after which the outside supply of that constraint can be withdrawn for good is the crossing of a threshold in the joint state of constraint, nuclei and material, and neither the number of nuclei formed nor the share of the constraint they make marks it: in one kinetic construction it was crossed with nuclei at 0.02 % to 30 % of their maintained number and a self-made share of 0.2 % to 65 %'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-093, from the
    runs of CASE-365.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation of CASE-365: a founding schedule in
  that model where withdrawal at the reported shortest time fails, or
  withdrawal earlier succeeds; or a state reported as crossing that lies
  on the empty side of the saddle's stable manifold. Or, for the general
  statement, a cooperative nucleus-constraint loop with a stable empty
  state in which withdrawal is safe exactly when the number of nuclei, or
  the self-made share of the constraint's supply, passes one fixed level
  whatever the founding schedule. Not defeated by loops that ignite from
  nothing and need no founding, which the claim excludes, nor by finite
  systems in which a closed loop is eventually lost, which it does not
  address.
tags:
- complex-systems
- individuation
- mathematics
date: '2026-11-22'
line:
- transient-support
- distributed-agency
grounds:
- CASE-365
uses:
- TERM-117
corroborates:
- CLAIM-604
bears_on:
- QUESTION-399
summary: >-
  [QUESTION-399](../questions.d/QUESTION-399.md) asks for a measure of when a nucleus's loop closes.
  In [CASE-365](../cases.d/CASE-365.md) the answer is a time: the founding by an outside
  teacher can stop once the joint state has crossed the saddle's
  separatrix. That crossing came at very different nucleus counts and
  self-made shares across founding rates and turnovers. A cheap proxy, such
  as "most of the constraint is now made inside" or "the nucleus has
  formed", would withdraw too early in some schedules and too late in
  others. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-365 CASE-265 — new or Proposed; the run this claim is drawn from, and the earlier construction with a joint threshold -->

# CLAIM-953: Where a nucleus forms fast only on a constraint that it produces once formed, and formation is cooperative enough that a founding is needed, the moment after which the outside supply of that constraint can be withdrawn for good is the crossing of a threshold in the joint state of constraint, nuclei and material, and neither the number of nuclei formed nor the share of the constraint they make marks it: in one kinetic construction it was crossed with nuclei at 0.02 % to 30 % of their maintained number and a self-made share of 0.2 % to 65 %

## The claim

In [CASE-365](../cases.d/CASE-365.md) the setup is as follows:

- Nuclei form fast only on a teacher T, at a rate that rises with T².
- Each nucleus makes teachers from material.
- With no outside teacher, there is a stable empty state, a saddle and a
  stable maintained state.

An outside teacher, supplied at σ for a time t_w and then withdrawn for
good, founds the loop only if t_w is long enough. The shortest t_w is when
the loop closes in time. The bisection finds it to within 0.01 time units.

At that moment:

- **Few nuclei.** Nuclei number 0.0006 to 0.45, against 1.5 to 3.6 when
  maintained.
- **Self-made share varies.** The nuclei's share of the teacher supply is
  0.002 to 0.65, depending on σ and on the teacher turnover.
- **Most of the forming is still ahead.** After withdrawal, N takes
  120 to 275 time units to reach half its maintained value.

So the threshold is not a level of either variable. It is the stable
manifold of the saddle, a surface in (m, T, N). Withdrawal is safe once the
state is on the maintained side of it. Since t_w is minimal, withdrawal
just before it fails.

This is [CLAIM-604](../claims.d/CLAIM-604.md)'s ignition threshold in a loop of two constraints.
Here it is a surface and not a level, as it is in [CASE-265](../cases.d/CASE-265.md)'s
mutual-maintenance model, now for a loop in which the nucleus also speeds
formation ([TERM-117](../terms.d/TERM-117.md)).

## What it does not say

- **No proxy is ruled out in general.** A measure of the joint state could
  well track the separatrix in a given system. The claim is only that
  neither nucleus count nor self-made share does.
- **Material.** Closure here is of the teacher loop alone. Material must
  still be supplied ([CASE-365](../cases.d/CASE-365.md), e3).
- **Finite systems.** In finite numbers, crossing the threshold buys a
  lifetime, not permanence (e9).

## Note of 2026-11-25: rerun, and what holds it back

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of LEAD-tmpc0rqa, at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). CASE-365's study was regenerated from nothing (its note of this date), and every figure this claim states matches: at the shortest founding, nuclei 0.0006 to 0.45 against 1.49 to 3.57 maintained (0.017 % to 30 %), the self-made share 0.0024 to 0.649, and the halving after withdrawal 122 to 275 time units over the eleven schedules. What holds it back: ADR-057's first criterion. Its one ground, CASE-365, stays Proposed, held by a misstated figure in its text (the halving with the supply kept on, 8.4 to 105.6 and not 8 to 39), which this claim does not quote. It can go Active with CASE-365. The note is the assistant's (Claude, in this session). No status change.
