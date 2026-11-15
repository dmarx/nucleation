---
status: Proposed
title: 'When an institution produces challengeable decisions faster than its corrective process can resolve them, the formal right to challenge stays with everyone while its preventive effect cannot: if valid challenges arrive at rate λ and are resolved at rate μ < λ, at most a share μ/λ can ever be resolved in time, whatever the order of review, and under first-come review none filed after a finite time is'
version: 1
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
  TERM-085's deadline applied to a stream of cases. The wording is A's; the
  derivation is the filer's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpwpvbz — filed from the same exchange, Proposed -->

# CLAIM-tmpfmmkt: When an institution produces challengeable decisions faster than its corrective process can resolve them, the formal right to challenge stays with everyone while its preventive effect cannot: if valid challenges arrive at rate λ and are resolved at rate μ < λ, at most a share μ/λ can ever be resolved in time, whatever the order of review, and under first-come review none filed after a finite time is

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
TERM-085's horizon for that challenge).

1. **The backlog is unbounded.** By time T, λT challenges have been filed
   and at most μT resolved, so at least (λ − μ)T wait.
2. **At most μ/λ are ever resolved in time, under any order.** At most μT
   are resolved by T, so at most a share μT/λT = μ/λ of those filed, in
   time or not. The bound does not depend on which challenges are taken
   first.
3. **Under first-come review, the share resolved in time goes to zero.** A
   challenge filed at t finds (λ − μ)t ahead of it and waits (λ − μ)t/μ. It
   is late when that exceeds F, that is, for every t > t* = Fμ/(λ − μ).
   Only the challenges filed before t*, a fixed number, are resolved in
   time, so their share of all those filed tends to zero.

With A's numbers (λ = 100, μ = 50, F = 10 days), t* = 10 days. A
day-by-day simulation (`python3 -I`, scratchpad, 2026-11-15) agrees: under
first-come review, every challenge filed from day 11 on is late, and the
share resolved in time falls to 10.5% by day 100 and 1.05% by day 1,000;
serving the newest first keeps it at the bound, 50%, with the oldest
challenges never served.

Throughout, every affected person keeps the same formal right to
challenge. What the rates fix is how many of those rights can prevent
anything.

## Where it sits

- TERM-085, correctability: the chance of
  achieving a corrective objective before its deadline. This claim is that
  chance for a stream of cases when the corrector is congested.
- CLAIM-462 (Active): capacity for action can grow while
  capacity to be corrected degrades. Here the degradation is arithmetic: λ
  rises with the speed of action and μ does not.
- CLAIM-464 (Active) is about one intervention changing the
  cost of its own correction; this is about many decisions outrunning a
  corrector whose cost per case is unchanged.
- QUESTION-279 asks what certifies that
  no remedy is available rather than that procedures failed to deliver one
  before the deadline. Past t*, under first-come review, a remedy exists
  for every case and the arrangement delivers it for none in time.

## What it does not say

- **That real arrival and service rates are steady.** The bound needs only
  long-run averages; the first-come result needs the backlog to persist.
- **Which order of review is right.** The bound holds for any order.
- **That faster correction is the only response.** A35 names fewer errors,
  more appellate capacity, and suspension; CLAIM-tmpwpvbz, from the same
  exchange, adds standing constraints that stop decisions before they take
  effect.
