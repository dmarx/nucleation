---
status: Proposed
title: 'Google, 11 August 2014: a bug in turndown automation sent every satellite machine to disk erasure; the postmortem the SRE workbook shows as good blameless practice names a staffing limit among what went poorly and assigns its fourteen action items, all technical, to engineers'
version: 1
standing: documented
kind: specimen
tags:
- software-engineering
- society-and-governance
date: '2026-11-22'
line:
- rightful-power
- organizational-normativity
reported_in:
- LIT-tmpujx6j
- NOTE-tmpf58r7
illustrates:
- CLAIM-750
bears_on:
- QUESTION-476
summary: >-
  A real Google postmortem, published in the SRE workbook (2018,
  LIT-tmpujx6j, read in NOTE-tmpf58r7) as the good counterpart of a
  blameful draft. A manual re-run of a decommission workflow triggered a
  validation bug that sent all satellite machines to diskerase. The
  postmortem blames "No individual or team", traces the failure across
  several teams' systems, lists ""The installer" has limited staffing"
  among what went poorly in recovery, and assigns fourteen action items,
  each to an engineer, none about staffing, priorities or budgets. Filed as
  a specimen for CLAIM-750, with an alternative reading in its body and an
  ARG (ARG-tmp117cw). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-750 CLAIM-905 CASE-335 — Proposed; the claim this illustrates and the pilot it parallels -->
<!-- inactive-ok-file: ARG-tmp117cw CLAIM-tmpauu5r — new; the argument for the illustration and the objection filed with it -->

# CASE-tmptkkgm: Google, 11 August 2014: a bug in turndown automation sent every satellite machine to disk erasure; the postmortem the SRE workbook shows as good blameless practice names a staffing limit among what went poorly and assigns its fourteen action items, all technical, to engineers

## The case

From chapter 10 of *The Site Reliability Workbook* (LIT-tmpujx6j, read in
NOTE-tmpf58r7). The chapter says: "This is an actual postmortem. In some
cases, we fictionalized names of individuals and teams."

- **What happened.** "A longstanding input validation bug in the Traffic
  Admin server was triggered by the manual reexecution of a workflow to
  decommission the a12bcd34 satellite. The bug removed the machine
  constraint on the decom action, sending all satellite machines to
  decommission." Satellites carried "typically 60% of global queries";
  latency rose "for nearly two days".
- **Who.** The manual run is attributed to a team: "When the Cluster
  Turnup team manually started another run of the workflow". "No
  individual or team is blamed for the incident."
- **What went poorly.** Missing sanity checks, no rate limit on the decom
  workflow, slow reinstalls, overly strict timeouts, a concurrency
  regression, and ""The installer" has limited staffing. As a result,
  making changes is difficult and slow."
- **Action items.** Fourteen, in five themes, each with a priority, an
  engineer as owner and a bug: audits of destructive systems, input
  rejection, a cap on nodes per operation, approval by a safety-check
  service, an emergency stop, alerts, HTTPS reinstalls, DiRT tests. None
  addresses the installer's staffing, or any priority, deadline or budget.
- **Praised for depth.** "Rather than only investigating the proximate
  area of the system failure, the postmortem explores the impact and
  system flaws across multiple teams."

## What it can show

The reading filed, which the filer leans to:

- **An upstream condition recorded, its repair not routed.** The review
  names a staffing limit as a cause of slow recovery and assigns it no
  action item, while its fourteen action items go to technical fixes. Staffing is set by
  whoever allocates headcount, not by the engineers who own the action
  items. That fits CLAIM-750's prediction that action items "cluster at or
  below the reviewing team's authority", in the exemplar the practice
  itself holds up as good. ARG-tmp117cw sets out the inference.
- **Depth across, not up.** The postmortem's praised depth is lateral,
  "across multiple teams": it reaches peer systems, not the decisions
  that set their conditions.

## The alternative reading

- **Not an upstream decision.** "The installer" may be a peer team, and
  its staffing a matter for its own management, not above the reviewing
  teams' authority. The limit bears on recovery speed, not on the cause of
  the outage, and a reviewer could reasonably judge it outside the
  incident's action plan. On this reading the case shows nothing about
  where the trace stops, and should carry no `illustrates`.
- **Routed elsewhere.** Google's practice puts questions about priorities
  in reviews across incidents (CLAIM-tmpauu5r). The staffing limit may
  have been taken up there, which the chapter does not say.

The filer leans to the first reading, because the staffing limit is the
one contributing condition in the postmortem that no engineer could fix,
and no action item touches it. Which reading holds is the
owner's call; the `illustrates` link stands or falls with it.

## What it cannot show

- One postmortem, chosen as an exemplar, with values redacted and the
  timeline elided. Not a sample.
- What the installer's staffing was, who set it, or whether it changed.
- It parallels CASE-335 and CLAIM-905, the pilot's finding that public
  postmortems' traces stop at the engineering group, but is not in that
  pilot's corpus and adds one more instance, not an independent test.
