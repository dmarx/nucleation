---
number: 705
status: Proposed
formerly:
- CLAIM-tmpfmmkt
title: 'When an institution produces challengeable decisions faster than its corrective process can resolve them, the formal right to challenge stays with everyone while its preventive effect cannot: if valid challenges arrive at rate λ and are resolved at rate μ < λ, at most a share μ/λ can ever be resolved in time, whatever the order of review, and under first-come review none filed after a finite time is'
version: 7
history:
- version: 2
  date: '2026-11-16'
  note: >-
    A dated note added: Hong Kong Monetary Authority (LIT-2696) read on 2026-11-16, NOTE-2018. No change of status or title.
- version: 3
  date: '2026-11-16'
  note: >-
    A dated note added: Citron (LIT-2719) read on 2026-11-16, NOTE-2003. No change of status or title.
- version: 4
  date: '2026-11-16'
  note: >-
    A dated note added: Bovens and Zouridis (LIT-2661) read on 2026-11-16, NOTE-2030. No change of status or title.
- version: 5
  date: '2026-11-16'
  note: >-
    At the second review of 2026-11-16 (ChatGPT's, forwarded by the owner),
    which found the same omission in CLAIM-704: step 3 now says its
    t* = Fμ/(λ − μ) treats review as taking no time, and gives
    t* = (F − s)μ/(λ − μ) for a service time s. The bound and the result are
    unchanged.
- version: 6
  date: '2026-11-18'
  note: >-
    Reconciled with the continuation's filing of the same exchange (PR 512):
    its CLAIM-740 (explanation, contestation and interruption, A23 §6)
    was compared with this entry and judged distinct (this claim derives a
    bound from rates; that one separates three entitlements, of which this
    shows one failure); complements CLAIM-740 added; a sentence on the
    difference added. No change of status or title.
- version: 7
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §10.3, §13.4. No other
    change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation; or a showing that its idealizations carry the
  result, for instance that corrective throughput in real arrangements
  rises with backlog without bound (so μ is not fixed while λ > μ), or that
  challenges not resolved within the window still prevent the harm they
  target, so that resolution after foreclosure is not "too late". Not
  defeated by arrangements with μ ≥ λ, which the claim does not cover.
tags:
- society-and-governance
- operations-research
- philosophy-of-technology
date: '2026-11-15'
line:
- distributed-agency
complements:
- CLAIM-462
- CLAIM-464
- CLAIM-740
uses:
- TERM-085
bears_on:
- QUESTION-279
summary: >-
  A's, from A35 §3 of the exchange "Assess Depp Heard Abuse" (2026-11-15):
  "an action-producing system can exceed the corrective throughput of the
  institutions intended to constrain it", with A's worked numbers (10,000
  decisions a day, 1% needing correction, 50 appeals resolved a day) and its
  analogy to queueing stability. The derivation here makes A's statement
  exact: the backlog grows at λ − μ; whatever the service order, at most
  μ/λ of challenges are ever resolved; and under first-come review every
  challenge filed after t* = Fμ/(λ − μ) is resolved after its window F has
  closed. With A's numbers t* is ten days. Checked by simulation. It is
  [TERM-085](../terms.d/TERM-085.md)'s deadline applied to a stream of cases. The wording is A's; the
  derivation is the filer's; adopting it is the owner's call.
works:
- governance-of-possibility
---
<!-- inactive-ok-file: CLAIM-704 — Proposed or Deferred; filed from the exchange "Assess Depp Heard Abuse" or its readings, cited with its standing -->
<!-- inactive-ok-file: THEORY-1931 — Proposed or Deferred; filed from the exchange "Assess Depp Heard Abuse" or its readings, cited with its standing -->
<!-- inactive-ok-file: CLAIM-711 — filed from the same exchange, Proposed -->

# CLAIM-705: When an institution produces challengeable decisions faster than its corrective process can resolve them, the formal right to challenge stays with everyone while its preventive effect cannot: if valid challenges arrive at rate λ and are resolved at rate μ < λ, at most a share μ/λ can ever be resolved in time, whatever the order of review, and under first-come review none filed after a finite time is

## The claim

A35 §3 of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afa2a8d-2598-83ea-8d1a-d9ceb992a99c):
an agency's automated system makes 10,000 consequential decisions a day,
1% need correction, so 100 valid challenges a day if each is detected and
appealed, and appeals resolve 50 a day. "If some consequences become
irreversible within ten days, the growing backlog may cause the effective
loss of preventive remedies, despite the legal right to appeal remaining
unchanged." And:

> the distinctive point is that **an action-producing system can exceed
> the corrective throughput of the institutions intended to constrain it**.

A called it "analogous to stability conditions in queueing theory".

## The derivation

Valid challenges arrive at a steady rate λ; the corrective process resolves
them at a steady rate μ < λ; a challenge resolved more than F after it is
filed comes after the harm it targets has become irreversible (F is
[TERM-085](../terms.d/TERM-085.md)'s horizon for that challenge).

1. **The backlog is unbounded.** By time T, λT challenges have been filed
   and at most μT resolved, so at least (λ − μ)T wait.
2. **At most μ/λ are ever resolved in time, under any order.** At most μT
   are resolved by T, so at most a share μT/λT = μ/λ of those filed, in
   time or not. The bound does not depend on which challenges are taken
   first.
3. **Under first-come review, the share resolved in time goes to zero.** A
   challenge filed at t finds (λ − μ)t ahead of it and waits (λ − μ)t/μ. It
   is late when that exceeds F, that is, for every t > t* = Fμ/(λ − μ).
   This treats review as taking no time of its own (the fluid limit); with
   a service time s = 1/μ per challenge the latency is s + (λ − μ)t/μ and
   t* = (F − s)μ/(λ − μ) ([CLAIM-704](CLAIM-704.md)).
   Only the challenges filed before t*, a fixed number, are resolved in
   time, so their share of all those filed tends to zero.

With A's numbers (λ = 100, μ = 50, F = 10 days), t* = 10 days in the fluid limit, 9.98 days with s = 0.02. A
day-by-day simulation (`python3 -I`, scratchpad, 2026-11-15) agrees: under
first-come review, every challenge filed from day 11 on is late, and the
share resolved in time falls to 10.5% by day 100 and 1.05% by day 1,000;
serving the newest first keeps it at the bound, 50%, with the oldest
challenges never served.

Throughout, every affected person keeps the same formal right to
challenge. What the rates fix is how many of those rights can prevent
anything.

## Where it sits

- [TERM-085](../terms.d/TERM-085.md), correctability: the chance of
  achieving a corrective objective before its deadline. This claim is that
  chance for a stream of cases when the corrector is congested.
- [CLAIM-462](CLAIM-462.md) (Active): capacity for action can grow while
  capacity to be corrected degrades. Here the degradation is arithmetic: λ
  rises with the speed of action and μ does not.
- [CLAIM-464](CLAIM-464.md) (Active) is about one intervention changing the
  cost of its own correction; this is about many decisions outrunning a
  corrector whose cost per case is unchanged.
- [QUESTION-279](../questions.d/QUESTION-279.md) asks what certifies that
  no remedy is available rather than that procedures failed to deliver one
  before the deadline. Past t*, under first-come review, a remedy exists
  for every case and the arrangement delivers it for none in time.
- [CLAIM-740](CLAIM-740.md), from the continuation of the same exchange (A23 §6):
  explanation, contestation and interruption are separate entitlements,
  and contestation without interruption is a right that arrives too late.
  This claim derives one case of that failure from rates; that one names
  the entitlements. Distinct, and complementary.

## What it does not say

- **That real arrival and service rates are steady.** The bound needs only
  long-run averages; the first-come result needs the backlog to persist.
- **Which order of review is right.** The bound holds for any order.
- **That faster correction is the only response.** A35 names fewer errors,
  more appellate capacity, and suspension; [CLAIM-711](CLAIM-711.md), from the same
  exchange, adds standing constraints that stop decisions before they take
  effect.

## Note of 2026-11-16: Hong Kong Monetary Authority, read

The HKMA states this claim's point qualitatively. "Approval fatigue" leaves
an approval step "formally in place" but no longer effective, which "creates a
practical limit on the speed and volume at which an agent can" operate
safely. Where the rate of actions exceeds reviewers' ability, the formal step
is not to be treated as oversight (§4.4, p. 20; §7.2, p. 37). That is the
formal right staying while its preventive effect does not. The paper gives
no rates or derivation, and A had read it (A23) before stating the claim
(A35), so its independence is partial. Relation: [THEORY-1931](../theory.d/THEORY-1931.md) corroborates
(qualitatively).

## Note of 2026-11-16: Citron, read

Citron supports the picture of rights that remain formally intact while correction comes too late: "It
took the accused man and his attorney over two months" to clear a false child-support match (p. 1273);
"At present, there is no assured way to get removed from the “No" Fly” list (p. 1275); programmers
"delayed fixing incorrect rules for" extended periods (p. 1269). It also qualifies the derivation's
fixed μ. Citron's central point about cost is that correcting code is a fixed cost whose benefit recurs, so
a Mathews analysis of one case "will capture all of the costs of improved process but only a tiny
fraction of its benefits" (p. 1285); one discovered distortion, once fixed, "would avoid errors in
thousands of other cases" (p. 1308). Where errors are systematic, a single correction resolves many
pending challenges at once: corrective throughput is not fixed per case. That is near the claim's stated
defeater and should be recorded as its limit for rule-level errors; the claim stands for errors that must
be corrected case by case (misidentifications, factual errors). Relation: bears_on (qualifies); not
corroborates.

## Note of 2026-11-16: Bovens and Zouridis, read

Only qualitative support: appeals in the automated traffic system are rare ("These cases are, however, far"
and few between, §3.2), and at welfare-state scale case-by-case accountability "is no longer feasible in
each concrete case" (§7). No rates or deadlines. Relation: bears_on, nothing more.
