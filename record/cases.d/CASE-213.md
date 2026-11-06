---
number: 213
status: Active
formerly:
- CASE-tmpt6fm7
title: 'Provisional dispatch and cancellation of a specialized rescue resource: a capability is mobilized under uncertainty, then released without performing its specialized task'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings); ADR-057: a construction (ADR-042) whose arithmetic, (A + T)
    − max(A, T) = min(A, T), was re-run by a second checker with python3
    -I, and whose provenance statements about the NFIRS page check against
    NOTE-1573. Standing fictional is kept. It now illustrates CLAIM-559,
    whose body never uses it and from whose grounds it moves; it still
    grounds CLAIM-561.
standing: fictional
kind: construction
tags:
- operations-research
- society-and-governance
- probabilistic-modeling
date: '2026-11-04'
line:
- readiness
illustrates:
- CLAIM-559
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 1 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)". A heavy
  rescue squad is dispatched to a reported collision before the first
  engine has established whether extrication is needed, and is cancelled
  when the engine finds it is not. Waiting costs A + T minutes;
  provisional dispatch costs max(A, T), so it saves min(A, T). A
  constructed case: the USFA page [LIT-2084](../literature.d/LIT-2084.md) is a real-world analogue,
  not its documentation. The case grounds [CLAIM-561](../claims.d/CLAIM-561.md) and
  [CLAIM-559](../claims.d/CLAIM-559.md). The wording is A's; adopting it is the owner's call.
---

# CASE-213: Provisional dispatch and cancellation of a specialized rescue resource: a capability is mobilized under uncertainty, then released without performing its specialized task

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
the reliability of the first unit's assessment. [CLAIM-561](../claims.d/CLAIM-561.md) adds the
costs; [QUESTION-394](../questions.d/QUESTION-394.md) asks how coverage changes them.

**Provenance.** The heavy-rescue example is constructed. A: "The
heavy-rescue example here is our constructed case. The USFA document is a
real-world analogue". The U.S. Fire Administration's NFIRS coding page,
[LIT-2084](../literature.d/LIT-2084.md), has no heavy rescue squad. Its second scenario cancels one
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
states." The dispatch is a provisional commitment ([TERM-109](../terms.d/TERM-109.md)), not an
exercise of the squad's specialized function. [CLAIM-559](../claims.d/CLAIM-559.md) states the
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
- **Anything about the squad's readiness** ([TERM-115](../terms.d/TERM-115.md)): it assumes the
  squad can deploy, and asks only when to send it.

## Note of 2026-11-05: A's resource models and further distinctions

The pasted synthesis on constraint architectures reads this case through FACT: dispatch, staging, cancellation and redeployment rules constrain the squad's immediate freedom so that the specialized response can be produced reliably. A: "A dispatch protocol is therefore not merely a restriction. It is part of the architecture that makes specialized response operationally effective." A limits the analogy itself: "These cannot be represented directly as six-dimensional screw systems." [CLAIM-582](../claims.d/CLAIM-582.md) says what such a constraint can and cannot improve. No status changes.
