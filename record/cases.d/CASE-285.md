---
number: 285
formerly:
- CASE-tmpdn372
status: Proposed
title: 'A proposed study: two arrangements whose overseer has the same authority and resources differ only in how fast the acting institution can make its actions irreversible, and precommitted limits, automatic suspension and pauses are added in turn, to tell the value of delay from the value of control over when execution is allowed'
version: 1
standing: stipulated
kind: proposed-study
tags:
- society-and-governance
- philosophy-of-technology
- operations-research
date: '2026-11-17'
line:
- distributed-agency
- dependence-and-domination
variant_of:
- CASE-003
illustrates:
- CLAIM-731
- CLAIM-730
- CLAIM-710
bears_on:
- QUESTION-278
summary: >-
  From A33 §10 C of the exchange "Assess Depp Heard Abuse" (2026-11-15),
  "Same formal oversight, different timescales": "Construct two
  arrangements in which the overseer has identical authority and
  resources. Vary only the speed of the acting institution, with
  corresponding deadlines for preventing irreversible consequences." A
  presents it as an extension of [CASE-003](CASE-003.md) and says correctly that
  [CASE-003](CASE-003.md) varies escalation authority, not timing. It is the cleanest
  test of the owner's U11 ([CLAIM-710](../claims.d/CLAIM-710.md)) and U13, of [CLAIM-464](../claims.d/CLAIM-464.md) and of
  [CLAIM-462](../claims.d/CLAIM-462.md) that the exchange offers. Not run; the filer wrote the arms and
  measures out from A's text and added nothing else. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-280 — Proposed or Open; filed from the first share of the same exchange (PR 510) -->
<!-- inactive-ok-file: CLAIM-710 — Proposed or Open; filed from the first share of the same exchange (PR 510) and reconciled with this filing on 2026-11-18 -->
<!-- inactive-ok-file: CLAIM-730 — filed from the exchange "Assess Depp Heard Abuse" on 2026-11-17 -->

# CASE-285: A proposed study: two arrangements whose overseer has the same authority and resources differ only in how fast the acting institution can make its actions irreversible, and precommitted limits, automatic suspension and pauses are added in turn, to tell the value of delay from the value of control over when execution is allowed

## The case

A33 §10 C:

> Construct two arrangements in which the overseer has identical authority
> and resources.
>
> Vary only the speed of the acting institution, with corresponding
> deadlines for preventing irreversible consequences.
>
> Then introduce precommitted constraints, automatic suspension, or
> temporary pauses to determine which can restore effective oversight
> without sacrificing all the benefits of fast execution.

**Arms.** [CASE-003](CASE-003.md)'s two Northstars hold policy and evidence fixed and vary
whether a specialist's objection suspends deployment. Here the overseer's
authority is held fixed, objection suspends in both, and the acting
institution is slow in one arm and fast in the other, with the time before
an action becomes irreversible set accordingly. In the fast arm, three
variants add in turn:

- **precommitted limits** set by the overseer before action (permissions,
  caps, budgets), with escalation for what exceeds them, A33 §8's "slowly
  established rules that constrain action before it happens";
- **automatic suspension** of a class of actions on a flagged objection;
- **temporary pauses** of fixed length before each consequential action.

**Measures.** A23 §10's three: "**intervention capacity**", how often a
consequential action is identified, suspended or redirected before it
becomes irreversible; "**friction distribution**", what initiating,
challenging and correcting cost each party; and what is lost of the fast
arm's benefit under each variant. A23 §3's timing condition, detection plus
evaluation plus intervention within the time before harm, read as a
sequential and deterministic special case, gives the prediction for the
unmodified arms.

**Held fixed.** The overseer's authority, information and resources; the
objection channel; the policy.

## What it can show

A33: "The resulting study could distinguish the value of procedural delay
from the value of *effective control over when execution is allowed*." If
the fast arm loses intervention capacity with authority unchanged,
[CLAIM-462](../claims.d/CLAIM-462.md)'s separation of action from correction holds by timing alone,
and the owner's U11 and U13 (speed as a bound on others' intervention) are
supported in a controlled form. If precommitted limits restore it without
pauses, [CLAIM-730](../claims.d/CLAIM-730.md)'s second clause is supported over its first.

## What it cannot show

Being stipulated, nothing about any real executive, agency or AI system,
and nothing about intent to outrun review, which [CLAIM-464](../claims.d/CLAIM-464.md) leaves aside.
The arms fix authority by construction; real arrangements that act fast
often also hold more authority, which this design removes on purpose.

[CASE-280](CASE-280.md), from the first share of the same exchange, is distinct: a worked
construction in which two organizations alike in rules, rates and initial
corrective capacity differ only in whether their decisions use that
capacity up. It varies endogenous foreclosure at a fixed speed; this
proposed study varies speed at fixed authority and then adds precommitted
limits, suspension and pauses. Both bear on [QUESTION-278](../questions.d/QUESTION-278.md).

## Note of 2026-11-22: carried out by simulation
<!-- inactive-ok-file: CASE-tmp8riid CLAIM-tmpsaql8 — new; the executed study and claim of LEAD-068, filed 2026-11-22 -->

This design was carried out as a queueing model at [LEAD-068](../leads.d/LEAD-068.md)'s request: [CASE-tmp8riid](CASE-tmp8riid.md), with [CLAIM-tmpsaql8](../claims.d/CLAIM-tmpsaql8.md) stating its result. Arms, variants and measures follow this case's text. Two choices it left open were made and stated: "speed" read both as a shorter time to irreversibility alone and as that with proportionally more actions, each reported; and escalations and suspensions share the overseer's reviewers without priority. In the model the fast arm lost intervention capacity with authority unchanged (0.994 to 0.396 at ten times the speed). This case's test of [CLAIM-730](../claims.d/CLAIM-730.md) ("If precommitted limits restore it without pauses") was met, in proportion to what the limits cover. The historical arm is not attempted. No status changes.
