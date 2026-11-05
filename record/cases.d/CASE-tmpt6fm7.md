---
status: Proposed
title: 'Provisional dispatch and cancellation of a specialized rescue resource: a capability is mobilized under uncertainty, then released without performing its specialized task'
version: 1
standing: fictional
kind: construction
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-04'
line:
- readiness
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 1 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)". A heavy
  rescue squad is dispatched to a reported collision before the first
  engine has established whether extrication is needed, and is cancelled
  when the engine finds it is not. Waiting costs A + T minutes;
  provisional dispatch costs max(A, T), so it saves min(A, T). A
  constructed case: the USFA page [LIT-tmpnhw2v](../literature.d/LIT-tmpnhw2v.md) is a real-world analogue,
  not its documentation. The case grounds [CLAIM-tmp5rh3v](../claims.d/CLAIM-tmp5rh3v.md) and
  [CLAIM-tmp4pk8d](../claims.d/CLAIM-tmp4pk8d.md). The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp5rh3v CLAIM-tmp4pk8d TERM-tmp5t7y8 TERM-tmpuc919 — Proposed or new; A's proposals of 2026-11-04 and the readings they cite, as open -->
<!-- inactive-ok-file: CLAIM-tmpr4sof — Proposed or new; entries of 2026-11-05 from the pasted synthesis on constraint architectures, cited as open -->

# CASE-tmpt6fm7: Provisional dispatch and cancellation of a specialized rescue resource: a capability is mobilized under uncertainty, then released without performing its specialized task

## The case

**Setting.** Dispatch receives a report of a motor vehicle collision.
With probability p the incident needs specialized extrication. A
first-arriving engine establishes whether it does after A minutes; the
heavy rescue squad needs T minutes to reach the incident.

**Two policies.**
- **Wait**: dispatch the squad only after the first unit has established
  the need.
- **Provisional dispatch**: dispatch the squad at once, and cancel it if
  the first unit finds it unnecessary.

**What is held fixed.** Travel times are fixed, the squad can be
dispatched immediately, and the specialized work cannot begin before both
the assessment and the squad's arrival.

**The arithmetic.** Under waiting, the specialized work can begin at
t_wait = A + T. Under provisional dispatch it can begin at
t_provisional = max(A, T). The saving is

  Δt = (A + T) − max(A, T) = min(A, T),

since A + T = max(A, T) + min(A, T). The lead checked this. In A's words,
"provisional dispatch overlaps information gathering and physical
mobilization."

**What a full version would add**, in A's list: the incremental cost of a
response, the squad's temporary unavailability for other incidents, and
the reliability of the first unit's assessment. [CLAIM-tmp5rh3v](../claims.d/CLAIM-tmp5rh3v.md) adds the
costs; [QUESTION-tmpvweyo](../questions.d/QUESTION-tmpvweyo.md) asks how coverage changes them.

**Provenance.** The heavy-rescue example is constructed. A: "The
heavy-rescue example here is our constructed case. The USFA document is a
real-world analogue". The U.S. Fire Administration's NFIRS coding page,
[LIT-tmpnhw2v](../literature.d/LIT-tmpnhw2v.md), has no heavy rescue squad. Its second scenario cancels one
tanker/tender and one rescue vehicle after the first-arriving engine finds
a false alarm. The page also says that a call a department could not
answer for lack of resources is not an NFIRS incident, so the failures
closest to the value of readiness leave no record there. The page shows
that cancellation en route is ordinary enough to have a coding rule; it
documents nothing about this case.

## What it can show

A's reading: "A resource may be correctly mobilized and correctly
canceled without performing its specialized operation. The two decisions
can both be optimal because they are made under different information
states." The dispatch is a provisional commitment ([TERM-tmp5t7y8](../terms.d/TERM-tmp5t7y8.md)), not an
exercise of the squad's specialized function. [CLAIM-tmp4pk8d](../claims.d/CLAIM-tmp4pk8d.md) states the
two-stage result.

It sits beside the record's other work on deployment under a deadline:
[CLAIM-296](../claims.d/CLAIM-296.md) and [TERM-055](../terms.d/TERM-055.md) separate having a resource from deploying it in
time, and [CLAIM-535](../claims.d/CLAIM-535.md) asks which observations a policy must act on. Here the
policy acts first on a report and then on the first unit's assessment.

## What it cannot show

- **That a high cancellation rate is good.** A: "A high cancellation rate
  is not automatically desirable."
- **That any real department's policy is optimal**, or that any real
  cancellation was appropriate. It is a construction with fixed travel
  times and a perfect assessment.
- **Anything about the squad's readiness** ([TERM-tmpuc919](../terms.d/TERM-tmpuc919.md)): it assumes the
  squad can deploy, and asks only when to send it.

## Note of 2026-11-05: A's resource models and further distinctions

The pasted synthesis on constraint architectures reads this case through FACT: dispatch, staging, cancellation and redeployment rules constrain the squad's immediate freedom so that the specialized response can be produced reliably. A: "A dispatch protocol is therefore not merely a restriction. It is part of the architecture that makes specialized response operationally effective." A limits the analogy itself: "These cannot be represented directly as six-dimensional screw systems." [CLAIM-tmpr4sof](../claims.d/CLAIM-tmpr4sof.md) says what such a constraint can and cannot improve. No status changes.
